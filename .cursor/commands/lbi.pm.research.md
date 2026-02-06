---
description: "Conduct market and competitive research"
---

# Market Research

Gather and analyze market data to inform product decisions.

## Purpose

Understand the market landscape, competitive positioning, and trends to validate opportunities.

## Prerequisites

- Discovery scope defined
- Access to market data sources

## Instructions

1. Define research questions
2. Gather market data
3. Analyze competition
4. Document findings

## Research Framework

### Market Analysis

```markdown
## Market Overview

**Market**: {Market name}
**Size**: ${TAM}
**Growth Rate**: {X}% CAGR
**Key Trends**:
- {Trend 1}
- {Trend 2}

### Market Segmentation

| Segment | Size | Growth | Our Focus |
|---------|------|--------|-----------|
| {Segment A} | ${X}B | {Y}% | Primary |
| {Segment B} | ${X}B | {Y}% | Secondary |

### Market Drivers

1. **{Driver}**: {Impact on market}
2. **{Driver}**: {Impact on market}

### Market Barriers

1. **{Barrier}**: {Impact on entry}
2. **{Barrier}**: {Impact on entry}
```

### Competitive Analysis

```markdown
## Competitive Landscape

### Direct Competitors

| Competitor | Position | Strengths | Weaknesses |
|------------|----------|-----------|------------|
| {Name} | Leader | {List} | {List} |
| {Name} | Challenger | {List} | {List} |

### Indirect Competitors

| Alternative | Use Case | Threat Level |
|-------------|----------|--------------|
| {Solution} | {When used} | Medium |

### Feature Comparison

| Feature | Us | Comp A | Comp B |
|---------|-----|--------|--------|
| {Feature 1} | ✅ | ✅ | ❌ |
| {Feature 2} | 🔜 | ✅ | ✅ |
| {Feature 3} | ✅ | ❌ | ❌ |

### Pricing Analysis

| Competitor | Model | Price Range | Target |
|------------|-------|-------------|--------|
| {Name} | SaaS | ${X}-${Y}/mo | SMB |
| {Name} | Enterprise | Custom | Enterprise |
```

### Trend Analysis

```markdown
## Industry Trends

### Technology Trends

| Trend | Maturity | Impact | Timeframe |
|-------|----------|--------|-----------|
| {AI/ML} | Growing | High | 1-2 years |
| {Cloud} | Mature | Medium | Now |

### Behavioral Trends

| Trend | Evidence | Implication |
|-------|----------|-------------|
| {Remote work} | {Data} | {What it means} |

### Regulatory Trends

| Regulation | Status | Impact |
|------------|--------|--------|
| {GDPR} | Active | High |
```

## Research Sources

| Source Type | Examples | Use For |
|-------------|----------|---------|
| Industry Reports | Gartner, Forrester | Market size, trends |
| Financial Data | SEC filings, earnings | Competitor revenue |
| User Data | G2, Capterra | User sentiment |
| News | TechCrunch, industry blogs | Recent developments |

## Output

Create `.lbi/specs/{feature}/research/market-analysis.md`

## Next Steps

After research:
1. Run `/lbi.pm.validate-problem` to validate opportunity
2. Run `/lbi.pm.prd` to create product requirements