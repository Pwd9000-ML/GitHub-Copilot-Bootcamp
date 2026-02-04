# GitHub Copilot Interaction Modes

GitHub Copilot offers four distinct interaction modes designed for different stages of the development lifecycle: **Ask**, **Edit**, **Agent**, and **Plan**. Each mode serves a specific purpose and understanding when to use each one will help you get the most out of GitHub Copilot.

> **Note:** Feature availability varies by IDE and version. For example, GitHub's feature overview notes that **Edit mode is only available in Visual Studio Code and JetBrains IDEs**, but you should use the [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) as the source of truth for your specific IDE/version.

---

## Contents

- [Quick Comparison](#quick-comparison)
- [Detailed Breakdown](#detailed-breakdown)
  - [1. Ask Mode (Chat)](#1-ask-mode-chat)
  - [2. Edit Mode (Inline)](#2-edit-mode-inline)
  - [3. Agent Mode (Autonomous Developer)](#3-agent-mode-autonomous-developer)
  - [4. Plan Mode (Architect)](#4-plan-mode-architect)
- [Custom Agents (Extensions)](#custom-agents-extensions)
- [Summary](#summary)
- [Next Steps](#next-steps)

---

## Quick Comparison

| Mode | Best For | Key Capability | Example Use Case |
|------|----------|----------------|------------------|
| **Ask** | Learning & Debugging | Conversational Q&A without modifying code | *"What does this function do?"* or *"Explain this error."* |
| **Edit** | Refactoring & Fixes | Precise, user-controlled changes to specific files | *"Rename this variable to `isUserLoggedIn`"* or *"Refactor this into a new method."* |
| **Agent** | Autonomous Building | Iterative coding, running terminal commands, and multi-file changes | *"Create a new React component with tests and add it to the router."* |
| **Plan** | Architecture & Strategy | Generates a step-by-step blueprint before coding | *"How should we structure a new user authentication module?"* |

---

## Detailed Breakdown

### 1. Ask Mode (Chat)

> **Function:** Acts as a knowledgeable pair programmer who can see your code but touches nothing. It answers questions, explains concepts, and generates code snippets you must manually copy/insert.

**When to use:**
- Exploring a new codebase
- Understanding how existing code works
- Getting explanations without risking accidental changes

**Example:**
> *"You are exploring a new codebase and want to understand how the `AuthService` works without risking accidental deletions."*

---

### 2. Edit Mode (Inline)

> **Function:** A "do what I say" mode for targeted execution. You highlight code (or select files) and give a specific instruction. Copilot applies the changes directly to the editor for your review in a Diff View.

**When to use:**
- Making precise, controlled changes
- Refactoring specific sections of code
- Adding documentation or comments

**Example:**
> *"You have a 50-line function and want to refactor it to use `async/await` instead of callbacks, or add comments to a class."*

---

### 3. Agent Mode (Autonomous Developer)

> **Function:** The most powerful mode. It functions autonomously to complete a task. It can edit multiple files, run terminal commands (like `npm install` or running tests), and self-correct if it encounters errors.

**When to use:**
- Scaffolding new projects or features
- Tasks requiring changes across multiple files
- Operations that need terminal commands

**Example:**
> *"Scaffold a new Next.js project with Tailwind CSS." The Agent will create folders, install dependencies, and write the initial pages while you watch.*

---

### 4. Plan Mode (Architect)

> **Function:** The "think before you act" mode. Instead of writing code immediately, it analyses your request and codebase to generate a structured implementation plan (often in Markdown). You review and refine this plan before handing it off to Agent Mode to execute.

**When to use:**
- Planning complex features
- Understanding the scope of changes needed
- Ensuring nothing is missed in a large implementation

**Example:**
> *"You need to implement a complex feature like adding Dark Mode support. Plan Mode lists every file that needs changing (CSS, components, user settings) so you don't miss anything."*

---

## Custom Agents (Extensions)

In addition to the core modes, GitHub Copilot supports **custom agents** that provide specialised capabilities for Copilot coding agent.

### What are Custom Agents?

Custom Agents allow repositories or organisations to define specialised AI assistants. Instead of a generic Copilot, you interact with an agent tailored to specific rules, documentation, or external services.
GitHub describes custom agents as specialised versions of Copilot coding agent. You define them using Markdown files called **agent profiles**, which can specify prompts, tools, and MCP servers.

### How it works

Depending on your IDE and configuration, you can scope your prompt using chat participants (type `@` in the prompt box to see what’s available). For example:
- `@github` - GitHub-specific skills (available in Copilot Chat)
- `@workspace` - Workspace-aware assistance (availability varies by IDE/version)
- Organisation-specific custom agents (availability varies by IDE/version)

### Example

| Standard Copilot | Custom Agent |
|------------------|--------------|
| Writes generic Python code | Writes Python code that strictly follows your company's style guide, uses your internal libraries, and ignores deprecated patterns |

> **Tip:** Don't conflate these configuration mechanisms:
> - **Repository custom instructions** (for example `.github/copilot-instructions.md` and `.github/instructions/*.instructions.md`) provide repository and path-specific guidance.
> - **Custom agents** are defined via agent profile files (for example `.github/agents/AGENT-NAME.md`).
> - **MCP servers/tools** are integrations that an agent (or chat experience) can use, depending on environment support.
>
> References: [About custom agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents) and [Adding repository custom instructions](https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot).

---

## Summary

Choose your mode based on your current task:

- **Need answers?** → Use **Ask Mode**
- **Need targeted changes?** → Use **Edit Mode**
- **Need autonomous help?** → Use **Agent Mode**
- **Need a roadmap?** → Use **Plan Mode**

## Next Steps

- **Week 1 Session 4:** In the next session, we'll complete an interactive [hands-on lab](4-week1-lab.md) to apply GitHub Copilot in real-world scenarios

