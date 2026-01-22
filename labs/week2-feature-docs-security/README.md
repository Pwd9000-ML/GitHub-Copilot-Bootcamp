# Week 2 Lab: Features, Documentation & Security

## Overview

Build on your Week 1 project by implementing features with security awareness and generating comprehensive documentation.

## Objectives

- Implement new features using Copilot
- Write security-aware code
- Generate API and code documentation
- Implement input validation and sanitization
- Pass security scans

## Prerequisites

- Completed Week 1 lab
- GitHub Copilot configured
- Understanding of common security vulnerabilities

## Lab Exercises

### Exercise 1: Feature Implementation

Add the following features to your project:

**For Web APIs:**
- [ ] User authentication (JWT or similar)
- [ ] CRUD endpoints for a new resource
- [ ] Filtering and pagination
- [ ] Error handling with proper status codes

**For CLI Applications:**
- [ ] User preferences/settings
- [ ] Data export/import
- [ ] Search functionality
- [ ] Configuration file support

### Exercise 2: Security Implementation

Implement security measures:

1. **Input Validation**
   - [ ] Validate all user inputs
   - [ ] Use schema validation (Zod, Joi, etc.)
   - [ ] Return clear validation errors

2. **Security Measures**
   - [ ] Prevent SQL injection
   - [ ] Prevent XSS attacks
   - [ ] Sanitize user inputs
   - [ ] Secure password hashing (if applicable)
   - [ ] Rate limiting (if API)

3. **Secrets Management**
   - [ ] No hardcoded secrets
   - [ ] Use environment variables
   - [ ] Create .env.example file

### Exercise 3: Documentation Generation

Generate comprehensive documentation:

1. **API Documentation** (if applicable)
   - [ ] OpenAPI/Swagger spec
   - [ ] Request/response examples
   - [ ] Error code documentation

2. **Code Documentation**
   - [ ] JSDoc/docstrings for all functions
   - [ ] Inline comments for complex logic
   - [ ] Architecture documentation

3. **User Documentation**
   - [ ] Updated README
   - [ ] Usage examples
   - [ ] Troubleshooting guide

### Exercise 4: Security Testing

1. **Run Security Scans**
   - [ ] Enable CodeQL (if not already enabled)
   - [ ] Run dependency vulnerability scan
   - [ ] Check for exposed secrets

2. **Write Security Tests**
   - [ ] Test input validation
   - [ ] Test authentication/authorization
   - [ ] Test error handling

## Security Checklist

Before submitting, verify:

- [ ] Input validation implemented for all user inputs
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] Sensitive data is encrypted/hashed
- [ ] Secrets not committed to repository
- [ ] Dependencies are up to date
- [ ] Security tests pass
- [ ] CodeQL analysis passes

## Deliverables

Submit via Pull Request:

1. **Enhanced Project**
   - New features implemented
   - Security measures in place
   - All tests passing

2. **Documentation**
   - API documentation (if applicable)
   - Updated README
   - Code documentation

3. **Security Report**
   - CodeQL results
   - Dependency scan results
   - Security test results

4. **Reflection**
   - Submit Week 2 lab issue
   - Include security learnings
   - Share effective security prompts

## Using Copilot for Security

### Security Prompts

```typescript
// Implement input validation for user registration with:
// - Email format validation (RFC 5322 compliant)
// - Password strength check (min 8 chars, uppercase, number, special char)
// - Username validation (3-30 alphanumeric characters)
// - Sanitize inputs to prevent XSS
// Return detailed validation errors
```

```python
# Create a secure password hashing function with:
# - bcrypt algorithm
# - Configurable salt rounds
# - Error handling
# - Type hints
# Include a verification function
```

### Security Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Security Guidelines](../../docs/org-standards/security-guidelines.md)
- [Security Prompt Library](../../prompts/prompt-library.md#security)

## Evaluation Criteria

- **Feature Quality** (25%): Are features well-implemented?
- **Security** (30%): Are security measures comprehensive?
- **Documentation** (25%): Is documentation complete and clear?
- **Testing** (15%): Are security tests thorough?
- **Code Quality** (5%): Is code maintainable?

## Resources

- [Week 2 Materials](../../docs/week-2.md)
- [Security Guidelines](../../docs/org-standards/security-guidelines.md)
- [Documentation Style](../../docs/org-standards/documentation-style.md)
- [Prompt Library - Security](../../prompts/prompt-library.md#security)

## Common Pitfalls

❌ **Don't**: Trust user input without validation  
✅ **Do**: Validate and sanitize all inputs

❌ **Don't**: Use string concatenation for SQL queries  
✅ **Do**: Use parameterized queries

❌ **Don't**: Store passwords in plain text  
✅ **Do**: Hash passwords with bcrypt or similar

❌ **Don't**: Expose internal error details to users  
✅ **Do**: Log detailed errors, return generic messages

## Next Steps

After completing this lab:
1. Submit your PR with security checklist completed
2. Review CodeQL findings
3. Complete daily reflections
4. Prepare for Week 3: DevOps & Testing

Stay secure! 🔒
