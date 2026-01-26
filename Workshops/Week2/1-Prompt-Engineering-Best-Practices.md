# Prompt Engineering Best Practices

**Duration:** 45-60 minutes  
**Format:** Presentation with interactive examples  
**Objective:** Master the art of crafting effective prompts to guide GitHub Copilot for consistent, high-quality code generation.

---

## What is Prompt Engineering?

Prompt engineering is the practice of crafting clear, specific instructions that guide AI tools like GitHub Copilot to produce the desired output. Think of it as learning to communicate effectively with your AI pair programmer.

**Why it matters:**
- Better prompts = better code suggestions
- Reduces iteration time and rework
- Ensures consistency with team standards
- Improves accuracy for complex tasks

---

## The CRAFT Framework for Effective Prompts

Use this framework to structure your prompts for optimal results:

| Element | Description | Example |
|---------|-------------|---------|
| **C**ontext | Background information about your project or task | *"In a Node.js Express application..."* |
| **R**ole | What perspective should Copilot take? | *"As a senior developer..."* |
| **A**ction | What specific task should be performed? | *"...create a function that..."* |
| **F**ormat | How should the output be structured? | *"...with JSDoc comments and error handling"* |
| **T**one | Any style or standards to follow | *"...following our team's naming conventions"* |

---

## Prompt Types and When to Use Them

### 1. Comment-Driven Prompts (Inline)

Write descriptive comments above where you want code generated.

**Basic Example:**
```javascript
// Function to validate email addresses
function validateEmail(email) {
  // Copilot generates the implementation
}
```

**Enhanced Example (with CRAFT):**
```javascript
/**
 * Validates an email address against RFC 5322 standard.
 * Returns true if valid, false otherwise.
 * Should handle edge cases like empty strings and null values.
 * @param {string} email - The email address to validate
 * @returns {boolean} - Whether the email is valid
 */
function validateEmail(email) {
  // Copilot generates a more robust implementation
}
```

---

### 2. Chat-Based Prompts (Ask Mode)

Use conversational prompts in Copilot Chat for exploration, explanation, and generation.

**Weak Prompt:**
> "Write a function"

**Strong Prompt:**
> "Write a JavaScript function to add a new book to an inventory array. The book should have properties for title, author, genre, and publication year. Prevent duplicate entries based on the title. Include input validation and return appropriate error messages."

---

### 3. Template Generation Prompts

Use when you need reusable code structures.

#### Exercise: Book Inventory System

**Prompt 1 - Basic Function:**
> "Generate a JavaScript function template to add a new book with fields like title, author, and genre."

**Prompt 2 - Enhanced Function:**
> "Can you create a reusable function to add books with properties such as title, author, genre, and publication year? Include validation to prevent duplicates."

**Prompt 3 - Search Functionality:**
> "Write a function template to search for books in an inventory by title or genre. Make it case-insensitive and support partial matches."

**Sample Output:**
```javascript
/**
 * Adds a new book to the inventory
 * @param {Array} inventory - The current book inventory
 * @param {Object} book - The book to add
 * @param {string} book.title - Book title
 * @param {string} book.author - Book author
 * @param {string} book.genre - Book genre
 * @param {number} [book.publicationYear] - Optional publication year
 * @returns {Object} Result object with success status and message
 */
function addBook(inventory, book) {
  // Validate required fields
  if (!book.title || !book.author || !book.genre) {
    return { success: false, message: 'Missing required fields' };
  }
  
  // Check for duplicates
  const exists = inventory.some(
    b => b.title.toLowerCase() === book.title.toLowerCase()
  );
  
  if (exists) {
    return { success: false, message: 'Book already exists' };
  }
  
  inventory.push(book);
  return { success: true, message: 'Book added successfully' };
}
```

---

## Writing Effective Prompts: Best Practices

### 1. Be Specific and Detailed

| Weak | Strong |
|------|--------|
| "Create a search function" | "Create a function to search for books by title or genre, returning all matches as an array" |
| "Handle errors" | "Add try-catch blocks with specific error messages for network failures and validation errors" |
| "Make it faster" | "Optimise this function for arrays larger than 10,000 items using indexing or memoization" |

### 2. Provide Context

**Without Context:**
> "Write a login function"

**With Context:**
> "Write a login function for a React application using Firebase Authentication. It should handle email/password login, show loading states, and redirect to the dashboard on success."

### 3. Specify Output Format

```
Generate a function with:
- JSDoc comments describing parameters and return values
- Input validation for all parameters
- Error handling with descriptive messages
- Unit test examples in comments
```

### 4. Use Examples (Few-Shot Prompting)

Give Copilot examples of what you want:

```javascript
// Example of the pattern I want to follow:
// Input: { name: "John", age: 30 }
// Output: "John is 30 years old"

// Now create a similar function for:
// Input: { title: "The Great Gatsby", author: "F. Scott Fitzgerald" }
// Output: Should format book information in a similar readable way
```

### 5. Iterate and Refine

Start broad, then narrow down:

1. **First prompt:** "Create a user authentication system"
2. **Refinement:** "Add password strength validation requiring 8+ characters, uppercase, lowercase, and numbers"
3. **Further refinement:** "Also add rate limiting to prevent brute force attacks"

---

## Organizational Standards with Instruction Files

### What are Copilot Instructions?

Instruction files tell Copilot about your project's conventions, standards, and preferences. They ensure consistent code generation across your team.

### Setting Up Repository Instructions

Create a file at `.github/copilot-instructions.md`:

```markdown
# Copilot Instructions for This Repository

## Code Style
- Use TypeScript for all new files
- Follow ESLint rules defined in .eslintrc
- Use functional components for React
- Prefer async/await over .then() chains

## Naming Conventions
- Use camelCase for variables and functions
- Use PascalCase for classes and React components
- Use SCREAMING_SNAKE_CASE for constants
- Prefix private methods with underscore

## Documentation
- All public functions must have JSDoc comments
- Include @param, @returns, and @throws tags
- Add usage examples for complex functions

## Error Handling
- Always use try-catch for async operations
- Log errors with context using our logger utility
- Return standardised error objects: { success: false, error: string, code: number }

## Security
- Never hardcode credentials or API keys
- Sanitise all user inputs
- Use parameterised queries for database operations
```

### File-Specific Instructions

Create instructions for specific file types or directories:

**For test files (`.github/instructions/tests.instructions.md`):**
```markdown
# Test File Instructions

applyTo: "**/*.test.js,**/*.spec.ts"

- Use Jest as the testing framework
- Follow AAA pattern: Arrange, Act, Assert
- Use descriptive test names: "should [expected behavior] when [condition]"
- Mock external dependencies
- Aim for 80% code coverage minimum
```

---

## Incorporating Security Recommendations

### Prompting for Secure Code

Always include security considerations in your prompts:

**Basic Prompt:**
> "Write a function to query the database for users"

**Security-Aware Prompt:**
> "Write a function to query the database for users using parameterised queries to prevent SQL injection. Include input validation and sanitisation. Log failed attempts for security monitoring."

### Security Prompt Patterns

#### SQL Operations
```
When generating SQL queries:
- Always use parameterised queries or prepared statements
- Validate and sanitise all input before use
- Limit result sets with pagination
- Use principle of least privilege for database connections
```

#### User Input Handling
```
For any function handling user input:
- Validate input type and format
- Sanitise strings to prevent XSS
- Check for maximum length limits
- Reject unexpected characters for sensitive fields
```

#### Authentication
```
For authentication-related code:
- Never store passwords in plain text
- Use bcrypt or argon2 for password hashing
- Implement rate limiting
- Use secure session management
```

---

## Practical Exercises

### Exercise 1: Template Generation

Using Copilot Chat, generate the following with well-crafted prompts:

1. **Add Book Function:**
   > "Generate a JavaScript function template to add a new book with fields like title, author, and genre. Include validation and duplicate checking."

2. **Search Function:**
   > "Write a function template to search for books in an inventory by title or genre. Make it case-insensitive."

3. **Customisation:**
   > "Refactor the addBook function to include an optional field for publication year with validation that it's a valid year."

### Exercise 2: Scaffolding a Project

Use these prompts to scaffold a complete project structure:

1. **Project Structure:**
   > "Create a project structure with folders for src, tests, and public directories."

2. **Initial Files:**
   > "Generate a package.json file with a basic project configuration for a Node.js application."

3. **Modular Structure:**
   > "Add subfolders models, controllers, and views inside the src folder for better modularity."

### Exercise 3: Security-Focused Code

Practice writing security-aware prompts:

1. **Input Validation:**
   > "Write a function to validate and sanitise user registration data (email, password, username) following OWASP guidelines."

2. **Secure Database Query:**
   > "Generate a function to fetch user data by ID using parameterised queries with proper error handling."

### Exercise 4: SQL Query Generation

Practice SQL prompts with Copilot:

| Task | Prompt |
|------|--------|
| Basic SELECT | "Write a SQL query to select all columns from the 'employees' table where the department is 'Sales'." |
| JOIN | "Write a SQL query to join the 'orders' and 'customers' tables on 'customer_id', selecting order ID, customer name, and order total." |
| Aggregation | "Write a SQL query to calculate the average salary of employees in each department." |
| Subquery | "Write a SQL query to find employees who earn more than the average salary in the company." |

---

## Common Pitfalls to Avoid

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Vague prompts** | Generic, unhelpful suggestions | Be specific about inputs, outputs, and constraints |
| **No context** | Code that doesn't fit your project | Include language, framework, and project context |
| **Ignoring output** | Accepting code without review | Always review and test generated code |
| **Single attempt** | Settling for suboptimal results | Iterate and refine your prompts |
| **No security mention** | Potentially vulnerable code | Always include security requirements |

---

## Key Takeaways

1. **Structure your prompts** using the CRAFT framework
2. **Be specific** - detail beats brevity
3. **Provide context** - help Copilot understand your project
4. **Use instruction files** for team-wide consistency
5. **Include security** from the start
6. **Iterate** - refine prompts based on output
7. **Review everything** - Copilot assists, you decide

---

## Next Steps

- Proceed to [Advanced Developer Workflow](2-Advanced-Developer-Workflow.md) to learn about documentation generation and refining Copilot suggestions
- Complete the [Week 2 Lab](3-Week2-Lab.md) to practice customising your Copilot experience
- Review [Week 2 Prompts](4-Week2-Prompts.md) for additional prompt examples
