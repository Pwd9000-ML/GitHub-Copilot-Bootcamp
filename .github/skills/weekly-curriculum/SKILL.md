---
name: weekly-curriculum
description: Scaffold a new weekly workshop for the GitHub Copilot Bootcamp curriculum. Use when the user asks to add a new week, create a new workshop, generate Week N content, scaffold weekly curriculum, draft a new bootcamp module, or add a new topic such as "MCPs with GitHub Copilot" to the training programme. Generates the Workshops/WeekN folder, the four standard markdown pages (two sessions, one lab, one prompts reference), the matching lab issue template, and updates the root README.md and Last Updated date.
license: MIT
---

# Weekly Curriculum Scaffolder

Use this skill to add a brand new week of content to the GitHub Copilot Bootcamp curriculum. It enforces the existing folder layout, file naming, placeholder fill-in, styling rules, and root README updates so a new week is consistent with Weeks 1 to 5.

## When to use this skill

- The user asks to add, create, scaffold, or draft a new week of workshop content.
- The user names a topic for a future week (for example "MCPs with GitHub Copilot", "Security with Copilot", "Testing with Copilot").
- The user wants to extend the curriculum and asks how to start, or asks you to "use the templates".

## When NOT to use this skill

- Editing or fixing content inside an existing week. Edit those files directly and follow `.github/instructions/Currriculum-Styling.instructions.md`.
- Updating only the FAQ, metrics, or the root README without adding a new week.
- Authoring a new GitHub Copilot Skill or prompt file. Those are unrelated to weekly workshop content.

## Inputs to gather from the user

Before generating any files, confirm the following with the user. Ask them as one batched question if values are missing, and use sensible defaults where shown.

| Input | Required | Example | Notes |
|---|---|---|---|
| Week number | Yes | `5` | Must be the next free integer after the highest existing `Workshops/WeekN/` folder. |
| Week title | Yes | `MCPs with GitHub Copilot` | Short, sentence case, no trailing punctuation. |
| Week objective | Yes | `Understand the Model Context Protocol and integrate MCP servers with GitHub Copilot.` | One sentence. |
| Week total duration | No | `2-3 hours` | Default `2-3 hours`. |
| Session 1 title | Yes | `Introduction to the Model Context Protocol` | |
| Session 2 title | Yes | `Using and Building MCP Servers with Copilot` | |
| Lab style | Yes | `skills` | All labs in this curriculum link to an external `github.com/skills/...` exercise. Do not compose inline lab exercises. |
| External GitHub Skills repo | Yes | `skills/integrate-mcp-with-copilot` | The `github.com/skills/<repo>` exercise this lab points to. Do not invent a URL; if none exists yet, ask the user to provide one. |
| Lab title | Yes | `Hands-On with MCP Servers` | |
| Lab duration | No | `60-90 minutes` | Default `60-90 minutes`. |
| Four lab activities | Yes | Short labels for the issue template checkboxes | Used as `{{ACTIVITY_1}}` to `{{ACTIVITY_4}}`. |
| Prompt categories (5 to 8) | Yes | `MCP discovery`, `Server configuration`, `Tool invocation`, ... | Used in the prompts reference. |

If any required input is missing or ambiguous, ask the user before generating files.

## Step-by-step workflow

Follow these steps in order. Read each referenced file from the repository before generating output so placeholders match the latest template versions.

### 1. Verify the target week is free

1. List `Workshops/` and confirm `Workshops/Week{{WEEK_NUMBER}}/` does not already exist.
2. Confirm `.github/ISSUE_TEMPLATE/week{{WEEK_NUMBER}}-lab.yml` does not already exist.
3. If either exists, stop and ask the user how to proceed.

### 2. Read the canonical templates

Read these files from the repo before authoring anything. They are the source of truth for structure and placeholders, do not invent your own layout:

- `templates/SESSION-TEMPLATE.md`
- `templates/LAB-SKILLS-TEMPLATE.md`
- `templates/PROMPTS-TEMPLATE.md`
- `templates/ISSUE-TEMPLATE.yml`
- `templates/README-SNIPPET.md`
- `templates/README.md` for the full placeholder reference table

### 3. Create the Workshops/WeekN folder and four pages

Create the folder `Workshops/Week{{WEEK_NUMBER}}/` and write these four files. File naming is mandatory:

```text
Workshops/Week{{WEEK_NUMBER}}/
├── 1-{{SESSION_1_FILENAME}}.md          # from SESSION-TEMPLATE.md
├── 2-{{SESSION_2_FILENAME}}.md          # from SESSION-TEMPLATE.md
├── 3-Week{{WEEK_NUMBER}}-Lab.md         # from chosen LAB template
└── 4-Week{{WEEK_NUMBER}}-Prompts.md     # from PROMPTS-TEMPLATE.md
```

Rules for the session filenames:

- Convert the session title to title case with hyphens, drop punctuation. Example: `Introduction to the Model Context Protocol` becomes `Introduction-to-the-Model-Context-Protocol`.
- Final filename is `1-Introduction-to-the-Model-Context-Protocol.md`.

For each generated file:

- Replace every `{{PLACEHOLDER}}` with a real value. Do not leave any `{{` or `}}` markers in committed output.
- Ensure each session page has three main sections, a Best Practices table (4 to 6 rows), four Key Takeaways, three Discussion Questions, and a Next Steps section.
- Ensure each page ends with a `## Next Steps` section that links to the next file in the sequence. The last page (prompts) links forward to the next week if known, otherwise to the weekly reflection issue template.
- Cross-link files using relative paths within the week folder, for example `2-...md`, `3-Week5-Lab.md`, `4-Week5-Prompts.md`.

### 4. Create the lab issue template

1. Copy `.github/ISSUE_TEMPLATE/week1-lab.yml` as the structural baseline (it is the most complete real example).
2. Save it as `.github/ISSUE_TEMPLATE/week{{WEEK_NUMBER}}-lab.yml`.
3. Replace the week number, lab title, session filenames, and the four activity labels.
4. Keep the IDE dropdown, Copilot modes checkboxes, time impact dropdown, and confidence dropdown unchanged unless the user explicitly asks otherwise.

### 5. Update the root README.md

1. Read `templates/README-SNIPPET.md`.
2. Fill all placeholders. Provide four bullets for each session, four for the lab, and four for the prompts reference.
3. Insert the filled snippet into `README.md` under the `## Curriculum` heading, placed after the previous week and before any `## Additional Resources` heading.
4. Add the Table of Contents entries from the snippet's HTML comment block to the existing TOC at the top of `README.md`, immediately after the previous week's entries. Compute markdown anchor slugs by lowercasing the heading and replacing spaces and punctuation with single hyphens.
5. Update the `**Last Updated:** DD/MM/YYYY` line near the top of `README.md` to today's date in DD/MM/YYYY format.

### 6. Validate against the styling checklist

Run through every item in [references/CHECKLIST.md](references/CHECKLIST.md) before reporting done. If any item fails, fix it before finishing.

### 7. Report back to the user

Summarise:

- The folder and files created.
- Lines changed in `README.md`.
- Any placeholders that still need a human decision (for example, a real GitHub Skills exercise URL when one does not yet exist).
- Suggested git commit message, for example `Add Week 5: MCPs with GitHub Copilot`.

Do not push or open a pull request unless the user explicitly asks.

## Styling rules that must be enforced

These are pulled from `.github/instructions/Currriculum-Styling.instructions.md` and `.github/instructions/markdown.instructions.md`. They apply to every file you generate.

- British English spelling and grammar throughout (for example "customise", "behaviour", "organisation").
- No em dashes (—). Use a full stop or comma instead.
- No emojis.
- Every page ends with a `## Next Steps` section, except FAQ documents (this skill does not edit FAQ).
- Code blocks include a comment explaining purpose and any important details.
- Tables are used for comparisons, feature matrices, and best practices.
- Headings follow the hierarchy: H1 for page title, H2 for major sections, H3 for subsections.
- Verify any external links and references against authoritative sources before including them.

## Examples

### Example invocation

> User: "Add a new week to the bootcamp covering MCPs and how to use them with GitHub Copilot."

Expected behaviour:

1. Confirm Week 6 is free.
2. Ask the user (one batched question) for: session 1 and 2 titles, lab style, four lab activities, five to eight prompt categories. Suggest sensible defaults for the topic.
3. Generate `Workshops/Week6/1-...md`, `2-...md`, `3-Week6-Lab.md`, `4-Week6-Prompts.md`.
4. Generate `.github/ISSUE_TEMPLATE/week6-lab.yml`.
5. Update `README.md` curriculum section, TOC, and Last Updated date.
6. Run the checklist.
7. Report changes and suggest a commit message.

### Example session filename derivation

| Session title | Derived filename |
|---|---|
| `Introduction to the Model Context Protocol` | `1-Introduction-to-the-Model-Context-Protocol.md` |
| `Using and Building MCP Servers with Copilot` | `2-Using-and-Building-MCP-Servers-with-Copilot.md` |

## Edge cases

- **No real GitHub Skills exercise exists for the topic.** Ask the user to supply or wait for a real `github.com/skills/<repo>` URL. Do not invent a URL.
- **The user provides only a topic with no session titles.** Propose two session titles and confirm with the user before generating.
- **`README.md` TOC anchors collide** because two weeks share session titles. Make the headings unique, for example by including `Week {{WEEK_NUMBER}}` in the heading text, so the generated GitHub anchor is unique. If duplicate headings must remain, use GitHub's deduplicated anchor format with `-1`, `-2`, and so on.
- **The user wants more or fewer than two sessions.** The current convention is exactly two sessions, one lab, one prompts page. If the user wants a different shape, confirm explicitly and update file numbers accordingly (`{{LAB_FILE_NUMBER}}` and `{{PROMPTS_FILE_NUMBER}}`).
- **The user already started the new week manually.** Ask whether to overwrite, merge, or abort.

## Files in this skill

- [SKILL.md](SKILL.md) - this file.
- [references/CHECKLIST.md](references/CHECKLIST.md) - validation checklist run before reporting done.

## Next Steps

After scaffolding a new week, recommend the user:

1. Review the generated files in the new branch and tweak content for accuracy.
2. Run the `Research.prompt.md` prompt in `.github/prompts/` to verify all external references are current.
3. Open a pull request for review when satisfied.
