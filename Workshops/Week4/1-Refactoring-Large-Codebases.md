# Refactoring Large Codebases with GitHub Copilot

**Duration:** 30-45 minutes  
**Format:** Presentation with interactive demonstrations  
**Objective:** Learn techniques for using GitHub Copilot to refactor legacy code, improve code quality, and modernise codebases efficiently.

---

## Session Overview

Refactoring is the process of restructuring existing code without changing its external behaviour. Copilot excels at identifying patterns, suggesting improvements, and helping you navigate complex codebases during refactoring efforts.

**What you'll learn:**
- Techniques for analysing and understanding legacy code
- Patterns for incremental refactoring with Copilot
- Strategies for improving readability and maintainability
- Performance optimisation approaches

---

## 1. Understanding Legacy Code with Copilot

### The Challenge of Legacy Code

| Challenge | How Copilot Helps |
|-----------|-------------------|
| Poor documentation | Generates explanations and adds comments |
| Complex logic | Breaks down and explains intricate code |
| Outdated patterns | Suggests modern equivalents |
| Missing tests | Generates test coverage for existing code |
| Tight coupling | Identifies opportunities for modularisation |

### Code Analysis Prompts

#### Understanding Complex Functions

**Prompt:**
```text
Explain what this function does, identify any code smells, and suggest improvements:

function processData(d, f, x) {
    var r = [];
    for (var i = 0; i < d.length; i++) {
        if (f(d[i])) {
            var t = d[i];
            if (x) {
                t = x(d[i]);
            }
            r.push(t);
        }
    }
    return r;
}
```

**Expected Analysis:**
- Function filters and optionally transforms array elements
- Code smells: unclear variable names, mutable state, imperative style
- Suggestions: use descriptive names, modern array methods, TypeScript types

#### Navigating Large Codebases with Semantic Search

GitHub Copilot Agent mode includes a built-in `semantic_search` tool that searches your codebase by meaning rather than exact text matches. This is especially valuable when exploring unfamiliar or large codebases before making refactoring changes, as it understands intent and context rather than relying on keywords alone.

**When to use `semantic_search`:**

| Use Case | Example Query |
|----------|---------------|
| Find all usages of a concept | *"Find all places where database connections are opened directly"* |
| Locate related patterns | *"Find functions that validate user input"* |
| Impact analysis before renaming | *"Find everything related to order calculations"* |
| Discover inconsistencies | *"Find all error handling patterns in this codebase"* |

**Using `#codebase` in Agent Mode**

In Copilot Chat (Ask or Agent mode), reference the entire workspace with `#codebase` to trigger semantic search across all files:

**Prompt:**
```text
#codebase Find all places where error handling is missing or inconsistent.
List each location with the file path and a brief description of the issue.
```

**Expected behaviour:**
- Copilot searches semantically across all workspace files
- Returns a ranked list of relevant code locations with context
- Groups similar issues together for easier prioritisation

**Impact Analysis Before Refactoring**

Use semantic search to understand the full scope of a change before making it:

**Prompt:**
```text
Before I refactor the 'processOrder' function, use semantic search to find:
1. All direct callers of this function
2. Any functions with similar logic that could be consolidated
3. Tests that cover this function
4. Any documentation or comments that reference it

Provide a summary so I can plan the refactoring safely.
```

**Expected Analysis:**
- Direct callers identified across multiple files
- Related functions that share logic highlighted for potential consolidation
- Test coverage gaps identified
- Documentation that will need updating listed

**Enabling Semantic Search in Prompt Files**

You can explicitly include `semantic_search` in a prompt file to create a reusable refactoring discovery workflow:

**`.github/prompts/refactor-discovery.prompt.md`:**
```markdown
---
agent: 'agent'
name: 'refactor-discovery'
description: 'Discover refactoring opportunities using semantic codebase analysis'
tools: ['semantic_search', 'read_file']
---

# Refactoring Discovery

Search the codebase for the following common refactoring opportunities and provide
a prioritised list of findings:

1. Functions with more than three parameters that could use object destructuring
2. Direct database or API calls outside of dedicated service or repository layers
3. Hardcoded configuration values that should use environment variables
4. Duplicated logic that could be extracted into shared utilities

For each finding, include the file path, function name, and a brief explanation
of why it needs refactoring.
```

> **Note:** Replace `read_file` or add additional tools as needed for your specific workflow. See [VS Code prompt file tools](https://code.visualstudio.com/docs/copilot/chat/chat-tools) for the full list of available built-in tools.

---

#### Identifying Code Smells

**Prompt:**
```text
Analyse this code for code smells and anti-patterns. List each issue with severity (high/medium/low) and suggest fixes:

class UserManager {
    constructor() {
        this.users = [];
        this.database = new Database();
        this.emailService = new EmailService();
        this.logger = new Logger();
        this.cache = new Cache();
    }
    
    createUser(name, email, password, role, department, manager, startDate) {
        // validation
        if (!name) throw new Error('Name required');
        if (!email) throw new Error('Email required');
        if (!password) throw new Error('Password required');
        if (password.length < 8) throw new Error('Password too short');
        if (!email.includes('@')) throw new Error('Invalid email');
        
        const user = { name, email, password, role, department, manager, startDate };
        this.users.push(user);
        this.database.save(user);
        this.emailService.sendWelcome(email);
        this.logger.log('User created: ' + email);
        this.cache.invalidate('users');
        return user;
    }
}
```

**Expected Issues:**
- Too many constructor dependencies (God class)
- Long parameter list
- Password stored in plain text
- Multiple responsibilities in one method
- String concatenation instead of template literals

---

## 2. Incremental Refactoring Strategies

### The Refactoring Workflow

```
1. Understand → 2. Test → 3. Refactor → 4. Verify → 5. Document
```

### Strategy 1: Extract and Rename

Start with the simplest improvements:

**Original Code:**
```javascript
function calc(a, b, c) {
    let x = a * b;
    let y = x + c;
    let z = y * 0.2;
    return y + z;
}
```

**Prompt:**
```text
Refactor this function with:
- Descriptive function and variable names
- Clear comments explaining the business logic
- Extract magic numbers into named constants
```

**Refactored Output:**
```javascript
const VAT_RATE = 0.2;

/**
 * Calculates the total price including VAT.
 * @param {number} quantity - Number of items
 * @param {number} unitPrice - Price per item
 * @param {number} shipping - Shipping cost
 * @returns {number} Final price including VAT
 */
function calculateTotalPriceIncludingVat(quantity, unitPrice, shipping) {
    const subtotal = quantity * unitPrice;
    const totalBeforeTax = subtotal + shipping;
    const vatAmount = totalBeforeTax * VAT_RATE;
    return totalBeforeTax + vatAmount;
}
```

---

### Strategy 2: Modernise Syntax

Update code to use modern language features:

**Original Code:**
```javascript
function fetchUsers(callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/users');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);
            callback(null, data);
        } else {
            callback(new Error('Request failed'));
        }
    };
    xhr.onerror = function() {
        callback(new Error('Network error'));
    };
    xhr.send();
}
```

**Prompt:**
```text
Modernise this code to use:
- async/await syntax
- fetch API
- const/let instead of var
- Arrow functions where appropriate
- Proper error handling with try/catch
```

**Modernised Output:**
```javascript
/**
 * Fetches all users from the API.
 * @returns {Promise<User[]>} Array of user objects
 * @throws {Error} If the request fails
 */
async function fetchUsers() {
    try {
        const response = await fetch('/api/users');
        
        if (!response.ok) {
            throw new Error(`Request failed with status ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        if (error instanceof TypeError) {
            throw new Error('Network error: Unable to reach server');
        }
        throw error;
    }
}
```

---

### Strategy 3: Extract Methods

Break down long functions:

**Original Code:**
```javascript
function processOrder(order) {
    // Validate order
    if (!order.items || order.items.length === 0) {
        throw new Error('Order must have items');
    }
    if (!order.customer) {
        throw new Error('Order must have customer');
    }
    if (!order.customer.email) {
        throw new Error('Customer must have email');
    }
    
    // Calculate totals
    let subtotal = 0;
    for (const item of order.items) {
        subtotal += item.price * item.quantity;
    }
    const tax = subtotal * 0.1;
    const shipping = subtotal > 100 ? 0 : 10;
    const total = subtotal + tax + shipping;
    
    // Save to database
    const savedOrder = database.save({
        ...order,
        subtotal,
        tax,
        shipping,
        total,
        status: 'pending'
    });
    
    // Send confirmation email
    emailService.send({
        to: order.customer.email,
        subject: 'Order Confirmation',
        body: `Your order total is $${total}`
    });
    
    return savedOrder;
}
```

**Prompt:**
```text
Refactor this function by extracting separate methods for:
- Validation
- Price calculation
- Order persistence
- Email notification

Each method should have a single responsibility and be testable in isolation.
```

**Refactored Output:**
```javascript
class OrderProcessor {
    constructor(database, emailService) {
        this.database = database;
        this.emailService = emailService;
    }

    processOrder(order) {
        this.validateOrder(order);
        const pricing = this.calculatePricing(order.items);
        const savedOrder = this.saveOrder(order, pricing);
        this.sendConfirmation(order.customer.email, pricing.total);
        return savedOrder;
    }

    validateOrder(order) {
        if (!order.items?.length) {
            throw new Error('Order must have items');
        }
        if (!order.customer?.email) {
            throw new Error('Customer must have valid email');
        }
    }

    calculatePricing(items) {
        const subtotal = items.reduce(
            (sum, item) => sum + item.price * item.quantity, 
            0
        );
        const tax = subtotal * 0.1;
        const shipping = subtotal > 100 ? 0 : 10;
        
        return { subtotal, tax, shipping, total: subtotal + tax + shipping };
    }

    saveOrder(order, pricing) {
        return this.database.save({
            ...order,
            ...pricing,
            status: 'pending'
        });
    }

    sendConfirmation(email, total) {
        this.emailService.send({
            to: email,
            subject: 'Order Confirmation',
            body: `Your order total is $${total}`
        });
    }
}
```

---

## 3. Improving Readability and Maintainability

### Pattern: Replace Conditionals with Polymorphism

**Original Code:**
```javascript
function calculateShipping(order) {
    if (order.type === 'standard') {
        if (order.weight < 1) return 5;
        if (order.weight < 5) return 10;
        return 15;
    } else if (order.type === 'express') {
        if (order.weight < 1) return 15;
        if (order.weight < 5) return 25;
        return 40;
    } else if (order.type === 'overnight') {
        if (order.weight < 1) return 25;
        if (order.weight < 5) return 45;
        return 75;
    }
    throw new Error('Unknown shipping type');
}
```

**Prompt:**
```text
Refactor this shipping calculation to use the Strategy pattern. Create separate shipping calculators for each type that can be easily extended without modifying existing code.
```

**Refactored Output:**
```javascript
// Shipping strategies
const shippingStrategies = {
    standard: {
        baseRates: { light: 5, medium: 10, heavy: 15 }
    },
    express: {
        baseRates: { light: 15, medium: 25, heavy: 40 }
    },
    overnight: {
        baseRates: { light: 25, medium: 45, heavy: 75 }
    }
};

function getWeightCategory(weight) {
    if (weight < 1) return 'light';
    if (weight < 5) return 'medium';
    return 'heavy';
}

function calculateShipping(order) {
    const strategy = shippingStrategies[order.type];
    
    if (!strategy) {
        throw new Error(`Unknown shipping type: ${order.type}`);
    }
    
    const weightCategory = getWeightCategory(order.weight);
    return strategy.baseRates[weightCategory];
}

// Easy to extend: just add new strategy
shippingStrategies.same_day = {
    baseRates: { light: 35, medium: 55, heavy: 85 }
};
```

---

### Pattern: Replace Magic Numbers and Strings

**Prompt:**
```text
Identify all magic numbers and strings in this code and refactor them into named constants with meaningful names:

function validatePassword(password) {
    if (password.length < 8) return false;
    if (password.length > 128) return false;
    if (!/[A-Z]/.test(password)) return false;
    if (!/[a-z]/.test(password)) return false;
    if (!/[0-9]/.test(password)) return false;
    if (!/[!@#$%^&*]/.test(password)) return false;
    return true;
}
```

**Refactored Output:**
```javascript
const PASSWORD_RULES = {
    MIN_LENGTH: 8,
    MAX_LENGTH: 128,
    PATTERNS: {
        UPPERCASE: /[A-Z]/,
        LOWERCASE: /[a-z]/,
        DIGIT: /[0-9]/,
        SPECIAL: /[!@#$%^&*]/
    }
};

function validatePassword(password) {
    const { MIN_LENGTH, MAX_LENGTH, PATTERNS } = PASSWORD_RULES;
    
    if (password.length < MIN_LENGTH || password.length > MAX_LENGTH) {
        return false;
    }
    
    return Object.values(PATTERNS).every(pattern => pattern.test(password));
}
```

---

## 4. Performance Optimisation

### Identifying Performance Issues

**Prompt:**
```text
Analyse this code for performance issues and suggest optimisations:

function findDuplicates(array) {
    const duplicates = [];
    for (let i = 0; i < array.length; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] === array[j] && !duplicates.includes(array[i])) {
                duplicates.push(array[i]);
            }
        }
    }
    return duplicates;
}
```

**Expected Analysis:**
- O(n²) nested loop complexity
- Additional O(n) check with `includes()`
- Total complexity: O(n³)

**Optimised Output:**
```javascript
/**
 * Finds duplicate values in an array.
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
function findDuplicates(array) {
    const seen = new Set();
    const duplicates = new Set();
    
    for (const item of array) {
        if (seen.has(item)) {
            duplicates.add(item);
        } else {
            seen.add(item);
        }
    }
    
    return Array.from(duplicates);
}
```

---

### Common Performance Optimisations

| Pattern | Before | After | Improvement |
|---------|--------|-------|-------------|
| Array lookup | `array.includes()` | `set.has()` | O(n) → O(1) |
| String concatenation | `str += value` | `array.join()` | O(n²) → O(n) |
| Object creation in loop | `new Object()` | Object pool/reuse | Reduces GC pressure |
| Synchronous iteration | `forEach` | `Promise.all` | Parallel execution |

**Prompt for Memoisation:**
```text
Add memoisation to this recursive Fibonacci function to improve performance:

function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

**Optimised with Memoisation:**
```javascript
function createMemoizedFibonacci() {
    const cache = new Map();
    
    return function fibonacci(n) {
        if (cache.has(n)) {
            return cache.get(n);
        }
        
        if (n <= 1) {
            return n;
        }
        
        const result = fibonacci(n - 1) + fibonacci(n - 2);
        cache.set(n, result);
        return result;
    };
}

const fibonacci = createMemoizedFibonacci();
```

---

## 5. Refactoring Prompting Patterns

### The Analysis-First Pattern

```text
Before refactoring, analyse this code and provide:
1. What the code currently does
2. List of code smells (with severity)
3. Suggested refactoring steps in priority order
4. Potential risks of each refactoring

[paste code here]
```

### The Incremental Improvement Pattern

```text
Refactor this code in small, safe steps. After each step, the code should still work correctly:

Step 1: Rename variables to be more descriptive
Step 2: Extract magic numbers into constants
Step 3: Extract methods for each responsibility
Step 4: Add type annotations/JSDoc comments

[paste code here]
```

### The Modernisation Pattern

```text
Modernise this [language] code to use current best practices:
- Update to [language version] syntax
- Replace deprecated APIs with modern equivalents
- Add proper error handling
- Include type safety where applicable
- Follow [style guide] conventions

[paste code here]
```

---

## Key Takeaways

1. **Understand before refactoring** - Use Copilot to explain complex code first
2. **Use semantic search to map the codebase** - Run `semantic_search` in Agent mode (or use `#codebase`) to find all related code before making changes
3. **Refactor incrementally** - Small, testable changes are safer than big rewrites
4. **Maintain tests** - Generate tests before refactoring to ensure behaviour is preserved
5. **Document decisions** - Have Copilot generate comments explaining why code was changed
6. **Review suggestions critically** - Copilot suggestions may not always be optimal for your context
7. **Measure improvements** - Use metrics to verify refactoring actually improved the code

---

## Next Steps

- Proceed to [Quality Refinements and Standards](2-Quality-Refinements-and-Standards.md) for enforcing coding standards
- Complete the [Week 4 Lab](4-Week4-Lab.md) for hands-on refactoring practice
- Review [Week 4 Prompts](5-Week4-Prompts.md) for additional refactoring prompt examples

---
