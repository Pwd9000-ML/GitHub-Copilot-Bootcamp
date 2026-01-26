# GitHub Copilot Setup and Configuration Guide

**Duration:** 1 hour  
**Format:** LIVE Demo/Recording  
**Objective:** Get GitHub Copilot installed, configured, and ready to use in your preferred development environment.

---

## Prerequisites

- Active GitHub account
- GitHub Copilot subscription (Pro, Business, or Enterprise plan)
- IDE installed on your machine

---

## Part 1: Getting GitHub Copilot Access

### Step 1: Verify Your Subscription

1. Visit [github.com/copilot](https://github.com/copilot)
2. Check your subscription status under **Settings → Billing and Plans**
3. Ensure your plan includes GitHub Copilot access

### Step 2: Install the GitHub Copilot Extension

The installation process varies by IDE. Follow the relevant section below for your development environment.

---

## Part 2: IDE-Specific Setup

### Visual Studio Code (Recommended for Beginners)

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
4. Return to VS Code—you're ready to use Copilot!

#### Basic Commands

| Action | Keyboard Shortcut |
|--------|------------------|
| **Trigger Copilot Chat** | `Ctrl+L` (Windows/Linux) or `Cmd+L` (Mac) |
| **Open Chat in Sidebar** | `Ctrl+Shift+L` (Windows/Linux) or `Cmd+Shift+L` (Mac) |
| **Inline Suggestions** | Start typing—suggestions appear automatically |
| **Accept Suggestion** | `Tab` or `Enter` |
| **Dismiss Suggestion** | `Esc` |
| **Next Suggestion** | `Alt+]` (Windows/Linux) or `Option+]` (Mac) |
| **Previous Suggestion** | `Alt+[` (Windows/Linux) or `Option+[` (Mac) |
| **Open Copilot Edits** | `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac) |

#### UI Overview

```
┌─────────────────────────────────────────────┐
│  VS Code Interface with Copilot             │
├──────────────┬──────────────────────────────┤
│   Sidebar    │                              │
│   - Copilot  │    Editor                    │
│     Chat     │    (Your Code)               │
│   - More...  │                              │
├──────────────┼──────────────────────────────┤
│              │  Terminal / Output           │
└──────────────┴──────────────────────────────┘
```

**Copilot Chat Sidebar:**
- Type questions about your code
- Ask for explanations, refactoring, or generation
- Use `@workspace` to reference your entire project
- Use `@github` for GitHub-specific commands

---

### Visual Studio (Full IDE)

#### Installation

1. **Open Visual Studio Installer**
2. **Click "Modify"** on your Visual Studio installation
3. **Go to Individual Components**
4. **Search for "GitHub Copilot"**
5. **Check the box** and click **Modify**
6. **Restart Visual Studio**

#### Sign In

1. Go to **Tools → Options → GitHub → Copilot**
2. **Sign in with GitHub** account
3. Authorize the connection in your browser

#### Basic Commands

| Action | Keyboard Shortcut |
|--------|------------------|
| **Open Copilot Chat** | `Alt+/` |
| **Inline Suggestions** | `Ctrl+Alt+\` to toggle, `Tab` to accept |
| **Refactor with Copilot** | Right-click code → **Copilot** → **Refactor** |
| **Explain Code** | Right-click code → **Copilot** → **Explain** |

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
| **Open Copilot Chat** | `Ctrl+\` (Windows/Linux) or `Cmd+\` (Mac) |
| **Show Inline Suggestions** | `Alt+\` (Windows/Linux) or `Option+\` (Mac) |
| **Accept Suggestion** | `Tab` |
| **Dismiss Suggestion** | `Esc` |

---

### Xcode (macOS)

#### Installation

1. **Open Xcode**
2. **Go to Xcode → Settings → Accounts**
3. **Add your GitHub account** if not already added
4. **Download the Copilot plugin** from the Mac App Store or GitHub
5. **Restart Xcode**

#### Sign In

1. Go to **Xcode → Settings → Extensions**
2. **Sign in with GitHub**
3. Authorize the connection

#### Basic Usage

- **Inline Suggestions** appear as you type
- **Press Tab** to accept
- **Press Esc** to dismiss

---

### Neovim / Vim

#### Installation (Github Copilot Plugin)

Using **vim-plug**:
```vim
Plug 'github/copilot.vim'
```

Then run `:PlugInstall`

#### Sign In

1. Open Neovim/Vim
2. Run `:Copilot setup`
3. Follow the authentication flow
4. Generate a GitHub device code and authorize

#### Basic Commands

| Action | Command |
|--------|---------|
| **Trigger Inline Suggestion** | Start typing in Insert mode |
| **Accept Suggestion** | `Tab` (or configured keybinding) |
| **Dismiss Suggestion** | `Escape` |
| **Next Suggestion** | `Alt+]` |
| **Previous Suggestion** | `Alt+[` |

---

## Part 3: Configuration and Customization

### Enable/Disable Copilot Globally or Per File

#### VS Code

1. **Disable for all files:** Click the Copilot icon in the status bar and select **Disable Globally**
2. **Disable for a language:** Right-click the status bar → **Disable for [Language]**
3. **Re-enable:** Click Copilot icon → **Enable**

#### Visual Studio

1. **Tools → Options → GitHub → Copilot**
2. Toggle **Enable GitHub Copilot** on/off

### Set Your Preferred Model

If your subscription provides multiple model options:

**VS Code:**
1. Open **Copilot Chat**
2. Look for **Model selector** (top of chat panel)
3. Choose your preferred model (GPT-4, GPT-3.5-turbo, etc.)

### Configure Keyboard Shortcuts

**VS Code:**
1. **File → Preferences → Keyboard Shortcuts** (`Ctrl+K Ctrl+S`)
2. Search for "Copilot"
3. Click the pencil icon next to any command to customize
4. Enter your preferred key combination

---

## Part 4: Common UI Elements and Tips

### Copilot Chat Interface

```
┌─ Copilot Chat ────────────────────┐
│ @workspace  [Model Selector ▼]   │
├───────────────────────────────────┤
│ Previous conversations...         │
│                                   │
│ Assistant: How can I help?       │
│ [Type your question...]           │
│                                   │
│ You: Explain this function        │
│ Assistant: This function...       │
├───────────────────────────────────┤
│ [Message input field...]          │
│ [Send button] [Attach file]       │
└───────────────────────────────────┘
```

### Inline Suggestion Indicators

When Copilot suggests code inline:
- **Gray, dimmed text** = Suggested completion
- **Tab to accept** or keep typing to dismiss
- **Use arrow keys** to cycle through suggestions

### Status Indicators

| Indicator | Meaning |
|-----------|---------|
| ✓ Green Copilot icon | Copilot is active and ready |
| ✗ Red/Disabled | Copilot is disabled for this file/language |
| ⟳ Spinning | Copilot is processing your request |

---

## Part 5: Basic Commands and Workflows

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

## Part 6: Troubleshooting

### Copilot Extension Won't Install

**Solution:**
- Verify you're using the latest IDE version
- Check internet connection
- Try uninstalling and reinstalling the extension
- Check IDE compatibility in the [IDE Support Guide](../../FAQ/IDE-support.md)

### No Suggestions Appearing

**Solution:**
- Verify Copilot is enabled (check status icon)
- Wait briefly—Copilot needs context
- Try opening Copilot Chat directly
- Ensure you're signed in to GitHub

### Authentication Errors

**Solution:**
1. Sign out: Open command palette → "Copilot: Sign Out"
2. Sign back in: Open command palette → "Copilot: Sign In"
3. Complete GitHub authentication in browser
4. Return to IDE and verify green status icon

### Slow or No Responses

**Solution:**
- Check internet connectivity
- Reduce file size if editing very large files
- Try a different model if available
- Review GitHub Copilot status page for service issues

---

## Part 7: Best Practices for Setup

1. **Start with VS Code** if you're new—it has the most complete Copilot integration
2. **Keep your IDE updated** to ensure compatibility with latest Copilot features
3. **Use keyboard shortcuts** to speed up workflow—refer back to this guide as needed
4. **Disable Copilot for sensitive files** if working with proprietary or security-critical code
5. **Customize your shortcuts** to match your existing workflow

---

## Next Steps

- Complete the [GitHub Copilot Interaction Modes](3-GitHub-Copilot-Interaction-Modes.md) guide to learn how to use different modes effectively
- Start the [Week 1 Hands-On Lab](4-week1-lab.md) to apply what you've learned
- Refer to [IDE Support Guide](../../FAQ/IDE-support.md) for detailed information on your specific IDE

---

## Quick Reference Card

**VS Code Essentials:**
- Open Chat: `Ctrl+L`
- Sidebar Chat: `Ctrl+Shift+L`
- Inline Edit: `Ctrl+Shift+I`
- Accept Suggestion: `Tab`
- Next Suggestion: `Alt+]`

**JetBrains Essentials:**
- Open Chat: `Ctrl+\`
- Show Suggestions: `Alt+\`
- Accept: `Tab`

**Visual Studio Essentials:**
- Open Chat: `Alt+/`
- Toggle Suggestions: `Ctrl+Alt+\`

---

**Still need help?** Refer to the [IDE Support Guide](../../FAQ/IDE-support.md) or check the [GitHub Copilot Documentation](https://docs.github.com/en/copilot).
