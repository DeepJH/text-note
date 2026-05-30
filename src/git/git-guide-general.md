# git-guide-general

Git 是目前全球最主流的**分布式版本控制系统**。简单来说，它就像是写代码时的“游戏存档管理器”，让你可以在写砸了的时候随时“读档”，或者和团队成员分工合作而不互相覆盖。

为了让你快速上手，我把 Git 的核心用法整理成了以下几个核心场景：

---

## 1. 核心概念（四大工作区域）

在使用 Git 之前，理解这四个区域至关重要：

* **Workspace（工作区）**：你电脑上正在实际修改的代码目录。
* **Index / Stage（暂存区）**：准备提交的临时保存区域，像一个快递打包盒。
* **Repository（本地仓库）**：存放在本地的安全加密数据库，记录了所有历史版本。
* **Remote（远程仓库）**：托管在云端（如 GitHub, GitLab, Gitee）的代码库，用于团队协作。

---

## 2. 最常用的基础指令（单人开发常用）

### 初始化与配置

如果你是第一次使用 Git，需要先告诉 Git 你是谁：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"

```

* **新建本地仓库**：进入项目文件夹，运行 `git init`。
* **克隆远程项目**：`git clone <远程仓库URL>`。

### 提交流程（最经典的三板斧）

1. **查看当前状态**：看看有哪些文件被修改了。
```bash
git status

```


2. **添加至暂存区**：把修改过的文件放进“打包盒”。
```bash
git add file.txt      # 添加指定文件
git add .             # 添加当前目录下所有修改过的文件

```


3. **提交到本地仓库**：正式生成一个历史版本（存档）。
```bash
git commit -m "这次提交的修改说明（比如：修复了登录Bug）"

```



---

## 3. 分支管理（团队协作的核心）

分支（Branch）允许你在不影响主线代码（通常是 `main` 或 `master`）的情况下开发新功能。

* **查看所有分支**：`git branch`
* **创建新分支**：`git branch <新分支名>`
* **切换到该分支**：`git checkout <分支名>` （新版 Git 推荐使用 `git switch <分支名>`）
* **创建并直接切换**：`git checkout -b <新分支名>` （新版：`git switch -c <新分支名>`）
* **合并分支**：先切换回主分支，然后把新分支合并进来。
```bash
git switch main
git merge <新分支名>

```


* **删除分支**（通常在合并后）：`git branch -d <分支名>`

---

## 4. 与远程仓库交互（同步代码）

当你的本地代码需要上传到 GitHub 或拉取同事的代码时：

* **关联远程仓库**（如果本地是新建的库）：
```bash
git remote add origin <远程仓库URL>

```


* **推送本地代码到远程**：
```bash
git push origin <分支名>

```


*(第一次推送主分支通常用 `git push -u origin main`，以后直接 `git push` 即可)*
* **拉取远程最新代码并合并**：
```bash
git pull

```


* **只获取远程更新但不合并**：`git fetch` （更安全，可以先查看变化再决定是否合并）

---

## 5. 后悔药：撤销与回滚

代码写烂了？别慌，Git 有的是办法帮你找回来：

* **改动还没加到暂存区，想丢弃工作区的修改**：
```bash
git checkout -- <文件名>  # 新版：git restore <文件名>

```


* **已经 `git add` 了，想从暂存区撤回来（保持文件内容不变）**：
```bash
git reset HEAD <文件名>   # 新版：git restore --staged <文件名>

```


* **已经 `git commit` 了，想彻底回退到某一个历史版本**（慎用，会抹去后面的提交）：
```bash
git log                  # 先查看历史提交的 commit ID
git reset --hard <commit-id>

```



---

## Git 常用命令速查表

| 命令 | 作用 |
| --- | --- |
| `git init` | 在当前目录初始化一个 Git 仓库 |
| `git status` | 查看当前工作区和暂存区的状态 |
| `git diff` | 查看具体修改了哪些代码内容 |
| `git log` | 查看历史提交记录 |
| `git rm <file>` | 从版本库中删除文件 |

要不要聊聊你当前是准备从零开始建一个新项目，还是准备克隆现有的代码库来开发？