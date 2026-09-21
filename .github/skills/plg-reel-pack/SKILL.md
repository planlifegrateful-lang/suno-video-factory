---
name: plg-reel-pack
description: 'Build a complete Plan Life Grateful reel pack from one Suno track. Use for UGC scripts, on-screen text, CapCut steps, captions, hashtags, thumbnails, TikTok Reels Shorts.'
argument-hint: '[track title] [theme] [platform]'
---

# PLG Reel Pack

## When to use
User asks for a reel, UGC script, hook pack, CapCut steps, caption, or thumbnail for a Suno track.

## Inputs (use defaults if missing)
- track title — default: Untitled PLG track
- theme — 2 lines
- platform — TikTok / Shorts / Reels (default Reels)
- length — 15–22s audio inside a 30s cap

## Procedure
1. Read AGENTS.md, [brand voice](../plg-brand-voice/SKILL.md), capcut/EASY-MODE.md, ugc-scripts/hook-scripts.md.
2. Create `ugc-scripts/packs/{slug}.md` from [pack template](./assets/pack-template.md).
3. Optionally create `prompts/packs/{slug}-visual.md` from [visual template](./assets/visual-template.md).
4. Add one README Quick Links row if this is a new user-facing pack.
5. Stop. Do not edit EASY-MODE unless the issue demands it.

## Required sections in the pack
1. 5 hooks under 8 words
2. On-screen timeline: 0–3s, 3–8s, 8–15s, last 3s CTA
3. Spoken UGC script (hook / body / CTA) matching existing hook-scripts tone
4. Caption + max 8 hashtags + 1 CTA
5. CapCut steps that only point at EASY-MODE + existing presets
6. Thumbnail text max 4 words
7. Rights line: audio = Suno track owned/licensed by creator; visuals = NEEDS_REVIEW unless specified

## Quality bar
- First frame readable with sound off
- One promise, one CTA
- No new CapCut tools
- Brand voice skill applied to every line
