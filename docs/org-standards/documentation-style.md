# Documentation Style Guide

This guide defines standards for documentation in our organization. Follow these guidelines when writing or generating documentation with GitHub Copilot.

## General Principles

### Write for Your Audience
- Understand who will read the documentation
- Use appropriate technical level
- Define acronyms and jargon
- Provide context and examples

### Keep It Current
- Update docs with code changes
- Review documentation regularly
- Remove outdated information
- Version documentation with code

### Make It Accessible
- Use clear, simple language
- Provide examples
- Include visual aids when helpful
- Use proper formatting

## Documentation Types

### 1. Code Comments

#### When to Comment
- Complex algorithms
- Business logic decisions
- Non-obvious code
- Workarounds or hacks
- Public APIs

#### When NOT to Comment
- Obvious code
- Self-explanatory names
- Redundant explanations

**Good Comments**:
```typescript
// Calculate tax using jurisdiction-specific rules
// See: https://docs.example.com/tax-calculation
function calculateTax(amount: number, jurisdiction: string): number {
  // Special handling for EU VAT reverse charge
  if (jurisdiction.startsWith('EU-') && isBusinessCustomer) {
    return 0;
  }
  
  return amount * getTaxRate(jurisdiction);
}
```

**Bad Comments**:
```typescript
// This function adds two numbers
function add(a: number, b: number): number {
  return a + b; // Return the sum
}
```

### 2. Function/Method Documentation

Use standardized documentation formats:

**TypeScript/JavaScript (JSDoc)**:
```typescript
/**
 * Retrieves a user by their unique identifier.
 * 
 * @param userId - The unique identifier of the user
 * @param includeDeleted - Whether to include soft-deleted users
 * @returns Promise resolving to the user object
 * @throws {NotFoundError} When user doesn't exist
 * @throws {DatabaseError} When database query fails
 * 
 * @example
 * ```typescript
 * const user = await getUserById('123', false);
 * console.log(user.email);
 * ```
 */
async function getUserById(
  userId: string,
  includeDeleted: boolean = false
): Promise<User> {
  // Implementation
}
```

**Python (docstrings)**:
```python
def calculate_discount(price: float, discount_code: str) -> float:
    """Calculate the final price after applying a discount code.
    
    This function validates the discount code and applies the appropriate
    discount percentage to the original price.
    
    Args:
        price: The original price before discount
        discount_code: The promotional code to apply
        
    Returns:
        The final price after discount is applied
        
    Raises:
        ValueError: If price is negative
        InvalidDiscountError: If discount code is invalid or expired
        
    Example:
        >>> calculate_discount(100.0, "SAVE20")
        80.0
    """
    # Implementation
```

**C# (XML comments)**:
```csharp
/// <summary>
/// Processes a payment transaction.
/// </summary>
/// <param name="amount">The amount to charge in USD</param>
/// <param name="paymentMethod">The payment method to use</param>
/// <returns>A task that represents the asynchronous operation.
/// The task result contains the transaction ID.</returns>
/// <exception cref="PaymentException">Thrown when payment processing fails</exception>
/// <example>
/// <code>
/// var transactionId = await ProcessPayment(99.99m, paymentMethod);
/// </code>
/// </example>
public async Task<string> ProcessPayment(
    decimal amount,
    PaymentMethod paymentMethod)
{
    // Implementation
}
```

### 3. README Files

Every project should have a comprehensive README with these sections:

**Required Sections**:
```markdown
# Project Name

Brief description of what this project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
npm install
```

## Usage

```typescript
import { feature } from 'project';

const result = feature();
```

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| apiKey | string | - | Your API key |
| timeout | number | 5000 | Request timeout in ms |

## API Documentation

See [API.md](./API.md) for detailed API documentation.

## Contributing

Please read [CONTRIBUTING.md](../CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
```

**Optional Sections**:
- Prerequisites
- Development Setup
- Testing
- Deployment
- Troubleshooting
- FAQ
- Changelog
- Acknowledgments

### 4. API Documentation

Document all public APIs comprehensively:

**REST API Example**:
```markdown
## GET /api/users/:id

Retrieves a user by ID.

### Parameters

- `id` (path, required): User ID (UUID format)

### Query Parameters

- `include` (optional): Comma-separated list of relations to include
  - Possible values: `posts`, `comments`, `profile`
  - Example: `?include=posts,profile`

### Headers

- `Authorization` (required): Bearer token
- `Accept`: `application/json`

### Response

**Success (200 OK)**:
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "email": "user@example.com",
  "name": "John Doe",
  "createdAt": "2024-01-01T00:00:00Z"
}
```

**Error (404 Not Found)**:
```json
{
  "error": "User not found",
  "code": "USER_NOT_FOUND"
}
```

### Example

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     https://api.example.com/users/123e4567-e89b-12d3-a456-426614174000
```
```

### 5. Architecture Documentation

Document high-level architecture:

**Example**:
```markdown
# Architecture Overview

## System Components

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Client    │─────▶│   API       │─────▶│  Database   │
│  (React)    │      │ (Node.js)   │      │ (PostgreSQL)│
└─────────────┘      └─────────────┘      └─────────────┘
                            │
                            ▼
                     ┌─────────────┐
                     │   Cache     │
                     │   (Redis)   │
                     └─────────────┘
```

## Data Flow

1. Client sends request to API
2. API checks cache
3. If cache miss, query database
4. Update cache with result
5. Return response to client

## Key Design Decisions

### Why PostgreSQL?
- ACID compliance required
- Complex relational data
- Mature ecosystem

### Why Redis?
- Fast read access
- Session storage
- Rate limiting
```

### 6. User Guides

Write step-by-step guides for end users:

**Example**:
```markdown
# How to Create a New Project

This guide walks you through creating a new project.

## Prerequisites

- Active account
- Organization membership
- Create project permission

## Steps

1. **Navigate to Projects**
   
   Click "Projects" in the main navigation.

2. **Click "New Project"**
   
   Find the "New Project" button in the top right corner.

3. **Fill in Project Details**
   
   - **Name**: Choose a descriptive name
   - **Description**: Explain the project's purpose
   - **Visibility**: Select Public or Private

4. **Configure Settings** (Optional)
   
   - Enable issues
   - Enable wiki
   - Set default branch name

5. **Click "Create Project"**
   
   Your project is now created!

## Next Steps

- [Add team members](./add-team-members.md)
- [Configure webhooks](./webhooks.md)
- [Set up CI/CD](./cicd-setup.md)

## Troubleshooting

### Error: "Name already exists"
The project name must be unique within your organization. Try a different name.

### Error: "Permission denied"
Contact your organization admin to request project creation permissions.
```

## Formatting Guidelines

### Markdown Best Practices

**Headings**:
```markdown
# H1 - Document Title (one per document)
## H2 - Major Sections
### H3 - Subsections
#### H4 - Minor Subsections
```

**Lists**:
```markdown
- Unordered lists for non-sequential items
- Use consistent bullet style
- Keep items parallel in structure

1. Ordered lists for sequential steps
2. Start numbering at 1
3. Use consistent numbering style
```

**Code Blocks**:
````markdown
```language
// Always specify language for syntax highlighting
const example = "code";
```
````

**Links**:
```markdown
[Link text](url) - Descriptive link text
[Relative link](./other-doc.md) - For internal docs
```

**Tables**:
```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

### Writing Style

**Be Concise**:
- Short sentences
- Active voice
- Clear language
- Avoid jargon

**Be Consistent**:
- Use same terms throughout
- Follow naming conventions
- Consistent formatting
- Consistent structure

**Be Helpful**:
- Provide examples
- Anticipate questions
- Include troubleshooting
- Link to related docs

## Documentation with Copilot

### Generating Documentation

**Prompt Examples**:
```typescript
// Generate JSDoc documentation for this function
function complexCalculation(input: ComplexInput): Result {
  // implementation
}

// Ask Copilot:
// "Add comprehensive JSDoc with examples"
```

### Best Practices

1. **Review Generated Docs**: Always verify accuracy
2. **Add Context**: Supplement with business logic explanations
3. **Include Examples**: Add real-world usage examples
4. **Update Regularly**: Keep docs in sync with code

## Documentation Checklist

Before considering documentation complete:

- [ ] All public APIs documented
- [ ] README is comprehensive
- [ ] Examples are provided
- [ ] Code comments where needed
- [ ] Architecture documented
- [ ] Setup instructions clear
- [ ] Troubleshooting section included
- [ ] Links are valid
- [ ] Spelling and grammar checked
- [ ] Formatted consistently

## Tools

### Recommended Tools
- **Documentation Generators**:
  - TypeDoc (TypeScript)
  - Sphinx (Python)
  - Javadoc (Java)
  - Doxygen (C/C++)

- **Linters**:
  - markdownlint
  - write-good
  - vale

- **Diagrams**:
  - Mermaid
  - PlantUML
  - Draw.io

### VS Code Extensions
- Markdown All in One
- Markdown Preview Enhanced
- Code Spell Checker
- markdownlint

## Documentation Review

### What to Review
- Accuracy
- Completeness
- Clarity
- Examples work
- Links are valid
- Formatting consistent

### Review Checklist
- [ ] Technical accuracy verified
- [ ] Examples tested
- [ ] Links checked
- [ ] Spelling checked
- [ ] Grammar checked
- [ ] Formatting consistent

## Maintaining Documentation

### When to Update
- Code changes
- API changes
- Bug fixes
- Feature additions
- Deprecations

### Documentation Debt
- Track outdated docs
- Regular review cycles
- Assign ownership
- Prioritize updates

## Examples

### Good Documentation Example
See `sample-app/backend-ts/README.md` for a complete example of well-documented code.

### Documentation Templates
- [API Documentation Template](./templates/api-docs.md)
- [User Guide Template](./templates/user-guide.md)
- [Architecture Doc Template](./templates/architecture.md)

## Resources

- [Google Developer Documentation Style Guide](https://developers.google.com/style)
- [Microsoft Writing Style Guide](https://docs.microsoft.com/style-guide/)
- [GitLab Documentation Guidelines](https://docs.gitlab.com/ee/development/documentation/)
- [Write the Docs](https://www.writethedocs.org/)

---

Good documentation is a gift to your future self and your teammates!
