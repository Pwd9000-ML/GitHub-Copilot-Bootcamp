# Week 4: Refactoring Legacy Code

## Overview

The final week! Apply all your GitHub Copilot skills to refactor legacy code, improve code quality, and modernize existing applications.

## Learning Objectives

By the end of this week, you will:
- Understand and analyze legacy codebases
- Apply refactoring patterns with Copilot
- Improve code quality and maintainability
- Add tests to legacy code
- Modernize outdated code patterns

## Daily Breakdown

### Day 1: Legacy Code Analysis
**Topics**:
- Reading and understanding legacy code
- Identifying code smells
- Using Copilot for code explanation
- Planning refactoring strategy

**Exercises**:
1. Analyze `legacy/messy_module.py`
2. Identify code smells
3. Use Copilot Chat to understand complex logic
4. Create refactoring plan

**Lab**: Start `labs/week4-refactor-legacy/`

### Day 2: Refactoring Fundamentals
**Topics**:
- Extract method/function
- Rename for clarity
- Remove duplication
- Simplify conditionals

**Exercises**:
1. Extract complex methods
2. Rename unclear variables
3. Eliminate duplicate code
4. Simplify boolean expressions

**Patterns**:
- DRY (Don't Repeat Yourself)
- SOLID principles
- Clean Code practices

### Day 3: Adding Tests to Legacy Code
**Topics**:
- Characterization tests
- Test coverage for legacy code
- Safe refactoring with tests
- Test-driven refactoring

**Exercises**:
1. Write characterization tests
2. Add unit tests for legacy functions
3. Ensure tests pass before refactoring
4. Refactor with test safety net

**Strategy**:
1. Understand current behavior
2. Write tests for current behavior
3. Refactor
4. Ensure tests still pass

### Day 4: Modernization & Best Practices
**Topics**:
- Update to modern syntax
- Improve error handling
- Add type hints/annotations
- Implement design patterns

**Exercises**:
1. Update to modern language features
2. Add comprehensive error handling
3. Include type information
4. Apply appropriate design patterns

### Day 5: Presentation & Graduation
**Topics**:
- Project presentation
- Lessons learned
- Next steps with Copilot
- Bootcamp retrospective

**Activities**:
1. Present refactoring project
2. Share before/after metrics
3. Complete final reflection
4. Bootcamp graduation

## Key Concepts

### Code Smells to Address

**Bloaters**:
- Long methods
- Large classes
- Long parameter lists
- Data clumps

**Object-Orientation Abusers**:
- Switch statements
- Refused bequest
- Alternative classes

**Change Preventers**:
- Divergent change
- Shotgun surgery
- Parallel inheritance

**Dispensables**:
- Comments (excessive)
- Duplicate code
- Dead code
- Speculative generality

**Couplers**:
- Feature envy
- Inappropriate intimacy
- Message chains

### Refactoring Strategies

1. **Incremental Changes**: Small, safe steps
2. **Test-Driven**: Ensure tests pass
3. **Version Control**: Commit frequently
4. **Code Reviews**: Get feedback
5. **Performance**: Measure before optimizing

### Using Copilot for Refactoring

- Ask Copilot to explain complex code
- Generate refactoring suggestions
- Create tests for legacy code
- Update documentation
- Identify patterns and anti-patterns

## Lab Assignment

Complete `labs/week4-refactor-legacy/`:
1. Refactor `legacy/messy_module.py`
2. Add comprehensive tests
3. Improve code quality metrics
4. Document improvements

Deliverables:
- Refactored code
- Test suite
- Before/after comparison
- Final presentation

## Refactoring Checklist

Before considering refactoring complete:
- [ ] All tests passing
- [ ] Code smells addressed
- [ ] Documentation updated
- [ ] Code coverage >80%
- [ ] No functionality broken
- [ ] Performance maintained/improved
- [ ] Code review completed

## Metrics to Track

Compare before and after:
- **Lines of Code**: Reduction expected
- **Cyclomatic Complexity**: Should decrease
- **Test Coverage**: Should increase
- **Code Duplication**: Should decrease
- **Maintainability Index**: Should improve

## Final Project Presentation

Prepare a 10-minute presentation covering:
1. **Initial Assessment**: What you found
2. **Refactoring Strategy**: Your approach
3. **Challenges**: What was difficult
4. **Solutions**: How you solved problems
5. **Results**: Metrics and improvements
6. **Learnings**: Key takeaways

## Resources

- [Refactoring Catalog](https://refactoring.com/)
- [Clean Code Principles](org-standards/coding-standards.md)
- Legacy code: `legacy/messy_module.py`

## Post-Bootcamp

### Continue Your Copilot Journey
- Join GitHub Copilot community
- Share your learnings
- Mentor new users
- Explore advanced features

### Apply to Daily Work
- Integrate Copilot into workflow
- Track productivity improvements
- Share best practices with team
- Contribute to organization standards

### Stay Updated
- Follow GitHub Copilot updates
- Try new features
- Participate in feedback programs
- Share success stories

## Congratulations! 🎉

You've completed the GitHub Copilot Bootcamp! You now have the skills to:
- Use Copilot effectively in daily development
- Write better code faster
- Maintain security awareness
- Implement DevOps best practices
- Refactor and improve legacy code

Keep coding with Copilot and share your success!
