# GitHub Copilot: Setup, Configuration, and Interaction Modes

**Duration:** 45-60 minutes (live demo) + self-study reference  
**Format:** LIVE Demo/Recording  
**Objective:** Get GitHub Copilot installed, configured, and ready to use in your preferred development environment.

> **Note:** The live session focuses on **Visual Studio Code** as the primary demo environment. The remaining IDE sections (Visual Studio, JetBrains, Xcode, Neovim/Vim, Eclipse) are provided as **self-study reference material** for participants using other editors. Refer to the [IDE Support Guide](../../FAQ/IDE-support.md) for a feature comparison across all supported IDEs.

---

## Contents

- [Part 1: Getting GitHub Copilot Access](#part-1-getting-github-copilot-access)
- [Part 2: IDE-Specific Setup](#part-2-ide-specific-setup)
  - [Visual Studio Code](#visual-studio-code-recommended)
  - [Visual Studio (Full IDE)](#visual-studio-full-ide)
  - [JetBrains IDEs](#jetbrains-ides-intellij-idea-pycharm-webstorm-etc)
  - [Xcode (macOS)](#xcode-macos)
  - [Neovim / Vim](#neovim--vim)
  - [Eclipse](#eclipse)
- [Part 3: Configuration and Customisation](#part-3-configuration-and-customisation)
- [Part 4: Basic Commands and Workflows](#part-4-basic-commands-and-workflows)
- [Part 5: GitHub Copilot Interaction Modes](#part-5-github-copilot-interaction-modes)
- [Part 6: Troubleshooting](#part-6-troubleshooting)
- [Part 7: Best Practices for Setup](#part-7-best-practices-for-setup)

---

## Prerequisites

- Active GitHub account
- GitHub Copilot access through Copilot Free, a paid individual plan, or a managed Business/Enterprise organisation
- IDE installed on your machine

> **April 2026 note:** Copilot Free can be enough for introductory exercises, but request limits, model access, feature availability, billing, and sign-up availability can vary by plan and organisation policy, and may change over time. Always verify current access and plan details on the official [GitHub Copilot plans page](https://github.com/features/copilot/plans) before delivering a live workshop.

---

## Part 1: Getting GitHub Copilot Access

### Step 1: Verify Your Subscription

1. Visit [https://github.com/](https://github.com/)  
   **Note:** If you're part of an enterprise organisation, your GitHub URL may differ. Check with your GitHub representative or Champion for details.
2. Check your subscription status under **Settings → Billing and Plans**
3. Ensure your plan includes GitHub Copilot access
4. If your organisation manages Copilot, confirm which IDEs, models, agents, MCP servers, and preview features are enabled by policy

### Step 2: Install the GitHub Copilot Extension

The installation process varies by IDE. Follow the relevant section below for your development environment.

---

## Part 2: IDE-Specific Setup

### Visual Studio Code (Recommended)

#### Installation

1. **Open VS Code**
2. **Open the Copilot menu** from the title bar, status bar, or Accounts menu
3. **Sign in or get Copilot access** when prompted. VS Code can guide new users through Copilot Free if they do not already have access
4. **Install or update the official GitHub Copilot extension** if VS Code prompts you to do so
5. **Reload VS Code** if prompted so the chat, inline suggestions, and agent tools are available

#### Sign In

1. Click **Sign in with GitHub** from the Copilot menu or Accounts menu
2. Authorise VS Code in your browser
3. Return to VS Code and confirm the Copilot status indicator is active
4. Open Copilot Chat and run `/init` in your project to create or refresh repository instructions when appropriate

#### Basic Commands

**Keyboard Shortcuts for macOS**

| Action | Shortcut | Command Name |
|--------|----------|--------------|
| Accept an inline suggestion | `Tab` | `editor.action.inlineSuggest.commit` |
| Dismiss an inline suggestion | `Esc` | `editor.action.inlineSuggest.hide` |
| Show next inline suggestion | `Option (⌥)+]` | `editor.action.inlineSuggest.showNext` |
| Show previous inline suggestion | `Option (⌥)+[` | `editor.action.inlineSuggest.showPrevious` |
| Trigger inline suggestion | `Option (⌥)+\` | `editor.action.inlineSuggest.trigger` |
| Open GitHub Copilot (additional suggestions in separate pane) | `Ctrl+Return` | `github.copilot.generate` |
| Toggle GitHub Copilot on/off | No default shortcut | `github.copilot.toggleCopilot` |

**Keyboard Shortcuts for Windows**

| Action | Shortcut | Command Name |
|--------|----------|--------------|
| Accept an inline suggestion | `Tab` | `editor.action.inlineSuggest.commit` |
| Dismiss an inline suggestion | `Esc` | `editor.action.inlineSuggest.hide` |
| Show next inline suggestion | `Alt+]` | `editor.action.inlineSuggest.showNext` |
| Show previous inline suggestion | `Alt+[` | `editor.action.inlineSuggest.showPrevious` |
| Trigger inline suggestion | `Alt+\` | `editor.action.inlineSuggest.trigger` |
| Open GitHub Copilot (additional suggestions in separate pane) | `Ctrl+Enter` | `github.copilot.generate` |
| Toggle GitHub Copilot on/off | No default shortcut | `github.copilot.toggleCopilot` |

**Keyboard Shortcuts for Linux**

| Action | Shortcut | Command Name |
|--------|----------|--------------|
| Accept an inline suggestion | `Tab` | `editor.action.inlineSuggest.commit` |
| Dismiss an inline suggestion | `Esc` | `editor.action.inlineSuggest.hide` |
| Show next inline suggestion | `Alt+]` | `editor.action.inlineSuggest.showNext` |
| Show previous inline suggestion | `Alt+[` | `editor.action.inlineSuggest.showPrevious` |
| Trigger inline suggestion | `Alt+\` | `editor.action.inlineSuggest.trigger` |
| Open GitHub Copilot (additional suggestions in separate pane) | `Ctrl+Enter` | `github.copilot.generate` |
| Toggle GitHub Copilot on/off | No default shortcut | `github.copilot.toggleCopilot` |

> **Note:** Keyboard shortcuts may vary depending on your VS Code version and any customisations you've made. To verify the current shortcuts in your installation:
> 1. Press `Ctrl+K Ctrl+S` (Windows/Linux) or `Cmd+K Cmd+S` (Mac) to open the Keyboard Shortcuts editor
> 2. Search for "Copilot" to see all GitHub Copilot commands and their assigned shortcuts
> 3. Official documentation: [Keyboard shortcuts for GitHub Copilot in the IDE](https://docs.github.com/en/copilot/reference/keyboard-shortcuts-for-github-copilot-in-the-ide)

---

### Visual Studio (Full IDE)

#### Installation

**Option 1: Via Visual Studio Installer (Recommended)**
1. **Open Visual Studio Installer**
2. **Click "Modify"** on your Visual Studio installation
3. **Go to Individual Components** tab
4. **Search for "GitHub Copilot"**
5. **Check the box** and click **Modify**
6. **Restart Visual Studio**

**Option 2: Via Extensions Menu**
1. **Open Visual Studio**
2. **Go to Extensions → Manage Extensions**
3. **Search for "GitHub Copilot"**
4. **Download and install** the extension
5. **Restart Visual Studio**

#### Sign In

1. After installation, a prompt will appear to sign in
2. Click **Add an Account** and select **GitHub**
3. Complete authentication in your browser
4. Return to Visual Studio

#### Basic Commands

| Action | Shortcut | Command name |
|--------|----------|--------------|
| Show next inline suggestion | Alt+. | Edit.NextSuggestion |
| Show previous inline suggestion | Alt+, | Edit.PreviousSuggestion |

> **Note:** Keyboard shortcuts may vary by Visual Studio version. To verify shortcuts:
> 1. Go to **Tools → Options → Environment → Keyboard**
> 2. Search for "Copilot" to see all available commands
> 3. Official documentation: [GitHub Copilot in Visual Studio](https://docs.github.com/en/copilot/reference/keyboard-shortcuts?tool=visualstudio)

#### Known Limitations

- **Feature availability varies by version/policy:** Check which Copilot features are available for your Visual Studio version and plan
- **Admin opt-in for preview features:** Copilot Business/Enterprise users require administrator approval to access preview features like latest/preview AI models

> See [GitHub Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, etc.)

#### Installation

1. **Open your JetBrains IDE**
2. **Go to Settings → Plugins** (or **JetBrains IDE → Preferences → Plugins** on Mac)
3. **Search for "GitHub Copilot"**
4. **Click Install** on the official JetBrains plugin
5. **Restart the IDE**

#### Sign In

1. Accept the license agreement when prompted
2. Click **Sign in with GitHub**
3. Authorise in your browser
4. Return to your IDE

#### Basic Commands

| Action | Keyboard Shortcut |
|--------|------------------|
| **Accept an inline suggestion** | `Tab` |
| **Dismiss an inline suggestion** | `Esc` |
| **Show next inline suggestion** | `Alt+]` (Windows/Linux) or `Option (⌥)+]` (Mac) |
| **Show previous inline suggestion** | `Alt+[` (Windows/Linux) or `Option (⌥)+[` (Mac) |
| **Trigger inline suggestion** | `Alt+\` (Windows/Linux) or `Option (⌥)+\` (Mac) |
| **Open GitHub Copilot (additional suggestions in separate pane)** | `Alt+Enter` (Windows/Linux) or `Option (⌥)+Return` (Mac) |

> **Note:** Keyboard shortcuts may vary by JetBrains IDE version. To verify shortcuts:
> 1. Go to **Settings → Keymap** and search for "Copilot"
> 2. Official documentation: [GitHub Copilot Keyboard Shortcuts for JetBrains](https://docs.github.com/en/copilot/reference/keyboard-shortcuts?tool=jetbrains)

#### Known Limitations

- **No .NET Upgrade Agent:** Automated .NET version migration assistance not available
- **No Checkpoints support:** Cannot create or restore checkpoints during agent sessions
- **Custom agents and reusable prompt files:** Availability and behaviour can differ from VS Code. Check the feature matrix before teaching these workflows in JetBrains
- **No Workspace indexing:** Local codebase indexing for improved context is not available
- **No Java Upgrade Agent:** Automated Java version migration assistance not supported
- **Next edit suggestions:** Availability varies by IDE/version (check the feature matrix)

> See [GitHub Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

### Xcode (macOS)

#### Prerequisites

- Supported Xcode/macOS versions vary (see Copilot for Xcode documentation)

#### Installation

1. **Download the extension** from the [GitHub Copilot for Xcode repository](https://github.com/github/CopilotForXcode/releases/latest)
2. **Install the .dmg file** - a background item will be added to start the extension when Xcode launches
3. **Open the GitHub Copilot for Xcode application** from the Applications folder
4. **Follow the on-screen instructions** for setting up the extension

#### Granting Required Permissions

1. **Accessibility permission** - you will be prompted when you first start the extension
2. **Xcode Source Editor Extension permission** (manual setup required):
   - Open the **GitHub Copilot for Xcode** application
   - Click **Extension Permission**
   - Enable **GitHub Copilot** and click **Done**
3. **Restart Xcode**. You will see a new "GitHub Copilot" item in the **Editor** menu

#### Sign In

1. Open the **GitHub Copilot for Xcode** application
2. Click **Login to GitHub** and follow the prompts to authorise

#### Basic Commands

| Action | Keyboard Shortcut |
|--------|------------------|
| Accept the first line of a suggestion | `Tab` |
| View full suggestion | Hold `Option` |
| Accept full suggestion | `Option + Tab` |

> **Note:** Official documentation: [GitHub Copilot for Xcode](https://docs.github.com/en/copilot/reference/keyboard-shortcuts?tool=xcode)

#### Known Limitations

- **No VS Code Edit mode:** The older VS Code Edit mode workflow is not available in Xcode. If agent mode is available in your IDE/version, Copilot may still be able to work across multiple files. Use the feature matrix as the source of truth.
- **Extensions:** Not supported
- **MCP:** Supported (see feature matrix; availability may vary by version/policy)
- **No Code referencing:** Cannot view public code matches for suggestions
- **No Workspace indexing:** Local codebase indexing for improved context is not available
- **No .NET or Java Upgrade Agents:** Automated migration assistance not supported
- **macOS permission requirements:** Requires Accessibility and Files & Folders permissions; missing permissions can cause communication issues or block real-time suggestions
- **External app architecture:** Runs as a separate application communicating with Xcode, which can occasionally cause synchronisation issues

> See [GitHub Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

### Neovim / Vim

#### Prerequisites

- Vim version 9.0.0185 or newer / Neovim version 0.6 or above
- Node.js version 18 or above

#### Installation (Using Built-in Plugin Manager - Recommended)

**For Neovim on macOS/Linux:**
```bash
git clone https://github.com/github/copilot.vim \
  ~/.config/nvim/pack/github/start/copilot.vim
```

**For Neovim on Windows (PowerShell):**
```powershell
git clone https://github.com/github/copilot.vim.git `
  $HOME/AppData/Local/nvim/pack/github/start/copilot.vim
```

**For Vim on macOS/Linux:**
```bash
git clone https://github.com/github/copilot.vim \
  ~/.vim/pack/github/start/copilot.vim
```

**For Vim on Windows (PowerShell):**
```powershell
git clone https://github.com/github/copilot.vim.git `
  $HOME/vimfiles/pack/github/start/copilot.vim
```

**Alternative:** You can also use a plugin manager like **vim-plug** or **lazy.nvim**:
```vim
Plug 'github/copilot.vim'
```

#### Sign In

1. Start Vim/Neovim
2. Run `:Copilot setup`
3. Follow the authentication flow in your browser
4. Run `:Copilot enable` to enable the extension

#### Basic Usage

Suggestions are displayed inline and can be accepted by pressing `Tab`. For detailed keybindings and customization options, run `:help copilot` within Vim/Neovim.

> **Note:** Keyboard shortcuts can be rebound to your preferences. See the [Neovim Map documentation](https://neovim.io/doc/user/map.html) and the [copilot.vim repository](https://github.com/github/copilot.vim) for more information.

#### Known Limitations

The Copilot Neovim/Vim plugin focuses on inline code suggestions. Compared to richer IDE integrations, note these key limitations:

- **Code completion only:** Only inline code suggestions are supported
- **No Copilot Chat or Agent mode:** No interactive chat or autonomous task execution
- **No VS Code Edit or Agent mode:** Multi-file editing and autonomous task execution capabilities are not available
- **No Extensions or MCP support:** Cannot use third-party integrations
- **No Code referencing:** Cannot view public code matches for suggestions
- **No Custom instructions or Prompt files:** Cannot customise Copilot behaviour
- **No Workspace indexing:** Local codebase indexing is not available
- **No Copilot code review:** Automated code review features are not supported

> **Source:** [GitHub Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

### Eclipse

Eclipse is a popular IDE for Java development and is also used for SAP ABAP development via ABAP Development Tools (ADT). This section covers how to set up GitHub Copilot in Eclipse.

> **Note:** For ABAP-specific language support, limitations, and best practices, see the [Language Support Guide](../../FAQ/language-support.md#abap).

#### Prerequisites

| Requirement | Version/Details |
|-------------|-----------------|
| **Eclipse** | 2024-03 or above (2025-12 recommended) |
| **Java Runtime** | JRE 21 (64-Bit, LTS) |
| **Operating System** | Windows 10+ or macOS 10.15+ |

> **Note:** GitHub Copilot for Eclipse has minimum version requirements and feature availability can vary by Eclipse/Copilot plugin version and policy settings. Validate compatibility using the [Copilot feature matrix (Eclipse)](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=eclipse) and the Eclipse Marketplace listing.

#### Step 1: Install Eclipse

1. Download **Eclipse IDE for Java Developers** (version 2025-12 recommended) from [eclipse.org/downloads](https://www.eclipse.org/downloads/)
2. Extract and install Eclipse
3. Launch Eclipse and select your workspace location

#### Step 2: Install GitHub Copilot Extension

1. Go to **Help → Eclipse Marketplace** (or **Help → Install New Software**)
2. Search for **"GitHub Copilot"**
3. Click **Install** and follow the prompts
4. **Restart Eclipse** after installation

> **Official Reference:** [GitHub Copilot Extension for Eclipse](https://marketplace.eclipse.org/content/github-copilot)

#### Step 3: Sign In to GitHub Copilot

1. Locate the **Copilot icon** in the bottom-right corner of Eclipse
2. Click the icon and select **"Sign In to GitHub"**
3. Click **"Copy Code and Open"** to copy your device code
4. Paste the code in your browser and authorise the GitHub Copilot Plugin
5. Return to Eclipse and click **OK** to complete setup

#### Basic Commands in Eclipse

| Action | Method |
|--------|--------|
| **Trigger Suggestions** | Start typing, suggestions appear inline |
| **Accept Suggestion** | `Tab` |
| **Dismiss Suggestion** | `Esc` |
| **Open Copilot Chat** | Click Copilot icon in toolbar |

#### Known Limitations

- **No Checkpoints support:** Cannot create or restore checkpoints during agent sessions
- **No Copilot code review:** Automated code review features not supported
- **No VS Code Edit mode:** The older VS Code Edit mode workflow is not available in Eclipse. If agent mode is available in your IDE/version, Copilot may still be able to work across multiple files. Use the feature matrix as the source of truth.
- **Extensions:** Not supported
- **MCP:** Supported (see feature matrix; availability may vary by version/policy)
- **No Prompt files:** Prompt files are not supported in Eclipse (see feature matrix). Note that `.github/copilot-instructions.md` is a repository custom instructions file (a different feature), and its support can vary by environment.
- **Custom instructions in preview:** Repository and file-level custom instructions have limited support
- **Installation dependency conflicts:** May encounter conflicts with Mylyn WikiText UI and LSP4e components

> See [GitHub Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

## Part 3: Configuration and Customisation

### Enable/Disable Copilot Globally or Per File

#### VS Code

1. **Enable/Disable Completions:** Click the arrow next to the Copilot icon in the title bar → **Configure Inline Suggestions** → Select **Enable Completions** or **Disable Completions**
2. **Via Settings:** Go to **File → Preferences → Settings**, navigate to **Extensions → Copilot**, then check/uncheck **Inline Suggest: Enable**
3. **Disable for specific languages:** In Settings, under "Enable or disable Copilot for specified languages," click **Edit in settings.json** and configure:
   ```json
   "github.copilot.enable": {
       "*": true,
       "yaml": false,
       "plaintext": false
   }
   ```
4. **Trigger inline suggestion:** Press `Alt+\` (Windows/Linux) or `Option+\` (Mac)

#### Visual Studio

1. **Click the GitHub Copilot icon** in the bottom panel (status bar) of the Visual Studio window
2. When disabling, you'll be prompted to choose:
   - **Disable Globally** - turns off Copilot for all files
   - **Disable for [Language]** - turns off Copilot only for the current file's language
3. The icon shows a diagonal line through it when disabled

### Set Your Preferred Model

If your subscription provides multiple model options:

**VS Code:**
1. Open **Copilot Chat** (for example: open the chat view from the Copilot icon, or use **Quick chat** `Ctrl+Shift+Alt+L`)
2. Use the **model picker** in the chat input field (if available for your plan/policy)
3. Select from available models (varies by subscription, see [Supported AI models](https://docs.github.com/en/copilot/using-github-copilot/ai-models/supported-ai-models-in-copilot))

> **Note:** Different models have different request costs, capabilities, and policy controls. Avoid hardcoding model lists in curriculum material because GitHub adds, removes, and changes model availability frequently. Copilot Business and Enterprise users may need their organisation to enable model switching.

---

## Part 4: Basic Commands and Workflows

### Getting Started: Your First Copilot Chat

**Scenario:** Understanding a function in an existing file

1. **Open a code file** and select a function you want to understand
2. **Open Copilot Chat** (for example: open the chat view from the Copilot icon, or use **Quick chat** `Ctrl+Shift+Alt+L` in VS Code)
3. **Type:** `"Explain what this function does"`
4. **Press Enter**
5. Copilot provides an explanation
6. **Ask follow-up questions** if needed

### Triggering Inline Suggestions

**Scenario:** Writing a new function

1. **Start typing a comment** describing what you want:
   ```python
   # Function to validate email addresses
   def validate_email(
   ```
2. **Wait for Copilot to suggest** the implementation
3. **Press Tab** to accept or keep typing to modify

### Using Copilot Chat with Code Context

**Scenario:** Debugging an error

1. **Highlight the problematic code**
2. **Open Copilot Chat** and paste the error message
3. **Type:** `"Why am I getting this error?"`
4. Copilot analyses your code and error to provide solutions

---

## Part 5: GitHub Copilot Interaction Modes

GitHub Copilot offers several interaction surfaces designed for different stages of the development lifecycle: **Ask**, **inline suggestions**, **inline chat and targeted edits**, **Plan**, **Agent**, **Copilot CLI**, and **Copilot cloud agent**. Understanding when to use each one helps you keep Copilot productive, reviewable, and aligned with organisation policy.

> **April 2026 note:** Older materials may refer to VS Code Edit mode as a standalone mode. Current VS Code workflows emphasise Agent mode for multi-file changes, inline chat for focused edits, and Plan for review-before-implementation workflows. Always use the [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) as the source of truth for your specific IDE/version.

### Quick Comparison

| Surface or mode | Best For | Key Capability | Example Use Case |
|-----------------|----------|----------------|------------------|
| **Inline Suggestions** | Fast coding flow | Predicts code as you type | *"Complete this validation function."* |
| **Ask** | Learning and debugging | Conversational Q&A without modifying code | *"What does this function do?"* or *"Explain this error."* |
| **Inline Chat and Targeted Edits** | Small, local changes | Applies focused edits to selected code or the current file | *"Rename this variable to `isUserLoggedIn`."* |
| **Plan** | Architecture and strategy | Generates a step-by-step blueprint before coding | *"Plan a user authentication module, including risks and tests."* |
| **Agent** | Autonomous building | Iterative coding, approved terminal commands, and multi-file changes | *"Create a React component with tests and add it to the router."* |
| **Copilot CLI** | Terminal workflows | Uses Copilot from a shell for scripts, tests, Git, and DevOps tasks | *"Run the test suite, explain failures, and propose the smallest fix."* |
| **Copilot Cloud Agent** | Asynchronous GitHub work | Researches, plans, and prepares changes on a branch or pull request where enabled | *"Research this issue and prepare an implementation plan."* |

### Detailed Breakdown

#### Ask Mode (Chat)

> **Function:** Acts as a knowledgeable pair programmer who can see your code but touches nothing. It answers questions, explains concepts, and generates code snippets you must manually copy/insert.

**When to use:**
- Exploring a new codebase
- Understanding how existing code works
- Getting explanations without risking accidental changes

**Example:**
> *"You are exploring a new codebase and want to understand how the `AuthService` works without risking accidental deletions."*

#### Inline Chat and Targeted Edits

> **Function:** A focused editing workflow for selected code or the current file. You highlight code or place the cursor in context, then give a specific instruction. Copilot applies changes for your review in the editor or diff view.

**When to use:**
- Making precise, controlled changes
- Refactoring specific sections of code
- Adding documentation or comments

**Example:**
> *"You have a 50-line function and want to refactor it to use `async/await` instead of callbacks, or add comments to a class."*

#### Plan Agent (Think Before Editing)

> **Function:** The plan-first workflow. Instead of writing code immediately, Copilot analyses your request and codebase to generate a structured implementation plan. You review and refine this plan before handing it to Agent mode or implementing it manually.

**When to use:**
- Planning complex features
- Understanding the scope of changes needed
- Creating acceptance criteria, test plans, and risk lists before code changes

**Example:**
> *"Plan how to add dark mode support. Identify the files that likely need changing, tests to add, risks, and manual verification steps. Do not edit files yet."*

#### Agent Mode (Autonomous Developer)

> **Function:** The most powerful mode. It functions autonomously to complete a task. It can edit multiple files, run terminal commands (like `npm install` or running tests), and self-correct if it encounters errors.

**When to use:**
- Scaffolding new projects or features
- Tasks requiring changes across multiple files
- Operations that need terminal commands

**Example:**
> *"Scaffold a new Next.js project with Tailwind CSS." The Agent will create folders, install dependencies, and write the initial pages while you watch.*

#### Copilot CLI and Copilot Cloud Agent

> **Function:** The CLI brings agentic Copilot workflows to the terminal. Copilot cloud agent works asynchronously through GitHub where enabled, commonly from issues, branches, and pull requests.

**When to use:**
- Running tests, linters, Git commands, and DevOps tasks from the terminal
- Delegating well-scoped GitHub work to a branch or pull request
- Asking Copilot to research an issue and produce a plan before code is written

**Example:**
> *"Research this failing workflow, identify the likely root cause, propose the smallest fix, and wait for approval before changing files."*

### Custom Agents (Extensions)

GitHub Copilot supports **custom agents** that provide specialised capabilities. Custom agents allow repositories or organisations to define specialised AI assistants tailored to specific rules, documentation, or external services. You define them using `.agent.md` files, which can specify prompts, tools, subagents, handoffs, and MCP servers.

MCP servers can expose external tools and data to Copilot. Enable only trusted MCP servers, scope their permissions carefully, and confirm that your organisation policy allows them before using them in a workshop.

> **Tip:** Custom agents are covered in detail in **Week 2, Session 1** ([Prompt Engineering and Customisation](../Week2/1-Prompt-Engineering-and-Customisation.md)), where you will learn how to create and configure your own agents.

### Choosing the Right Mode

- **Need fast completions?** Use **Inline Suggestions**
- **Need answers?** Use **Ask Mode**
- **Need a focused local edit?** Use **Inline Chat and Targeted Edits**
- **Need a roadmap?** Use **Plan**
- **Need multi-file implementation?** Use **Agent Mode**
- **Need terminal or DevOps help?** Use **Copilot CLI**
- **Need asynchronous GitHub work where enabled?** Use **Copilot Cloud Agent**

---

## Part 6: Troubleshooting

> **Tip:** If GitHub Copilot stops working, first check [GitHub's Status page](https://githubstatus.com/) for any active incidents.

### Copilot Extension Won't Install

**Solution:**
- Verify you're using the latest IDE version
- Check internet connection
- Try uninstalling and reinstalling the extension
- Update your GitHub Copilot extension. Older clients cannot communicate with Copilot servers
- Check IDE compatibility in the [IDE Support Guide](../../FAQ/IDE-support.md)

### No Suggestions Appearing

**Solution:**
- Verify Copilot is enabled (check status icon, a diagonal line means disabled)
- Check if the file is excluded by content exclusion settings (hover over the icon to see)
- Wait briefly. Copilot needs context and can sometimes take a while to load
- Ensure you're signed in to GitHub
- Update to the latest extension version

### Authentication Errors (VS Code)

**Solution:**
1. Click the **Accounts icon** in the bottom left corner of VS Code
2. Hover over your GitHub username and click **Sign out**
3. Press `F1` to open the command palette, then select **Developer: Reload Window**
4. After VS Code reloads, sign back in to your GitHub account

### Slow or No Responses

**Solution:**
- Check internet connectivity
- Reduce file size if editing very large files
- Try a different model if available
- Check [GitHub Status page](https://githubstatus.com/) for service issues
- Review firewall/proxy settings if in a corporate environment

---

## Part 7: Best Practices for Setup

1. **Start with VS Code** if you're new, it has the most complete Copilot integration
2. **Keep your IDE updated** to ensure compatibility with latest Copilot features
3. **Use keyboard shortcuts** to speed up workflow, refer back to this guide as needed
4. **Disable Copilot for sensitive files** if working with proprietary or security critical code
5. **Customise your shortcuts** to match your existing workflow
6. **Run `/init`** in VS Code to create project instructions before starting a team exercise
7. **Confirm approvals and permissions** for agents, terminal commands, MCP servers, and external network access

---

## Next Steps

- **Week 1 Session 3:** In the next session, we'll complete an interactive [hands-on lab](3-Week1-Lab.md) to apply GitHub Copilot in real-world scenarios

