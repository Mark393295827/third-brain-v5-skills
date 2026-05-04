# Contributing to Third Brain V5 Skills

Thanks for considering contributing! This project aims to make personal knowledge compounding accessible to everyone.

## How to Contribute

### 1. Report Issues

Open an issue describing:
- What you tried
- What happened
- What you expected
- Your agent harness and version

### 2. Suggest Skills

Have a recurring workflow that should be a skill? Open an issue with:
- **When to use** — when should this skill activate?
- **What it should do** — step-by-step workflow
- **How to verify** — how do we know it works?

### 3. Submit Pull Requests

PRs are welcome! Please:

1. **Read the PR template** at `.github/PULL_REQUEST_TEMPLATE.md` (if exists) or follow:
2. **One skill per PR** — makes review faster
3. **Follow the Skill format**:
   ```yaml
   ---
   name: your-skill
   description: One-line description — when to use this skill
   ---
   ```
4. **Include Quality Gates** — every skill needs a completion checklist
5. **Test your skill** — describe how you verified it works

### Skill Standards

Every skill in this repo must have:

| Element | Required | Example |
|---------|----------|---------|
| YAML frontmatter | ✅ | `name:`, `description:` |
| When to Use | ✅ | List of trigger conditions |
| Clear Workflow | ✅ | Step-by-step instructions |
| Quality Gates | ✅ | Completion checklist |
| Anti-patterns | ✅ | Common mistakes |

### Code of Conduct

Be respectful, constructive, and patient. This is a learning project as much as a utility.
