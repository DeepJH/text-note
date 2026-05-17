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


* **第二步：简单设计（详细设计 Design）** [[04:55](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=295)]
    * **技巧：** 基于上一步的文档，让 AI 将系统划分为独立的模块（如 CPU、PPU、ROM 加载等）。
    * **新建对话：** 此时应**新开一个 AI 会话**，只把核心的 `proposal.md` 喂给 AI，保持上下文简短，防止 token 消耗过大和 AI 产生幻觉 [[06:17](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=377)]。
    * **产物：** 生成详细的设计文档 [[06:55](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=415)]。


* **第三步：任务拆解（Tasks）** [[07:44](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=464)]
    * **技巧：** 命令 AI 为每个模块生成单边缘任务清单（Checklist），并生成一个 `progress.md` 记录整体进度 [[07:52](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=472)]。


* **第四步：代码实现（Coding - 主/子 Agent 架构）** [[08:38](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=518)]
    * **架构：** 为了避免单会话因上下文过长而导致 AI 自动压缩总结、遗漏代码细节，博主命令编程工具（如 Claude Code）采用 **“1 个主监督 Agent + N 个子编程 Agent”** 的架构 [[09:17](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=557)]。
    * **约束：** 要求子 Agent 编写的每行代码都必须有对应的单元测试，且必须通过 `mypy` 和 `ruff` 检查 [[10:13](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=613)]。



### 3. 最终成果与验证 [[11:46](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=706)]

* AI 在大约 15 分钟内完成了模拟器的编写。
* 运行测试表明模拟器完全可行，可以成功跑起超级马里奥（虽然帧率稍慢，不到 60 帧）[[11:57](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=717)]。
* 最终生成的代码结构极为清晰，模块一一对应，跑 `mypy` 和 `ruff` 顺利通过，且 **196 个单元测试全部通过** [[12:36](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=756)]。

### 💡 核心金句/总结

* **“有了这些测试和检查，未来的持续开发中，AI 才不会在增加新功能的时候，破坏原有的功能。”** [[12:44](https://www.youtube.com/watch?v=ytT4-lGEf6A&t=764)]  
* 用嘴写代码不等于盲目乱试，而是要把人类程序员在传统软件工程中积累的经验（如需求分析、模块化设计、单元测试、CI 检查）作为限制条件架设给 AI，才能让 AI 稳定产出高质量的复杂工程。  
* *YouTube 视频观看记录会存储在你的 YouTube 历史记录中，YouTube 会根据其 [《服务条款》](https://www.youtube.com/static?template=terms) 存储和使用你的数据*