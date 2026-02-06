---
description: "Discover and document product opportunities"
---

# Product Discovery

Identify and document product opportunities and user needs.

## Purpose

Systematically discover problems worth solving and opportunities worth pursuing before committing to solutions.

## Prerequisites

- Access to users or stakeholders
- Understanding of business context

## Instructions

1. Define discovery scope
2. Identify key questions
3. Plan discovery activities
4. Document findings

## Discovery Framework

### Step 1: Define Scope

```markdown
## Discovery Scope

**Problem Space**: {Area to explore}
**Time Box**: {Duration}
**Team**: {Who's involved}

### Goals

- Understand {user segment} needs
- Identify pain points in {domain}
- Validate assumptions about {hypothesis}

### Non-Goals

- Building solutions
- Detailed specifications
- Technical design
```

### Step 2: Identify Assumptions

```markdown
## Assumptions to Validate

| ID | Assumption | Risk Level | Validation Method |
|----|------------|------------|-------------------|
| A1 | Users need {X} | High | User interviews |
| A2 | Problem costs ${Y} | Medium | Data analysis |
| A3 | Users will pay for {Z} | High | Survey |
```

### Step 3: Plan Activities

```markdown
## Discovery Activities

| Activity | Purpose | Participants | Duration |
|----------|---------|--------------|----------|
| User interviews | Understand needs | 5-8 users | 2 weeks |
| Competitive analysis | Market landscape | PM team | 3 days |
| Data analysis | Quantify problem | Data + PM | 1 week |
```

### Step 4: Document Findings

```markdown
## Discovery Findings

### Key Insights

1. **Insight**: {Finding}
   - **Evidence**: {Supporting data}
   - **Implication**: {What it means}

2. **Insight**: {Finding}
   - **Evidence**: {Supporting data}
   - **Implication**: {What it means}

### User Segments Identified

| Segment | Size | Pain Level | Willingness to Pay |
|---------|------|------------|-------------------|
| {Segment A} | {N} | High | Medium |
| {Segment B} | {N} | Medium | High |

### Opportunities Ranked

| Opportunity | Impact | Effort | Priority |
|-------------|--------|--------|----------|
| {Opportunity 1} | High | Medium | P0 |
| {Opportunity 2} | Medium | Low | P1 |
```

## Output

Create `.lbi/specs/{discovery}/discovery-findings.md`

## Next Steps

After discovery:
1. Run `/lbi.pm.interview` to conduct user interviews
2. Run `/lbi.pm.research` for market research
3. Run `/lbi.pm.validate-problem` to validate findings