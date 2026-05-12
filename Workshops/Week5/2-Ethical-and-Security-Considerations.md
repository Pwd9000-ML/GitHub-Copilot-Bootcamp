# Ethical and Security Considerations with GitHub Copilot

**Duration:** 30-45 minutes  
**Format:** Discussion-led session with real-world scenarios  
**Objective:** Understand the ethical implications, security risks, and responsible practices when using AI-assisted coding tools.

---

## Session Overview

AI coding assistants like GitHub Copilot are powerful tools, but they come with responsibilities. This session explores the critical ethical and security considerations developers must understand.

**What you'll learn:**
- Intellectual property considerations in AI-generated code
- Security vulnerabilities and how to prevent them
- Responsible AI usage and bias awareness
- Organisational policies and compliance
- Best practices for safe AI-assisted development
- Enterprise controls for models, policies, custom instructions, content exclusion, and data residency
- Agent-specific risks such as prompt injection, data exfiltration, tool permissions, and MCP server trust

---

## 1. Intellectual Property Considerations

### Understanding How Copilot Works

GitHub Copilot was trained on publicly available code from GitHub repositories. This raises important questions:

| Concern | Description | Mitigation |
|---------|-------------|------------|
| **License Attribution** | Generated code may resemble open-source code | Review for familiar patterns, add attribution where needed |
| **Copyrighted Code** | Suggestions may match publicly available code | Configure whether suggestions matching public code are allowed, and review code references when they appear |
| **Company IP** | Prompt and code handling depends on your plan and organisation settings | Follow your organisation policy, and review GitHub Copilot data and policy settings |
| **Patent Concerns** | Generated algorithms might infringe patents | Review novel implementations carefully |

### Copilot Settings for IP Protection

**Suggestions matching public code and code referencing**

GitHub Copilot can be configured to allow or block suggestions that match publicly available code. If suggestions matching public code are allowed, Copilot can also provide references to similar public code ("code referencing").

This is configured in either your personal settings or your organisation settings on GitHub.com.

In Visual Studio Code you can also view code references for accepted suggestions via the "GitHub Copilot Log (Code References)" output.

### Best Practices for IP Safety

1. **Review generated code** - Don't blindly accept, especially for algorithms
2. **Check for attribution** - If code looks familiar, search for its origin
3. **Use organisation settings** - Enable corporate IP protections
4. **Document AI usage** - Note when significant code is AI-generated
5. **Understand your licence** - Know what Copilot's terms allow

---

## 2. Data Protection and Enterprise Governance

Copilot features are governed by plan, policy, IDE, and organisation settings. The safest curriculum stance is to teach learners to verify the current policy before using advanced agents, external tools, or sensitive code.

### Governance Controls to Know

| Control | Why it matters | Learner action |
|---------|----------------|----------------|
| Feature policies | Organisations can enable or disable features such as agents, models, code review, and preview capabilities | Check policy before assuming a feature is available |
| Model controls | Available models, premium request costs, and data residency options can vary | Use approved models and avoid hardcoded model names in shared guidance |
| Content exclusion | Repositories or paths can be excluded from some Copilot features | Confirm the exact surfaces where exclusion applies before relying on it |
| Organisation custom instructions | Shared instructions can enforce standards across repositories | Review inherited instructions when Copilot behaviour seems unexpected |
| MCP and external tools | Tools can expose data or take actions outside the IDE | Use trusted servers only and scope permissions carefully |
| BYOK and data residency | Some organisations control model providers or regional processing | Follow enterprise guidance for regulated workloads |

> **Important:** Content exclusion does not apply uniformly to every Copilot surface. GitHub Docs state that Copilot CLI, Copilot cloud agent, and Agent mode in Copilot Chat in IDEs do not support content exclusion. Verify the current [content exclusion documentation](https://docs.github.com/en/copilot/how-tos/configure-content-exclusion/exclude-content-from-copilot) before using sensitive repositories or paths.

### Governance Prompt

```text
Review our planned Copilot rollout for governance gaps.
Cover feature policies, model access, content exclusion limits, custom instructions, MCP tools, code review automation, usage metrics, and human approval requirements.
Return risks, recommended controls, and owner actions.
```

---

## 3. Security Vulnerabilities

### Common Security Risks in AI-Generated Code

**1. SQL Injection Vulnerabilities**

**Risky Generated Code:**
```python
def get_user(username):
    # DANGEROUS: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return db.execute(query)
```

**Secure Alternative:**
```python
def get_user(username: str) -> Optional[User]:
    """Safely retrieve user by username using parameterised query."""
    query = "SELECT * FROM users WHERE username = %s"
    return db.execute(query, (username,))
```

**2. Hardcoded Secrets**

**Risky Pattern:**
```python
# DANGEROUS: Copilot might suggest realistic-looking credentials
API_KEY = "sk_example_do_not_use"
DATABASE_URL = "postgresql://user:password@localhost:5432/dbname"
```

Tip: Use clearly fake placeholders in examples to avoid triggering secret scanners or accidental reuse.

**Secure Alternative:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")

if not API_KEY or not DATABASE_URL:
    raise EnvironmentError("Required environment variables not set")
```

**3. Insecure Cryptography**

**Risky Generated Code:**
```python
import hashlib

def hash_password(password):
    # DANGEROUS: MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()
```

**Secure Alternative:**
```python
import bcrypt

def hash_password(password: str) -> bytes:
    """Hash password using bcrypt with appropriate work factor."""
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def verify_password(password: str, hashed: bytes) -> bool:
    """Verify password against stored hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
```

**4. Path Traversal Vulnerabilities**

**Risky Generated Code:**
```python
def read_file(filename):
    # DANGEROUS: Allows reading any file on the system
    with open(f"/uploads/{filename}") as f:
        return f.read()
```

**Secure Alternative:**
```python
import os
from pathlib import Path

UPLOAD_DIR = Path("/uploads").resolve()

def read_file(filename: str) -> str:
    """Safely read file from uploads directory."""
    # Resolve the path and verify it's within UPLOAD_DIR
    file_path = (UPLOAD_DIR / filename).resolve()
    
    if not file_path.is_relative_to(UPLOAD_DIR):
        raise ValueError("Invalid file path")
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {filename}")
    
    return file_path.read_text()
```

---

### Security Review Prompts

**Prompt for Security Audit:**
```text
Perform a security audit on this code. Check for:
1. Injection vulnerabilities (SQL, command, XSS)
2. Authentication/authorisation flaws
3. Cryptographic weaknesses
4. Sensitive data exposure
5. Input validation gaps
6. Error handling issues that leak information

Provide severity rating and remediation for each finding.

[paste code here]
```

**Prompt for Secure Implementation:**
```text
Generate a secure implementation with these requirements:
- Input validation and sanitisation
- Parameterised queries for database access
- No hardcoded credentials
- Proper error handling without information leakage
- Secure cryptographic functions where needed
- OWASP Top 10 protection

Function: User authentication with password hashing
```

---

### Security Scanning Integration

**Prompt for Pre-Commit Security Check:**
```text
Create a pre-commit hook that scans for:
1. Hardcoded API keys or secrets (regex patterns)
2. SQL string concatenation
3. eval() or exec() usage
4. Insecure hash functions (MD5, SHA1)
5. HTTP URLs instead of HTTPS
6. Debug/development flags in production code

Fail commit if any issues found.
```

### GitHub Security Features to Pair with Copilot

| Feature | Purpose | Copilot-assisted workflow |
|---------|---------|---------------------------|
| Secret scanning and push protection | Prevent secrets from entering repositories | Ask Copilot to explain a blocked push and help rotate or remove the secret safely |
| Code scanning with CodeQL | Find vulnerabilities in code and pull requests | Ask Copilot to triage an alert, explain the data flow, and propose a minimal fix |
| Copilot Autofix | Suggest remediations for supported code scanning alerts | Ask Copilot to justify why the Autofix is safe before applying it |
| Dependency review | Flag risky dependency changes in pull requests | Ask Copilot to summarise package risk, alternatives, and required updates |
| Security and quality tab | Centralise security and code quality findings on GitHub | Ask Copilot to group findings by owner, severity, and remediation effort |

**Prompt for alert triage:**
```text
Explain this CodeQL alert in plain language.
Identify the source, sink, exploitability, likely false-positive reasons, safest fix, and tests that should prove the fix.
Do not apply an Autofix until you have explained the trade-offs.
```

---

## 4. Responsible AI Usage

### Bias in AI-Generated Code

AI models can perpetuate biases present in training data:

| Bias Type | Example | Impact |
|-----------|---------|--------|
| **Variable naming** | Gender-specific defaults | Exclusionary code |
| **Assumptions** | Western-centric date formats | International users affected |
| **Stereotypes** | Role-based examples | Reinforces social biases |
| **Accessibility** | Missing ARIA labels | Excludes disabled users |

**Example of Biased Generation:**
```javascript
// Prompt: "Create a user profile form"
// Potentially biased output:
const userForm = {
    title: ['Mr', 'Mrs', 'Miss'],  // Missing inclusive options
    gender: ['Male', 'Female'],     // Binary assumption
    name: { first: '', last: '' }   // Assumes Western naming convention
};
```

**Inclusive Alternative:**
```javascript
const userForm = {
    title: ['Mr', 'Mrs', 'Ms', 'Mx', 'Dr', 'Prof', 'Prefer not to say'],
    gender: ['Male', 'Female', 'Non-binary', 'Prefer to self-describe', 'Prefer not to say'],
    name: { 
        displayName: '',      // Flexible for all cultures
        legalName: '',        // When legally required
        preferredName: ''     // User preference
    }
};
```

### Prompting for Inclusive Code

**Prompt:**
```text
Generate a user registration form that:
- Uses inclusive language and options
- Supports international name formats
- Provides flexible gender options
- Includes accessibility features (ARIA labels)
- Works with screen readers
- Supports right-to-left languages
```

---

### AI Transparency

**When to disclose AI usage:**

- **Internal documentation** - Note when significant code blocks are AI-generated
- **Code reviews** - Inform reviewers of AI assistance
- **Compliance contexts** - Some industries require disclosure
- **Educational settings** - Academic integrity requirements

**Documentation Pattern:**
```python
# AI-ASSISTED: Initial implementation generated with GitHub Copilot
# REVIEWED: [Date] by [Developer]
# MODIFIED: [List significant changes from original generation]
def complex_algorithm():
    """
    Implementation of X algorithm.
    
    Note: Core logic AI-generated, security review completed,
    edge cases added manually.
    """
    pass
```

---

## 5. Organisational Policies

### Developing an AI Coding Policy

**Key Policy Components:**

```markdown
# AI-Assisted Coding Policy

## Approved Tools
- GitHub Copilot through approved individual or managed organisation access
- [List other approved tools]

## Prohibited Uses
- Generating code for security-critical systems without review
- Using AI for client-confidential codebases without approval
- Accepting suggestions without understanding them
- Bypassing code review processes

## Required Practices
1. Configure whether suggestions matching public code are allowed, and use code referencing when it is available
2. Review all AI suggestions before accepting
3. Run security scans on AI-generated code
4. Document significant AI-assisted implementations
5. Report concerning suggestions

## Data Handling
- No client data in prompts
- No proprietary algorithms as context
- Follow data classification guidelines
- Confirm whether content exclusion, model policy, and data residency controls apply to the Copilot surface being used
- Use trusted MCP servers only and record approved tool scopes

## Review Requirements
- AI-generated code requires standard code review
- Security-sensitive code requires additional security review
- Novel algorithms require architecture review
- Agent-generated changes require diff review, tests, and tool activity review before merge
```

### Team Guidelines Prompt

**Prompt:**
```text
Create a team code review checklist specifically for AI-generated code:
- What additional scrutiny is needed?
- What patterns should reviewers watch for?
- How should AI assistance be documented in PRs?
- What questions should reviewers ask?
```

---

## 6. Practical Security Checklist

### Before Accepting AI Suggestions

- [ ] **Understand the code** - Can you explain what it does?
- [ ] **Check inputs** - Is all user input validated?
- [ ] **Review queries** - Are database queries parameterised?
- [ ] **Verify authentication** - Is access properly controlled?
- [ ] **Examine secrets** - Are there any hardcoded credentials?
- [ ] **Test error handling** - Does it fail safely?
- [ ] **Consider edge cases** - What happens with unexpected input?

### Code Review Checklist for AI-Generated Code

- [ ] **Logic verification** - Does the code do what was intended?
- [ ] **Security review** - Are there any OWASP Top 10 vulnerabilities?
- [ ] **Performance check** - Are there efficiency concerns?
- [ ] **Dependency review** - Are imported libraries secure and necessary?
- [ ] **Test coverage** - Are tests comprehensive and meaningful?
- [ ] **Documentation** - Is the code properly documented?
- [ ] **Standards compliance** - Does it follow team conventions?
- [ ] **Tool activity** - Did an agent run commands, fetch external content, or call MCP tools that need review?
- [ ] **Policy alignment** - Did the workflow respect content exclusion, model, data residency, and approval requirements?

---

## 7. Agent Threat Model

Agentic workflows introduce risks beyond code completion because agents can use tools, read broader context, and run commands where approved.

| Risk | Example | Mitigation |
|------|---------|------------|
| Prompt injection | A README or web page tells the agent to ignore project rules | Treat external and repository text as untrusted instructions, and ask Copilot to identify conflicting instructions |
| Data exfiltration | An agent sends sensitive context to an external tool or URL | Restrict tools, avoid sensitive files, and review network access approvals |
| Over-broad terminal permissions | An agent runs destructive commands or modifies deployment state | Require approval, use granular permissions, and use disposable environments for training |
| Untrusted MCP servers | A server exposes unexpected data or performs unexpected actions | Use approved MCP servers only, document permissions, and disable unused tools |
| Cloud-agent runner risk | Background work runs in organisation-controlled infrastructure | Configure runner controls, firewall settings, signed commits, and audit logs |
| False confidence | Copilot comments on a PR and reviewers assume it approved the change | Teach that Copilot Code Review is advisory and human approval remains required |

**Prompt:**
```text
Threat model this agentic workflow.
Identify prompt injection risks, sensitive data exposure, unsafe tools, MCP server risks, terminal command risks, and human approval checkpoints.
Recommend controls before we let an agent implement the task.
```

---

## 8. Scenario Exercises

### Scenario 1: Suspicious Suggestion

You ask Copilot to generate a login function and it produces:

```python
def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    # ... rest of implementation
```

**Discussion:**
- Why might Copilot suggest this?
- What's the security risk?
- How should you respond?

---

### Scenario 2: Familiar Code

Copilot suggests a sorting algorithm that looks identical to a well-known open-source implementation.

**Discussion:**
- What are the IP implications?
- Should you accept this suggestion?
- How do you verify the origin?

---

### Scenario 3: Biased Generation

When generating test data, Copilot produces:

```javascript
const employees = [
    { name: 'John', role: 'Engineer', salary: 100000 },
    { name: 'Sarah', role: 'Secretary', salary: 45000 },
    { name: 'Mike', role: 'Manager', salary: 120000 }
];
```

**Discussion:**
- What bias is present?
- How might this affect your application?
- How would you prompt for better test data?

---

## Key Takeaways

1. **AI is a tool, not a replacement** - You remain responsible for the code
2. **Trust but verify** - Always review AI suggestions critically
3. **Security first** - Assume AI-generated code may have vulnerabilities
4. **Be inclusive** - Actively prompt for unbiased, accessible code
5. **Know your policies** - Understand your organisation's AI guidelines
6. **Document appropriately** - Track AI assistance for transparency
7. **Govern agents deliberately** - Review tool permissions, MCP servers, model policies, and approval boundaries
8. **Understand content exclusion limits** - Do not assume one policy applies to every Copilot surface
9. **Use security platforms together** - Pair Copilot with secret scanning, push protection, code scanning, dependency review, and human review
10. **Stay informed** - AI capabilities and risks evolve rapidly

---

## Next Steps

- Complete the [Week 5 Lab](3-Week5-Lab.md) covering collaborative refactoring exercises
- Review the [Week 5 Prompts](4-Week5-Prompts.md) for security-focused prompt examples
- Revisit [Week 5 Overview](../../README.md) for additional resources
