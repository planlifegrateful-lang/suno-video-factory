#!/usr/bin/env python3
"""Plan Life Grateful publish-sync server.

Source of truth for jobs across CapCut / YouTube / TikTok.
Does not post. It reports what is connected and what each job still needs.

  python3 server/sync_server.py
  curl http://127.0.0.1:8787/health
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
JOBS = ROOT / "jobs"
PORT = int(os.environ.get("PORT", "8787"))

CHANNELS = {
    "youtube": {
        "name": "Charles",
        "buffer_id": "67c2266b3b85969eafab2932",
        "connected": True,
        "studio": "https://studio.youtube.com",
    },
    "tiktok": {
        "name": "hustleguru46",
        "buffer_id": "67bf7c323b85969eafc45670",
        "connected": False,
        "studio": "https://www.tiktok.com/studio",
        "blocker": "Buffer channel disconnected — reconnect before auto-queue",
    },
    "youtube_music": {
        "name": "distributor",
        "connected": False,
        "blocker": "Official catalog requires DistroKid/TuneCore packet, not an upload",
    },
}


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_jobs() -> list[dict]:
    items = []
    if not JOBS.exists():
        return items
    for folder in sorted(JOBS.iterdir()):
        if not folder.is_dir():
            continue
        manifest_path = folder / "manifest.json"
        manifest = {}
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text())
        surfaces = {
            "youtube": (folder / "youtube.md").exists(),
            "tiktok": (folder / "tiktok.md").exists(),
            "brief": (folder / "brief.md").exists(),
        }
        ready = all(
            [
                surfaces["youtube"],
                surfaces["tiktok"],
                manifest.get("status") in {"approved", "ready"},
                CHANNELS["youtube"]["connected"],
                CHANNELS["tiktok"]["connected"],
            ]
        )
        items.append(
            {
                "job_id": folder.name,
                "status": manifest.get("status", "unknown"),
                "platforms": manifest.get("platforms", []),
                "rights": manifest.get("rights", {}),
                "surfaces": surfaces,
                "sync_ready": ready,
                "blockers": blockers_for(manifest, surfaces),
            }
        )
    return items


def blockers_for(manifest: dict, surfaces: dict) -> list[str]:
    out = []
    if manifest.get("status") not in {"approved", "ready"}:
        out.append("job not approved")
    for key in ("audio", "visuals"):
        if manifest.get("rights", {}).get(key) == "NEEDS_REVIEW":
            out.append(f"rights.{key} NEEDS_REVIEW")
    if not surfaces.get("youtube"):
        out.append("missing youtube.md")
    if not surfaces.get("tiktok"):
        out.append("missing tiktok.md")
    if not CHANNELS["tiktok"]["connected"]:
        out.append("tiktok buffer disconnected")
    return out


def job_by_id(job_id: str) -> dict | None:
    for job in load_jobs():
        if job["job_id"] == job_id:
            return job
    return None


class Handler(BaseHTTPRequestHandler):
    server_version = "plg-sync/1.0"

    def log_message(self, fmt: str, *args) -> None:
        print(f"[{utcnow()}] {self.address_string()} {fmt % args}")

    def _send(self, code: int, payload: dict) -> None:
        body = json.dumps(payload, indent=2).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:
        path = urlparse(self.path).path.rstrip("/") or "/"
        if path == "/health":
            return self._send(200, {"ok": True, "service": "plg-publish-sync", "time": utcnow()})
        if path == "/channels":
            return self._send(200, {"channels": CHANNELS, "time": utcnow()})
        if path == "/jobs":
            jobs = load_jobs()
            return self._send(200, {"count": len(jobs), "jobs": jobs, "time": utcnow()})
        if path.startswith("/jobs/"):
            job = job_by_id(path.split("/", 2)[-1])
            if not job:
                return self._send(404, {"error": "job not found"})
            return self._send(200, job)
        if path == "/sync":
            jobs = load_jobs()
            return self._send(
                200,
                {
                    "youtube_connected": CHANNELS["youtube"]["connected"],
                    "tiktok_connected": CHANNELS["tiktok"]["connected"],
                    "jobs_total": len(jobs),
                    "jobs_sync_ready": sum(1 for j in jobs if j["sync_ready"]),
                    "jobs": jobs,
                    "next_human_action": (
                        "Reconnect Buffer TikTok hustleguru46"
                        if not CHANNELS["tiktok"]["connected"]
                        else "Approve a job and provide a public MP4 URL"
                    ),
                    "time": utcnow(),
                },
            )
        return self._send(
            200,
            {
                "service": "plg-publish-sync",
                "routes": ["/health", "/channels", "/jobs", "/jobs/{id}", "/sync", "POST /webhooks/buffer"],
            },
        )

    def do_POST(self) -> None:
        path = urlparse(self.path).path.rstrip("/") or "/"
        length = int(self.headers.get("Content-Length", "0") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw or b"{}")
        except json.JSONDecodeError:
            return self._send(400, {"error": "invalid json"})
        if path == "/webhooks/buffer":
            return self._send(
                200,
                {"accepted": True, "note": "logged only — posting stays in Buffer after human approve", "payload_keys": list(data)},
            )
        if path.startswith("/jobs/") and path.endswith("/status"):
            return self._send(400, {"error": "status writes live in git jobs/*/manifest.json — not here"})
        return self._send(404, {"error": "unknown route"})


def main() -> None:
    httpd = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"plg-publish-sync on http://0.0.0.0:{PORT}")
    print("GET /sync")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
