---
description: "Conduct and document user interviews"
---

# User Interviews

Plan, conduct, and synthesize user interview findings.

## Purpose

Gather qualitative insights directly from users to understand their needs, behaviors, and pain points.

## Prerequisites

- Discovery scope defined
- Access to target users
- Interview guide prepared

## Instructions

1. Prepare interview guide
2. Recruit participants
3. Conduct interviews
4. Synthesize findings

## Interview Guide Template

```markdown
# Interview Guide: {Topic}

## Objectives

- Understand {specific goal 1}
- Explore {specific goal 2}
- Validate {assumption}

## Participant Criteria

- {Criterion 1}
- {Criterion 2}
- {Criterion 3}

## Introduction Script

"Thank you for taking the time to speak with us. We're exploring
{topic} and would love to learn about your experience. There are
no right or wrong answers - we're just trying to understand your
perspective. This will take about {duration}."

## Questions

### Warm-up (5 min)

1. Tell me about your role at {company/context}
2. How long have you been doing {activity}?

### Current State (10 min)

3. Walk me through how you currently {do the task}
4. What tools or processes do you use?
5. What's the most challenging part?

### Pain Points (10 min)

6. When was the last time you struggled with {problem}?
7. What happened? How did you feel?
8. How did you resolve it?

### Ideal State (10 min)

9. If you could wave a magic wand, what would change?
10. What would that enable you to do?
11. How much would that be worth to you?

### Wrap-up (5 min)

12. Is there anything else you think we should know?
13. Who else should we talk to?

## Probing Questions

- "Tell me more about that..."
- "Why is that important to you?"
- "Can you give me an example?"
- "How often does that happen?"
```

## Interview Notes Template

```markdown
# Interview: {Participant ID}

**Date**: {YYYY-MM-DD}
**Duration**: {minutes}
**Interviewer**: {Name}

## Participant Profile

- **Role**: {Job title}
- **Experience**: {Years in role}
- **Segment**: {User segment}

## Key Quotes

> "{Direct quote from user}"
> - Context: {When/why they said this}

## Observations

- {Behavior or reaction noted}
- {Non-verbal cues}

## Insights

| Theme | Finding | Evidence |
|-------|---------|----------|
| {Theme} | {What we learned} | {Quote/observation} |

## Follow-up Items

- [ ] {Action item}
- [ ] {Question for next interview}
```

## Synthesis Template

```markdown
# Interview Synthesis

**Interviews Completed**: {N}
**Date Range**: {Start} - {End}

## Themes

### Theme 1: {Name}

**Frequency**: {N} of {Total} mentioned
**Summary**: {One sentence}

**Evidence**:
- P1: "{Quote}"
- P3: "{Quote}"
- P5: "{Quote}"

### Theme 2: {Name}

[Same structure]

## User Segments Refined

| Segment | Characteristics | Key Needs |
|---------|-----------------|-----------|
| {Name} | {Traits} | {Needs} |

## Recommendations

1. {Recommendation based on findings}
2. {Recommendation based on findings}
```

## Next Steps

After interviews:
1. Run `/lbi.pm.research` for supporting market data
2. Run `/lbi.pm.validate-problem` to validate findings