---
description: "Systematic debugging assistance"
---

# Debug Issue

Systematically investigate and resolve bugs, errors, or unexpected behavior.

## Instructions

1. Describe the issue clearly
2. Gather evidence (error messages, logs, stack traces)
3. Form hypotheses about root cause
4. Test hypotheses systematically
5. Implement and verify the fix

## Issue Description

**Expected Behavior**: [What should happen]

**Actual Behavior**: [What actually happens]

**Steps to Reproduce**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Evidence Collection

### Error Messages
```
[Paste error messages here]
```

### Relevant Logs
```
[Paste relevant log output here]
```

### Stack Trace
```
[Paste stack trace if available]
```

## Debugging Checklist

- [ ] Reproduce the issue consistently
- [ ] Identify the exact line/component where failure occurs
- [ ] Check recent changes that might have caused the issue
- [ ] Review related code for obvious issues
- [ ] Add logging/debugging statements if needed
- [ ] Test fix in isolation before integrating

## Hypothesis Testing

| Hypothesis | Test | Result |
|------------|------|--------|
| [Theory 1] | [How to test] | [Pass/Fail] |
| [Theory 2] | [How to test] | [Pass/Fail] |

## Root Cause Analysis

**Root Cause**: [Identified root cause]

**Contributing Factors**: [Any contributing factors]

## Fix Implementation

**Proposed Fix**: [Description of the fix]

**Files Changed**: [List of files to modify]

## Next Steps

After implementing the fix, run `/lbi.tests` to verify the fix works and doesn't break existing functionality.