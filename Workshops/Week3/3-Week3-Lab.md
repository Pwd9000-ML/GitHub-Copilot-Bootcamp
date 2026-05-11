# Week 3 - Integrate MCP with GitHub Copilot Hands-On Lab

Please follow the instructions below to complete the hands-on lab for Week 3.

_Connect the GitHub MCP server to Copilot Agent Mode and use it to research, plan, and implement a feature end-to-end in under two hours._

- **Who is this for**: Developers and GitHub Copilot users who have completed Weeks 1 and 2 and want hands-on experience connecting Copilot to external tools via MCP.
- **What you'll learn**: How to configure the GitHub MCP server in a Codespace, use Copilot Agent Mode to invoke MCP tools for research and issue creation, and delegate a complete feature implementation (branch, code changes, pull request) to Copilot.
- **What you'll build**: You will guide Copilot to update the Mergington High School extracurricular activities website using the GitHub MCP server tools, resulting in a merged pull request and a closed issue with a Copilot-generated closing comment.
- **Prerequisites**:
  - Skills exercise: [Integrate MCP with Copilot](https://github.com/skills/integrate-mcp-with-copilot)
  - Familiarity with [VS Code](https://code.visualstudio.com/)
  - A GitHub account with an active GitHub Copilot subscription (Free, Pro, or higher)
  - Completion of the Week 3 sessions: `Workshops/Week3/1-MCP-Foundations.md` and `Workshops/Week3/2-MCP-in-Production.md`
- **How long**: This exercise takes approximately 60-90 minutes to complete.

In this exercise, you will:

1. Open the exercise repository in a GitHub Codespace, create `.vscode/mcp.json` pointing at the remote GitHub MCP server, authenticate via OAuth, and verify the GitHub tools appear in Copilot's Agent Mode tool picker.
1. Switch to Agent Mode and use natural language prompts to invoke GitHub MCP tools: search for similar public repositories, compare their features with your project, and ask Copilot to create enhancement issues directly in the repository.
1. Use Agent Mode to query the open issues, ask Copilot to select and implement the most important one end-to-end (checkout a branch, make code changes, push, and open a pull request), then review, merge the pull request, and have Copilot post a closing comment on the resolved issue.

### How to start this exercise

Simply copy the exercise to your account, then give your favourite Octocat (Mona) **about 20 seconds** to prepare the first lesson, then **refresh the page**.

[![](https://img.shields.io/badge/Copy%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/new?template_owner=skills&template_name=integrate-mcp-with-copilot&owner=%40me&name=skills-integrate-mcp-with-copilot&description=Exercise:+Integrate+MCP+with+GitHub+Copilot&visibility=public)

<details>
<summary>Having trouble?</summary><br/>

When copying the exercise, we recommend the following settings:

- For owner, choose your personal account or an organisation to host the repository.

- We recommend creating a public repository, since private repositories will use Actions minutes.

If the exercise isn't ready in 20 seconds, please check the [Actions](../../actions) tab.

- Check to see if a job is running. Sometimes it simply takes a bit longer.

- If the page shows a failed job, please submit an issue. You found a bug!

</details>

---

## Lab Walkthrough

The exercise has four steps, each tracked automatically by GitHub Actions workflows. Below is a summary of what you will do in each step.

### Step 1: Introduction to MCP and Environment Setup (~10 minutes)

Open the exercise repository in a GitHub Codespace. Verify that the GitHub Copilot Chat and Python extensions are installed and that the sample application runs correctly.

Create `.vscode/mcp.json` with the following content:

```json
// .vscode/mcp.json - connect to the remote GitHub MCP server
{
  "servers": {
    "github": {
      // Streamable HTTP transport; requires VS Code 1.101 or later
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

Click the **Start** code lens in the file, complete the OAuth authentication prompt, and verify the server appears as running. Open the tools icon in the Copilot panel and confirm GitHub tools are visible.

Commit and push `.vscode/mcp.json` to the `main` branch. This push triggers the automated step-checking workflow, which advances the exercise to Step 2.

### Step 2: Agent Mode and an MCP Server for GitHub (~15 minutes)

Switch to Copilot Agent Mode in the Chat view. Use the following prompts to explore MCP tool calling:

```text
// Search GitHub for public repositories similar to the Mergington High School project
Search GitHub for Python web applications that manage school extracurricular activities.
List the top five results, including star count and a brief description.
```

```text
// Ask Copilot to compare a similar project with the current repository
Compare the features of the repository you found with the highest star count
against the features in this project. What is our project missing?
```

```text
// Instruct Copilot to create enhancement issues based on the comparison
Based on the feature gaps you identified, create three enhancement issues in this
repository. Each issue should have a clear title, a concise description of the
requested feature, and an acceptance criteria section.
```

Review each tool call approval prompt before confirming. After Copilot has created the issues, start a new chat (to clear context) before moving to Step 3.

### Step 3: Solve Issues with Agent Mode and the GitHub MCP Server (~15 minutes)

Use Agent Mode to query and prioritise the open issues:

```text
// Query and prioritise the open issues
List all open issues in this repository. Rank them from most to least impactful
for end users, and explain your ranking in one sentence per issue.
```

Ask Copilot to implement the highest-priority issue end-to-end:

```text
// Delegate full implementation of the top-priority issue to Copilot
Implement the top-priority issue you identified. Check out a new branch named
"feature/<issue-slug>", make the necessary code changes, push the branch, and
open a pull request targeting "main". Include the issue number in the PR description.
```

Use the **Bypass Approvals** option in the permissions picker for frequently called tools such as file reads and branch operations, to avoid approving every individual call. Always verify arguments before approving destructive actions such as file writes or branch pushes.

### Step 4: Validating AI-Generated Code (~10 minutes)

Open the pull request that Copilot created and review the changes carefully. Use Copilot Code Review if your subscription supports it.

Merge the pull request after you are satisfied with the changes. Return to the active Copilot Chat session and post a closing comment on the resolved issue:

```text
// Ask Copilot to post a closing comment on the resolved issue
The pull request for issue #<number> has been merged. Post a closing comment on
the issue thanking any contributors and noting that the feature has been shipped.
```

Mona (the automated teaching bot) verifies each completed step via GitHub Actions and advances the exercise to the final review stage.

---

Attribution: This lab is based on the GitHub Skills template **Integrate MCP with Copilot**.
Upstream source: https://github.com/skills/integrate-mcp-with-copilot

---

## Next Steps

- **Week 3 Prompt Examples:** After completing this hands-on lab, take a look at [Week 3 Prompt Examples](4-Week3-Prompts.md) to see how to craft effective prompts for MCP-powered GitHub Copilot workflows.
