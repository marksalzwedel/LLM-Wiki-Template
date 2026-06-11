# Agent Instructions

This repository is a reusable Codex plus Obsidian research-template project.

## Active Workspace

- Treat `raw/` as the active source-material folder for the current project.
- Treat `wiki/` as the active Obsidian vault.
- Treat `examples/` as reference material only. Do not mix example content into the active `wiki/` unless the user explicitly asks.

## Default Workflow

1. Read the active source files in `raw/`.
2. Create or update Markdown entity pages in `wiki/`.
3. Use Obsidian-style `[[bracket links]]` between related pages.
4. Maintain `wiki/Project Index.md` as the main map.
5. Maintain `wiki/Contradictions and Tensions.md` as the cross-source disagreement and open-question map.
6. Preserve user-written notes unless the user asks for a rewrite.

## Help Routing

If the user says only `help`, or asks broadly for help with the template, do not edit files immediately. First orient them and ask what kind of help they want.

Use wording like:

```text
I can help initialize or customize a fresh project, add new source material, update or clean the wiki, run a project health check, publish a SharePoint-ready template, or troubleshoot SharePoint/GitHub/Codex/Obsidian setup. Which path are you trying to take?
```

If the user chooses a path, proceed with that workflow. If they ask for `setup wizard`, `customize this template`, `initialize project`, or `configure project`, use the Setup Wizard workflow.

## SharePoint Template Workflow

This template may be distributed as a read-only SharePoint folder that users copy into their own SharePoint-synced workspace.

If a user asks how to create a project from the SharePoint template:

1. Tell them to copy the entire template folder into their own SharePoint-synced project area before editing.
2. Tell them to rename the copied folder to the project name.
3. If OneDrive Files On-Demand is enabled, tell them to right-click the copied project folder and choose **Always keep on this device**.
4. Tell them to open the copied top-level folder in Codex.
5. Then offer the Setup Wizard workflow.

If a maintainer asks to publish or refresh the SharePoint-ready template, run:

```powershell
python scripts\publish_sharepoint_template.py
```

The generated folder under `dist/Codex-SharePoint-Template/` is the folder to review and copy or sync into the read-only SharePoint template library. Do not put `.git/` metadata into the SharePoint-distributed template unless the user explicitly asks for a Git-based workflow.

## Fresh vs Established Project Detection

Before running setup or making broad structural changes, inspect the project state.

Treat the project as fresh when most of these are true:

- `raw/` is empty or contains only `README.md`.
- `wiki/` contains only starter pages such as `Project Index.md`, `Entity Page Template.md`, and `Contradictions and Tensions.md`.
- `wiki/Project Index.md` still contains placeholder starter text.
- There are no project-specific source pages or concept pages.

Treat the project as established when any of these are true:

- `raw/` contains real source files.
- `wiki/` contains project-specific pages.
- `wiki/Project Index.md` has been customized.
- `wiki/Contradictions and Tensions.md` contains real project tensions.

For a fresh project, it is acceptable to customize starter files after asking the setup questions. For an established project, summarize what you found and ask before restructuring, renaming, deleting, or rewriting major files.

## Setup Wizard Workflow

When the user asks for setup wizard behavior:

1. Detect whether the project looks fresh or established.
2. If established, say so and ask whether they want a cautious update rather than a fresh initialization.
3. Ask a short series of questions, preferably in one message:
   - What is the purpose of this project?
   - Who is the intended audience?
   - What kinds of source material will go in `raw/`?
   - What kinds of entities should the wiki track?
   - What kinds of contradictions, risks, decisions, or open questions matter?
   - Are there naming conventions, confidentiality rules, or source-citation preferences?
4. Use the answers to update project-specific starter guidance in `wiki/Project Index.md`, `wiki/Contradictions and Tensions.md`, and, when appropriate, `AGENTS.md`.
5. Create optional extra templates only when they match the user's answers, such as `Decision Template.md`, `Source Document Template.md`, or `Meeting Notes Template.md`.
6. Run the health check after edits.

Do not mix content from `examples/` into the active project unless the user explicitly asks.

## Health Check Workflow

If the user asks for `health check`, `lint wiki`, `check project health`, or similar, run:

```powershell
python scripts\check_wiki_health.py
```

If `python` is unavailable, use the bundled Codex Python runtime or perform the checks manually.

Report the important findings clearly, especially unresolved links, missing starter files, missing sections, or signs that example content leaked into the active wiki.

## Page Expectations

Concept and source pages should usually include:

- `## Summary`
- `## Explanation`
- `## Related Links`
- `## Source Documents`
- `## Contradictions and Tensions`

Keep pages concise enough to navigate, but specific enough that they are useful as project memory.

## Validation

After meaningful wiki edits, run `python scripts\check_wiki_health.py` before finishing whenever practical. At minimum, check for:

- unresolved `[[links]]`
- important sources missing from the index
- duplicated concept pages with slightly different names
- contradictions or tensions that should be added to the tensions page
- example content copied into the active wiki by accident
