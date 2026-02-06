---
description: "Validate problem-solution fit before building"
---

# Validate Problem

Confirm the problem is real, significant, and worth solving.

## Purpose

Ensure we're solving a real problem before investing in solutions. Validate assumptions with evidence.

## Prerequisites

- Discovery findings
- User interview insights
- Market research

## Instructions

1. Define validation criteria
2. Gather supporting evidence
3. Assess problem validity
4. Make go/no-go recommendation

## Validation Framework

### Problem Statement

```markdown
## Problem Definition

**Problem Statement**:
{User segment} experiences {problem} when {situation}, which results
in {negative outcome}. This costs them {quantified impact}.

**Affected Users**: {Number/percentage}
**Frequency**: {How often it occurs}
**Severity**: {Impact level: Critical/High/Medium/Low}
```

### Validation Criteria

```markdown
## Validation Criteria

| Criterion | Threshold | Evidence Required |
|-----------|-----------|-------------------|
| Problem exists | >70% of users confirm | Interview data |
| Problem is painful | Pain score >7/10 | Survey data |
| Users seek solutions | >50% tried alternatives | Interview data |
| Problem is growing | YoY increase | Market data |
| Users will pay | >30% willingness | Survey data |
```

### Evidence Assessment

```markdown
## Evidence Summary

### Qualitative Evidence

| Source | Finding | Confidence |
|--------|---------|------------|
| User interviews (N={X}) | {Finding} | High |
| Support tickets | {Finding} | Medium |
| Social listening | {Finding} | Low |

### Quantitative Evidence

| Metric | Value | Benchmark |
|--------|-------|-----------|
| Users affected | {N} | - |
| Time lost | {hours/week} | - |
| Money lost | ${X}/year | - |
| NPS for alternatives | {score} | Industry: {X} |

### Supporting Quotes

> "{User quote demonstrating problem}"
> - {User segment}, {Context}
```

### Risk Assessment

```markdown
## Validation Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Sample bias | Medium | High | Diversify sources |
| Confirmation bias | Medium | Medium | Devil's advocate review |
| Market timing | Low | High | Trend analysis |
```

### Decision Framework

```markdown
## Validation Scorecard

| Criterion | Target | Actual | Status |
|-----------|--------|--------|--------|
| Problem confirmed | >70% | {X}% | ✅/❌ |
| Pain level | >7/10 | {X}/10 | ✅/❌ |
| Seeking solutions | >50% | {X}% | ✅/❌ |
| Willingness to pay | >30% | {X}% | ✅/❌ |
| Market growing | Yes | {Yes/No} | ✅/❌ |

**Overall Score**: {X}/5 criteria met

## Recommendation

**Decision**: ✅ Proceed / ⚠️ Pivot / ❌ Stop

**Rationale**: {Why this recommendation}

**Next Steps**:
1. {Action if proceeding}
2. {Action if pivoting}
```

## Output

Create `.lbi/specs/{feature}/validation/problem-validation.md`

## Next Steps

After validation:
- If validated: Run `/lbi.pm.prd` to create requirements
- If not validated: Run `/lbi.pm.discover` with new hypothesis