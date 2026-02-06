---
description: "Verify claims and facts in documentation"
---

# Fact Check

Verify the accuracy of claims, versions, and facts in documentation.

## Purpose

Ensure documentation and specifications contain accurate, verifiable information.

## Prerequisites

- Document to verify
- Access to authoritative sources

## Instructions

1. Identify claims to verify
2. Find authoritative sources
3. Verify each claim
4. Document findings

## Verification Categories

### Version Claims

```markdown
## Version Verification

| Technology | Claimed | Actual | Source | Status |
|------------|---------|--------|--------|--------|
| Python | 3.11+ | 3.11.7 | python.org | ✅ |
| FastAPI | 0.100+ | 0.109.0 | pypi.org | ✅ |
| React | 18 | 18.2.0 | npmjs.com | ✅ |
```

### API/SDK Claims

```markdown
## API Verification

| Claim | Source | Status |
|-------|--------|--------|
| "API supports pagination" | API docs | ✅ Verified |
| "Rate limit is 100/min" | API docs | ⚠️ Changed to 60/min |
| "OAuth2 supported" | Provider docs | ✅ Verified |
```

### Performance Claims

```markdown
## Performance Verification

| Claim | Method | Result | Status |
|-------|--------|--------|--------|
| "Response time < 100ms" | Load test | p95: 85ms | ✅ |
| "Supports 10k concurrent" | Load test | 8k max | ❌ |
| "99.9% uptime" | Historical data | 99.7% | ⚠️ |
```

### Feature Claims

```markdown
## Feature Verification

| Claim | Verification | Status |
|-------|--------------|--------|
| "Supports SSO" | Tested integration | ✅ |
| "WCAG 2.1 AA compliant" | Accessibility audit | ⚠️ Partial |
| "Works offline" | Manual test | ✅ |
```

## Verification Process

### Step 1: Extract Claims

Read the document and list all verifiable claims:

```markdown
## Claims to Verify

1. {Claim 1}
2. {Claim 2}
3. {Claim 3}
```

### Step 2: Identify Sources

For each claim, find authoritative source:

| Source Type | Examples | Trust Level |
|-------------|----------|-------------|
| Official docs | python.org, aws.amazon.com | High |
| Package registry | pypi.org, npmjs.com | High |
| Test results | Actual test output | High |
| Third-party reviews | Blog posts, articles | Medium |
| Assumptions | Undocumented | Low |

### Step 3: Verify Each Claim

```markdown
### Claim: "{Exact claim text}"

**Source**: {URL or reference}
**Verified Date**: {YYYY-MM-DD}
**Status**: ✅ Verified / ❌ False / ⚠️ Outdated / ❓ Unverifiable
**Notes**: {Any relevant context}
```

### Step 4: Document Findings

```markdown
## Fact Check Report

**Document**: {Document name/path}
**Checked By**: {Name}
**Date**: {YYYY-MM-DD}

### Summary

| Status | Count |
|--------|-------|
| ✅ Verified | {N} |
| ⚠️ Needs Update | {N} |
| ❌ Incorrect | {N} |
| ❓ Unverifiable | {N} |

### Issues Found

#### Issue 1: {Incorrect claim}

- **Location**: {Where in document}
- **Current**: "{What it says}"
- **Correct**: "{What it should say}"
- **Source**: {Authoritative source}

### Recommendations

1. {Recommendation 1}
2. {Recommendation 2}
```

## Common Verification Sources

| Category | Source |
|----------|--------|
| Python packages | pypi.org, GitHub releases |
| NPM packages | npmjs.com, GitHub releases |
| Cloud services | Official documentation |
| APIs | Provider API docs, Postman tests |
| Performance | Load test results, monitoring |
| Security | CVE databases, security advisories |

## Next Steps

After fact-checking:
1. Update documentation with corrections
2. Add source links for verifiable claims
3. Mark unverifiable claims for removal