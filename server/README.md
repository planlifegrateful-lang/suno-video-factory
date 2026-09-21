# Publish-sync server

Keeps YouTube, TikTok, and job packets on one status plane.
It does **not** upload videos. It tells you what is connected and what is blocking a sync publish.

```bash
python3 server/sync_server.py
# http://127.0.0.1:8787/sync
```

| Route | Meaning |
|---|---|
| GET /health | liveness |
| GET /channels | Charles + hustleguru46 + YT Music |
| GET /jobs | every folder under jobs/ |
| GET /jobs/{id} | one job + blockers |
| GET /sync | ready count + next human action |
| POST /webhooks/buffer | accept Buffer callbacks (log only) |

`sync_ready` is true only when:
- manifest.status is `approved` or `ready`
- youtube.md and tiktok.md exist
- rights are not NEEDS_REVIEW
- Buffer YouTube **and** TikTok are connected

Right now TikTok Buffer is disconnected, so no job is sync_ready. Reconnect hustleguru46, then GET /sync again.
