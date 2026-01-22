# Week 3 Lab: DevOps & Testing

## Overview

Implement comprehensive testing and CI/CD automation for your project using GitHub Copilot.

## Objectives

- Implement test-driven development (TDD)
- Achieve high test coverage
- Create CI/CD pipeline
- Automate quality checks
- Track DORA metrics

## Prerequisites

- Completed Week 1 & 2 labs
- GitHub Copilot configured
- Basic understanding of testing frameworks

## Lab Exercises

### Exercise 1: Test-Driven Development

Implement TDD workflow:

1. **Unit Tests**
   - [ ] Write tests for all functions/methods
   - [ ] Test happy path scenarios
   - [ ] Test error conditions
   - [ ] Test edge cases
   - [ ] Achieve >80% code coverage

2. **Integration Tests**
   - [ ] Test API endpoints (if applicable)
   - [ ] Test component interactions
   - [ ] Test database operations (if applicable)
   - [ ] Test authentication flows

3. **Test Organization**
   - [ ] Organize tests by feature
   - [ ] Use descriptive test names
   - [ ] Follow AAA pattern (Arrange, Act, Assert)
   - [ ] Use test fixtures and mocks

### Exercise 2: CI/CD Pipeline

Create automated pipeline:

1. **GitHub Actions Workflow**
   - [ ] Trigger on push and PR
   - [ ] Run linting
   - [ ] Run tests with coverage
   - [ ] Build application
   - [ ] Run security scans

2. **Quality Gates**
   - [ ] Enforce test coverage threshold
   - [ ] Block PR on failing tests
   - [ ] Require code review
   - [ ] Pass security scans

3. **Optimization**
   - [ ] Cache dependencies
   - [ ] Parallelize jobs
   - [ ] Optimize build time

### Exercise 3: Code Quality

Implement quality checks:

1. **Linting**
   - [ ] Configure linter (ESLint, Pylint, etc.)
   - [ ] Fix linting errors
   - [ ] Add pre-commit hooks

2. **Formatting**
   - [ ] Configure formatter (Prettier, Black, etc.)
   - [ ] Auto-format on save
   - [ ] Enforce in CI

3. **Static Analysis**
   - [ ] Run type checking (TypeScript, mypy)
   - [ ] Address warnings
   - [ ] Document exceptions

### Exercise 4: DORA Metrics

Track metrics for your project:

1. **Deployment Frequency**
   - Track number of deployments
   - Calculate average per week

2. **Lead Time for Changes**
   - Measure commit to production time
   - Identify bottlenecks

3. **Change Failure Rate**
   - Track failed deployments
   - Calculate percentage

4. **Time to Restore Service**
   - Document incident response time
   - Create runbook

## Testing Checklist

Before submitting:

- [ ] >80% test coverage achieved
- [ ] All tests passing
- [ ] Unit tests implemented
- [ ] Integration tests implemented
- [ ] Edge cases covered
- [ ] Error conditions tested
- [ ] CI/CD pipeline configured
- [ ] All quality checks passing
- [ ] Documentation updated

## Deliverables

Submit via Pull Request:

1. **Test Suite**
   - Comprehensive tests
   - Coverage report
   - Test documentation

2. **CI/CD Pipeline**
   - GitHub Actions workflows
   - Pipeline documentation
   - Build status badges

3. **Metrics Report**
   - DORA metrics for bootcamp period
   - Analysis and insights
   - Improvement suggestions

4. **Reflection**
   - Submit Week 3 lab issue
   - Include testing learnings
   - Share effective test generation prompts

## Using Copilot for Testing

### Test Generation Prompts

```typescript
// Generate Jest unit tests for the calculateDiscount function covering:
// - Valid discount code (20% off)
// - Invalid discount code (throws error)
// - Expired discount code (throws error)
// - Zero price (returns 0)
// - Negative price (throws error)
// Use describe and it blocks
// Mock external dependencies
```

```python
# Write pytest integration tests for the /api/users endpoint with:
# - Test successful user creation (201 status)
# - Test duplicate email (400 status)
# - Test invalid input (400 status with validation errors)
# - Test authentication required (401 status)
# Use fixtures for test data
# Clean up after tests
```

### CI/CD Pipeline Prompts

```yaml
# Create a GitHub Actions workflow that:
# - Runs on push to main and pull requests
# - Sets up Node.js environment
# - Installs dependencies with caching
# - Runs linting (ESLint)
# - Runs tests with coverage
# - Uploads coverage report
# - Builds the application
# - Fails if coverage below 80%
```

## Evaluation Criteria

- **Test Coverage** (30%): Is coverage >80% with meaningful tests?
- **CI/CD Pipeline** (25%): Is pipeline well-configured?
- **Code Quality** (20%): Does code pass quality checks?
- **Metrics** (15%): Are DORA metrics tracked?
- **Documentation** (10%): Is testing documented?

## Testing Best Practices

✅ **Do**:
- Write tests before implementation (TDD)
- Test behavior, not implementation
- Use descriptive test names
- Keep tests independent
- Mock external dependencies

❌ **Don't**:
- Test implementation details
- Write flaky tests
- Skip edge cases
- Ignore failing tests
- Duplicate test logic

## Resources

- [Week 3 Materials](../../docs/week-3.md)
- [DORA Metrics Guide](../../scorecards/dora-cheat-sheet.md)
- [Testing Prompts](../../prompts/prompt-library.md#testing)
- [GitHub Actions Documentation](https://docs.github.com/actions)

## CI/CD Pipeline Template

Your pipeline should include:

```yaml
jobs:
  lint:
    # Code linting
  
  test:
    # Run tests with coverage
  
  build:
    # Build application
  
  security:
    # Security scans
```

## Next Steps

After completing this lab:
1. Submit your PR with passing CI
2. Review coverage reports
3. Complete daily reflections
4. Prepare for Week 4: Legacy Code Refactoring

Test everything! ✅
