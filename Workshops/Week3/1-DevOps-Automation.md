# DevOps Automation with GitHub Copilot

**Duration:** 30-45 minutes  
**Format:** Presentation with interactive demonstrations  
**Objective:** Learn to leverage GitHub Copilot for automating CI/CD pipelines, generating Infrastructure as Code, and ensuring deployment readiness.

---

## Session Overview

DevOps automation is one of Copilot's strongest use cases. The repetitive nature of pipeline configurations, infrastructure definitions, and validation scripts makes them ideal for AI-assisted generation.

**What you'll learn:**
- Generate CI/CD pipelines for various platforms
- Create Infrastructure as Code (IaC) configurations
- Build pre-deployment validation scripts
- Apply DevOps best practices through effective prompting

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
              "text": "Build ${{ job.status }}: ${{ github.repository }}",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Build Status:* ${{ job.status }}\n*Repository:* ${{ github.repository }}\n*Branch:* ${{ github.ref_name }}\n*Commit:* ${{ github.sha }}"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
```

---

### Platform-Specific Pipeline Prompts

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

**Expected Output:**
```dockerfile
# Use official Node.js runtime as base image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application source
COPY . .

# Expose port
EXPOSE 3000

# Set non-root user for security
USER node

# Start the application
CMD ["node", "src/index.js"]
```

#### Multi-Stage Dockerfile

**Prompt:**
```text
Create a multi-stage Dockerfile for a React application with nginx serving the production build.
```

**Expected Output:**
```dockerfile
# Build stage
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy custom nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy built assets from builder stage
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --quiet --tries=1 --spider http://localhost/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
```

---

### Docker Compose Examples

**Prompt:**
```text
Create a docker-compose.yml file for a Node.js app with MongoDB and Redis for development.
```

**Expected Output:**
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - MONGODB_URI=mongodb://mongo:27017/myapp
      - REDIS_URL=redis://redis:6379
    volumes:
      - .:/app
      - /app/node_modules
    depends_on:
      - mongo
      - redis
    restart: unless-stopped

  mongo:
    image: mongo:7
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db
    environment:
      - MONGO_INITDB_DATABASE=myapp

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  mongo_data:
  redis_data:
```

---

### Kubernetes Examples

#### Basic Deployment

**Prompt:**
```text
Generate a Kubernetes deployment YAML file for a Node.js app with 3 replicas, resource limits, and health checks.
```

**Expected Output:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nodejs-app
  labels:
    app: nodejs-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nodejs-app
  template:
    metadata:
      labels:
        app: nodejs-app
    spec:
      containers:
        - name: nodejs-app
          image: myregistry/nodejs-app:latest
          ports:
            - containerPort: 3000
          resources:
            requests:
              memory: "128Mi"
              cpu: "100m"
            limits:
              memory: "256Mi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 5
          env:
            - name: NODE_ENV
              value: "production"
            - name: PORT
              value: "3000"
---
apiVersion: v1
kind: Service
metadata:
  name: nodejs-app-service
spec:
  selector:
    app: nodejs-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
  type: ClusterIP
```

---

### Terraform Examples

**Prompt:**
```text
Generate a Terraform configuration to provision an AWS EC2 instance with a security group allowing HTTP and SSH access.
```

**Expected Output:**
```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region"
  default     = "eu-west-2"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t3.micro"
}

# Security Group
resource "aws_security_group" "app_sg" {
  name        = "app-security-group"
  description = "Allow HTTP and SSH traffic"

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Restrict in production
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "app-security-group"
  }
}

# EC2 Instance
resource "aws_instance" "app_server" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type

  vpc_security_group_ids = [aws_security_group.app_sg.id]

  tags = {
    Name = "app-server"
  }
}

# Get latest Amazon Linux 2 AMI
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

output "instance_public_ip" {
  value = aws_instance.app_server.public_ip
}
```

---

## 3. Pre-Review Validation for Deployment

### Why Validation Matters

Pre-deployment validation catches issues early:
- **Syntax errors** in configuration files
- **Missing environment variables** or secrets
- **Security vulnerabilities** in dependencies
- **Configuration drift** between environments

### Validation Script Generation

#### YAML Validation

**Prompt:**
```text
Write a shell script to validate all YAML files in a directory and report any syntax errors.
```

**Expected Output:**
```bash
#!/bin/bash

# YAML Validation Script
# Validates all YAML files in the specified directory

set -e

DIRECTORY="${1:-.}"
ERRORS=0

echo "Validating YAML files in: $DIRECTORY"
echo "=================================="

# Find all YAML files
for file in $(find "$DIRECTORY" -name "*.yaml" -o -name "*.yml"); do
    echo -n "Checking $file... "
    
    if python3 -c "import yaml; yaml.safe_load(open('$file'))" 2>/dev/null; then
        echo "✓ Valid"
    else
        echo "✗ Invalid"
        python3 -c "import yaml; yaml.safe_load(open('$file'))" 2>&1 || true
        ERRORS=$((ERRORS + 1))
    fi
done

echo "=================================="
echo "Validation complete. Errors found: $ERRORS"

exit $ERRORS
```

#### Environment Variable Check

**Prompt:**
```text
Create a script that verifies all required environment variables are set before deployment.
```

**Expected Output:**
```bash
#!/bin/bash

# Environment Variable Validation Script

REQUIRED_VARS=(
    "DATABASE_URL"
    "API_KEY"
    "NODE_ENV"
    "PORT"
)

MISSING=0

echo "Checking required environment variables..."
echo "=========================================="

for var in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!var}" ]; then
        echo "✗ Missing: $var"
        MISSING=$((MISSING + 1))
    else
        echo "✓ Set: $var"
    fi
done

echo "=========================================="

if [ $MISSING -gt 0 ]; then
    echo "Error: $MISSING required variable(s) not set"
    exit 1
else
    echo "All required variables are set"
    exit 0
fi
```

---

### CI Pipeline Validation Steps

**Prompt:**
```text
Add validation steps to a GitHub Actions workflow that check YAML syntax, Dockerfile best practices, and security vulnerabilities.
```

**Expected Output:**
```yaml
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Validate YAML files
        run: |
          pip install yamllint
          yamllint -d relaxed .

      - name: Lint Dockerfile
        uses: hadolint/hadolint-action@v3.1.0
        with:
          dockerfile: Dockerfile

      - name: Check for secrets in code
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          extra_args: --only-verified

      - name: Security audit - npm
        run: npm audit --audit-level=high

      - name: Validate Kubernetes manifests
        run: |
          curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
          chmod +x kubectl
          ./kubectl apply --dry-run=client -f k8s/ -R
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

---

## Key Takeaways

1. **Build incrementally** - Start with basic pipelines and add complexity step by step
2. **Be specific** - Include ports, versions, and environment details in prompts
3. **Include security** - Always ask for security best practices
4. **Validate early** - Add validation steps to catch issues before deployment
5. **Use platform conventions** - Let Copilot leverage its knowledge of CI/CD best practices
6. **Review generated code** - Always verify configurations before applying them

---

## Next Steps

- Proceed to [Testing and Quality Assurance](2-Testing-and-Quality-Assurance.md) for test automation techniques
- Complete the [Week 3 Lab](3-Week3-Lab.md) for hands-on practice
- Review [Week 3 Prompts](4-Week3-Prompts.md) for additional DevOps prompt examples

---

