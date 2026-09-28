# Suno Video Factory v1.0.0

**Turn any Suno track into ready-to-post Reels in minutes.**  
Built for **Plan Life Grateful**.

[![CI](https://github.com/planlifegrateful-lang/suno-video-factory/actions/workflows/ci.yml/badge.svg)](https://github.com/planlifegrateful-lang/suno-video-factory/actions)
[![Version](https://img.shields.io/badge/version-1.0.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## START HERE (Easiest Way)

### → [capcut/EASY-MODE.md](capcut/EASY-MODE.md)

7-minute system. Zero decisions. Then open **[LAUNCH.md](LAUNCH.md)**.

---

## Quick Links

| What you need | File |
|---------------|------|
| **Make a Reel right now** | [EASY-MODE.md](capcut/EASY-MODE.md) |
| Copy-paste text only | [QUICK-TEXT.md](capcut/QUICK-TEXT.md) |
| Launch checklist | [LAUNCH.md](LAUNCH.md) |
| Operator runbook | [OPERATOR.md](OPERATOR.md) |
| Full production contract | [PRODUCTION_SYSTEM.md](PRODUCTION_SYSTEM.md) |
| Publish-sync server | [server/README.md](server/README.md) |
| 14-day posting plan | [content-calendar/14-day-plan.md](content-calendar/14-day-plan.md) |
| UGC talking scripts | [ugc-scripts/hook-scripts.md](ugc-scripts/hook-scripts.md) |
| Job template | [templates/job-manifest.json](templates/job-manifest.json) |

---

## How This Works

1. Open **EASY-MODE.md**
2. Duplicate CapCut master template
3. Drop Suno audio + background video
4. Add text from the cheat sheet
5. Export and post (or queue via Buffer)
6. Track status with the publish-sync server

---

## Publish-sync server

```bash
python3 server/sync_server.py
curl http://127.0.0.1:8787/sync
```

**Important:** The server does **not** upload videos. It reports channel connectivity and job blockers. Human + Buffer perform the actual publish.

Current known blocker (as of last commit): TikTok Buffer for hustleguru46 is marked disconnected. Reconnect in Buffer, then update the CHANNELS flag if needed.

---

## Environment

Copy `.env.example` → `.env`. Only `PORT` is used by the current stdlib server.

---

## Known limitations (honest)

- CapCut workflow is manual (no headless CapCut API)
- Server never posts; Buffer + human approval required
- Rights/provenance must be set by the operator
- Suno downloads and platform account connections are outside this repo

---

**Suno:** [suno.com/@planlifegrateful](https://suno.com/@planlifegrateful)  
**Repo:** https://github.com/planlifegrateful-lang/suno-video-factory

MIT License – see LICENSE.
