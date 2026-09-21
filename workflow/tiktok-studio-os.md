# TikTok Studio + generator + sync OS

Brand: Plan Life Grateful  
TikTok Buffer channel: **hustleguru46** (`67bf7c323b85969eafc45670`) — **DISCONNECTED**  
YouTube Buffer channel: **Charles** — connected

One master file feeds TikTok and YouTube Shorts. Do not render two different edits.

## Generator (already running)

1. Suno lock → job folder  
2. CapCut EASY-MODE or factory ffmpeg Short  
3. Master file: `1080x1920`, `30fps`, `H.264 + AAC 48kHz stereo`, `+faststart`, `15–22s`  
4. Same file = TikTok + YouTube Shorts + Reels

Live example already cut:
`GratefulMorning_Shorts_LIVE.mp4` (Cold Wudu Water, 48–66s slice)

TikTok ingest spec: 9:16, MP4 H.264, AAC, 23–60 fps, min 3s. Studio upload: MP4/WebM, ≥720x1280, ≤30 min, <10GB. API upload cap is tighter (4GB / ~10 min).

Safe zone: keep hook text off the bottom ~250px and right-side buttons.

## TikTok Studio (human app — cannot be remote-controlled from here)

studio.tiktok.com or in-app Studio

Every post:
- [ ] Upload the **same** master MP4 (do not CapCut a second version)
- [ ] Cover frame at ~1.0s (hook text visible) — Buffer field `thumbnailOffset: 1000`
- [ ] Caption from `jobs/{id}/tiktok.md`
- [ ] Disclose AI-generated content when Suno/AI visual is used
- [ ] Allow comments. Duet/stitch on unless the issue says off
- [ ] Add sound: this file already has the track baked. Do not layer a second commercial sound on top
- [ ] Post time: first 90 min after Fajr local or 7–9pm local
- [ ] First hour: reply to every comment

TikTok Studio is analytics + upload + inbox. It is not a second editor. Editing stays in EASY-MODE.

## Sync map (one job, three outlets)

| Step | TikTok | YouTube Shorts | YouTube Music |
|---|---|---|---|
| File | same 9:16 master | same 9:16 master | full WAV + cover via distributor |
| Caption | short hook + 4–8 tags | title + description | metadata form |
| Tool now | TikTok Studio manual until Buffer reconnects | Buffer Charles or YT Studio | DistroKid/TuneCore |
| Privacy first | friends-only / private review | private | scheduled release |
| After watch | public | public | Art Track live |

Never post TikTok and Shorts with different hooks the same day. Same hook, same file, same hour window.

## Buffer TikTok (blocked until reconnect)

Channel id `67bf7c323b85969eafc45670` is disconnected. Reconnect in Buffer → hustleguru46.

Then:
```
channelId: 67bf7c323b85969eafc45670
schedulingType: notification
text: {tiktok caption}
assets: [{ video: { url: "https://direct.mp4", metadata: { thumbnailOffset: 1000 } } }]
metadata.tiktok.title: {hook}
metadata.tiktok.isAiGenerated: true
```

Official TikTok Content Posting API exists but unaudited apps are forced SELF_ONLY. Do not build a custom TikTok app for this factory. Buffer after reconnect is the pipe.

## What is not possible from this agent

- Click Reconnect on Buffer for you
- Log into TikTok Studio as hustleguru46
- Public-post without a direct MP4 URL
- A separate "TikTok video generator" app — the generator is this factory
