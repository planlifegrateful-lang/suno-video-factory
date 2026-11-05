import json
import tempfile
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from unittest.mock import patch
import server.sync_server as sync_server


class SyncServerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.jobs = Path(self.temp.name)
        self.patch = patch.object(sync_server, "JOBS", self.jobs)
        self.patch.start()

    def tearDown(self):
        self.patch.stop()
        self.temp.cleanup()

    def make_job(self, manifest):
        folder = self.jobs / "2026-10-30-test"
        folder.mkdir()
        (folder / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        (folder / "youtube.md").write_text("draft", encoding="utf-8")
        (folder / "tiktok.md").write_text("draft", encoding="utf-8")
        return folder

    def test_default_bind_is_loopback(self):
        self.assertEqual(sync_server.HOST, "127.0.0.1")

    def test_channel_state_is_unverified(self):
        self.assertEqual(sync_server.CHANNELS["youtube"]["connection_state"], "unverified")
        self.assertEqual(sync_server.CHANNELS["tiktok"]["connection_state"], "unverified")
        self.assertNotIn("connected", sync_server.CHANNELS["youtube"])

    def test_job_requires_verified_rights_and_channel_state(self):
        self.make_job({"status":"approved","target_platforms":["youtube_shorts","tiktok"],"rights":{"audio":"VERIFIED","audio_evidence":["catalog://track-001/download-record"],"visuals":"VERIFIED","visuals_evidence":["library://asset-001/license-record"],"remix":"NOT_A_REMIX"}})
        job = sync_server.load_jobs()[0]
        self.assertFalse(job["sync_ready"])
        self.assertIn("youtube connection not verified by this server", job["blockers"])
        self.assertIn("tiktok connection not verified by this server", job["blockers"])

    def test_missing_rights_evidence_blocks_job(self):
        self.make_job({"status":"approved"})
        job = sync_server.load_jobs()[0]
        self.assertIn("rights.audio not VERIFIED", job["blockers"])
        self.assertIn("rights.visuals not VERIFIED", job["blockers"])
        self.assertIn("rights.audio_evidence missing", job["blockers"])
        self.assertIn("rights.visuals_evidence missing", job["blockers"])
        self.assertIn("rights.remix must be NOT_A_REMIX for commercial sync", job["blockers"])

    def test_verified_rights_without_evidence_references_remain_blocked(self):
        self.make_job({"status":"approved","rights":{"audio":"VERIFIED","audio_evidence":[],"visuals":"VERIFIED","visuals_evidence":["  "],"remix":"NOT_A_REMIX"}})
        job = sync_server.load_jobs()[0]
        self.assertIn("rights.audio_evidence missing", job["blockers"])
        self.assertIn("rights.visuals_evidence missing", job["blockers"])
        self.assertFalse(job["sync_ready"])

    def test_remix_output_never_passes_commercial_sync_gate(self):
        self.make_job({"status":"approved","rights":{"audio":"VERIFIED","audio_evidence":["catalog://track/download"],"visuals":"VERIFIED","visuals_evidence":["library://asset/license"],"remix":"REMIX"}})
        job = sync_server.load_jobs()[0]
        self.assertIn("rights.remix must be NOT_A_REMIX for commercial sync", job["blockers"])
        self.assertFalse(job["sync_ready"])
    def test_malformed_manifest_is_reported_without_crashing(self):
        folder = self.make_job({"status":"draft"})
        (folder / "manifest.json").write_text("{bad json", encoding="utf-8")
        job = sync_server.load_jobs()[0]
        self.assertEqual(job["status"], "blocked")
        self.assertIn("manifest.json is unreadable or invalid JSON", job["blockers"])

    def test_template_is_valid_json_and_has_nested_rights(self):
        template = Path(__file__).resolve().parents[1] / "templates" / "job-manifest.json"
        manifest = json.loads(template.read_text(encoding="utf-8"))
        self.assertEqual(manifest["rights"]["audio"], "NEEDS_REVIEW")
        self.assertEqual(manifest["rights"]["visuals"], "NEEDS_REVIEW")
        self.assertEqual(manifest["rights"]["audio_evidence"], [])
        self.assertEqual(manifest["rights"]["visuals_evidence"], [])
        self.assertEqual(manifest["target_platforms"], ["youtube_shorts", "tiktok"])


class HttpSafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), sync_server.Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def test_health_has_no_wildcard_cors(self):
        with urlopen(f"{self.base}/health", timeout=2) as response:
            self.assertEqual(response.status, 200)
            self.assertNotIn("Access-Control-Allow-Origin", response.headers)

    def test_buffer_webhook_returns_501_not_fake_acceptance(self):
        request = Request(f"{self.base}/webhooks/buffer", data=b'{"event":"sentinel"}', headers={"Content-Type":"application/json"}, method="POST")
        with self.assertRaises(HTTPError) as error:
            urlopen(request, timeout=2)
        self.assertEqual(error.exception.code, 501)
        body = json.loads(error.exception.read())
        self.assertEqual(body["error"], "webhook_not_implemented")
        self.assertNotIn("accepted", body)

    def test_options_does_not_enable_cors(self):
        request = Request(f"{self.base}/health", method="OPTIONS")
        with self.assertRaises(HTTPError) as error:
            urlopen(request, timeout=2)
        self.assertEqual(error.exception.code, 405)
        self.assertNotIn("Access-Control-Allow-Origin", error.exception.headers)


if __name__ == "__main__":
    unittest.main()
