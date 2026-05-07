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

## Page Expectations

Concept and source pages should usually include:

- `## Summary`
- `## Explanation`
- `## Related Links`
- `## Source Documents`
- `## Contradictions and Tensions`

Keep pages concise enough to navigate, but specific enough that they are useful as project memory.

## Validation

After wiki edits, check for:

- unresolved `[[links]]`
- important sources missing from the index
- duplicated concept pages with slightly different names
- contradictions or tensions that should be added to the tensions page
