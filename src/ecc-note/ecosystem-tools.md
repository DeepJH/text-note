## Ecosystem Tools

与其他工具相连，例如 Github 。

### Skill Creator

- Local Analysis (Built-in)
    
    Use the /skill-create command for local analysis without external services:
    
    ```shell
    /skill-create                    # Analyze current repo
    /skill-create --instincts        # Also generate instincts for continuous-learning-v2
    
    ```

    This analyzes your git history locally and generates SKILL.md files.

- GitHub App (Advanced)

    For advanced features (10k+ commits, auto-PRs, team sharing):

    Install ECC Tools [GitHub App](https://github.com/apps/ecc-tools) | [ecc.tools](https://ecc.tools/)

    > notice: There are a bunch of limits if you don't spend money. Mainly are public repo gitHub app analysis only, 10 analyses per month, 200 commits per run. See deatail on ecc.tools. It's depends on you.

    ```shell
    # Comment on any issue:
    /ecc-tools analyze

    # Or run against a repo from the hosted app
    
    ```
    Both options create:

    - SKILL.md files - Ready-to-use skills for the active harness
    - Instinct collections - For continuous-learning-v2
    - Pattern extraction - Learns from your commit history

### AgentShield — Security Auditor

see [https://github.com/affaan-m/ecc#agentshield--security-auditor](https://github.com/affaan-m/ecc#agentshield--security-auditor)

### Continuous Learning v2

It is automatic.
see [https://github.com/affaan-m/ecc#continuous-learning-v2](https://github.com/affaan-m/ecc#continuous-learning-v2)