# Organization-Specific Style Prompts

This document contains prompts customized for our organization's specific coding standards, frameworks, and practices.

> **Note**: Customize this file to match your organization's actual standards, conventions, and preferred technologies.

## Overview

Use these prompts to ensure generated code aligns with our organization's standards as defined in [docs/org-standards/](../docs/org-standards/).

## General Code Style

### Standard Function Template

```typescript
// Create a [language] function following our standards:
// - Use [naming convention]
// - Include comprehensive error handling
// - Add [documentation style] documentation
// - Follow [specific style guide]
// - Include type definitions
// - Handle edge cases
```

### Error Handling Pattern

```typescript
// Add error handling following our standard pattern:
// - Use custom error classes from src/errors
// - Log errors with our logger (winston)
// - Include error codes for client errors
// - Never expose internal errors to clients
// - Always log stack traces
```

## Framework-Specific

### Our React Component Standard

```typescript
// Create a React functional component following our standards:
// - Use TypeScript with explicit prop types
// - Use styled-components for styling
// - Include PropTypes and defaultProps
// - Add JSDoc comments
// - Export as named export
// - Co-locate test file
// - Use our custom hooks from src/hooks
// - Follow our component folder structure
```

**Example**:
```typescript
// Create a UserCard component with:
// - Props: user (User type), onEdit callback
// - Display user name, email, avatar
// - Edit button that calls onEdit
// - Use our theme from styled-components
// - Responsive design (mobile-first)
// - Accessibility: proper ARIA labels
// - TypeScript types
// - Unit tests with React Testing Library
```

### Our API Endpoint Standard

```typescript
// Create an Express API endpoint following our standards:
// - Use async/await with express-async-errors
// - Validate input with Zod schemas
// - Use our standard response format: { data, error, meta }
// - Include rate limiting middleware
// - Add authentication middleware from src/middleware/auth
// - Log requests with our request logger
// - Handle errors with our error handler
// - Include OpenAPI/Swagger comments
// - Return appropriate HTTP status codes
```

### Our Database Query Standard

```typescript
// Create a database query following our standards:
// - Use Prisma ORM
// - Include proper error handling
// - Use transactions for multi-step operations
// - Add query logging for debugging
// - Optimize with proper indexes (note in comment)
// - Handle not found cases
// - Include pagination for list queries
// - Use our standard page/limit parameters
```

## Testing Standards

### Unit Test Template

```typescript
// Write unit tests following our standards:
// - Use Jest as testing framework
// - Follow AAA pattern (Arrange, Act, Assert)
// - Use descriptive test names: should [expected behavior] when [condition]
// - Mock external dependencies with jest.mock
// - Use our test fixtures from __fixtures__
// - Aim for >80% coverage
// - Test edge cases and error conditions
// - Clean up after tests (afterEach)
```

### Integration Test Template

```typescript
// Write integration tests following our standards:
// - Use supertest for API testing
// - Set up test database with test containers
// - Use our test fixtures
// - Test complete user flows
// - Clean up test data after each test
// - Test authentication/authorization
// - Verify response structure
// - Check database state after operations
```

## Security Standards

### Input Validation Template

```typescript
// Add input validation following our security standards:
// - Use Zod for schema validation
// - Validate all user inputs
// - Sanitize HTML content with DOMPurify
// - Check string lengths (prevent DoS)
// - Validate file uploads (type, size)
// - Use parameterized queries (prevent SQL injection)
// - Encode output for context (HTML, SQL, JavaScript)
// - Return generic error messages (don't leak info)
```

### Authentication Template

```typescript
// Implement authentication following our standards:
// - Use JWT with RS256 algorithm
// - Token expiry: 1 hour (access), 7 days (refresh)
// - Store refresh tokens in Redis
// - Hash passwords with bcrypt (12 rounds)
// - Implement rate limiting (5 attempts per 15 min)
// - Include CSRF protection
// - Set secure cookie flags (httpOnly, secure, sameSite)
// - Log authentication events
```

## Documentation Standards

### API Documentation Template

```typescript
// Add API documentation following our standards:
// - Use JSDoc format
// - Include OpenAPI/Swagger annotations
// - Document all parameters and return types
// - Provide request/response examples
// - List possible error codes
// - Include authentication requirements
// - Note rate limits
// - Link to related endpoints
```

### Code Comment Template

```typescript
// Add code comments following our standards:
// - Explain "why", not "what"
// - Document complex business logic
// - Reference ticket numbers for workarounds
// - Keep comments concise and current
// - Use TODO comments with assigned person
// - Include examples for complex functions
// - Don't comment obvious code
```

## Our Tech Stack Specific

### Backend Service Template

```
Create a new backend service following our architecture:

Technology Stack:
- Node.js with TypeScript
- Express.js framework
- Prisma ORM with PostgreSQL
- Redis for caching
- Winston for logging
- Jest for testing
- Zod for validation

Structure:
- src/routes - API endpoints
- src/services - Business logic
- src/repositories - Data access
- src/middleware - Express middleware
- src/types - TypeScript types
- src/utils - Utility functions
- src/config - Configuration

Requirements:
- Environment-based config
- Health check endpoint
- Graceful shutdown
- Error handling middleware
- Request logging
- CORS configuration
- Helmet for security headers
- Rate limiting
```

### Frontend Application Template

```
Create a new frontend component following our architecture:

Technology Stack:
- React with TypeScript
- styled-components
- React Router
- React Query for data fetching
- Formik + Yup for forms
- React Testing Library

Structure:
- components/ - Reusable components
- pages/ - Route components
- hooks/ - Custom hooks
- services/ - API clients
- types/ - TypeScript types
- utils/ - Utility functions
- styles/ - Theme and global styles

Requirements:
- Mobile-first responsive design
- Accessibility (WCAG AA)
- Error boundaries
- Loading states
- Empty states
- Internationalization ready (i18next)
```

## Database Patterns

### Migration Template

```typescript
// Create a database migration following our standards:
// - Use Prisma migrate
// - Include both up and down migrations
// - Add indexes for foreign keys
// - Use appropriate column types
// - Set NOT NULL appropriately
// - Add default values where needed
// - Include comments for complex fields
// - Test migration on sample data
```

### Model Template

```typescript
// Create a Prisma model following our standards:
// - Use uuid for id (@@id @default(uuid()))
// - Include timestamps (createdAt, updatedAt)
// - Add indexes for commonly queried fields
// - Use appropriate field types
// - Define relations explicitly
// - Add validation rules
// - Include soft delete if needed (deletedAt)
// - Add unique constraints where applicable
```

## CI/CD Patterns

### GitHub Actions Workflow Template

```yaml
# Create a GitHub Actions workflow following our standards:
# - Trigger on push to main and pull requests
# - Run linting (ESLint, Prettier)
# - Run type checking (TypeScript)
# - Run tests with coverage
# - Run security scans (npm audit, Snyk)
# - Build application
# - Deploy to staging (on main branch)
# - Use caching for dependencies
# - Fail fast on errors
# - Send notifications on failure
```

## Performance Patterns

### Optimization Template

```typescript
// Optimize this code following our standards:
// - Use Redis caching where appropriate (15-minute TTL)
// - Implement database query optimization (use indexes)
// - Add pagination for large datasets (default: 20 per page)
// - Use connection pooling
// - Implement request batching
// - Add database query logging in development
// - Consider using CDN for static assets
// - Minimize N+1 queries
// - Use lazy loading for expensive operations
```

## Monitoring and Observability

### Logging Template

```typescript
// Add logging following our standards:
// - Use Winston logger
// - Log level: error, warn, info, debug
// - Include correlation ID for tracing
// - Structured logging (JSON format)
// - Never log sensitive data (passwords, tokens, PII)
// - Include context: userId, requestId, action
// - Log: errors, security events, business events
// - Use appropriate log levels
```

### Metrics Template

```typescript
// Add metrics following our standards:
// - Use Prometheus client
// - Track: request duration, request count, error rate
// - Include labels: endpoint, method, status
// - Use histogram for durations
// - Use counter for counts
// - Use gauge for current values
// - Prefix metrics with service name
// - Don't create high-cardinality metrics
```

## Customization Guide

To customize this file for your organization:

1. **Update Tech Stack**: Replace with your actual technologies
2. **Add Your Patterns**: Include organization-specific patterns
3. **Reference Your Docs**: Link to internal documentation
4. **Include Examples**: Add real examples from your codebase
5. **Keep Updated**: Review and update quarterly
6. **Get Feedback**: Ask developers what prompts would help them

## Contributing

To add new organization-specific prompts:
1. Ensure it follows an established pattern
2. Test with GitHub Copilot
3. Document any prerequisites
4. Include examples
5. Submit PR for review

## Resources

- [Coding Standards](../docs/org-standards/coding-standards.md)
- [Security Guidelines](../docs/org-standards/security-guidelines.md)
- [Documentation Style](../docs/org-standards/documentation-style.md)
- [General Prompt Library](./prompt-library.md)

---

**Remember**: These prompts are starting points. Adjust and iterate based on the specific context of your task!
