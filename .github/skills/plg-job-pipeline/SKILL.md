---
name: plg-job-pipeline
description: 'Create or advance a versioned production job folder from idea to approved export. Use for jobs/, manifest.json, briefs, scripts, review gates, PRODUCTION_SYSTEM.'
argument-hint: '[slug] [mode]'
---

# PLG Job Pipeline

## When to use
User mentions a job, brief, production run, approval, export package, or PRODUCTION_SYSTEM.

## Procedure
1. Read PRODUCTION_SYSTEM.md and workflow/production-runbook.md.
2. Create or update `jobs/{YYYY-MM-DD}_{slug}/` with:
   - brief.md
   - script.v1.md
   - manifest.json from [manifest template](./assets/manifest-template.json)
   - empty folders noted in brief: voice/, visuals/, captions/, edit/, review/, exports/
3. Fill brief using [brief template](./assets/brief-template.md).
4. Status starts as `draft`. Only a human sets `approved`.
5. Never put credentials in the manifest.
6. Never publish.

## Modes
UGC ads | motivational reels | faceless VO | product demos | disclosed AI-avatar | music-led | cinematic short-form

## Gate
If rights, claims, or disclosures are unknown → `NEEDS_REVIEW` in manifest and review/notes.md.
