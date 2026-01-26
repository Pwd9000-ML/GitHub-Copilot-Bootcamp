# Week 4 Prompts: Refactoring, Quality, and Security

A comprehensive collection of prompts for Week 4 topics covering legacy code refactoring, quality standards enforcement, and ethical/security considerations.

---

## Quick Navigation

- [Refactoring Prompts](#refactoring-prompts)
- [Quality Standards Prompts](#quality-standards-prompts)
- [Security Audit Prompts](#security-audit-prompts)
- [Ethical AI Prompts](#ethical-ai-prompts)
- [Code Review Prompts](#code-review-prompts)

---

## Refactoring Prompts

### Legacy Code Analysis

```text
Analyse this legacy code and provide:
1. A summary of what it does
2. Identified code smells (list each with line numbers)
3. Technical debt assessment
4. Dependencies and coupling issues
5. Recommended refactoring priority

[paste legacy code]
```

### Characterisation Test Generation

```text
Generate characterisation tests for this legacy function:
- Capture current behaviour (even if buggy)
- Cover happy path and edge cases
- Document observed behaviour in test names
- Mock external dependencies
- Use [Jest/pytest/JUnit] framework

Purpose: Enable safe refactoring by detecting behaviour changes.

[paste function code]
```

### Incremental Refactoring - Extract Method

```text
Extract a method from this code section:
- Create a well-named function for [specific logic]
- Use meaningful parameter names
- Add JSDoc/docstring documentation
- Ensure no side effects in extracted method
- Keep original function calls intact

[paste code with highlighted section]
```

### Rename for Clarity

```text
Improve variable and function names in this code:
- Replace single-letter variables with descriptive names
- Use domain terminology
- Follow [camelCase/snake_case] convention
- Add comments explaining any non-obvious names
- Provide a mapping of old → new names

[paste code]
```

### Modernise Syntax

```text
Modernise this [JavaScript/Python/Java] code to current standards:
- Replace deprecated patterns
- Use modern language features ([ES2022/Python 3.11/Java 17])
- Apply destructuring where beneficial
- Use appropriate iteration methods (map, filter, reduce)
- Maintain identical functionality

[paste legacy code]
```

### Remove Code Duplication

```text
Identify and eliminate duplication in this code:
1. Find repeated patterns (list each)
2. Extract common logic into reusable functions
3. Use abstraction to handle variations
4. Ensure tests still pass after changes

[paste code]
```

### Simplify Conditionals

```text
Refactor these nested conditionals:
- Reduce nesting depth to maximum 2 levels
- Use early returns for guard clauses
- Apply polymorphism if appropriate
- Improve readability without changing logic

Current nesting depth: [X levels]
Target: Maximum 2 levels

[paste nested conditional code]
```

---

## Quality Standards Prompts

### Generate Coding Standards

```text
Create a coding standards document for [TypeScript/Python/Java]:
- Naming conventions (variables, functions, classes, files)
- Code formatting rules
- Documentation requirements
- Error handling patterns
- Testing requirements
- Accessibility guidelines

Format as markdown suitable for .github/copilot-instructions.md
```

### Standards Compliance Check

```text
Check this code against our project standards:
1. Naming conventions: [camelCase for functions, PascalCase for classes]
2. Documentation: [All public APIs must have JSDoc]
3. Error handling: [No empty catch blocks]
4. Line length: [Max 100 characters]
5. Complexity: [Max cyclomatic complexity 10]

Report violations with line numbers and fixes.

[paste code]
```

### Generate ESLint/Linting Configuration

```text
Generate a [ESLint/Pylint/Checkstyle] configuration that enforces:
- [List your rules]
- No unused variables
- Consistent formatting
- Required documentation
- Security-focused rules

Include explanation comments for each rule.
```

### Pre-Commit Hook Setup

```text
Create a pre-commit hook configuration that:
1. Runs linting and fails on errors
2. Auto-formats code with Prettier/Black
3. Runs type checking
4. Scans for secrets and credentials
5. Validates commit message format
6. Runs tests for changed files

Use [husky/pre-commit/Git hooks] setup.
```

### Documentation Generation

```text
Generate comprehensive documentation for this module:
- Module overview (what it does, when to use it)
- Installation/setup instructions
- Public API reference with examples
- Error handling guidance
- Configuration options table

[paste module code]
```

### Code Metrics Analysis

```text
Analyse these quality metrics for the given code:
- Cyclomatic complexity (target: <10 per function)
- Cognitive complexity (target: <15)
- Lines per function (target: <30)
- Nesting depth (target: <4)
- Test coverage percentage

Flag any metrics exceeding targets with specific recommendations.

[paste code]
```

---

## Security Audit Prompts

### Comprehensive Security Review

```text
Perform a security audit on this code checking for:
1. Injection vulnerabilities (SQL, command, XSS, LDAP)
2. Authentication/authorisation flaws
3. Cryptographic weaknesses
4. Sensitive data exposure
5. Input validation gaps
6. Error handling issues
7. Insecure dependencies
8. Configuration vulnerabilities

Severity ratings: CRITICAL / HIGH / MEDIUM / LOW
Provide remediation for each finding.

[paste code]
```

### SQL Injection Prevention

```text
Review this database code for SQL injection:
- Identify injection points
- Show example attack payloads
- Provide parameterised query alternatives
- Add input validation

Current code:
[paste database query code]
```

### Secret Detection

```text
Scan this code for exposed secrets:
- API keys and tokens
- Database credentials
- Private keys
- Configuration passwords
- OAuth secrets
- AWS/Azure/GCP credentials

Provide regex patterns for automated detection.

[paste code]
```

### Input Validation Generator

```text
Generate input validation for this [API endpoint/function]:
- Validate all user inputs
- Sanitise for XSS prevention
- Check data types and ranges
- Validate file uploads if applicable
- Return clear error messages

Endpoint/Function:
[paste code]
```

### Security Test Generation

```text
Generate security test cases for this [API/function]:
- SQL injection attempts
- XSS payloads
- Invalid/malformed inputs
- Boundary value attacks
- Authentication bypass attempts
- Rate limiting tests

Use [Jest/pytest/JUnit] with security testing library.

[paste code]
```

### Dependency Security Check

```text
Review these dependencies for security:
1. Check for known vulnerabilities
2. Identify outdated packages
3. Flag abandoned/unmaintained packages
4. Recommend secure alternatives

Package file:
[paste package.json/requirements.txt/pom.xml]
```

### Secure Code Transformation

```text
Transform this code to be secure:
Original (insecure):
[paste insecure code]

Requirements:
- Fix all identified vulnerabilities
- Add input validation
- Use secure coding patterns
- Include security comments explaining changes
```

---

## Ethical AI Prompts

### Bias Detection in Code

```text
Review this code for potential bias:
- Gender assumptions
- Cultural/regional assumptions
- Accessibility barriers
- Language/naming stereotypes
- Default values that exclude groups

Suggest inclusive alternatives for each issue.

[paste code]
```

### Inclusive Code Generation

```text
Generate code for [feature] that is:
- Gender-inclusive (no binary assumptions)
- Culturally neutral (international name/date formats)
- Accessible (ARIA labels, keyboard navigation)
- Language-agnostic (supports RTL, multiple character sets)
- Localisation-ready
```

### AI Usage Documentation

```text
Create an AI-assisted code documentation template:
- AI tool used
- Prompts that generated the code
- Human modifications made
- Security review status
- Test coverage verification
```

### Responsible AI Checklist

```text
Generate a checklist for responsible AI-assisted development:
- Pre-acceptance verification steps
- Security review requirements
- Bias checking procedures
- Documentation requirements
- Disclosure guidelines
```

---

## Code Review Prompts

### Senior Developer Review

```text
Perform a senior developer code review:
1. Logic correctness - Does it do what it should?
2. Edge cases - What could break it?
3. Performance - Any inefficiencies?
4. Security - Any vulnerabilities?
5. Maintainability - Will it be easy to modify?
6. Testing - Is coverage adequate?
7. Documentation - Is it clear?

Be critical. Provide specific line references and fixes.

[paste code]
```

### SOLID Principles Check

```text
Analyse this code against SOLID principles:
- Single Responsibility: One reason to change?
- Open/Closed: Extendable without modification?
- Liskov Substitution: Subtypes substitutable?
- Interface Segregation: Focused interfaces?
- Dependency Inversion: Depends on abstractions?

Identify violations and provide refactoring suggestions.

[paste code]
```

### Clean Code Review

```text
Review this code against Clean Code principles:
- Meaningful names
- Small functions (one thing)
- No side effects
- DRY (Don't Repeat Yourself)
- Error handling
- Comments (explain why, not what)
- Formatting consistency

Score each principle 1-5 with justification.

[paste code]
```

### Pull Request Review Template

```text
Generate a PR review for this code change:

Checklist:
- [ ] Logic is correct
- [ ] Tests are adequate
- [ ] No security issues
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Performance acceptable

Summary: [Approve/Request Changes/Comment]
Feedback: [Specific comments with line refs]

[paste code diff]
```

---

## Combination Prompts

### Full Refactoring Workflow

```text
Plan a complete refactoring for this legacy code:

Phase 1 - Prepare
- Add characterisation tests
- Document current behaviour

Phase 2 - Secure
- Remove hardcoded secrets
- Fix injection vulnerabilities
- Add input validation

Phase 3 - Modernise  
- Update syntax to modern standards
- Apply SOLID principles
- Improve naming

Phase 4 - Optimise
- Address performance issues
- Remove duplication
- Simplify complexity

Provide specific prompts for each phase step.

[paste legacy code]
```

### Quality Gate Implementation

```text
Create a complete quality gate for CI/CD:
1. Linting configuration
2. Security scanning setup
3. Test coverage requirements
4. Documentation checks
5. Performance benchmarks

Include GitHub Actions workflow YAML.
```

---

## Prompt Engineering Tips for Week 4

| Technique | Example |
|-----------|---------|
| **Be specific about standards** | "Follow PEP 8 style guide" |
| **Provide context** | "This is a financial application requiring strict security" |
| **Request explanations** | "Explain why each change improves security" |
| **Ask for alternatives** | "Provide 2-3 approaches to fixing this issue" |
| **Specify output format** | "Return as a markdown table with severity ratings" |
| **Include constraints** | "Must maintain backward compatibility" |

---

## Quick Reference Commands

```text
# Analyse legacy code
"Analyse this code for refactoring opportunities"

# Security audit
"Perform a security audit and prioritise findings"

# Generate tests
"Generate tests to capture current behaviour before refactoring"

# Apply standards
"Refactor to follow [standard name] conventions"

# Document code
"Generate comprehensive documentation with usage examples"

# Review code
"Review as a senior developer - be critical and specific"
```

---
