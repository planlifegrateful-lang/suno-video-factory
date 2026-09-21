# YouTube + YouTube Music + Studio OS

Brand: Plan Life Grateful  
Buffer org: My Organization (`67bf60560ff0f143e13ac2a8`)  
YouTube channel in Buffer: **Charles** (`67c2266b3b85969eafab2932`) — connected  
TikTok in Buffer: hustleguru46 — disconnected; reconnect before using Buffer for TikTok

This is not one pipe. Treat it as two products that share a track.

## Path A — YouTube (videos you control)

Uploaded by you. Lives on the channel. Analytics in YouTube Studio.

From **one downloaded Suno track** cut three files after CapCut EASY-MODE:

| File | Length | Use |
|---|---|---|
| `{Track}_Shorts_{date}.mp4` | 15–22s (max 3 min, 9:16) | YouTube Shorts |
| `{Track}_Visualizer_{date}.mp4` | full track, 16:9 or 9:16 loop | long-form / Music tab companion |
| `{Track}_UGC_{date}.mp4` | 15–30s talking | Shorts + community |

Specs that make a Short: **9:16 or 1:1, ≤ 3 minutes**, 1080×1920, H.264 + AAC. YouTube classifies it. `#Shorts` is optional now.

### Studio checklist (every upload)

YouTube Studio → Content → the video

- [ ] Title ≤ 100 chars, hook first, track name in it
- [ ] Description: 1-line promise + track name + @planlifegrateful + Suno credit if required by your license + pack CTA
- [ ] Made for kids: **No**
- [ ] Altered / AI content: disclose if the vocal/visual is synthetic (YouTube altered-content toggle)
- [ ] Category: Music (`10`) for visualizers; People & Blogs (`22`) only if it is talking UGC
- [ ] Playlist: `Plan Life Grateful — Shorts` and `Plan Life Grateful — Tracks`
- [ ] First comment: pinned CTA
- [ ] End screen / cards: link the official Art Track once Path B is live
- [ ] Thumbnail: 4 words max (QUICK-TEXT / pack thumbnail)
- [ ] Publish as **Private** first if this is a new system. Watch processing. Then Public or schedule.

### Buffer automation (already connected)

Buffer can publish to Charles when the **MP4 is at a public HTTPS URL** (Drive public link will fail; need a direct file URL).

Required metadata:

```
channelId: 67c2266b3b85969eafab2932
schedulingType: notification   # human approve until the system is trusted
mode: addToQueue
text: {caption}
assets: [{ video: { url: "https://...mp4" } }]
metadata.youtube.title: {title}
metadata.youtube.categoryId: "10"
metadata.youtube.privacy: private
metadata.youtube.madeForKids: false
metadata.youtube.isAiGenerated: true
metadata.youtube.notifySubscribers: false   # Shorts: off unless it is a drop
```

Do not auto-public until one human has watched the file.

Official API alternative: YouTube Data API `videos.insert` (OAuth on the Charles channel). Same file rules. Default quota ~6 uploads/day. Not wired in this repo yet — Buffer is the live pipe.

## Path B — YouTube Music (official catalog)

Uploading a video to Studio does **not** put a proper track on YouTube Music search / playlists / Art Tracks.

Official YT Music requires a **distributor** (DistroKid, TuneCore, RouteNote, etc.) delivering WAV + cover + metadata. YouTube then builds an Art Track + Topic channel. Studio analytics for streams still sit on the channel once you have an Official Artist Channel (OAC).

### Distributor packet per track

- WAV (not the 20s Reel trim — the full mix)
- Cover 3000×3000
- Title, artist: Plan Life Grateful, language, genre: inspirational / world
- Explicit: no
- ISRC if the distributor assigns one
- Release date ≥ 7 days out
- Stores: YouTube Music + others you want

After it lands:
1. Confirm the Topic / Art Track exists
2. Ask the distributor to request **OAC merge** into Charles (channel name should match artist name — rename Charles → Plan Life Grateful when you are ready)
3. In Studio, link Shorts and visualizers to the official release

Royalties for YT Music streams pay through the **distributor**, not Studio’s AdSense tab.

## One-track operating week

Day 0: lock Suno file + rights in the job manifest  
Day 0: CapCut EASY-MODE → Short + optional UGC  
Day 1: Buffer/Studio upload Short as private → watch → public  
Day 1–2: send full WAV + cover to distributor (Path B)  
Day 2–7: reply to comments 2 hours; do not upload a second Short of the same hook  
When Art Track is live: pin it on the Short

## What this system will not do

- Upload a local file from this chat (no file on the agent machine)
- Claim Content ID on music you do not control
- Treat a Short as a YouTube Music official release
- Auto-public without a human watch
