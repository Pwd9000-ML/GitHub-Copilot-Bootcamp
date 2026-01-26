# GitHub Copilot Prompt Examples - Week 3: DevOps & Testing

A comprehensive guide to prompting techniques for CI/CD pipelines, Infrastructure as Code (IaC), test generation, and DevOps automation.

---

## Table of Contents

1. [CI/CD Pipeline Generation](#1-cicd-pipeline-generation)
2. [Infrastructure as Code (IaC)](#2-infrastructure-as-code-iac)
3. [Test Generation](#3-test-generation)
4. [Validation and Security Scanning](#4-validation-and-security-scanning)
5. [Test Optimization](#5-test-optimization)

---

## 1. CI/CD Pipeline Generation

**Technique:** Use structured prompts with specific requirements for pipeline steps, triggers, and job dependencies.

**When to use:** When creating or extending CI/CD workflows for build, test, and deployment automation.

### Example Prompts

#### Basic CI Pipeline

```text
Create a GitHub Actions workflow for a Node.js 20 application that:
- Triggers on push to main and pull requests
- Runs on ubuntu-latest
- Includes steps for: checkout, setup Node.js with caching, install dependencies, run linter, run tests with coverage, and build
- Uploads test coverage as an artifact
```

#### Multi-Stage Pipeline with Deployment

```text
Generate a GitHub Actions workflow with:
- A build job that compiles the application and runs tests
- A staging deployment job that runs only on main branch after tests pass
- Uses environment: staging with required approval
- Deploys to Azure App Service
- Sends Slack notification on completion
```

#### Validation Job with Dependencies

```text
Add a validation job to my GitHub Actions workflow that runs first and includes:
- YAML linting with yamllint
- Security scanning with npm audit
- Dockerfile linting with hadolint
- Secret detection with trufflehog
The other jobs should depend on this validation passing.
```

#### Platform-Specific Pipelines

```text
Create a GitLab CI pipeline for a Python application that:
- Runs tests in parallel across Python 3.9, 3.10, and 3.11
- Generates coverage reports
- Deploys to staging on merge to main
- Uses Docker images for consistency
```

> **Tip:** Be specific about trigger conditions, job dependencies, and artifacts to ensure proper workflow orchestration.

---

## 2. Infrastructure as Code (IaC)

**Technique:** Specify infrastructure requirements with security best practices, environment configuration, and resource optimization.

**When to use:** When creating Docker configurations, Kubernetes manifests, or Terraform/CloudFormation templates.

### Example Prompts

#### Optimized Dockerfile

```text
Create a production Dockerfile for a Node.js Express application that:
- Uses multi-stage build for smaller image size
- Runs as non-root user for security
- Only copies production dependencies
- Includes health check
- Uses node:20-alpine as base
- Application runs on port 3000
```

#### Docker Compose for Development

```text
Create a docker-compose.yml for local development with:
- Node.js application service with hot reload (volume mounts)
- PostgreSQL database with persistent volume
- Redis for caching
- Proper environment variables
- Network configuration for service communication
```

#### Kubernetes Deployment

```text
Generate Kubernetes manifests for a Node.js microservice including:
- Deployment with 3 replicas and health checks
- Service for load balancing
- ConfigMap for environment variables
- Horizontal Pod Autoscaler (HPA) based on CPU
- Resource limits and requests
```

#### Terraform Infrastructure

```text
Create a Terraform configuration for AWS that provisions:
- VPC with public and private subnets across 2 availability zones
- Application Load Balancer
- ECS cluster with Fargate for containerized applications
- RDS PostgreSQL database in private subnet
- Security groups with least-privilege access
```

#### Environment-Specific Configuration

```text
Generate a Helm values file for production deployment with:
- High availability (5 replicas)
- Resource limits: CPU 1000m, Memory 2Gi
- Production database connection string
- Horizontal autoscaling configuration
- Rolling update strategy
```

> **Tip:** Always include security considerations (non-root users, resource limits, health checks) in IaC prompts.

---

## 3. Test Generation

**Technique:** Specify test framework, coverage requirements, and edge cases to generate comprehensive test suites.

**When to use:** When creating unit tests, integration tests, or improving test coverage for existing code.

### Example Prompts

#### Unit Tests for Existing Code

```text
Generate comprehensive unit tests for this calculateTotal function using Jest. Include:
- Happy path with valid items
- Edge cases (empty array, null, undefined)
- Boundary conditions (zero prices, large numbers)
- Mock external dependencies
```

#### Test Suite with High Coverage

```text
Create a complete Jest test suite for the UserService class that:
- Tests all public methods
- Achieves >90% code coverage
- Uses proper mocking for database calls
- Includes setup and teardown
- Tests error scenarios
```

#### Parameterized Tests

```text
Generate parameterized tests for the validateEmail function using Jest's test.each:
- Test valid email formats (standard, with +, with subdomains)
- Test invalid formats (missing @, missing domain, special chars)
- Use descriptive test names for each case
```

#### Integration Tests

```text
Create integration tests for the API endpoint /api/users using supertest and Jest:
- Test successful user creation (POST)
- Test retrieving users (GET)
- Test authentication requirements
- Test validation errors
- Setup test database and cleanup
```

#### Async Function Tests

```text
Write Jest tests for this async fetchUserData function that:
- Tests successful data retrieval
- Tests network errors
- Tests timeout scenarios
- Uses async/await syntax
- Mocks the fetch API
```

> **Tip:** Specify the test framework and what should be mocked to get tests that match your project structure.

---

## 4. Validation and Security Scanning

**Technique:** Create pre-deployment validation scripts and security scanning steps to catch issues early.

**When to use:** In CI/CD pipelines before deployment, or as pre-commit hooks.

### Example Prompts

#### Pre-Deployment Validation Script

```text
Create a Node.js validation script that checks:
- All required environment variables are set
- Database connection is successful
- External API dependencies are reachable
- Configuration files are valid JSON/YAML
- Returns exit code 0 on success, 1 on failure
```

#### Security Scanning Integration

```text
Add to my GitHub Actions workflow:
- npm audit for dependency vulnerabilities
- Trivy for container image scanning
- SAST scanning with CodeQL
- License compliance checking
- Fail the build if high severity issues found
```

#### Configuration Linting

```text
Create a validation job that lints:
- YAML files with yamllint
- Dockerfile with hadolint
- Terraform with terraform fmt and validate
- Display errors and fail if any issues found
```

#### Secret Detection

```text
Add secret scanning to my CI pipeline using:
- trufflehog to scan git history
- Custom regex patterns for API keys
- Fail the build if secrets detected
- Report findings as GitHub Security alert
```

> **Tip:** Integrate validation early in the pipeline to fail fast and save compute resources.

---

## 5. Test Optimization

**Technique:** Refactor and optimize existing tests for better maintainability, performance, and coverage.

**When to use:** When tests are slow, repetitive, or difficult to maintain.

### Example Prompts

#### Convert Test Framework

```text
Convert these Selenium tests to Cypress:
[paste Selenium test code]
- Maintain the same test coverage
- Use Cypress best practices
- Update assertions to Cypress syntax
- Simplify wait conditions
```

#### Extract Test Utilities

```text
Refactor these Jest tests to reduce duplication:
[paste test code]
- Extract common setup into beforeEach
- Create helper functions for repeated assertions
- Use describe blocks to organize tests
- Improve test names for clarity
```

#### Add Test Fixtures

```text
Create test fixtures for the User model tests:
- Valid user data (multiple personas)
- Invalid data for validation testing
- Edge case data
- Export as reusable test data
```

#### Parallel Test Execution

```text
Modify this Jest configuration to:
- Run tests in parallel using maxWorkers
- Split slow tests into separate files
- Use test.concurrent for independent tests
- Optimize test database setup
```

#### Improve Test Performance

```text
Optimize these integration tests that are taking too long:
[paste test code]
- Identify slow operations
- Use transaction rollback instead of database cleanup
- Mock slow external APIs
- Reduce unnecessary test data creation
```

> **Tip:** When converting frameworks, ask Copilot to explain key differences to understand the changes better.

---

## Quick Reference: DevOps & Testing Prompts

| Task | Key Elements to Include | Example Keywords |
|------|------------------------|------------------|
| **CI Pipeline** | Triggers, jobs, dependencies, artifacts | "on push", "needs", "upload artifact", "cache" |
| **Dockerfile** | Multi-stage, security, optimization | "multi-stage", "non-root", "alpine", "health check" |
| **Kubernetes** | Replicas, health checks, resources, HPA | "replicas: 3", "readinessProbe", "limits", "autoscale" |
| **Unit Tests** | Framework, coverage, mocking, edge cases | "Jest", "90% coverage", "mock", "edge cases" |
| **Validation** | Checks, exit codes, error handling | "validate", "exit code", "fail if", "lint" |
| **Test Conversion** | Source/target framework, best practices | "convert from X to Y", "best practices", "syntax" |

---

## Best Practices for Week 3

### CI/CD Best Practices
1. **Fail Fast:** Put validation jobs first in the pipeline
2. **Cache Dependencies:** Cache npm/pip/maven dependencies to speed up builds
3. **Parallel Jobs:** Run independent jobs in parallel to reduce total time
4. **Environment Secrets:** Never hardcode secrets; use GitHub Secrets or vault solutions
5. **Incremental Builds:** Only build/test what changed when possible

### IaC Best Practices
1. **Multi-Stage Builds:** Use for smaller, more secure Docker images
2. **Health Checks:** Always include readiness and liveness probes
3. **Resource Limits:** Set memory and CPU limits to prevent resource exhaustion
4. **Non-Root Users:** Run containers as non-root for security
5. **Configuration as Code:** Store all infrastructure configuration in version control

### Testing Best Practices
1. **Test Pyramid:** Many unit tests, fewer integration tests, minimal E2E tests
2. **Fast Tests:** Keep unit tests fast (<100ms each) for quick feedback
3. **Isolated Tests:** Each test should be independent and not rely on others
4. **Clear Names:** Use descriptive test names that explain what is being tested
5. **Meaningful Assertions:** Test behavior, not implementation details

---

## Common Pitfalls to Avoid

### CI/CD
- ❌ **Don't:** Run all tests sequentially when they could be parallel
- ✅ **Do:** Organize tests into parallel jobs based on test type or module

- ❌ **Don't:** Use latest tag for Docker images in production
- ✅ **Do:** Pin specific versions for reproducible builds

### IaC
- ❌ **Don't:** Copy-paste configurations without understanding them
- ✅ **Do:** Ask Copilot to explain generated configs before using them

- ❌ **Don't:** Forget health checks and resource limits
- ✅ **Do:** Always include liveness/readiness probes and set resource constraints

### Testing
- ❌ **Don't:** Accept generated tests without verifying they actually test the right behavior
- ✅ **Do:** Run generated tests and verify they catch real bugs

- ❌ **Don't:** Mock everything, including the code under test
- ✅ **Do:** Only mock external dependencies and test the actual code logic

---

## Next Steps

After mastering DevOps and Testing with Copilot:
- Apply these patterns to your real projects
- Experiment with different CI/CD platforms (GitHub Actions, GitLab CI, Jenkins)
- Explore advanced Kubernetes patterns (service mesh, operators)
- Move on to Week 4 for refactoring, quality standards, and ethical AI practices

For related prompting techniques, see:
- [Week 2 Prompt Engineering](../Week2/4-Week2-Prompts.md) - CRAFT framework and documentation
- [Week 4 Refactoring Prompts](../Week4/5-Week4-Prompts.md) - Code quality and security
