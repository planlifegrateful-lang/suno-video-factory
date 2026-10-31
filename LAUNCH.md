# LAUNCH CHECKLIST — Suno Video Factory

**Goal:** prepare one rights-checked, reviewable video package without publishing automatically.

## 1. Rights preflight
- [ ] Find the exact track/version in PLG Music — Master Song Catalog.
- [ ] Confirm the permitted Suno download and applicable paid plan evidence.
- [ ] Confirm lyrics/source rights and any collaborator permissions.
- [ ] If evidence is missing, keep the work private and do not monetize or distribute.

## 2. CapCut path
- [ ] Open [capcut/EASY-MODE.md](capcut/EASY-MODE.md).
- [ ] Duplicate the master template.
- [ ] Add the approved audio and visual assets.
- [ ] Fix captions and review the full export end-to-end.
- [ ] Save the export as a draft until human approval is recorded.

## 3. Local status checker
```bash
python3 server/sync_server.py
curl http://127.0.0.1:8787/health
curl http://127.0.0.1:8787/sync
```
- [ ] Confirm `/health` returns ok.
- [ ] Read local job blockers from `/sync`.
- [ ] Verify Buffer/YouTube status manually; this server does not query those APIs.

## 4. Job packet
- [ ] Copy `templates/job-manifest.json` into `jobs/YYYY-MM-DD_slug/manifest.json`.
- [ ] Fill brief, script, and platform surfaces.
- [ ] Add stable references to `rights.audio_evidence` and `rights.visuals_evidence`; set each status to `VERIFIED` only after the exact track/version download/plan and visual-source rights are documented.
- [ ] Set status to `approved` only after human review.

## Success criteria
- One rights-checked video exported and reviewed.
- Manifest records exact source, version, rights evidence, and approval.
- No post is published without explicit approval.
