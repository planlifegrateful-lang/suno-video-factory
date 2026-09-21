# Suno audio tools — factory map

Account: [suno.com/@planlifegrateful](https://suno.com/@planlifegrateful)
Official help: https://help.suno.com

This file is the audio half of EASY-MODE. CapCut never starts until the clip is locked.

## Tool chooser

| Problem | Tool | Plan |
|---|---|---|
| Whole idea is wrong | Create (new gen) | any |
| Starts or ends ugly | Crop | Pro/Premier |
| Song dies mid-phrase | Extend → Get Whole Song | any paid-ish |
| One verse/chorus is bad | Replace Section | Pro/Premier |
| Need same voice across tracks | Persona | V5+ |
| Need vocal vs beat for UGC | Split from Mix | Pro/Premier |
| Need mix control / duck under voice | Auto Split (up to 12) or Studio | Pro / Premier |
| Need one odd instrument out | Advanced Split | Premier |
| Arrange / FX / MIDI / export WAV | Studio 2.0 | Premier uncapped 32-bit/48kHz |
| Sharpen an old take | Remaster | paid |
| Same melody, new style | Cover | paid |

There is **no official public Suno API**. Third-party “Suno APIs” are not Suno. Do not wire them into this factory.

## Factory path (Grateful Morning and every Reel)

1. Generate or pick the track on Suno.
2. Crop dead air. Replace only the broken section. Do not re-roll a good chorus.
3. Export for CapCut:
   - Fast path: download the mix, trim 15–22s in CapCut (EASY-MODE Step 2).
   - UGC talking path: **Split from Mix → Vocals** so you can duck the instrumental under your phone voice.
   - Cinematic / lyrics path: mix is enough.
4. Name the file `TrackName_Type_Date.wav` or `.mp3` and drop it in the job folder when you have one.
5. Write the filename into `jobs/.../manifest.json` `source_assets` + set `rights.audio`.
6. Only then open CapCut EASY-MODE.

## Stems — use the cheap split first

From Library: `...` → Get Stems → Extract.
From Studio: right-click clip → Split Stems.

- **Split from Mix** — 10 credits/stem. Vocal + everything-else. This is the UGC default.
- **Auto Split** — 50 credits, up to 12 stems. Only if you will actually mix.
- **Advanced Split** — Premier, ~100 instruments, 10 credits/stem. Rare for Reels.

Cleaner, sparser prompts = cleaner stems. Dense stacks bleed.

## Studio 2.0 — when a Reel is not enough

Browser DAW (Chrome, not phone, not Safari MIDI). Chat bar can Cover/Remix stems, rename clips, generate audio from MIDI.
Effects on tracks. Automation. Wavetable synth. Advanced split on the timeline.
Premier: unlimited Studio export at 32-bit/48kHz.
Regular song downloads are capped; Studio export is the leak valve on Premier.

For this factory, Studio is optional. CapCut Reels do not need 12 stems.

## Persona

Save the vocal you want as a Persona. Reuse it so the account sounds like one artist, not twelve random singers. Album coherence > one-off bangers.

## Rights note

Generation is a draft. Manifest stays `NEEDS_REVIEW` until you confirm you may use that file commercially on Reels. Do not invent a license in the caption.
