# GitHub Copilot Training Program

**Last Updated:** 12/05/2026

A comprehensive 5-week curriculum designed to help developers master GitHub Copilot, from foundational concepts to advanced techniques including prompt engineering, agentic workflows, Copilot CLI, Copilot cloud agent, customisation, DevOps automation, testing, code review, governance, and ethical AI practices.

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
  - [Week 3: MCP Servers and GitHub Copilot](#week-3-mcp-servers-and-github-copilot)
    - [1. MCP Foundations: Connecting GitHub Copilot to the World](#1-mcp-foundations-connecting-github-copilot-to-the-world-45-60-minutes)
    - [2. MCP in Production: GitHub, Copilot CLI, and Governance](#2-mcp-in-production-github-copilot-cli-and-governance-45-60-minutes)
    - [3. Hands-On Lab: Integrate MCP with GitHub Copilot](#3-hands-on-lab-integrate-mcp-with-github-copilot-60-90-minutes)
    - [4. Week 3 Prompt Examples](#4-week-3-prompt-examples-reference-guide-self-study)
    - [Week 3 Feedback](#week-3-feedback)
  - [Week 4: DevOps and Testing with Copilot](#week-4-devops-and-testing-with-copilot)
    - [1. GitHub Copilot CLI for DevOps Automation](#1-github-copilot-cli-for-devops-automation-45-60-minutes)
    - [2. Testing and Quality Assurance with Copilot CLI](#2-testing-and-quality-assurance-with-copilot-cli-45-60-minutes)
    - [3. Hands-On Lab: Create Applications with the Copilot CLI](#3-hands-on-lab-create-applications-with-the-copilot-cli-60-90-minutes)
    - [4. Week 4 Prompt Examples](#4-week-4-prompt-examples-reference-guide-self-study)
    - [Week 4 Feedback](#week-4-feedback)
  - [Week 5: Refactoring, Optimisation, and Ethical Practices](#week-5-refactoring-optimisation-and-ethical-practices)
    - [1. Refactoring Large Codebases](#1-refactoring-large-codebases-30-45-minutes)
    - [2. Ethical and Security Considerations](#2-ethical-and-security-considerations-30-45-minutes)
    - [3. Hands-On Lab: Modernise Your Legacy Code with GitHub Copilot](#3-hands-on-lab-modernise-your-legacy-code-with-github-copilot-30-minutes)
    - [4. Week 5 Prompt Examples](#4-week-5-prompt-examples-reference-guide-self-study)
    - [Week 5 Feedback](#week-5-feedback)
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

> **Note:** Copilot features (inline suggestions, Ask, inline chat, Plan, Agent, CLI, cloud agent, custom agents, and advanced capabilities) vary by IDE, version, plan, and organisation policy. Use the [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) as the source of truth.

#### 1. Understanding GitHub Copilot (45-60 minutes)

- Overview of its purpose, architecture, and AI-driven capabilities
- Supported languages, frameworks, and environments
- Copilot in real-world developer workflows
- Plan-first and agentic workflows for multi-file tasks
- Value proposition and use cases

**Content:** [1. Understanding GitHub Copilot](Workshops/Week1/1-Understanding-GitHub-Copilot.md)

#### 2. Setup, Configuration, and Interaction Modes (45-60 minutes)

- Installation and setup in multiple IDEs (VS Code - Demo)
- Configuring authentication and preferences
- Basic commands and UI navigation
- Understanding core surfaces: inline suggestions, Ask, inline chat, Plan, Agent, Copilot CLI, and Copilot cloud agent
- When and how to use each surface effectively
- Custom Agents and Extensions overview
- Access, usage limits, model selection, and organisation policy considerations
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
- Inline chat and targeted edits for controlled code modifications
- Agent mode for multi-file changes
- Plan agent for implementation planning
- Context, review, and verification prompts using `#codebase`, `#changes`, `#problems`, `#terminalSelection`, and `#fetch`
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
- Agent skills (`SKILL.md`), MCP tools, approval boundaries, model guidance, and customisation diagnostics
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
- Team customisation packs using instructions, prompt files, custom agents, skills, diagnostics, and plan-first workflows

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
- Context, custom agent, skill, diagnostics, and governance prompts

**Content:** [4. Week 2 Prompt Examples](Workshops/Week2/4-Week2-Prompts.md)

#### Week 2 Feedback

- [Submit Week 2 Lab Reflection](../../issues/new?template=week2-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

### Week 3: MCP Servers and GitHub Copilot

**Duration:** 2.5 to 3.5 hours

**Objective:** Understand the Model Context Protocol, connect MCP servers to GitHub Copilot in VS Code and the CLI, and use MCP tools in Agent Mode to manage GitHub workflows end-to-end.

#### Reflection
Before starting Week 3, please complete your Week 2 reflections if you haven't already: [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

#### 1. MCP Foundations: Connecting GitHub Copilot to the World (45-60 minutes)

- MCP specification fundamentals: JSON-RPC 2.0 data layer, host/client/server roles, and the three server-side primitives (tools, resources, prompts)
- Transport mechanisms: stdio for local servers and Streamable HTTP for remote servers, with HTTP+SSE noted as deprecated
- Configuring MCP servers in VS Code using workspace-scoped `.vscode/mcp.json` and user-profile `mcp.json`, with the `chat.mcp.enabled` setting
- Trust prompts, auto-discovery (`chat.mcp.discovery.enabled`), and using the tool picker in Agent Mode

**Content:** [1. MCP Foundations: Connecting GitHub Copilot to the World](Workshops/Week3/1-MCP-Foundations.md)

#### 2. MCP in Production: GitHub, Copilot CLI, and Governance (45-60 minutes)

- The GitHub MCP server: remote and local deployment, OAuth and PAT authentication, toolsets, read-only mode, and dynamic toolsets
- Configuring MCP for the Copilot coding agent (`mcpServers` JSON, `COPILOT_MCP_` secrets, tools-only constraint) and the Copilot CLI (`~/.copilot/mcp-config.json`, `/mcp` slash commands)
- Security model: trust-on-first-use, prompt injection, tool poisoning, supply chain risks, sandboxing, and audit logging
- Organisation governance: GitHub org policy, VS Code enterprise policies (`ChatMCP`, `McpGalleryServiceUrl`), and private MCP registries

**Content:** [2. MCP in Production: GitHub, Copilot CLI, and Governance](Workshops/Week3/2-MCP-in-Production.md)

#### 3. Hands-On Lab: Integrate MCP with GitHub Copilot (60-90 minutes)

- Set up the GitHub MCP server in a Codespace by creating `.vscode/mcp.json` and authenticating via OAuth
- Use Agent Mode and GitHub MCP tools to search for similar projects, compare features, and create enhancement issues in the repository
- Delegate a complete feature implementation to Copilot (branch, code changes, push, pull request) and review the AI-generated output
- Merge the pull request and use Copilot to post a closing comment on the resolved issue

**Content:** [3. Hands-On Lab: Integrate MCP with GitHub Copilot](Workshops/Week3/3-Week3-Lab.md)

#### 4. Week 3 Prompt Examples (Reference Guide Self Study)

- Server discovery and setup prompts for finding and configuring MCP servers in VS Code and the CLI
- Agent Mode tool use prompts for implicit and explicit tool invocation using `#tool_name` references
- GitHub issue and PR workflow prompts for end-to-end feature delivery via MCP
- Research and code exploration prompts using GitHub MCP search and repository tools

**Content:** [4. Week 3 Prompt Examples](Workshops/Week3/4-Week3-Prompts.md)

#### Week 3 Feedback

- [Submit Week 3 Lab Reflection](../../issues/new?template=week3-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

### Week 4: DevOps and Testing with Copilot

**Duration:** 2 to 2.5 hours (1 session)

**Objective:** Equip participants to use Copilot, in the IDE, the CLI, and GitHub workflows, for CI/CD automation, testing, review, and governed delivery.

#### Reflection
Before starting Week 4, please complete your Week 3 reflections if you haven't already: [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

#### 1. GitHub Copilot CLI for DevOps Automation (45-60 minutes)

- Copilot CLI quick start: installation (WinGet, Homebrew, npm), slash commands, and headless mode
- Interactive vs programmatic modes and session management
- CI/CD pipeline generation from the IDE and the CLI
- Infrastructure as Code (Docker, Kubernetes, Terraform) with CLI generation
- Incident response and log analysis from the terminal
- Built-in agents (Explore, Task, Plan, Code-review) and context management
- Copilot cloud agent, Copilot Code Review, and GitHub Actions governance patterns
- Pre-review validation for deployment readiness (including CLI-powered checks)
- Effective DevOps prompting patterns, security permissions, and `/delegate` workflow

**Content:** [1. GitHub Copilot CLI for DevOps Automation](Workshops/Week4/1-DevOps-Automation.md)

#### 2. Testing and Quality Assurance with Copilot CLI (45-60 minutes)

- Unit test generation from the IDE and the CLI
- Ensuring repeatable test coverage with CLI gap analysis
- Test optimisation and parameterisation
- Framework conversion (with full examples in Week 4 Prompts)
- VS Code test workflows such as `/setupTests`, `/tests`, and `/fixTestFailure` where available
- Quality gates, required checks, rulesets, merge queues, and Copilot Code Review as an assistive review layer
- Quality assurance checklists and testing best practices

**Content:** [2. Testing and Quality Assurance with Copilot CLI](Workshops/Week4/2-Testing-and-Quality-Assurance.md)

#### 3. Hands-On Lab: Create Applications with the Copilot CLI (60-90 minutes)

- Install and configure the standalone GitHub Copilot CLI
- Use Copilot CLI to create GitHub issues from templates
- Build a Node.js calculator application with iterative CLI guidance
- Practice collaborative development with Copilot on the command line
- Explore `/delegate` and `/share` commands

**Content:** [3. Hands-On Lab: Create Applications with the Copilot CLI](Workshops/Week4/3-Week4-Lab.md)

#### 4. Week 4 Prompt Examples (Reference Guide Self Study)

- CI/CD pipeline generation for GitHub Actions and GitLab CI (IDE and CLI)
- Infrastructure as Code (Docker, Kubernetes, Terraform) with CLI generation
- Test generation with coverage requirements and CLI gap analysis
- Validation and security scanning prompts
- Test optimisation and framework conversion with CLI bulk operations
- Cloud agent planning, pull request review, secure workflow review, and quality gate prompts

**Content:** [4. Week 4 Prompt Examples](Workshops/Week4/4-Week4-Prompts.md)

#### Week 4 Feedback

- [Submit Week 4 Lab Reflection](../../issues/new?template=week4-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

### Week 5: Refactoring, Optimisation, and Ethical Practices

**Duration:** 2 to 3 hours (1 session or 2 × 30-45 minutes)

**Objective:** Focus on enhancing code quality through refactoring, fostering ethical AI use, and reinforcing long-term Copilot adoption.

#### Reflection
Before starting Week 5, please complete your Week 4 reflections if you haven't already: [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

#### 1. Refactoring Large Codebases (30-45 minutes)

- Understanding and navigating legacy code
- Using semantic search to map and explore large codebases
- Plan-first agentic refactoring with explicit context, approval boundaries, tests, and checkpoints
- Incremental refactoring strategies (extract, rename, modernise)
- Improving readability, maintainability, and performance
- Prompting patterns for complex refactoring

**Content:** [1. Refactoring Large Codebases](Workshops/Week5/1-Refactoring-Large-Codebases.md)

#### 2. Ethical and Security Considerations (30-45 minutes)

- Intellectual property concerns in AI-generated code
- Security vulnerabilities and prevention strategies
- Responsible AI usage and bias awareness
- Organisational policies and compliance
- Enterprise controls for models, content exclusion, custom instructions, MCP tools, BYOK, and data residency
- Secret scanning, push protection, CodeQL/code scanning, Copilot Autofix, and agent threat modelling

**Content:** [2. Ethical and Security Considerations](Workshops/Week5/2-Ethical-and-Security-Considerations.md)

#### 3. Hands-On Lab: Modernise Your Legacy Code with GitHub Copilot (30 minutes)

- Explain the current state of a legacy COBOL accounting system
- Create a data flow diagram with Copilot assistance
- Identify areas of legacy code that can be improved
- Use GitHub Copilot to generate modern Node.js code snippets
- Replace old code with the new snippets and test the changes

**Content:** [3. Hands-On Lab: Modernise Your Legacy Code with GitHub Copilot](Workshops/Week5/3-Week5-Lab.md)

#### 4. Week 5 Prompt Examples (Reference Guide Self Study)

- Refactoring prompts for legacy code analysis
- Quality standards and compliance checking
- Security audit and vulnerability detection
- Ethical AI and bias detection prompts
- Code review patterns and SOLID principles
- Combination prompts for complete workflows
- Governance, content exclusion, public-code reference, CodeQL, Autofix, and agent security prompts

**Content:** [4. Week 5 Prompt Examples](Workshops/Week5/4-Week5-Prompts.md)

#### Week 5 Feedback

- [Submit Week 5 Lab Reflection](../../issues/new?template=week5-lab.yml)
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

