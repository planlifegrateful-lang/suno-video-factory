# Copilot operating kit

## Install
- macOS: `brew install --cask github-copilot-app`
- Latest: https://github.com/github/app/releases/latest
- Sign in as planlifegrateful-lang
- Settings → Experimental → Impeccable
- Customize → Skills: confirm repo skills are listed
- Agent picker: reel-producer / content-ops / offer-architect

## Skills in this repo
| Skill | Use when |
|---|---|
| plg-brand-voice | any copy |
| plg-reel-pack | track → reel pack |
| plg-job-pipeline | jobs/ + manifests |
| plg-content-calendar | posting plans |
| plg-sales-pack | Gumroad/Payhip |
| plg-skill-builder | new skills/agents |

## Agents
| Agent | File |
|---|---|
| reel-producer | .github/agents/reel-producer.md |
| content-ops | .github/agents/content-ops.md |
| offer-architect | .github/agents/offer-architect.md |

## Session 1
Start FROM issue #1 with agent **reel-producer**.

## Session 2
Issue #2 with agent **content-ops**.

## Session 3
Issue #3 with agent **reel-producer**.

## Invocation examples
```
/agent reel-producer
Build a reel pack for theme: waking up with gratitude instead of anxiety.
Use plg-reel-pack.
```

```
/agent content-ops
Open a job folder for today's Grateful Morning reel. Draft only.
```

```
/agent offer-architect
Turn ummah-anthems-pack + this factory into a $17 Gumroad listing draft under offers/.
```
