---
description: "Quick feature request without full ceremony"
---

# Lite Request

Capture a feature request quickly without full SDD ceremony.

## Purpose

For small, well-understood features that don't need extensive specification.

## When to Use

Use lite workflow for:
- Simple bug fixes (< 1 day)
- Small enhancements (< 2 days)
- Well-understood changes
- Low-risk modifications

**Don't use for**:
- New features requiring design
- Changes affecting architecture
- High-risk modifications
- Changes requiring stakeholder input

## Quick Request Format

```markdown
# Lite Request: {Title}

## Summary

{One paragraph describing what needs to be done}

## Motivation

{Why this is needed - problem or opportunity}

## Proposed Solution

{Brief description of the solution approach}

## Acceptance Criteria

- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] {Criterion 3}

## Scope

**Includes**:
- {What's in scope}

**Excludes**:
- {What's explicitly out}

## Effort Estimate

- **Size**: S/M (< 2 days)
- **Risk**: Low
- **Files**: ~{N} files affected

## Notes

{Any additional context}
```

## Example

```markdown
# Lite Request: Add Retry Logic to API Client

## Summary

Add automatic retry with exponential backoff for failed API requests.

## Motivation

Intermittent network issues cause unnecessary failures. Retries would
improve reliability without user intervention.

## Proposed Solution

Add a retry decorator to the API client with:
- Max 3 retries
- Exponential backoff (1s, 2s, 4s)
- Retry on 5xx and network errors only

## Acceptance Criteria

- [ ] API client retries on 5xx errors
- [ ] Exponential backoff implemented
- [ ] Max retries configurable
- [ ] Logging for retry attempts

## Scope

**Includes**: API client retry logic

**Excludes**: Circuit breaker, rate limiting

## Effort Estimate

- **Size**: S (< 1 day)
- **Risk**: Low
- **Files**: 2 files (client.py, test_client.py)
```

## Output

Create `.lbi/specs/{feature}/lite-request.md`

## Next Steps

After lite request:
1. Run `/lbi.lite.plan` for quick planning
2. Or jump directly to `/lbi.lite.implement`