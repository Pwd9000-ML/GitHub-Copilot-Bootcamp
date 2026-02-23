# Quality Refinements and Standards with GitHub Copilot

**Duration:** 30-45 minutes  
**Format:** Presentation with practical examples  
**Objective:** Learn to enforce coding standards, ensure consistency, and maintain high code quality using GitHub Copilot.

---

## Session Overview

Maintaining consistent code quality across a team or project is challenging. Copilot can help enforce standards, generate compliant code, and identify deviations from best practices.

**What you'll learn:**
- Configuring Copilot to follow coding standards
- Prompting techniques for consistent code generation
- Automated code review and quality checks
- Building quality gates into your workflow

---

## 1. Enforcing Coding Standards

### Using Instruction Files for Standards

Create `.github/copilot-instructions.md` to establish project-wide standards:

```markdown
# Project Coding Standards

## Language and Framework
- Use TypeScript with strict mode enabled
- Target ES2022 or later
- Use React 18+ with functional components and hooks

## Naming Conventions
- Variables and functions: camelCase
- Classes and types: PascalCase
- Constants: SCREAMING_SNAKE_CASE
- File names: kebab-case for utilities, PascalCase for components

## Code Style
- Maximum line length: 100 characters
- Use single quotes for strings
- Always use semicolons
- Use 2-space indentation

## Documentation
- All public functions must have JSDoc comments
- Include @param, @returns, and @throws tags
- Add examples for complex functions

## Error Handling
- Never use empty catch blocks
- Always provide meaningful error messages
- Use custom error classes for domain errors

## Testing
- Minimum 80% code coverage
- Follow AAA pattern (Arrange, Act, Assert)
- Use descriptive test names: "should [action] when [condition]"
```

---

### Standards-Aware Prompting

#### Prompt for Standards-Compliant Code

**Prompt:**
```text
Generate a TypeScript function following our coding standards:
- Calculate the total price of items in a shopping cart
- Apply percentage-based discount if provided
- Include JSDoc documentation with examples
- Use proper error handling for invalid inputs
- Follow functional programming principles
```

**Expected Output:**
```typescript
/**
 * Calculates the total price of items in a shopping cart with optional discount.
 * 
 * @param items - Array of cart items with price and quantity
 * @param discountPercent - Optional discount percentage (0-100)
 * @returns The calculated total after discount
 * @throws {Error} If items array is empty or discount is invalid
 * 
 * @example
 * const items = [
 *   { price: 10.00, quantity: 2 },
 *   { price: 15.50, quantity: 1 }
 * ];
 * calculateCartTotal(items, 10); // Returns 31.95 (10% off 35.50)
 */
export function calculateCartTotal(
  items: ReadonlyArray<CartItem>,
  discountPercent?: number
): number {
  if (!items.length) {
    throw new Error('Cart cannot be empty');
  }

  if (discountPercent !== undefined && (discountPercent < 0 || discountPercent > 100)) {
    throw new Error('Discount must be between 0 and 100');
  }

  const subtotal = items.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );

  const discountMultiplier = discountPercent 
    ? (100 - discountPercent) / 100 
    : 1;

  return Math.round(subtotal * discountMultiplier * 100) / 100;
}

interface CartItem {
  readonly price: number;
  readonly quantity: number;
}
```

---

### Converting Code to Match Standards

**Prompt:**
```text
Refactor this JavaScript code to match our TypeScript coding standards:
- Add TypeScript types and interfaces
- Add JSDoc documentation
- Use const/let instead of var
- Apply proper error handling
- Follow our naming conventions

function getUserData(id) {
    var user = db.find(id)
    if (user == null) {
        return null
    }
    var result = {
        name: user.name,
        email: user.email,
        created: user.createdAt
    }
    return result
}
```

**Standards-Compliant Output:**
```typescript
/**
 * Retrieves user data by ID from the database.
 * 
 * @param userId - The unique identifier of the user
 * @returns User data object or null if not found
 * @throws {Error} If userId is invalid
 * 
 * @example
 * const user = await getUserData('user-123');
 * if (user) {
 *   console.log(user.displayName);
 * }
 */
export async function getUserData(userId: string): Promise<UserData | null> {
  if (!userId?.trim()) {
    throw new Error('User ID is required');
  }

  const user = await db.find(userId);
  
  if (!user) {
    return null;
  }

  return {
    displayName: user.name,
    emailAddress: user.email,
    createdAt: user.createdAt,
  };
}

interface UserData {
  readonly displayName: string;
  readonly emailAddress: string;
  readonly createdAt: Date;
}
```

---

## 2. Code Analysis and Quality Checks

### Automated Code Review Prompts

#### Comprehensive Code Review

**Prompt:**
```text
Perform a code review on this function. Check for:
1. Correctness - Does it do what it's supposed to?
2. Performance - Are there any inefficiencies?
3. Security - Are there any vulnerabilities?
4. Maintainability - Is the code clean and readable?
5. Standards compliance - Does it follow best practices?

Provide specific feedback with line references and suggested fixes.

[paste code here]
```

#### SOLID Principles Check

**Prompt:**
```text
Analyse this class against SOLID principles. Identify violations and suggest refactoring:

class ReportGenerator {
    constructor() {
        this.database = new Database();
        this.emailService = new EmailService();
        this.pdfGenerator = new PDFGenerator();
        this.logger = new Logger();
    }

    generateSalesReport(startDate, endDate) {
        const data = this.database.query(`SELECT * FROM sales WHERE date BETWEEN '${startDate}' AND '${endDate}'`);
        const report = this.formatReport(data);
        const pdf = this.pdfGenerator.create(report);
        this.emailService.send('manager@company.com', 'Sales Report', pdf);
        this.logger.log('Report generated');
        return pdf;
    }

    formatReport(data) {
        // ... formatting logic
    }
}
```

**Expected Analysis:**
| Principle | Violation | Suggestion |
|-----------|-----------|------------|
| **S**ingle Responsibility | Class handles data, formatting, PDF, email, logging | Extract separate services |
| **O**pen/Closed | Hard-coded email recipient | Use configuration/injection |
| **L**iskov Substitution | N/A | - |
| **I**nterface Segregation | Depends on entire services | Define focused interfaces |
| **D**ependency Inversion | Creates own dependencies | Use dependency injection |

---

### Quality Metrics Analysis

**Prompt:**
```text
Analyse this code for quality metrics and provide scores:
- Cyclomatic complexity (target: <10)
- Cognitive complexity (target: <15)
- Lines of code per function (target: <30)
- Nesting depth (target: <4)
- Comment ratio (target: >10%)

Suggest specific improvements for any metrics that exceed targets.

[paste code here]
```

---

## 3. Consistency Patterns

### Generating Consistent APIs

**Prompt:**
```text
Generate CRUD operations for a "Product" entity following this consistent pattern:

- Use async/await
- Return standardised response objects: { success: boolean, data?: T, error?: string }
- Include input validation
- Use TypeScript with strict types
- Add JSDoc for each function
- Handle errors with try-catch

Existing pattern example:
async function createUser(userData: CreateUserInput): Promise<ApiResponse<User>> {
    try {
        validateUserInput(userData);
        const user = await db.users.create(userData);
        return { success: true, data: user };
    } catch (error) {
        return { success: false, error: error.message };
    }
}
```

**Consistent Output:**
```typescript
interface Product {
  id: string;
  name: string;
  price: number;
  description: string;
  createdAt: Date;
  updatedAt: Date;
}

interface CreateProductInput {
  name: string;
  price: number;
  description?: string;
}

interface UpdateProductInput {
  name?: string;
  price?: number;
  description?: string;
}

interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}

/**
 * Creates a new product in the database.
 * @param productData - The product data to create
 * @returns ApiResponse containing the created product or error
 */
async function createProduct(
  productData: CreateProductInput
): Promise<ApiResponse<Product>> {
  try {
    validateProductInput(productData);
    const product = await db.products.create(productData);
    return { success: true, data: product };
  } catch (error) {
    return { success: false, error: error.message };
  }
}

/**
 * Retrieves a product by its ID.
 * @param productId - The unique identifier of the product
 * @returns ApiResponse containing the product or error
 */
async function getProduct(productId: string): Promise<ApiResponse<Product>> {
  try {
    validateId(productId);
    const product = await db.products.findById(productId);
    if (!product) {
      return { success: false, error: 'Product not found' };
    }
    return { success: true, data: product };
  } catch (error) {
    return { success: false, error: error.message };
  }
}

/**
 * Updates an existing product.
 * @param productId - The unique identifier of the product
 * @param updates - The fields to update
 * @returns ApiResponse containing the updated product or error
 */
async function updateProduct(
  productId: string,
  updates: UpdateProductInput
): Promise<ApiResponse<Product>> {
  try {
    validateId(productId);
    validateProductUpdates(updates);
    const product = await db.products.update(productId, updates);
    if (!product) {
      return { success: false, error: 'Product not found' };
    }
    return { success: true, data: product };
  } catch (error) {
    return { success: false, error: error.message };
  }
}

/**
 * Deletes a product by its ID.
 * @param productId - The unique identifier of the product
 * @returns ApiResponse indicating success or error
 */
async function deleteProduct(productId: string): Promise<ApiResponse<void>> {
  try {
    validateId(productId);
    const deleted = await db.products.delete(productId);
    if (!deleted) {
      return { success: false, error: 'Product not found' };
    }
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
}
```

---

### Error Handling Consistency

**Prompt:**
```text
Create a standardised error handling pattern for this API. Include:
- Custom error classes for different error types
- Error codes for client identification
- Consistent error response format
- Logging integration
- Stack trace handling (dev vs production)

Error types needed: ValidationError, NotFoundError, AuthenticationError, AuthorizationError
```

**Output:**
```typescript
// Error codes for client-side handling
const ERROR_CODES = {
  VALIDATION_ERROR: 'E001',
  NOT_FOUND: 'E002',
  AUTHENTICATION_FAILED: 'E003',
  AUTHORIZATION_FAILED: 'E004',
  INTERNAL_ERROR: 'E500',
} as const;

// Base custom error class
abstract class AppError extends Error {
  abstract readonly code: string;
  abstract readonly statusCode: number;
  readonly timestamp: Date;
  
  constructor(message: string) {
    super(message);
    this.name = this.constructor.name;
    this.timestamp = new Date();
    Error.captureStackTrace(this, this.constructor);
  }

  toResponse(includeStack = false): ErrorResponse {
    return {
      success: false,
      error: {
        code: this.code,
        message: this.message,
        timestamp: this.timestamp.toISOString(),
        ...(includeStack && { stack: this.stack }),
      },
    };
  }
}

class ValidationError extends AppError {
  readonly code = ERROR_CODES.VALIDATION_ERROR;
  readonly statusCode = 400;
  readonly fields: Record<string, string>;

  constructor(message: string, fields: Record<string, string> = {}) {
    super(message);
    this.fields = fields;
  }
}

class NotFoundError extends AppError {
  readonly code = ERROR_CODES.NOT_FOUND;
  readonly statusCode = 404;
  readonly resource: string;

  constructor(resource: string, id?: string) {
    super(id ? `${resource} with ID ${id} not found` : `${resource} not found`);
    this.resource = resource;
  }
}

class AuthenticationError extends AppError {
  readonly code = ERROR_CODES.AUTHENTICATION_FAILED;
  readonly statusCode = 401;
}

class AuthorizationError extends AppError {
  readonly code = ERROR_CODES.AUTHORIZATION_FAILED;
  readonly statusCode = 403;
}

// Error handler middleware
function errorHandler(error: Error, req: Request, res: Response) {
  const isDevelopment = process.env.NODE_ENV === 'development';
  
  logger.error({
    error: error.message,
    stack: error.stack,
    path: req.path,
    method: req.method,
  });

  if (error instanceof AppError) {
    return res.status(error.statusCode).json(error.toResponse(isDevelopment));
  }

  // Unknown error - return generic response
  return res.status(500).json({
    success: false,
    error: {
      code: ERROR_CODES.INTERNAL_ERROR,
      message: isDevelopment ? error.message : 'An unexpected error occurred',
      timestamp: new Date().toISOString(),
    },
  });
}
```

---

## 4. Building Quality Gates

### Pre-Commit Quality Checks

**Prompt:**
```text
Create a pre-commit hook script that:
1. Runs ESLint and fails on errors
2. Runs Prettier and auto-fixes formatting
3. Runs TypeScript type checking
4. Checks for console.log statements
5. Validates commit message format (conventional commits)
6. Runs unit tests for changed files

Use husky and lint-staged configuration.
```

**Output - package.json scripts:**
```json
{
  "scripts": {
    "lint": "eslint . --ext .ts,.tsx",
    "lint:fix": "eslint . --ext .ts,.tsx --fix",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "typecheck": "tsc --noEmit",
    "test": "jest",
    "test:staged": "jest --findRelatedTests --passWithNoTests",
    "prepare": "husky install"
  },
  "lint-staged": {
    "*.{ts,tsx}": [
      "eslint --fix",
      "prettier --write",
      "jest --findRelatedTests --passWithNoTests"
    ],
    "*.{json,md,yml}": [
      "prettier --write"
    ]
  }
}
```

**.husky/pre-commit:**
```bash
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

# Type check
echo "Running type check..."
npm run typecheck || exit 1

# Check for console.log
echo "Checking for console.log statements..."
if git diff --cached --name-only | xargs grep -l 'console.log' 2>/dev/null; then
    echo "Error: console.log statements found. Please remove them."
    exit 1
fi

# Run lint-staged
npx lint-staged
```

Note: Husky supports Windows, but hooks are shell scripts. If you are on Windows, ensure your Git environment can run POSIX shell scripts (for example via Git for Windows' bundled tooling). See <https://typicode.github.io/husky/>

---

### CI/CD Quality Gates

**Prompt:**
```text
Create a GitHub Actions workflow that enforces these quality gates before merging:

1. All tests pass with >80% coverage
2. No ESLint errors or warnings
3. TypeScript compiles without errors
4. No security vulnerabilities in dependencies
5. Bundle size increase <10%
6. Performance benchmarks pass
7. Documentation is up-to-date

Fail the build with clear messages if any gate fails.
```

---

## 5. Documentation Standards

### Auto-Generating Documentation

**Prompt:**
```text
Generate comprehensive API documentation for this module:
- Overview of what the module does
- Installation and setup instructions
- API reference with all public functions
- Code examples for common use cases
- Error handling guidance
- TypeScript type definitions

[paste module code here]
```

### README Generation

**Prompt:**
```text
Generate a README.md for this project following this structure:
1. Project title and badges (build status, coverage, npm version)
2. One-paragraph description
3. Features list
4. Quick start guide (install, configure, run)
5. API documentation (brief)
6. Configuration options table
7. Contributing guidelines link
8. License
```

---

## Quality Standards Quick Reference

| Category | Standard | Verification |
|----------|----------|--------------|
| **Naming** | camelCase for functions, PascalCase for classes | ESLint rules |
| **Documentation** | JSDoc on all public APIs | TypeDoc generation |
| **Types** | Strict TypeScript, no `any` | TSC strict mode |
| **Testing** | 80%+ coverage, AAA pattern | Jest coverage report |
| **Security** | No hardcoded secrets, input validation | npm audit, custom rules |
| **Performance** | No N+1 queries, proper memoisation | Performance tests |
| **Accessibility** | WCAG 2.1 AA compliance | axe-core, Lighthouse |

---

## Key Takeaways

1. **Codify your standards** - Use instruction files to teach Copilot your conventions
2. **Be explicit in prompts** - Reference specific standards when generating code
3. **Automate enforcement** - Use pre-commit hooks and CI pipelines for quality gates
4. **Generate consistently** - Use templates and patterns for uniform code structure
5. **Review critically** - Copilot follows instructions but may miss context
6. **Document decisions** - Standard code is easier to maintain

---

## Next Steps

- Proceed to [Ethical and Security Considerations](3-Ethical-and-Security-Considerations.md) for responsible AI usage
- Complete the [Week 4 Lab](4-Week4-Lab.md) for hands-on practice
- Review [Week 4 Prompts](5-Week4-Prompts.md) for additional quality-focused prompts

---
