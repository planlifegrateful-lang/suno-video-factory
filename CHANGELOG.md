# Changelog

## [1.0.0] – 2026-09-28

### Production package
- Complete CapCut EASY-MODE + QUICK-TEXT + full template system
- Publish-sync server (stdlib only) with /health /channels /jobs /sync
- Job folder contract + manifest template
- Content calendars (14-day + 7-day)
- UGC scripts + prompts + production system docs
- Copilot agents + skills under .github/
- LICENSE, LAUNCH.md, OPERATOR.md, .env.example, CI workflow
- Explicit documentation that the server does **not** upload videos

### Known limitations
- TikTok Buffer channel currently marked disconnected in CHANNELS config (reconnect in Buffer)
- Server never posts; human + Buffer still required for actual publish
- CapCut is a manual/desktop workflow (no headless CapCut API in this repo)
- Suno track download and rights verification are operator responsibility
