# Codex Obsidian Research Template

This project is a reusable template for turning a small collection of source documents into an Obsidian-style knowledge base with Codex. It is useful when you want an LLM assistant to read papers, reports, notes, or source material and create linked entity pages for concepts, source documents, contradictions, and reusable research patterns.

The current example uses foundational LLM papers, but the structure is meant to be copied and adapted to any domain.

## Folder Layout

```text
.
|-- raw/        Source documents to read, such as PDFs, text files, reports, or notes.
|-- wiki/       Generated Markdown entity pages for Obsidian or any Markdown reader.
|-- README.md   Instructions for using and customizing the template.
```

## Quick Start

1. Put your source documents in `raw/`.
2. Open this folder in Codex.
3. Ask Codex to read the files in `raw/` and build or update entity pages in `wiki/`.
4. Open the folder, or just the `wiki/` folder, as an Obsidian vault.
5. Start from the index page in `wiki/` and follow the `[[bracket links]]`.

For a fresh project, you can delete the example LLM pages in `wiki/` after reviewing the structure. Keep `wiki/Entity Page Template.md` if you want a reusable page pattern.

## GitHub Setup Tip

When creating or cloning a GitHub repository, make sure the repository root is the high-level project folder that contains `raw/`, `wiki/`, and `README.md`.

If GitHub Desktop or `git clone` creates a second folder inside the project, such as `ProjectName/ProjectName/`, the repository is one level too deep. This usually happens when you clone into an existing project folder instead of cloning into its parent folder.

The healthy shape is:

```text
ProjectName/
|-- .git/
|-- raw/
|-- wiki/
|-- README.md
```

The one-level-off shape is:

```text
ProjectName/
|-- raw/
|-- wiki/
|-- README.md
|-- ProjectName/
    |-- .git/
```

To fix it, move the nested `.git/` folder up into the high-level project folder, move any generated Git files such as `.gitattributes` up with it, then remove the now-empty nested folder.

## Recommended Codex Prompt

Use a prompt like this after adding your own files to `raw/`:

```text
Read the papers and notes under raw/ and create entity pages in wiki/.
For each key concept, create a Markdown file with:
- a summary
- an explanation
- related links using [[brackets]]
- source-paper links
- notes about contradictions, disagreements, or tensions between sources

Also create or update an index page and a contradictions page.
```

For an update pass, use:

```text
Read the new files in raw/ and update wiki/ without deleting existing notes.
Add new concept pages where needed, extend related links, and update the contradictions page.
```

## Page Pattern

Most concept pages should follow this shape:

```markdown
# Concept Name

## Summary

One or two sentences defining the concept.

## Explanation

How the concept works, why it matters, and how the sources use it.

## Related Links

- [[Another Concept]]
- [[Source Paper]]

## Source Papers

- [[Relevant Source]]

## Contradictions and Tensions

- Where sources disagree, revise one another, or use the concept differently.
```

The included `wiki/Entity Page Template.md` provides this same pattern inside the vault.

## Customizing the Template

Change the domain by replacing the files in `raw/`. Examples:

- Academic literature review
- Product research
- Legal or policy document comparison
- Medical-device design history
- Internal technical documentation
- Strategy memos
- Historical archive notes

Adjust the entity types to fit the domain. For example:

- For research papers: concepts, methods, datasets, metrics, limitations, contradictions.
- For product work: users, workflows, features, competitors, constraints, decisions.
- For legal or policy work: statutes, rules, obligations, exceptions, risks, precedents.
- For engineering docs: services, APIs, modules, failure modes, dependencies, runbooks.

## Obsidian Tips

- When opening this project in Obsidian, select the `wiki/` folder as the vault. Use the higher-level project folder in Codex so Codex can see both `raw/` and `wiki/`.
- Use `[[Page Name]]` links for concepts that deserve their own pages.
- Keep one concept per file when possible.
- Use an index page as the main map.
- Use a contradictions or tensions page to track disagreements across sources.
- Rename pages carefully; Obsidian can update links if configured to do so.
- Add tags only if they help your workflow. Links are usually more useful than broad tags.

## Quality Checks

After Codex updates the wiki, ask it to run a sanity pass:

```text
Check wiki/ for unresolved [[links]], missing required sections, duplicate concept pages, and source pages that are not linked from the index.
```

Useful checks include:

- Every important source has a page.
- Every key concept has a page.
- The index links to major clusters.
- The contradictions page captures real tensions, not just summaries.
- No `[[links]]` point to missing files.
- Pages distinguish source claims from interpretation.

## Suggested Workflow

1. Add or replace source files in `raw/`.
2. Ask Codex for a first-pass wiki.
3. Read the index and contradictions page.
4. Ask Codex to deepen weak areas or split overloaded pages.
5. Add your own notes in Obsidian.
6. When new sources arrive, ask Codex to update the vault incrementally.

## Notes for Future Users

This template is intentionally small. It does not require a database, build step, or web app. The source documents live in `raw/`, and the knowledge base lives in `wiki/`.

The best results come from asking Codex to preserve citations, compare sources explicitly, and avoid flattening disagreements into a single consensus summary.
