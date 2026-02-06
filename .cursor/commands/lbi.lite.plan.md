---
description: "Quick implementation plan for lite workflow"
---

# Lite Plan

Create a lightweight implementation plan.

## Purpose

Quick planning for small, well-understood changes.

## Prerequisites

- Lite request at `.lbi/specs/{feature}/lite-request.md`

## Quick Plan Format

```markdown
# Lite Plan: {Title}

## Approach

{1-2 sentences on how you'll implement this}

## Changes

### Files to Modify

| File | Change Type | Description |
|------|-------------|-------------|
| `src/module.py` | Modify | Add retry logic |
| `tests/test_module.py` | Modify | Add retry tests |

### New Files (if any)

| File | Purpose |
|------|---------|
| `src/retry.py` | Retry decorator |

## Implementation Steps

1. [ ] {Step 1}
2. [ ] {Step 2}
3. [ ] {Step 3}
4. [ ] Write/update tests
5. [ ] Manual verification

## Testing Approach

- Unit tests for new logic
- Integration test for happy path
- Manual test of edge cases

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| {Risk} | {How to handle} |

## Time Estimate

- Implementation: {X} hours
- Testing: {Y} hours
- **Total**: {Z} hours
```

## Example

```markdown
# Lite Plan: Add Retry Logic to API Client

## Approach

Create a retry decorator that wraps API calls, catching transient errors
and retrying with exponential backoff.

## Changes

### Files to Modify

| File | Change Type | Description |
|------|-------------|-------------|
| `src/api/client.py` | Modify | Apply retry decorator |
| `tests/unit/test_client.py` | Modify | Add retry tests |

### New Files

| File | Purpose |
|------|---------|
| `src/utils/retry.py` | Retry decorator implementation |

## Implementation Steps

1. [ ] Create retry decorator with configurable params
2. [ ] Add exponential backoff logic
3. [ ] Apply decorator to API client methods
4. [ ] Add unit tests for retry logic
5. [ ] Test manually with simulated failures

## Testing Approach

- Unit test retry decorator in isolation
- Mock network failures to test retry behavior
- Verify backoff timing

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Retry on non-idempotent | Only retry GET, HEAD by default |
| Too aggressive retries | Cap at 3 with backoff |

## Time Estimate

- Implementation: 2 hours
- Testing: 1 hour
- **Total**: 3 hours
```

## Output

Create `.lbi/specs/{feature}/lite-plan.md`

## Next Steps

After lite plan:
1. Run `/lbi.lite.implement` to implement