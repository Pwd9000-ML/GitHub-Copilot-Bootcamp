# Advanced Developer Workflow

**Duration:** 30-45 minutes  
**Format:** Presentation with demonstrations  
**Objective:** Learn to leverage GitHub Copilot for documentation generation and refining suggestions for maintainable, production-ready code.

---

## Part 1: Documentation Generation with Copilot

Documentation is essential for maintainable code, but often neglected due to time constraints. Copilot can significantly reduce the effort required to create comprehensive documentation.

---

### Types of Documentation Copilot Can Generate

| Type | Description | When to Use |
|------|-------------|-------------|
| **Inline Comments** | Single-line explanations within code | Complex logic, non-obvious decisions |
| **JSDoc/Docstrings** | Structured function documentation | All public functions and methods |
| **README Files** | Project overviews and setup guides | Every repository |
| **API Documentation** | Endpoint descriptions and examples | REST/GraphQL APIs |
| **Architecture Docs** | System design explanations | Complex systems |
| **Code Explanations** | Detailed walkthrough of existing code | Onboarding, knowledge sharing |

---

### Generating Function Documentation

#### Using Inline Suggestions

Type `/**` above a function to trigger documentation generation:

```javascript
/**
 * // Copilot will suggest documentation here
 */
function calculateCompoundInterest(principal, rate, time, n) {
  return principal * Math.pow((1 + rate / n), n * time);
}
```

**Expected Output:**
```javascript
/**
 * Calculates compound interest over a specified period.
 * @param {number} principal - The initial amount of money
 * @param {number} rate - The annual interest rate (as decimal, e.g., 0.05 for 5%)
 * @param {number} time - The number of years
 * @param {number} n - The number of times interest is compounded per year
 * @returns {number} The final amount after compound interest
 * @example
 * // Calculate 5% annual interest compounded monthly for 10 years on $1000
 * calculateCompoundInterest(1000, 0.05, 10, 12); // Returns ~1647.01
 */
```

#### Using Copilot Chat

For existing undocumented code, use Ask mode:

**Prompt:**
> "Generate comprehensive JSDoc documentation for all functions in this file, including parameter types, return values, exceptions thrown, and usage examples."

---

### Generating README Files

#### Quick README Generation

**Prompt:**
> "Generate a README.md for this project that includes: project title and description, features list, installation instructions, usage examples, API documentation (if applicable), contributing guidelines, and license information."

#### Example: Book Inventory System README

**Prompt:**
> "Create a README.md for a Book Inventory Management System built with Node.js. Include sections for setup, usage, API endpoints, and testing."

**Sample Output:**
```markdown
# Book Inventory Management System

A Node.js application for managing book inventories with add, search, and list functionality.

## Features

- Add books with title, author, genre, and publication year
- Search books by title or genre (case-insensitive)
- Duplicate detection based on book title
- Persistent storage using JSON files or local storage

## Installation

npm install

## Usage

const { addBook, searchBooks, listBooks } = require('./src/inventory');

// Add a new book
addBook(inventory, {
  title: 'The Great Gatsby',
  author: 'F. Scott Fitzgerald',
  genre: 'Fiction',
  publicationYear: 1925
});

// Search for books
const results = searchBooks(inventory, 'gatsby');

## Testing

npm test

## License

MIT
```

---

### Code Explanation Documentation

Use Copilot to explain complex code for documentation purposes:

**Prompt:**
> "Explain the logic in this addBook function, especially how duplicates are handled. Format the explanation as a documentation comment that could be added above the function."

**Another Prompt:**
> "Describe how this searchBooks function works and how it filters by title or genre. Write it as internal documentation for other developers."

---

### API Documentation Generation

For REST APIs, generate endpoint documentation:

**Prompt:**
> "Generate OpenAPI/Swagger documentation for this Express router file. Include request/response schemas, status codes, and example payloads."

**Sample Output:**
```yaml
/api/books:
  post:
    summary: Add a new book to the inventory
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - title
              - author
              - genre
            properties:
              title:
                type: string
                example: "The Great Gatsby"
              author:
                type: string
                example: "F. Scott Fitzgerald"
              genre:
                type: string
                example: "Fiction"
              publicationYear:
                type: integer
                example: 1925
    responses:
      201:
        description: Book created successfully
      400:
        description: Invalid input or duplicate book
```

---

## Part 2: Refining Copilot Suggestions

Not every suggestion from Copilot is production-ready. Learning to refine and improve suggestions is key to effective use.

---

### The Review-Refine-Iterate Cycle

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Generate   │────▶│   Review    │────▶│   Refine    │
│  Suggestion │     │   Output    │     │   Prompt    │
└─────────────┘     └─────────────┘     └─────────────┘
       ▲                                       │
       │                                       │
       └───────────────────────────────────────┘
                    Iterate
```

### What to Look For When Reviewing

| Aspect | Questions to Ask | Action |
|--------|------------------|--------|
| **Correctness** | Does it work? Any logic errors? | Test and debug |
| **Completeness** | Are edge cases handled? | Add missing scenarios |
| **Security** | Any vulnerabilities? Input validation? | Add security measures |
| **Performance** | Will it scale? Any inefficiencies? | Optimise as needed |
| **Readability** | Is it clear? Well-named? | Refactor for clarity |
| **Standards** | Follows team conventions? | Align with guidelines |

---

### Refinement Techniques

#### 1. Ask for Improvements

After receiving a suggestion, ask Copilot to improve it:

**Initial Prompt:**
> "Write a function to search for books in an inventory"

**Refinement Prompts:**
> "Now optimise this for performance when searching through 10,000+ books"

> "Add input validation to handle null, undefined, and empty string searches"

> "Refactor to follow our team's error handling pattern with try-catch and standardised error objects"

#### 2. Request Alternatives

**Prompt:**
> "Can you suggest a more efficient algorithm for this search function? Show me 2-3 alternative approaches with their trade-offs."

#### 3. Add Missing Features Incrementally

**Prompt:**
> "Modify the searchBooks function to also filter by author, not just title and genre."

**Prompt:**
> "Update the addBook function to include an optional field for publication year with validation that it's a valid year between 1450 and the current year."

---

### Example: Progressive Refinement

**Step 1 - Basic Generation:**
```javascript
// Initial prompt: "Write a function to add books to an array"
function addBook(books, book) {
  books.push(book);
}
```

**Step 2 - Add Validation:**
```javascript
// Refinement: "Add input validation and duplicate checking"
function addBook(books, book) {
  if (!book.title || !book.author) {
    throw new Error('Title and author are required');
  }
  
  if (books.some(b => b.title === book.title)) {
    throw new Error('Book already exists');
  }
  
  books.push(book);
}
```

**Step 3 - Improve Error Handling:**
```javascript
// Refinement: "Return a result object instead of throwing errors"
function addBook(books, book) {
  if (!book.title || !book.author) {
    return { success: false, error: 'Title and author are required' };
  }
  
  const exists = books.some(
    b => b.title.toLowerCase() === book.title.toLowerCase()
  );
  
  if (exists) {
    return { success: false, error: 'Book already exists' };
  }
  
  books.push(book);
  return { success: true, data: book };
}
```

**Step 4 - Add Documentation:**
```javascript
// Refinement: "Add JSDoc documentation and make it production-ready"
/**
 * Adds a new book to the inventory with duplicate detection.
 * @param {Array<Object>} books - The current book inventory
 * @param {Object} book - The book to add
 * @param {string} book.title - The book's title (required)
 * @param {string} book.author - The book's author (required)
 * @param {string} [book.genre] - The book's genre (optional)
 * @param {number} [book.publicationYear] - Year of publication (optional)
 * @returns {Object} Result object with success status and data/error
 * @example
 * const result = addBook(inventory, { title: '1984', author: 'George Orwell' });
 * if (result.success) {
 *   console.log('Added:', result.data);
 * }
 */
function addBook(books, book) {
  // Validate required fields
  if (!book?.title?.trim() || !book?.author?.trim()) {
    return { 
      success: false, 
      error: 'Title and author are required and cannot be empty' 
    };
  }
  
  // Check for duplicates (case-insensitive)
  const normalizedTitle = book.title.toLowerCase().trim();
  const exists = books.some(
    b => b.title.toLowerCase().trim() === normalizedTitle
  );
  
  if (exists) {
    return { 
      success: false, 
      error: `Book titled "${book.title}" already exists` 
    };
  }
  
  // Add the book
  const newBook = {
    ...book,
    title: book.title.trim(),
    author: book.author.trim(),
    addedAt: new Date().toISOString()
  };
  
  books.push(newBook);
  return { success: true, data: newBook };
}
```

---

### Scoping Suggestions for Maintainability

#### Single Responsibility Principle

When Copilot generates large functions, ask it to break them down:

**Prompt:**
> "Refactor this function to follow the Single Responsibility Principle. Break it into smaller, focused functions."

#### Modular Architecture

**Prompt:**
> "Reorganise this code into a modular structure with separate files for models, controllers, and utilities. Show me the file structure and the code for each file."

#### Removing Code Duplication

**Prompt:**
> "Identify any duplicate or similar code patterns and refactor them into reusable utility functions."

---

### Debugging with Copilot

When code doesn't work as expected, use Copilot to debug:

#### Identify Issues

**Prompt:**
> "Analyse this function and identify any potential bugs, edge cases, or logical errors."

#### Fix Specific Errors

**Prompt:**
> "I'm getting 'TypeError: Cannot read property of undefined' when calling searchBooks. What could cause this and how do I fix it?"

#### Alternative Approaches

**Prompt:**
> "Research alternative error-handling strategies for saving data to local storage. Which approach would be most robust?"

---

## Part 3: Practical Exercises

### Exercise 1: Documentation Challenge

Take an undocumented function and generate complete documentation:

1. **Start with this code:**
```javascript
function processData(input, options) {
  const results = [];
  for (let i = 0; i < input.length; i++) {
    if (options.filter && !options.filter(input[i])) continue;
    const processed = options.transform ? options.transform(input[i]) : input[i];
    results.push(processed);
  }
  return options.sort ? results.sort(options.sort) : results;
}
```

2. **Use Copilot to:**
   - Generate JSDoc documentation
   - Add inline comments explaining the logic
   - Create usage examples

### Exercise 2: Refinement Practice

Starting with a basic function, progressively refine it:

1. **Initial Prompt:**
   > "Write a function to list all books in an inventory"

2. **Refinements:**
   - Add pagination support
   - Add sorting by title, author, or date added
   - Add filtering by genre
   - Ensure it handles empty inventories gracefully

### Exercise 3: Code Explanation

Use the code explanation prompts with sample code:

1. **Prompt:**
   > "Explain the logic used in the addBook function, especially how duplicates are handled."

2. **Prompt:**
   > "Suggest ways to optimise the addBook function for performance when handling large inventories."

3. **Prompt:**
   > "Identify any potential edge cases in the searchBooks function and how they could be handled."

### Exercise 4: Test Generation and Refinement

Generate tests and refine them:

1. **Prompt:**
   > "Write unit tests using Jest for the addBook function to ensure it handles duplicates correctly."

2. **Prompt:**
   > "Generate Jest test cases for the searchBooks function, including cases for no results and multiple matches."

3. **Refinement:**
   > "Generate additional test cases for edge scenarios, like searching with an empty query or adding books with missing fields."

---

## Best Practices Summary

### Documentation Generation

| Practice | Description |
|----------|-------------|
| **Document as you go** | Generate docs when writing new functions |
| **Use structured formats** | JSDoc, docstrings, OpenAPI for consistency |
| **Include examples** | Real usage examples aid understanding |
| **Keep docs updated** | Regenerate when code changes significantly |

### Refining Suggestions

| Practice | Description |
|----------|-------------|
| **Never accept blindly** | Always review before accepting |
| **Iterate incrementally** | Build up complexity through refinements |
| **Request alternatives** | Compare different approaches |
| **Test thoroughly** | Verify correctness with unit tests |
| **Apply standards** | Ensure alignment with team conventions |

---

## Key Takeaways

1. **Copilot excels at documentation** - Use it to generate JSDoc, README files, and API docs
2. **Review before accepting** - Every suggestion needs human verification
3. **Iterate to improve** - Start simple, then refine progressively
4. **Maintain single responsibility** - Ask Copilot to break down large functions
5. **Test generated code** - Use Copilot to generate tests, then verify coverage
6. **Debug with context** - Provide error messages and context for better debugging help

---

## Next Steps

- Complete the [Week 2 Lab](3-Week2-Lab.md) to practice customising your Copilot experience with instructions and custom agents
- Review [Week 2 Prompts](4-Week2-Prompts.md) for additional prompt examples and exercises
- Apply these techniques in your daily development workflow
