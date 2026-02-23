# Prompt Engineering and Customisation

**Duration:** 45-60 minutes  
**Format:** Presentation with interactive examples  
**Objective:** Master the art of crafting effective prompts and learn the three pillars of Copilot customisation (instruction files, prompt files, and custom agents) for consistent, high-quality code generation.

---

## What is Prompt Engineering?

Prompt engineering is the practice of crafting clear, specific instructions that guide AI tools like GitHub Copilot to produce the desired output. Think of it as learning to communicate effectively with your AI pair programmer.

**Why it matters:**
- Better prompts = better code suggestions
- Reduces iteration time and rework
- Ensures consistency with team standards
- Improves accuracy for complex tasks

---

## The CRAFT Framework for Effective Prompts

Use this mnemonic to structure your prompts for optimal results:

| Element | Description | Example |
|---------|-------------|---------|
| **C**ontext | Background information about your project or task | *"In a Node.js Express application..."* |
| **R**ole | What perspective should Copilot take? | *"As a senior developer..."* |
| **A**ction | What specific task should be performed? | *"...create a function that..."* |
| **F**ormat | How should the output be structured? | *"...with JSDoc comments and error handling"* |
| **T**one | Any style or standards to follow | *"...following our team's naming conventions"* |

> **Note:** CRAFT is a helpful mnemonic for remembering key prompt elements, not an official GitHub term.

---

## Prompt Types and When to Use Them

### 1. Comment-Driven Prompts (Inline)

Write descriptive comments above where you want code generated.

**Basic Example:**
```javascript
// Function to validate email addresses
function validateEmail(email) {
  // Copilot generates the implementation
}
```

**Enhanced Example (with CRAFT):**
```javascript
/**
 * Performs basic validation of an email address format using common rules,
 * without claiming full RFC 5322 or RFC 5321 compliance.
 * Returns true if valid, false otherwise.
 * Should handle edge cases like empty strings and null values.
 * @param {string} email - The email address to validate
 * @returns {boolean} - Whether the email is valid
 */
function validateEmail(email) {
  // Copilot generates a more robust implementation
}
```

---

### 2. Chat-Based Prompts (Ask Mode)

Use conversational prompts in Copilot Chat for exploration, explanation, and generation.

**Weak Prompt:**
> "Write a function"

**Strong Prompt:**
> "Write a JavaScript function to add a new book to an inventory array. The book should have properties for title, author, genre, and publication year. Prevent duplicate entries based on the title. Include input validation and return appropriate error messages."

---

### 3. Template Generation Prompts

Use when you need reusable code structures.

#### Exercise: Book Inventory System

**Prompt 1 - Basic Function:**
> "Generate a JavaScript function template to add a new book with fields like title, author, and genre."

**Prompt 2 - Enhanced Function:**
> "Can you create a reusable function to add books with properties such as title, author, genre, and publication year? Include validation to prevent duplicates."

**Prompt 3 - Search Functionality:**
> "Write a function template to search for books in an inventory by title or genre. Make it case-insensitive and support partial matches."

**Sample Output:**
```javascript
/**
 * Adds a new book to the inventory
 * @param {Array} inventory - The current book inventory
 * @param {Object} book - The book to add
 * @param {string} book.title - Book title
 * @param {string} book.author - Book author
 * @param {string} book.genre - Book genre
 * @param {number} [book.publicationYear] - Optional publication year
 * @returns {Object} Result object with success status and message
 */
function addBook(inventory, book) {
  // Validate required fields
  if (!book.title || !book.author || !book.genre) {
    return { success: false, message: 'Missing required fields' };
  }
  
  // Check for duplicates
  const exists = inventory.some(
    b => b.title.toLowerCase() === book.title.toLowerCase()
  );
  
  if (exists) {
    return { success: false, message: 'Book already exists' };
  }
  
  inventory.push(book);
  return { success: true, message: 'Book added successfully' };
}
```

---

## Writing Effective Prompts: Best Practices

### 1. Be Specific and Detailed

| Weak | Strong |
|------|--------|
| "Create a search function" | "Create a function to search for books by title or genre, returning all matches as an array" |
| "Handle errors" | "Add try-catch blocks with specific error messages for network failures and validation errors" |
| "Make it faster" | "Optimise this function for arrays larger than 10,000 items using indexing or memoization" |

### 2. Provide Context

**Without Context:**
> "Write a login function"

**With Context:**
> "Write a login function for a React application using Firebase Authentication. It should handle email/password login, show loading states, and redirect to the dashboard on success."

### 3. Specify Output Format

```
Generate a function with:
- JSDoc comments describing parameters and return values
- Input validation for all parameters
- Error handling with descriptive messages
- Unit test examples in comments
```

### 4. Use Examples (Few-Shot Prompting)

Give Copilot examples of what you want:

```javascript
// Example of the pattern I want to follow:
// Input: { name: "John", age: 30 }
// Output: "John is 30 years old"

// Now create a similar function for:
// Input: { title: "The Great Gatsby", author: "F. Scott Fitzgerald" }
// Output: Should format book information in a similar readable way
```

### 5. Iterate and Refine

Start broad, then narrow down:

1. **First prompt:** "Create a user authentication system"
2. **Refinement:** "Add password strength validation requiring 8+ characters, uppercase, lowercase, and numbers"
3. **Further refinement:** "Also add rate limiting to prevent brute force attacks"

---

## Organisational Standards with Instruction Files

### What are Copilot Instructions?

Instruction files tell Copilot about your project's conventions, standards, and preferences. They ensure consistent code generation across your team.

### Setting Up Repository Instructions

Create a file at `.github/copilot-instructions.md`:

```markdown
# Copilot Instructions for This Repository

## Code Style
- Use TypeScript for all new files
- Follow ESLint rules defined in .eslintrc
- Use functional components for React
- Prefer async/await over .then() chains

## Naming Conventions
- Use camelCase for variables and functions
- Use PascalCase for classes and React components
- Use SCREAMING_SNAKE_CASE for constants
- Prefix private methods with underscore

## Documentation
- All public functions must have JSDoc comments
- Include @param, @returns, and @throws tags
- Add usage examples for complex functions

## Error Handling
- Always use try-catch for async operations
- Log errors with context using our logger utility
- Return standardised error objects: { success: false, error: string, code: number }

## Security
- Never hardcode credentials or API keys
- Sanitise all user inputs
- Use parameterised queries for database operations
```

### File-Specific Instructions

Create instructions for specific file types or directories:

> **VS Code reference:** Instructions files support YAML frontmatter like `applyTo`, `name`, and `description`. See https://code.visualstudio.com/docs/copilot/customization/custom-instructions

**For test files (`.github/instructions/tests.instructions.md`):**

> **Note:** `applyTo` is a single glob pattern. If you need multiple patterns with different scopes, create multiple `.instructions.md` files.
```markdown

---
applyTo: "**/*.test.js,**/*.spec.ts"
description: "Guidelines for writing unit tests"
---

# Test File Instructions

- Use Jest as the testing framework
- Follow AAA pattern: Arrange, Act, Assert
- Use descriptive test names: "should [expected behavior] when [condition]"
- Mock external dependencies
- Aim for 80% code coverage minimum
```

### Prompt Files (Reusable Prompts)

Create reusable prompt templates for common tasks in `.github/prompts/`. Prompt files support frontmatter with the following properties:

> **VS Code reference:** Prompt file frontmatter uses `agent` and supports `tools`. See https://code.visualstudio.com/docs/copilot/customization/prompt-files

| Property | Description | Values |
|----------|-------------|--------|
| `description` | A short description of the prompt | Free text |
| `name` | The name of the prompt, used after typing `/` in chat (defaults to the file name) | Free text |
| `argument-hint` | Optional hint text shown in the chat input field to guide users | Free text |
| `agent` | The agent used for running the prompt: `ask`, `edit`, `agent`, or the name of a custom agent (defaults to the current agent) | `ask`, `edit`, `agent`, or custom agent name |
| `model` | The language model used when running the prompt (defaults to the currently selected model in the model picker) | Model identifier (string) |
| `tools` | A list of tool or tool set names available for this prompt. Can include built-in tools, tool sets, MCP tools, or extension-contributed tools. To include all tools from an MCP server, use `<server name>/*`. | Array of tool or tool-set names |

> Learn more about tools in chat: https://code.visualstudio.com/docs/copilot/chat/chat-tools

> **Tip:** If you specify tools in a prompt file, VS Code uses the priority order: prompt file tools → referenced custom agent tools → default tools for the selected agent.

#### Example 1: Code Review (`.github/prompts/code-review.prompt.md`)

Uses `agent` mode with tools for active repository analysis:

```markdown
---
agent: 'agent'
name: 'code-review'
description: 'Language-agnostic code review with repository analysis and fix-oriented feedback'
argument-hint: 'focus=<security|performance|readability>'
model: '<model-id>'
tools: ['codebase', 'githubRepo', 'search', 'usages', 'myMcpServer/*']
---

# Code Review

Perform a comprehensive code review of the selected code:

## Review Checklist
- [ ] Logic correctness and edge case handling
- [ ] Error handling and defensive programming
- [ ] Code readability and naming conventions
- [ ] Performance considerations
- [ ] Adherence to SOLID principles

## Output Format
Provide feedback as:
1. **Critical issues** - Must fix before merge
2. **Suggestions** - Recommended improvements
3. **Positive observations** - Good practices to maintain

Include specific line references and concrete fix suggestions.
```

> **Note:** Replace `<model-id>` with a model available in your environment, and replace `myMcpServer` with the name of an installed MCP server (or remove that entry if you are not using MCP).

#### Example 2: Security Review (`.github/prompts/security-review.prompt.md`)

Uses `ask` mode for security-focused analysis and discussion:

```markdown
---
agent: 'ask'
name: 'security-review'
description: 'OWASP-aligned security review identifying vulnerabilities and remediation steps'
argument-hint: 'target=<auth|api|data|ui>'
---

# Security Review

Analyse the selected code for security vulnerabilities following OWASP guidelines.

## Check for:
- **Injection flaws**: SQL, NoSQL, OS command, LDAP injection
- **Broken authentication**: Weak credentials, session management issues
- **Sensitive data exposure**: Hardcoded secrets, improper encryption
- **XSS vulnerabilities**: Reflected, stored, and DOM-based XSS
- **Insecure deserialisation**: Untrusted data deserialisation
- **Components with known vulnerabilities**: Outdated dependencies

## For each issue found:
1. Describe the vulnerability and its severity (Critical/High/Medium/Low)
2. Explain the potential impact
3. Provide a secure code example as remediation

Reference OWASP Top 10 categories where applicable.
```

#### Example 3: README Update (`.github/prompts/readme-update.prompt.md`)

Uses `edit` mode for direct file modifications:

```markdown
---
agent: 'edit'
name: 'readme-update'
description: 'Update README with current project structure and usage instructions'
argument-hint: 'audience=<devs|ops|users>'
---

# README Update

Update the README.md file to reflect the current state of the project.

## Sections to include or update:
1. **Project title and description** - Clear, concise overview
2. **Installation** - Step-by-step setup instructions
3. **Usage** - Code examples showing common use cases
4. **API reference** - Document public functions/endpoints
5. **Contributing** - Guidelines for contributors
6. **License** - Current license information

## Guidelines:
- Keep language clear and beginner-friendly
- Include working code examples
- Update version numbers if applicable
- Ensure all links are valid
```

Use prompt files for tasks your team performs frequently, such as code reviews, documentation generation, test creation, and refactoring patterns.

---

## Custom Agent Files (Specialised Personas)

### What are Custom Agents?

Custom agents let you configure Copilot to adopt different personas tailored to specific development roles and tasks. Each agent bundles its own **instructions**, **tools**, and optional **model** selection into a single reusable definition. Think of them as pre-configured specialists you can switch to with one click.

> **VS Code reference:** Custom agents are available as of VS Code release 1.106 (previously known as custom chat modes). See https://code.visualstudio.com/docs/copilot/customization/custom-agents

**Why use custom agents?**

| Benefit | Example |
|---------|---------|
| **Role isolation** | A planning agent uses only read-only tools so it cannot accidentally edit code |
| **Consistent behaviour** | A code-review agent always follows the same checklist |
| **Tool scoping** | A security agent only has access to analysis tools, not deployment tools |
| **Guided workflows** | Chain agents together with handoffs: Plan → Implement → Review |

### Creating a Custom Agent

Custom agent files use the `.agent.md` extension and are stored in:

| Location | Scope |
|----------|-------|
| `.github/agents/` | Available to everyone working in the repository |
| User profile folder | Available across all your workspaces (personal) |
| `.github-private` repository | Organisation/enterprise-wide (all repos) |
| `.claude/agents/` | Claude Code compatibility format |

> **Tip:** Type `/agents` in the chat input to quickly open the **Configure Custom Agents** menu, or run `Chat: New Custom Agent` from the Command Palette (<kbd>Ctrl+Shift+P</kbd>).

### Custom Agent File Structure

Agent files are Markdown with optional YAML frontmatter:

| Property | Description | Values |
|----------|-------------|--------|
| `name` | Agent name (defaults to filename if omitted) | Free text |
| `description` | Brief description shown as placeholder text in chat | Free text (required on GitHub) |
| `argument-hint` | Hint text shown in the chat input field | Free text |
| `tools` | List of available tools (built-in, MCP, extension-contributed). Omit to allow all tools. | Array of tool/tool-set names |
| `agents` | List of agents available as subagents. Use `*` for all, `[]` for none. | Array of agent names |
| `model` | AI model to use. Can be a single string or prioritised array (first available is used). | Model identifier or array |
| `target` | Restrict to a specific environment | `vscode` or `github-copilot` |
| `user-invokable` | Show in agents dropdown (default: `true`). Set `false` for subagent-only agents. | Boolean |
| `disable-model-invocation` | Prevent other agents from invoking this agent as a subagent (default: `false`) | Boolean |
| `mcp-servers` | MCP server configurations (for org/enterprise agents on GitHub) | JSON |
| `handoffs` | Suggested next actions to transition between agents | Array (see below) |

> **VS Code reference:** See https://code.visualstudio.com/docs/copilot/customization/custom-agents for the full property reference.

#### Handoff Properties

| Property | Description |
|----------|-------------|
| `handoffs.label` | Display text on the handoff button |
| `handoffs.agent` | Target agent to switch to |
| `handoffs.prompt` | Prompt text to send to the target agent |
| `handoffs.send` | Auto-submit the prompt (default: `false`) |
| `handoffs.model` | Optional model override for the handoff, e.g. `GPT-5.2 (copilot)` |

### Example 1: Code Review Agent (`.github/agents/code-reviewer.agent.md`)

A review-only agent that cannot modify production code:

```markdown
---
name: code-reviewer
description: Reviews code for quality, security, and adherence to team standards
tools: ['codebase', 'search', 'usages', 'githubRepo', 'fetch']
---

You are an expert code reviewer. Follow these guidelines:

## Review Checklist
- [ ] Logic correctness and edge case handling
- [ ] Error handling and defensive programming
- [ ] Code readability and naming conventions
- [ ] Performance considerations
- [ ] SOLID principles adherence
- [ ] Security vulnerabilities (OWASP Top 10)

## Output Format
For each issue found, provide:
1. **Severity**: Critical / High / Medium / Low
2. **Location**: File and line reference
3. **Issue**: Clear description of the problem
4. **Fix**: Concrete code example showing the remediation

Never modify production code directly — only suggest changes.
```

### Example 2: Test Specialist Agent (`.github/agents/test-specialist.agent.md`)

Focuses on testing without touching production code. Omitting `tools` grants access to all available tools:

```markdown
---
name: test-specialist
description: Focuses on test coverage, quality, and testing best practices without modifying production code
---

You are a testing specialist focused on improving code quality through comprehensive testing. Your responsibilities:

- Analyse existing tests and identify coverage gaps
- Write unit tests, integration tests, and end-to-end tests following best practices
- Review test quality and suggest improvements for maintainability
- Ensure tests are isolated, deterministic, and well-documented
- Focus only on test files and avoid modifying production code unless specifically requested

Always include clear test descriptions and use appropriate testing patterns for the language and framework.
```

### Example 3: Planning Agent with Handoffs (`.github/agents/planner.agent.md`)

A read-only agent that creates implementation plans and hands off to an implementation agent:

```markdown
---
name: planner
description: Creates detailed implementation plans and technical specifications
tools: ['search', 'codebase', 'fetch', 'githubRepo']
handoffs:
  - label: Start Implementation
    agent: implementation
    prompt: Now implement the plan outlined above.
    send: false
---

You are a technical planning specialist. Your responsibilities:

- Analyse requirements and break them into actionable tasks
- Create detailed technical specifications with architecture decisions
- Generate implementation plans with clear steps, dependencies, and risks
- Document API designs, data models, and system interactions

Structure plans with clear headings, task breakdowns, acceptance criteria, and testing considerations.
Do NOT modify any files — only produce documentation and plans.
```

> **Tip:** When the planner finishes, the **Start Implementation** handoff button appears. Clicking it switches to the `implementation` agent with the plan context carried forward.

### Sharing Custom Agents Across Teams

- **Workspace level:** Store `.agent.md` files in `.github/agents/` and commit them to the repository
- **Organisation level:** Place agent files in the `agents/` directory of a `.github-private` repository. Enable discovery in VS Code with `github.copilot.chat.organizationCustomAgents.enabled: true`
- **User level:** Create agents in your user profile for personal use across all workspaces

> **GitHub reference:** See https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents for creating and managing custom agents.

### The Three Pillars of Copilot Customisation

Together, instruction files, prompt files, and custom agents form a complete customisation layer:

| Layer | File Type | Location | Purpose |
|-------|-----------|----------|---------|
| **Instructions** | `.instructions.md` | `.github/instructions/` | Define project-wide conventions and standards |
| **Prompts** | `.prompt.md` | `.github/prompts/` | Create reusable task templates |
| **Custom Agents** | `.agent.md` | `.github/agents/` | Bundle instructions + tools into switchable personas |

> **Note:** Instructions are always-on context, prompts are on-demand tasks you invoke with `/`, and agents are full persona switches with their own tool sets and behaviours.

---

## Incorporating Security Recommendations

### Prompting for Secure Code

Always include security considerations in your prompts:

**Basic Prompt:**
> "Write a function to query the database for users"

**Security-Aware Prompt:**
> "Write a function to query the database for users using parameterised queries to prevent SQL injection. Include input validation and sanitisation. Log failed attempts for security monitoring."

### Security Prompt Patterns

#### SQL Operations
```
When generating SQL queries:
- Always use parameterised queries or prepared statements
- Validate and sanitise all input before use
- Limit result sets with pagination
- Use principle of least privilege for database connections
```

#### User Input Handling
```
For any function handling user input:
- Validate input type and format
- Sanitise strings to prevent XSS
- Check for maximum length limits
- Reject unexpected characters for sensitive fields
```

#### Authentication
```
For authentication-related code:
- Never store passwords in plain text
- Use Argon2id for password hashing (recommended by OWASP)
  - Alternatives: scrypt, or bcrypt with a high work factor for compatibility requirements
- Implement rate limiting
- Use secure session management
```

---

## Practical Exercises

### Exercise 1: Template Generation

Using Copilot Chat, generate the following with well-crafted prompts:

1. **Add Book Function:**
   > "Generate a JavaScript function template to add a new book with fields like title, author, and genre. Include validation and duplicate checking."

2. **Search Function:**
   > "Write a function template to search for books in an inventory by title or genre. Make it case-insensitive."

3. **Customisation:**
   > "Refactor the addBook function to include an optional field for publication year with validation that it's a valid year."

### Exercise 2: Scaffolding a Project

Use these prompts to scaffold a complete project structure:

1. **Project Structure:**
   > "Create a project structure with folders for src, tests, and public directories."

2. **Initial Files:**
   > "Generate a package.json file with a basic project configuration for a Node.js application."

3. **Modular Structure:**
   > "Add subfolders models, controllers, and views inside the src folder for better modularity."

### Exercise 3: Security-Focused Code

Practice writing security-aware prompts:

1. **Input Validation:**
   > "Write a function to validate and sanitise user registration data (email, password, username) following OWASP guidelines."

2. **Secure Database Query:**
   > "Generate a function to fetch user data by ID using parameterised queries with proper error handling."

### Exercise 4: SQL Query Generation

Practice SQL prompts with Copilot:

| Task | Prompt |
|------|--------|
| Basic SELECT | "Write a SQL query to select all columns from the 'employees' table where the department is 'Sales'." |
| JOIN | "Write a SQL query to join the 'orders' and 'customers' tables on 'customer_id', selecting order ID, customer name, and order total." |
| Aggregation | "Write a SQL query to calculate the average salary of employees in each department." |
| Subquery | "Write a SQL query to find employees who earn more than the average salary in the company." |

### Exercise 5: Custom Agent Creation

Practice creating custom agents for your team:

1. **Planning Agent:**
   Create a `.github/agents/planner.agent.md` that only has read-only tools (`search`, `codebase`, `fetch`) and instructions to produce implementation plans without modifying code.

2. **Test Writer Agent:**
   Create a `.github/agents/test-writer.agent.md` with instructions to focus exclusively on writing tests, never modifying production code. Omit the `tools` property to grant access to all tools.

3. **Agent with Handoffs:**
   Extend your planning agent to include a handoff to an implementation agent. Test the workflow by starting in the planner, generating a plan, then clicking the handoff button.

4. **Organisation Sharing:**
   Discuss with your team which agents would benefit from being shared at the organisation level via a `.github-private` repository.

---

## Common Pitfalls to Avoid

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Vague prompts** | Generic, unhelpful suggestions | Be specific about inputs, outputs, and constraints |
| **No context** | Code that doesn't fit your project | Include language, framework, and project context |
| **Ignoring output** | Accepting code without review | Always review and test generated code |
| **Single attempt** | Settling for suboptimal results | Iterate and refine your prompts |
| **No security mention** | Potentially vulnerable code | Always include security requirements |
| **No custom agents** | Manually switching tools and context each time | Create agents for recurring roles (reviewer, planner, tester) |

---

## Key Takeaways

1. **Structure your prompts** using the CRAFT framework
2. **Be specific** - detail beats brevity
3. **Provide context** - help Copilot understand your project
4. **Use instruction files** (`.instructions.md`) for team-wide consistency
5. **Use prompt files** (`.prompt.md`) for reusable task templates
6. **Use custom agents** (`.agent.md`) to bundle instructions + tools into switchable personas
7. **Include security** from the start
8. **Iterate** - refine prompts based on output
9. **Review everything** - Copilot assists, you decide

---

## Next Steps

- Proceed to [Customisation in Practice](2-Customisation-in-Practice.md) to see how instruction files, prompt files, and custom agents improve documentation, refinement, and debugging workflows
- Complete the [Week 2 Lab](3-Week2-Lab.md) to practice customising your Copilot experience
- Review [Week 2 Prompts](4-Week2-Prompts.md) for additional prompt examples
