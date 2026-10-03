# GitHub `codex` 与 `agent` 开源装备速查清单（Simple CheatSheet）

> **速查指南**：按“你想用它干啥”大白话分类，完整收录 2026-10-03 GitHub `codex` 与 `agent` Top 10 页去重后的全部 **178 个** 核心开源项目。
> **特点**：无废话、大白话、重在实操。按 `Ctrl + F` 搜功能或关键词即可快速定位。

---

## 目录速览（你想干什么？）

- [🛠️ 1. 想找 AI 帮你写代码、改 Bug、跑命令行（编程智能体 & 终端助手）](#1-想找-ai-帮你写代码-改-bug-跑命令行-编程智能体-终端助手)（共 51 个项目）
- [📏 2. 觉得 AI 瞎写代码、想给它立规矩提质感（工程规范、技能库 & 审美注入）](#2-觉得-ai-瞎写代码-想给它立规矩提质感-工程规范-技能库-审美注入)（共 45 个项目）
- [🧠 3. AI 聊几句就失忆、想让它记住整个代码库（长期记忆 & 架构图谱）](#3-ai-聊几句就失忆-想让它记住整个代码库-长期记忆-架构图谱)（共 32 个项目）
- [🎛️ 4. 想把多个智能体组队协同干大活（多智能体框架 & 工作流编排）](#4-想把多个智能体组队协同干大活-多智能体框架-工作流编排)（共 13 个项目）
- [🌐 5. 想让 AI 自动联网搜资料、爬网页（全网调研 & 浏览器自动化）](#5-想让-ai-自动联网搜资料-爬网页-全网调研-浏览器自动化)（共 13 个项目）
- [🔄 6. 手头一堆 API Key 想一键切换、集中管理（模型切换器 & 桌面网关）](#6-手头一堆-api-key-想一键切换-集中管理-模型切换器-桌面网关)（共 9 个项目）
- [🛡️ 7. 怕 AI 乱删库乱执行命令、想要安全评测（安全沙箱 & 评测门禁）](#7-怕-ai-乱删库乱执行命令-想要安全评测-安全沙箱-评测门禁)（共 6 个项目）
- [🏢 8. 垂直场景专用智能体（特定行业 & 业务自动化）](#8-垂直场景专用智能体-特定行业-业务自动化)（共 5 个项目）
- [🎨 9. 想让 AI 直接出前端设计、做原型和美化 UI（设计与多模态创意）](#9-想让-ai-直接出前端设计-做原型和美化-ui-设计与多模态创意)（共 4 个项目）

---

## 🛠️ 1. 想找 AI 帮你写代码、改 Bug、跑命令行（编程智能体 & 终端助手）
> 💡 **怎么用**：核心用途：在终端、IDE 里直接叫 AI 帮你写业务代码、修 bug、看工程、甚至多分支自动探索。

### 1. [anomalyco/opencode](https://github.com/anomalyco/opencode) `⭐ 211,545`
- **能帮你干啥**：它为你提供了一个开源跨平台的 AI 编程助手，能够通过规划与构建双 Agent 模式，帮你安全高效地理解分析代码库并自动化完成编码与开发任务。
- **项目一句话**：The open source coding agent.
- **搜索标签**：`agent`

### 2. [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) `⭐ 195,236`
- **能帮你干啥**：为你提供一个基于 Rust 实现的本地 CLI 智能体工具，并作为探索完全由 AI Agent 无人工干预自主维护软件项目的实战参考。
- **项目一句话**：An agent-managed museum exhibit, built in Rust with Gajae-Code / LazyCodex — developed and maintained with no human intervention.
- **搜索标签**：`agent`

### 3. [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) `⭐ 188,061`
- **能帮你干啥**：它能帮我免去代理轮换、动态渲染和反爬等复杂底层配置，直接将任意网页转换为适合大模型消费的纯净 Markdown 与结构化数据，让我的 AI 智能体轻松具备实时联网检索与交互能力。
- **项目一句话**：Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥
- **搜索标签**：`agent`

### 4. [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) `⭐ 159,008`
- **能帮你干啥**：为我提供了一站式、成体系的 Java 后端与通用技术知识库及备考方案，帮助我告别碎片化复习，高效突破技术面试并系统夯实后端核心开发能力。
- **项目一句话**：Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发
- **搜索标签**：`agent`

### 5. [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) `⭐ 152,161`
- **能帮你干啥**：它可以防止 AI 编程助手过度工程化，引导其优先复用现有与原生功能生成极简且安全的代码，从而为你显著减少冗余代码并降低 Token 成本与开发耗时。
- **项目一句话**：Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **搜索标签**：`agent`

### 6. [openai/codex](https://github.com/openai/codex) `⭐ 127,679`
- **能帮你干啥**：让你无需脱离本地命令行环境，即可直接调用 OpenAI 的轻量级智能编程代理高效处理编码任务，并能无缝复用现有的 ChatGPT 订阅权益。
- **项目一句话**：Lightweight coding agent that runs in your terminal
- **搜索标签**：`codex & agent`

### 7. [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) `⭐ 119,303`
- **能帮你干啥**：只需将现成的知名产品 DESIGN.md 放入项目，就能让 AI 编程助手零门槛为你生成视觉风格高度一致且专业的高质量 UI 界面。
- **项目一句话**：A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **搜索标签**：`agent`

### 8. [earendil-works/pi](https://github.com/earendil-works/pi) `⭐ 111,881`
- **能帮你干啥**：它为你提供了一个极简且高度可扩展的 AI 编码 Agent 工具箱，让你无需迁就固化框架，即可按自身开发习惯自由定制扩展，轻松打造完全贴合个人工作流的专属智能编程助手或集成应用。
- **项目一句话**：AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **搜索标签**：`agent`

### 9. [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) `⭐ 107,220`
- **能帮你干啥**：让你无需离开终端即可免费使用强大的 Gemini 大模型及内置工具，高效完成代码分析编辑、故障排查与命令行任务自动化。
- **项目一句话**：An open-source AI agent that brings the power of Gemini directly into your terminal.
- **搜索标签**：`agent`

### 10. [stablyai/orca](https://github.com/stablyai/orca) `⭐ 84,062`
- **能帮你干啥**：让你能够在统一工作台中并行调度多个 AI 编程 Agent 在独立 Git 工作树中同时开发与择优合并，并支持跨端监控，成倍提升编码试错与交付效率。
- **项目一句话**：Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and remote runtime.
- **搜索标签**：`codex & agent`

### 11. [lobehub/lobehub](https://github.com/lobehub/lobehub) `⭐ 82,957`
- **能帮你干啥**：它能帮你统一搭建、调度并协同管理专属的 AI 智能体团队，实现 7×24 小时自主运转，让你无需时刻在线即可获得持续高效的自动化生产力。
- **项目一句话**：🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.
- **搜索标签**：`agent`

### 12. [opendatalab/MinerU](https://github.com/opendatalab/MinerU) `⭐ 81,023`
- **能帮你干啥**：它可以帮我将PDF、图片及各类Office复杂文档（含公式、表格与排版）精准解析，转化为大模型与智能体工作流可直接消费的高质量结构化Markdown和JSON。
- **项目一句话**：Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows.
- **搜索标签**：`agent`

### 13. [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) `⭐ 77,935`
- **能帮你干啥**：帮助你从零构建类 Claude Code 的极简智能体运行底座（Harness），彻底摆脱脆弱的工作流胶水代码，掌握释放大模型自主解决复杂任务潜力的核心工程架构能力。
- **项目一句话**：Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1
- **搜索标签**：`agent`

### 14. [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) `⭐ 76,354`
- **能帮你干啥**：它能为我提供一套零基础友好的系统化实战教程与配套代码，帮助我快速跨越技术门槛，掌握从概念到工程落地构建 AI 智能体的核心开发技能。
- **项目一句话**：18 Lessons to Get Started Building AI Agents
- **搜索标签**：`agent`

### 15. [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB) `⭐ 73,776`
- **能帮你干啥**：它能帮我通过“一次连接、处处消费”的统一数据架构，一站式整合各类公开、授权与专有数据源，并无缝分发给 Python 量化分析、REST API 以及 AI Agent 等多样化下游应用。
- **项目一句话**：Open Data Platform for analysts, quants and AI agents.
- **搜索标签**：`agent`

### 16. [cline/cline](https://github.com/cline/cline) `⭐ 69,752`
- **能帮你干啥**：为你提供一个贯穿 IDE、终端与桌面环境的开源自主编程智能体，能够自动跨文件修改代码、执行命令并排查修复报错，大幅解放日常编码与调试的精力。
- **项目一句话**：Autonomous coding agent as an SDK, IDE extension, or CLI assistant.
- **搜索标签**：`agent`

### 17. [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) `⭐ 68,495`
- **能帮你干啥**：让你能够无缝兼容现有 Codex 与编辑器生态，通过针对性优化的架构让低成本开源模型发挥出极致的编程与系统自动化执行能力。
- **项目一句话**：A coding agent for open models like Kimi K3 and GLM 5.3
- **搜索标签**：`agent`

### 18. [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) `⭐ 66,680`
- **能帮你干啥**：它可以让你无需繁琐配置即可快速搭建支持任意本地或云端模型的私有化全功能 ChatGPT，在完全掌控数据隐私的前提下高效实现文档知识库问答与 AI Agent 自动化工作流。
- **项目一句话**：Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience 
- **搜索标签**：`agent`

### 19. [warpdotdev/warp](https://github.com/warpdotdev/warp) `⭐ 65,350`
- **能帮你干啥**：它将传统终端升级为智能体开发环境，让你能直接在命令行中无缝调度各类 AI 编程 Agent 自动化完成开发任务，大幅提升编码与工程效率。
- **项目一句话**：Warp is an agentic development environment, born out of the terminal.
- **搜索标签**：`agent`

### 20. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) `⭐ 56,035`
- **能帮你干啥**：它能让我直接借助熟悉的 HTML、CSS 及 AI 编程智能体，以代码化方式自动化渲染出确定性的高质量 MP4 视频，彻底解决传统视频制作流程繁琐且难以程序化扩展的痛点。
- **项目一句话**：Write HTML. Render video. Built for agents.
- **搜索标签**：`agent`

### 21. [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) `⭐ 55,485`
- **能帮你干啥**：它能让我通过直观的可视化拖拽界面，无需编写复杂代码即可快速构建、测试并部署专属的 AI 智能体与大模型工作流，极大降低开发门槛与时间成本。
- **项目一句话**：Build AI Agents, Visually
- **搜索标签**：`agent`

### 22. [aaif-goose/goose](https://github.com/aaif-goose/goose) `⭐ 54,887`
- **能帮你干啥**：它打破了传统 AI 仅能提供代码建议的局限，让我在本地桌面或终端中自由接入任意大模型，直接自主执行、编辑与测试代码，全自动化搞定开发调试与复杂工作流。
- **项目一句话**：an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM
- **搜索标签**：`agent`

### 23. [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) `⭐ 52,333`
- **能帮你干啥**：它能为你提供开箱即用的一站式跨平台桌面客户端，统一接入和对比主流云端与本地大模型，借助300多个内置助手及MCP生态全面聚合并提升个人AI生产力。
- **项目一句话**：AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs
- **搜索标签**：`codex & agent`

### 24. [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) `⭐ 52,145`
- **能帮你干啥**：通过系统化的理论全书与109个配套实操实验，帮助你成体系地掌握AI Agent从底层架构设计到生产级工程落地的全流程实战能力。
- **项目一句话**：《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码
- **搜索标签**：`agent`

### 25. [multica-ai/multica](https://github.com/multica-ai/multica) `⭐ 51,865`
- **能帮你干啥**：它能将分散在终端里的各类 AI 编码 Agent 整合为看板上的协作队友，让你像给同事派发 Issue 一样自动指派、追踪和审查任务，彻底告别在多终端间充当保姆与重复同步上下文的繁琐负担。
- **项目一句话**：Make humans and AI agents work as one team — open-source and self-hostable.
- **搜索标签**：`agent`

### 26. [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) `⭐ 51,405`
- **能帮你干啥**：它可以将各类原本面向人类的软件转化为 Agent 原生的标准化命令行工具，让你能够直接借助 AI 智能体操控任意软件并自动化执行复杂工作流。
- **项目一句话**："CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/
- **搜索标签**：`agent`

### 27. [tldraw/tldraw](https://github.com/tldraw/tldraw) `⭐ 50,719`
- **能帮你干啥**：它可以帮我免去从零自研复杂画布系统的成本，轻松在 React 应用中快速构建出高度可定制、支持多人实时协同及 AI 交互的专业级无限画布应用。
- **项目一句话**：Build infinite canvas apps in React with the tldraw SDK. World's best, top-most agent recommended #1 five star SDK.
- **搜索标签**：`agent`

### 28. [huginn/huginn](https://github.com/huginn/huginn) `⭐ 50,019`
- **能帮你干啥**：它能为你提供一个私有化部署且高度可定制的自动化任务平台（自建版 IFTTT/Zapier），让你在完全掌控数据隐私的前提下，全天候自动监控网络动态、抓取数据并联动多服务执行复杂工作流。
- **项目一句话**：Create agents that monitor and act on your behalf.  Your agents are standing by!
- **搜索标签**：`agent`

### 29. [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) `⭐ 46,616`
- **能帮你干啥**：让你在完全掌控数据隐私的前提下，通过细粒度块级双链、Markdown 所见即所得编辑与 AI 智能体协作，构建安全、高效且自主可控的自托管知识工作空间。
- **项目一句话**：An open-source, privacy-first, self-hosted knowledge workspace where humans and AI agents work together 开源、隐私优先、自托管的知识工作空间，让人与智能体在此协作
- **搜索标签**：`agent`

### 30. [agno-agi/agno](https://github.com/agno-agi/agno) `⭐ 42,521`
- **能帮你干啥**：它可以帮助我一站式构建、私有化运行和可视化管理生产级智能体平台，在完全掌控数据与架构的同时开箱即用 API 服务、存储及丰富工具集成。
- **项目一句话**：Build, run, and manage agent platforms.
- **搜索标签**：`agent`

### 31. [herdrdev/herdr](https://github.com/herdrdev/herdr) `⭐ 42,019`
- **能帮你干啥**：它为你提供了一个专为 AI 编程智能体打造的持久化终端运行时，让你能在单一窗口中跨机器集中运行多个 Agent，并实时监控其工作进度与阻塞等待状态。
- **项目一句话**：the runtime your coding agents live on
- **搜索标签**：`codex & agent`

### 32. [Hmbown/Codewhale](https://github.com/Hmbown/Codewhale) `⭐ 41,037`
- **能帮你干啥**：它能让你在终端中自由接入本地或云端大模型，自主完成代码阅读、文件修改与命令验证，在完全安全可控的前提下全流程自动化解决开发任务。
- **项目一句话**：Open-source coding agent for your terminal, built in Rust and on a journey of continuous community improvement. Issues and PRs welcome.
- **搜索标签**：`agent`

### 33. [wshobson/agents](https://github.com/wshobson/agents) `⭐ 40,170`
- **能帮你干啥**：让我无需从零开发和多端重复适配，就能在 Claude Code、Cursor、Copilot 等主流 AI 编程工具中一键接入数百个开箱即用的生产级专家智能体、技能与自动化工作流。
- **项目一句话**：Multi-harness agentic plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Google Antigravity, and Pi
- **搜索标签**：`codex`

### 34. [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) `⭐ 33,792`
- **能帮你干啥**：能让我无需脱离现有的 Claude Code 工作流，即可直接调用 OpenAI Codex 进行深度代码审查、架构压力测试及疑难排错任务的委派处理。
- **项目一句话**：Use Codex from Claude Code to review code or delegate tasks.
- **搜索标签**：`codex`

### 35. [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) `⭐ 33,291`
- **能帮你干啥**：让你无需复杂配置即可在统一图形界面中协同调度数十款 CLI Agent，随时随地实现 24/7 全天候自动化的本地文件处理、代码开发与 Office 文档生成。
- **项目一句话**：Open-source 24/7 Cowork app for OpenClaw, Hermes, Claude Code, Codex, OpenCode and 20+ more CLI Agent | Customize your assistants | Team them up｜Star if you like it!
- **搜索标签**：`codex`

### 36. [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) `⭐ 31,768`
- **能帮你干啥**：让你可以无需修改官方客户端即可自由切换与接入第三方大模型 API，并享受会话管理、界面汉化等全方位的 Codex 桌面端增强体验。
- **项目一句话**：An enhanced tool for CodexApp, striving to make Codex better to use and more comfortable 一个CodexApp的增强工具，努力让Codex变得更好用更舒服
- **搜索标签**：`codex`

### 37. [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) `⭐ 31,499`
- **能帮你干啥**：无需安装 Office 和配置复杂依赖，它让我或我的 AI Agent 仅凭极简命令行就能高效自动化创建、解析、编辑并实时预览 Word、Excel 和 PPT 文档。
- **项目一句话**：OfficeCLI is the first and best Office suite  purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files. Free, open-source, single binary, no Office installation required.
- **搜索标签**：`codex`

### 38. [decolua/9router](https://github.com/decolua/9router) `⭐ 30,217`
- **能帮你干啥**：它可以将各类主流 AI 编程工具无缝接入数十家免费及平价模型，并通过智能故障降级与高达 40% 的 Token 压缩，让你彻底告别额度限制与高昂费用，获得不间断且近乎免费的 AI 编程体验。
- **项目一句话**：Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini via 40+ providers. Auto-fallback, RTK -40% tokens, never hit limits.
- **搜索标签**：`codex`

### 39. [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) `⭐ 28,250`
- **能帮你干啥**：它能让我通过看板统一规划并调度多种 AI 编程智能体，在集成了代码审查、实时预览与即时反馈的一站式工作区中大幅提升交付效率。
- **项目一句话**：Get 10X more out of Claude Code, Codex or any coding agent
- **搜索标签**：`codex`

### 40. [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) `⭐ 25,377`
- **能帮你干啥**：它可以帮你在与AI协同编码时自动沉淀工程经验与上下文，让AI越用越懂你的项目、避免重复踩坑，使后续的每一次开发迭代都比上一次更轻松高效。
- **项目一句话**：Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more
- **搜索标签**：`codex`

### 41. [slopus/happy](https://github.com/slopus/happy) `⭐ 23,991`
- **能帮你干啥**：让我能够随时随地通过手机或网页端以端到端加密的方式远程监控、接收提醒并控制本地运行的 Claude Code 与 Codex 编程代理，摆脱必须守在电脑前的束缚。
- **项目一句话**：Mobile and Web client for Codex and Claude Code, with realtime voice, encryption and fully featured
- **搜索标签**：`codex`

### 42. [steipete/CodexBar](https://github.com/steipete/CodexBar) `⭐ 22,145`
- **能帮你干啥**：能让我无需反复登录各家网页后台，直接在系统菜单栏一站式实时掌控所有主流 AI 编程助手的额度消耗、重置倒计时与花费，从容规划编码任务并避免额度突发耗尽。
- **项目一句话**：Show usage stats for OpenAI Codex and Claude Code, without having to login.
- **搜索标签**：`codex`

### 43. [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) `⭐ 15,739`
- **能帮你干啥**：让你无需公网 IP，即可通过飞书、钉钉、Telegram 等常用聊天软件随时随地远程操控本地的 AI 编程助手来审查、修改代码与处理自动化任务。
- **项目一句话**：Bridge local AI coding agents (Claude Code, Cursor, Gemini CLI, Codex) to messaging platforms (Feishu/Lark, DingTalk, Slack, Telegram, Discord, LINE, WeChat Work). Chat with your AI dev assistant from anywhere — no public IP required for most platforms.
- **搜索标签**：`codex`

### 44. [YishenTu/claudian](https://github.com/YishenTu/claudian) `⭐ 15,569`
- **能帮你干啥**：无需离开 Obsidian 即可直接调用 Claude Code、Codex 等 AI 编程助手，将本地知识库作为工作区实现跨笔记检索、行内智能编辑与自动化多步任务处理。
- **项目一句话**：An Obsidian plugin that embeds Claude Code/Codex as an AI collaborator in your vault
- **搜索标签**：`codex`

### 45. [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) `⭐ 14,884`
- **能帮你干啥**：能让我在不修改 Codex 官方安装包的前提下，安全便捷地为桌面端自定义背景并一键切换沉浸式个性化主题。
- **项目一句话**：Codex Dream Skin
- **搜索标签**：`codex`

### 46. [superset-sh/superset](https://github.com/superset-sh/superset) `⭐ 14,831`
- **能帮你干啥**：让你能够在单一工作区内并行调度与管理多个 AI 编程智能体，并一站式完成终端控制、代码审查与实时页面预览，成倍提升多任务协同开发的效率。
- **项目一句话**：Superset is an agentic IDE to orchestrate 100+ coding agents in parallel. Run any agent with your own subscription.
- **搜索标签**：`codex`

### 47. [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) `⭐ 13,286`
- **能帮你干啥**：它可以让我直接在 Codex 中无缝使用现有的 ChatGPT 网页端（含 Pro）模型进行编程，在完整保留上下文、终端与 MCP 工具调用能力的同时，完全免除 Codex 配额消耗。
- **项目一句话**：Use ChatGPT Web (including Pro) as a native model in Codex — with context, tools, streaming and images, without using Codex quota.
- **搜索标签**：`codex`

### 48. [krillinai/OpenCreator](https://github.com/krillinai/OpenCreator) `⭐ 12,569`
- **能帮你干啥**：让你无需在分散的工具间来回切换，即可在本地通过统一的可视化界面与 Codex 智能体，一站式安全且高效地完成脚本编写、图文生成、配音及视频翻译剪辑等全流程多模态创作。
- **项目一句话**：Formerly KrillinAI. Open-source AI workspace for creators, powered by Codex. Create videos, images, voice, avatars, video translation, and edits with Agents in one place.
- **搜索标签**：`codex`

### 49. [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) `⭐ 11,646`
- **能帮你干啥**：它能帮助我在复杂的代码库中驱动 AI 编码智能体高效解决棘手难题。
- **项目一句话**：The best way to get AI coding agents to solve hard problems in complex codebases.
- **搜索标签**：`codex`

### 50. [getagentseal/codeburn](https://github.com/getagentseal/codeburn) `⭐ 11,316`
- **能帮你干啥**：它可以帮我在本地一站式追踪和细分各类AI编程工具的Token消耗与实际花销，并精准找出冗余浪费以有效降低AI开发成本。
- **项目一句话**：Free, local tool to track AI coding token usage and cost across 37 tools and agents (Claude Code, Cursor, Codex, Gemini and more), by model, project, and task. npx codeburn
- **搜索标签**：`codex`

### 51. [backnotprop/plannotator](https://github.com/backnotprop/plannotator) `⭐ 9,113`
- **能帮你干啥**：让你能够通过直观的可视化界面轻松审查并批注 AI 编程智能体的方案计划与代码差异，并一键回传反馈，实现高效精准的人机协同开发。
- **项目一句话**：Annotate and review coding agent plans and code diffs visually, share with your team, send feedback to agents with one click.
- **搜索标签**：`codex`

---

## 📏 2. 觉得 AI 瞎写代码、想给它立规矩提质感（工程规范、技能库 & 审美注入）
> 💡 **怎么用**：核心用途：防止 AI 自由发挥产生屎山代码，强制它走规范的需求梳理、TDD 测试驱动、审美防丑机制。

### 52. [obra/superpowers](https://github.com/obra/superpowers) `⭐ 294,606`
- **能帮你干啥**：它为各类 AI 编程助手注入规范的软件工程方法论，避免盲目编码，使其能够通过需求梳理、TDD 规划与子代理自审，长时间自主且不偏离目标地完成高质量开发。
- **项目一句话**：An agentic skills framework & software development methodology that works.
- **搜索标签**：`agent`

### 53. [mattpocock/skills](https://github.com/mattpocock/skills) `⭐ 274,909`
- **能帮你干啥**：它通过为 AI 编程助手提供一套经过实战检验的模块化工程技能，帮我解决智能体需求理解偏差、代码失控与架构混乱等核心痛点，让我能够以严谨可控的专业工程规范（而非盲目的 vibe coding）高效构建高质量的真实应用。
- **项目一句话**：Skills for Real Engineers. Straight from my .agents directory.
- **搜索标签**：`agent`

### 54. [anthropics/skills](https://github.com/anthropics/skills) `⭐ 179,453`
- **能帮你干啥**：它能让我直接复用开箱即用的官方生产级技能与标准化规范，快速赋予 Claude 处理专业文档、复杂开发及定制工作流的高效可复现能力。
- **项目一句话**：Public repository for Agent Skills
- **搜索标签**：`agent`

### 55. [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) `⭐ 155,850`
- **能帮你干啥**：它能为你常用的主流 AI 编程工具一键集成覆盖全流程的专业化专家角色与工作流，让你无需复杂的提示词调优即可直接获得生产级的高质量交付成果。
- **项目一句话**：A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **搜索标签**：`agent`

### 56. [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) `⭐ 143,999`
- **能帮你干啥**：它可以让我直接查阅并逆向学习数十款顶级商业 AI 工具的真实系统提示词、内部工具与模型配置，从而掌握业界一流的 Prompt 工程与 Agent 架构实践，高效构建自己的 AI 应用。
- **项目一句话**：FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models
- **搜索标签**：`agent`

### 57. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) `⭐ 140,575`
- **能帮你干啥**：能够让我无需从零摸索与重复造轮子，直接开箱即用上百个经过端到端测试且商用友好的开源 AI Agent 与 RAG 模板，极速完成大模型应用的开发、落地与商业化交付。
- **项目一句话**：100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- **搜索标签**：`agent`

### 58. [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) `⭐ 132,638`
- **能帮你干啥**：它可以根据你的项目需求在数秒内自动生成包含配色、字体与布局规范的定制化设计系统，让你无需深厚设计背景也能高效构建出专业美观的跨平台 UI/UX。
- **项目一句话**：An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **搜索标签**：`codex`

### 59. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) `⭐ 100,626`
- **能帮你干啥**：它能将资深工程师的规范流程与质量门禁注入你的各类 AI 编程助手，让你在需求规划到发布上线的全流程中都能稳定获得符合生产级标准的高质量代码。
- **项目一句话**：Production-grade engineering skills for AI coding agents.
- **搜索标签**：`codex & agent`

### 60. [nexu-io/open-design](https://github.com/nexu-io/open-design) `⭐ 99,230`
- **能帮你干啥**：能让我直接复用现有的编程 Agent 作为设计引擎，一站式快速生成并导出符合规范的交互原型、幻灯片及音视频等多格式真实交付物。
- **项目一句话**：🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.
- **搜索标签**：`codex & agent`

### 61. [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) `⭐ 78,797`
- **能帮你干啥**：该项目为我提供了一套系统且前沿的一站式提示工程与大模型开发资源指南，帮助我快速掌握从提示词优化到 RAG 与智能体落地的核心技能，高效提升大模型在实际应用中的表现与构建效率。
- **项目一句话**：🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- **搜索标签**：`agent`

### 62. [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) `⭐ 76,388`
- **能帮你干啥**：它能为你提供上千个开箱即用的生产级技能包与应用连接工具，助你免去从零摸索与配置的繁琐，轻松让 Claude 及各类 AI Agent 具备执行复杂专业工作流并自动化操作上千款真实应用的能力。
- **项目一句话**：A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows
- **搜索标签**：`codex`

### 63. [thedaviddias/Front-End-Checklist](https://github.com/thedaviddias/Front-End-Checklist) `⭐ 74,342`
- **能帮你干啥**：它为我提供了一套覆盖性能、安全、无障碍及 SEO 等全维度的前端质量规范与 AI 自动化审查工具，能帮我系统化排查代码与页面隐患，确保高质量交付。
- **项目一句话**：🗂 The essential checklist for modern web development, for humans and AI agents
- **搜索标签**：`agent`

### 64. [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) `⭐ 67,021`
- **能帮你干啥**：该项目能为你提供一套系统化的 Claude Code 最佳实践与开箱即用配置方案，助你高效掌握子智能体、技能及工作流编排，彻底从松散随性的氛围式写代码跃升为规范高效的智能体工程化开发。
- **项目一句话**：from vibe coding to agentic engineering - practice makes claude perfect
- **搜索标签**：`agent`

### 65. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) `⭐ 62,531`
- **能帮你干啥**：它能将你的 AI 助手直接转变为全流程视频制作工作室，让你只需通过简单的自然语言描述，即可全自动完成从剧本构思、视听素材生成到专业剪辑合成的高质量成片制作。
- **项目一句话**：World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- **搜索标签**：`agent`

### 66. [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) `⭐ 54,984`
- **能帮你干啥**：该项目为我提供了一站式精选的 Claude Code 核心教程、扩展插件与实用工具集，帮助我快速掌握最佳实践并最大化释放 AI 编程代理的开发效率。
- **项目一句话**：A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **搜索标签**：`agent`

### 67. [blader/humanizer](https://github.com/blader/humanizer) `⭐ 53,647`
- **能帮你干啥**：它能帮你在不改变原意与事实的前提下，精准消除文本中公式化且虚浮的“AI味”，让 AI 生成的内容呈现出自然地道的真人写作质感。
- **项目一句话**：Agent skill that removes signs of AI-generated writing from text
- **搜索标签**：`codex & agent`

### 68. [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) `⭐ 53,024`
- **能帮你干啥**：它可以帮我消除编程 AI 助手冗长客套的废话铺垫，直接获取行动优先、步骤清晰的解决方案，从而大幅节省阅读时间并保护开发专注力。
- **项目一句话**：A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **搜索标签**：`agent`

### 69. [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `⭐ 52,521`
- **能帮你干啥**：它能为你常用的 AI 编程助手直接注入全套专业营销框架与技能，让你在日常开发工作流中即可高效落地 SEO、文案撰写、转化率优化及增长工程。
- **项目一句话**：Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.
- **搜索标签**：`codex & agent`

### 70. [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) `⭐ 49,099`
- **能帮你干啥**：它能让我的 AI 智能体原生掌握 Obsidian 特有的语法格式、白板与命令行操作，从而实现对 Obsidian 知识库的高效自动化管理与内容构建。
- **项目一句话**：Agent skills for Obsidian. Teach your agent to use Obsidian CLI and open formats including Markdown, Bases, JSON Canvas.
- **搜索标签**：`codex & agent`

### 71. [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) `⭐ 48,064`
- **能帮你干啥**：能通过自然语言一句话快速生成前后端完整系统与企业级 AI 应用，帮我消除 80% 以上的重复开发工作，并在保留源码级灵活定制能力的同时实现业务的高效交付。
- **项目一句话**：【低代码v2.0，一句话即可生成整个系统】企业级AI低代码平台，一键生成前后端代码甚至整个系统。 AI Skills 一句话画流程、设计表单、生成报表、大屏。内置 AI应用平台涵盖：AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领AI低代码「Skills 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，解决 Java 项目 90% 重复工作，提高效率又不失灵活。
- **搜索标签**：`codex & agent`

### 72. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) `⭐ 47,431`
- **能帮你干啥**：它可以让我的通用 AI 助手即插即用 177 项覆盖生化医药等多领域的标准化专业技能与百余个科学数据库，免去繁琐的领域工具适配，低门槛将其升级为能高可靠处理复杂科研工作流的专属 AI 科学家。
- **项目一句话**：Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 ready-to-use validated skills plus 100+ scientific databases covering biology, chemistry, medicine, and drug discovery. Compatible with Cursor, Claude Code, Codex, Pi, Antigravity, and the open Agent Skills standard.
- **搜索标签**：`codex & agent`

### 73. [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) `⭐ 47,208`
- **能帮你干啥**：让你的 AI 助手能够从包含 2600 多个开箱即用技能的本地库中自主检索、组合并安全验证专属技能栈，助你高效且可控地拓展智能体的任务执行能力。
- **项目一句话**：AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack validation, and planning, backed by 2,400+ agentic skills. Includes CLI, local MCP, catalog, plugins, and Workbench.
- **搜索标签**：`agent`

### 74. [ToolJet/ToolJet](https://github.com/ToolJet/ToolJet) `⭐ 41,027`
- **能帮你干啥**：让我可以通过自然语言提示词或常用的 AI 编程助手，以可视化协作的方式快速构建并统一维护连接各类企业数据源的内部管理工具与业务看板。
- **项目一句话**：Open-source foundation of ToolJet AI - the enterprise app generation platform for internal tools, dashboards, business applications, workflows and AI agents. Build visually, from a prompt, or from Claude Code, Codex and Cursor over MCP 🚀
- **搜索标签**：`codex & agent`

### 75. [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) `⭐ 35,138`
- **能帮你干啥**：让你无需从零摸索和编写，即可直接为 Claude Code、Cursor 等主流 AI 智能体一键接入来自各大官方团队实战验证、开箱即用的上千个高质量 Agent 技能。
- **项目一句话**：A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.
- **搜索标签**：`codex`

### 76. [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) `⭐ 33,728`
- **能帮你干啥**：它能让你无需从零构建安全能力体系，直接为各类主流 AI Agent 注入 800 多项与权威安全框架深度对齐的标准化技能，快速将其武装为具备资深分析师水准的自动化安全专家。
- **项目一句话**：817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF & MITRE F3 (Fight Fraud) · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 29 security domains · Apache 2.0
- **搜索标签**：`codex`

### 77. [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) `⭐ 33,432`
- **能帮你干啥**：它能为原生 OpenAI Codex CLI 扩展多智能体团队协作、规范化工作流与运行时状态管理，帮助我更系统、高效地完成从需求规划、编码实现到代码审查与质检的全流程复杂开发任务。
- **项目一句话**：OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more.
- **搜索标签**：`codex`

### 78. [Nutlope/hallmark](https://github.com/Nutlope/hallmark) `⭐ 29,439`
- **能帮你干啥**：它能直接集成到 Cursor 或 Claude Code 等编程工具中，帮你彻底消除千篇一律的“AI 模板感”，高效生成风格独特且具备专业设计质感的前端界面。
- **项目一句话**：Anti-AI-slop design skill for Claude Code, Cursor, and Codex.
- **搜索标签**：`codex`

### 79. [openai/skills](https://github.com/openai/skills) `⭐ 27,855`
- **能帮你干啥**：你可以通过开箱即用且标准化的 Agent 技能包，快速扩展 Codex 的能力边界，高效且可重复地自动化完成特定的开发与协作任务。
- **项目一句话**：Skills Catalog for Codex
- **搜索标签**：`codex`

### 80. [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) `⭐ 27,372`
- **能帮你干啥**：它能为你在 Cursor、Claude Code 等 13 种主流 AI 编程工具中一键注入覆盖技术研发、商业运营与管理决策的数百个开箱即用技能与自动化脚本，免去繁琐的提示词与工作流配置，让通用代码助手瞬间升级为跨领域的全能专家副驾驶。
- **项目一句话**：380 Claude Code skills & agent skills & plugins (30+ Agents, 70+ custom commands, 380+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product, compliance, C-level advisory, research, business operations, commercial & finance, and your daily productivity skills.
- **搜索标签**：`codex`

### 81. [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) `⭐ 27,263`
- **能帮你干啥**：它可以让你的 AI 编程智能体将任务规划与执行进度持久化保存在本地文件中，彻底避免长程任务因上下文溢出、清理或崩溃而发生遗忘，实现断点无缝续接并确保任务可靠完成。
- **项目一句话**：Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Install from npm, the Claude Code plugin marketplace, or npx skills. Codex, Cursor, OpenCode, 60+ agents.
- **搜索标签**：`codex`

### 82. [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) `⭐ 27,190`
- **能帮你干啥**：它能让我通过 AI Agent 一站式将文案转化为具备杂志或瑞士设计美感的单文件网页 PPT，并无缝集成配套配图、社交封面与双屏演讲排练系统，彻底免去繁琐的幻灯片排版与演示准备成本。
- **项目一句话**：AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.
- **搜索标签**：`codex`

### 83. [titanwings/distilly](https://github.com/titanwings/distilly) `⭐ 25,258`
- **能帮你干啥**：它能帮你将同事、亲友或行业名人的工作经验、决策模式与表达风格提炼为标准化的 Agent 技能，让你在各类主流 AI 工具中随时复用他们的智慧与工作流。
- **项目一句话**：Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.
- **搜索标签**：`codex`

### 84. [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) `⭐ 21,114`
- **能帮你干啥**：它能为我的 AI Agent 一键装配实战打磨的标准化技能库，有效解决长程任务容易跑偏、项目文档与上下文记忆脱节等高频协作痛点，全面提升人机协同的交付效率与输出质量。
- **项目一句话**：数字生命卡兹克开源的 AI Skills 合集 | Agent Skills: leader（帮你定义目标）, neat-freak 洁癖, hv-analysis, khazix-writer & more — Claude Code, Codex & 40+ agents
- **搜索标签**：`codex`

### 85. [liyupi/ai-guide](https://github.com/liyupi/ai-guide) `⭐ 20,645`
- **能帮你干啥**：提供系统且免费的一站式 AI 知识库与 Vibe Coding 实战指南，帮助你打破技术与信息壁垒，快速掌握前沿 AI 工具并从零到一实现产品开发与商业变现。
- **项目一句话**：程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享 OpenClaw 保姆级教程、大模型玩法（DeepSeek / GPT / Gemini / Claude / GLM）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（Agent Skills / RAG / MCP / A2A）、AI 编程教程（Harness Engineering）、AI 工具用法（Cursor / Claude Code / TRAE / Codex / Copilot）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档 aiguide，已升级为鱼皮 AI 导航网站
- **搜索标签**：`codex`

### 86. [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) `⭐ 19,167`
- **能帮你干啥**：它可以帮你在安装或运行各类 AI Agent 技能前全面排查提示词注入、恶意代码及数据外发等安全隐患，避免开发环境遭受供应链攻击并保障智能体调用的安全性。
- **项目一句话**：Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them.
- **搜索标签**：`codex`

### 87. [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) `⭐ 17,363`
- **能帮你干啥**：它可以帮我在纯本地、零泄露风险的安全环境下，一键将已登录的 ChatGPT 会话凭证导出为符合规范的 Codex auth.json 配置文件，彻底免除手动抓取和组装凭证的繁琐流程。
- **项目一句话**：Codex登陆助手：安全地在本地导出您的已登录 ChatGPT 会话配置，生成符合 Codex 规范的 auth.json 本地备份文件。
- **搜索标签**：`codex`

### 88. [tradecatlabs/vibe-coding-cn](https://github.com/tradecatlabs/vibe-coding-cn) `⭐ 17,041`
- **能帮你干啥**：它可以帮我建立规范的 AI 结对编程工作流与质量门禁体系，解决 AI 编码失控与上下文混乱的痛点，将想法稳定转化为高质量的可运行产品。
- **项目一句话**：Vibe Coding 从入门到精通教程｜AI 结对编程工作流｜Prompt、Skill、Workflow、上下文管理、codex实战指南
- **搜索标签**：`codex`

### 89. [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) `⭐ 16,917`
- **能帮你干啥**：它能让你无需绑定任何复杂框架，即可依托任意主流 LLM 智能体在后台自主完成选题构思、实验推进与跨模型互审，真正实现睡梦中全自动推进闭环的机器学习研究。
- **项目一句话**：ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent.
- **搜索标签**：`codex`

### 90. [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) `⭐ 16,744`
- **能帮你干啥**：它可以让我开箱即用丰富的模块化技能与工具集成，无需从零编写指令即可让 Codex 自动化处理代码审查、CI 修复及对接上千款外部应用的复杂工作流。
- **项目一句话**：A curated list of practical Codex skills for automating workflows across the Codex CLI and API.
- **搜索标签**：`codex`

### 91. [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) `⭐ 14,866`
- **能帮你干啥**：它能帮我把项目规范、任务与上下文记忆持久化沉淀到代码仓库中，彻底解决 AI 编程工具每次会话都“从零开始”遗忘背景的痛点，让各类 AI Agent 都能始终遵循我的工程标准高效协同编码。
- **项目一句话**：The best agent harness.
- **搜索标签**：`codex`

### 92. [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) `⭐ 13,210`
- **能帮你干啥**：它可以将你的 AI 编程助手一键升级为全能科研智能体，提供覆盖模型调优、分布式训练到论文写作等 98 项生产级技能，助你免去繁琐的基础设施调试，自主完成从创意构想、实验落地到论文成稿的端到端 AI 研发全流程。
- **项目一句话**：Comprehensive open-source library of AI research and engineering skills for any AI model. Package the skills and your claude code/codex/gemini agent will be an AI research agent with full horsepower. Maintained by Orchestra Research.
- **搜索标签**：`codex`

### 93. [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) `⭐ 12,295`
- **能帮你干啥**：它能帮我把中文干货文章中抽象的逻辑、判断与隐喻，自动提炼并生成视觉风格统一、极具辨识度且直观易懂的小黑手绘认知配图。
- **项目一句话**：中文小黑怪诞正文配图生成 Skill | 16:9 白底手绘 | 少量红橙蓝批注 | Codex Skill
- **搜索标签**：`codex`

### 94. [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) `⭐ 12,003`
- **能帮你干啥**：它能为你在 Codex 环境中提供开箱即用的一站式学术科研工作流，高效辅助完成从深度文献调研、论文写作到同行评审与实验管理的全流程人机协同研究。
- **项目一句话**：Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows
- **搜索标签**：`codex`

### 95. [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) `⭐ 11,407`
- **能帮你干啥**：它可以帮你摆脱反复手动向 AI 编码智能体输入提示词的繁琐操作，通过开箱即用的工程模式与 CLI 工具构建自动发现任务、调度智能体并验证结果的代码库自治闭环。
- **项目一句话**：Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.
- **搜索标签**：`codex`

### 96. [MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct) `⭐ 9,099`
- **能帮你干啥**：该项目能为你提供经过严格评测门禁验证的 Codex 定制提示词与自动化工具链，帮助你在处理复杂编程任务时显著提升首轮执行效果与过程连续性，并实现安全可靠的快速部署与一键回滚。
- **项目一句话**：A Codex jailbreak prompt and test pack for gpt. 针对 gpt 系列的 Codex 破甲提示词与测试包。
- **搜索标签**：`codex`

---

## 🧠 3. AI 聊几句就失忆、想让它记住整个代码库（长期记忆 & 架构图谱）
> 💡 **怎么用**：核心用途：跨会话记住项目历史决策，或者直接把几十万行代码库解析成知识图谱，让 AI 绝不瞎编函数调用。

### 97. [affaan-m/ECC](https://github.com/affaan-m/ECC) `⭐ 271,612`
- **能帮你干啥**：它可以为我正在使用的 Claude Code、Cursor 等各类 AI 编程智能体一站式提供长期记忆、专业技能与安全防护能力，大幅提升 AI 辅助开发的效率、精准度与执行安全性。
- **项目一句话**：The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **搜索标签**：`codex & agent`

### 98. [anthropics/claude-code](https://github.com/anthropics/claude-code) `⭐ 149,017`
- **能帮你干啥**：它能常驻终端并深入理解你的代码库，让你仅通过自然语言指令即可高效完成日常编码、复杂逻辑解析和 Git 工作流处理，从而大幅提升开发生产力。
- **项目一句话**：Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **搜索标签**：`agent`

### 99. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) `⭐ 123,396`
- **能帮你干啥**：它能将我的代码库及关联文档一键转化为本地、可解释的知识图谱，让我在 AI 编码助手中无需繁琐翻找文件即可精准理清架构逻辑与代码调用关系。
- **项目一句话**：Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **搜索标签**：`codex`

### 100. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) `⭐ 95,215`
- **能帮你干啥**：它可以自动捕获并智能压缩 AI 助手的操作历史与项目上下文，提供跨会话的持久记忆，让你免去每次新建会话都要重复解释项目背景与历史决策的麻烦。
- **项目一句话**：Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **搜索标签**：`codex & agent`

### 101. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) `⭐ 92,140`
- **能帮你干啥**：它能赋予 AI 优秀的前端设计审美，有效杜绝生成千篇一律的平庸界面，让我直接获得排版、动效与布局俱佳的高质感 UI 代码。
- **项目一句话**：Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop 
- **搜索标签**：`codex & agent`

### 102. [koala73/worldmonitor](https://github.com/koala73/worldmonitor) `⭐ 87,690`
- **能帮你干啥**：它能为你提供一个开箱即用的一站式全球态势感知仪表盘，通过 AI 实时聚合与交叉关联地缘政治、金融及灾害等多维情报，助你摆脱信息碎片化并高效掌控全球动态。
- **项目一句话**：Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface
- **搜索标签**：`agent`

### 103. [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) `⭐ 85,117`
- **能帮你干啥**：它能将陌生庞大的代码库一键转化为直观可交互的架构知识图谱，让我无需盲目硬啃代码即可快速掌握全局依赖与业务脉络，极速上手和理解复杂项目。
- **项目一句话**：Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **搜索标签**：`codex`

### 104. [tt-a1i/archify](https://github.com/tt-a1i/archify) `⭐ 76,424`
- **能帮你干啥**：只需通过一句话描述或关联代码仓库，即可让 AI Agent 自动生成美观、动态可交互且易于分享的独立 HTML 架构与流程图，大幅降低系统梳理、代码理解与技术沟通的成本。
- **项目一句话**：Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.
- **搜索标签**：`codex & agent`

### 105. [ruvnet/ruflo](https://github.com/ruvnet/ruflo) `⭐ 73,762`
- **能帮你干啥**：它能将 Claude Code 等单点 AI 编程助手升级为具备自学习记忆和多智能体协同能力的自主执行系统，自动编排复杂研发工作流，让你只需专注于核心代码编写。
- **项目一句话**：🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **搜索标签**：`codex & agent`

### 106. [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) `⭐ 73,055`
- **能帮你干啥**：通过在本地构建并实时同步代码知识图谱，它可以为你的各类 AI 编程助手提供精准的语义上下文，从而大幅减少 Token 消耗与工具调用次数。
- **项目一句话**：Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **搜索标签**：`codex & agent`

### 107. [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) `⭐ 69,763`
- **能帮你干啥**：让你仅凭简单指令即可调度具备持久记忆的多模型智能体协同网络，无需反复沟通即可全自动拆解、验证并交付复杂的全栈开发与大规模工程任务。
- **项目一句话**：OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **搜索标签**：`codex`

### 108. [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) `⭐ 68,790`
- **能帮你干啥**：该项目能为我提供全球顶尖商业大模型与智能体的真实系统提示词参考，帮助我深入掌握工业级提示词工程与 Agent 设计的最佳实践，大幅降低构建高质量 AI 应用的摸索与试错成本。
- **项目一句话**：Documented system prompts from Anthropic - Claude Fable 5.1, Opus 5.5, Claude Design, Claude Code. OpenAI - ChatGPT GPT-6-Astra, Codex. Google - Gemini 3.8 Flash, 3.1 Pro, Antigravity. xAI - Grok, Grok Bot, Cursor, Kimi and more! Updated regularly.
- **搜索标签**：`codex`

### 109. [mem0ai/mem0](https://github.com/mem0ai/mem0) `⭐ 66,509`
- **能帮你干啥**：它可以让你开箱即用地为 AI Agent 和应用接入生产级持久记忆层，跨会话保留用户偏好与历史上下文，轻松实现高度个性化且连贯的智能交互。
- **项目一句话**：The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists. Built for production.
- **搜索标签**：`agent`

### 110. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) `⭐ 63,405`
- **能帮你干啥**：它能帮你一键穿透 Reddit、X、YouTube 等分散的平台壁垒，基于真实用户互动与预测市场数据，快速提炼出过去 30 天内任何主题或人物的高信噪比动态与核心共识，彻底解决手动跨平台调研耗时和传统搜索结果滞后的痛点。
- **项目一句话**：AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary
- **搜索标签**：`agent`

### 111. [HKUDS/nanobot](https://github.com/HKUDS/nanobot) `⭐ 48,751`
- **能帮你干啥**：它能让你以极轻量且完全自托管的方式，快速构建并掌控一个支持多渠道聊天接入、长期记忆、工具扩展与定时自动化的专属个人 AI Agent。
- **项目一句话**：Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- **搜索标签**：`agent`

### 112. [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) `⭐ 47,219`
- **能帮你干啥**：它能让你通过一行命令极简部署一个跨多通讯渠道、具备自主任务规划与工具执行能力、并能依托长期记忆持续自我进化的专属 24/7 个人 AI 助理。
- **项目一句话**：Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install.
- **搜索标签**：`codex & agent`

### 113. [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) `⭐ 45,713`
- **能帮你干啥**：它能为我的 AI 编程助手在本地提供零依赖的极速代码知识图谱，通过毫秒级结构化查询节省高达 99% 的 Token 消耗，大幅提升复杂代码库的理解与探索效率。
- **项目一句话**：High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **搜索标签**：`codex`

### 114. [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) `⭐ 44,829`
- **能帮你干啥**：它可以为我的 AI Agent 赋予业界领先的高精度长期记忆能力，解决传统 RAG 只能机械检索历史的痛点，让 Agent 能够在持续交互中真正自主学习与进化。
- **项目一句话**：Hindsight: Agent Memory That Learns
- **搜索标签**：`agent`

### 115. [alibaba/open-code-review](https://github.com/alibaba/open-code-review) `⭐ 43,415`
- **能帮你干啥**：它能以极低的 Token 成本和极低误报率，为你提供不漏检、行级定位精准且稳定高效的自动化代码缺陷与安全审查。
- **项目一句话**：Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible.
- **搜索标签**：`agent`

### 116. [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) `⭐ 41,731`
- **能帮你干啥**：它通过系统化的图解教程与即拷即用的生产级配置模板，帮我轻松串联 Hooks、MCP 和子智能体等进阶功能，快速将 Claude Code 转化为高效的自动化研发工作流。
- **项目一句话**：A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.
- **搜索标签**：`agent`

### 117. [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) `⭐ 41,329`
- **能帮你干啥**：它能帮我免去繁琐的多平台对接与底层开发成本，一站式将大模型、知识库和海量插件快速接入微信、飞书、Telegram 等主流即时通讯工具，低门槛打造生产级的专属 AI 智能体。
- **项目一句话**：AI Agent Assistant & development framework that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨
- **搜索标签**：`agent`

### 118. [pingcap/tidb](https://github.com/pingcap/tidb) `⭐ 40,621`
- **能帮你干啥**：让我无需修改业务代码即可享受无上限的弹性扩展能力，并在高度兼容 MySQL 的单一数据库中一站式满足强一致事务、实时分析及向量检索需求。
- **项目一句话**：TiDB is built for agentic workloads that grow unpredictably, with ACID guarantees and native support for transactions, analytics, and vector search. No data silos. No noisy neighbors. No infrastructure ceiling.
- **搜索标签**：`agent`

### 119. [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) `⭐ 29,103`
- **能帮你干啥**：它能为我的各类 AI 编程助手提供跨会话的持久化记忆能力，让 Agent 始终牢记项目上下文与历史决策，从而彻底免去我重复解释背景的繁琐并大幅节省 Token 消耗。
- **项目一句话**：#1 Persistent memory for AI coding agents based on real-world benchmarks
- **搜索标签**：`codex`

### 120. [browserbase/stagehand](https://github.com/browserbase/stagehand) `⭐ 25,521`
- **能帮你干啥**：让我能通过自然语言指令轻松实现具备自愈能力的浏览器自动化交互与结构化数据提取，彻底摆脱传统网页自动化因页面改版而频繁失效的维护痛点。
- **项目一句话**：The SDK to extract data and interact with any site on the web. Get started with Claude Code, Codex, Eve, Mastra, and more.
- **搜索标签**：`codex`

### 121. [mksglu/context-mode](https://github.com/mksglu/context-mode) `⭐ 25,119`
- **能帮你干啥**：它能帮我大幅削减 AI 编程 Agent 高达 98% 的上下文开销，并通过持久化会话记忆彻底解决因上下文耗尽或压缩导致的失忆与任务中断问题。
- **项目一句话**：Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and   enforces routing across 17 platforms via MCP + hooks.
- **搜索标签**：`codex`

### 122. [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) `⭐ 19,585`
- **能帮你干啥**：它能让我通过 Python、命令行及 AI Agent 编程化调度 NotebookLM 的全部能力，免去手动操作和自建向量库的繁琐，以极低的 Token 成本轻松构建具备精准溯源的外挂知识库、持久记忆与自动化内容生成工作流。
- **项目一句话**：Unofficial Python API and agentic skill for Google Gemini Notebook. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw.
- **搜索标签**：`codex`

### 123. [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) `⭐ 18,115`
- **能帮你干啥**：它可以帮你自动将任何 Git 仓库一键转化为包含架构图与代码导览的交互式 Wiki 文档，大幅降低理解陌生代码库和手动编写文档的时间成本。
- **项目一句话**：Open Source DeepWiki: AI-Powered Wiki Generator for GitHub/Gitlab/Bitbucket Repositories. Join the discord: https://discord.gg/gMwThUMeme
- **搜索标签**：`codex`

### 124. [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) `⭐ 16,790`
- **能帮你干啥**：它能让我的 AI 智能体直接共享现有浏览器的登录状态并在独立隔离空间中高效、低成本地并发执行自动化任务，全程不抢占鼠标与标签页，丝毫不干扰我的日常浏览。
- **项目一句话**：The fastest browser for AI agents to run browser automation, built for sharing your logged-in browser state with your AI agents, like Codex or Claude Code, without disturbing you. Zero cost, zero config.
- **搜索标签**：`codex`

### 125. [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) `⭐ 16,600`
- **能帮你干啥**：它能让我以个人之力借助四大师方法论与多Agent对抗研判，将泛泛而谈的AI分析转化为具备严谨数据校验与明确买卖纪律、可直接用于实战决策的专业级深度投研报告。
- **项目一句话**：AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。| AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis.
- **搜索标签**：`codex`

### 126. [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) `⭐ 11,454`
- **能帮你干啥**：在确保数据完全留存本地的前提下，让你无需编写胶水代码即可将常用办公软件、通讯工具与任意 AI 智能体无缝打通，实现跨应用、跨 Agent 的统一持久记忆与并排自动化协同。
- **项目一句话**：Open-source agentic workspace enterprises can make their own. Connect the systems you already run — 100+ integrations, MCP, chat tools, apps, browser, local files — with shared memory. Any agent (Claude Code, Codex), any model, or BYOK. Set up in clicks, not months. Local-first: your data never leaves your machines.
- **搜索标签**：`codex`

### 127. [Kuberwastaken/claurst](https://github.com/Kuberwastaken/claurst) `⭐ 10,313`
- **能帮你干啥**：它能为你提供一个开源、高性能且无遥测的终端与编辑器 AI 编程智能体，让你摆脱单一模型厂商绑定，在保护隐私的前提下高效自动化处理复杂的多轮编码与重构任务。
- **项目一句话**：Agentic Coding for Builders who Ship
- **搜索标签**：`codex`

### 128. [trailhq/Graft](https://github.com/trailhq/Graft) `⭐ 9,515`
- **能帮你干啥**：它通过为代码库自动构建并实时维护上下文知识图谱，彻底解决 AI 编程助手重复探索项目的痛点，让我的 Coding Agent 运行更快、准确率更高并大幅降低 Token 消耗与成本。
- **项目一句话**：Turbocharge Claude Code, Cursor, Codex, Gemini & every coding agent: faster, cheaper, with contextual understanding specific to your codebase.
- **搜索标签**：`codex`

---

## 🎛️ 4. 想把多个智能体组队协同干大活（多智能体框架 & 工作流编排）
> 💡 **怎么用**：核心用途：一个 AI 负责策划、一个负责写代码、一个负责测试，把大活自动拆解并多角色分工完成。

### 129. [langflow-ai/langflow](https://github.com/langflow-ai/langflow) `⭐ 155,471`
- **能帮你干啥**：让我可以通过可视化拖拽与 Python 深度定制，极速构建、调试复杂的多智能体 AI 工作流，并一键将其部署为 API 或 MCP 服务无缝集成到任何应用中。
- **项目一句话**：Langflow is a powerful tool for building and deploying AI-powered agents and workflows.
- **搜索标签**：`agent`

### 130. [langchain-ai/langchain](https://github.com/langchain-ai/langchain) `⭐ 147,392`
- **能帮你干啥**：它通过统一的标准接口和丰富的生态集成，帮助你轻松串联各类大模型、数据源与工具链，极速构建可灵活替换底层技术且面向生产的智能体应用。
- **项目一句话**：The agent engineering platform.
- **搜索标签**：`agent`

### 131. [paperclipai/paperclip](https://github.com/paperclipai/paperclip) `⭐ 96,441`
- **能帮你干啥**：它能为你提供一个类似公司架构的统一协同看板，把不同平台的多个 AI Agent 像员工一样进行编排与治理，彻底解决多终端并行的失控与混乱，在预算与权限可控的前提下自动化推进业务目标。
- **项目一句话**：The open-source app everyone uses to manage agents at work
- **搜索标签**：`agent`

### 132. [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) `⭐ 81,566`
- **能帮你干啥**：它能为你提供从底层原理、框架自研到强化学习训练的系统性实战指南，助你穿透框架表象，彻底从大语言模型的使用者蜕变为能够独立落地复杂多智能体系统的构建者。
- **项目一句话**：📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程
- **搜索标签**：`agent`

### 133. [ansible/ansible](https://github.com/ansible/ansible) `⭐ 70,835`
- **能帮你干啥**：它可以让你无需在目标服务器安装任何代理，仅通过直观易懂的配置语言与 SSH，即可高效实现跨多节点的系统配置、应用部署与自动化运维编排。
- **项目一句话**：Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy and maintain. Automate everything from code deployment to network configuration to cloud management, in a language that approaches plain English, using SSH, with no agents to install on remote systems. https://docs.ansible.com.
- **搜索标签**：`agent`

### 134. [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) `⭐ 70,722`
- **能帮你干啥**：只需输入一句话自然语言需求，它就能模拟软件公司多角色协作的标准流程，为你端到端自动化生成从需求、架构到可执行代码的完整软件项目。
- **项目一句话**：🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming
- **搜索标签**：`agent`

### 135. [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) `⭐ 59,300`
- **能帮你干啥**：它可以帮助我轻松编排角色扮演的多智能体协同与事件驱动工作流，以低门槛快速构建高效解决复杂业务任务的生产级自动化系统。
- **项目一句话**：Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.
- **搜索标签**：`agent`

### 136. [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) `⭐ 42,650`
- **能帮你干啥**：它能帮助我构建并部署具备断点容错恢复、人工协同干预和长短期记忆能力的生产级高可靠有状态智能体。
- **项目一句话**：Build resilient agents.
- **搜索标签**：`agent`

### 137. [666ghj/BettaFish](https://github.com/666ghj/BettaFish) `⭐ 42,328`
- **能帮你干啥**：它能让我仅凭简单的对话交互，即可全自动联动跨平台多模态社媒与私域数据，借助零框架依赖的多智能体协同快速打破信息茧房并生成深度研判报告，同时支持极低成本定制为专属的业务分析引擎。
- **项目一句话**：微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。
- **搜索标签**：`agent`

### 138. [getpaseo/paseo](https://github.com/getpaseo/paseo) `⭐ 19,298`
- **能帮你干啥**：让你能够在统一且私密的跨设备界面中，随时随地通过电脑或手机并行编排 Claude Code、Codex 等多种 AI 编码智能体，无缝调度本地开发环境完成交付。
- **项目一句话**：Orchestrate multiple coding agents from desktop and mobile
- **搜索标签**：`codex`

### 139. [eigent-ai/eigent](https://github.com/eigent-ai/eigent) `⭐ 15,452`
- **能帮你干啥**：它可以让我以完全开源、本地私有化且免费的方式，在桌面端调度多智能体协同工作并接入任意模型，安全高效地自动化执行复杂的开发与日常工作流。
- **项目一句话**：Eigent: The Open Source Cowork Desktop - Local and Free Alternative to Claude Cowork and Codex
- **搜索标签**：`codex`

### 140. [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) `⭐ 12,627`
- **能帮你干啥**：它能为你提供一个统一的桌面工作区与可视化看板，通过环境隔离与全局编排并行调度多个 AI 编码助手，助你轻松掌控从需求拆解到 PR 合并的全流程，彻底解决多 Agent 协作时的上下文污染与分支冲突痛点。
- **项目一句话**：Run and supervise teams of coding agents from planning to merge. Any harness (Claude code, codex, +25 more). Desktop, web, mobile, and cloud agents.
- **搜索标签**：`codex`

### 141. [spinabot/brigade](https://github.com/spinabot/brigade) `⭐ 11,208`
- **能帮你干啥**：它能让你在无需依赖第三方SaaS且完全掌控数据隐私的前提下，在本地自主编排具备持久共享记忆、多渠道交互与丰富工具集成的企业级多智能体团队。
- **项目一句话**：Brigade — Your personal intelligence, built enterprise-grade
- **搜索标签**：`codex`

---

## 🌐 5. 想让 AI 自动联网搜资料、爬网页（全网调研 & 浏览器自动化）
> 💡 **怎么用**：核心用途：让智能体自己上网找最新资料、绕过反爬把任意网页洗成干净的 Markdown 格式。

### 142. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) `⭐ 250,838`
- **能帮你干啥**：为你提供一个无需受限于本地设备、能在多平台低成本运行，并通过自主沉淀技能与长期记忆实现越用越聪明的自我进化型 AI 助手。
- **项目一句话**：The agent that grows with you
- **搜索标签**：`codex & agent`

### 143. [browser-use/browser-use](https://github.com/browser-use/browser-use) `⭐ 117,030`
- **能帮你干啥**：它可以让你的 AI 智能体像真人一样自主浏览与操作网页，无需编写繁琐的传统自动化脚本即可高效完成数据查询、表单填写与验证码处理等复杂网络任务。
- **项目一句话**：Agents that use the browser.
- **搜索标签**：`agent`

### 144. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) `⭐ 109,560`
- **能帮你干啥**：该项目为你提供了一套模拟真实专业投研机构的多智能体协同框架，助你借助大模型全自动完成从多维度市场分析、多空博弈到风控决策的全流程量化交易与严谨回测。
- **项目一句话**：TradingAgents: Multi-Agents LLM Financial Trading Framework
- **搜索标签**：`agent`

### 145. [karpathy/autoresearch](https://github.com/karpathy/autoresearch) `⭐ 97,173`
- **能帮你干啥**：它能替你自动化完成繁琐的模型调优与架构探索，让 AI 智能体在单卡上自主进行代码修改、实验与评估的迭代闭环，使你无需人工干预即可持续获得性能更优的语言模型。
- **项目一句话**：AI agents running research on single-GPU nanochat training automatically
- **搜索标签**：`agent`

### 146. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) `⭐ 89,142`
- **能帮你干啥**：它能以零 API 成本和极简的一键配置，为我的 AI Agent 赋予自由检索与阅读推特、小红书、YouTube 等全网主流平台内容的能力，彻底免去手动对抗风控反爬与维护各类接口的繁琐负担。
- **项目一句话**：Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.
- **搜索标签**：`agent`

### 147. [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) `⭐ 84,668`
- **能帮你干啥**：它能帮你轻松搞定复杂动态网页的抓取与反爬，直接将任意网站转换为专供大模型使用的干净 Markdown 和结构化数据，大幅降低 RAG 与 AI Agent 开发中的数据处理成本。
- **项目一句话**：Open-source web crawler and scraper for LLMs and AI agents: any website into clean, LLM-ready Markdown. Run it yourself, or use Crawl4AI Cloud with one key.
- **搜索标签**：`agent`

### 148. [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) `⭐ 73,343`
- **能帮你干啥**：它能在本地智能评估职位匹配度并定制简历与申请材料，帮我告别盲目海投、显著提高求职效率与面试成功率。
- **项目一句话**：Open-source AI job search agent and job finder: scan job boards, score each job 1-5 against your CV before you apply, tailor an ATS-friendly resume and cover letter, get interview prep and a job application tracker. It helps you fill in each application; you press Submit. Runs locally in your AI coding CLI (Claude Code, Codex, OpenCode and more).
- **搜索标签**：`codex & agent`

### 149. [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) `⭐ 56,426`
- **能帮你干啥**：通过聚合数十家合规服务商的海量免费 Token 额度，让我能在终端、IDE 或浏览器中零成本无缝运行 Claude Code、Codex 等主流 AI 编程智能体，彻底解决高昂的 API 费用并提供自动容灾与消耗优化。
- **项目一句话**：Use Claude Code, Codex, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)
- **搜索标签**：`codex`

### 150. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) `⭐ 52,897`
- **能帮你干啥**：它能将 Chrome 开发者工具的完整能力接入我的 AI 编程助手，帮我自动化完成真实浏览器环境下的前端深度调试、页面交互与性能分析。
- **项目一句话**：Chrome DevTools for coding agents
- **搜索标签**：`agent`

### 151. [microsoft/qlib](https://github.com/microsoft/qlib) `⭐ 49,104`
- **能帮你干啥**：它能为你提供覆盖因子挖掘、模型训练到回测部署的全流程AI量化投资研发平台，借助前沿机器学习技术与自动化智能体大幅提升策略研发效率与落地能力。
- **项目一句话**：Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process.
- **搜索标签**：`agent`

### 152. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) `⭐ 43,470`
- **能帮你干啥**：它为你提供了一个轻量极速的命令行工具，让 AI Agent 能够通过精准的无障碍树节点引用和低 Token 消耗的快照感知，免去编写繁杂自动化代码即可高可靠地操控浏览器。
- **项目一句话**：Browser automation CLI for AI agents
- **搜索标签**：`agent`

### 153. [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) `⭐ 27,585`
- **能帮你干啥**：它通过直观的智能体待处理提醒、富上下文侧边栏与内嵌可编程浏览器，为你解决并行运行多个 AI 编程智能体时难以追踪与频繁切换的痛点，提供流畅高效的原生终端多任务协作体验。
- **项目一句话**：Open source Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agents. Built for multitasking, organization, and programmability.
- **搜索标签**：`codex`

### 154. [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) `⭐ 13,918`
- **能帮你干啥**：让你摆脱本地命令行的限制，随时随地在手机或任意浏览器中通过直观的可视化界面远程管理与操控 Claude Code、Cursor CLI 等 AI 编程助手及项目。
- **项目一句话**：Use Claude Code, OpenCode, Cursor CLI, and Codex on mobile and web with CloudCLI (aka Claude Code UI). CloudCLI is a free open source webui/GUI that helps you manage your Claude Code session and projects remotely.
- **搜索标签**：`codex`

---

## 🔄 6. 手头一堆 API Key 想一键切换、集中管理（模型切换器 & 桌面网关）
> 💡 **怎么用**：核心用途：多模型（Claude、Codex、Gemini等）供应商秒级切换，集中管理各种 API Key 与 MCP 插件。

### 155. [farion1231/cc-switch](https://github.com/farion1231/cc-switch) `⭐ 139,656`
- **能帮你干啥**：它可以让我一键切换主流 AI 编程助手的 API 供应商，并一站式集中管理 MCP、Skills 与提示词，彻底告别手动修改复杂配置文件的繁琐操作。
- **项目一句话**：A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **搜索标签**：`codex & agent`

### 156. [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) `⭐ 109,238`
- **能帮你干啥**：它能在不影响代码质量的前提下，通过消除 AI 编码助手的客套废话并压缩上下文输入，为你大幅削减高达 65% 的 Token 消耗与使用成本。
- **项目一句话**：🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
- **搜索标签**：`agent`

### 157. [bytedance/deer-flow](https://github.com/bytedance/deer-flow) `⭐ 83,342`
- **能帮你干啥**：它能为你提供一套开箱即用的超级智能体编排框架，通过协同子智能体、沙箱执行与长效记忆，助你自动化、高可靠地搞定耗时数分钟至数小时的复杂深度调研、编程开发与内容创作任务。
- **项目一句话**：An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **搜索标签**：`agent`

### 158. [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) `⭐ 74,312`
- **能帮你干啥**：它能在数据发送给大模型前于本地智能压缩冗长的工具输出与上下文，在完全不影响回答质量的前提下为你大幅降低 Token 消耗并节省 API 成本。
- **项目一句话**：Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **搜索标签**：`agent`

### 159. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) `⭐ 72,458`
- **能帮你干啥**：它能通过单一接口为你聚合数百家AI供应商的海量免费额度，并结合自动故障转移与极高比例的Token压缩技术，让你在主流AI开发工具中以零成本或极低成本享受永不中断的顶级大模型编码体验。
- **项目一句话**：Never stop coding. Free MIT AI gateway: one endpoint, 359 providers (150+ free), 1200+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by hundreds of contributors
- **搜索标签**：`codex`

### 160. [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) `⭐ 53,937`
- **能帮你干啥**：它可以将各种 CLI 工具与平台账户统一转换为兼容 OpenAI、Claude 和 Gemini 的标准 API 接口，让我能在任意第三方客户端或代码中直接调用并畅享各家主流前沿大模型。
- **项目一句话**：Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build, Muse Code, Devin as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini Series, GPT Series, Grok Series, Claude model through API
- **搜索标签**：`codex`

### 161. [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat) `⭐ 45,209`
- **能帮你干啥**：为你提供一个完全自主可控的一站式 AI 交互平台，不仅能自由聚合与切换所有商业及本地大模型，还能开箱即用智能体、沙盒代码执行与 MCP 扩展等高级生产力工具。
- **项目一句话**：Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active
- **搜索标签**：`agent`

### 162. [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) `⭐ 18,603`
- **能帮你干啥**：它能帮我一站式集中管理多款主流 AI IDE 的多个账号，通过一键无缝切号、实时配额监控与多实例隔离运行，彻底解决频繁切换登录的繁琐并最大化利用 AI 编程额度。
- **项目一句话**： 🚀 通用 AI IDE 账号管理工具：支持 Antigravity / Codex / GitHub Copilot / Windsurf / Kiro / Cursor / Gemini-cli / CodeBuddy，多账号切换、配额监控、自动唤醒与多开实例管理。 🚀 Universal AI IDE account manager for Antigravity / Codex / GitHub Copilot / Windsurf / Kiro / Cursor / Gemini-cli / CodeBuddy, with multi-account switching, quota monitoring, wake-up automation, and multi-insta
- **搜索标签**：`codex`

### 163. [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) `⭐ 16,840`
- **能帮你干啥**：它可以让我打破厂商生态限制，在 Codex、Claude Code 等主流 AI 编程工具中无缝调用 DeepSeek、Claude 或本地 Ollama 等任意大模型，并通过多账号池化管理解决额度限制与故障转移痛点。
- **项目一句话**：Universal provider proxy for OpenAI Codex & Claude Code — use any LLM (Claude, Gemini, Grok, DeepSeek, Ollama…) with Codex CLI, App, SDK, and Claude Code
- **搜索标签**：`codex`

---

## 🛡️ 7. 怕 AI 乱删库乱执行命令、想要安全评测（安全沙箱 & 评测门禁）
> 💡 **怎么用**：核心用途：把 AI 关进沙箱里跑命令，防止 rm -rf 事故，或者自动化评测不同模型和智能体的表现。

### 164. [infiniflow/ragflow](https://github.com/infiniflow/ragflow) `⭐ 91,619`
- **能帮你干啥**：它能帮你精准解析各类复杂多源文档并融合 Agent 深度检索能力，轻松构建有据可查、极低幻觉且开箱即用的生产级 RAG 应用。
- **项目一句话**：RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs
- **搜索标签**：`agent`

### 165. [jumpserver/jumpserver](https://github.com/jumpserver/jumpserver) `⭐ 31,707`
- **能帮你干啥**：为我提供一个集成 AI 能力的统一特权访问管理平台，实现对服务器、数据库、Kubernetes 及远程桌面等多协议 IT 资产的一站式安全访问与运维审计。
- **项目一句话**：JumpServer is an Open-source Privileged Access Management (PAM) platform with AI-powered capabilities, providing DevOps and IT teams a unified workspace to securely access SSH, RDP, Kubernetes, databases, websites, RemoteApp, VirtualApp, and more.
- **搜索标签**：`codex`

### 166. [oraios/serena](https://github.com/oraios/serena) `⭐ 29,954`
- **能帮你干啥**：它能为我的 AI 编程助手赋予 IDE 级别的符号理解与重构能力，告别脆弱易错的纯文本编辑，在大型复杂代码库中实现更快速、精准且可靠的跨文件代码检索与修改。
- **项目一句话**：A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for your agent
- **搜索标签**：`codex`

### 167. [openai/codex-security](https://github.com/openai/codex-security) `⭐ 10,957`
- **能帮你干啥**：它可以帮助你通过 CLI 或 TypeScript SDK 全流程自动化地发现、验证并修复代码安全漏洞，大幅提升代码安全审查与合规策略落地的效率。
- **项目一句话**：OpenAI's Codex Security CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities. npm: https://www.npmjs.com/package/@openai/codex-security
- **搜索标签**：`codex`

### 168. [google/artemis](https://github.com/google/artemis) `⭐ 10,895`
- **能帮你干啥**：它能让我直接在常用 AI 编程助手中通过自然语言驱动真实 Android 设备，以超高成功率自动完成跨 App 端到端测试与诊断排障，无需再繁琐编写和维护脆弱的自动化脚本。
- **项目一句话**：ARTEMIS turns natural-language instructions into reliable Android automation. It automates end-to-end workflows, captures logs, and integrates seamlessly with AI coding assistants such as Antigravity, Codex, and Claude Code.  It also achieves 99%+ success rate on AndroidWorld Benchmark.
- **搜索标签**：`codex`

### 169. [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) `⭐ 10,428`
- **能帮你干啥**：它能让我无需重写代码即可统一编排与自由切换 Claude Code、Cursor 等多种主流及自定义 AI Agent，并在任意设备上轻松实现安全沙盒隔离与跨端实时协作。
- **项目一句话**：Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.
- **搜索标签**：`codex`

---

## 🏢 8. 垂直场景专用智能体（特定行业 & 业务自动化）
> 💡 **怎么用**：核心用途：针对特定业务垂直领域（如面试刷题、量化金融、特定软硬件操控）定制的拿来即用工具。

### 170. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) `⭐ 89,838`
- **能帮你干啥**：它能为你提供一个可自托管的统一控制中心，跨本地与云端自由调度各类 AI 编程智能体，全天候自动化执行日常开发任务与工程工作流。
- **项目一句话**：🙌 OpenHands: AI-Driven Development
- **搜索标签**：`agent`

### 171. [unslothai/unsloth](https://github.com/unslothai/unsloth) `⭐ 77,156`
- **能帮你干啥**：让你通过开箱即用的桌面应用，以节省70%显存和两倍速度的高效表现，在本地轻松运行、微调与部署各类主流大语言模型及扩散模型。
- **项目一句话**：Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4, MiniMax-H3, Gemma 4, FLUX and more.
- **搜索标签**：`agent`

### 172. [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) `⭐ 75,285`
- **能帮你干啥**：它可以让我无需编写复杂代码，通过统一的 Web 界面或命令行以极低的显存成本一站式完成上百种主流大语言及多模态模型的高效微调与推理部署。
- **项目一句话**：Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
- **搜索标签**：`agent`

### 173. [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) `⭐ 43,224`
- **能帮你干啥**：它能帮我将 Claude、OpenAI 等多平台 AI 订阅统一转化为标准 API，通过账号拼车共享大幅降低使用成本，并无缝接入各类原生开发工具。
- **项目一句话**：Sub2API 一站式开源中转服务，让 Claude、Openai 、Gemini、Grok订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。
- **搜索标签**：`codex`

### 174. [mindsdb/mindshub](https://github.com/mindsdb/mindshub) `⭐ 39,780`
- **能帮你干啥**：它能让你摆脱单一模型生态锁定，在一个可灵活部署的统一工作区中安全连接多源业务数据，自由调度商业与开源大模型来高效自动化知识工作及软件开发。
- **项目一句话**：The unified workspace where open-source models get things done for you.
- **搜索标签**：`codex`

---

## 🎨 9. 想让 AI 直接出前端设计、做原型和美化 UI（设计与多模态创意）
> 💡 **怎么用**：核心用途：直接让编程 Agent 充当设计师，产出符合审美的高保真交互原型、PPT、动效与多媒体素材。

### 175. [langgenius/dify](https://github.com/langgenius/dify) `⭐ 157,747`
- **能帮你干啥**：它让我能够在一个可视化的协作平台上轻松编排工作流、构建 RAG 并接入各类大模型，无需重构技术栈即可极速将 AI 原型推向生产环境。
- **项目一句话**：Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.
- **搜索标签**：`agent`

### 176. [microsoft/autogen](https://github.com/microsoft/autogen) `⭐ 61,248`
- **能帮你干啥**：它可以帮助我轻松构建并灵活编排能够自主运行或人机协同的多智能体（Multi-Agent）AI 应用，大幅降低复杂任务工作流的开发与原型验证门槛。
- **项目一句话**：A programming framework for agentic AI
- **搜索标签**：`agent`

### 177. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) `⭐ 43,145`
- **能帮你干啥**：它可以让你在使用 AI 编程助手时彻底告别粗糙生硬的通用图表和繁琐的 Figma 手工调整，直接生成兼具出版级美感、完美契合品牌调性且开箱即用的专业 HTML/SVG 图表。
- **项目一句话**：Editorial diagram design for Claude Code, Codex, GitHub Copilot, Factory Droid, and Pi. 42 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop.
- **搜索标签**：`codex`

### 178. [onlook-dev/onlook](https://github.com/onlook-dev/onlook) `⭐ 26,849`
- **能帮你干啥**：它可以让我像使用 Figma 等设计工具一样，通过可视化界面与 AI 辅助直接编辑与生成真实的 Next.js 代码，彻底消除设计原型与前端实现之间的脱节。
- **项目一句话**：The Developer Tool for Designers • An Open-Source AI-First Design tool • Visually build, style, and edit your code with AI • World's best, top-most agent recommended #1 Developer tool for Designers to design with Real Code.
- **搜索标签**：`codex`

---

## 总结统计
本速查清单共收录 **178** 个仓库，无任何删减，按 Star 数自上而下并结合用途归类。随时取用！