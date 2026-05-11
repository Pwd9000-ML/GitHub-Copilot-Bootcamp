# Weekly Curriculum Scaffolding Checklist

Run through every item before reporting the new week as done. Fix any failure before finishing.

## Folder and files

- [ ] `Workshops/Week{{WEEK_NUMBER}}/` exists and contains exactly four markdown files.
- [ ] File names follow the pattern `1-Title.md`, `2-Title.md`, `3-Week{{WEEK_NUMBER}}-Lab.md`, `4-Week{{WEEK_NUMBER}}-Prompts.md`.
- [ ] No `{{PLACEHOLDER}}` markers remain in any generated file.
- [ ] All relative links between the four files resolve.

## Issue template

- [ ] `.github/ISSUE_TEMPLATE/week{{WEEK_NUMBER}}-lab.yml` exists.
- [ ] Title prefix, labels, and week number all match `{{WEEK_NUMBER}}`.
- [ ] The four activity checkboxes have been replaced with real activity labels.
- [ ] References to session filenames inside the issue template match the real generated filenames.

## Root README.md

- [ ] A new `### Week {{WEEK_NUMBER}}: {{WEEK_TITLE}}` section has been added under `## Curriculum`, in numerical order.
- [ ] Four bullets per session, lab, and prompts list (no empty bullets, no placeholders).
- [ ] Two feedback links present: `week{{WEEK_NUMBER}}-lab.yml` and `weekly-reflection.yml`.
- [ ] Table of Contents at the top of `README.md` has matching entries with valid anchor slugs.
- [ ] `**Last Updated:** DD/MM/YYYY` line reflects today's date in DD/MM/YYYY format.

## Styling and language

- [ ] British English spelling throughout. Common swaps: customize -> customise, behavior -> behaviour, organize -> organise, color -> colour.
- [ ] No em dashes (—) anywhere in the new files. Use full stops or commas.
- [ ] No emojis anywhere in the new files.
- [ ] Every new page ends with a `## Next Steps` section.
- [ ] Code blocks include comments explaining purpose and any important details.
- [ ] Heading hierarchy is consistent: one H1 per page, H2 for major sections, H3 for subsections.

## Cross-linking

- [ ] Session 1 Next Steps links to Session 2.
- [ ] Session 2 Next Steps links to the Lab.
- [ ] Lab Next Steps links to the Prompts reference.
- [ ] Prompts Next Steps links forward (to the next week if known, otherwise the weekly reflection issue template).

## External references

- [ ] Any external links to docs.github.com, code.visualstudio.com, or github.com/skills resolve and refer to real, current pages.
- [ ] No invented or hallucinated URLs.

## Final report

- [ ] Summary of created files and changed files.
- [ ] List of any human decisions still required.
- [ ] Suggested git commit message of the form `Add Week {{WEEK_NUMBER}}: {{WEEK_TITLE}}`.
