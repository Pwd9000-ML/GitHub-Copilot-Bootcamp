---
description: Curriculum styling instructions for the GitHub Copilot workshops and Issue templates.
applyTo: "**/*.md,**/.github/ISSUE_TEMPLATE/*.yml"
---

## Language and spelling

- Use British English spelling throughout all curriculum files. Common substitutions: "customise" not "customize", "behaviour" not "behavior", "organisation" not "organization", "optimise" not "optimize", "recognise" not "recognize", "analyse" not "analyze".

## Formatting and structure

- Use consistent heading hierarchy across all markdown files: one H1 per page for the page title, H2 for major sections, H3 for subsections.
- Use consistent formatting for lists and links across all markdown files.
- Do not use em dashes (—). Use a full stop (.) or a comma (,) to separate clauses instead.
- When listing prerequisites, use bullet points and keep each item concise.

## Code blocks

- In every code block, include a comment that explains the purpose of the code and any important detail that learners should be aware of.

## Page completeness

- Every page must end with a `## Next Steps` section that links to the next page in the curriculum or to additional resources. Exception: FAQ documents do not require a Next Steps section.

## Issue templates

- Issue templates must include clear, specific sections for the user to fill out (for example: "What did you try?", "What happened?", "Expected behaviour", "Actual behaviour").
- When curriculum content changes, review the corresponding issue template and update it if the changed content is referenced.

## README maintenance

- When curriculum content or structure changes, update the root `README.md` to reflect those changes.
- After any update, set the `**Last Updated:** DD/MM/YYYY` line near the top of `README.md` to today's date in DD/MM/YYYY format.

## Adding a new week

- When adding a brand new week of content, use the `weekly-curriculum` skill in `.github/skills/weekly-curriculum/SKILL.md`. It enforces the folder layout, file naming, placeholder fill-in, styling rules, and README updates automatically.