# MCP in Production: GitHub, Copilot CLI, and Governance

## Session Overview

**Duration:** 45-60 minutes  
**Format:** Presentation with live demonstration  
**Objective:** Understand the GitHub MCP server's toolset system, configure MCP for the Copilot coding agent and Copilot CLI, and apply security and governance controls for MCP usage in a production or enterprise environment.

---

## Contents

- [1. The GitHub MCP Server](#1-the-github-mcp-server)
- [2. MCP for the Copilot Coding Agent and CLI](#2-mcp-for-the-copilot-coding-agent-and-cli)
- [3. Security, Governance, and Enterprise Controls](#3-security-governance-and-enterprise-controls)
- [Best Practices](#best-practices)
- [Key Takeaways](#key-takeaways)
- [Classroom Discussion Questions](#classroom-discussion-questions)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

---

## 1. The GitHub MCP Server

### Overview

The GitHub MCP Server (`github/github-mcp-server`) is an official GitHub-maintained MCP server written in Go. It exposes GitHub platform capabilities as MCP tools, including repositories, issues, pull requests, Actions workflows, code security findings, Dependabot alerts, discussions, and notifications.

The server is available in two deployment models:

| Deployment | URL or command | Authentication | Notes |
|-----------|---------------|---------------|-------|
| **Remote (recommended)** | `https://api.githubcopilot.com/mcp/` | OAuth via VS Code GitHub sign-in, or PAT in `Authorization: Bearer` header | Requires VS Code 1.101 or later for remote MCP and OAuth support |
| **Local (Docker)** | `docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server` | PAT via `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable | Also available as a compiled binary; communicates over stdio |

An Insiders variant of the remote server is available at `https://api.githubcopilot.com/mcp/insiders` or by passing the header `X-MCP-Insiders: true`.

Source: [github.com/github/github-mcp-server](https://github.com/github/github-mcp-server).

### Connecting the Remote GitHub MCP Server

To add the remote GitHub MCP server to VS Code, create or update `.vscode/mcp.json`:

```json
// .vscode/mcp.json - remote GitHub MCP server (no local installation required)
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

After saving the file, VS Code presents a trust prompt. Once accepted, the server starts and authenticates via the GitHub OAuth sign-in flow already active in VS Code. No token needs to be configured manually.

### Connecting the Local GitHub MCP Server

For environments where outbound network access is restricted, the local server runs in Docker:

```json
// .vscode/mcp.json - local GitHub MCP server via Docker (stdio transport)
{
  "servers": {
    "github-local": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        // Pass the PAT as an environment variable; never embed tokens as literal strings
        "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        // Reference the PAT from an input variable so VS Code stores it securely
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github-pat}"
      }
    }
  },
  "inputs": [
    {
      "id": "github-pat",
      "type": "promptString",
      "description": "GitHub Personal Access Token with required scopes",
      "password": true
    }
  ]
}
```

### Toolsets

The server groups tools into named **toolsets**. When no explicit configuration is provided, the default toolsets are enabled automatically:

| Toolset | Availability | Contents |
|---------|-------------|---------|
| `repos` | Default | Repository management tools |
| `issues` | Default | Issue creation, listing, and management |
| `pull_requests` | Default | PR creation, review, and merging |
| `actions` | Optional | GitHub Actions workflow management |
| `code_security` | Optional | Code scanning alerts, Dependabot findings |
| `secret_protection` | Optional | Secret scanning alerts |
| `notifications` | Optional | Notification management |
| `discussions` | Optional | GitHub Discussions management |
| `orgs` | Optional | Organisation management tools |
| `copilot` | Remote only | Copilot cloud agent tools (requires paid Copilot subscription) |
| `github_support_docs_search` | Remote only | Search GitHub Support documentation |

To enable specific toolsets, use the `--toolsets` command-line flag or the `GITHUB_TOOLSETS` environment variable. The keyword `all` enables every toolset; `default` enables the standard set.

```json
// .vscode/mcp.json - enabling additional toolsets for the local server
{
  "servers": {
    "github-local": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
        "-e", "GITHUB_TOOLSETS",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github-pat}",
        // Enable default toolsets plus Actions and code security scanning tools
        "GITHUB_TOOLSETS": "default,actions,code_security"
      }
    }
  }
}
```

Source: [docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/configure-toolsets](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/configure-toolsets).

### Read-Only Mode

Passing `--read-only` restricts the server to non-mutating tools only, preventing unintended writes. This is particularly useful in review or audit workflows where you want Copilot to read and summarise data without modifying repositories.

```json
// .vscode/mcp.json - read-only mode to prevent any write operations
{
  "servers": {
    "github-readonly": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
        // --read-only flag restricts the server to non-mutating tools only
        "ghcr.io/github/github-mcp-server", "--read-only"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github-pat}"
      }
    }
  }
}
```

### Dynamic Toolsets

Setting the environment variable `GITHUB_DYNAMIC_TOOLSETS=1` enables the server to expose a `get_available_toolsets` and `enable_toolset` meta-tool pair. This allows the AI to discover and activate toolsets at runtime, reducing the initial tool catalogue size and improving performance.

### Enterprise Server and GitHub Enterprise Cloud Support

- **GitHub Enterprise Server (GHES)**: Use the `--gh-host` flag or set `GITHUB_HOST=https://your-ghes-hostname` for the local server.
- **GitHub Enterprise Cloud with data residency (ghe.com)**: Use the remote server URL format `https://copilot-api.SUBDOMAIN.ghe.com/mcp`.

Source: [github.com/github/github-mcp-server](https://github.com/github/github-mcp-server).

---

## 2. MCP for the Copilot Coding Agent and CLI

### The Copilot Coding Agent and MCP

The Copilot coding agent is the cloud-side agent that runs tasks autonomously on GitHub.com. It has native MCP support with several important differences from IDE MCP:

| Aspect | IDE (VS Code) | Coding agent |
|--------|--------------|-------------|
| Primitives supported | Tools, resources, and prompts | Tools only |
| Per-call approval prompts | Yes (configurable) | No (autonomous) |
| OAuth for remote servers | Yes | No (use PAT or static credential) |
| Default servers | None (user-configured) | GitHub MCP (read-only token) and Playwright (localhost only) |
| Configuration location | `.vscode/mcp.json` | Repository Settings > Copilot > Cloud agent > MCP configuration |

Source: [docs.github.com/en/copilot/concepts/agents/cloud-agent/mcp-and-cloud-agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/mcp-and-cloud-agent).

### Configuring MCP for the Coding Agent

Repository administrators navigate to **Settings > Copilot > Cloud agent > MCP configuration** and enter a JSON block. Note that the format uses `mcpServers` (not `servers` as in the VS Code `mcp.json`):

```json
// Repository MCP configuration for the Copilot coding agent
// Navigate to: Settings > Copilot > Cloud agent > MCP configuration
{
  "mcpServers": {
    "sentry": {
      // Local server spawned by the coding agent runtime
      "type": "local",
      "command": "npx",
      "args": ["@sentry/mcp-server@latest", "--host=$SENTRY_HOST"],
      "env": {
        "SENTRY_HOST": "https://contoso.sentry.io",
        // Reference secrets using the $COPILOT_MCP_ prefix
        // Store these as Agents secrets with the name COPILOT_MCP_SENTRY_ACCESS_TOKEN
        "SENTRY_ACCESS_TOKEN": "$COPILOT_MCP_SENTRY_ACCESS_TOKEN"
      },
      // List specific tool names, or use ["*"] to allow all tools
      "tools": ["*"]
    },
    "azure": {
      "type": "local",
      "command": "npx",
      "args": ["@azure/mcp@latest", "server", "start"],
      "env": {
        "AZURE_SUBSCRIPTION_ID": "$COPILOT_MCP_AZURE_SUBSCRIPTION_ID"
      },
      "tools": ["resources_list", "storage_blobs_list"]
    }
  }
}
```

Key rules for coding agent MCP configuration:

- Use `"type": "local"` or `"type": "stdio"` for subprocess servers; `"type": "http"` or `"type": "sse"` for remote servers.
- Secrets must be stored as **Agents secrets** with names prefixed `COPILOT_MCP_` and referenced using `$COPILOT_MCP_*` substitution syntax.
- The `"tools"` array is an allowlist. Use `["*"]` to allow all tools, or list specific tool names for fine-grained control.
- Organisation and enterprise administrators can also configure MCP for custom agents via YAML frontmatter.

Source: [docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp](https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp).

### MCP in the Copilot CLI

The GitHub Copilot CLI (`gh copilot` or the standalone `copilot` binary) has native MCP support. The GitHub MCP server is built into the CLI and is available without any additional configuration. You can immediately ask Copilot questions about your GitHub repositories without setting up a server.

Additional MCP servers are persisted in `~/.copilot/mcp-config.json`:

```json
// ~/.copilot/mcp-config.json - additional MCP servers for the Copilot CLI
{
  "mcpServers": {
    "playwright": {
      // Local Playwright MCP server via npx
      "type": "local",
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {},
      // Allow all Playwright tools
      "tools": ["*"]
    },
    "context7": {
      // Remote context7 MCP server for library documentation
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": { "CONTEXT7_API_KEY": "YOUR-API-KEY" },
      "tools": ["*"]
    }
  }
}
```

### Slash Commands for CLI MCP Management

Within an interactive Copilot CLI session, the following `/mcp` slash commands manage MCP servers:

| Command | Purpose |
|---------|---------|
| `/mcp add` | Interactive form to add a new server (Tab to navigate fields) |
| `/mcp show` | List all configured servers and their current status |
| `/mcp show SERVER-NAME` | Show status and available tools for a specific server |
| `/mcp edit SERVER-NAME` | Edit a server's configuration |
| `/mcp delete SERVER-NAME` | Remove a server |
| `/mcp disable SERVER-NAME` | Disable a server for the current session |
| `/mcp enable SERVER-NAME` | Re-enable a disabled server |

When adding a server interactively, the **Server Type** field accepts: `Local` or `STDIO` (both launch a local subprocess), `HTTP` (Streamable HTTP, current standard), or `SSE` (legacy HTTP+SSE, deprecated).

The `tools` field in `mcp-config.json` acts as an allowlist. Set it to `["*"]` to allow all tools, or list specific tool names for fine-grained control.

Source: [docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers).

---

## 3. Security, Governance, and Enterprise Controls

### Security Model Overview

MCP introduces a trust boundary between the AI model and external systems. The following risks and mitigations apply across all MCP surfaces:

| Risk | Description | Mitigation |
|------|-------------|-----------|
| **Prompt injection** | Malicious content returned by a tool (for example, instructions hidden in web page text fetched by a fetch server) may attempt to redirect the AI's subsequent actions | Review tool outputs carefully; prefer read-only modes; limit the scope of tools the model can invoke |
| **Tool poisoning** | A server exposes a tool with a misleading name or description that tricks the model into calling it unexpectedly | Use servers from verified publishers in the GitHub MCP Registry; review tool catalogues before enabling |
| **Supply chain risks** | A community-published npm or Docker image that provides an MCP server may be updated to include malicious behaviour | Pin server versions (`@specific-version` not `@latest`); prefer servers with verified publishers |
| **Token passthrough** | An MCP server accepts tokens that were not issued to it, or forwards them to downstream APIs | The MCP specification forbids token passthrough; only use servers that comply with this requirement |
| **Confused deputy** | A malicious server tricks the host into making requests on behalf of the user with excessive permissions | Use minimum-scope credentials; prefer the `--read-only` flag where available |
| **DNS rebinding** | A locally running HTTP server may be targeted by DNS rebinding attacks via a malicious web page | Servers must validate the `Origin` header; local servers should bind only to `127.0.0.1` |

Sources: [modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices), [learn.microsoft.com/azure/app-service/tutorial-ai-model-context-protocol-server-python#security-best-practices](https://learn.microsoft.com/azure/app-service/tutorial-ai-model-context-protocol-server-python#security-best-practices).

### Trust-on-First-Use

VS Code implements a trust-on-first-use pattern for MCP servers:

1. The first time a server is started (or its configuration changes), VS Code presents a trust dialogue showing the server's command, arguments, and environment variables.
2. If the user accepts, VS Code stores the trust decision and starts the server automatically on future workspace opens.
3. If the user declines, the server is not started.
4. The command **MCP: Reset Trust** clears all stored trust decisions, forcing re-evaluation of every configured server.

### Audit and Logging

VS Code records all MCP tool calls in the output log. To access the log:

1. Open the Command Palette and run **MCP: List Servers**.
2. Select a server and choose **Show Output**.

Regular review of the log helps detect unexpected tool invocations and supports incident investigation. The coding agent's default read-only GitHub MCP token limits the surface area available to the agent.

### Push Protection

For public repositories and private repositories covered by GitHub Advanced Security, the GitHub MCP server enforces push protection. This blocks secrets from appearing in AI-generated responses, preventing accidental credential exposure through MCP tool outputs.

### Organisation-Level Policy Controls

#### GitHub Organisation Policy

The **MCP servers in Copilot** toggle in **Settings > Copilot > Policies** (disabled by default) must be explicitly enabled before members can use MCP with Copilot Business or Copilot Enterprise subscriptions. This policy does not apply to Copilot Free, Pro, or Pro+ plans.

Source: [docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp).

#### VS Code Enterprise Policies

Organisations can deploy VS Code policies via device management tools (for example, Intune or Group Policy). The relevant policies are:

| Policy | Values | Effect |
|--------|--------|--------|
| `ChatMCP` | `all`, `registry`, `none` | `all` allows any MCP source; `registry` allows only approved registry servers; `none` disables MCP entirely. Configures the `chat.mcp.access` setting. |
| `McpGalleryServiceUrl` | URL string | Points VS Code to a private internal MCP registry instead of the public GitHub MCP Registry. |
| `ChatToolsAutoApprove` | `true` / `false` | Set to `false` to prevent users from enabling global auto-approval of tool calls. |
| `ChatToolsEligibleForAutoApproval` | Array of tool names | Allowlist of tools that may be auto-approved even when `ChatToolsAutoApprove` is restricted. |
| `ChatAgentMode` | `true` / `false` | Set to `false` to disable Agent Mode entirely, preventing any MCP tool access from chat. |
| `ChatApprovedAccountOrganizations` | Array of org names | Restricts AI features to accounts belonging to approved GitHub organisations. |

Source: [code.visualstudio.com/docs/enterprise/ai-settings](https://code.visualstudio.com/docs/enterprise/ai-settings).

#### Private MCP Registry

Organisations can host a curated allowlist of approved MCP servers in a private registry and point VS Code to it using the `McpGalleryServiceUrl` policy. This prevents developers from adding arbitrary community servers while still giving them access to vetted tools.

### Summary of Security Best Practices

1. **Review trust prompts carefully.** Local stdio MCP servers run arbitrary code on the developer's machine. The trust dialogue is the checkpoint to verify the server source before execution begins.
2. **Use minimum-scope credentials.** PATs should grant only the permissions required for the tools in use. OAuth flows for the remote GitHub MCP server limit access to the scopes approved during sign-in.
3. **Store secrets in input variables or Agents secrets.** Never embed token values as literal strings in `mcp.json` or the coding agent configuration JSON.
4. **Use the `tools` allowlist.** Explicitly list required tools rather than using `["*"]`, especially in contexts where there are no per-call approval prompts (coding agent).
5. **Enable sandboxing for local servers where supported.** VS Code sandboxing (macOS and Linux) restricts a server's file system and network access.
6. **Pin server versions in production.** Avoid using `@latest` for critical servers; pin to a specific version and review changes before upgrading.
7. **Monitor the MCP output log.** Regular log review detects unexpected tool invocations and supports incident investigation.

---

## Best Practices

| Practice | Why It Matters |
|----------|---------------|
| **Use the remote GitHub MCP server for most users** | The remote server requires no local installation, Docker, or PAT management. OAuth via VS Code's GitHub sign-in is secure and low-friction for individuals and teams. |
| **Restrict the coding agent to a minimum `tools` allowlist** | The coding agent invokes tools autonomously without per-call approval. Explicitly listing only the tools required for each workflow limits the blast radius if the agent makes an unexpected decision. |
| **Enable the GitHub organisation MCP policy before team rollout** | The policy is disabled by default for Copilot Business and Enterprise. Enabling it at the organisation level ensures all members can use MCP; forgetting to enable it is the most common reason MCP tools do not appear for team members. |
| **Use `ChatMCP: registry` for enterprise environments** | Pointing VS Code to a private registry ensures developers only use pre-approved servers, reducing supply chain and compliance risk without blocking all MCP usage. |
| **Audit MCP tool calls regularly** | The VS Code MCP output log and the coding agent's activity log provide an audit trail for all tool invocations. Regular review helps detect misuse or unexpected behaviour before it causes harm. |

---

## Key Takeaways

1. **The GitHub MCP server has two deployment models.** The remote server (`https://api.githubcopilot.com/mcp/`) is zero-configuration for VS Code users; the local Docker server is required for air-gapped or network-restricted environments.
2. **The coding agent and the IDE use different configuration formats and have different constraints.** The coding agent uses `mcpServers` (not `servers`), supports tools only, and requires `COPILOT_MCP_`-prefixed secrets. Mixing up these formats is a common source of configuration errors.
3. **Security requires layered controls.** Trust prompts, minimum-scope credentials, tool allowlists, sandboxing, and organisation policies each address different threat vectors. No single control is sufficient on its own.
4. **Governance starts with enabling the policy.** Copilot Business and Enterprise organisations must explicitly enable the MCP policy in GitHub organisation settings before their members can use MCP. VS Code enterprise policies (`ChatMCP`, `McpGalleryServiceUrl`) then provide finer-grained control over which servers are permitted.

---

## Classroom Discussion Questions

1. Your organisation runs GitHub Enterprise Server and has strict network controls. Which deployment model of the GitHub MCP server would you choose, and what additional security measures would you apply to the configuration?
2. The coding agent does not show approval prompts before invoking MCP tools. How does this affect your decision about which tools to include in the `tools` allowlist for a production repository?
3. A developer on your team suggests using the `ChatMCP: all` policy to allow maximum flexibility. What counterarguments would you make, and what policy configuration would you recommend instead?

---

## Next Steps

- **Hands-On Lab:** In the next session [Week 3 - Integrate MCP with GitHub Copilot Hands-On Lab](3-Week3-Lab.md), you will apply the concepts from both sessions by working through the GitHub Skills exercise: setting up the GitHub MCP server in a Codespace, using Agent Mode to research and create issues, and delegating an end-to-end feature implementation to Copilot.

---

## Additional Resources

- [GitHub MCP Server Repository](https://github.com/github/github-mcp-server)
- [GitHub Docs: About MCP](https://docs.github.com/en/copilot/concepts/about-mcp)
- [GitHub Docs: Set Up the GitHub MCP Server](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server)
- [GitHub Docs: Configure Toolsets](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/configure-toolsets)
- [GitHub Docs: Extend the Coding Agent with MCP](https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp)
- [GitHub Docs: Add MCP Servers to Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers)
- [VS Code Enterprise AI Settings](https://code.visualstudio.com/docs/enterprise/ai-settings)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
