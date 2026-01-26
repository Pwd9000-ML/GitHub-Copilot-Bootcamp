# Week 4 Lab: Collaborative Refactoring and Quality Improvement

**Duration:** 90-120 minutes (core exercises). Additional extension options available.  
**Format:** Hands-on collaborative exercises  
**Prerequisites:** Completion of Week 4 sessions (Refactoring, Quality Standards, Ethics)

---

## Lab Overview

This lab brings together all Week 4 concepts through collaborative exercises that simulate real-world scenarios. You'll work with legacy code, apply quality standards, and address security concerns using GitHub Copilot.

**Learning Objectives:**
- Apply incremental refactoring strategies to legacy code
- Enforce coding standards using Copilot
- Identify and fix security vulnerabilities
- Practice responsible AI-assisted development
- Collaborate effectively using AI tools

---

## Lab Setup

### Prerequisites Checklist

- [ ] VS Code with GitHub Copilot extension installed
- [ ] Git configured and repository access
- [ ] Language runtime installed (Node.js/Python/Java as applicable)
- [ ] Copilot Chat panel accessible

### Workspace Preparation

Create a new folder for the lab exercises:
```bash
mkdir week4-lab
cd week4-lab
git init
```

---

## Part 1: Legacy Code Assessment (25 minutes)

### Exercise 1.1: Code Archaeology

**Scenario:** You've inherited a legacy order processing system. Your first task is to understand and document what it does.

**Starter Code - Create `legacy-order-processor.js`:**
```javascript
// Legacy Order Processor - v1.2 (2019)
// Original author unknown, multiple contributors

var config = {
    tax: 0.20,
    discount: 0.1,
    threshold: 100,
    api_key: "sk_live_1234567890abcdef",
    db_connection: "mongodb://admin:password@localhost:27017"
};

function process(o) {
    var t = 0;
    for (var i = 0; i < o.items.length; i++) {
        var item = o.items[i];
        if (item.qty > 0) {
            t = t + (item.price * item.qty);
        }
    }
    
    if (t > config.threshold) {
        t = t - (t * config.discount);
    }
    
    var tax = t * config.tax;
    t = t + tax;
    
    var result = {
        orderId: o.id,
        items: o.items,
        subtotal: t - tax,
        tax: tax,
        total: t,
        status: "pending"
    };
    
    // Log to file
    var fs = require('fs');
    fs.appendFileSync('orders.log', JSON.stringify(result) + '\n');
    
    // Send to external API
    var http = require('http');
    var req = http.request({
        host: 'api.payments.com',
        path: '/process?key=' + config.api_key,
        method: 'POST'
    });
    req.write(JSON.stringify(result));
    req.end();
    
    return result;
}

function validate(o) {
    if (o == null || o == undefined) return false;
    if (o.items == null) return false;
    if (o.items.length == 0) return false;
    return true;
}

function getOrder(id) {
    var db = require('./db');
    var query = "SELECT * FROM orders WHERE id = '" + id + "'";
    return db.query(query);
}

module.exports = { process, validate, getOrder, config };
```

**Task 1: Documentation Generation**

Use Copilot Chat to analyse the code:

```text
Prompt: Analyse this legacy code and create documentation:
1. What is the main purpose of this module?
2. What are the inputs and outputs?
3. Identify any code smells or issues
4. What dependencies does it have?
5. What configuration does it require?

[paste the code]
```

**Expected Deliverable:** A markdown documentation file explaining the codebase.

---

**Task 2: Risk Assessment**

```text
Prompt: Perform a risk assessment on this legacy code:
- Security vulnerabilities (critical, high, medium, low)
- Technical debt items
- Maintenance concerns
- Compliance issues

Provide a prioritised remediation plan.
```

**Checklist - Did you identify:**
- [ ] Hardcoded API key
- [ ] Hardcoded database credentials
- [ ] SQL injection vulnerability
- [ ] Synchronous file operations
- [ ] Missing error handling
- [ ] Poor variable naming
- [ ] No input validation for individual items

**Extension Option (Optional):**
Generate a comprehensive test suite (characterization tests) for the legacy code before refactoring to ensure safe refactoring. Create `legacy-order-processor.test.js` with tests that pass with the current implementation.

---

## Part 2: Incremental Refactoring (30 minutes)

### Exercise 2.1: Security Hardening

**Priority 1 - Remove Hardcoded Secrets**

```text
Prompt: Refactor this code to remove hardcoded secrets:
- Use environment variables
- Add validation for required config
- Create a secure configuration loader
- Maintain backward compatibility

Current code:
var config = {
    api_key: "sk_live_1234567890abcdef",
    db_connection: "mongodb://admin:password@localhost:27017"
};
```

**Expected Output - Create `config.js`:**
```javascript
require('dotenv').config();

const requiredEnvVars = [
  'TAX_RATE',
  'DISCOUNT_RATE',
  'DISCOUNT_THRESHOLD',
  'PAYMENT_API_KEY',
  'DATABASE_URL',
];

function validateConfig() {
  const missing = requiredEnvVars.filter(
    (envVar) => !process.env[envVar]
  );
  
  if (missing.length > 0) {
    throw new Error(
      `Missing required environment variables: ${missing.join(', ')}`
    );
  }
}

validateConfig();

module.exports = {
  taxRate: parseFloat(process.env.TAX_RATE),
  discountRate: parseFloat(process.env.DISCOUNT_RATE),
  discountThreshold: parseFloat(process.env.DISCOUNT_THRESHOLD),
  paymentApiKey: process.env.PAYMENT_API_KEY,
  databaseUrl: process.env.DATABASE_URL,
};
```

**Create `.env.example`:**
```env
TAX_RATE=0.20
DISCOUNT_RATE=0.10
DISCOUNT_THRESHOLD=100
PAYMENT_API_KEY=your_api_key_here
DATABASE_URL=mongodb://localhost:27017/orders
```

---

### Exercise 2.2: Fix SQL Injection

```text
Prompt: Refactor this function to prevent SQL injection:
- Use parameterised queries
- Add input validation
- Include proper error handling
- Add TypeScript types (or JSDoc)

function getOrder(id) {
    var db = require('./db');
    var query = "SELECT * FROM orders WHERE id = '" + id + "'";
    return db.query(query);
}
```

**Verify your refactored code:**
- [ ] Uses parameterised queries
- [ ] Validates the ID format
- [ ] Handles database errors
- [ ] Returns null/undefined for not found
- [ ] Has proper documentation

**Extension Option (Optional):**
If you have extra time, modernize the function syntax to ES2022+ standards using const/let, arrow functions, array methods (reduce, filter, map), destructuring, and async/await. Create `order-processor.mjs`.

---

## Part 3: Quality Standards Enforcement (25 minutes)

### Exercise 3.1: Apply Coding Standards

**Task:** Create a project configuration that enforces quality standards.

**Generate ESLint Configuration:**
```text
Prompt: Generate an ESLint configuration for a Node.js project that enforces:
- No var declarations
- Required semicolons
- Consistent spacing (2 spaces)
- Maximum line length 100
- Required JSDoc for functions
- No console.log
- No unused variables
- Security-focused rules
```

**Generate Prettier Configuration:**
```text
Prompt: Generate a Prettier configuration matching our ESLint rules
and a package.json with lint and format scripts.
```

**Verification:**
- [ ] Created `.eslintrc.js`
- [ ] Created `.prettierrc`
- [ ] Added scripts to `package.json`
- [ ] Running `npm run lint` reports issues in legacy code
- [ ] Running `npm run format` applies consistent formatting

---

### Exercise 3.2: Documentation Standards

**Task:** Generate comprehensive documentation for your refactored code.

```text
Prompt: Generate JSDoc documentation for this refactored module that includes:
- Module overview
- Function descriptions with @param and @returns
- @throws documentation
- @example for each public function
- Type definitions

[paste your refactored code]
```

**Create a README for the module:**
```text
Prompt: Generate a README.md for this Order Processing module with:
- Overview and purpose
- Installation steps
- Environment configuration table
- Usage examples
- API reference
- Testing instructions
```

---

### Exercise 3.3: Code Review Simulation

**Task:** Use Copilot to perform a code review on your refactored code.

```text
Prompt: Perform a senior developer code review on this refactored code:
1. Check for any remaining code smells
2. Verify security best practices
3. Assess test coverage adequacy
4. Review documentation completeness
5. Identify any missed edge cases
6. Suggest any final improvements

Be critical and thorough.

[paste refactored code]
```

**Address the feedback:**
- [ ] Document review findings
- [ ] Implement suggested improvements
- [ ] Re-run review to verify fixes

---

## Part 4: Collaborative Exercise (30 minutes)

### Exercise 4.1: Pair Refactoring

**Scenario:** Work with a partner (or simulate both roles) to refactor the remaining functionality.

**Role A - Navigator:**
- Describes what changes need to be made
- Reviews Copilot suggestions
- Ensures tests pass after each change

**Role B - Driver:**
- Writes prompts for Copilot
- Implements suggestions
- Runs tests and linting

**Task:** Convert the entire `process` function to be:
- Fully async
- Properly error-handled
- Following the single responsibility principle
- Fully tested

**Collaborate using these prompts:**

**Navigator provides requirements:**
```text
We need to extract these responsibilities:
1. Calculate subtotal
2. Apply discounts  
3. Calculate tax
4. Create order record
5. Log order
6. Submit payment

Each should be a separate, testable function.
```

**Driver implements:**
```text
Prompt: Extract a calculateSubtotal function from this code:
- Accept an array of items
- Calculate total of price * quantity
- Filter out items with qty <= 0
- Return the subtotal

Include tests using Jest.
```

**Continue for each extracted function.**

---

### Exercise 4.2: Security Audit

**Task:** Perform a collaborative security audit using Copilot.

**Step 1 - Threat Modelling:**
```text
Prompt: Perform threat modelling for this order processing system:
- What are the assets?
- Who are the threat actors?
- What are the attack vectors?
- What are the potential impacts?

Create a threat matrix with risk scores.
```

**Step 2 - Security Testing:**
```text
Prompt: Generate security test cases for this API:
- SQL injection attempts
- Invalid input handling
- Authentication bypass attempts
- Rate limiting tests

Use Jest with appropriate assertions.
```

**Step 3 - Remediation Verification:**
```text
Prompt: Create a security checklist to verify all vulnerabilities are fixed.
Include automated tests where possible.
```

---

## Part 5: Reflection and Best Practices (10 minutes)

### Exercise 5.1: Document Learnings

Create a `LESSONS-LEARNED.md` file:

```text
Prompt: Help me document lessons learned from this refactoring exercise:
- What worked well with Copilot?
- What required manual intervention?
- What security issues were easy/hard to catch?
- What would you do differently?

Format as a retrospective document.
```

### Exercise 5.2: Best Practices Checklist

Generate a reusable checklist:

```text
Prompt: Create a comprehensive checklist for refactoring legacy code with AI assistance:
- Pre-refactoring preparation
- Security considerations
- Testing requirements
- Quality standards
- Documentation needs
- Review process

Make it suitable for team use.
```

---

## Lab Deliverables

By the end of this lab, you should have:

| Deliverable | Description |
|-------------|-------------|
| `legacy-order-processor.js` | Original code (unchanged for reference) |
| `legacy-order-processor.test.js` | Characterisation tests |
| `config.js` | Secure configuration loader |
| `.env.example` | Environment variable template |
| `order-processor.mjs` | Refactored modern implementation |
| `order-processor.test.js` | Comprehensive test suite |
| `.eslintrc.js` | ESLint configuration |
| `.prettierrc` | Prettier configuration |
| `README.md` | Module documentation |
| `LESSONS-LEARNED.md` | Retrospective document |

---

## Bonus Challenges

### Challenge 1: TypeScript Migration

Convert the entire module to TypeScript:
```text
Prompt: Migrate this JavaScript module to TypeScript:
- Add interfaces for all data structures
- Use strict type checking
- Add generic types where applicable
- Create type guards for validation
```

### Challenge 2: Performance Optimisation

```text
Prompt: Analyse this code for performance issues:
- Identify inefficient operations
- Suggest caching strategies
- Recommend batch processing for multiple orders
- Add performance tests
```

### Challenge 3: API Design

```text
Prompt: Design a RESTful API around this order processing logic:
- OpenAPI specification
- Input validation middleware
- Error response format
- Rate limiting
- Authentication
```

---

## Assessment Criteria

| Criterion | Excellent | Good | Needs Improvement |
|-----------|-----------|------|-------------------|
| **Security** | All vulnerabilities fixed, security tests added | Most vulnerabilities fixed | Security issues remain |
| **Code Quality** | Clean, modern code, passes all linting | Mostly clean, minor issues | Multiple code smells |
| **Testing** | >90% coverage, edge cases covered | >70% coverage | Insufficient tests |
| **Documentation** | Complete, clear, with examples | Adequate documentation | Missing or unclear |
| **Collaboration** | Effective pair programming, good prompts | Worked together adequately | Limited collaboration |

---

## Next Steps

- Review the [Week 4 Prompts](5-Week4-Prompts.md) for additional reference
- Share your refactored code for peer review
- Apply these techniques to your own codebase
