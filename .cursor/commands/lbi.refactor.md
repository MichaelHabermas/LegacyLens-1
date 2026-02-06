---
description: "Guided code refactoring workflow"
---

# Refactor Code

Analyze target code and apply refactoring improvements following SOLID principles and clean code practices.

## Instructions

1. Read the project constitution at `.lbi/memory/constitution.md`
2. Identify the target code to refactor
3. Analyze code smells and anti-patterns
4. Plan refactoring steps incrementally
5. Apply changes while preserving behavior
6. Verify tests still pass after each change

## Refactoring Checklist

- [ ] Extract method for long functions (>50 lines)
- [ ] Rename unclear variables and functions
- [ ] Remove duplicate code (DRY principle)
- [ ] Split large classes (Single Responsibility)
- [ ] Reduce cyclomatic complexity
- [ ] Remove dead code
- [ ] Simplify conditional expressions
- [ ] Replace magic numbers with named constants

## Common Refactoring Patterns

### Extract Method
When a code fragment can be grouped together:
- Identify the fragment to extract
- Create a new method with a clear name
- Replace the fragment with a method call

### Rename
When names don't clearly express intent:
- Choose a name that reveals purpose
- Update all references consistently

### Replace Conditional with Polymorphism
When conditionals select behavior based on type:
- Create subclasses for each type
- Move conditional branches to overriding methods

## Next Steps

After refactoring, run `/lbi.tests` to verify behavior is unchanged.