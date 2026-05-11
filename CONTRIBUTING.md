# Contributing to GitHub Copilot Training

Thank you for helping improve this training curriculum! Here's how to contribute.

## Ways to Contribute

- **Fix errors** - Typos, broken links, outdated information
- **Improve content** - Clarify explanations, add examples, enhance prompts
- **Add exercises** - New hands-on activities or lab scenarios
- **Update for new features** - Keep pace with Copilot updates

## Guidelines

1. **Keep it practical** - Focus on real-world developer workflows
2. **Be concise** - Training time is valuable; avoid unnecessary content
3. **Test your prompts** - Verify Copilot prompts produce expected results
4. **Follow the structure** - Match existing file formats and naming conventions

## Submitting Changes

1. Fork the repository
2. Create a branch: `feature/your-change` or `fix/issue-description`
3. Make your changes
4. Submit a pull request with a clear description

## Adding a New Week

The fastest way to add a new week is to use the **weekly-curriculum** Copilot skill in `.github/skills/weekly-curriculum/`. Ask GitHub Copilot something like `add a new week covering <topic>` and it will scaffold the `Workshops/WeekN/` folder, the lab issue template, and the root `README.md` updates from the canonical templates in `templates/`.

If you prefer to scaffold by hand, copy the files in `templates/` and follow the placeholder reference in `templates/README.md`.

## Content Structure

| Folder | Purpose |
|--------|---------|
| `Workshops/WeekN/` | Weekly training content and labs |
| `FAQ/` | Guides for facilitators and participants |
| `templates/` | Canonical templates for new weekly content |
| `.github/skills/` | Copilot skills that automate repository workflows |
| `.github/ISSUE_TEMPLATE/` | Lab reflection templates |

## Questions?

Open an issue for discussion before making large changes.
