# MCP Foundations: Connecting GitHub Copilot to the World

## Session Overview

**Duration:** 45-60 minutes  
**Format:** Presentation with live demonstration  
**Objective:** Understand the Model Context Protocol specification, learn how to add and configure MCP servers in VS Code, and use MCP tools in Copilot Agent Mode to extend Copilot's capabilities beyond the IDE.

---

## Contents

- [1. MCP Specification Fundamentals](#1-mcp-specification-fundamentals)
- [2. Adding MCP Servers to VS Code Copilot](#2-adding-mcp-servers-to-vs-code-copilot)
- [3. Using MCP Tools in Agent Mode](#3-using-mcp-tools-in-agent-mode)
- [Best Practices](#best-practices)
- [Key Takeaways](#key-takeaways)
- [Classroom Discussion Questions](#classroom-discussion-questions)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

---

## 1. MCP Specification Fundamentals

### What Is the Model Context Protocol?

The Model Context Protocol (MCP) is an open standard that defines a universal way for AI applications to connect to external data sources, tools, and workflows. Before MCP, each AI application had to build bespoke integrations with every external service, creating an N times M integration problem. MCP collapses this to N plus M by providing one standardised protocol that any host can speak and any server can implement.

The MCP project describes itself as "USB-C for AI applications": a universal connector that eliminates one-off glue code. MCP was originally created by Anthropic and is now maintained as an open community project. Sources: [modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction), [modelcontextprotocol.io/docs/concepts/architecture](https://modelcontextprotocol.io/docs/concepts/architecture).

### JSON-RPC Architecture

MCP is a two-layer protocol:

- **Data layer.** Encodes all messages as JSON-RPC 2.0 requests, responses, and notifications. It governs lifecycle management (initialisation, capability negotiation, termination), exposes primitives (see table below), and defines cross-cutting utilities such as notifications and progress tracking. Every JSON-RPC message must be UTF-8 encoded.
- **Transport layer.** Handles the physical communication channel and authentication, abstracting away the difference between a local subprocess and a remote HTTPS endpoint.

```json
// Example JSON-RPC 2.0 tool call message (MCP data layer)
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_issue",
    "arguments": {
      "owner": "my-org",
      "repo": "my-repo",
      "title": "Add dark mode support",
      "body": "Users have requested a dark mode option."
    }
  }
}
```

### Participants: Host, Client, and Server

An MCP **host** is any AI application that coordinates the session. For example, VS Code or the Copilot CLI acts as the host. The host instantiates one **MCP client** object per connected server. Each client maintains a dedicated session with its corresponding **MCP server**. A single host can therefore be connected to multiple servers simultaneously.

MCP servers can run:

- **Locally**, as a subprocess on the same machine as the host (stdio transport).
- **Remotely**, as an independent networked process (Streamable HTTP transport).

```
┌──────────────────────────────────────────────────────────┐
│  MCP Host (e.g., VS Code with GitHub Copilot)            │
│                                                          │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   │
│  │  MCP Client │   │  MCP Client │   │  MCP Client │   │
│  │  (GitHub)   │   │ (Playwright)│   │  (Custom)   │   │
│  └──────┬──────┘   └──────┬──────┘   └──────┬──────┘   │
│         │                 │                 │           │
└─────────┼─────────────────┼─────────────────┼───────────┘
          │ stdio/HTTP       │ stdio/HTTP       │ stdio/HTTP
          ▼                 ▼                 ▼
    ┌──────────┐      ┌──────────┐      ┌──────────┐
    │  GitHub  │      │Playwright│      │  Custom  │
    │  Server  │      │  Server  │      │  Server  │
    └──────────┘      └──────────┘      └──────────┘
```

### Primitives

Servers expose three **server-side primitives**:

| Primitive | Offered by | Description | Discovery method |
|-----------|------------|-------------|-----------------|
| **Tool** | Server | Executable function invoked by the AI (file writes, API calls, database queries) | `tools/list`, executed via `tools/call` |
| **Resource** | Server | Read-only data attached as context (file contents, database records, API responses) | `resources/list`, fetched via `resources/read` |
| **Prompt** | Server | Reusable interaction template that guides the model | `prompts/list`, retrieved via `prompts/get` |

Clients expose two **client-side primitives**:

| Primitive | Offered by | Description |
|-----------|------------|-------------|
| **Sampling** | Client | Allows a server to request an LLM completion from the host |
| **Elicitation** | Client | Allows a server to request additional information from the user |

Source: [modelcontextprotocol.io/docs/concepts/architecture](https://modelcontextprotocol.io/docs/concepts/architecture).

### Transport Mechanisms

MCP currently specifies two recommended transport mechanisms:

| Transport | Status | Typical use case | Authentication |
|-----------|--------|-----------------|----------------|
| **stdio** | Current and recommended | Local subprocess on the same machine | N/A (process trust) |
| **Streamable HTTP** | Current and recommended | Remote or local server over HTTP | Bearer tokens, OAuth, API keys |
| HTTP+SSE | Deprecated (spec 2024-11-05 only; still supported by many clients for backward compatibility) | Remote server with SSE streaming | Bearer tokens, API keys |

Sources: [modelcontextprotocol.io/specification/2025-03-26/basic/transports](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports).

---

## 2. Adding MCP Servers to VS Code Copilot

### Configuration Scopes

MCP servers in VS Code are defined in a `mcp.json` configuration file. There are four scopes:

| Scope | File location | Sharing |
|-------|--------------|---------|
| **Workspace** | `.vscode/mcp.json` in the project root | Check into version control to share with the team |
| **User profile** | Opened via the command **MCP: Open User Configuration** | Available in every workspace for the current profile |
| **Dev Container** | `devcontainer.json` under `customizations.vscode.mcp.servers` | Written to the remote `mcp.json` at container creation time |
| **Command line** | `code --add-mcp '{"name":"...","command":"...","args":[]}'` | Adds a server to the user profile |

The Extensions view also lets you browse the GitHub MCP Registry (public preview) by searching `@mcp`, then selecting **Install** (user profile) or right-clicking and selecting **Install in Workspace** (`.vscode/mcp.json`).

### Configuration File Structure

```json
// .vscode/mcp.json - workspace-scoped MCP server configuration
{
  "servers": {
    "github": {
      // Remote GitHub MCP server using Streamable HTTP transport (requires VS Code 1.101+)
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "playwright": {
      // Local Playwright MCP server launched via npx (stdio transport)
      "type": "stdio",
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "filesystem": {
      // Local filesystem MCP server restricted to a specific directory
      "type": "stdio",
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "${workspaceFolder}/data"
      ]
    },
    "fetch-server": {
      // Remote MCP server using an API key stored as an input variable
      // VS Code prompts once and stores the value securely
      "type": "stdio",
      "command": "uvx",
      "args": ["mcp-server-fetch"],
      "env": {
        "API_KEY": "${input:fetch-api-key}"
      }
    }
  },
  "inputs": [
    {
      // Declares a named secret; VS Code prompts the user and stores securely
      "id": "fetch-api-key",
      "type": "promptString",
      "description": "API key for the fetch server",
      "password": true
    }
  ]
}
```

Key rules:
- Use `"type": "stdio"` for local subprocess servers (provide `"command"` and `"args"`).
- Use `"type": "http"` for remote Streamable HTTP servers (provide `"url"`).
- Use `"type": "sse"` for legacy HTTP+SSE servers (deprecated; use only for backward compatibility).
- Never hard-code secrets. Use `${input:variable-id}` references so VS Code prompts and stores them securely.

Sources: [code.visualstudio.com/docs/copilot/chat/mcp-servers](https://code.visualstudio.com/docs/copilot/chat/mcp-servers), [code.visualstudio.com/docs/copilot/reference/mcp-configuration](https://code.visualstudio.com/docs/copilot/reference/mcp-configuration).

### Enabling MCP in VS Code

The setting `chat.mcp.enabled` controls whether MCP support is active. It is enabled by default in VS Code when the GitHub Copilot Chat extension is installed.

```jsonc
// settings.json - enabling MCP support and auto-discovery
{
  // Enable MCP support in Copilot Chat (default: true)
  "chat.mcp.enabled": true,

  // Auto-discover MCP server configurations from other applications (e.g., Claude Desktop)
  "chat.mcp.discovery.enabled": true,

  // Automatically restart MCP servers when their configuration changes (experimental)
  "chat.mcp.autoStart": true
}
```

### The Trust Prompt

When an MCP server is started for the first time, or when its configuration changes, VS Code presents a trust dialogue. If the user declines, the server does not start. Important notes:

- The command **MCP: Reset Trust** clears all stored trust decisions.
- Starting a server directly from the **Start** code lens in `mcp.json` bypasses the trust prompt. This pattern is not recommended for untrusted servers.
- Once trusted, a server starts automatically on workspace open.

### Auto-Discovery

Setting `"chat.mcp.discovery.enabled": true` instructs VS Code to detect and reuse MCP server configurations from other installed applications, such as Claude Desktop. This is a multi-select setting where each enabled source is polled for its existing MCP configuration. Source: [docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp).

### Sandboxing Local Servers

On macOS and Linux, setting `"sandboxEnabled": true` in a server's configuration restricts a stdio server's access to the file system and network. The `sandbox` object accepts sub-fields including `filesystem.allowWrite`, `filesystem.denyRead`, `filesystem.denyWrite`, `network.allowedDomains`, and `network.deniedDomains`. When a server is sandboxed, tool call confirmations are auto-approved. Sandboxing is not yet available on Windows.

```json
// .vscode/mcp.json - example sandbox configuration (macOS and Linux only)
{
  "servers": {
    "fetch-server": {
      "type": "stdio",
      "command": "uvx",
      "args": ["mcp-server-fetch"],
      "sandboxEnabled": true,
      "sandbox": {
        // Restrict network access to these domains only
        "network": {
          "allowedDomains": ["docs.github.com", "code.visualstudio.com"]
        },
        // Deny all file-system writes to protect local files
        "filesystem": {
          "denyWrite": ["/"]
        }
      }
    }
  }
}
```

Source: [code.visualstudio.com/docs/copilot/reference/mcp-configuration](https://code.visualstudio.com/docs/copilot/reference/mcp-configuration).

### Managing Servers

The VS Code command palette provides the following MCP-related commands:

| Command | Purpose |
|---------|---------|
| `MCP: Open User Configuration` | Open the user-profile `mcp.json` |
| `MCP: List Servers` | Show all configured servers and their status |
| `MCP: Reset Trust` | Clear all stored trust decisions |
| `MCP: Browse Resources` | Browse resources exposed by running servers |

---

## 3. Using MCP Tools in Agent Mode

### How Agent Mode Exposes MCP Tools

MCP tools are available exclusively in **Agent Mode** in Copilot Chat. When a user submits a prompt in Agent Mode, the host sends the full tool catalogue (names and input schemas from all running MCP servers) alongside the user message. The model decides autonomously which tools to call and with what arguments. Results are streamed back and fed into the next reasoning step.

To access the tool picker in Agent Mode:

1. Open Copilot Chat and select **Agent** in the mode selector at the bottom of the chat panel.
2. Click the **Configure Tools** button (spanner or wrench icon) to see and toggle individual tools and MCP servers.
3. The tool picker groups tools by server. You can enable or disable entire servers, or individual tools within a server.

### Approving Tool Calls

By default, VS Code asks for approval before each tool invocation. The approval dialogue shows:

- The name of the tool being called.
- The arguments the model has prepared.
- A brief description of what the tool will do.

Users can grant session-wide auto-approval for specific tools or for all tools via the **permissions picker** in the chat panel:

- **Per-call approval**: the default. Review each invocation individually.
- **Bypass Approvals for this server**: auto-approve all calls to a specific server for the current session.
- **Autopilot**: auto-approve all tool calls for the current session.

Always verify tool arguments before approving destructive actions (file writes, repository changes, deletions).

### Referencing Tools Explicitly

To nudge Copilot to use a specific tool rather than choosing automatically, include a `#tool_name` reference in the prompt:

```text
// Explicitly invoke the create_issue tool from the GitHub MCP server
#create_issue Create an issue titled "Add dark mode toggle" with a description
explaining the user request and suggesting implementation using a CSS variable approach.
```

```text
// Use the GitHub MCP server to search for similar open-source projects
#search_repositories Find Python web applications that manage school extracurricular
activities. List the top five by star count.
```

### Working with Resources and Prompts

In addition to tools, MCP servers may expose **resources** and **prompts**:

- **Resources**: Accessible via **Add Context > MCP Resources** in the Chat view, or by running the command **MCP: Browse Resources**. Resources appear as context attachments similar to files.
- **Prompts**: Accessible via slash commands in the format `/mcp.servername.promptname`. For example, if the GitHub MCP server exposes a prompt named `summarise_pr`, it can be triggered with `/mcp.github.summarise_pr`.

### Example Workflow: GitHub MCP Server in Agent Mode

The following walkthrough illustrates end-to-end use of the GitHub MCP server in Agent Mode:

**Step 1.** Ensure the GitHub MCP server is configured in `.vscode/mcp.json` as shown in Section 2.

**Step 2.** In Copilot Chat, switch to Agent Mode and confirm the GitHub tools appear in the tool picker.

**Step 3.** Use a natural language prompt to trigger tool usage:

```text
// Ask Copilot to list open issues in the current repository
What are the open issues in this repository? Summarise each one in a single sentence
and flag any that appear to be blocking other work.
```

```text
// Ask Copilot to create a pull request after implementing a change
I've implemented the feature described in issue #42. Create a pull request on the
"feature/dark-mode" branch targeting "main", with a descriptive title and body that
references the issue.
```

**Step 4.** Review each tool call approval prompt before confirming. Check the arguments to ensure the action is correct.

**Step 5.** After Copilot completes the task, review the output and any generated artefacts (issues, PRs, comments) in GitHub.

Sources: [code.visualstudio.com/docs/copilot/chat/mcp-servers](https://code.visualstudio.com/docs/copilot/chat/mcp-servers), [docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp).

---

## Best Practices

| Practice | Why It Matters |
|----------|---------------|
| **Use workspace-scoped `.vscode/mcp.json` for shared server configurations** | Checking the file into version control ensures every team member uses the same MCP server setup without manual configuration steps. |
| **Store secrets in input variables, not as plain text** | Using `${input:variable-id}` causes VS Code to prompt once and store the value securely. Hard-coded tokens in `mcp.json` risk accidental exposure via version control. |
| **Review trust prompts carefully before accepting** | Local stdio MCP servers run arbitrary code on the developer's machine. The trust prompt is the moment to verify the server source and configuration before execution begins. |
| **Enable `chat.mcp.enabled` and verify tool visibility in Agent Mode** | Confirming that tools appear in the tool picker before starting a task prevents confusion later and ensures the model has the intended capabilities available. |
| **Start with read-only or low-privilege servers before broadening access** | Beginning with servers that can only read data (for example, the GitHub MCP server in read-only mode) limits risk while you build familiarity with how MCP tools behave in practice. |

---

## Key Takeaways

1. **MCP is an open protocol, not a GitHub or VS Code feature.** Any AI host and any server that implements the JSON-RPC 2.0 MCP specification can interoperate, regardless of vendor.
2. **Tools, resources, and prompts are the three server-side primitives.** Tools are invocable functions, resources are read-only context blobs, and prompts are reusable templates. Understanding the distinction shapes how you configure and use MCP servers.
3. **Configuration scope determines who benefits.** A workspace-scoped `.vscode/mcp.json` serves the whole team; a user-profile `mcp.json` is personal. Choose the right scope for the right audience.
4. **Agent Mode is the gateway to MCP tools in VS Code Copilot.** MCP tools are not available in Ask Mode or inline chat. Switch to Agent Mode and verify tool availability in the tool picker before relying on MCP-powered workflows.

---

## Classroom Discussion Questions

1. What kinds of external systems or data sources would most benefit your team if connected to GitHub Copilot via MCP? How would you decide whether to use an existing community server or build a custom one?
2. The trust prompt appears every time an MCP server configuration changes. How would you explain the importance of this checkpoint to a colleague who finds it inconvenient?
3. The research brief notes that MCP uses a USB-C analogy. In what ways does this analogy hold, and in what ways does it fall short when describing security and governance considerations?

---

## Next Steps

- **MCP in Production:** In the next session ['MCP in Production: GitHub, Copilot CLI, and Governance'](2-MCP-in-Production.md), you will explore the GitHub MCP server's toolset system, how to configure MCP for the Copilot coding agent and Copilot CLI, and how organisations govern MCP usage at scale.

---

## Additional Resources

- [MCP Introduction](https://modelcontextprotocol.io/introduction)
- [MCP Architecture and Primitives](https://modelcontextprotocol.io/docs/concepts/architecture)
- [VS Code MCP Servers Documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
- [VS Code MCP Configuration Reference](https://code.visualstudio.com/docs/copilot/reference/mcp-configuration)
- [GitHub Docs: Extend Copilot Chat with MCP](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
