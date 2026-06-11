# Setup Wizard

## Summary

Use this page as a checklist when customizing a fresh copy of the template for a new project.

## Explanation

The setup wizard is a Codex-guided onboarding flow. It helps distinguish a fresh project from an established one, asks the right customization questions, and updates starter guidance without mixing example content into the active wiki.

For SharePoint-distributed copies, the wizard should first confirm the user is
working in their own copied project folder, not the read-only master template.
If OneDrive Files On-Demand is enabled, the copied project folder should be set
to **Always keep on this device** before Codex starts reading or editing files.

## Setup Questions

- What is the purpose of this project?
- Who is the intended audience?
- What source material will go in `raw/`?
- What kinds of entities should the wiki track?
- What kinds of contradictions, risks, decisions, or open questions matter?
- Are there naming conventions, confidentiality rules, or citation preferences?

## Codex Prompt

```text
Setup wizard: help me customize this project.
First determine whether it looks fresh or established.
Then ask the setup questions and update the starter wiki and agent guidance accordingly.
```

## SharePoint Copy Prompt

```text
I copied this template from SharePoint into my own project folder.
Help me verify that I am working in the copy, then run the setup wizard.
```

## Related Links

- [[Project Index]]
- [[Entity Page Template]]
- [[Contradictions and Tensions]]
- [[Project Health Check]]
