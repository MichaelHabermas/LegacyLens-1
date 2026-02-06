---
description: "Share specifications for external review"
---

# Upload Specification

Prepare and share feature specifications for external review, collaboration, or documentation.

## Instructions

1. Identify the feature specification to share
2. Review and sanitize content for external sharing
3. Choose the sharing method
4. Generate shareable output
5. Track feedback and updates

## Pre-Upload Checklist

- [ ] Remove any sensitive information (API keys, internal URLs)
- [ ] Remove internal comments or notes
- [ ] Verify all referenced files are included
- [ ] Check for broken links or references
- [ ] Ensure formatting is consistent
- [ ] Add context for external reviewers

## Files to Include

For a complete specification package, include:

| File | Purpose | Required |
|------|---------|----------|
| `request.md` | Original feature request | Yes |
| `spec.md` | Technical specification | Yes |
| `plan.md` | Implementation plan | Recommended |
| `tasks.md` | Task breakdown | Optional |
| `architecture.md` | Architecture overview | If exists |

## Sharing Options

### 1. Archive Package
Create a zip archive of specification files:
```
.lbi/specs/{feature}/
├── request.md
├── spec.md
├── plan.md
└── tasks.md
```

### 2. Markdown Export
Combine all specs into a single markdown document for easy sharing.

### 3. Git Branch
Push specifications to a dedicated branch for review:
```
git checkout -b spec/{feature-name}
git add .lbi/specs/{feature}/
git commit -m "spec: add {feature} specification for review"
git push origin spec/{feature-name}
```

## Sanitization Guidelines

### Remove
- API keys and secrets
- Internal IP addresses or URLs
- Employee names (use roles instead)
- Proprietary algorithm details
- Internal tooling references

### Keep
- Technical requirements
- Architecture decisions
- Integration points
- Acceptance criteria
- Timeline estimates

## Feedback Tracking

| Reviewer | Date | Feedback | Status |
|----------|------|----------|--------|
| [Name] | [Date] | [Summary] | [Open/Resolved] |

## Next Steps

After gathering feedback, update specifications with `/lbi.specify` if changes are needed.