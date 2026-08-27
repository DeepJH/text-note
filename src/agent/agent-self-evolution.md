# agent-self-evolution

## reference

### <https://www.eigent.ai/zh-CN/blog/self-evolved-agents>  

### <https://zhuanlan.zhihu.com/p/2022259769969255910>  

### <https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra10-Agent%E8%87%AA%E8%BF%9B%E5%8C%96.md>  

### Self-Evolving Agents - A Cookbook for Autonomous Agent Retraining

<https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining>  

这篇文章发布于 nov 4, 2025。对于现在（aug 27, 2026）来说并不太久。  
但是这玩意也太老套了，我早就想到了。不就是提示词版的强化训练嘛😑。  
![!\[alt text\](image.png)](.image/image.png)

总之，它就是设计了一个框架。  
`Baseline Agent`，`Human Feedback or LLM-as-judge`，`自优化loop` 是一个大循环。  
然后 `自优化loop` 里是一个小循环。`尝试优化提示词`，`测试`，`评估`。  
这样一来，人就可以不管，或者只需在大方向上指导一下即可。

### <https://arxiv.org/abs/2508.02085>

## usage
