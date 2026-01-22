# Week 4 Lab: Refactoring Legacy Code

## Overview

Apply all your GitHub Copilot skills to refactor the messy legacy code in [legacy/messy_module.py](../../legacy/messy_module.py).

This is your final project! Demonstrate mastery of Copilot-assisted development.

## Objectives

- Analyze and understand legacy code
- Create tests for existing behavior
- Refactor code systematically
- Improve code quality metrics
- Apply all bootcamp learnings

## Prerequisites

- Completed Week 1, 2, and 3 labs
- Understanding of refactoring patterns
- Test-driven refactoring approach

## The Challenge

The file `legacy/messy_module.py` is intentionally terrible code. It has:

- 🐛 Unclear naming
- 🔀 Complex nested logic
- 📦 Code duplication
- 🔢 Magic numbers
- 🚨 Security vulnerabilities
- 📝 Poor documentation
- 🎯 Multiple responsibilities
- 💥 No error handling
- 🧪 No tests
- 🎨 Inconsistent style

**Your mission**: Transform it into production-quality code!

## Lab Exercises

### Exercise 1: Analysis & Planning

1. **Understand the Code**
   - [ ] Read through messy_module.py
   - [ ] Use Copilot Chat to explain functions
   - [ ] Document what each function does
   - [ ] Identify code smells

2. **Create Refactoring Plan**
   - [ ] List all issues found
   - [ ] Prioritize improvements
   - [ ] Define success criteria
   - [ ] Estimate effort

### Exercise 2: Test Creation

**Critical**: Write tests BEFORE refactoring!

1. **Characterization Tests**
   - [ ] Test current behavior
   - [ ] Cover all functions
   - [ ] Document assumptions
   - [ ] Ensure tests pass

2. **Test Coverage**
   - [ ] Achieve >80% coverage
   - [ ] Test edge cases
   - [ ] Test error conditions
   - [ ] Document test scenarios

### Exercise 3: Systematic Refactoring

Refactor in small, safe steps:

1. **Naming & Clarity**
   - [ ] Rename unclear variables
   - [ ] Rename unclear functions
   - [ ] Use descriptive names
   - [ ] Run tests after each change

2. **Extract Functions**
   - [ ] Break down complex functions
   - [ ] Single responsibility
   - [ ] Reduce nesting
   - [ ] Run tests after each change

3. **Remove Duplication**
   - [ ] Identify duplicate code
   - [ ] Extract common logic
   - [ ] Create helper functions
   - [ ] Run tests after each change

4. **Fix Magic Numbers**
   - [ ] Extract constants
   - [ ] Use named constants
   - [ ] Document meanings
   - [ ] Run tests after each change

5. **Security Fixes**
   - [ ] Fix SQL injection risk
   - [ ] Remove eval() usage
   - [ ] Proper file handling
   - [ ] Input validation

6. **Error Handling**
   - [ ] Add try-except blocks
   - [ ] Handle edge cases
   - [ ] Provide clear errors
   - [ ] Document exceptions

7. **Documentation**
   - [ ] Add docstrings
   - [ ] Add type hints
   - [ ] Document parameters
   - [ ] Add usage examples

### Exercise 4: Quality Verification

1. **Code Quality Metrics**
   - [ ] Measure complexity (before/after)
   - [ ] Measure lines of code
   - [ ] Measure test coverage
   - [ ] Document improvements

2. **Final Checks**
   - [ ] All tests passing
   - [ ] Linting passes
   - [ ] Type checking passes
   - [ ] Security scans pass
   - [ ] Documentation complete

## Refactoring Checklist

Complete transformation:

- [ ] All functions have clear names
- [ ] All variables have descriptive names
- [ ] No function longer than 30 lines
- [ ] No nesting deeper than 3 levels
- [ ] No duplicated code
- [ ] No magic numbers
- [ ] All security issues fixed
- [ ] Comprehensive error handling
- [ ] Type hints added
- [ ] Docstrings added
- [ ] >80% test coverage
- [ ] All tests passing
- [ ] Consistent naming convention
- [ ] Removed commented code
- [ ] Removed unused functions

## Deliverables

Submit via Pull Request:

1. **Refactored Code**
   - Clean, readable code
   - Well-organized structure
   - Production quality

2. **Test Suite**
   - Comprehensive tests
   - High coverage
   - All passing

3. **Metrics Report**
   - Before/after comparison
   - Complexity metrics
   - Coverage metrics
   - Lines of code

4. **Documentation**
   - Code documentation
   - Refactoring summary
   - Design decisions

5. **Presentation**
   - 10-minute presentation
   - Before/after demo
   - Key learnings
   - Metrics and improvements

6. **Final Reflection**
   - Submit Week 4 lab issue
   - Overall bootcamp reflection
   - Copilot effectiveness rating
   - Future plans with Copilot

## Using Copilot for Refactoring

### Analysis Prompts

```
Explain what this function does:
[paste function]

Identify code smells in this code:
[paste code]

Suggest refactoring improvements for this function:
[paste function]
```

### Refactoring Prompts

```python
# Refactor this function to:
# - Use descriptive variable names
# - Extract nested logic into separate functions
# - Add error handling
# - Add type hints and docstring
# - Follow PEP 8
```

```python
# Create tests for this function covering:
# - Valid inputs
# - Edge cases (empty lists, None values)
# - Error conditions
# - Different data types
# Use pytest framework
```

## Evaluation Criteria

- **Code Quality** (30%): Is refactored code clean and maintainable?
- **Testing** (25%): Is test coverage comprehensive?
- **Metrics Improvement** (20%): Are quality metrics improved?
- **Presentation** (15%): Is presentation clear and insightful?
- **Process** (10%): Was refactoring systematic and safe?

## Before/After Template

Document your transformation:

```markdown
## Refactoring Summary

### Before
- Lines of Code: 500
- Functions: 15
- Average Complexity: 12
- Test Coverage: 0%
- Code Smells: 47

### After
- Lines of Code: 350
- Functions: 25
- Average Complexity: 4
- Test Coverage: 92%
- Code Smells: 0

### Key Improvements
1. Extracted 10 new focused functions
2. Eliminated all code duplication
3. Fixed security vulnerabilities
4. Added comprehensive error handling
5. 100% type hint coverage
```

## Resources

- [Week 4 Materials](../../docs/week-4.md)
- [Coding Standards](../../docs/org-standards/coding-standards.md)
- [Refactoring Catalog](https://refactoring.com/)
- [Legacy Code](../../legacy/messy_module.py)

## Presentation Guidelines

Prepare a 10-minute presentation:

1. **Introduction** (1 min)
   - Project overview
   - Initial assessment

2. **Challenges** (2 min)
   - Main problems identified
   - Difficult decisions

3. **Approach** (3 min)
   - Refactoring strategy
   - Use of Copilot
   - Step-by-step process

4. **Results** (3 min)
   - Metrics comparison
   - Code examples
   - Improvements

5. **Learnings** (1 min)
   - Key takeaways
   - Future applications

## Final Tips

✅ **Do**:
- Commit after each safe refactoring
- Run tests constantly
- Make small, incremental changes
- Use Copilot for suggestions
- Document your process

❌ **Don't**:
- Make large changes at once
- Skip running tests
- Change behavior without tests
- Trust Copilot blindly
- Rush the process

## Congratulations! 🎉

This is your final lab. Show everything you've learned:
- Effective Copilot usage
- Security awareness
- Testing practices
- Clean code principles
- DevOps automation

Make it count! This is your bootcamp finale! 🚀
