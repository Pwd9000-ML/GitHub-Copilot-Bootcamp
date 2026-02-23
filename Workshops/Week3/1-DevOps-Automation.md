# GitHub Copilot CLI for DevOps Automation

**Duration:** 45-60 minutes  
**Format:** Presentation with interactive demonstrations  
**Objective:** Learn to leverage the standalone GitHub Copilot CLI, alongside the IDE, for automating CI/CD pipelines, generating Infrastructure as Code, and validating deployments.

---

## Session Overview

DevOps automation is one of Copilot's strongest use cases. The repetitive nature of pipeline configurations, infrastructure definitions, and validation scripts makes them ideal for AI-assisted generation. In this session you will use both the **VS Code Chat** experience and the standalone **Copilot CLI** side by side, learning when each tool fits best.

**What you'll learn:**
- Install Copilot CLI (WinGet, Homebrew, npm) and understand interactive vs programmatic modes
- Use built-in agents, session management, context management, and security permissions
- Generate CI/CD pipelines for various platforms, from the IDE and the CLI
- Create Infrastructure as Code (IaC) configurations (Docker, Kubernetes, Terraform)
- Perform incident response and log analysis from the terminal
- Build pre-deployment validation scripts
- Use headless mode to embed Copilot in scripts and pipelines
- Delegate generated work to pull requests with `/delegate`

---

## Copilot CLI Quick Start

The standalone Copilot CLI brings agentic AI to your terminal, where DevOps work already happens. Instead of covering the CLI in isolation, we use it throughout every topic below alongside the VS Code Chat experience.

> **Note:** The standalone GitHub Copilot CLI replaces the retired `gh copilot` extension. It is a separate application, not a GitHub CLI extension. See [GitHub Copilot CLI documentation](https://docs.github.com/en/copilot/github-copilot-in-the-cli) for details.

**Prerequisites:** An active GitHub Copilot subscription (Pro, Pro+, Business, or Enterprise). Node.js 22+ is required for the npm installation method.

```bash
# Option 1: Windows (WinGet)
winget install GitHub.Copilot

# Option 2: macOS/Linux (Homebrew)
brew install copilot-cli

# Option 3: npm (macOS, Linux, or Windows, requires Node.js 22+)
npm install -g @github/copilot

# Verify installation
copilot --version

# Authenticate with GitHub
copilot /login
```

### Interactive vs Programmatic Modes

Copilot CLI supports two main usage patterns:

- **Interactive mode:** Launch `copilot` with no arguments to open a conversational session. Use slash commands to navigate context, delegate tasks, and manage agents.
- **Programmatic (headless) mode:** Pass a prompt directly with flags for non-interactive use in scripts, Makefiles, pre-commit hooks, and CI pipeline steps. Example: `copilot --allow-all-tools -p "your prompt"`.

### Key Slash Commands

| Command | Purpose |
|---------|---------|
| `/delegate` | Create a PR with generated changes |
| `/agent` | Use built-in or custom agents (e.g. `Explore`, `Task`, `Plan`, `Code-review`) |
| `/mcp` | Manage MCP servers (GitHub repos, issues, PRs) |
| `/share` | Export session as Markdown |
| `/cwd` | Change working directory |
| `/add-dir` | Add directory to context |
| `/model` | Switch AI model |
| `/terminal-setup` | Configure terminal integration |
| `/usage` | Show current token usage |
| `/context` | Display loaded context and files |
| `/compact` | Compress session context (auto-triggers at 95% token limit) |

### Session Management

Resume or continue previous sessions to maintain context across terminal restarts:

```bash
# Continue the most recent session
copilot --continue

# Resume a specific past session by selecting from history
copilot --resume
```

### Built-in Agents

Call built-in agents via the `/agent` command for specialised workflows:

| Agent | Purpose |
|-------|---------|
| `Explore` | Open-ended research and exploration |
| `Task` | Execute a specific, well-defined task |
| `Plan` | Break a goal into steps and produce an implementation plan |
| `Code-review` | Review code for bugs, style issues, and improvements |

```bash
copilot
> /agent Code-review Review all Terraform files in ./infrastructure for security issues and best practices
```

### Security Permissions

By default, Copilot CLI asks before executing any tool. Use granular `--allow-tool` flags to pre-approve specific tools in headless or CI scenarios:

```bash
# Allow only kubectl and helm commands
copilot --allow-tool 'shell(kubectl)' --allow-tool 'shell(helm)' -p "Check the health of all pods in the staging namespace"

# Allow all tools (use with caution, appropriate for trusted CI environments)
copilot --allow-all-tools -p "your prompt"

# Allow specific URL access
copilot --allow-url 'https://api.github.com/*' -p "Fetch the latest release for my repo"
```

> **Tip:** In production CI pipelines, prefer granular `--allow-tool` flags over `--allow-all-tools` to follow the principle of least privilege.

---

## 1. CI/CD Pipeline Generation

### Why Use Copilot for CI/CD?

| Challenge | How Copilot Helps |
|-----------|-------------------|
| Syntax complexity | Generates valid YAML/JSON with correct indentation and structure |
| Platform variations | Knows conventions for GitHub Actions, Azure DevOps, GitLab CI, Jenkins |
| Boilerplate code | Quickly scaffolds common patterns (build, test, deploy) |
| Best practices | Suggests caching, parallelisation, and optimisation techniques |

### Pipeline Generation Strategy

Build pipelines incrementally using progressive prompts:

```
Step 1: Basic Build → Step 2: Add Tests → Step 3: Add Deploy → Step 4: Add Notifications
```

This approach allows you to:
- Verify each step works before adding complexity
- Understand what Copilot generates
- Customise each section for your needs

---

### GitHub Actions Pipeline Examples

#### Step 1: Create a Basic Build Pipeline

**Prompt:**
```text
Write a GitHub Actions workflow YAML file for a Node.js project that includes build and test steps.
```

**Expected Output:**
```yaml
name: Node.js CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x, 20.x]

    steps:
      - uses: actions/checkout@v4

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint

      - name: Run tests
        run: npm test

      - name: Build
        run: npm run build
```

#### Step 2: Add Deployment Stage

**Prompt:**
```text
Extend this pipeline to include a deployment step for staging that only runs on the main branch.
```

**Expected Addition:**
```yaml
  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: staging
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy to staging
        run: |
          echo "Deploying to staging environment"
          # Add your deployment commands here
        env:
          DEPLOY_TOKEN: ${{ secrets.STAGING_DEPLOY_TOKEN }}
```

#### Step 3: Add Notifications

**Prompt:**
```text
Add a step to notify the team on Slack when the build succeeds or fails.
```

**Expected Addition:**
```yaml
  notify:
    needs: [build, deploy-staging]
    runs-on: ubuntu-latest
    if: always()
    
    steps:
      - name: Notify Slack
        uses: slackapi/slack-github-action@v1.25.0
        with:
          payload: |
            {
              "text": "Build ${{ needs.build.result }}: ${{ github.repository }}",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Build Result:* ${{ needs.build.result }}\n*Staging Deploy Result:* ${{ needs['deploy-staging'].result }}\n*Repository:* ${{ github.repository }}\n*Branch:* ${{ github.ref_name }}\n*Commit:* ${{ github.sha }}"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
```

---

### Platform-Specific Pipeline Prompts

#### Terminal (Copilot CLI)

Generate pipelines directly from the terminal, no IDE required:

**Interactive mode:**
```bash
copilot
> Create a GitHub Actions workflow for a Node.js 20 app that builds, tests with coverage, lints, and deploys to Azure App Service on main branch. Include caching and matrix strategy for Node 18 and 20.
```

**Headless mode (scriptable):**
```bash
# Generate and save directly
copilot --allow-all-tools -p "Create a GitHub Actions workflow for a Node.js app with build, test, linting, and deployment to staging on main" > .github/workflows/ci.yml

# Generate and create a PR in one flow
copilot
> Create a GitHub Actions CI/CD pipeline for this repo with build, test, and deploy stages
> /delegate
```

The `/delegate` command is particularly powerful for DevOps. It creates a pull request with all the generated files, adds a description, and submits it for review.

#### Azure DevOps

```text
Create an Azure DevOps YAML pipeline for a .NET 8 application with:
- Build and test stages
- Code coverage reporting
- Artifact publishing
- Deployment to Azure App Service
```

#### GitLab CI

```text
Generate a .gitlab-ci.yml file for a Python Django application with:
- Linting with flake8
- Unit tests with pytest
- Docker image build and push to registry
- Deployment to Kubernetes
```

#### Jenkins

```text
Create a Jenkinsfile for a Java Maven project with:
- Parallel test execution
- SonarQube code analysis
- Artifact deployment to Nexus
- Slack notifications
```

---

### CI/CD Best Practices Prompts

| Goal | Prompt |
|------|--------|
| **Caching** | "Add dependency caching to speed up the Node.js CI workflow" |
| **Parallelisation** | "Modify the pipeline to run linting and tests in parallel" |
| **Security scanning** | "Add a security vulnerability scan step using npm audit" |
| **Conditional execution** | "Only run deployment when changes are in the src/ directory" |
| **Environment variables** | "Add environment-specific configuration using GitHub secrets" |

---

## 2. Infrastructure as Code (IaC)

### IaC Generation with Copilot

Copilot understands major IaC tools and cloud provider APIs:

| Tool | Use Case |
|------|----------|
| **Docker** | Containerisation, local development |
| **Docker Compose** | Multi-container applications |
| **Kubernetes** | Container orchestration |
| **Terraform** | Multi-cloud infrastructure provisioning |
| **Helm** | Kubernetes package management |
| **Bicep/ARM** | Azure-specific infrastructure |
| **CloudFormation** | AWS-specific infrastructure |

---

### Docker Examples

#### Basic Dockerfile

**Prompt:**
```text
Create a Dockerfile for a Node.js application running on port 3000.
```

Copilot generates a production-ready Dockerfile using `node:20-alpine` as the base image, with `npm ci --omit=dev` for efficient dependency installation, a non-root `USER node` directive for security, and an `EXPOSE 3000` port declaration.

#### Multi-Stage Dockerfile

**Prompt:**
```text
Create a multi-stage Dockerfile for a React application with nginx serving the production build.
```

Copilot produces a two-stage build: a `node:20-alpine` builder stage that installs dependencies and runs `npm run build`, followed by an `nginx:alpine` production stage that copies the built assets, adds a health check, and serves on port 80.

---

### Docker Compose Examples

**Prompt:**
```text
Create a docker-compose.yml file for a Node.js app with MongoDB and Redis for development.
```

Copilot generates a complete Compose file with three services (app, mongo, redis), volume mounts for live reloading and data persistence, environment variable wiring between containers, and port mappings for local development.

---

### Kubernetes Examples

#### Basic Deployment

**Prompt:**
```text
Generate a Kubernetes deployment YAML file for a Node.js app with 3 replicas, resource limits, and health checks.
```

Copilot outputs a Deployment manifest with 3 replicas, CPU/memory resource requests and limits, liveness and readiness probes on `/health` and `/ready` endpoints, environment variables, and a companion ClusterIP Service on port 80 targeting container port 3000.

---

### Terraform Examples

**Prompt:**
```text
Generate a Terraform configuration to provision an AWS EC2 instance with a security group allowing HTTP and SSH access.
```

Copilot generates a complete Terraform configuration including provider setup, input variables for region and instance type, a security group with HTTP/SSH ingress rules, an EC2 instance referencing the latest Amazon Linux 2 AMI via a data source, and an output for the public IP.

> **Tip:** For full code examples of each IaC prompt above, see the [Week 3 Prompts](4-Week3-Prompts.md) reference guide.

---

### Generating IaC from the CLI

The CLI excels at IaC because you can work directly in the directory where configs live:

```bash
# Navigate to your infrastructure directory
copilot
> /cwd ./infrastructure

# Generate Docker, K8s, and Terraform in context
> Create a production Dockerfile for the Node.js app in the parent directory. Use multi-stage build, non-root user, and health checks.

# Add multiple directories for cross-referencing
> /add-dir ./k8s
> /add-dir ./terraform
> Review all infrastructure configs and ensure consistency between Docker, Kubernetes, and Terraform resource definitions.
```

**Headless IaC generation:**
```bash
# Generate a Dockerfile
copilot --allow-all-tools -p "Create a production multi-stage Dockerfile for a Node.js Express app on port 3000 with security best practices" > Dockerfile

# Generate Kubernetes manifests
copilot --allow-all-tools -p "Create K8s deployment, service, and HPA for a Node.js app with 3 replicas, health checks, and resource limits" > k8s/deployment.yml

# Generate and submit as a PR
copilot
> Generate Terraform configuration for an AWS VPC with public/private subnets, ALB, and ECS Fargate cluster
> /delegate
```

---

## 3. Incident Response and Log Analysis

The CLI is particularly powerful for incident response, where speed matters and you are already working in the terminal.

### Analysing Logs from the Terminal

```bash
# Pipe logs directly into Copilot for analysis, using least privilege as no tools are required for this task
copilot -p "Analyse these Kubernetes pod logs and identify the root cause of the crash loop" < /tmp/pod-logs.txt

# Interactive incident investigation
copilot
> /add-dir ./logs
> Analyse the error patterns in these application logs. Identify the most frequent errors, their likely root causes, and suggest fixes in priority order.
```

### Correlating Across Services

```bash
copilot
> /add-dir ./logs/api
> /add-dir ./logs/worker
> /add-dir ./logs/gateway
> Correlate errors across these three services. Identify the timeline of failures and determine which service triggered the cascade.
```

### Quick Diagnostics

```bash
# Check cluster health and diagnose issues
copilot --allow-tool 'shell(kubectl)' -p "List all pods in CrashLoopBackOff state across all namespaces, then fetch their logs and suggest fixes"

# Headless monitoring check
copilot --allow-tool 'shell(curl)' -p "Check the health endpoints for these services: api:3000/health, web:8080/health, worker:5000/health. Report any that are down."
```

> **Tip:** During incidents, use `copilot --continue` to maintain context across multiple terminal sessions as you investigate.

---

## 4. Pre-Review Validation for Deployment

### Why Validation Matters

Pre-deployment validation catches issues early:
- **Syntax errors** in configuration files
- **Missing environment variables** or secrets
- **Security vulnerabilities** in dependencies
- **Configuration drift** between environments

### Validation Script Generation

Use Copilot to generate validation scripts that catch issues before deployment. Each prompt below produces a ready-to-run script or workflow.

| Prompt | What Copilot Generates |
|--------|------------------------|
| _Write a shell script to validate all YAML files in a directory and report any syntax errors._ | A Bash script that recursively finds `.yaml`/`.yml` files, validates each with `python3 -c "import yaml; yaml.safe_load(...)"`, and exits with the error count. |
| _Create a script that verifies all required environment variables are set before deployment._ | A Bash script that loops over a `REQUIRED_VARS` array, reports missing variables, and exits non-zero if any are absent. |
| _Add validation steps to a GitHub Actions workflow that check YAML syntax, Dockerfile best practices, and security vulnerabilities._ | A `validate` job with steps for `yamllint`, `hadolint`, `trufflehog`, `npm audit`, and `kubectl --dry-run` on Kubernetes manifests. |

> **Tip:** Full code outputs for all three prompts are available in the [Week 3 Prompt Examples](4-Week3-Prompts.md#4-validation-and-security-scanning) reference guide.

---

### Validating from the CLI

Validate configurations from the terminal before committing:

```bash
# Interactive validation review
copilot
> /add-dir .github/workflows
> /add-dir k8s
> /add-dir .
> Validate all YAML files in these directories. Check for syntax errors, security issues, and missing best practices. Report findings as a checklist.

# Headless validation in a pre-commit hook or CI step
copilot --allow-all-tools -p "Check all Dockerfiles in this repo for security issues: hardcoded secrets, running as root, using latest tags, missing health checks"
```

**Using CLI in a CI Pipeline (GitHub Actions):**
```yaml
jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install Copilot CLI
        run: npm install -g @github/copilot
      
      - name: AI-Powered Config Review
        run: |
          copilot --allow-all-tools -p "Review the Kubernetes manifests in k8s/ for security best practices and report any issues"
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

## Effective DevOps Prompting Patterns

### The Specification Pattern

```text
Create a [resource type] for [application type]:
- Running on [port/environment]
- With [dependencies/services]
- Including [features like health checks, logging]
- Following [security/compliance requirements]
```

### The Incremental Build Pattern

```text
1. "Create a basic CI workflow with build step"
2. "Add test step with coverage reporting"
3. "Add deployment to staging environment"
4. "Add production deployment with approval gate"
5. "Add rollback capability on failure"
```

### The Security-First Pattern

```text
Generate [resource] with security best practices:
- Non-root user execution
- Minimal base image
- No hardcoded secrets
- Resource limits defined
- Network policies applied
```

### The Delegate Pattern

Use `/delegate` to go from idea to pull request in one session:

```bash
copilot
> Create a complete CI/CD pipeline for this Node.js project:
> 1. GitHub Actions workflow with build, test, security scan, and deploy stages
> 2. Production Dockerfile with multi-stage build
> 3. Kubernetes deployment with health checks and HPA
> Review all the files you've created and ensure they are consistent.
> /delegate
```

This creates a PR with all generated files, a descriptive title, and a summary body, ready for team review.

### The Monorepo Context Pattern

Use `/add-dir` and `/cwd` to work across services in a monorepo:

```bash
copilot
> /add-dir ./services/api
> /add-dir ./services/web
> /add-dir ./infrastructure
> Create a GitHub Actions workflow that builds and tests both the api and web services in parallel, then deploys them together
```

---

## Key Takeaways

1. **Build incrementally** - Start with basic pipelines and add complexity step by step
2. **Be specific** - Include ports, versions, and environment details in prompts
3. **Include security** - Always ask for security best practices and use granular `--allow-tool` flags
4. **Validate early** - Add validation steps to catch issues before deployment
5. **Use platform conventions** - Let Copilot leverage its knowledge of CI/CD best practices
6. **Review generated code** - Always verify configurations before applying them
7. **Use CLI for terminal workflows** - Copilot CLI brings AI directly to where DevOps work happens
8. **Automate with headless mode** - Embed `copilot --allow-all-tools -p` in scripts and CI steps
9. **Delegate to PRs** - Use `/delegate` to go from generation to pull request in one flow
10. **Leverage built-in agents** - Use `Explore`, `Task`, `Plan`, and `Code-review` for specialised workflows
11. **Manage context** - Use `/usage`, `/context`, and `/compact` to stay within token limits
12. **Resume sessions** - Use `--continue` and `--resume` to maintain context across terminal restarts

---

## Next Steps

- Proceed to [Testing and Quality Assurance with Copilot CLI](2-Testing-and-Quality-Assurance.md) for test automation techniques
- Complete the [Week 3 Lab](3-Week3-Lab.md) for hands-on practice
- Review [Week 3 Prompts](4-Week3-Prompts.md) for additional DevOps prompt examples

---

