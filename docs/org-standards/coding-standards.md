# Organization Coding Standards

This document outlines the coding standards and best practices for our organization. Use these guidelines when writing code with GitHub Copilot.

## General Principles

### Code Quality
- Write clean, readable, and maintainable code
- Follow DRY (Don't Repeat Yourself) principle
- Keep functions small and focused (single responsibility)
- Use meaningful names for variables, functions, and classes
- Write self-documenting code

### Code Style
- Consistency is key - follow existing patterns
- Use consistent indentation (spaces preferred)
- Keep line length reasonable (80-120 characters)
- Use clear and descriptive comments when needed
- Avoid commented-out code

## Language-Specific Standards

### JavaScript/TypeScript
- Use ES6+ features
- Prefer `const` over `let`, avoid `var`
- Use async/await over raw promises
- Include type definitions (TypeScript)
- Use meaningful interface names

**Example**:
```typescript
// Good
async function fetchUserData(userId: string): Promise<User> {
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
}

// Avoid
var getUser = function(id) {
  return fetch('/api/users/' + id).then(r => r.json());
}
```

### Python
- Follow PEP 8 style guide
- Use type hints for function signatures
- Use descriptive variable names (snake_case)
- Include docstrings for classes and functions
- Prefer list comprehensions over loops when appropriate

**Example**:
```python
# Good
def calculate_total_price(items: list[Item]) -> float:
    """Calculate the total price of items including tax."""
    return sum(item.price * (1 + item.tax_rate) for item in items)

# Avoid
def calc(i):
    t = 0
    for x in i:
        t = t + x.price * (1 + x.tax_rate)
    return t
```

### C#
- Follow Microsoft's C# Coding Conventions
- Use PascalCase for public members
- Use camelCase for private fields
- Include XML documentation comments
- Use LINQ where appropriate

### Java
- Follow Google Java Style Guide
- Use camelCase for methods and variables
- Use PascalCase for classes
- Keep methods under 30 lines when possible
- Use JavaDoc for public APIs

## Project Structure

### Organize by Feature
```
src/
├── features/
│   ├── auth/
│   ├── users/
│   └── products/
├── shared/
│   ├── utils/
│   ├── models/
│   └── services/
└── config/
```

### Separate Concerns
- Models/Entities
- Services/Business Logic
- Controllers/Routes
- Utilities/Helpers
- Configuration

## Naming Conventions

### Variables
- Use descriptive names: `userCount` not `uc`
- Boolean variables: `isActive`, `hasPermission`, `canEdit`
- Arrays/Lists: plural names `users`, `products`

### Functions/Methods
- Start with verbs: `getUserById`, `calculateTotal`, `validateInput`
- Be specific: `fetchUserFromDatabase` vs. `getUser`
- Avoid generic names: `process`, `handle`, `manage`

### Classes/Types
- Use nouns: `User`, `Product`, `OrderService`
- Be specific: `UserRepository` vs. `Repository`
- Avoid abbreviations: `Customer` not `Cust`

## Error Handling

### Always Handle Errors
```typescript
// Good
try {
  const data = await fetchData();
  return processData(data);
} catch (error) {
  logger.error('Failed to process data', error);
  throw new DataProcessingError('Unable to process data', { cause: error });
}

// Avoid
const data = await fetchData(); // No error handling
return processData(data);
```

### Provide Context
- Include relevant information in error messages
- Use custom error types
- Log errors appropriately
- Don't swallow exceptions

## Testing Standards

### Write Tests First (TDD)
- Write tests before implementation
- Test behavior, not implementation
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)

### Test Coverage
- Aim for >80% coverage
- Test edge cases and error conditions
- Test happy path and sad path
- Mock external dependencies

### Test Naming
```typescript
// Good
describe('UserService', () => {
  it('should return user when valid ID is provided', async () => {
    // test implementation
  });
  
  it('should throw error when user is not found', async () => {
    // test implementation
  });
});
```

## Documentation

### Code Documentation
- Document public APIs
- Explain "why", not "what"
- Keep documentation close to code
- Update docs with code changes

### README Standards
Every project should include:
- Project description
- Installation instructions
- Usage examples
- Configuration options
- Contributing guidelines

## Version Control

### Commit Messages
Follow conventional commits format:
```
type(scope): subject

body

footer
```

**Types**: feat, fix, docs, style, refactor, test, chore

**Example**:
```
feat(auth): add OAuth2 authentication

Implement OAuth2 flow for third-party authentication
with support for Google and GitHub providers.

Closes #123
```

### Branch Naming
- `feature/description`
- `fix/bug-description`
- `refactor/component-name`
- `docs/update-readme`

## Code Review Guidelines

### What to Look For
- Code quality and maintainability
- Test coverage
- Security concerns
- Performance implications
- Documentation completeness

### Review Checklist
- [ ] Code follows organization standards
- [ ] Tests are included and passing
- [ ] Documentation is updated
- [ ] No security vulnerabilities
- [ ] Performance is acceptable
- [ ] Error handling is appropriate

## Using Copilot Effectively

### Provide Context
- Write detailed comments before code
- Include function signatures
- Reference related code
- Specify expected behavior

### Review Suggestions
- Don't accept blindly
- Verify correctness
- Check for security issues
- Ensure alignment with standards

### Iterate
- Refine prompts for better results
- Break complex tasks into steps
- Use Copilot Chat for explanations
- Combine manual and AI-assisted coding

## Performance Considerations

- Avoid premature optimization
- Profile before optimizing
- Consider time and space complexity
- Use appropriate data structures
- Cache when beneficial

## Accessibility

- Follow WCAG guidelines for web applications
- Include ARIA labels
- Support keyboard navigation
- Provide alternative text for images
- Ensure color contrast

## Maintenance

- Regular dependency updates
- Remove dead code
- Refactor technical debt
- Keep dependencies minimal
- Document breaking changes

## Resources

- [Clean Code by Robert C. Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/)
- Organization Wiki (internal)
- Team Style Guides (internal)

---

Remember: These standards are guidelines to improve code quality and team collaboration. Use your judgment and discuss with the team when standards need adjustment.
