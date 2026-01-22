# Prompt Library

A collection of effective prompts for GitHub Copilot to help you work more efficiently.

## Getting Started

### Basic Code Generation

```
Create a TypeScript interface for a User with id, email, name, and created date
```

```
Write a Python function to validate email addresses using regex
```

```
Generate a REST API endpoint to create a new product with validation
```

### Function Implementation

```
// Create a function that:
// - Takes an array of numbers
// - Filters out negative values
// - Returns the sum of remaining numbers
// - Handles empty arrays gracefully
```

```
// Implement a debounce function that:
// - Accepts a function and delay in milliseconds
// - Returns a debounced version of the function
// - Cancels pending executions on new calls
```

## Code Patterns

### Error Handling

```
Add comprehensive error handling to this function with:
- Try-catch block
- Specific error types
- Logging
- User-friendly error messages
```

```
Create a custom error class for API errors with:
- HTTP status code
- Error message
- Error code
- Original error cause
```

### Validation

```
Write input validation for user registration with:
- Email format check
- Password strength requirements (min 8 chars, 1 uppercase, 1 number)
- Username length (3-30 chars, alphanumeric)
- Return detailed validation errors
```

```
Create a schema validator using Zod for product creation with:
- Name (string, required, max 100 chars)
- Price (number, positive, max 2 decimals)
- Category (enum of allowed values)
- Description (optional string)
```

## Testing

### Unit Tests

```
Write unit tests for the getUserById function using Jest with:
- Test for successful user retrieval
- Test for non-existent user
- Test for database error
- Use mocks for database calls
```

```
Generate pytest tests for the calculate_discount function covering:
- Valid discount codes
- Expired discount codes
- Invalid discount codes
- Edge cases (zero price, negative price)
```

### Integration Tests

```
Create integration tests for the user registration endpoint:
- Test successful registration
- Test duplicate email handling
- Test invalid input validation
- Test password hashing
```

## Documentation

### Function Documentation

```
Add comprehensive JSDoc documentation to this function including:
- Description
- All parameters with types
- Return type and description
- Possible exceptions
- Usage example
```

```
Generate Python docstring following Google style for this class including:
- Class description
- Attributes
- Methods
- Examples
```

### README Generation

```
Create a comprehensive README for this project including:
- Project description
- Features
- Installation instructions
- Usage examples
- Configuration options
- Contributing guidelines
```

## Database

### Query Building

```
Write a SQL query to:
- Select users who registered in the last 30 days
- Include their total order count
- Order by registration date descending
- Limit to 100 results
```

```
Create a TypeORM entity for a Product with:
- UUID primary key
- Name (string, required, indexed)
- Price (decimal)
- Category relationship (many-to-one)
- Timestamps (created_at, updated_at)
```

### Migrations

```
Generate a database migration to:
- Add email_verified boolean column to users table
- Default value false
- Add index on email_verified
- Include rollback logic
```

## API Development

### REST Endpoints

```
Create a REST API endpoint to update user profile with:
- PUT /api/users/:id
- Authentication required
- Input validation
- Authorization check (user can only update own profile)
- Return updated user object
```

```
Implement a pagination endpoint for products with:
- GET /api/products
- Query params: page, limit, sort, filter
- Return products array and pagination metadata
- Default limit of 20
```

### Middleware

```
Create Express middleware for rate limiting with:
- Limit requests per IP address
- Configurable time window and max requests
- Return 429 status when limit exceeded
- Include retry-after header
```

```
Write authentication middleware that:
- Extracts JWT from Authorization header
- Verifies token signature
- Adds user object to request
- Returns 401 for invalid/missing token
```

## Frontend

### React Components

```
Create a React component for a user profile card with:
- Props: user object (name, email, avatar)
- Display user information
- Edit button
- TypeScript types
- Styled with Tailwind CSS
```

```
Generate a custom React hook for fetching data with:
- Generic type parameter
- Loading state
- Error handling
- Automatic refetch on dependency change
```

### Form Handling

```
Create a form component with validation using React Hook Form:
- Email field (required, valid email)
- Password field (required, min 8 chars)
- Submit button (disabled while submitting)
- Display validation errors
- TypeScript types
```

## Refactoring

### Code Improvement

```
Refactor this function to:
- Extract complex logic into separate functions
- Use descriptive variable names
- Add error handling
- Improve readability
```

```
Simplify this conditional logic by:
- Reducing nesting
- Using early returns
- Extracting conditions into named variables
```

### Performance

```
Optimize this function for better performance:
- Reduce time complexity
- Minimize database queries
- Add caching where appropriate
- Explain the improvements
```

## Security

### Input Sanitization

```
Add input sanitization to prevent XSS attacks:
- Escape HTML special characters
- Validate against whitelist
- Remove dangerous tags
```

```
Implement SQL injection prevention using:
- Parameterized queries
- Input validation
- Type checking
```

### Authentication

```
Implement JWT authentication with:
- Token generation on login
- Token verification middleware
- Refresh token logic
- Secure token storage recommendations
```

## DevOps

### CI/CD

```
Create a GitHub Actions workflow for:
- Running tests on pull requests
- Linting code
- Building the application
- Deploying to staging on main branch
```

```
Generate a Docker Compose configuration with:
- Application service
- PostgreSQL database
- Redis cache
- Environment variable handling
```

### Configuration

```
Create a configuration file for:
- Database connection
- API keys (from environment variables)
- Feature flags
- Logging levels
```

## Advanced Patterns

### Design Patterns

```
Implement the Repository pattern for User data access with:
- Interface defining CRUD operations
- Implementation using TypeORM
- Error handling
- TypeScript types
```

```
Create a Factory pattern for creating different types of notifications:
- Email notification
- SMS notification
- Push notification
- Common interface
```

### Async Operations

```
Implement a retry mechanism for API calls with:
- Exponential backoff
- Maximum retry attempts
- Configurable delay
- Error logging
```

```
Create a queue processor that:
- Processes jobs from a queue
- Handles failures with retry
- Concurrent job processing
- Progress tracking
```

## Debugging

### Logging

```
Add comprehensive logging to this function with:
- Input parameters
- Execution flow
- Error conditions
- Performance metrics
```

### Error Analysis

```
Analyze this error stack trace and:
- Identify the root cause
- Suggest fixes
- Explain why the error occurred
```

## Tips for Effective Prompts

### Be Specific
- Include exact requirements
- Specify technologies/frameworks
- Define expected behavior
- Mention edge cases

### Provide Context
- Describe the broader application
- Explain business requirements
- Reference related code
- Include constraints

### Iterate
- Start with basic prompt
- Refine based on results
- Add more details as needed
- Combine multiple prompts

### Use Comments
```typescript
// TODO: Implement user authentication with:
// - Email and password
// - JWT token generation
// - Password hashing with bcrypt
// - Error handling for invalid credentials
```

## Organization-Specific Prompts

See [org-style-prompts.md](./org-style-prompts.md) for prompts customized to our organization's standards and practices.

## Practice Exercises

Work through [prompt-katas.md](./prompt-katas.md) to practice writing effective prompts and improve your Copilot skills.

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- Organization standards in [docs/org-standards/](../docs/org-standards/)
