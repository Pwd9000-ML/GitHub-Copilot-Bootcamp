# Week 3: DevOps & Testing

## Overview

Week 3 focuses on DevOps practices, test automation, and CI/CD pipeline development using GitHub Copilot.

## Learning Objectives

By the end of this week, you will:
- Write comprehensive tests with Copilot assistance
- Implement test-driven development (TDD)
- Create CI/CD pipelines
- Automate code quality checks
- Integrate Copilot into DevOps workflows

## Daily Breakdown

### Day 1: Test-Driven Development
**Topics**:
- TDD principles and workflow
- Unit test generation
- Test frameworks (Jest, pytest, etc.)
- Mocking and stubbing

**Exercises**:
1. Write tests before implementation
2. Generate test cases with Copilot
3. Implement code to pass tests
4. Refactor with confidence

**Lab**: Start `labs/week3-devops-testing/`

### Day 2: Advanced Testing
**Topics**:
- Integration testing
- End-to-end testing
- Test coverage analysis
- Edge case identification

**Exercises**:
1. Write integration tests
2. Generate E2E test scenarios
3. Achieve high test coverage
4. Test error conditions

**Tools**:
- Jest, pytest, JUnit
- Coverage.py, Istanbul
- Testing frameworks

### Day 3: CI/CD Pipeline Creation
**Topics**:
- GitHub Actions workflows
- Build automation
- Test automation
- Deployment strategies

**Exercises**:
1. Create GitHub Actions workflow
2. Automate testing
3. Set up continuous deployment
4. Configure branch protections

**Resources**:
- `.github/workflows/ci.yml`
- `.github/workflows/codeql.yml`

### Day 4: Code Quality & Automation
**Topics**:
- Linting and formatting
- Static analysis
- Performance testing
- Quality gates

**Exercises**:
1. Configure linters
2. Set up automated formatting
3. Add pre-commit hooks
4. Implement quality checks

**Tools**:
- ESLint, Pylint, RuboCop
- Prettier, Black
- SonarQube

### Day 5: DevOps Best Practices
**Topics**:
- Infrastructure as Code
- Container configuration
- Monitoring and logging
- DORA metrics

**Activities**:
1. Review DORA metrics
2. Complete week 3 lab
3. Present testing strategies
4. Submit reflection

## Key Concepts

### Test-Driven Development
1. Write a failing test
2. Write minimal code to pass
3. Refactor with confidence
4. Repeat

### Testing Pyramid
- **Unit Tests**: Fast, isolated, numerous
- **Integration Tests**: Component interactions
- **E2E Tests**: Full user workflows

### CI/CD Best Practices
- Automate everything
- Fast feedback loops
- Fail fast
- Keep builds green
- Deploy frequently

### Code Quality Metrics
- Test coverage
- Code complexity
- Technical debt
- Build success rate

## Lab Assignment

Complete `labs/week3-devops-testing/`:
1. Implement TDD workflow
2. Achieve >80% test coverage
3. Create CI/CD pipeline
4. Configure quality gates

Submit via Pull Request:
- Test suite with high coverage
- Working CI/CD pipeline
- Quality reports
- Reflection on DevOps practices

## Testing Checklist

Before submitting:
- [ ] Unit tests written
- [ ] Integration tests passing
- [ ] >80% code coverage
- [ ] CI pipeline configured
- [ ] All checks passing
- [ ] Edge cases covered
- [ ] Performance tested

## CI/CD Pipeline Components

Your pipeline should include:
1. **Build stage**: Compile/transpile code
2. **Test stage**: Run all tests
3. **Lint stage**: Code quality checks
4. **Security stage**: Vulnerability scanning
5. **Deploy stage**: Automated deployment

## Resources

- [GitHub Actions Documentation](https://docs.github.com/actions)
- [DORA Metrics](../scorecards/dora-cheat-sheet.md)
- [Testing Best Practices](org-standards/coding-standards.md)

## DORA Metrics Focus

Track these metrics for your project:
- **Deployment Frequency**: How often you deploy
- **Lead Time for Changes**: Time from commit to production
- **Time to Restore Service**: Recovery time from failures
- **Change Failure Rate**: Percentage of failed deployments

## Next Week Preview

Week 4 is the final week, focusing on legacy code refactoring. You'll apply all learned skills to improve existing codebases using Copilot!
