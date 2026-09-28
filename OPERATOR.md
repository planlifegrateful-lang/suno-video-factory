# OPERATOR RUNBOOK – Suno Video Factory

## Daily loop
1. Pull or select new Suno track from @planlifegrateful
2. Run CapCut EASY-MODE (7 min)
3. Export → upload / Buffer queue
4. Update job manifest status after review
5. Check `GET /sync` for blockers

## Server commands
```bash
python3 server/sync_server.py
curl -s http://127.0.0.1:8787/sync | jq
curl -s http://127.0.0.1:8787/channels | jq
curl -s http://127.0.0.1:8787/jobs | jq
```

## When TikTok is disconnected
1. Open Buffer → reconnect hustleguru46
2. Update `CHANNELS["tiktok"]["connected"] = True` in `server/sync_server.py` (or make it env-driven later)
3. Restart server → GET /sync should clear the blocker

## Rights gate
Never set status to `approved` while any rights field is `NEEDS_REVIEW`.

## What this system does NOT do
- Does not download Suno audio for you
- Does not run CapCut headlessly
- Does not upload or schedule posts (Buffer + human do that)
- Does not invent testimonials or metrics

## Metrics
| Metric | Target |
|--------|--------|
| Videos exported / day | ≥3 |
| Posts live / day | ≥3 |
| Jobs with blockers | 0 after reconnect |
