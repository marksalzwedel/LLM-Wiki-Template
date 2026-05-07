# Project Health Check

## Summary

Use this page to remember how to ask Codex to lint the active wiki and template structure.

## Explanation

The health check catches common maintenance problems before they build up: unresolved links, missing starter pages, missing sections, duplicate page names, and example material copied into the active wiki by accident.

## Codex Prompt

```text
Run a health check on this project.
Check unresolved wiki links, missing starter pages, missing required sections, duplicate concept pages, and whether example content has leaked into the active wiki.
```

## Script

From the top-level project folder, Codex can run:

```powershell
python scripts\check_wiki_health.py
```

## Related Links

- [[Project Index]]
- [[Setup Wizard]]
- [[Contradictions and Tensions]]
- [[Entity Page Template]]
