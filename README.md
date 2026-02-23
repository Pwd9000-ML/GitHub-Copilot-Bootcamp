# GitHub Copilot Training Program

**Last Updated:** 22/02/2026

A comprehensive 4-week curriculum designed to help developers master GitHub Copilot, from foundational concepts to advanced techniques including prompt engineering, DevOps automation, and ethical AI practices.

## Table of Contents

- [About This Training](#about-this-training)
- [Curriculum](#curriculum)
  - [Week 1: Introduction and Developer Workflow Essentials](#week-1-introduction-and-developer-workflow-essentials)
    - [1. Understanding GitHub Copilot](#1-understanding-github-copilot-45-60-minutes)
    - [2. Setup, Configuration, and Interaction Modes](#2-setup-configuration-and-interaction-modes-45-60-minutes)
    - [3. Hands-On Lab: Getting Started with GitHub Copilot](#3-hands-on-lab-getting-started-with-github-copilot-45-60-minutes)
    - [4. Week 1 Prompt Examples](#4-week-1-prompt-examples-reference-guide-self-study)
    - [Week 1 Feedback](#week-1-feedback)
  - [Week 2: Advanced Development and Support Use Cases](#week-2-advanced-development-and-support-use-cases)
    - [1. Prompt Engineering and Customisation](#1-prompt-engineering-and-customisation-45-60-minutes)
    - [2. Customisation in Practice](#2-customisation-in-practice-45-60-minutes)
    - [3. Hands-On Lab: Customise Your Copilot Experience](#3-hands-on-lab-customise-your-copilot-experience-30-45-minutes)
    - [4. Week 2 Prompt Examples](#4-week-2-prompt-examples-reference-guide-self-study)
    - [Week 2 Feedback](#week-2-feedback)
  - [Week 3: DevOps and Testing with Copilot](#week-3-devops-and-testing-with-copilot)
    - [1. GitHub Copilot CLI for DevOps Automation](#1-github-copilot-cli-for-devops-automation-45-60-minutes)
    - [2. Testing and Quality Assurance with Copilot CLI](#2-testing-and-quality-assurance-with-copilot-cli-45-60-minutes)
    - [3. Hands-On Lab: Create Applications with the Copilot CLI](#3-hands-on-lab-create-applications-with-the-copilot-cli-60-90-minutes)
    - [4. Week 3 Prompt Examples](#4-week-3-prompt-examples-reference-guide-self-study)
    - [Week 3 Feedback](#week-3-feedback)
  - [Week 4: Refactoring, Optimisation, and Ethical Practices](#week-4-refactoring-optimisation-and-ethical-practices)
    - [1. Refactoring Large Codebases](#1-refactoring-large-codebases-30-45-minutes)
    - [2. Quality Refinements and Standards](#2-quality-refinements-and-standards-30-45-minutes)
    - [3. Ethical and Security Considerations](#3-ethical-and-security-considerations-30-45-minutes)
    - [4. Hands-On Lab: Collaborative Refactoring](#4-hands-on-lab-collaborative-refactoring-90-120-minutes)
    - [5. Week 4 Prompt Examples](#5-week-4-prompt-examples-reference-guide-self-study)
    - [Week 4 Feedback](#week-4-feedback)
- [Additional Resources](#additional-resources)
- [Contributing](#contributing)
- [License](#license)

## About This Training

This training program is structured as a progressive learning journey, taking participants from GitHub Copilot basics to advanced usage patterns. Each week builds on the previous, with hands-on labs and reflection exercises to reinforce learning.

**Target Audience:** Developers at any experience level looking to accelerate their workflow with AI-assisted coding.

---

## Curriculum

### Week 1: Introduction and Developer Workflow Essentials

**Duration:** 2-3 hours

**Objective:** Establish a foundational understanding of GitHub Copilot and introduce core workflows for developers.

> **Note:** Copilot features (Ask/Edit/Agent/Plan, shortcuts, and advanced capabilities) vary by IDE and version. Use the [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) as the source of truth.

#### 1. Understanding GitHub Copilot (45-60 minutes)

- Overview of its purpose, architecture, and AI-driven capabilities
- Supported languages, frameworks, and environments
- Copilot in real-world developer workflows
- Value proposition and use cases

**Content:** [1. Understanding GitHub Copilot](Workshops/Week1/1-Understanding-GitHub-Copilot.md)

#### 2. Setup, Configuration, and Interaction Modes (45-60 minutes)

- Installation and setup in multiple IDEs (VS Code - Demo)
- Configuring authentication and preferences
- Basic commands and UI navigation
- Understanding the four core modes: Ask, Edit, Agent, and Plan
- When and how to use each mode effectively
- Custom Agents and Extensions overview
- Troubleshooting common issues
- Best practices for setup

**Content:** [2. Setup, Configuration, and Interaction Modes](Workshops/Week1/2-Setup-and-Configuration.md)

#### 3. Hands-On Lab: Getting Started with GitHub Copilot (45-60 minutes)

- Learn different ways to interact with Copilot to explain, write, debug, and develop code
- Practical application by updating Mergington High School's extracurricular activities website
- Guided exercises covering all interaction modes
- Real-world problem-solving scenarios

**Content:** [3. Hands-On Lab: Getting Started with GitHub Copilot](Workshops/Week1/3-Week1-Lab.md)

#### 4. Week 1 Prompt Examples (Reference Guide Self Study)

- Inline code completions and function suggestions
- Ask mode for code explanations and learning
- Edit mode for controlled code modifications
- Agent mode for multi-file changes
- Plan mode for implementation planning
- Debugging assistance techniques
- Documentation generation patterns

**Content:** [4. Week 1 Prompt Examples](Workshops/Week1/4-Week1-Prompts.md)

#### Week 1 Feedback

- [Submit Week 1 Lab Reflection](../../issues/new?template=week1-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

### Week 2: Advanced Development and Support Use Cases

**Duration:** 2 to 4 hours

**Objective:** Dive deeper into advanced use cases for developers and introduce Copilot as a support tool for maintaining high-quality standards.

#### Reflection
Before starting Week 2, please complete your Week 1 reflections if you haven't already: [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

#### 1. Prompt Engineering and Customisation (45-60 minutes)

- Introduction to **prompt engineering**: crafting effective comments and instructions to guide Copilot
- The CRAFT framework for structuring prompts
- Writing effective prompts for code explanation and generation
- Generating code aligned with organisational standards using the three pillars of customisation:
  - **Instruction files** (`.instructions.md`) for project-wide conventions
  - **Prompt files** (`.prompt.md`) for reusable task templates
  - **Custom agent files** (`.agent.md`) for specialised personas with scoped tools and handoffs
- Incorporating pre-emptive security recommendations
- Practical prompt exercises with examples (including custom agent creation)

**Content:** [1. Prompt Engineering and Customisation](Workshops/Week2/1-Prompt-Engineering-and-Customisation.md)

#### 2. Customisation in Practice (45-60 minutes)

- Applying instruction files, prompt files, and custom agents to real developer workflows
- Documentation generation with Copilot (JSDoc, README, API docs)
- The Review-Refine-Iterate cycle for improving suggestions
- Refining Copilot suggestions for scoped, maintainable code
- Debugging with Copilot assistance
- Progressive refinement techniques

**Content:** [2. Customisation in Practice](Workshops/Week2/2-Customisation-in-Practice.md)

#### 3. Hands-On Lab: Customise Your Copilot Experience (30-45 minutes)

- Set up repository-wide custom instructions
- Create targeted custom instructions for specific file types
- Build reusable prompt templates for common tasks
- Configure custom agents for specialised workflows
- Practice customising your Copilot experience

**Content:** [3. Hands-On Lab: Customise Your Copilot Experience](Workshops/Week2/3-Week2-Lab.md)

#### 4. Week 2 Prompt Examples (Reference Guide Self Study)

- Template generation for reusable functions
- Project scaffolding and directory structures
- Custom scaffolding for architecture patterns
- Code generation with constraints
- Code explanation and debugging prompts
- Unit test generation techniques
- SQL query generation patterns

**Content:** [4. Week 2 Prompt Examples](Workshops/Week2/4-Week2-Prompts.md)

#### Week 2 Feedback

- [Submit Week 2 Lab Reflection](../../issues/new?template=week2-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

### Week 3: DevOps and Testing with Copilot

**Duration:** 2 to 2.5 hours (1 session)

**Objective:** Equip participants to use Copilot — in the IDE and the CLI — for CI/CD automation and testing, with the Copilot CLI integrated into every topic rather than treated as a standalone tool.

#### Reflection
Before starting Week 3, please complete your Week 2 reflections if you haven't already: [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

#### 1. GitHub Copilot CLI for DevOps Automation (45-60 minutes)

- Copilot CLI quick start: installation (WinGet, Homebrew, npm), slash commands, and headless mode
- Interactive vs programmatic modes and session management
- CI/CD pipeline generation from the IDE and the CLI
- Infrastructure as Code (Docker, Kubernetes, Terraform) with CLI generation
- Incident response and log analysis from the terminal
- Built-in agents (Explore, Task, Plan, Code-review) and context management
- Pre-review validation for deployment readiness (including CLI-powered checks)
- Effective DevOps prompting patterns, security permissions, and `/delegate` workflow

**Content:** [1. GitHub Copilot CLI for DevOps Automation](Workshops/Week3/1-DevOps-Automation.md)

#### 2. Testing and Quality Assurance with Copilot CLI (45-60 minutes)

- Unit test generation from the IDE and the CLI
- Ensuring repeatable test coverage with CLI gap analysis
- Test optimisation and parameterisation
- Framework conversion (with full examples in Week 3 Prompts)
- Quality assurance checklists and testing best practices

**Content:** [2. Testing and Quality Assurance with Copilot CLI](Workshops/Week3/2-Testing-and-Quality-Assurance.md)

#### 3. Hands-On Lab: Create Applications with the Copilot CLI (60-90 minutes)

- Install and configure the standalone GitHub Copilot CLI
- Use Copilot CLI to create GitHub issues from templates
- Build a Node.js calculator application with iterative CLI guidance
- Practice collaborative development with Copilot on the command line
- Explore `/delegate` and `/share` commands

**Content:** [3. Hands-On Lab: Create Applications with the Copilot CLI](Workshops/Week3/3-Week3-Lab.md)

#### 4. Week 3 Prompt Examples (Reference Guide Self Study)

- CI/CD pipeline generation for GitHub Actions and GitLab CI (IDE and CLI)
- Infrastructure as Code (Docker, Kubernetes, Terraform) with CLI generation
- Test generation with coverage requirements and CLI gap analysis
- Validation and security scanning prompts
- Test optimisation and framework conversion with CLI bulk operations

**Content:** [4. Week 3 Prompt Examples](Workshops/Week3/4-Week3-Prompts.md)

#### Week 3 Feedback

- [Submit Week 3 Lab Reflection](../../issues/new?template=week3-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

### Week 4: Refactoring, Optimisation, and Ethical Practices

**Duration:** 3 to 4.5 hours (1 session or 3 × 30-45 minutes)

**Objective:** Focus on enhancing code quality through refactoring, fostering ethical AI use, and reinforcing long-term Copilot adoption.

#### Reflection
Before starting Week 4, please complete your Week 3 reflections if you haven't already: [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

#### 1. Refactoring Large Codebases (30-45 minutes)

- Understanding and navigating legacy code
- Using semantic search to map and explore large codebases
- Incremental refactoring strategies (extract, rename, modernise)
- Improving readability, maintainability, and performance
- Prompting patterns for complex refactoring

**Content:** [1. Refactoring Large Codebases](Workshops/Week4/1-Refactoring-Large-Codebases.md)

#### 2. Quality Refinements and Standards (30-45 minutes)

- Enforcing coding standards through Copilot prompts
- Using instruction files for project-wide standards
- Automated code review and quality checks
- Building quality gates into your workflow

**Content:** [2. Quality Refinements and Standards](Workshops/Week4/2-Quality-Refinements-and-Standards.md)

#### 3. Ethical and Security Considerations (30-45 minutes)

- Intellectual property concerns in AI-generated code
- Security vulnerabilities and prevention strategies
- Responsible AI usage and bias awareness
- Organisational policies and compliance

**Content:** [3. Ethical and Security Considerations](Workshops/Week4/3-Ethical-and-Security-Considerations.md)

#### 4. Hands-On Lab: Collaborative Refactoring (90-120 minutes)

- Legacy code assessment and documentation
- Incremental refactoring with test coverage
- Quality standards enforcement
- Pair refactoring and security audit exercises

**Content:** [4. Hands-On Lab: Collaborative Refactoring](Workshops/Week4/4-Week4-Lab.md)

#### 5. Week 4 Prompt Examples (Reference Guide Self Study)

- Refactoring prompts for legacy code analysis
- Quality standards and compliance checking
- Security audit and vulnerability detection
- Ethical AI and bias detection prompts
- Code review patterns and SOLID principles
- Combination prompts for complete workflows

**Content:** [5. Week 4 Prompt Examples](Workshops/Week4/5-Week4-Prompts.md)

#### Week 4 Feedback

- [Submit Week 4 Lab Reflection](../../issues/new?template=week4-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

## Additional Resources

- [IDE Support Guide](FAQ/IDE-support.md) - Detailed information on Copilot features per IDE
- [Language Support](FAQ/language-support.md) - Language-specific limitations, best practices, and integration guidance
- [Facilitator Guide](FAQ/facilitator-guide.md) - For trainers delivering this curriculum
- [Participant Quickstart](FAQ/participant-quickstart.md) - Quick reference for participants

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this training program.

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

---

