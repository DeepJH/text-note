## Quick Start

为了简单，这里只讲全部安装。

### Step 0: Install the Claude Code

1. 打开[https://nodejs.org/zh-cn/download](https://nodejs.org/zh-cn/download)

2. 在系统的 Console 中执行一下网页中的安装命令。
    部分 Console 例如 zsh 不能解析 # 注释，需要删掉注释执行指令，例如：
    ```bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

    \. "$HOME/.nvm/nvm.sh"

    nvm install 24

    node -v

    npm -v

    ```

3. 如果`node -v；npm -v`正常显示版本号说明安装好了

4. 配置 npm 全局注册表，切换为国内镜像

    ```bash
    npm config set registry https://registry.npmmirror.com

    ```

5. 安装 Claude Code

    ```bash
    npm install -g @anthropic-ai/claude-code

    npm config get registry

    ```

### Step 1: Install the Plugin

1. 打开Claude Code

    ```shell
    claude

    ```

2. Install the Plugin

    ```shell
    /plugin marketplace add https://github.com/affaan-m/ECC
    /plugin install ecc@ecc

    ```

### Step 2: Install Rules Only If You Need Them

这可以增强效果。但是代价是要占用一些上下文窗口，并且轻微增加开销。如果你不明白，就选执行吧。

    ```shell
    git clone https://github.com/affaan-m/ECC.git
    cd ECC

    npm install

    mkdir -p ~/.claude/rules/ecc
    cp -R rules/common ~/.claude/rules/ecc/
    cp -R rules/typescript ~/.claude/rules/ecc/

    ```

### Step 3: Start Using

    That's it! You now have access to 67 agents, 271 skills, and 92 legacy command shims.

    ```shell
    # Skills are the primary workflow surface.
    # 技能（Skills）是主要的工作流入口。
    # Existing slash-style command names still work while ECC migrates off commands/.
    # 现有的斜杠式（slash-style）命令名称仍可正常工作，在 ECC 从 commands/ 目录迁移期间。

    # Plugin install uses the canonical namespaced form
    # 插件安装使用规范的命名空间形式：
   
    /ecc:plan "Add user authentication"

    # Manual install keeps the shorter slash form:
    # 手动安装则保留较短的斜杠形式：

    # /plan "Add user authentication"

    # Check available commands
    # 查看可用命令：

    /plugin list ecc@ecc
    
    ```

### Step 4: Multi-model commands require additional setup

WARNING: `multi-*` commands are not covered by the base plugin/rules install above.
To use `/multi-plan`, `/multi-execute`, `/multi-backend`, `/multi-frontend`, and `/multi-workflow`, you must also install the `ccg-workflow` runtime.
Initialize it with `npx ccg-workflow`.
That runtime provides the external dependencies these commands expect, including:

- `~/.claude/bin/codeagent-wrapper`
- `~/.claude/.ccg/prompts/*`

Without `ccg-workflow`, these `multi-*` commands will not run correctly.

### Step 5: See all ECC Components

- npm run dashboard
    
    1. go to local ECC repo
    
    2. run `npm run dashboard`

- tree
    
    1. go to local ECC repo
    
    2. run `tree`

    3. what's Inside

    ```text
    ECC/
    |-- .claude-plugin/   # Plugin and marketplace manifests
    |   |-- plugin.json         # Plugin metadata and component paths
    |   |-- marketplace.json    # Marketplace catalog for /plugin marketplace add
    |
    |-- agents/           # 67 specialized subagents for delegation
    |   |-- planner.md           # Feature implementation planning
    |   |-- architect.md         # System design decisions
    |   |-- tdd-guide.md         # Test-driven development
    |   |-- code-reviewer.md     # Quality and security review
    |   |-- security-reviewer.md # Vulnerability analysis
    |   |-- build-error-resolver.md
    |   |-- e2e-runner.md        # Playwright E2E testing
    |   |-- refactor-cleaner.md  # Dead code cleanup
    |   |-- doc-updater.md       # Documentation sync
    |   |-- docs-lookup.md       # Documentation/API lookup
    |   |-- chief-of-staff.md    # Communication triage and drafts
    |   |-- loop-operator.md     # Autonomous loop execution
    |   |-- harness-optimizer.md # Harness config tuning
    |   |-- cpp-reviewer.md      # C++ code review
    |   |-- cpp-build-resolver.md # C++ build error resolution
    |   |-- fsharp-reviewer.md   # F# functional code review
    |   |-- go-reviewer.md       # Go code review
    |   |-- go-build-resolver.md # Go build error resolution
    |   |-- python-reviewer.md   # Python code review
    |   |-- database-reviewer.md # Database/Supabase review
    |   |-- typescript-reviewer.md # TypeScript/JavaScript code review
    |   |-- java-reviewer.md     # Java/Spring Boot code review
    |   |-- java-build-resolver.md # Java/Maven/Gradle build errors
    |   |-- kotlin-reviewer.md   # Kotlin/Android/KMP code review
    |   |-- kotlin-build-resolver.md # Kotlin/Gradle build errors
    |   |-- harmonyos-app-resolver.md # HarmonyOS/ArkTS app development
    |   |-- rust-reviewer.md     # Rust code review
    |   |-- rust-build-resolver.md # Rust build error resolution
    |   |-- pytorch-build-resolver.md # PyTorch/CUDA training errors
    |   |-- mle-reviewer.md      # Production ML pipeline, eval, serving, and monitoring review
    |
    |-- skills/           # Workflow definitions and domain knowledge
    |   |-- coding-standards/           # Language best practices
    |   |-- clickhouse-io/              # ClickHouse analytics, queries, data engineering
    |   |-- backend-patterns/           # API, database, caching patterns
    |   |-- frontend-patterns/          # React, Next.js patterns
    |   |-- frontend-slides/            # HTML slide decks and PPTX-to-web presentation workflows (NEW)
    |   |-- article-writing/            # Long-form writing in a supplied voice without generic AI tone (NEW)
    |   |-- content-engine/             # Multi-platform social content and repurposing workflows (NEW)
    |   |-- market-research/            # Source-attributed market, competitor, and investor research (NEW)
    |   |-- investor-materials/         # Pitch decks, one-pagers, memos, and financial models (NEW)
    |   |-- investor-outreach/          # Personalized fundraising outreach and follow-up (NEW)
    |   |-- continuous-learning/        # Legacy v1 Stop-hook pattern extraction
    |   |-- continuous-learning-v2/     # Instinct-based learning with confidence scoring
    |   |-- iterative-retrieval/        # Progressive context refinement for subagents
    |   |-- strategic-compact/          # Manual compaction suggestions (Longform Guide)
    |   |-- tdd-workflow/               # TDD methodology
    |   |-- security-review/            # Security checklist
    |   |-- eval-harness/               # Verification loop evaluation (Longform Guide)
    |   |-- verification-loop/          # Continuous verification (Longform Guide)
    |   |-- videodb/                   # Video and audio: ingest, search, edit, generate, stream (NEW)
    |   |-- golang-patterns/            # Go idioms and best practices
    |   |-- golang-testing/             # Go testing patterns, TDD, benchmarks
    |   |-- cpp-coding-standards/         # C++ coding standards from C++ Core Guidelines (NEW)
    |   |-- cpp-testing/                # C++ testing with GoogleTest, CMake/CTest (NEW)
    |   |-- django-patterns/            # Django patterns, models, views (NEW)
    |   |-- django-security/            # Django security best practices (NEW)
    |   |-- django-tdd/                 # Django TDD workflow (NEW)
    |   |-- django-verification/        # Django verification loops (NEW)
    |   |-- laravel-patterns/           # Laravel architecture patterns (NEW)
    |   |-- laravel-security/           # Laravel security best practices (NEW)
    |   |-- laravel-tdd/                # Laravel TDD workflow (NEW)
    |   |-- laravel-verification/       # Laravel verification loops (NEW)
    |   |-- python-patterns/            # Python idioms and best practices (NEW)
    |   |-- python-testing/             # Python testing with pytest (NEW)
    |   |-- quarkus-patterns/            # Java Quarkus patterns (NEW)
    |   |-- quarkus-security/            # Quarkus security (NEW)
    |   |-- quarkus-tdd/                 # Quarkus TDD (NEW)
    |   |-- quarkus-verification/        # Quarkus verification (NEW)
    |   |-- springboot-patterns/        # Java Spring Boot patterns (NEW)
    |   |-- springboot-security/        # Spring Boot security (NEW)
    |   |-- springboot-tdd/             # Spring Boot TDD (NEW)
    |   |-- springboot-verification/    # Spring Boot verification (NEW)
    |   |-- configure-ecc/              # Interactive installation wizard (NEW)
    |   |-- security-scan/              # AgentShield security auditor integration (NEW)
    |   |-- java-coding-standards/     # Java coding standards (NEW)
    |   |-- jpa-patterns/              # JPA/Hibernate patterns (NEW)
    |   |-- postgres-patterns/         # PostgreSQL optimization patterns (NEW)
    |   |-- nutrient-document-processing/ # Document processing with Nutrient API (NEW)
    |   |-- docs/examples/project-guidelines-template.md  # Template for project-specific skills
    |   |-- database-migrations/         # Migration patterns (Prisma, Drizzle, Django, Go) (NEW)
    |   |-- api-design/                  # REST API design, pagination, error responses (NEW)
    |   |-- deployment-patterns/         # CI/CD, Docker, health checks, rollbacks (NEW)
    |   |-- docker-patterns/            # Docker Compose, networking, volumes, container security (NEW)
    |   |-- e2e-testing/                 # Playwright E2E patterns and Page Object Model (NEW)
    |   |-- content-hash-cache-pattern/  # SHA-256 content hash caching for file processing (NEW)
    |   |-- cost-aware-llm-pipeline/     # LLM cost optimization, model routing, budget tracking (NEW)
    |   |-- regex-vs-llm-structured-text/ # Decision framework: regex vs LLM for text parsing (NEW)
    |   |-- swift-actor-persistence/     # Thread-safe Swift data persistence with actors (NEW)
    |   |-- swift-protocol-di-testing/   # Protocol-based DI for testable Swift code (NEW)
    |   |-- search-first/               # Research-before-coding workflow (NEW)
    |   |-- skill-stocktake/            # Audit skills and commands for quality (NEW)
    |   |-- liquid-glass-design/         # iOS 26 Liquid Glass design system (NEW)
    |   |-- foundation-models-on-device/ # Apple on-device LLM with FoundationModels (NEW)
    |   |-- swift-concurrency-6-2/       # Swift 6.2 Approachable Concurrency (NEW)
    |   |-- mle-workflow/               # Production ML data contracts, evals, deployment, monitoring (NEW)
    |   |-- perl-patterns/             # Modern Perl 5.36+ idioms and best practices (NEW)
    |   |-- perl-security/             # Perl security patterns, taint mode, safe I/O (NEW)
    |   |-- perl-testing/              # Perl TDD with Test2::V0, prove, Devel::Cover (NEW)
    |   |-- autonomous-loops/           # Autonomous loop patterns: sequential pipelines, PR loops, DAG orchestration (NEW)
    |   |-- plankton-code-quality/      # Write-time code quality enforcement with Plankton hooks (NEW)
    |   |-- codehealth-mcp/             # Optional CodeScene Code Health MCP skill (opt-in; not enabled by default) (NEW)
    |
    |-- commands/         # Maintained slash-entry compatibility; prefer skills/
    |   |-- plan.md             # /plan - Implementation planning
    |   |-- code-review.md      # /code-review - Quality review
    |   |-- build-fix.md        # /build-fix - Fix build errors
    |   |-- refactor-clean.md   # /refactor-clean - Dead code removal
    |   |-- quality-gate.md     # /quality-gate - Verification gate
    |   |-- learn.md            # /learn - Extract patterns mid-session (Longform Guide)
    |   |-- learn-eval.md       # /learn-eval - Extract, evaluate, and save patterns (NEW)
    |   |-- checkpoint.md       # /checkpoint - Save verification state (Longform Guide)
    |   |-- setup-pm.md         # /setup-pm - Configure package manager
    |   |-- go-review.md        # /go-review - Go code review (NEW)
    |   |-- go-test.md          # /go-test - Go TDD workflow (NEW)
    |   |-- go-build.md         # /go-build - Fix Go build errors (NEW)
    |   |-- skill-create.md     # /skill-create - Generate skills from git history (NEW)
    |   |-- instinct-status.md  # /instinct-status - View learned instincts (NEW)
    |   |-- instinct-import.md  # /instinct-import - Import instincts (NEW)
    |   |-- instinct-export.md  # /instinct-export - Export instincts (NEW)
    |   |-- evolve.md           # /evolve - Cluster instincts into skills
    |   |-- prune.md            # /prune - Delete expired pending instincts (NEW)
    |   |-- pm2.md              # /pm2 - PM2 service lifecycle management (NEW)
    |   |-- multi-plan.md       # /multi-plan - Multi-agent task decomposition (NEW)
    |   |-- multi-execute.md    # /multi-execute - Orchestrated multi-agent workflows (NEW)
    |   |-- multi-backend.md    # /multi-backend - Backend multi-service orchestration (NEW)
    |   |-- multi-frontend.md   # /multi-frontend - Frontend multi-service orchestration (NEW)
    |   |-- multi-workflow.md   # /multi-workflow - General multi-service workflows (NEW)
    |   |-- sessions.md         # /sessions - Session history management
    |   |-- test-coverage.md    # /test-coverage - Test coverage analysis
    |   |-- update-docs.md      # /update-docs - Update documentation
    |   |-- update-codemaps.md  # /update-codemaps - Update codemaps
    |   |-- python-review.md    # /python-review - Python code review (NEW)
    |-- legacy-command-shims/   # Opt-in archive for retired shims such as /tdd and /eval
    |   |-- tdd.md              # /tdd - Prefer the tdd-workflow skill
    |   |-- e2e.md              # /e2e - Prefer the e2e-testing skill
    |   |-- eval.md             # /eval - Prefer the eval-harness skill
    |   |-- verify.md           # /verify - Prefer the verification-loop skill
    |   |-- orchestrate.md      # /orchestrate - Prefer dmux-workflows or multi-workflow
    |
    |-- rules/            # Always-follow guidelines (copy to ~/.claude/rules/ecc/)
    |   |-- README.md            # Structure overview and installation guide
    |   |-- common/              # Language-agnostic principles
    |   |   |-- coding-style.md    # Immutability, file organization
    |   |   |-- git-workflow.md    # Commit format, PR process
    |   |   |-- testing.md         # TDD, 80% coverage requirement
    |   |   |-- performance.md     # Model selection, context management
    |   |   |-- patterns.md        # Design patterns, skeleton projects
    |   |   |-- hooks.md           # Hook architecture, TodoWrite
    |   |   |-- agents.md          # When to delegate to subagents
    |   |   |-- security.md        # Mandatory security checks
    |   |-- typescript/          # TypeScript/JavaScript specific
    |   |-- python/              # Python specific
    |   |-- golang/              # Go specific
    |   |-- swift/               # Swift specific
    |   |-- php/                 # PHP specific (NEW)
    |   |-- arkts/               # HarmonyOS / ArkTS specific
    |
    |-- hooks/            # Trigger-based automations
    |   |-- README.md                 # Hook documentation, recipes, and customization guide
    |   |-- hooks.json                # All hooks config (PreToolUse, PostToolUse, Stop, etc.)
    |   |-- memory-persistence/       # Session lifecycle hooks (Longform Guide)
    |   |-- strategic-compact/        # Compaction suggestions (Longform Guide)
    |
    |-- scripts/          # Cross-platform Node.js scripts (NEW)
    |   |-- lib/                     # Shared utilities
    |   |   |-- utils.js             # Cross-platform file/path/system utilities
    |   |   |-- package-manager.js   # Package manager detection and selection
    |   |-- hooks/                   # Hook implementations
    |   |   |-- session-start.js     # Load context on session start
    |   |   |-- session-end.js       # Save state on session end
    |   |   |-- pre-compact.js       # Pre-compaction state saving
    |   |   |-- suggest-compact.js   # Strategic compaction suggestions
    |   |   |-- evaluate-session.js  # Extract patterns from sessions
    |   |-- setup-package-manager.js # Interactive PM setup
    |
    |-- tests/            # Test suite (NEW)
    |   |-- lib/                     # Library tests
    |   |-- hooks/                   # Hook tests
    |   |-- run-all.js               # Run all tests
    |
    |-- contexts/         # Dynamic system prompt injection contexts (Longform Guide)
    |   |-- dev.md              # Development mode context
    |   |-- review.md           # Code review mode context
    |   |-- research.md         # Research/exploration mode context
    |
    |-- examples/         # Example configurations and sessions
    |   |-- CLAUDE.md             # Example project-level config
    |   |-- user-CLAUDE.md        # Example user-level config
    |   |-- saas-nextjs-CLAUDE.md   # Real-world SaaS (Next.js + Supabase + Stripe)
    |   |-- go-microservice-CLAUDE.md # Real-world Go microservice (gRPC + PostgreSQL)
    |   |-- django-api-CLAUDE.md      # Real-world Django REST API (DRF + Celery)
    |   |-- laravel-api-CLAUDE.md     # Real-world Laravel API (PostgreSQL + Redis) (NEW)
    |   |-- rust-api-CLAUDE.md        # Real-world Rust API (Axum + SQLx + PostgreSQL) (NEW)
    |
    |-- mcp-configs/      # MCP server configurations
    |   |-- mcp-servers.json    # GitHub, Supabase, Vercel, Railway, etc.
    |
    |-- ecc_dashboard.py  # Desktop GUI dashboard (Tkinter)
    |
    |-- assets/           # Assets for dashboard
    |   |-- images/
    |       |-- ecc-logo.png
    |
    |-- marketplace.json  # Self-hosted marketplace config (for /plugin marketplace add)

    ```    
    
### Step 6: Uninstall

1. 进入插件管理
    
    ```shell
    /plugin

    ```
2. 切换到 ecc ，按 d 删除

3. 删除 ~/.claude/rules/ecc/
    ```bash
    rm -rf ~/.claude/rules/ecc/
    
    ```
4. 查看 ~/.claude/plugins/marketplaces ， ecc 或者类似的项应该没了。
    查看 ~/.claude/rules/ecc/ ，它应该没了。 

5. 如果 4 ，则说明卸载成功。

## Running Tests

The plugin includes a comprehensive test suite:

```bash
# Run all tests
node tests/run-all.js

# Run individual test files
node tests/lib/utils.test.js
node tests/lib/package-manager.test.js
node tests/hooks/hooks.test.js

```