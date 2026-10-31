#!/usr/bin/env python3
"""Local-only PLG publish-sync status server; no provider API or publishing."""
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
HOST = "127.0.0.1"

CHANNELS = {
    "youtube": {"name": "Charles", "buffer_id": "67c2266b3b85969eafab2932", "connection_state": "unverified", "status_source": "not checked by this server", "studio": "https://studio.youtube.com"},
    "tiktok": {"name": "hustleguru46", "buffer_id": "67bf7c323b85969eafc45670", "connection_state": "unverified", "status_source": "not checked by this server", "studio": "https://www.tiktok.com/studio"},
    "youtube_music": {"name": "distributor", "connection_state": "unverified", "status_source": "not checked by this server", "blocker": "Official catalog requires a distributor packet; this server does not upload music"},
}


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def blockers_for(manifest: dict, surfaces: dict) -> list[str]:
    out = []
    if manifest.get("status") not in {"approved", "ready"}:
        out.append("job not approved")
    rights = manifest.get("rights")
    if not isinstance(rights, dict):
        rights = {}
    for key in ("audio", "visuals"):
        if rights.get(key) != "VERIFIED":
            out.append(f"rights.{key} not VERIFIED")
        evidence = rights.get(f"{key}_evidence")
        if not isinstance(evidence, list) or not any(
            isinstance(item, str) and item.strip() for item in evidence
        ):
            out.append(f"rights.{key}_evidence missing")
    if not surfaces.get("youtube"):
        out.append("missing youtube.md")
    if not surfaces.get("tiktok"):
        out.append("missing tiktok.md")
    for channel in ("youtube", "tiktok"):
        if CHANNELS[channel].get("connection_state") != "verified_connected":
            out.append(f"{channel} connection not verified by this server")
    return out


def load_jobs() -> list[dict]:
    items = []
    if not JOBS.exists():
        return items
    for folder in sorted(JOBS.iterdir()):
        if not folder.is_dir():
            continue
        manifest_path = folder / "manifest.json"
        manifest: dict = {}
        manifest_error = None
        if not manifest_path.exists():
            manifest_error = "manifest.json missing"
        else:
            try:
                loaded = json.loads(manifest_path.read_text(encoding="utf-8"))
                if isinstance(loaded, dict):
                    manifest = loaded
                else:
                    manifest_error = "manifest.json must contain a JSON object"
            except (OSError, json.JSONDecodeError):
                manifest_error = "manifest.json is unreadable or invalid JSON"
        surfaces = {
            "youtube": (folder / "youtube.md").is_file(),
            "tiktok": (folder / "tiktok.md").is_file(),
            "brief": (folder / "brief.md").is_file(),
        }
        blockers = blockers_for(manifest, surfaces)
        if manifest_error:
            blockers.insert(0, manifest_error)
        items.append({
            "job_id": folder.name,
            "status": manifest.get("status", "blocked" if manifest_error else "unknown"),
            "platforms": manifest.get("target_platforms", manifest.get("platforms", [])),
            "rights": manifest.get("rights", {}),
            "surfaces": surfaces,
            "manifest_error": manifest_error,
            "sync_ready": not blockers,
            "blockers": blockers,
        })
    return items


def job_by_id(job_id: str) -> dict | None:
    for job in load_jobs():
        if job["job_id"] == job_id:
            return job
    return None


class Handler(BaseHTTPRequestHandler):
    server_version = "plg-sync/1.1"
    sys_version = ""

    def log_message(self, fmt: str, *args) -> None:
        print(f"[{utcnow()}] {self.address_string()} {self.command} {urlparse(self.path).path}")

    def _send(self, code: int, payload: dict) -> None:
        body = json.dumps(payload, indent=2).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self) -> None:
        self.send_response(405)
        self.send_header("Allow", "GET")
        self.end_headers()

    def do_GET(self) -> None:
        path = urlparse(self.path).path.rstrip("/") or "/"
        if path == "/health":
            return self._send(200, {"ok": True, "service": "plg-publish-sync", "time": utcnow()})
        if path == "/channels":
            return self._send(200, {"channels": CHANNELS, "note": "Connection states are unverified; this server does not call Buffer or YouTube APIs.", "time": utcnow()})
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
            return self._send(200, {
                "youtube_connection_state": CHANNELS["youtube"]["connection_state"],
                "tiktok_connection_state": CHANNELS["tiktok"]["connection_state"],
                "jobs_total": len(jobs),
                "jobs_sync_ready": sum(1 for job in jobs if job["sync_ready"]),
                "jobs": jobs,
                "next_human_action": "Verify YouTube and TikTok status in their dashboards; this server does not query provider APIs or upload.",
                "time": utcnow(),
            })
        return self._send(200, {"service": "plg-publish-sync", "routes": ["/health", "/channels", "/jobs", "/jobs/{id}", "/sync"]})

    def do_POST(self) -> None:
        path = urlparse(self.path).path.rstrip("/") or "/"
        if path == "/webhooks/buffer":
            return self._send(501, {"error": "webhook_not_implemented", "message": "No signature verification or event persistence exists; this endpoint does not accept Buffer callbacks."})
        if path.startswith("/jobs/") and path.endswith("/status"):
            return self._send(405, {"error": "status writes are not supported by this server"})
        return self._send(404, {"error": "unknown route"})


def main() -> None:
    httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"plg-publish-sync on http://{HOST}:{PORT} (loopback only)")
    print("GET /sync")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
