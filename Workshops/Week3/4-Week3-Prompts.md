# GitHub Copilot Prompt Examples - Week 3: MCP and GitHub Copilot

## Session Overview

**Purpose:** Reference guide for practical MCP prompts  
**Format:** Example prompts with explanations and tips  
**Objective:** Provide ready-to-use prompts that demonstrate how to configure MCP servers, invoke tools in Agent Mode, manage GitHub workflows via the GitHub MCP server, and apply security and governance controls across all MCP surfaces.

---

## Contents

- [1. Server Discovery and Setup](#1-server-discovery-and-setup)
- [2. Agent Mode Tool Use](#2-agent-mode-tool-use)
- [3. GitHub Issue and PR Workflows](#3-github-issue-and-pr-workflows)
- [4. Research and Code Exploration](#4-research-and-code-exploration)
- [5. Security and Access Control](#5-security-and-access-control)
- [6. Governance and Enterprise Management](#6-governance-and-enterprise-management)
- [7. Troubleshooting](#7-troubleshooting)
- [Week 3 Feedback](#week-3-feedback)
- [Next Steps](#next-steps)

---

## 1. Server Discovery and Setup

Prompts in this category help you find, understand, and configure MCP servers in VS Code, the Copilot CLI, or the Copilot coding agent. Use them when onboarding a new team to MCP or when adding a server to an existing project.

### Example Prompts

#### Finding Available MCP Servers

```text
// Ask Copilot to recommend MCP servers for a specific use case
I am building a Python web application that reads data from Azure Blob Storage and
exposes a REST API. Which MCP servers would be most useful for GitHub Copilot to
help me with this project? Include the configuration snippet for each server.
```

```text
// Discover what servers are available in the GitHub MCP Registry
Search the GitHub MCP Registry for servers related to cloud infrastructure.
List the server name, publisher, and a brief description for each result.
```

#### Generating a `.vscode/mcp.json` Configuration

```text
// Ask Copilot to generate a workspace MCP configuration for a team project
Generate a .vscode/mcp.json file that configures:
1. The remote GitHub MCP server using Streamable HTTP transport.
2. The Playwright MCP server as a local subprocess via npx.
3. A local filesystem server restricted to the "data" subdirectory.
Ensure that any sensitive values use input variables rather than literal strings.
```

#### Adding a Server to the Copilot CLI

```text
// Configure a new MCP server in the Copilot CLI
I want to add the Context7 MCP server to my Copilot CLI configuration.
The server URL is https://mcp.context7.com/mcp and it requires an API key in a
"CONTEXT7_API_KEY" header. Show me the JSON block to add to
~/.copilot/mcp-config.json and explain each field.
```

> **Tip:** Always specify transport type, authentication method, and the scope (workspace vs user profile vs CLI) when asking Copilot to generate MCP configuration. The more precise the prompt, the more accurate the output.

---

## 2. Agent Mode Tool Use

These prompts demonstrate how to invoke MCP tools in Copilot Agent Mode, both implicitly (natural language) and explicitly using `#tool_name` references. Use them after the MCP server is running and tools are visible in the tool picker.

### Example Prompts

#### Listing Available Tools

```text
// Ask Copilot to describe the tools available from a running MCP server
What tools does the GitHub MCP server currently expose? List each tool by name
and provide a one-sentence description of what it does.
```

#### Implicit Tool Invocation

```text
// Let Copilot choose which tool to use based on natural language intent
List all open pull requests in this repository that have been open for more than
seven days and have no reviewer assigned. For each one, suggest a reviewer from
the list of recent contributors.
```

#### Explicit Tool Invocation Using a Reference

```text
// Explicitly reference a specific tool to guide Copilot's choice
#list_issues List all open issues labelled "enhancement" in this repository.
Group them by estimated complexity (low, medium, high) based on the issue body.
```

```text
// Chain tool calls explicitly for a multi-step workflow
#search_repositories Find the top three Python repositories on GitHub related to
"school management systems". Then #get_repository_details on each one and
summarise their README in two sentences.
```

> **Tip:** Use `#tool_name` references when you know exactly which tool you need and want to prevent Copilot from choosing a different one. For exploratory tasks, natural language intent often produces better results because Copilot can chain multiple tools autonomously.

---

## 3. GitHub Issue and PR Workflows

These prompts leverage the GitHub MCP server's issue and pull request toolsets to manage development work directly from Copilot Agent Mode. They are particularly useful for teams that want to reduce context-switching between the IDE and GitHub.com.

### Example Prompts

#### Creating Issues from Code Analysis

```text
// Analyse the codebase and create issues for identified technical debt
#codebase Identify the top five areas of technical debt in this codebase.
For each area, create a GitHub issue with a title, a description explaining the
problem and its impact, and an acceptance criteria section describing what "done"
looks like.
```

#### Implementing an Issue End-to-End

```text
// Delegate a complete feature implementation to Copilot via MCP
The issue #23 describes a request to add a search filter to the activities page.
Check out a new branch named "feature/search-filter", implement the feature,
write a unit test for the new functionality, push the branch, and open a pull
request targeting "main". Reference issue #23 in the PR body.
```

#### Pull Request Review and Merge

```text
// Ask Copilot to summarise a pull request before you review it
Summarise pull request #17 for me. Include: the problem it solves, the files
changed, any tests added, and whether there are obvious risks or missing pieces
I should check before merging.
```

```text
// Post a structured closing comment on a merged issue
Issue #23 has been resolved by the merged pull request. Post a closing comment
that thanks the contributor, summarises the change in one sentence, and notes
the version or branch where the fix will be available.
```

> **Tip:** When delegating implementation to Copilot via MCP, always start a fresh chat to clear previous context. A clean context reduces the risk of Copilot carrying over incorrect assumptions from earlier in the session.

---

## 4. Research and Code Exploration

These prompts direct Copilot to use MCP tools to search GitHub, compare codebases, explore repository structure, or analyse commit history. They are useful for onboarding, competitive analysis, and understanding unfamiliar projects.

### Example Prompts

#### Searching for Similar Projects

```text
// Search GitHub for open-source projects similar to the current codebase
Search GitHub for JavaScript repositories that implement a task management
application with user authentication. Return the top five results by star count,
including the repository URL, star count, last updated date, and a one-sentence
description.
```

#### Comparing Features Across Repositories

```text
// Compare the features of two repositories to identify gaps
Compare the feature set of "owner/repo-a" with "owner/repo-b". Identify three
features that repo-b has which repo-a is missing, and suggest how each could be
added to repo-a.
```

#### Analysing Commit History

```text
// Summarise recent changes in a repository
Show me the last ten commits to the "main" branch of this repository. Group them
by type (feature, bug fix, refactor, documentation) and identify which contributor
has been most active in the past 30 days.
```

> **Tip:** For research tasks, start your prompts with a clearly stated goal ("I want to understand...", "Find repositories that...", "Summarise the changes...") rather than specifying tool names. Copilot will select and chain the appropriate GitHub MCP tools automatically.

---

## 5. Security and Access Control

These prompts help you configure minimum-scope credentials, enable sandboxing, set tool allowlists, review MCP logs, and understand the trust model. Use them when hardening an MCP configuration or preparing a security review.

### Example Prompts

#### Auditing an MCP Configuration

```text
// Review a .vscode/mcp.json file for security issues
Review the .vscode/mcp.json file in this workspace for security risks. Check for:
hard-coded secrets or tokens, overly broad tool allowlists, servers using the
deprecated SSE transport, missing input variables for sensitive values, and
any server commands that execute code from untrusted sources.
```

#### Generating a Minimum-Scope PAT Scope List

```text
// Determine the minimum PAT scopes required for a set of GitHub MCP toolsets
I want to use the GitHub MCP server with the "repos", "issues", and "pull_requests"
toolsets in read-only mode. What is the minimum set of Personal Access Token scopes
I need to grant? Explain why each scope is required.
```

#### Reviewing the MCP Output Log

```text
// Interpret an MCP output log for unexpected activity
I have pasted the contents of my MCP output log below. Identify any tool calls
that appear unexpected or potentially harmful, and explain what each suspicious
call was attempting to do.

[paste log contents here]
```

> **Tip:** Use the `--read-only` flag for the GitHub MCP server in environments where you only need to read data. This prevents any accidental write operations even if a prompt injection attack attempts to trigger a mutating tool.

---

## 6. Governance and Enterprise Management

These prompts are aimed at administrators and team leads who need to enable MCP for an organisation, configure VS Code enterprise policies, or set up a private MCP registry. Use them when rolling out MCP across a team or enterprise.

### Example Prompts

#### Enabling MCP in a GitHub Organisation

```text
// Guide an administrator through enabling the MCP policy
I am an organisation administrator on GitHub and I want to enable MCP server
support for all members using Copilot Business. Walk me through the steps to
enable the "MCP servers in Copilot" policy, and explain what happens to users
who are on Copilot Free or Pro plans.
```

#### Configuring VS Code Policies via Intune

```text
// Generate an Intune policy JSON for VS Code MCP governance
Generate a VS Code policy configuration for Intune that:
1. Restricts MCP usage to approved servers from our private registry at
   https://mcp-registry.internal.example.com.
2. Prevents users from enabling global auto-approval of tool calls.
3. Disables Agent Mode for all users on the Finance team device group.
Include the policy key names and valid values for each setting.
```

#### Documenting MCP Governance for a Team

```text
// Draft a team MCP governance guide
Draft a one-page MCP governance guide for our development team. It should cover:
which MCP servers are approved for use, how to request approval for a new server,
the minimum PAT scope requirements, how to report a suspected prompt injection
incident, and who to contact for policy questions.
```

> **Tip:** When writing governance documentation, ask Copilot to include references to specific policy setting names (`ChatMCP`, `McpGalleryServiceUrl`) and the official GitHub Docs and VS Code enterprise documentation pages so that the guidance stays auditable and up to date.

---

## 7. Troubleshooting

These prompts address common problems encountered when working with MCP servers: servers that do not start, tools that do not appear in Agent Mode, authentication failures, and network policy blocks.

### Example Prompts

#### MCP Server Not Starting

```text
// Diagnose why an MCP server is not starting in VS Code
My MCP server named "playwright" is configured in .vscode/mcp.json but it does
not appear as running in the MCP: List Servers output. The server command is
"npx @playwright/mcp@latest". What are the most common reasons a stdio MCP server
fails to start in VS Code, and how do I diagnose each one?
```

#### Tools Not Appearing in Agent Mode

```text
// Troubleshoot missing tools in the Agent Mode tool picker
I have configured the GitHub MCP server in .vscode/mcp.json and the server shows
as running in MCP: List Servers, but no GitHub tools appear in the Copilot Agent
Mode tool picker. What are the possible causes and how do I fix each one?
```

#### Docker Path Quoting on Windows

```text
// Resolve Docker command path issues on Windows
I am on Windows and my Docker-based MCP server command in mcp.json is failing
with a path-not-found error. The command is:
"docker run -i --rm ghcr.io/github/github-mcp-server"
How should I format the command and args array in mcp.json to avoid path
quoting issues on Windows?
```

#### Authentication Failures

```text
// Debug an OAuth or PAT authentication failure for the GitHub MCP server
The GitHub MCP server is returning a 401 Unauthorized error. I am using the
remote server at https://api.githubcopilot.com/mcp/ and I have a GitHub
Copilot subscription. Walk me through the steps to diagnose and resolve the
authentication failure, including how to reset the OAuth sign-in if needed.
```

> **Tip:** For most MCP issues, start by running **MCP: List Servers** in the VS Code Command Palette and selecting **Show Output** for the affected server. The output log contains the raw JSON-RPC messages and any error responses, which usually identify the root cause within the first few lines.

---

## Week 3 Feedback

Please complete the following reflections after completing Week 3 activities:

- [Submit Week 3 Lab Reflection](../../issues/new?template=week3-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

## Next Steps

After mastering MCP integration with GitHub Copilot in Week 3, we will explore DevOps automation, testing strategies, and GitHub Copilot CLI workflows in Week 4 to streamline software delivery.

**[← Back to Main README](../../README.md)** | **[Continue to Week 4 →](../Week4/1-DevOps-Automation.md)**
