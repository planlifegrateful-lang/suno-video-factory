# Production Runbook

## Job lifecycle

1. Create a job folder from `templates/job-manifest.json`.
2. Mark missing inputs `needs_review`; never invent them.
3. Generate draft script, shot list, voice direction, and captions.
4. Record source assets and provenance in the manifest.
5. Assemble the master edit and render a local review export.
6. Obtain human approval for claims, rights, accessibility, disclosure, and final playback.
7. Render platform variants and update the manifest.
8. Publish only approved variants; record URLs after publication.

## Batch controls

- Use one unique job ID per concept and revision.
- Keep drafts separate from approved exports.
- Do not overwrite an approved export; increment the version.
- Quarantine failed renders and record the reason.
- Review a batch sample before releasing the whole batch.

## Definition of done

A job is complete only when the manifest is complete, the final export was watched end-to-end, and an identified reviewer approved it.
