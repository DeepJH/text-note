# agent-self-evolution

## catlog

- [agent-self-evolution](#agent-self-evolution)
  - [catlog](#catlog)
  - [reference](#reference)
    - [Agent Self-Evolution：智能体自进化的四类闭环⭐](#agent-self-evolution智能体自进化的四类闭环)
      - [概述](#概述)
    - [Self-Evolving Agents - A Cookbook for Autonomous Agent Retraining⭐](#self-evolving-agents---a-cookbook-for-autonomous-agent-retraining)
    - [文章3](#文章3)
    - [文章4](#文章4)
    - [文章5](#文章5)
  - [usage](#usage)

## reference

### Agent Self-Evolution：智能体自进化的四类闭环⭐

<https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra10-Agent%E8%87%AA%E8%BF%9B%E5%8C%96.md>  

#### 概述

Agent Self-Evolution 和 memory `是不一样的`。Agent Self-Evolution 是`提升能力`。而 memory 是`记住事情`。

1. 经验驱动：更新来自真实任务、执行反馈、用户纠错、评测结果或环境信号，而不是一次性人工配置。
2. 持续生效：更新会进入记忆、技能库、工作流、代码或参数中，在未来任务继续发挥作用。
3. 可评估、可回滚：`越强的自进化越需要``评估器`、`版本记录`、`沙箱`、`权限控制`和`回滚机制`。
   - 评估器：能够`判断好坏`。从而确保 agent 是在综合地`正向进步`，而`不是进步幻觉或自嗨`。
   - 版本记录：能够`回去看`，不至于`怎么变成这样`（怎么好，怎么坏）的都不知道
   - 沙箱：做好隔离，`防止出问题了污染得到处都是`。（无直接关系，本来就要做好，但是防止进化坏了，还是要注意一点）
   - 权限控制：最小权限，`防止出问题了到处乱用权限`。（无直接关系，本来就要做好，但是防止进化坏了，还是要注意一点）
   - 回滚机制：保守地暴露，`出了问题立即回滚兜底`。

### Self-Evolving Agents - A Cookbook for Autonomous Agent Retraining⭐

<https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining>  

这篇文章发布于 nov 4, 2025。对于现在（aug 27, 2026）来说并不太久。  
但是这玩意也太老套了，我早就想到了。不就是提示词版的强化训练嘛😑。  

![!\[!\\[alt text\\](image.png)\](.image/image.png)](.image/openai-ase-framework.png)

总之，它就是设计了一个框架。  

`Baseline Agent`，`Human Feedback or LLM-as-judge`，`自优化loop` 是一个大循环。  
然后 `自优化loop` 里是一个小循环。`尝试优化提示词`，`测试`，`评估`。  

这样一来，人就可以不管，或者只需在大方向上指导一下即可。

### 文章3

<https://www.eigent.ai/zh-CN/blog/self-evolved-agents>  

### 文章4

<https://zhuanlan.zhihu.com/p/2022259769969255910>  

### 文章5

<https://arxiv.org/abs/2508.02085>

## usage
