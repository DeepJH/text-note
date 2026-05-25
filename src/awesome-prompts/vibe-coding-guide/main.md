# vibe-coding-guide

这视频的主题是**如何正确、高效地进行 “Vibe Coding”**，博主“程序员老王”以“从零开发一个 FC 模拟器（红白机）并运行超级马里奥”为例，详细讲解了如何通过系统化的工程方法，避免 AI 在面对复杂项目时写出“史山代码”或陷入上下文丢失的困境。

> 参考内容：[VibeCoding就该这么做！(YouTube)](https://www.youtube.com/watch?v=ytT4-lGEf6A)  
> Gemini 总结原文：[https://gemini.google.com/app/8818ce31cf14fd6f?hl=zh-cn](https://gemini.google.com/app/8818ce31cf14fd6f?hl=zh-cn)  
> 后期经过`DeepJH`大量手动编辑

## 核心内容和步骤总结如下：

### 1. 语言与工具的选择 [[01:04](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=64)]

* **语言选择：** 推荐 **Python、JavaScript 或 Rust**。  
    * Python 和 JS
        * 因为是 AI 的母语
        * 因为第三方库丰富
    * Rust
        * 语法严苛，质量好，但是超级难。  
            > 反正丢给AI了，难受的也不是你。enjoy 高质量代码吧~  
    
    > 示例中，博主最终选择了自己最熟悉的 **Python**。

* **环境配置：** 使用 `uv`   
    使用 `uv` 构建 Python 基础空工程并引入 `mypy`（类型检查）、`ruff`（语法检查）和 `pytest`（单元测试），用以约束 AI 代码的自由发挥 [[02:17](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=137)]。
    > 关于 uv ：(用uv管理Python的一切！)[https://www.youtube.com/watch?v=aVXs8lb7i9U]

### 2. 核心开发四步（标准 Prompt 结构）[[03:26](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=206)]

博主建议与 AI 沟通时，任何提示词都应包含四部分：**目标、输入、输出、步骤**。并以此展开了四个阶段：

* **第一步：简单设计（确定需求 Proposal）** [[03:11](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=191)]
    * **技巧：** 让 AI 主动提问。提示词中加入 **“我不了解相关知识，请用提问的方式帮助我确定需求，不要猜测我的意图”** [[04:03](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=243)]。
    * **产物：** 生成 `proposal.md` 需求文档 [[04:42](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=282)]。  
    
    [stage-1.png](images/stage-1.png)
    ```
    # 角色与任务
    你是一个经验丰富的软件架构师与AI开发助手。当前的任务是协助我完成一个用 Python 开发的 FC（NES）模拟器的需求文档。该模拟器的最终目标是能够成功运行《超级玛丽》（Super Mario Bros.）。

    # 已知输入
    1. 当前项目目录是一个使用 `uv` 管理的 Python 工程。
    2. 在 `rom` 目录下已经准备好了《超级玛丽》的 ROM 镜像。

    # 输出要求
    请在 `doc` 目录下生成需求文档，文件名为 `proposal.md`。

    # 执行步骤与严苛限制
    1. 我目前不了解任何关于 FC 模拟器开发的底层知识。
    2. 你必须使用【提问】的方式来逐步引导我，帮助我确认和梳理具体的需求。
    3. 【绝对禁止】猜测我的意图。任何不明确、不确定、或者有多种实现方案的地方，你必须向我提问，直到我们达成共识。
    4. 在开始生成 `doc/proposal.md` 之前，请先列出第一批你需要向我确认的核心问题。
    ```

* **第二步：简单设计（详细设计 Design）** [[04:55](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=295)]
    * **技巧：** 基于上一步的文档，让 AI 将系统划分为独立的模块（如 CPU、PPU、ROM 加载等）。
    * **新建对话：** 此时应**新开一个 AI 会话**，只把核心的 `proposal.md` 喂给 AI，保持上下文简短，防止 token 消耗过大和 AI 产生幻觉 [[06:17](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=377)]。
    * **产物：** 生成详细的设计文档 [[06:55](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=415)]。
    
    [stage-2.png](images/stage-2.png)
    ```
    # 角色与任务
    你是一个顶级的系统架构师。请根据已有的需求文档，为这个 Python 开发的 FC 模拟器生成概要设计（High-Level Design）文档。

    # 输入
    - 需求文档：`doc/proposal.md`（请阅读此文件内容）

    # 输出要求
    - 概要设计文档：`doc/high-level-design.md`

    # 执行步骤与严苛限制
    1. 深入阅读并根据需求文档的内容，合理划分出模拟器的核心模块（例如：CPU、PPU、APU、Bus、Controller 等）。
    2. 清晰识别并定义各个模块之间的调用关系与数据流向。
    3. 最终生成完整的 `doc/high-level-design.md`。
    4. 【绝对禁止】猜测我的意图。在模块划分、架构选择或任何不明确的地方，你必须立刻向我提问，确认后再继续。
    ```


* **第三步：任务拆解（Tasks）** [[07:44](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=464)]
    * **技巧：** 命令 AI 为每个模块生成单边缘任务清单（Checklist），并生成一个 `progress.md` 记录整体进度 [[07:52](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=472)]。

    [stage-3](images/stage-3.png)
    ```
    # 角色与任务
    你是一个敏捷开发专家与项目经理。我们需要将设计转化为可落地执行的开发任务。

    # 输入
    - 需求文档：`doc/proposal.md`
    - 详细设计文档：`doc/detailed-design.md`（注：通常在概要设计后生成，请结合现有设计文档进行）

    # 输出要求
    - 任务列表文件：
    1. `doc/tasks/<module-name>.md`（每个独立模块对应一个任务文件）
    2. `doc/tasks/progress.md`（整体进度跟踪文件）

    # 执行步骤
    1. 根据需求文档和详细设计文档，将每个模块拆解为适合 AI 进行 Vibe Coding（氛围感编码/全自动编码）的【最小可执行任务】。
    2. 为每一个模块生成对应的 `doc/tasks/<module-name>.md`，并在其中使用 Markdown 的 Check list（`- [ ]`）来表示子任务的完成状态。
    3. 生成全局的 `doc/tasks/progress.md`，并在其中使用 Check list 来表示各个大模块的整体完成进度。
    ```


* **第四步：代码实现（Coding - 主/子 Agent 架构）** [[08:38](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=518)]
    * **架构：** 为了避免单会话因上下文过长而导致 AI 自动压缩总结、遗漏代码细节，博主命令编程工具（如 Claude Code）采用 **“1 个主监督 Agent + N 个子编程 Agent”** 的架构 [[09:17](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=557)]。
    * **约束：** 要求子 Agent 编写的每行代码都必须有对应的单元测试，且必须通过 `mypy` 和 `ruff` 检查 [[10:13](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=613)]。

    [stage-4.png](images/stage-4.png)
    ```
    # 角色与任务
    你是一个精通 AI Agent 架构的提示词工程师。我们需要为全自动的 Vibe Coding 阶段生成一份核心启动提示词（System Prompt / Master Prompt）。

    # 输入
    - 需求文档：`doc/proposal.md`
    - 详细设计文档：`doc/detailed-design.md`
    - 任务划分文件：`doc/tasks/` 目录下的所有任务列表

    # 输出要求
    - 启动提示词文件：`doc/prompt.md`

    # 执行步骤与技术约束
    1. 阅读所有输入信息，深度理解当前要实现的项目工程（Python FC模拟器跑超级玛丽）。
    2. 生成 `doc/prompt.md`，该文件将作为后续 Vibe Coding 自动化执行的起始 Prompt。
    3. 提示词中必须包含并设计好以下 Agent 架构：
    - **主 Agent（Main Agent）**：负责全局统筹，跟踪并更新 `doc/tasks/progress.md` 中的整体进度。
    - **子 Agent（Sub Agent）**：由主 Agent 动态生成，专门用来实现某一个具体的模块代码，并负责运行和完成测试。
    - **自动化要求**：明确整个代码编写、测试、修复的过程将【完全没有人工参与】，要求 Agent 具备自主闭环能力。
    4. **代码质量硬性约束**：
    - 所有生成的 Python 代码必须附带完整的 `pytest` 单元测试。
    - 所有代码和测试必须无警告、无错误地通过 `mypy`（类型检查）和 `ruff`（代码风格与 Linter）的检测。
    5. 【严苛限制】：在生成此 prompt 的过程中，若有任何不明确或需要取舍的地方，必须向我提问，严禁自行猜测。
    ```



### 3. 最终成果与验证 [[11:46](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=706)]

* AI 在大约 15 分钟内完成了模拟器的编写。
* 运行测试表明模拟器完全可行，可以成功跑起超级马里奥（虽然帧率稍慢，不到 60 帧）[[11:57](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=717)]。
* 最终生成的代码结构极为清晰，模块一一对应，跑 `mypy` 和 `ruff` 顺利通过，且 **196 个单元测试全部通过** [[12:36](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=756)]。

### 💡 核心金句/总结

* **“有了这些测试和检查，未来的持续开发中，AI 才不会在增加新功能的时候，破坏原有的功能。”** [[12:44](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=764)]  
* 用嘴写代码不等于盲目乱试，而是要把人类程序员在传统软件工程中积累的经验（如需求分析、模块化设计、单元测试、CI 检查）作为限制条件架设给 AI，才能让 AI 稳定产出高质量的复杂工程。  
* *YouTube 视频观看记录会存储在你的 YouTube 历史记录中，YouTube 会根据其 [《服务条款》](https://www.youtube.com/static?template=terms) 存储和使用你的数据*