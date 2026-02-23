# GitHub Copilot IDE Support

Quick reference for IDE feature availability. For detailed setup instructions, see the [Week 1 Setup and Configuration Guide](../Workshops/Week1/2-Setup-and-Configuration.md).

---

## Supported IDEs

| Category | Platforms |
|----------|-----------|
| Microsoft | VS Code, Visual Studio |
| JetBrains | IntelliJ IDEA, PyCharm, WebStorm, Rider, GoLand, Android Studio |
| Text Editors | Neovim, Vim |
| Other | Xcode, Eclipse, Azure Data Studio |
| Additional | GitHub.com, GitHub Mobile, GitHub CLI, Windows Terminal |

---

## Feature Matrix

Copilot features change frequently, and availability depends on your IDE version, Copilot extension version, and your organisation's policy settings. Use GitHub's feature matrix as the source of truth.

Official feature matrix: https://docs.github.com/en/copilot/reference/copilot-feature-matrix

The table below is a simplified guide that assumes you are using current, stable IDE and extension versions.

| Feature | VS Code | Visual Studio | JetBrains | Eclipse | Xcode |
|---------|---------|---------------|-----------|---------|-------|
| Inline Suggestions | Full | Full | Full | Full | Full |
| Copilot Chat | Full | Full | Full | Full | Full |
| Copilot Edits | Full | Full | Full | No | No |
| Agent Mode | Full | Full | Full | Preview | No |
| Next Edit Suggestions | Full | No | No | Preview | Preview |
| MCP Server Support | Full | No | No | No | No |

Feature availability may vary by subscription plan and IDE version. See the [official feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) for current information.

---

## IDE Selection Guide

| Use Case | Recommended IDE |
|----------|-----------------|
| Most complete Copilot features | VS Code |
| .NET, C#, C++ on Windows | Visual Studio |
| Java, Kotlin, Python | JetBrains IDEs |
| iOS, macOS development | Xcode |
| Terminal-based workflows | Neovim/Vim with GitHub CLI |

VS Code typically receives new Copilot features first, followed by Visual Studio and JetBrains IDEs.

---

## Language-Specific Guides

- [Language Support](language-support.md) - Language-specific limitations, best practices, and integration guidance (includes [ABAP](language-support.md#abap))
