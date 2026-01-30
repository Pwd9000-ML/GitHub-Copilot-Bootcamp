# GitHub Copilot Setup and Configuration Guide

**Duration:** 30 minutes
**Format:** LIVE Demo/Recording  
**Objective:** Get GitHub Copilot installed, configured, and ready to use in your preferred development environment.

---

## Contents

- [Part 1: Getting GitHub Copilot Access](#part-1-getting-github-copilot-access)
- [Part 2: IDE-Specific Setup](#part-2-ide-specific-setup)
  - [Visual Studio Code](#visual-studio-code-recommended)
  - [Visual Studio (Full IDE)](#visual-studio-full-ide)
  - [JetBrains IDEs](#jetbrains-ides-intellij-idea-pycharm-webstorm-etc)
  - [Xcode (macOS)](#xcode-macos)
  - [Neovim / Vim](#neovim--vim)
  - [Eclipse for SAP ABAP Development (ADT)](#eclipse-for-sap-abap-development-adt)
  - [Known Limitations for ABAP Development](#known-limitations-for-abap-development-with-github-copilot)
- [Part 3: Configuration and Customisation](#part-3-configuration-and-customisation)
- [Part 4: Basic Commands and Workflows](#part-4-basic-commands-and-workflows)
- [Part 5: Troubleshooting](#part-5-troubleshooting)
- [Part 6: Best Practices for Setup](#part-6-best-practices-for-setup)

---

## Prerequisites

- Active GitHub account
- GitHub Copilot subscription/license (Pro, Business, or Enterprise plan)
- IDE installed on your machine

---

## Part 1: Getting GitHub Copilot Access

### Step 1: Verify Your Subscription

1. Visit [https://github.com/](https://github.com/)  
   **Note:** If you're part of an enterprise organization, your GitHub URL may differ. Check with your GitHub representative or Champion for details.
2. Check your subscription status under **Settings → Billing and Plans**
3. Ensure your plan includes GitHub Copilot access

### Step 2: Install the GitHub Copilot Extension

The installation process varies by IDE. Follow the relevant section below for your development environment.

---

## Part 2: IDE-Specific Setup

### Visual Studio Code (Recommended)

#### Installation

1. **Open VS Code**
2. **Go to Extensions** (`Ctrl+Shift+X` or `Cmd+Shift+X`)
3. **Search for "GitHub Copilot"**
4. **Click Install** on the official GitHub extension
5. **Restart VS Code**

#### Sign In

1. After restart, you'll see a **"Sign in to use GitHub Copilot"** notification
2. Click **"Sign in with GitHub"**
3. Authorize the extension in your browser
4. Return to VS Code, you're ready to use Copilot!

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
> 3. Official documentation: [GitHub Copilot Keyboard Shortcuts](https://docs.github.com/en/copilot/reference/keyboard-shortcuts)

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

- **No Checkpoints support:** Cannot create or restore checkpoints during agent sessions
- **No Custom chat modes:** Unable to define custom slash commands or chat behaviours
- **No Workspace indexing:** Local codebase indexing for improved context is not available
- **No Java Upgrade Agent:** Automated Java version migration assistance not supported
- **Version requirements:** Some features require Visual Studio 2022 version 17.11 or later
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
3. Authorize in your browser
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
- **No Custom chat modes:** Unable to define custom slash commands or chat behaviours
- **No Workspace indexing:** Local codebase indexing for improved context is not available
- **No Java Upgrade Agent:** Automated Java version migration assistance not supported
- **No Next edit suggestions:** Proactive suggestions for your next likely edit not available (VS Code and Xcode only)

> See [GitHub Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

### Xcode (macOS)

#### Prerequisites

- Xcode version 8.0 or above
- macOS Monterey (12.0) or above

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
3. **Restart Xcode** — you will see a new "GitHub Copilot" item in the **Editor** menu

#### Sign In

1. Open the **GitHub Copilot for Xcode** application
2. Click **Login to GitHub** and follow the prompts to authorize

#### Basic Commands

| Action | Keyboard Shortcut |
|--------|------------------|
| Accept the first line of a suggestion | `Tab` |
| View full suggestion | Hold `Option` |
| Accept full suggestion | `Option + Tab` |

> **Note:** Official documentation: [GitHub Copilot for Xcode](https://docs.github.com/en/copilot/reference/keyboard-shortcuts?tool=xcode)

#### Known Limitations

- **No Edit mode (Copilot Edits)** — Multi-file editing capabilities not available
- **No Extensions support** — Cannot use MCP extensions or third-party integrations
- **No Code referencing** — Cannot view public code matches for suggestions
- **No Workspace indexing** — Local codebase indexing for improved context is not available
- **No .NET or Java Upgrade Agents** — Automated migration assistance not supported
- **macOS permission requirements** — Requires Accessibility and Files & Folders permissions; missing permissions can cause communication issues or block real-time suggestions
- **External app architecture** — Runs as a separate application communicating with Xcode, which can occasionally cause synchronisation issues

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

- **Code completion only** — Only inline code suggestions are supported
- **No Copilot Chat** — Interactive chat assistant not available
- **No Agent mode** — Autonomous task execution not supported
- **No Edit mode (Copilot Edits)** — Multi-file editing capabilities not available
- **No Extensions or MCP support** — Cannot use third-party integrations
- **No Code referencing** — Cannot view public code matches for suggestions
- **No Custom instructions or Prompt files** — Cannot customise Copilot behaviour
- **No Vision support** — Cannot process images or screenshots
- **No Workspace indexing** — Local codebase indexing not available
- **No Copilot code review** — Automated code review features not supported
- **No Next edit suggestions** — Proactive suggestions for next edits not available

> **Source:** [GitHub Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

---

### Eclipse for SAP ABAP Development (ADT)

SAP ABAP developers use **ABAP Development Tools (ADT)** within Eclipse to develop ABAP applications. This section covers how to set up both ADT and GitHub Copilot in Eclipse.

#### Prerequisites for ABAP Development

| Requirement | Version/Details |
|-------------|-----------------|
| **Eclipse** | 2025-09 (4.37) or 2025-12 (4.38) |
| **Java Runtime** | JRE 21 (64-Bit, LTS) |
| **SAP GUI** | Windows 8.00+ or macOS Java 8.10+ |
| **Operating System** | Windows 10+ or macOS 10.15+ |
| **Visual C++ (Windows)** | Microsoft Visual C++ 2015-2022 Redistributable (x64) |

> **Note:** GitHub Copilot for Eclipse requires Eclipse version 2024-03 or above. Since ADT requires Eclipse 2025-09+, you will meet the Copilot requirement automatically.

#### Step 1: Install Eclipse

1. Download **Eclipse IDE for Java Developers** (version 2025-12 recommended) from [eclipse.org/downloads](https://www.eclipse.org/downloads/)
2. Extract and install Eclipse
3. Launch Eclipse and select your workspace location

#### Step 2: Install ABAP Development Tools (ADT)

1. In Eclipse, go to **Help → Install New Software**
2. Click **Add** to add a new repository
3. Enter the following:
   - **Name:** `SAP Development Tools`
   - **Location:** `https://tools.hana.ondemand.com/latest`
4. Select **ABAP Development Tools** from the list
5. Click **Next** and accept the license agreement
6. Complete installation and **restart Eclipse**

> **Official Reference:** [SAP Development Tools Installation Guide](https://tools.hana.ondemand.com/#abap)

#### Step 3: Install GitHub Copilot Extension

1. Go to **Help → Eclipse Marketplace** (or **Help → Install New Software**)
2. Search for **"GitHub Copilot"**
3. Click **Install** and follow the prompts
4. **Restart Eclipse** after installation

> **Official Reference:** [GitHub Copilot Extension for Eclipse](https://marketplace.eclipse.org/content/github-copilot)

#### Step 4: Sign In to GitHub Copilot

1. Locate the **Copilot icon** in the bottom-right corner of Eclipse
2. Click the icon and select **"Sign In to GitHub"**
3. Click **"Copy Code and Open"** to copy your device code
4. Paste the code in your browser and authorize the GitHub Copilot Plugin
5. Return to Eclipse and click **OK** to complete setup

#### Basic Commands in Eclipse

| Action | Method |
|--------|--------|
| **Trigger Suggestions** | Start typing—suggestions appear inline |
| **Accept Suggestion** | `Tab` |
| **Dismiss Suggestion** | `Esc` |
| **Open Copilot Chat** | Click Copilot icon in toolbar |

---

### Known Limitations for ABAP Development with GitHub Copilot

Before relying on GitHub Copilot for ABAP development, be aware of these important limitations:

#### 1. Agent Mode URI Scheme Limitation

GitHub Copilot's Agent Mode in Eclipse **does not support the `semanticfs` URI scheme** used by ABAP Development Tools. This means:

- Advanced agent-based features may not work correctly with ABAP files
- Workspace-level operations that depend on file system access may be limited
- You may encounter errors related to unsupported URI schemes when using agent features

> **Source:** [Eclipse Marketplace - GitHub Copilot User Reviews](https://marketplace.eclipse.org/content/github-copilot)

#### 2. ABAP Language Support Quality

GitHub Copilot's AI models are trained primarily on publicly available code repositories. Since ABAP is a **proprietary SAP language** with limited open-source code available:

- Suggestions may be **less accurate** compared to popular languages (Python, JavaScript, Java)
- Complex SAP-specific patterns, BAPIs, and function modules may not be well-represented in training data
- Code completions for standard ABAP constructs work, but domain-specific SAP modules may have inconsistent support
- Custom SAP tables, data elements, and domains are unknown to Copilot

#### 3. Eclipse Installation Dependencies

Users have reported dependency conflicts during GitHub Copilot installation in Eclipse:

- Conflicts with **Mylyn WikiText UI** and **LSP4e** components may occur
- "Cannot satisfy dependency" errors may prevent installation
- **Solution:** Ensure your Eclipse installation is fully up-to-date and consider removing conflicting plugins if necessary

> **Source:** [Eclipse Marketplace - GitHub Copilot Reviews](https://marketplace.eclipse.org/content/github-copilot)

#### 4. Network and Certificate Issues

Organisations using corporate proxies may experience:

- Certificate validation failures during sign-in
- Language server connection issues
- **Solution:** Configure the `NODE_EXTRA_CA_CERTS` environment variable to point to your organisation's CA certificates

#### 5. SAP Backend Connectivity

ABAP development requires connection to an SAP backend system. GitHub Copilot:

- Cannot access your SAP system metadata directly
- Has no visibility into your custom function modules, classes, or data dictionary objects
- Cannot suggest code based on your specific SAP customisations or transport requests

#### Best Practices for ABAP Developers Using Copilot

1. **Use Copilot for boilerplate code** — Standard ABAP syntax, loops, SELECT statements, and common patterns
2. **Provide detailed comments** — Help Copilot understand your intent with descriptive ABAP comments (`" comment`)
3. **Verify all suggestions** — Always review generated ABAP code against SAP documentation and your system's data dictionary
4. **Combine with SAP tools** — Use Copilot alongside SAP's built-in code templates, patterns, and ABAP documentation
5. **Leverage for non-ABAP files** — Copilot works well for related files like JSON, XML, JavaScript (UI5/Fiori), and documentation

#### Official References

- [SAP Development Tools](https://tools.hana.ondemand.com/#abap) — Official ADT download and documentation
- [GitHub Copilot in Eclipse](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment) — Official installation guide
- [Eclipse Marketplace - GitHub Copilot](https://marketplace.eclipse.org/content/github-copilot) — Extension page with user reviews and known issues

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
1. Open **Copilot Chat** (`Ctrl+Alt+I`)
2. Use the **model picker** in the chat input field
3. Select from available models (varies by subscription — see [Supported AI models](https://docs.github.com/en/copilot/using-github-copilot/ai-models/supported-ai-models-in-copilot))

> **Note:** Different models have different premium request multipliers, which can affect your monthly usage allowance. Copilot Business users may need their organization to enable model switching.

---

## Part 4: Basic Commands and Workflows

### Getting Started: Your First Copilot Chat

**Scenario:** Understanding a function in an existing file

1. **Open a code file** and select a function you want to understand
2. **Open Copilot Chat** (`Ctrl+L` in VS Code)
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
4. Copilot analyzes your code and error to provide solutions

---

## Part 5: Troubleshooting

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

## Part 6: Best Practices for Setup

1. **Start with VS Code** if you're new, it has the most complete Copilot integration
2. **Keep your IDE updated** to ensure compatibility with latest Copilot features
3. **Use keyboard shortcuts** to speed up workflow, refer back to this guide as needed
4. **Disable Copilot for sensitive files** if working with proprietary or security critical code
5. **Customise your shortcuts** to match your existing workflow

---

## Next Steps

- **Week 1 Session 3:** In the next session ['GitHub Copilot Interaction Modes'](3-GitHub-Copilot-Interaction-Modes.md), we will learn how to use different modes of GitHub Copilot available in VS Code, when and how to use them effectively

