# npm-like-package-manager-compairsion

## 目录

- [npm-like-package-manager-compairsion](#npm-like-package-manager-compairsion)
  - [目录](#目录)
  - [结论](#结论)
  - [有哪些？](#有哪些)
    - [核心对比表](#核心对比表)
  - [选哪个？](#选哪个)
  - [大不大？（换不换？）](#大不大换不换)
  - [怎么换？](#怎么换)

## 结论

用 bun。或者 pnpm。怎么换见[#怎么换](#怎么换)

## 有哪些？

npm vs pnpm vs yarn vs bun vs deno

在 JavaScript 生态中，这五者可以分为两类：**npm、pnpm、Yarn** 是纯包管理器，而 **Bun** 和 **Deno** 则是集成了包管理功能的全栈 JavaScript 运行时（Runtime）。

### 核心对比表

| 工具 | 类型 | 核心优势 | 磁盘占用 | 适合场景 |
| --- | --- | --- | --- | --- |
| **npm** | 纯包管理器 | Node.js 原生内置，无需额外安装，生态最稳 | 高（重复安装） | 小型项目、初学者、不想折腾配置 |
| **pnpm** | 纯包管理器 | **全局硬链接**，节省磁盘空间，严格依赖隔离 | **极低** | 大型项目、Monorepo（多包管理） |
| **Yarn** | 纯包管理器 | 改进了旧版 npm 的体验，支持 Plug'n'Play (PnP) | 中/低 | 大型企业项目、已有 Yarn 配置的项目 |
| **Bun** | 运行时 + 工具链 | **极速**（用 Zig 编写），内置极快的包管理器 | 极低 | 追求极致安装与执行速度的项目 |
| **Deno** | 运行时 + 工具链 | 原生支持 TypeScript，基于 URL 引用，极高安全性 | 低 | 重视安全性、无需复杂的构建配置 |

## 选哪个？

* **一般商业项目 / Monorepo 架构：** 优先选择 **pnpm**（兼具速度、磁盘空间与安全性）。
* **个人新项目 / 追求极致性能：** 尝试 **Bun**（安装速度极快，兼顾打包与运行）。
* **对安全性要求极高 / 全 TS 栈：** 选择 **Deno**。
* **维护老项目 / 避免团队额外学习成本：** 继续使用 **npm** 或 **Yarn**。

## 大不大？（换不换？）

**1. 检查当前项目的 `node_modules` 大小**
在项目根目录运行命令：

* **Mac/Linux:** `du -sh node_modules`
* **Windows (PowerShell):** `(Get-ChildItem -Recurse node_modules | Measure-Object -Property Length -Sum).Sum / 1MB`

**2. 检查全局包管理器缓存**

* **pnpm 存储空间:** `pnpm store status`（查看全局 Store 占用的总大小及孤立包）
* **Bun 缓存空间:** `bun pm cache`（查看 Bun 的全局缓存路径及大小）
* **npm 缓存空间:** `npm cache verify`

**3. 查看具体是哪些依赖最占空间**

* **命令行可视化:** 使用 `npx npkill`，它会扫描你电脑里所有的 `node_modules`，按体积排序，并支持一键按空格键清理。

## 怎么换？

> 如果是 codex cli 这种 用npm 安装的软件。先卸载。再用对应 pm 装一遍就可以了。

**1. 删除现有产物与锁文件**
清理项目中的原生 `node_modules` 及旧的锁文件：

* 删除 `node_modules`
* 删除 `package-lock.json` 或 `yarn.lock`

**2. 生成新的锁文件并安装**
在项目根目录下直接运行：

* **迁移到 pnpm:**

```bash
pnpm import # (可选) 会自动根据现有的 lockfile 转换为 pnpm-lock.yaml
pnpm install

```

* **迁移到 Bun:**

```bash
bun install # 会自动读取 package.json 并生成 bun.lockb / bun.lock

```

**3. 修改 NPM 脚本（`package.json`）**
将 `package.json` 中的 `scripts` 调用的包管理器前缀替换：

* `npm run dev` 转换为 `pnpm dev` 或 `bun run dev`
* `npx <package>` 转换为 `pnpm dlx <package>` 或 `bunx <package>`

---

* **代码兼容性测试:** 运行 `pnpm test` / `bun test` 或启动开发服务，确保没有幽灵依赖（Ghost Dependencies）缺失问题（pnpm 的依赖隔离较为严格）。
* **配置打包器限制（仅 Bun）:** 如果是将 Bun 作为 **Runtime**（替代 Node.js 执行脚本），需注意部分使用 Node.js C++ 原生扩展的库可能存在兼容性差异；若仅将 Bun 作为**包管理器**使用，兼容性与 pnpm/npm 无异。
