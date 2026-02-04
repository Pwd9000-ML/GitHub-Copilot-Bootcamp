# GitHub Copilot Prompt Examples - Week 3: DevOps & Testing

## Session Overview

**Purpose:** Reference guide for DevOps and testing prompts  
**Format:** Example prompts with explanations and tips  
**Objective:** Provide prompting techniques for CI/CD pipelines, Infrastructure as Code (IaC), test generation, and DevOps automation.

---

## Contents

- [1. CI/CD Pipeline Generation](#1-cicd-pipeline-generation)
- [2. Infrastructure as Code (IaC)](#2-infrastructure-as-code-iac)
- [3. Test Generation](#3-test-generation)
- [4. Validation and Security Scanning](#4-validation-and-security-scanning)
- [5. Test Optimisation](#5-test-optimisation)

---

## 1. CI/CD Pipeline Generation

CI/CD pipeline generation creates automated workflows for build, test, and deployment processes.

- Use structured prompts with specific requirements for pipeline steps
- Define triggers, job dependencies, and artifacts
- Create multi-stage pipelines with deployment environments
- Include validation jobs and parallel execution strategies

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
- Sends a Slack notification on completion that summarises the build and deploy results using `needs.<job_id>.result`
```

#### Validation Job with Dependencies

```text
Add a validation job to my GitHub Actions workflow that runs first and includes:
- YAML linting with yamllint
- Security scanning with npm audit
- Dockerfile linting with hadolint
- Secret detection with trufflehog
The other jobs should depend on this validation passing.

If needed, install yamllint in the job using `python3 -m pip install yamllint`.
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

Infrastructure as Code prompts create Docker configurations, Kubernetes manifests, and cloud templates.

- Specify infrastructure requirements with security best practices
- Include environment configuration and resource optimisation
- Create multi-stage Docker builds for production
- Generate Kubernetes manifests with health checks and autoscaling
- Build Terraform/CloudFormation templates with proper security groups

### Example Prompts

#### Optimised Dockerfile

```text
Create a production Dockerfile for a Node.js Express application that:
- Uses multi-stage build for smaller image size
- Runs as non-root user for security
- Only copies production dependencies
- Installs dependencies with `npm ci --omit=dev`
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

Test generation creates comprehensive test suites with proper coverage and edge case handling.

- Specify test framework and coverage requirements
- Include edge cases and boundary conditions
- Generate unit tests, integration tests, and parameterised tests
- Use proper mocking for external dependencies
- Test async functions and error scenarios

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
- Use `%p` placeholders in the test name to handle non-integer inputs
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

Validation and security scanning creates pre-deployment checks to catch issues early in the pipeline.

- Create validation scripts for environment variables and connections
- Integrate security scanning tools (npm audit, Trivy, CodeQL)
- Add configuration linting for YAML, Dockerfile, and Terraform
- Implement secret detection in CI pipelines
- Fail builds early when issues are detected

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

## 5. Test Optimisation

Test optimisation refactors and improves existing tests for better maintainability and performance.

- Convert tests between frameworks (Selenium to Cypress)
- Extract common setup into reusable utilities
- Create test fixtures and reusable test data
- Enable parallel test execution for faster feedback
- Identify and fix slow test operations

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
- Optimise test database setup
```

#### Improve Test Performance

```text
Optimise these integration tests that are taking too long:
[paste test code]
- Identify slow operations
- Use transaction rollback instead of database cleanup
- Mock slow external APIs
- Reduce unnecessary test data creation
```

> **Tip:** When converting frameworks, ask Copilot to explain key differences to understand the changes better.

---

## Week 3 Feedback

Please complete the following reflections after completing Week 3 activities:

- [Submit Week 3 Lab Reflection](../../issues/new?template=week3-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

## Next Steps

After mastering DevOps automation and testing with Copilot in Week 3, we will explore refactoring, quality standards, and ethical AI practices in Week 4.

**[← Back to Main README](../../README.md)** | **[Continue to Week 4 →](../Week4/1-Refactoring-Large-Codebases.md)**
