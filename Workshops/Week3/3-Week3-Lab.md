# Week 3 - DevOps and Testing Hands-On Lab

Practice CI/CD automation, infrastructure generation, and comprehensive test coverage using GitHub Copilot.

---

## Welcome

- **Who is this for**: Developers looking to accelerate DevOps workflows and testing practices
- **What you'll learn**: How to use Copilot for CI/CD pipelines, IaC generation, and automated testing
- **What you'll build**: A complete CI/CD pipeline with infrastructure configurations and a comprehensive test suite
- **Prerequisites**: 
  - Completion of Week 1 and Week 2 exercises
  - Basic understanding of CI/CD concepts
  - Familiarity with at least one testing framework
- **How long**: This exercise takes 60-90 minutes to complete (core exercises). Extension options available for additional practice.

In this exercise, you will:

1. Create a CI/CD pipeline using GitHub Actions
2. Generate Docker and Kubernetes configurations
3. Build validation scripts for deployment readiness
4. Generate comprehensive unit tests with Copilot
5. Optimise tests using parameterisation

---

## Part 1: CI/CD Pipeline Generation

### Exercise 1.1: Create a Node.js CI Pipeline

**Objective:** Generate a GitHub Actions workflow for a Node.js application.

**Instructions:**

1. Open Copilot Chat in VS Code
2. Use the following prompt:

```text
Create a GitHub Actions workflow for a Node.js 20 application that:
- Triggers on push to main and pull requests
- Runs on ubuntu-latest
- Includes steps for: checkout, setup Node.js with caching, install dependencies, run linter, run tests with coverage, and build
- Uploads test coverage as an artifact
```

3. Review the generated workflow
4. Save as `.github/workflows/ci.yml` (or note it down for reference)

**Expected Outcome:** A complete CI workflow with build, test, and coverage steps.

**Discussion Points:**
- What additional steps might you add for your projects?
- How would you modify this for a monorepo?

**Extension Options (Optional):**
If you have extra time, try extending the pipeline:
- Add a staging deployment job that runs only on main branch
- Add environment approval requirements
- Include Slack/email notifications on build status

---

### Exercise 1.2: Create a Validation Job

**Objective:** Add pre-deployment validation to catch issues early.

**Instructions:**

1. Use this prompt:

```text
Add a validation job to the workflow that runs first and includes:
- YAML linting with yamllint
- Security scanning with npm audit
- Dockerfile linting with hadolint
- Secret detection with trufflehog
The other jobs should depend on this validation passing.
```

2. Observe how Copilot chains jobs with dependencies
3. Consider which validations are most important for your projects

---

## Part 2: Infrastructure as Code

### Exercise 2.1: Generate a Production Dockerfile

**Objective:** Create an optimised, secure Dockerfile.

**Instructions:**

1. Open a new file or Copilot Chat
2. Use this prompt:

```text
Create a production Dockerfile for a Node.js Express application that:
- Uses multi-stage build for smaller image size
- Runs as non-root user for security
- Only copies production dependencies
- Includes health check
- Uses node:20-alpine as base
- Application runs on port 3000
```

3. Review the generated Dockerfile
4. Identify the security best practices included

**Key Points to Review:**
- Multi-stage build benefits
- Using `npm ci --only=production`
- Non-root user configuration
- Health check configuration

---

### Exercise 2.2: Generate Kubernetes Deployment

**Objective:** Create Kubernetes manifests for production deployment.

**Instructions:**

1. Use this prompt:

```text
Generate Kubernetes manifests for deploying the Node.js app including:
- Deployment with 3 replicas, resource limits (128Mi memory, 100m CPU), and rolling update strategy
- Service of type ClusterIP
- Horizontal Pod Autoscaler scaling between 3-10 replicas at 70% CPU
- ConfigMap for environment variables
- Secret for sensitive data (database URL, API keys)
Include proper labels and health probes.
```

2. Review each generated resource
3. Understand how components connect together

**Extension Option (Optional):**
If you have time, generate a docker-compose.yml for local development with PostgreSQL, Redis, and hot reload.

---

## Part 3: Test Generation

### Exercise 3.1: Generate Unit Tests for a Function

**Objective:** Create comprehensive tests for existing code.

**Instructions:**

1. Create or open a file with this function:

```javascript
// utils/calculator.js
function calculateOrderTotal(items, discountCode = null) {
    if (!Array.isArray(items) || items.length === 0) {
        throw new Error('Items must be a non-empty array');
    }

    let subtotal = items.reduce((sum, item) => {
        if (!item.price || !item.quantity) {
            throw new Error('Each item must have price and quantity');
        }
        return sum + (item.price * item.quantity);
    }, 0);

    let discount = 0;
    if (discountCode === 'SAVE10') {
        discount = subtotal * 0.1;
    } else if (discountCode === 'SAVE20') {
        discount = subtotal * 0.2;
    } else if (discountCode && discountCode !== null) {
        throw new Error('Invalid discount code');
    }

    const total = subtotal - discount;
    return {
        subtotal: subtotal,
        discount: discount,
        total: total
    };
}

module.exports = { calculateOrderTotal };
```

2. Use this prompt with the code in context:

```text
Generate comprehensive Jest tests for the calculateOrderTotal function. Include:
- Valid calculations with single and multiple items
- All discount code scenarios (SAVE10, SAVE20, invalid, null)
- Error cases for invalid input (empty array, missing price/quantity)
- Edge cases (very large numbers, zero values)
Use descriptive test names following the pattern "should [expected] when [condition]"
```

3. Review the generated tests for completeness

**Extension Option (Optional):**
If time permits, refactor the discount code tests to use Jest's test.each for parameterized testing to reduce code duplication.

---

### Exercise 3.2: Generate Async Tests with Mocking

**Objective:** Test async functions with mocked dependencies.

**Instructions:**

1. Consider this async function:

```javascript
// services/userService.js
const db = require('../db');

async function getUserWithOrders(userId) {
    const user = await db.findUser(userId);
    if (!user) {
        throw new Error('User not found');
    }
    
    const orders = await db.findOrdersByUser(userId);
    
    return {
        ...user,
        orders: orders,
        totalOrders: orders.length
    };
}

module.exports = { getUserWithOrders };
```

2. Use this prompt:

```text
Generate Jest tests for getUserWithOrders that:
- Mock the db module using jest.mock
- Test successful retrieval with orders
- Test user not found scenario
- Test empty orders array
- Test database error handling
Include proper async/await syntax and mock setup/teardown.
```

3. Understand how mocking isolates the function under test

**Extension Option (Optional):**
If you have extra time, try converting a Mocha/Chai/Sinon test to Jest to understand framework differences and migration patterns.

---

## Part 4: Integration Challenge

### Exercise 4.1: Complete DevOps Pipeline

**Objective:** Bring everything together into a complete solution.

**Instructions:**

1. Create a unified prompt that generates:

```text
For a Node.js Express API project, generate a complete DevOps setup:

1. GitHub Actions workflow with:
   - Validation job (lint, security scan)
   - Test job with coverage threshold of 80%
   - Build Docker image job
   - Deploy to staging job (on main branch)

2. Production Dockerfile (multi-stage, secure)

3. Kubernetes manifests:
   - Deployment with health checks
   - Service
   - Ingress with TLS

4. Pre-deployment validation script that checks:
   - All YAML files are valid
   - Required environment variables are set
   - Docker image builds successfully
```

2. Review how the components work together
3. Identify any missing pieces for production readiness

---

## Reflection and Discussion

### What Worked Well?

Consider:
- Which prompts produced the best results?
- How did context affect the quality of generated code?
- What patterns did you notice in effective prompts?

### What Required Refinement?

Consider:
- Which generated code needed the most changes?
- What context was missing that would have helped?
- How did you iterate to improve results?

### Best Practices Learned

Document:
- Your most effective prompt patterns
- Common adjustments needed for your project
- Tips for future DevOps automation tasks

---

## Bonus Challenges

### Challenge 1: Multi-Environment Pipeline

Create a pipeline that deploys to:
- Development (on any push)
- Staging (on main branch)
- Production (manual approval required)

### Challenge 2: Database Migration Integration

Add database migration steps to the deployment pipeline with:
- Migration validation before deploy
- Automatic rollback on failure
- Migration status notifications

### Challenge 3: End-to-End Test Integration

Add Cypress E2E tests to the pipeline that:
- Run against the staging deployment
- Record videos on failure
- Block production deployment on failure

---

## Submission

### Lab Reflection

After completing the lab, submit your reflection:

- [Submit Week 3 Lab Reflection](../../issues/new?template=week3-lab.yml)

Include:
- Which exercises you completed
- Most effective prompts you used
- Challenges encountered and how you solved them
- Key learnings about DevOps automation with Copilot

### Weekly Reflection

- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---
