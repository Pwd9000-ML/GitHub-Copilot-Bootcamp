# GitHub Copilot Interaction Modes

GitHub Copilot offers four distinct interaction modes designed for different stages of the development lifecycle: **Ask**, **Edit**, **Agent**, and **Plan**. Each mode serves a specific purpose and understanding when to use each one will help you get the most out of GitHub Copilot.

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

In addition to the core modes, GitHub Copilot supports **Custom Agents** (also known as Extensions or MCP Servers) that provide specialized capabilities.

### What are Custom Agents?

Custom Agents allow repositories or organizations to define specialized AI assistants. Instead of a generic Copilot, you interact with an agent tailored to specific rules, documentation, or external services.

### How it works

You can switch your chat context to a specific agent using the `@` syntax:
- `@workspace` - Context-aware assistance for your current workspace
- `@github` - GitHub-specific operations
- Custom agents defined for your organization

### Example

| Standard Copilot | Custom Agent |
|------------------|--------------|
| Writes generic Python code | Writes Python code that strictly follows your company's style guide, uses your internal libraries, and ignores deprecated patterns |

Custom agents can be configured via instruction files (like `.github/copilot-instructions.md`) in your repository to provide organization-specific guidance.

---

## Summary

Choose your mode based on your current task:

- **Need answers?** → Use **Ask Mode**
- **Need targeted changes?** → Use **Edit Mode**
- **Need autonomous help?** → Use **Agent Mode**
- **Need a roadmap?** → Use **Plan Mode**