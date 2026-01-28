# GitHub Copilot Prompt Examples - Week 1

A collection of practical prompts to help you get started with GitHub Copilot's different interaction modes and basic workflows.

---

## Table of Contents

1. [Inline Code Completions](#1-inline-code-completions)
2. [Ask Mode - Code Explanations](#2-ask-mode---code-explanations)
3. [Edit Mode - Code Modifications](#3-edit-mode---code-modifications)
4. [Agent Mode - Multi-File Changes](#4-agent-mode---multi-file-changes)
5. [Plan Mode - Implementation Planning](#5-plan-mode---implementation-planning)
6. [Debugging Assistance](#6-debugging-assistance)
7. [Documentation Generation](#7-documentation-generation)

---

## 1. Inline Code Completions

**Technique:** Write descriptive comments or function signatures, then let Copilot suggest the implementation as you type.

**When to use:** During active coding when you need quick suggestions for common patterns or boilerplate code.

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

**Technique:** Use Copilot Chat to ask questions about code, understand functionality, or learn new concepts.

**When to use:** When you need to understand existing code, learn about libraries, or explore best practices.

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

## 3. Edit Mode - Code Modifications

**Technique:** Select Edit from the agents dropdown in Copilot Chat, add files to your working set, and prompt Copilot to make controlled edits.

**When to use:** When you want granular control over which files Copilot can edit, making quick specific updates to a defined set of files.

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

> **Tip:** Add relevant files to your working set before submitting your prompt. Review and Accept or Discard edits for each file.

---

## 4. Agent Mode - Multi-File Changes

**Technique:** Select Agent from the agents dropdown in Copilot Chat and describe your task. Copilot autonomously determines which files to change, suggests terminal commands, and iterates to complete the task.

**When to use:** When you have a complex task involving multiple steps, iterations, and error handling, and want Copilot to determine the necessary steps autonomously.

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

#### Code Organization

```text
Reorganize the authentication code:
- Move auth functions to auth/index.ts
- Create types in auth/types.ts
- Update all imports across the project
```

> **Tip:** In Agent mode, Copilot autonomously determines which files need changes. Confirm or reject suggested terminal commands as Copilot iterates to complete your task.

---

## 5. Plan Mode - Implementation Planning

**Technique:** Select Plan from the agents dropdown in Copilot Chat and describe a task. Copilot researches your codebase, creates a detailed implementation plan, and waits for your approval before making changes.

**When to use:** When you want to think through a task before executing, ensure all requirements are considered, or need a plan for team review.

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

> **Tip:** After reviewing the plan, click "Start Implementation" to hand off to Agent mode, or "Open in Editor" to save the plan as Markdown for later.

---

## 6. Debugging Assistance

**Technique:** Ask Copilot to help identify and fix bugs in your code.

**When to use:** When you encounter errors, unexpected behavior, or need to trace through logic.

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

**Technique:** Ask Copilot to generate documentation for your code.

**When to use:** When you need to document functions, APIs, or add README content.

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

## Best Practices for Week 1

1. **Start Simple:** Begin with inline suggestions before moving to more complex interactions
2. **Iterate:** If a suggestion isn't quite right, refine your prompt and try again
3. **Learn Patterns:** Pay attention to how Copilot interprets different prompt styles
4. **Verify Output:** Always review and test Copilot's suggestions before accepting them
5. **Combine Modes:** Use Ask to understand, Plan to strategize, Edit for controlled changes, and Agent for autonomous tasks
6. **Be Specific:** The more context you provide, the better the suggestions

---

## Next Steps

After mastering these basic prompting techniques:
- Move on to Week 2 for advanced prompt engineering with the CRAFT framework
- Learn how to create custom instructions for project specific patterns
- Explore how to refine and iterate on Copilot's suggestions systematically
