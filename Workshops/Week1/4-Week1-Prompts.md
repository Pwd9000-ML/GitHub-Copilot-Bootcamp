# GitHub Copilot Prompt Examples - Week 1

## Session Overview

**Purpose:** Reference guide for practical prompts  
**Format:** Example prompts with explanations and tips  
**Objective:** Help developers get started with GitHub Copilot's different interaction modes and basic workflows.

---

## Contents

- [1. Inline Code Completions](#1-inline-code-completions)
- [2. Ask Mode - Code Explanations](#2-ask-mode---code-explanations)
- [3. Inline Chat and Targeted Edits](#3-inline-chat-and-targeted-edits)
- [4. Agent Mode - Multi-File Changes](#4-agent-mode---multi-file-changes)
- [5. Plan Agent - Implementation Planning](#5-plan-agent---implementation-planning)
- [6. Debugging Assistance](#6-debugging-assistance)
- [7. Documentation Generation](#7-documentation-generation)
- [8. Review, Context, and Verification](#8-review-context-and-verification)

---

## 1. Inline Code Completions

Inline code completions provide real-time suggestions as you type, helping you write code faster.

- Write descriptive comments or function signatures to guide Copilot
- Let Copilot suggest implementations for common patterns
- Use during active coding for quick boilerplate generation
- Accept suggestions with Tab key or reject with Escape

### Example Prompts

#### Function with Clear Intent

```javascript
// Function to validate email address format using regex
function validateEmail(email) {
```

Expected: Copilot suggests regex validation logic and return statement.

#### Array Operations

```javascript
// Filter students with grades above 80
const topStudents = students.filter(
```

Expected: Copilot completes the filter function with appropriate logic.

#### Error Handling

```javascript
// Try to fetch user data, catch and log errors
try {
```

Expected: Copilot suggests try-catch block with fetch call and error handling.

> **Tip:** The more descriptive your comment, the better Copilot can infer your intent.

---

## 2. Ask Mode - Code Explanations

Ask mode allows you to have conversational interactions with Copilot to understand code and concepts.

- Use Copilot Chat to ask questions about code
- Get explanations of functionality and libraries
- Learn best practices and modern patterns
- Explore unfamiliar codebases with guided assistance

### Example Prompts

#### Understanding Code

```text
What does this function do?
```

```text
Explain this regex pattern step by step
```

```text
How does this event listener work?
```

#### Learning Concepts

```text
What's the difference between `let` and `const` in JavaScript?
```

```text
Explain async/await and how it differs from promises
```

```text
What are the benefits of using TypeScript?
```

#### Best Practices

```text
What's the best way to handle errors in this function?
```

```text
How can I make this code more efficient?
```

```text
Is there a more modern JavaScript syntax for this code?
```

> **Tip:** Ask follow-up questions to dive deeper into topics you don't fully understand.

---

## 3. Inline Chat and Targeted Edits

> **April 2026 note:** Older VS Code material may call this workflow **Edit mode**. VS Code Edit mode is deprecated, so use inline chat for focused local edits and Agent mode for multi-file changes. Check your IDE/version against the [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix).

Inline chat and targeted edits enable controlled modifications to selected code, the current file, or an explicitly provided context set.

- Select the code or file you want to change
- Provide specific instructions and constraints
- Make targeted changes to a defined set of files
- Review and accept or discard individual edits

### Example Prompts

#### Refactoring

```text
Refactor this function to use arrow function syntax
```

```text
Convert this code to use async/await instead of callbacks
```

```text
Extract this validation logic into a separate function
```

#### Adding Features

```text
Add error handling to this function
```

```text
Add JSDoc comments to this function
```

```text
Add input validation for email and password
```

#### Bug Fixes

```text
Fix the off-by-one error in this loop
```

```text
Correct the logic in this conditional statement
```

```text
Fix the memory leak in this event listener
```

> **Tip:** Add relevant files, selections, or symbols before submitting your prompt. Review and accept or discard edits for each file.

---

## 4. Agent Mode - Multi-File Changes

> **Note:** Agent mode availability varies by IDE/version and may depend on policy settings. If you don’t see **Agent** in your Copilot Chat agents dropdown, check the [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix).

Agent mode allows Copilot to autonomously determine and execute multi-step tasks.

- Select Agent from the agents dropdown in Copilot Chat
- Describe your task and let Copilot determine the steps
- Copilot autonomously identifies files to change
- Suggests terminal commands and iterates to complete tasks
- Confirm or reject suggested actions as Copilot works

### Example Prompts

#### Feature Implementation

```text
Create a new user profile component with:
- ProfileCard component in components folder
- User interface in types folder
- Styling in styles folder
- Export from index.ts
```

```text
Add form validation across the login form:
- Client-side validation in the component
- Validation utilities in utils folder
- Error message constants in constants file
```

#### Code Organisation

```text
Reorganise the authentication code:
- Move auth functions to auth/index.ts
- Create types in auth/types.ts
- Update all imports across the project
```

#### Context-Rich Agent Prompt

```text
#codebase Add server-side validation for the checkout flow.
First identify the files that handle cart totals, payment submission, and order creation.
Then make the smallest set of changes, add tests, run the relevant test command, and summarise what changed.
Ask before running commands that modify dependencies or external services.
```

> **Tip:** In Agent mode, Copilot autonomously determines which files need changes. Confirm or reject suggested terminal commands as Copilot iterates to complete your task.

---

## 5. Plan Agent - Implementation Planning

> **Note:** The Plan agent is intended for review-before-implementation workflows. Availability and behaviour vary by IDE and policy, so confirm in the [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix).

The Plan agent helps you think through tasks before executing by creating detailed implementation plans.

- Select Plan from the agents dropdown in Copilot Chat, or use `/plan` where available
- Copilot researches your codebase to understand context
- Creates a detailed implementation plan for review
- Waits for your approval before making any changes
- Useful for team review and ensuring all requirements are considered

### Example Prompts

#### New Feature Planning

```text
Create a simple to-do web app with HTML, CSS, and JS files
```

```text
Plan adding user authentication to this Express application
```

#### Refactoring Planning

```text
Plan how to migrate this codebase from JavaScript to TypeScript
```

```text
Outline the steps to refactor this monolithic function into smaller modules
```

#### Verification Planning

```text
Create an implementation plan for this change.
Include acceptance criteria, files likely to change, tests to add or run, security risks, and manual verification steps.
Do not edit files yet.
```

> **Tip:** After reviewing the plan, click "Start Implementation" to hand off to Agent mode, or "Open in Editor" to save the plan as Markdown for later.

---

## 6. Debugging Assistance

Debugging assistance helps you identify, understand, and fix issues in your code.

- Ask Copilot to help identify bugs and errors
- Get explanations for unexpected behaviour
- Trace through logic to find issues
- Add debugging statements and test cases
- Include error messages for better diagnostics

### Example Prompts

#### Error Diagnosis

```text
Why am I getting "Cannot read property 'map' of undefined"?
```

```text
This function returns NaN, help me find the issue
```

```text
Why isn't this event listener triggering?
```

#### Logic Issues

```text
This loop doesn't produce the expected output, what's wrong?
```

```text
Help me understand why this condition is always false
```

```text
Why does this function return undefined?
```

#### Testing/Debugging

```text
Add console.log statements to help debug this function
```

```text
How can I test this function to identify the bug?
```

```text
What edge cases should I test for this validation function?
```

> **Tip:** Include the error message and relevant code context when asking for debugging help.

---

## 7. Documentation Generation

Documentation generation helps you create clear, professional documentation for your code.

- Generate JSDoc comments for functions
- Create API documentation for endpoints
- Write README content for projects
- Add inline comments explaining complex logic
- Produce usage examples for utilities

### Example Prompts

#### Function Documentation

```text
Add JSDoc comments to this function
```

```text
Generate documentation for this API endpoint
```

```text
Create inline comments explaining this complex algorithm
```

#### Project Documentation

```text
Generate a README.md for this project
```

```text
Create API documentation for these endpoints
```

```text
Write usage examples for this utility function
```

#### Code Comments

```text
Add comments explaining this regex pattern
```

```text
Document the purpose of each parameter in this function
```

```text
Explain what this code block does for future maintainers
```

> **Tip:** Good documentation makes your code more maintainable. Use Copilot to quickly add professional documentation.

---

## 8. Review, Context, and Verification

Modern Copilot workflows work best when you provide explicit context and ask for verification steps.

- Use `#codebase` to search the workspace semantically
- Use `#file` or attached files for exact context
- Use `#changes` to review current Git changes
- Use `#problems` to analyse editor diagnostics
- Use `#terminalSelection` or pasted terminal output for failing commands
- Use `#fetch` only for trusted external documentation and ask Copilot to cite the source URL in its answer

### Example Prompts

#### Codebase Context

```text
#codebase Explain how authentication works in this project.
List the key files, data flow, and any obvious risks or missing tests.
```

#### Change Review

```text
#changes Review these edits for bugs, security issues, missing tests, and unclear documentation.
Give findings first, ordered by severity, then provide a short summary.
```

#### Problems and Terminal Output

```text
#problems Explain these diagnostics and propose the smallest safe fix.
Do not change files until you have described the root cause.
```

```text
#terminalSelection Explain this failing test output.
Identify whether the failure is in the test, implementation, or setup, and recommend the next command to run.
```

#### Source Validation

```text
#fetch https://code.visualstudio.com/docs/copilot/overview
Summarise the current Copilot surfaces relevant to a beginner developer.
Only use information from the fetched source and include the URL in the answer.
```

> **Tip:** Ask Copilot to summarise changes, tests, and residual risks before you keep or commit generated work.

---

## Week 1 Feedback

Please complete the following reflections after completing Week 1 activities:

- [Submit Week 1 Lab Reflection](../../issues/new?template=week1-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

## Next Steps

After mastering these basic prompting techniques and workflows in Week 1, we will explore more advanced strategies in Week 2 to further enhance your productivity with GitHub Copilot.
**[← Back to Main README](../../README.md)** | **[Continue to Week 2 →](../Week2/1-Prompt-Engineering-and-Customisation.md)**

