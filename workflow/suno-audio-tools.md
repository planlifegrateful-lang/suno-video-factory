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

## Official downloads only

Suno's published help does not document a public API for downloading a user's Library or Workspace. Use the official Suno Library/Workspace → More Actions (…) → Download flow. Do not use unofficial wrappers, scrape the site, replay private endpoints, extract session cookies, record streams, or stream-rip audio. Suno's Terms say copies must be obtained through a download channel Suno makes available.

Current published download allowances (check the account page before each batch):
- Free: up to 7 lifetime trial downloads; trial downloads are non-commercial. Suno's download overview also says users who joined on/after September 3, 2026 may receive occasional trial downloads, so verify the account's actual allowance.
- Pro: 20 downloads per month.
- Premier: 60 downloads per month.
- Downloading the same song again does not consume another download.
- Download limits apply to the full Library, including older songs.

For a bulk export, Suno's official help says to select multiple songs in Library or Workspace (Ctrl-click on Windows, Command-click on Mac; Shift selects a range), right-click the selection, choose **Download All**, then choose the file type. Suno packages the selected songs into a ZIP. This is the supported bulk path; the factory does not automate Suno sign-in or download requests.

Commercial-use gate: verify that the exact track was created while subscribed to an eligible Pro/Premier tier and downloaded through an official permitted channel while that paid subscription was active. Suno's Help Center describes both paid-tier creation and paid-tier download as relevant to commercial use. A later subscription does not retroactively grant commercial rights to a song made on the free plan. If either the creation date, download date, or plan is unclear, keep the track non-commercial. A permitted paid download grants contractual commercial-use rights, but Suno does not guarantee copyright protection.

Suno also publishes a C2PA provenance detector API. That detector checks provenance metadata; it is not an API for downloading account-library audio and does not replace the download/rights evidence above.

## Factory path (Grateful Morning and every Reel)

1. Generate or pick the track on Suno.
2. Crop dead air. Replace only the broken section. Do not re-roll a good chorus.
3. Export for CapCut:
   - Fast path: download the mix through Suno's official Download menu, trim 15–22s in CapCut (EASY-MODE Step 2).
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
Suno's help documents a Studio workflow exception to the regular download limits. Confirm the exact feature and plan access in the account before relying on it.

For this factory, Studio is optional. CapCut Reels do not need 12 stems.

## Persona

Save the vocal you want as a Persona. Reuse it so the account sounds like one artist, not twelve random singers. Album coherence > one-off bangers.

## Rights note

Generation is a draft. Manifest stays `NEEDS_REVIEW` until you confirm the exact file was downloaded through an eligible official channel and may be used commercially. Do not invent a license in the caption.
