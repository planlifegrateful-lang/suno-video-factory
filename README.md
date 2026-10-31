# Suno Video Factory v1.0.0

**Turn a rights-checked Suno track into a reviewable short-form video package.**  
Built for **Plan Life Grateful**.

[![CI](https://github.com/planlifegrateful-lang/suno-video-factory/actions/workflows/ci.yml/badge.svg)](https://github.com/planlifegrateful-lang/suno-video-factory/actions)
[![Version](https://img.shields.io/badge/version-1.0.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Start here

- [CapCut EASY MODE](capcut/EASY-MODE.md)
- [Launch checklist](LAUNCH.md)
- [Operator runbook](OPERATOR.md)
- [Production contract](PRODUCTION_SYSTEM.md)
- [Publish-sync server](server/README.md)
- [14-day content plan](content-calendar/14-day-plan.md)
- [Job manifest template](templates/job-manifest.json)

## How this works

1. Select an existing Suno track and exact version.
2. Verify its commercial-use/download evidence in the existing PLG Music — Master Song Catalog.
3. Prepare the CapCut draft from the existing template.
4. Human-review audio, visuals, lyrics, rights, disclosures, and export.
5. Publish only after the required rights and human approval are recorded.

## Publish-sync server

Run the local status checker:

```bash
python3 server/sync_server.py
curl http://127.0.0.1:8787/health
curl http://127.0.0.1:8787/sync
```

**Truth and security limits:** it binds to `127.0.0.1` only, sends no wildcard CORS headers, does not query Buffer/YouTube APIs, and does not upload or schedule. All channel states are **unverified** until an authenticated integration exists. `POST /webhooks/buffer` returns HTTP 501 because signature verification and event persistence are not implemented. Do not configure it as a live webhook.

## Environment

Copy `.env.example` to `.env`. The current standard-library status server uses only `PORT`; its bind address is fixed to loopback. Do not add provider secrets to this repo.

## Known limitations

- CapCut editing is manual; there is no headless CapCut API here.
- Suno catalog access, downloads, and plan evidence are outside this repo.
- The status server is local-only and does not verify channel connectivity.
- The server never posts; human approval and the platform's own publishing tools remain required.
- Each job must set `rights.audio` and `rights.visuals` to `VERIFIED` and include at least one stable reference in each matching `*_evidence` array. For audio, record the exact Suno track/version, permitted downloaded file, plan/tier, and download date; for visuals, record the source, license, or permission. A status flag alone is not evidence.

**Suno:** [@planlifegrateful](https://suno.com/@planlifegrateful)  
**Repo:** https://github.com/planlifegrateful-lang/suno-video-factory

MIT License — see LICENSE.
