# token-optimize

## 能力

- 心法
    - [x]自己一定要对项目有所掌控。
    - [ ]vibe vibe
    - [ ]并行化，独立运行
        - [ ]自测试推进开发
            - [ ]停下来的时候，查看它为什么停下来，然后给他手动安排好，自己测去
    
- 装备
    - [x]ECC
    - [x]superpowers
    
## 价格

- 单价低

    - [x]低价站
        - [x]低价分组
            - [x]次一级的模型
    - 缓存命中
        - `关闭 cc-switch 路由`是否有效？    
            - 对比结果
                - 无效
        - `参数设置`是否有效？
            - 无效
        - 版本
            - 试试 codex
                - 有效。解决。是cc的问题。傻逼cc，滚蛋。
- token少   

    - [/src/ecc-note/part/token-optimization.md](/src/ecc-note/part/token-optimization.md)
        - [x]降低自动压缩阈值
        - [x]记得压缩
            - [x]进入新阶段之前压缩
        - [x]不要开太多已经装上的东西
        - [x]复杂的、较为独立的任务用 subagent 并行工作，很快。简单任务可以用 subagent 串行工作，因为相互压缩传递上下文，很好。
    - `使用 headroom `是否有效？
            - 记录
                - 29 Jun 2026 不使用 hr
                - 30 Jun 2026 使用 hr
            - 对比结果
                - 对比中
                - 我觉得有用吧