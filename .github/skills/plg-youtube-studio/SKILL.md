---
name: plg-youtube-studio
description: 'Turn a locked Suno track plus CapCut export into YouTube Shorts, Studio metadata, Buffer fields, and YouTube Music distributor packets. Use for YouTube, YouTube Music, YouTube Studio, Shorts, Art Tracks, OAC, Buffer upload.'
argument-hint: '[track] [short|visualizer|ugc]'
---

# PLG YouTube Studio

## When to use
User has downloaded tracks and wants videos/clips on YouTube or YouTube Music, Studio automation, or Buffer publish.

## Hard split
- Path A = upload video to the Charles / Plan Life Grateful channel (Studio + Buffer).
- Path B = distributor → official YouTube Music Art Track. Not an upload.
Never tell the user a Short is "on YouTube Music" as a catalog release.

## Procedure
1. Read workflow/youtube-studio-os.md and capcut/EASY-MODE.md.
2. Require a job folder. Create `jobs/{date}_{slug}/youtube.md` from the Grateful Morning example.
3. Write title, description, first comment, category, disclosure, filename.
4. Set Buffer metadata. schedulingType = notification until trusted.
5. Path B packet: WAV + 3000 cover + metadata. Leave NEEDS_REVIEW if files are missing.
6. Do not mark approved. Do not invent view counts.
7. Do not call Buffer create_post without a real direct video URL the user provided.
