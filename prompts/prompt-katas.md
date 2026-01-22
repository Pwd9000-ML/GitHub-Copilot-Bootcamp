# Prompt Katas

Practice exercises to improve your GitHub Copilot prompting skills. Work through these progressively to master effective prompting.

## What are Prompt Katas?

Inspired by code katas, these are focused exercises designed to practice specific prompting techniques with GitHub Copilot. Each kata builds on previous skills.

## How to Use

1. Read the kata description
2. Write your prompt in a comment
3. Let Copilot generate the solution
4. Review and refine
5. Compare with the solution notes
6. Reflect on what worked well

## Beginner Katas

### Kata 1: Basic Function Generation

**Goal**: Generate a simple utility function

**Exercise**: Create a function that converts Celsius to Fahrenheit.

**Your Prompt**:
```typescript
// Your prompt here
```

**Solution Notes**:
- Simple, direct prompt works: "Convert Celsius to Fahrenheit"
- Include return type for better results
- Specify parameter name for clarity

---

### Kata 2: Input Validation

**Goal**: Practice specifying validation requirements

**Exercise**: Create a function to validate a password with specific rules.

**Your Prompt**:
```typescript
// Your prompt here
```

**Solution Notes**:
- List all requirements explicitly
- Specify return type (boolean or validation result object)
- Mention error messages if needed

**Good Prompt Example**:
```typescript
// Validate password with requirements:
// - At least 8 characters
// - At least one uppercase letter
// - At least one number
// - At least one special character
// Return true if valid, false otherwise
```

---

### Kata 3: Error Handling

**Goal**: Learn to specify error handling requirements

**Exercise**: Create a function that fetches user data with proper error handling.

**Your Prompt**:
```typescript
// Your prompt here
```

**Solution Notes**:
- Specify error types to catch
- Mention logging requirements
- Define fallback behavior

---

## Intermediate Katas

### Kata 4: Type-Safe API Client

**Goal**: Generate complex TypeScript with proper types

**Exercise**: Create a type-safe HTTP client function for fetching user data.

**Your Prompt**:
```typescript
// Your prompt here
```

**Solution Notes**:
- Define the User type first
- Specify generic types if applicable
- Include error handling
- Mention response type

**Strong Prompt Example**:
```typescript
// Create a type-safe function to fetch user by ID:
// - Takes userId as string parameter
// - Returns Promise<User>
// - Uses fetch API
// - Throws error for non-200 responses
// - Includes proper TypeScript types
```

---

### Kata 5: Test Generation

**Goal**: Practice generating comprehensive tests

**Exercise**: Generate unit tests for a calculateDiscount function.

**Your Prompt**:
```typescript
// Your prompt here
```

**Solution Notes**:
- Specify testing framework (Jest, Mocha, etc.)
- List test cases to cover
- Mention mocking needs
- Include edge cases

**Strong Prompt Example**:
```typescript
// Write Jest unit tests for calculateDiscount function covering:
// - Valid discount code (20% off)
// - Invalid discount code (throws error)
// - Expired discount code (throws error)
// - Zero price (returns 0)
// - Negative price (throws error)
// Use describe and it blocks
```

---

### Kata 6: Database Query

**Goal**: Generate efficient database queries

**Exercise**: Create a function to fetch users with pagination and filtering.

**Your Prompt**:
```typescript
// Your prompt here
```

**Solution Notes**:
- Specify ORM/query builder (TypeORM, Prisma, raw SQL)
- Define parameters (page, limit, filters)
- Mention return type
- Include total count for pagination

---

## Advanced Katas

### Kata 7: Design Pattern Implementation

**Goal**: Generate code following specific design patterns

**Exercise**: Implement a Repository pattern for User management.

**Your Prompt**:
```typescript
// Your prompt here
```

**Solution Notes**:
- Name the pattern explicitly
- Define the interface first
- Specify all CRUD operations
- Include error handling

**Strong Prompt Example**:
```typescript
// Implement Repository pattern for User entity with:
// - Interface defining: findById, findAll, create, update, delete
// - Implementation class using TypeORM
// - Proper error handling
// - Return types: Promise<User>, Promise<User[]>, Promise<void>
// - TypeScript types throughout
```

---

### Kata 8: Security Implementation

**Goal**: Generate security-focused code

**Exercise**: Create a secure password reset flow.

**Your Prompt**:
```typescript
// Your prompt here
```

**Solution Notes**:
- List security requirements
- Specify token generation
- Mention expiration
- Include validation

**Strong Prompt Example**:
```typescript
// Create secure password reset endpoint with:
// - Generate cryptographically secure random token
// - Store token hash in database with expiration (1 hour)
// - Send email with reset link
// - Verify token on reset
// - Rate limit to prevent abuse
// - Invalidate token after use
```

---

### Kata 9: Performance Optimization

**Goal**: Generate optimized code

**Exercise**: Create a function to efficiently process large arrays.

**Your Prompt**:
```typescript
// Your prompt here
```

**Solution Notes**:
- Specify performance requirements
- Mention data size
- Consider memory efficiency
- Include complexity analysis

---

### Kata 10: Complex Business Logic

**Goal**: Generate code for complex requirements

**Exercise**: Implement a shopping cart discount calculator with multiple rule types.

**Your Prompt**:
```typescript
// Your prompt here
```

**Solution Notes**:
- Break down complex requirements
- Use clear, structured prompts
- Define data structures first
- Specify rule precedence

**Strong Prompt Example**:
```typescript
// Implement shopping cart discount calculator with:
// 
// Discount types:
// - Percentage: reduce by percent (e.g., 20% off)
// - Fixed amount: reduce by fixed value (e.g., $10 off)
// - BOGO: Buy one get one free
// - Tiered: Different discounts based on total (e.g., >$100 = 10% off)
//
// Rules:
// - Multiple discounts can apply
// - Percentage and fixed apply to subtotal
// - BOGO applies to individual items
// - Tiered applies last
// - Never reduce total below $0
//
// Input: Cart with items and applicable discount codes
// Output: Breakdown showing original price, each discount, final price
```

---

## Challenge Katas

### Challenge 1: Full Feature Implementation

**Goal**: Generate a complete feature with multiple components

**Exercise**: Create a complete user authentication system.

**Requirements**:
- User registration endpoint
- Login endpoint with JWT
- Password hashing
- Refresh token logic
- Logout functionality
- Middleware for protected routes
- Input validation
- Error handling
- TypeScript types

**Your Approach**:
1. Break into smaller parts
2. Write prompts for each component
3. Generate in logical order
4. Test incrementally

---

### Challenge 2: Legacy Code Refactoring

**Goal**: Use Copilot to understand and refactor complex legacy code

**Exercise**: Take the `legacy/messy_module.py` and:
1. Use Copilot Chat to explain what it does
2. Generate tests for current behavior
3. Refactor to clean code
4. Ensure tests still pass

**Tips**:
- Use Copilot Chat for explanations
- Ask specific questions
- Generate characterization tests first
- Refactor incrementally

---

### Challenge 3: Integration Testing

**Goal**: Generate comprehensive integration tests

**Exercise**: Create integration tests for a REST API with multiple endpoints.

**Your Approach**:
- Test all CRUD operations
- Test error conditions
- Test authentication/authorization
- Use proper test fixtures
- Clean up test data

---

## Reflection Questions

After each kata, reflect on:

1. **Prompt Clarity**: Was your prompt clear and specific?
2. **Completeness**: Did the generated code meet all requirements?
3. **Quality**: Was the code production-ready or did it need refinement?
4. **Iteration**: How many iterations did you need?
5. **Learning**: What did you learn about effective prompting?

## Tips for Success

### 1. Be Specific
❌ "Create a function"
✅ "Create a TypeScript function to validate email addresses using regex"

### 2. Provide Context
❌ "Add error handling"
✅ "Add error handling with try-catch, log errors with winston, return 500 status"

### 3. List Requirements
❌ "Create a user form"
✅ "Create a user form with: email field (required), password field (min 8 chars), submit button, validation error display"

### 4. Specify Technologies
❌ "Create a test"
✅ "Create a Jest unit test using @testing-library/react"

### 5. Include Examples
❌ "Parse date string"
✅ "Parse date string in format 'YYYY-MM-DD' to Date object, e.g., '2024-01-15' -> Date"

### 6. Mention Edge Cases
❌ "Calculate average"
✅ "Calculate average of numbers array, handle empty array (return 0), handle null values (skip)"

## Progress Tracker

Track your progress through the katas:

- [ ] Kata 1: Basic Function Generation
- [ ] Kata 2: Input Validation
- [ ] Kata 3: Error Handling
- [ ] Kata 4: Type-Safe API Client
- [ ] Kata 5: Test Generation
- [ ] Kata 6: Database Query
- [ ] Kata 7: Design Pattern Implementation
- [ ] Kata 8: Security Implementation
- [ ] Kata 9: Performance Optimization
- [ ] Kata 10: Complex Business Logic
- [ ] Challenge 1: Full Feature Implementation
- [ ] Challenge 2: Legacy Code Refactoring
- [ ] Challenge 3: Integration Testing

## Next Steps

After completing these katas:
1. Create your own katas for specific scenarios you encounter
2. Share successful prompts with your team
3. Contribute to [prompt-library.md](./prompt-library.md)
4. Practice with real project work

## Resources

- [Prompt Library](./prompt-library.md)
- [Organization Standards](../docs/org-standards/)
- [GitHub Copilot Documentation](https://docs.github.com/copilot)

---

Remember: The goal isn't perfect prompts on the first try, but learning to iterate and refine your prompts effectively!
