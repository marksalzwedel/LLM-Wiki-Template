# Codex Obsidian Research Template

This repository is a clean starting point for projects where Codex reads source material and builds an Obsidian-style Markdown knowledge base.

Use the top-level project folder in Codex. Use the `wiki/` folder as the Obsidian vault.

## What This Template Gives You

```text
.
|-- raw/          Active source files for the current project.
|-- wiki/         Active Obsidian vault for the current project.
|-- examples/     Completed example material for reference.
|-- scripts/      Health-check and maintenance helpers.
|-- AGENTS.md     Instructions for future Codex sessions.
|-- README.md     Setup and workflow guide.
|-- README - Start Here.md
                  Short user-facing guide for copied SharePoint projects.
```

The active starter wiki is intentionally small:

- `wiki/Project Index.md`
- `wiki/Entity Page Template.md`
- `wiki/Contradictions and Tensions.md`
- `wiki/Setup Wizard.md`
- `wiki/Project Health Check.md`

The completed LLM example has been moved out of the active vault:

- `examples/llm-raw/`
- `examples/llm-wiki/`

Use the example when you want to see what a finished vault can look like. Do not open it as the active project vault unless you are intentionally studying the example.

## Create a New Project From This Template

1. Copy the whole template folder.
2. Rename the copied folder to your new project name.
3. Open the copied folder and confirm it has this shape:

```text
Your Project/
|-- raw/
|-- wiki/
|-- examples/
|-- scripts/
|-- AGENTS.md
|-- README.md
```

4. Put project source files in `raw/`.
5. Keep the active notes in `wiki/`.

If your copy includes a `.git/` folder from the original template and you want a separate new repository, remove that `.git/` folder before creating the new repository. Keep `.git/` only if you intentionally want to preserve the old repository history and remote.

## Publish a SharePoint-Ready Template

Use this Git repository as the maintainer source of truth. When you want to give
non-software users a clean copyable template, publish a generated folder and
place that generated folder in a read-only SharePoint template library.

From the top-level project folder, run:

```powershell
python scripts\publish_sharepoint_template.py
```

The script creates:

```text
dist/Codex-SharePoint-Template/
```

The published folder excludes Git metadata, local caches, virtual environments,
logs, temporary files, and generated output. It keeps the project files users
need, including:

```text
AGENTS.md
README.md
README - Start Here.md
raw/
wiki/
scripts/
examples/
```

Recommended maintainer flow:

1. Update this Git-maintained template.
2. Run the wiki health check.
3. Run `python scripts\publish_sharepoint_template.py`.
4. Review `dist/Codex-SharePoint-Template/`.
5. Copy or sync that generated folder into the read-only SharePoint template library.

Recommended user flow from SharePoint:

1. Copy the whole published template folder into a personal or team SharePoint-synced workspace.
2. Rename the copied folder for the new project.
3. If OneDrive Files On-Demand is enabled, right-click the copied project folder and choose **Always keep on this device**.
4. Open the copied top-level folder in Codex.
5. Ask Codex for:

```text
setup wizard
```

Do not ask normal users to work in the read-only master template folder. The
published SharePoint folder is a starting point, not the project workspace.

## Create a GitHub Repository

You can use GitHub, GitHub Desktop, or another source-control or configuration-management tool if your team prefers something else.

For GitHub Desktop, the safest flow for an existing folder is:

1. Open PowerShell in the top-level project folder.
2. Initialize Git there:

```powershell
git init
```

3. Open GitHub Desktop.
4. Choose **File -> Add local repository...**
5. Select the top-level project folder, not `raw/`, not `wiki/`, and not the parent folder.
6. Commit the initial files.
7. Click **Publish repository** to create the GitHub repository.

This avoids the common nested-folder problem.

## Avoid the GitHub Desktop Folder Trap

In GitHub Desktop, **Create New Repository** treats:

- **Name** as the new folder it will create
- **Local path** as the parent folder where that new folder will be created

So if you already have:

```text
Documents/GitHub/My Project/
```

and then create a repository with:

```text
Name: My Project
Local path: Documents/GitHub/My Project
```

you can accidentally get:

```text
Documents/GitHub/My Project/My Project/.git
```

The healthy shape is:

```text
My Project/
|-- .git/
|-- raw/
|-- wiki/
|-- README.md
```

If you ever see this one-level-off shape:

```text
My Project/
|-- raw/
|-- wiki/
|-- README.md
|-- My Project/
    |-- .git/
```

fix it by moving the nested `.git/` folder up into the top-level project folder, moving any generated files such as `.gitattributes` with it, and deleting the now-empty nested folder.

## Open the Project in Codex

Open the top-level project folder in Codex:

```text
Your Project/
```

Codex needs the top-level folder because it should be able to see both:

- `raw/` source files
- `wiki/` Markdown notes

Do not open only `wiki/` in Codex unless you are doing note-only edits.

## Ask Codex for Help

You can type:

```text
help
```

Codex should not start editing files from that generic request. The agent instructions in `AGENTS.md` tell Codex to first route the request by asking whether you want to:

- initialize or customize a fresh project
- add new source material
- update or clean the wiki
- run a project health check
- troubleshoot GitHub, Codex, or Obsidian setup

For a guided setup, use:

```text
setup wizard
```

or:

```text
customize this template
```

Codex will first check whether the project looks fresh or already established. It should be cautious with established projects and avoid broad restructuring without confirmation.

## Open the Vault in Obsidian

When Obsidian asks you to open a folder as a vault, select:

```text
Your Project/wiki/
```

Do not select the top-level project folder as the Obsidian vault unless you intentionally want `raw/`, `examples/`, and project scaffolding to appear in Obsidian.

## First Codex Prompt for a New Project

For a guided setup, start with:

```text
setup wizard
```

Codex will ask about the project purpose, audience, source materials, entity types, important tensions, naming conventions, and citation preferences. It can then customize `wiki/Project Index.md`, `wiki/Contradictions and Tensions.md`, and `AGENTS.md`.

After adding source files to `raw/`, ask Codex:

```text
Read the source files under raw/ and create or update entity pages in wiki/.
For each key concept, source, decision, or entity, create a Markdown page with:
- a summary
- an explanation
- related links using [[brackets]]
- source-document links
- contradictions, disagreements, tensions, or open questions

Update Project Index.md and Contradictions and Tensions.md.
Do not mix example content from examples/ into the active wiki.
```

## Update Prompt After Adding More Sources

When you add new source material later, ask:

```text
Read the new or changed files in raw/ and update wiki/ incrementally.
Preserve existing user-written notes.
Add new pages where needed, extend related links, and update Contradictions and Tensions.md.
Then check for unresolved [[links]] and duplicate concept pages.
```

## Page Pattern

Most concept and source pages should follow this pattern:

```markdown
# Page Name

## Summary

One or two sentences defining the page.

## Explanation

How it works, why it matters, and how the sources use it.

## Related Links

- [[Related Page]]

## Source Documents

- [[Source Page]]

## Contradictions and Tensions

- Where sources disagree, revise one another, or leave important questions unresolved.
```

## Maintaining the Wiki

Use `wiki/Project Index.md` as the main map.

Use `wiki/Contradictions and Tensions.md` for:

- source disagreements
- term conflicts
- open questions
- changing interpretations as new sources are added

Keep one durable concept per page when possible. Prefer clear page names over clever names. If two pages describe the same idea, merge them and update links.

## Quality Checks

After major updates, ask Codex:

```text
health check
```

Codex should run:

```powershell
python scripts\check_wiki_health.py
```

Useful checks:

- Every important source has a page or index entry.
- Every important concept has a page.
- The index links to the major clusters.
- The tensions page captures real disagreements, not just summaries.
- Pages distinguish source claims from interpretation.
- Example content stays under `examples/` unless intentionally copied.

You can also run the script yourself from the top-level project folder:

```powershell
python scripts\check_wiki_health.py
```

## Customizing the Template

This structure works for many project types:

- academic literature reviews
- product research
- legal or policy comparison
- medical-device design history
- internal technical documentation
- strategy memos
- historical archive work
- customer discovery notes
- competitive analysis

Adjust the entity types to fit the project:

- Research: concepts, methods, datasets, metrics, limitations, contradictions.
- Product: users, workflows, features, competitors, constraints, decisions.
- Legal or policy: statutes, rules, obligations, exceptions, risks, precedents.
- Engineering: services, APIs, modules, failure modes, dependencies, runbooks.

## Practical Notes

- Codex works from the top-level folder.
- Obsidian works from `wiki/`.
- Source files go in `raw/`.
- Generated and hand-edited notes go in `wiki/`.
- Examples stay in `examples/`.
- Commit changes regularly after meaningful wiki updates.
