# AI UGC elite upgrade patch

This patch is prepared for application when repository write access is available.

## Required changes

1. Add a truthful README covering runtime, setup, environment variables, health checks, and limitations.
2. Add `.env.example` with blank values only.
3. Add `SECURITY.md` covering secret storage, prompt privacy, webhook authentication, and generated-content rights.
4. Add a deterministic `validate` or `test` command.
5. Add a smoke test for the primary content-agent request path.
6. Document the handoff contract: `job_id`, `status`, `script`, `captions`, `provenance_status`, and `approval_required`.

## Acceptance criteria

- No provider credential is returned to a client.
- Requests are size-limited and validated.
- Errors use stable, non-sensitive response codes.
- Unverified claims are marked `NEEDS_REVIEW`.
- Generated content cannot be published without explicit approval.
