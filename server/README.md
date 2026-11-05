# Publish-sync status server

This is a **local-only status checker**, not a publishing integration.

```bash
python3 server/sync_server.py
curl http://127.0.0.1:8787/health
curl http://127.0.0.1:8787/sync
```

The server binds to `127.0.0.1` only. It sends no wildcard CORS headers and does not accept remote/LAN connections. Do not put it behind a public reverse proxy.

| Route | Meaning |
|---|---|
| GET /health | local process liveness |
| GET /channels | configured channel labels; connection state is **unverified** |
| GET /jobs | job folders, manifest state, rights and blockers |
| GET /jobs/{id} | one job and blockers |
| GET /sync | counts and next human action |

There is no live Buffer, TikTok, or YouTube API call. The server does not upload, schedule, or prove that an account is connected.

A job is `sync_ready` only when:
- manifest status is `approved` or `ready`;
- `rights.audio` and `rights.visuals` are explicitly `VERIFIED`;
- `youtube.md` and `tiktok.md` exist; and
- both channel states are verified by a future authenticated provider integration.

At present, channel states are `unverified`, so the server will not mark a job sync-ready.

`POST /webhooks/buffer` returns HTTP 501. No signature verification or event persistence is implemented; do not configure this placeholder as a Buffer webhook.
