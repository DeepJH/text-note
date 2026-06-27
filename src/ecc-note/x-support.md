## X Support

ECC is the **first plugin to maximize every major AI coding tool**. Here's how each harness compares:

| Feature | Claude Code           | Cursor IDE | Codex CLI | OpenCode | GitHub Copilot |
|---------|-----------------------|------------|-----------|----------|----------------|
| **Agents** | 67                    | Shared (AGENTS.md) | Shared (AGENTS.md) | 12 | N/A |
| **Commands** | 92                    | Shared | Instruction-based | 35 | 5 prompts |
| **Skills** | 271                   | Shared | 10 (native format) | 37 | Via instructions |
| **Hook Events** | 8 types               | 15 types | None yet | 11 types | None |
| **Hook Scripts** | 20+ scripts           | 16 scripts (DRY adapter) | N/A | Plugin hooks | N/A |
| **Rules** | 34 (common + lang)    | 34 (YAML frontmatter) | Instruction-based | 13 instructions | 1 always-on file |
| **Custom Tools** | Via hooks             | Via hooks | N/A | 6 native tools | N/A |
| **MCP Servers** | 14                    | Shared (mcp.json) | 7 (auto-merged via TOML parser) | Full | N/A |
| **Config Format** | settings.json         | hooks.json + rules/ | config.toml | opencode.json | copilot-instructions.md + settings.json |
| **Context File** | CLAUDE.md + AGENTS.md | AGENTS.md | AGENTS.md | AGENTS.md | copilot-instructions.md |
| **Secret Detection** | Hook-based            | beforeSubmitPrompt hook | Sandbox-based | Hook-based | Instruction-based |
| **Auto-Format** | PostToolUse hook      | afterFileEdit hook | N/A | file.edited hook | N/A |
| **Version** | Plugin | Plugin | Reference config | 2.0.0 | Instruction layer |

**Key architectural decisions:**
- **AGENTS.md** at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode — GitHub Copilot uses `.github/copilot-instructions.md` instead)
- **DRY adapter pattern** lets Cursor reuse Claude Code's hook scripts without duplication
- **Skills format** (SKILL.md with YAML frontmatter) works across Claude Code, Codex, and OpenCode
- Codex's lack of hooks is compensated by `AGENTS.md`, optional `model_instructions_file` overrides, and sandbox permissions