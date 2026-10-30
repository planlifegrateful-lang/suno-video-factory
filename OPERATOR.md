# OPERATOR RUNBOOK — Suno Video Factory

## Daily loop
1. Select an existing Suno track and exact version.
2. Check its existing PLG Music — Master Song Catalog record.
3. Verify commercial-use/download evidence before public or commercial use.
4. Prepare a private CapCut draft using EASY-MODE.
5. Human-review the complete export; only then mark the job approved.
6. Check `GET /sync` for local job blockers.

## Server commands

```bash
python3 server/sync_server.py
curl -s http://127.0.0.1:8787/sync | jq
curl -s http://127.0.0.1:8787/channels | jq
curl -s http://127.0.0.1:8787/jobs | jq
```

## Channel connection uncertainty
1. Check the channel directly in Buffer or the platform's own dashboard.
2. Do not edit a local boolean to claim it is connected; this server does not call provider APIs.
3. Keep the server state unverified until an authenticated integration can verify the connection and record its evidence.

## Rights gate
Never set status to `approved` unless both `rights.audio` and `rights.visuals` are explicitly `VERIFIED`. A public Suno page, a current subscription, or a profile count is not commercial-use evidence. Record the permitted download and the plan active at download time before monetizing.

## What this system does NOT do
- Does not download Suno audio.
- Does not run CapCut headlessly.
- Does not upload or schedule posts.
- Does not query Buffer/YouTube connection APIs.
- Does not invent rights, testimonials, or metrics.

## Metrics
Track exported videos, approved jobs, published posts, rights evidence, clicks, and actual revenue separately. Do not treat profile counters as revenue.
