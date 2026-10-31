# Premium AI Video Production System

## Mission

Convert a brief into a reviewable, platform-ready vertical video package:

`idea → script → voice → visuals → captions → timeline → review → export → approved publish`

This repository is the content-operations layer. It defines production contracts, prompts, shot design, edit rules, export profiles, and approval gates. It does not silently publish content or assume rights that have not been verified.

## Content modes

Use the same pipeline contract for UGC ads, motivational reels, faceless voiceover videos, product demos, disclosed AI-avatar videos, music-led videos, and cinematic short-form stories.

## Production contract

Each job lives in a versioned folder:

```text
jobs/{YYYY-MM-DD}_{slug}/
  brief.md
  script.v{n}.md
  voice/
  visuals/
  captions/
  edit/
  review/
  exports/
  manifest.json
```

`manifest.json` must record the job ID, content mode, source assets, rights/provenance status, prompt versions, editor, reviewer, target platforms, and approval status. Never put credentials in the manifest.

## Pipeline stages

1. **Idea intake** — capture audience, promise, evidence, CTA, mode, target platform, and rights status.
2. **Script** — hook in the first two seconds, one clear promise, proof or context, beat-by-beat visual direction, and a single CTA.
3. **Voice** — record or synthesize only with appropriate consent and usage rights; normalize loudness and retain the source file.
4. **Visuals** — create or select a shot list; log asset provenance and required disclosures.
5. **Captions** — generate a reviewable transcript, then style for safe-area readability and silent viewing.
6. **Timeline** — assemble voice, visuals, music, captions, logo, and CTA with deliberate pacing.
7. **Review** — human approval for factual claims, cultural sensitivity, rights, accessibility, brand safety, and final rendering.
8. **Export** — render platform variants from the approved master; do not publish unreviewed drafts.
9. **Content ops** — create platform-specific descriptions and schedule only after approval.

## Approval gates

A job is `approved` only when factual claims are sourced, audio/visual/voice/brand rights are documented, captions are accurate, required AI disclosures are present, the final export has been watched end-to-end, and the manifest records reviewer and approval timestamp.

## Suno rights and local status-service truth gate

- A Suno public page proves that a track is publicly viewable, not that it is commercially cleared.
- Before public or commercial use, record the exact track/version, the applicable plan at creation/download, a permitted Suno download, lyrics/source rights, and any collaborator permissions.
- Keep audio and visual rights separate. Both statuses must be `VERIFIED` and `rights.audio_evidence` plus `rights.visuals_evidence` must each contain at least one stable evidence reference before a job can become `sync_ready`.
- The local publish-sync server binds to loopback and reports channel connections as unverified; it does not call Buffer/YouTube APIs or publish.
- Its Buffer webhook endpoint is not implemented and returns HTTP 501 until signature verification and event persistence exist.
