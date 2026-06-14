# SkillForge

**The agent-skills pack that actually works — auto-validated, zero broken references.**

Every skill here passes `forge validate` on every commit. No missing files, no malformed frontmatter, no dead directory paths. Drop them into Claude Code / Cursor and they just work.

---

## Why SkillForge?

Most skill packs break silently — files that don't exist, bad YAML, install steps that fail. SkillForge ships a **linter** so skills are guaranteed valid, plus a small set of **production-grade skills** focused on shipping and debugging real apps.

> Validated  •  Composable  •  Zero-config

## Quick Start (30 seconds)

```bash
git clone https://github.com/kunaltaydetayde7552-ship-it/skillforge
cp -r skillforge/skills/* ~/.claude/skills/   # or your agent's skills dir
```

Validate any skills folder:

```bash
python cli/forge.py validate ./skills
```

## Skills Included

| Skill | When it triggers |
|-------|------------------|
| `ship-web-app` | Deploy a web app safely with pre-flight checks |
| `debug-failing-test` | A test fails and you need root cause, not guesses |
| `safe-refactor` | Refactor without breaking behavior |
| `write-pr-description` | Generate a clear, reviewable PR description |
| `api-error-triage` | Diagnose a failing API call systematically |

## The Linter

`forge validate` catches the 5 most common skill breakages:
1. Referenced files that don't exist
2. Malformed / missing YAML frontmatter
3. Dead directory paths
4. Broken install commands
5. Missing trigger description

## Contributing

New skills welcome — they must pass `forge validate`. See CONTRIBUTING.md.

## License

MIT
