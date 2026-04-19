# VSCode 插件推荐指南

> 精选实用插件，覆盖日常开发全场景。安装量数据来源于 VSCode 插件市场，仅供参考。

---

## 目录

- [通用必装](#通用必装)
- [AI / 效率工具](#ai--效率工具)
- [语言专属](#语言专属)
- [界面 & 主题](#界面--主题)
- [开发工具](#开发工具)
- [插件管理建议](#插件管理建议)
- [相关链接](#相关链接)

---

## 通用必装

### Prettier - Code formatter
- **描述**：支持多种语言的代码格式化工具
- **推荐理由**：一键统一代码风格，告别格式争论，团队必备

### ESLint
- **描述**：JavaScript / TypeScript 静态代码分析工具
- **推荐理由**：实时发现潜在 bug 和不规范写法，提升代码质量

### Error Lens
- **描述**：将错误和警告信息直接显示在代码行尾
- **推荐理由**：不用悬停就能看到报错详情，调试效率翻倍

### GitLens
- **描述**：增强版 Git 可视化工具
- **推荐理由**：行级 blame、提交历史、代码作者一目了然，排查问题利器

### Auto Rename Tag
- **描述**：修改 HTML/XML 开标签时自动同步修改闭标签
- **推荐理由**：改标签名不再需要手动改两处，减少遗漏

### Path Intellisense
- **描述**：文件路径自动补全
- **推荐理由**：import 和 require 时自动提示路径，告别拼写错误

### EditorConfig for VS Code
- **描述**：EditorConfig 配置文件支持
- **推荐理由**：跨编辑器统一缩进、换行等基础格式，团队协作基础保障

### Todo Tree
- **描述**：在侧边栏收集和展示所有 TODO / FIXME 注释
- **推荐理由**：全局追踪待办事项，不再遗漏任何注释标记

### Better Comments
- **描述**：分类高亮注释（警告、待办、查询等）
- **推荐理由**：让注释层次分明，关键信息一眼可见

---

## AI / 效率工具

### GitHub Copilot
- **描述**：GitHub 官方 AI 代码补全助手
- **推荐理由**：理解上下文生成整段代码，大幅提升编码速度（付费）

### Codeium
- **描述**：免费 AI 代码补全工具
- **推荐理由**：Copilot 的优秀免费替代品，支持多种语言

### Tabnine
- **描述**：AI 驱动的代码自动补全
- **推荐理由**：支持本地模型运行，数据不出本机，适合对隐私有要求的场景

### Regex Previewer
- **描述**：正则表达式实时预览与测试
- **推荐理由**：边写边看匹配结果，写正则不再靠猜

### Thunder Client
- **描述**：轻量级 API 测试客户端（类似 Postman）
- **推荐理由**：无需离开编辑器即可测试接口，内置在 VSCode 中

---

## 语言专属

### Python

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| Python | 微软官方 Python 支持 | 调试、测试、虚拟环境一站式管理 |
| Pylance | 高性能 Python 语言服务器 | 类型检查、智能补全、自动导入 |
| Ruff | 极速 Python Linter 和格式化器 | 比 Flake8 + isort + Black 快 10-100 倍 |

### JavaScript / TypeScript

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| JavaScript (ES6) code snippets | ES6+ 代码片段 | 快速生成常用代码结构 |
| Import Cost | 显示 import 包体积 | 实时看到引入模块的大小，避免过度依赖 |
| npm Intellisense | npm 模块路径补全 | require / import 时自动提示已安装的包 |

### Go

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| Go | Go 官方插件 | 调试、Lint、格式化、测试全覆盖 |

### Java

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| Extension Pack for Java | Java 开发扩展包 | 语言支持、Maven/Gradle、调试器打包安装 |
| Spring Boot Extension Pack | Spring Boot 开发套件 | 项目模板、Dashboard、属性提示一站式支持 |

### Rust

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| rust-analyzer | Rust 语言服务器 | 类型推断、代码补全、内联提示，Rust 开发标配 |
| crates | Cargo 依赖管理 | 查看 crate 版本、更新提示，管理依赖更方便 |

### C / C++

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| C/C++ | 微软官方 C/C++ 支持 | IntelliSense、调试、代码浏览一体化 |
| CMake Tools | CMake 构建支持 | 配置、构建、调试 CMake 项目一站式 |

### Vue

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| Vue - Official (Vue Language Features) | Vue 3 官方语言支持 | 模板补全、类型检查、SFC 高亮 |

### React

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| ES7+ React/Redux/React-Native snippets | React 全家桶代码片段 | 快速生成组件、hooks、Redux 模板代码 |

---

## 界面 & 主题

### 颜色主题

| 插件名称 | 风格 | 推荐理由 |
|---------|------|---------|
| One Dark Pro | Atom 经典深色 | 最流行的 VSCode 主题，久看不 fatigue |
| Dracula Official | 暗黑紫调 | 配色对比度高，适合长时间编码 |
| Catppuccin | 柔和粉彩 | 温暖护眼，配色细腻 |
| Tokyo Night | 东京夜景蓝紫 | 清新不刺眼，现代感强 |
| GitHub Theme | GitHub 风格 | 与 GitHub 界面一致的熟悉感 |

### 图标主题

| 插件名称 | 风格 | 推荐理由 |
|---------|------|---------|
| Material Icon Theme | Material Design | 文件图标丰富，辨识度高 |
| vscode-icons | 经典图标集 | 支持文件类型最广 |

### UI 增强

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| Indent Rainbow | 缩进层级彩色显示 | 嵌套代码一目了然，告别缩进错误 |
| Bracket Pair Colorizer（内置） | 括号配对着色 | VSCode 内置，在设置中开启即可 |
| Code Spell Checker | 英文拼写检查 | 变量名拼写错误实时提醒 |
| Peacock | 为不同窗口设置不同颜色 | 多项目同时打开时快速区分 |

---

## 开发工具

### Docker & 容器

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| Docker | Docker 文件高亮、镜像/容器管理 | 可视化管理容器和镜像 |
| Dev Containers | 在容器中开发 | 环境一致性保障，团队开发体验统一 |

### Git 增强

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| GitGraph | Git 分支图可视化 | 图形化查看提交历史和分支关系 |
| GitHub Pull Requests and Issues | PR 和 Issue 管理 | 在编辑器内 Review 代码、管理 Issue |
| GitLens | （见通用必装） | 行级 Git 信息，无可替代 |

### 测试

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| Jest Runner | 快速运行 Jest 测试 | 点击 CodeLens 即可运行单个测试 |
| Vitest | Vitest 测试支持 | Vite 生态首选测试框架 |
| Coverage Gutters | 测试覆盖率行级显示 | 直接在编辑器看到哪些行被覆盖 |

### 远程开发

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| Remote - SSH | SSH 远程开发 | 像本地一样编辑远程服务器代码 |
| Remote - WSL | WSL 集成开发 | Windows 下使用 Linux 开发环境 |
| Remote - Tunnels | 安全隧道远程访问 | 无需 SSH 配置即可远程开发 |

### API & 数据库

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| REST Client | 用 .http 文件测试 API | 纯文本记录接口用例，版本可控 |
| MongoDB for VS Code | MongoDB 管理 | 在编辑器内连接和查询 MongoDB |
| SQLTools | 多数据库连接工具 | 支持 MySQL、PostgreSQL、SQLite 等 |

### 其他实用工具

| 插件名称 | 描述 | 推荐理由 |
|---------|------|---------|
| Live Server | 本地静态服务器 + 热重载 | 前端开发实时预览，保存即刷新 |
| Live Share | 实时协作编程 | 远程结对编程、Code Review 利器 |
| Markdown All in One | Markdown 编辑增强 | 快捷键、TOC 生成、预览一体化 |
| Draw.io Integration | 流程图绘制 | 在 VSCode 内直接画架构图 |
| Image Preview | 图片缩略图预览 | 侧边栏和 gutter 显示图片预览 |
| Project Manager | 多项目管理 | 快速切换不同项目工作区 |

---

## 插件管理建议

### 性能优化

- **按需安装**：不要一次装完所有插件，用到什么装什么
- **定期清理**：禁用 30 天未使用的插件，减少内存占用
- **工作区隔离**：通过工作区设置（`.vscode/extensions.json`）只推荐当前项目需要的插件
- **启动慢排查**：使用 `Help > Start Performance Troubleshooting` 定位拖慢启动的插件

### 团队协作

- **统一配置**：在项目根目录创建 `.vscode/settings.json` 和 `.vscode/extensions.json`
- **推荐插件列表**：在 `extensions.json` 的 `recommendations` 字段列出团队必备插件
- **代码风格统一**：配合 `.editorconfig` + Prettier + ESLint 确保全团队输出一致

### 推荐配置示例

```jsonc
// .vscode/extensions.json
{
  "recommendations": [
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint",
    "eamodio.gitlens",
    "streetsidesoftware.code-spell-checker"
  ]
}
```

---

## 相关链接

- [VSCode 插件市场](https://marketplace.visualstudio.com/vscode)
- [VSCode 官方文档](https://code.visualstudio.com/docs)
- [VSCode 快捷键速查](https://code.visualstudio.com/docs/getstarted/keybindings)
- [Open VSX（开源插件市场）](https://open-vsx.org/)

---

> 💡 **提示**：插件安装量数据来源于 VSCode 插件市场，会随时间变化。推荐以实际使用体验为准。
