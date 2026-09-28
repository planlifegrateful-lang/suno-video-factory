# LAUNCH CHECKLIST – Suno Video Factory

**Goal:** First video exported and queued within 1 hour using EASY-MODE.

## 1. CapCut path (fastest revenue content)
- [ ] Open [capcut/EASY-MODE.md](capcut/EASY-MODE.md)
- [ ] Duplicate master template
- [ ] Drop latest Suno track + background
- [ ] Paste text from [capcut/QUICK-TEXT.md](capcut/QUICK-TEXT.md)
- [ ] Export 9:16 MP4
- [ ] Upload to YouTube Shorts + TikTok (or Buffer)

## 2. Publish-sync server (status plane)
```bash
cd server
python3 sync_server.py
# or: PORT=8787 python3 sync_server.py
curl http://127.0.0.1:8787/health
curl http://127.0.0.1:8787/sync
```
- [ ] Confirm `/health` returns ok
- [ ] Read `next_human_action` from `/sync`
- [ ] Reconnect Buffer TikTok (hustleguru46) if disconnected

## 3. Job packet
- [ ] Copy `templates/job-manifest.json` into a new folder under `jobs/YYYY-MM-DD_slug/`
- [ ] Fill brief.md, script, youtube.md, tiktok.md
- [ ] Set manifest status to `approved` only after human review

## 4. Content calendar
- [ ] Open [content-calendar/14-day-plan.md](content-calendar/14-day-plan.md)
- [ ] Schedule next 3 posts today

## Success criteria (Day 1)
- At least 1 exported video posted
- Sync server running and reporting channel status
- One job folder with complete surfaces
