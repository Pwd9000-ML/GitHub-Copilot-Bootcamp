# Weekly Curriculum Templates

This folder contains reusable templates for creating new weekly curriculum material. Each template mirrors the file and folder structure used in `Workshops/Week1/` through `Workshops/Week4/`.

## How to Use

1. **Copy** the templates into a new folder, e.g. `Workshops/Week5/`.
2. **Rename** each file following the numbering convention: `{N}-{Topic-Name}.md`.
3. **Replace** every `{{PLACEHOLDER}}` with the appropriate value for the new week.
4. **Choose** the lab template that fits your delivery model:
   - [LAB-SKILLS-TEMPLATE.md](LAB-SKILLS-TEMPLATE.md) for short, external GitHub Skills exercises (Weeks 1-4 pattern, recommended).
   - [LAB-SELF-CONTAINED-TEMPLATE.md](LAB-SELF-CONTAINED-TEMPLATE.md) for longer, inline hands-on exercises (use when no suitable GitHub Skills exercise exists).
5. **Create** the matching issue template by copying [ISSUE-TEMPLATE.yml](ISSUE-TEMPLATE.yml) into `.github/ISSUE_TEMPLATE/` and updating the placeholders.
6. **Update** the root `README.md` using the snippet in [README-SNIPPET.md](README-SNIPPET.md).

## Folder Structure After Copying

```text
Workshops/Week{{WEEK_NUMBER}}/
├── 1-{{SESSION_1_TOPIC}}.md          ← from SESSION-TEMPLATE.md
├── 2-{{SESSION_2_TOPIC}}.md          ← from SESSION-TEMPLATE.md (duplicate for additional sessions)
├── {{LAB_FILE_NUMBER}}-Week{{WEEK_NUMBER}}-Lab.md  ← from LAB-SKILLS-TEMPLATE.md or LAB-SELF-CONTAINED-TEMPLATE.md
└── {{PROMPTS_FILE_NUMBER}}-Week{{WEEK_NUMBER}}-Prompts.md ← from PROMPTS-TEMPLATE.md
```

## Placeholder Reference

| Placeholder | Description | Example |
|---|---|---|
| `{{WEEK_NUMBER}}` | Week number (integer) | `5` |
| `{{WEEK_TITLE}}` | Short title for the week | `Advanced Agent Workflows` |
| `{{WEEK_OBJECTIVE}}` | One-sentence learning objective | `Explore autonomous agent capabilities and multi-step workflows.` |
| `{{WEEK_TOTAL_DURATION}}` | Estimated total hours | `2-3 hours` |
| `{{SESSION_TITLE}}` | H1 heading for a session | `Agent Mode Deep Dive` |
| `{{SESSION_DURATION}}` | Session length | `45-60 minutes` |
| `{{SESSION_FORMAT}}` | Delivery format | `Presentation with discussion points` |
| `{{SESSION_OBJECTIVE}}` | Session learning goal | `Understand how Agent Mode orchestrates multi-file changes.` |
| `{{SESSION_CONTENTS}}` | Table of contents entries | See SESSION-TEMPLATE.md |
| `{{SESSION_BODY}}` | Main session content sections | See SESSION-TEMPLATE.md |
| `{{LAB_TITLE}}` | H1 heading for the lab | `Agent Workflows Hands-On Lab` |
| `{{LAB_DURATION}}` | Lab time estimate | `60-90 minutes` |
| `{{LAB_DESCRIPTION}}` | Short lab description | `Build an agent-driven refactoring pipeline.` |
| `{{LAB_FILE_NUMBER}}` | Position in the file list | `3` |
| `{{PROMPTS_FILE_NUMBER}}` | Position in the file list | `4` |
| `{{PROMPTS_OBJECTIVE}}` | Purpose of the prompts page | `Provide reference prompts for agent workflows.` |
| `{{NEXT_SESSION_TITLE}}` | Title of the following page | `Week 5 Prompt Examples` |
| `{{NEXT_SESSION_FILE}}` | Relative path to the next file | `4-Week5-Prompts.md` |
| `{{NEXT_WEEK_SESSION_TITLE}}` | First session of the following week | `Continue to Week 6` |
| `{{NEXT_WEEK_SESSION_FILE}}` | Relative path to that file | `../Week6/1-Topic.md` |
| `{{PREVIOUS_WEEK_NUMBER}}` | Previous week number | `4` |
| `{{SKILLS_REPO_OWNER}}` | GitHub Skills template owner | `skills` |
| `{{SKILLS_REPO_NAME}}` | GitHub Skills template repo name | `getting-started-with-github-copilot` |
| `{{SKILLS_BADGE_TEXT}}` | Badge label text | `Copy Exercise` |

## Styling Rules

All new content **must** follow the rules in [`.github/instructions/Currriculum-Styling.instructions.md`](../.github/instructions/Currriculum-Styling.instructions.md):

- British English spelling throughout.
- No emdashes. Use full stops or commas to separate clauses.
- Every page ends with a **Next Steps** section.
- Code blocks include comments explaining purpose and key details.
- Update the root `README.md` date and Table of Contents when adding a week.
- Review and update issue templates when curriculum changes.
