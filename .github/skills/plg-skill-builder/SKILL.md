---
name: plg-skill-builder
description: 'Create or deepen GitHub Copilot agent skills and custom agents in this repo. Use when asked to add a skill, agent profile, SKILL.md, or customize Copilot.'
argument-hint: '[skill-name]'
---

# PLG Skill Builder

## Locations
- Skills: `.github/skills/{name}/SKILL.md` plus optional `assets/`, `references/`, `scripts/`
- Agents: `.github/agents/{name}.md`
- Repo rules: AGENTS.md and `.github/copilot-instructions.md`

## SKILL.md rules
- YAML frontmatter: name (matches folder), description (keyword-rich, when to use, max 1024)
- Body under 500 lines; put templates in assets/
- Relative links to other skills with ./
- Procedure is numbered and file-path specific
- Include When to use + Done definition

## Agent profile rules
- Frontmatter name + description
- Body states which skills to load and what not to touch

## After creating a skill
Link it from workflow/copilot-first-session.md in a table of skills.
