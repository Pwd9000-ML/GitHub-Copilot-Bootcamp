# GitHub Copilot Quick Reference Guide

A quick reference for training participants. For detailed instructions, see the Week 1 Setup and Configuration Guide in the workshop materials.

## Contents

- [Installation and Setup](#installation-and-setup)
- [Usage and Features](#usage-and-features)
- [Troubleshooting](#troubleshooting)

---

## Installation and Setup

### Supported IDEs

VS Code, Visual Studio, JetBrains IDEs, Eclipse, Vim/Neovim, Xcode, Azure Data Studio, GitHub Mobile, Windows Terminal.

### Quick Install

1. Open your IDE's extension/plugin marketplace
2. Search for "GitHub Copilot"
3. Install and restart your IDE
4. Sign in with your GitHub account when prompted

### Proxy Setup (VPN Users)

**VS Code:** Settings > search "proxy" > enter your proxy URL

**Environment variables:**
```bash
export HTTP_PROXY=http://proxy-server-url:port
export HTTPS_PROXY=http://proxy-server-url:port
```

Contact your IT team for your organisation's specific proxy settings.

---

## Usage and Features

### Does GitHub Copilot save chat history?

Copilot uses your prompts and relevant context to generate responses. How GitHub processes and retains Copilot data depends on your plan, settings, and where you use Copilot (for example, an IDE or GitHub.com).

See the [GitHub Copilot Trust Center](https://copilot.github.trust.page/) for current privacy and retention details.

### Supported programming languages

GitHub Copilot supports most programming languages. Performance is typically best for popular languages: JavaScript, Python, Java, TypeScript, Go, Ruby, PHP, C++, C#, and Swift.

### Cross-repository context

GitHub Copilot primarily references code within the active file and local repository. To include context from multiple repositories, open them in a single workspace or use Git submodules.

### Database support

GitHub Copilot can assist with:
- SQL queries (SELECT, INSERT, UPDATE, DELETE, JOINs, subqueries)
- ORM code (SQLAlchemy, Sequelize, Django ORM)
- Database migrations and schema definitions

It cannot connect to live databases or automatically detect your schema.

### Code generation scope

GitHub Copilot generates both small snippets and larger blocks including entire functions, classes, or modules. Always review and test generated code.

### Key features

| Feature | Description |
|---------|-------------|
| Code completion | Real-time inline suggestions |
| Copilot Chat | Natural language coding assistance |
| Agent Mode | Autonomous multi-file changes |
| Copilot Edits | Multi-file edits from a single prompt |
| Code Review | AI suggestions on pull requests |
| PR Summaries | Auto-generated pull request descriptions |
| Test Generation | Automatic unit test creation |

### Context and limits

GitHub Copilot Chat uses your current file, chat history, and workspace context to provide relevant responses. Use `@workspace` to help Copilot retrieve relevant files from your codebase.

Copilot Free includes **50 messages per month** for Copilot Chat in IDEs. Other plans have different entitlements, including premium request allowances.

See [Plans for GitHub Copilot](https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot) for up to date limits.

See the [GitHub Copilot documentation](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features) for full feature details.

---

## Troubleshooting

### Extension activation failed / Cannot connect to server

1. Update GitHub Copilot to the latest version
2. Sign out and sign back in
3. Check your subscription at [GitHub Billing Settings](https://github.com/settings/billing)

### Authentication issues

**Stuck on sign-in screen:**
1. Open Command Palette (Ctrl+Shift+P)
2. Run "GitHub Copilot: Sign Out"
3. Sign back in
4. Check proxy/firewall settings if on a corporate network

**Repeated sign-in prompts:**
1. Clear VS Code credentials: Settings > User > Clear Saved Credentials
2. Reinstall the GitHub Copilot extension

### No code suggestions appearing

1. Check the Copilot icon in the status bar (diagonal line means disabled)
2. Ensure you are editing a supported file type (.js, .py, .ts, etc.)
3. Try disabling other extensions that may conflict

### 403 Forbidden error

Wait 10-15 minutes if you have made multiple authentication attempts. Check [GitHub Status](https://www.githubstatus.com) for service issues.

### Corporate firewall blocking authentication

1. Configure proxy settings in VS Code (see Proxy Setup above)
2. Ask your IT team to whitelist GitHub's authentication endpoints
3. See [GitHub's network requirements](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-githubs-use-of-your-data)

### Licence not recognised

**VS Code:**
1. Close VS Code
2. Delete cache: `%APPDATA%\Code\CachedData` (Windows) or `~/Library/Application Support/Code/CachedData` (macOS)
3. Clear credentials in Windows Credential Manager or macOS Keychain
4. Reopen and sign in again

**JetBrains:**
1. Close the IDE
2. Delete cache contents from `.IntelliJIDEA<version>\system` (Windows) or `~/Library/Caches/JetBrains/<version>` (macOS)
3. Remove GitHub credentials in Settings > Passwords
4. Reopen and sign in again

### GHE.com sign-in issues

In VS Code settings, search for "Copilot", open settings.json under GitHub > Copilot: Advanced, and remove the line `"authProvider": "github-enterprise"` if present.

---

## Further Help

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Copilot Trust Center](https://copilot.github.trust.page/)
- [GitHub Support Community](https://github.com/orgs/community/discussions)
- [Official FAQ](https://github.com/features/copilot#faq)

---

**Last updated:** January 2026
