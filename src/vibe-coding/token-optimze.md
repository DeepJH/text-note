# token-optimize

## 能力

- 自己一定要对项目有所掌控。
- ECC

## 价格

- 单价低

    - 低价站
        -低价分组
            -次一级的模型
    - 缓存命中
        - headroom这种是否有效？
            - 记录
                - 29 Jun 2026 使用 hr
                - 30 Jun 2026 不使用 hr
            - 对比结果
                - 对比中
    
- token少

    - [/src/ecc-note/part/token-optimization.md](/src/ecc-note/part/token-optimization.md)
        - 降低自动压缩阈值
        - 记得压缩
            - 进入新阶段之前压缩
        - 不要开太多已经装上的东西
        - 复杂的、较为独立的任务用 subagent 并行工作，很快。简单任务可以用 subagent 串行工作，因为相互压缩传递上下文，很好。
