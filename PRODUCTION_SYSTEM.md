# Premium AI Video Production System

## Mission

Convert a brief into a reviewable, platform-ready vertical video package:

`idea → script → voice → visuals → captions → timeline → review → export → approved publish`

This repository is the content-operations layer. It defines production contracts, prompts, shot design, edit rules, export profiles, and approval gates. It does not silently publish content or assume rights that have not been verified.

## Content modes

Use the same pipeline contract for:

- UGC ads
- motivational reels
- faceless voiceover videos
- product demos
- disclosed AI-avatar videos
- music-led videos
- cinematic short-form stories

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

## Premium creative rules

- Open with the strongest truthful hook; do not use bait-and-switch claims.
- Make the first frame understandable without audio.
- Keep one visual idea per beat and cut on meaning or rhythm.
- Use a readable text hierarchy: hook, supporting phrase, CTA.
- Keep subtitles inside platform safe areas and validate contrast.
- Use music to support the voice, not bury it.
- End with a specific, low-friction CTA.
- Create platform variants from one approved source timeline; never resize blindly.

## Approval gates

A job is `approved` only when:

- factual claims are sourced or clearly framed as opinion;
- all audio, visual, voice, and brand assets have a rights/provenance record;
- captions are accurate and readable;
- AI-generated or synthetic media is disclosed when required;
- the final export has been watched end-to-end;
- the manifest records reviewer and approval timestamp.

## No hallucination policy

The system must label unknowns as `NEEDS_REVIEW`. It must not invent testimonials, product results, citations, rights, customer stories, or performance metrics. Generation creates drafts; human review creates publishable work.
