# Automation Contract

Automation may create drafts and queue review, but it must not publish unapproved media.

## Handoff payload

```json
{
  "job_id": "YYYY-MM-DD-slug",
  "status": "needs_review",
  "master_asset": "edit/master-v1.mp4",
  "target_platforms": ["tiktok", "instagram_reels", "youtube_shorts"],
  "rights_status": "needs_review",
  "approval_required": true
}
```

Consumers must reject payloads where `approval_required` is not `false` and `status` is not `approved`. Credentials belong in the automation platform secret store, never in payloads or repository files.
