---
description: "Database and code migration workflow"
---

# Migration Guide

Plan and execute database schema changes, data migrations, or code migrations safely.

## Instructions

1. Identify the migration scope and type
2. Create a migration plan with rollback strategy
3. Test migration in a safe environment
4. Execute migration with monitoring
5. Verify data integrity post-migration

## Migration Types

- **Schema Migration**: Database structure changes
- **Data Migration**: Moving or transforming data
- **Code Migration**: Updating codebase patterns or dependencies
- **Infrastructure Migration**: Moving to new systems or services

## Migration Checklist

### Pre-Migration
- [ ] Document current state
- [ ] Create backup of affected data
- [ ] Define rollback procedure
- [ ] Estimate downtime (if any)
- [ ] Notify stakeholders
- [ ] Test migration in staging environment

### Migration Execution
- [ ] Put system in maintenance mode (if needed)
- [ ] Execute migration scripts
- [ ] Monitor progress and errors
- [ ] Verify data integrity checks
- [ ] Run smoke tests

### Post-Migration
- [ ] Validate all data migrated correctly
- [ ] Run integration tests
- [ ] Monitor application performance
- [ ] Update documentation
- [ ] Remove maintenance mode

## Migration Plan Template

### Overview
**Migration Name**: [Name]
**Type**: [Schema/Data/Code/Infrastructure]
**Estimated Duration**: [Time]
**Risk Level**: [Low/Medium/High]

### Changes
| Change | Before | After | Risk |
|--------|--------|-------|------|
| [Change 1] | [Old] | [New] | [Risk] |

### Rollback Plan
1. [Rollback step 1]
2. [Rollback step 2]
3. [Rollback step 3]

### Dependencies
- [Dependency 1]
- [Dependency 2]

## Database Migration Script Template

```sql
-- Migration: [migration_name]
-- Date: [date]
-- Description: [description]

-- Forward migration
BEGIN TRANSACTION;

-- [Migration SQL here]

COMMIT;

-- Rollback (if needed)
-- BEGIN TRANSACTION;
-- [Rollback SQL here]
-- COMMIT;
```

## Next Steps

After migration, run `/lbi.tests` to verify application functionality.