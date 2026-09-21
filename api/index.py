from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime, timezone

CHANNELS = {
    "youtube": {"name": "Charles", "connected": True, "buffer_id": "67c2266b3b85969eafab2932"},
    "tiktok": {
        "name": "hustleguru46",
        "connected": False,
        "buffer_id": "67bf7c323b85969eafc45670",
        "blocker": "Buffer disconnected",
    },
}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps(
            {
                "service": "plg-publish-sync",
                "time": datetime.now(timezone.utc).isoformat(),
                "channels": CHANNELS,
                "next_human_action": "Reconnect Buffer TikTok hustleguru46",
                "jobs_note": "Full job scan runs on python3 server/sync_server.py locally",
                "routes_local": ["/health", "/channels", "/jobs", "/sync"],
            }
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)
