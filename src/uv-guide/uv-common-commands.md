`uv` 是由 Astral 开发的高性能 Python 包和项目管理器（用 Rust 编写）。它的速度极快，旨在替代 `pip`、`pip-tools` 和 `venv`。

以下是 `uv` 的常用指令分类指南：

---

## 1. 项目管理 (uv project)
这是目前最推荐的使用方式，类似于 Rust 的 `cargo` 或 Node.js 的 `npm`。

* **初始化新项目**：
    `uv init my-project`
    （创建一个包含 `pyproject.toml` 的基础项目结构）
* **添加依赖**：
    `uv add requests`
    （自动同步到 `pyproject.toml` 并更新环境）
* **移除依赖**：
    `uv remove requests`
* **运行脚本/命令**：
    `uv run main.py`
    （会自动在当前项目的虚拟环境中执行）
* **锁定依赖版本**：
    `uv lock`
    （生成或更新 `uv.lock` 文件）

---

## 2. 工具与 Python 版本管理
`uv` 可以直接管理 Python 解释器，你甚至不需要提前安装 Python。

* **安装指定版本的 Python**：
    `uv python install 3.12`
* **查看已安装的 Python**：
    `uv python list`
* **临时运行一个工具**（无需安装）：
    `uvx ruff check .`
    （`uvx` 是 `uv tool run` 的简写，类似于 `npx`）

---

## 3. 虚拟环境管理 (uv venv)
如果你更习惯传统的虚拟环境工作流：

* **创建虚拟环境**：
    `uv venv`
    （默认在 `.venv` 目录下创建）
* **指定 Python 版本创建**：
    `uv venv --python 3.11`
* **激活环境**：
    * Windows: `.venv\Scripts\activate`
    * macOS/Linux: `source .venv/bin/activate`

---

## 4. 兼容 Pip 的指令 (uv pip)
如果你只是想把 `uv` 当作极速版的 `pip` 来用，可以使用 `uv pip` 子命令：

* **安装包**：
    `uv pip install -r requirements.txt`
* **安装特定包**：
    `uv pip install flask`
* **查看已安装包**：
    `uv pip list`
* **生成静态依赖清单**：
    `uv pip compile pyproject.toml -o requirements.txt`
* **同步环境**（删除多余包）：
    `uv pip sync requirements.txt`

---

## 5. 缓存与更新
* **查看缓存路径**：
    `uv cache dir`
* **清理缓存**：
    `uv cache clean`
* **更新 uv 自身**：
    `uv self update`

### 💡 小贴士
> 在大多数情况下，直接使用 **`uv run`** 是最省心的。即使你没有创建虚拟环境，`uv run` 也会根据 `pyproject.toml` 自动帮你处理好一切。

你目前是打算将旧项目迁移到 `uv`，还是准备开启一个全新的项目？