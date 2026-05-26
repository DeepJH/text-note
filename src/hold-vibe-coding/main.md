# 问题
- 问题是，model 的 注意力是有限的，如果窗口爆了，或者压缩了，那就会丢失细节。此时项目就失控了。
- 问题是，model 只是不断地泛化，而不是像人一样考虑实际，有核心，有个性。所以生成的代码中会有很多屎，如果屎多了，此时项目就失控了。
- vibe coding 使代码写出来容易。这样一来，隐藏在写代码背后的工程控制问题就暴露了出来。

# 解决方案思想
- 使用`/init`
- 整体图(例如字符树形图) + 注意力压缩枝剪(找出问题需要的范围)
- 切分为最小问题
- 使用task.md、progress.md、plan.md、proposal.md
- 不断交流，直到达成共识

# 外部
[部分具体实现：vibe-coding-guide/main.md](../../src/awesome-prompts/vibe-coding-guide/main.md)