# uv 快速入门教程

> 面向 Python 开发者的现代包管理工具指南
> 推荐观看[视频](https://www.youtube.com/watch?v=jd1aRE5pJWc&t=175s)

---

## 1. 什么是 uv？

`uv` 是由 Astral（ruff 的同一团队）开发的极速 Python 包安装器和项目管理工具，用 Rust 编写。

```bash
# 传统方式 vs uv 方式
pip install requests          # 慢，无项目隔离
uv pip install requests       # 快 10-100 倍
uv add requests               # 现代项目管理方式（推荐）
```

**核心优势**：
- 🚀 **极速**：比 pip 快 10-100 倍，全局磁盘缓存
- 📦 **一体化**：替代 pip、pip-tools、virtualenv、pipx、pyenv
- 🔒 **可靠**：确定性锁定，可重复安装
- 🐍 **多版本**：自动管理多个 Python 版本
- 📝 **标准兼容**：完全支持 pyproject.toml（PEP 621）

---

## 2. 安装 uv

### 官方推荐方式

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用 pip
pip install uv

# 或使用 Homebrew（macOS）
brew install uv

# 或使用 Winget（Windows）
winget install --id=astral-sh.uv  --e
```

### 验证安装

```bash
uv --version
# uv 0.5.x
```

### 更新 uv

```bash
uv self update
```

---

## 3. 创建项目

> # **💡 提示** > 以下命令虽然简单完整，但是不够通用。如果你不是新手，建议参照[常用命令](uv-common-commands.md)以速查指令。
> # **💡 提示** > 如果你需要对一个项目使用uv，建议参照[兼容指南](uv-compatible.md)。
### 初始化新项目

```bash
# 创建项目（默认使用最新 Python 版本）
uv init my-project
cd my-project

# 项目结构
my-project/
├── pyproject.toml      # 项目配置（替代 setup.py/requirements.txt）
├── uv.lock             # 锁定文件（类似 pipfile.lock/poetry.lock）
├── README.md
└── .python-version     # Python 版本锁定（可选）
```

### 指定 Python 版本

```bash
# 创建项目时指定 Python 版本
uv init my-project --python 3.12

# 或在项目中切换 Python 版本
uv python install 3.12
uv python pin 3.12
```

---

## 4. 管理依赖

### 添加依赖

```bash
# 添加运行时依赖
uv add requests
uv add flask>=2.0
uv add "numpy>=1.24,<2.0"

# 添加开发依赖（类似 pip 的 extras）
uv add --dev pytest
uv add --dev black ruff mypy

# 对比传统方式:
# pip install requests                    # 无锁定
# pip freeze > requirements.txt           # 手动锁定
# pip install -r requirements.txt         # 重新安装
```

### 移除依赖

```bash
uv remove requests
uv remove --dev pytest
```

### 查看依赖

```bash
# 查看项目依赖
uv tree

# 查看已安装的包
uv pip list

# 查看某个包的信息
uv pip show requests
```

---

## 5. 虚拟环境管理

### 自动管理

```bash
# uv 自动创建和使用虚拟环境
uv run python main.py           # 在虚拟环境中运行
uv run pytest                   # 运行测试
uv run flask run                # 启动 Flask 应用

# 对比传统方式:
# python -m venv .venv          # 手动创建
# source .venv/bin/activate     # 手动激活
# python main.py                # 运行
```

### 手动管理虚拟环境

```bash
# 创建虚拟环境
uv venv

# 创建指定 Python 版本的虚拟环境
uv venv --python 3.11

# 激活虚拟环境（可选，uv run 不需要）
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

---

## 6. 运行脚本和工具

### 运行项目代码

```bash
# 运行 Python 脚本（自动使用项目虚拟环境）
uv run python src/main.py

# 运行模块
uv run -m http.server

# 运行已安装的命令行工具
uv run pytest
uv run black .
```

### 运行一次性脚本（无需项目）

```bash
# 直接运行 Python 脚本（自动下载依赖）
uv run script.py

# script.py 头部指定依赖:
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests", "rich"]
# ///

import requests
from rich import print
print("Hello!")
```

### 替代 pipx 运行工具

```bash
# 运行一次性工具（不安装到全局）
uvx ruff check .
uvx black .
uvx httpie

# 对比传统方式:
# pipx run ruff check .         # 需要 pipx
# pip install ruff && ruff .    # 需要手动安装
```

---

## 7. 锁定和安装

### 锁定依赖

```bash
# 生成锁定文件（类似 pip-compile/poetry lock）
uv lock

# 更新锁定文件
uv sync
```

### 安装依赖

```bash
# 安装所有依赖（包括开发依赖）
uv sync

# 只安装运行时依赖（生产环境）
uv sync --frozen --no-dev

# 安装指定 extras
uv sync --extra dev
```

### 更新依赖

```bash
# 更新所有依赖到最新兼容版本
uv lock --upgrade

# 更新特定依赖
uv lock --upgrade-package requests
```

---

## 8. Python 版本管理

### 安装和管理 Python 版本

```bash
# 查看可用的 Python 版本
uv python list

# 安装指定 Python 版本
uv python install 3.12
uv python install 3.11
uv python install 3.10

# 查看已安装的版本
uv python list --only-installed

# 移除 Python 版本
uv python uninstall 3.10
```

### 项目 Python 版本

```bash
# 设置项目使用的 Python 版本
uv python pin 3.12

# 查看当前项目 Python 版本
cat .python-version

# 运行项目时使用指定版本
uv run --python 3.12 python main.py
```

---

## 9. 工作流示例

### 从零开始创建项目

```bash
# 1. 创建项目
uv init my-web-app
cd my-web-app

# 2. 指定 Python 版本
uv python pin 3.12

# 3. 添加依赖
uv add flask
uv add --dev pytest gunicorn

# 4. 创建虚拟环境并安装依赖
uv sync

# 5. 运行开发服务器
uv run flask run

# 6. 运行测试
uv run pytest
```

### 克隆现有项目

```bash
# 1. 克隆项目
git clone https://github.com/example/my-project.git
cd my-project

# 2. 同步环境（自动读取 pyproject.toml 和 uv.lock）
uv sync

# 3. 运行项目
uv run python main.py
```

### 替代 requirements.txt 工作流

```bash
# 旧方式（pip）:
# pip install -r requirements.txt
# pip freeze > requirements.txt

# 新方式（uv）:
uv sync                     # 安装依赖
uv add new-package          # 添加依赖（自动更新锁定文件）
```

---

## 10. pyproject.toml 配置

### 基本结构

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.31",
    "click>=8.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
    "ruff>=0.1",
]

[project.scripts]
my-cli = "my_project.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    "mypy>=1.0",
    "pre-commit>=3.0",
]
```

### 常用配置

```toml
[tool.uv]
# 指定索引服务器
index-url = "https://pypi.org/simple"

# 额外索引服务器（私有源）
extra-index-urls = ["https://my-private-pypi.com/simple"]

# 环境变量
env = { DATABASE_URL = "sqlite:///dev.db" }

# 覆盖依赖版本
override-dependencies = ["requests>=2.32"]
```

---

## 11. 高级用法

### 工作空间（多包项目）

```bash
# 创建工作空间
uv init --lib
uv add ./packages/pkg-a
uv add ./packages/pkg-b

# 同步所有包
uv sync
```

### 自定义索引源

```bash
# 使用私有 PyPI 服务器
uv sync --index-url https://my-pypi.company.com/simple

# 添加额外索引
uv sync --extra-index-url https://pypi.org/simple
```

### 离线安装

```bash
# 使用缓存离线安装
uv sync --offline
```

### 环境变量

```bash
# 设置 uv 缓存目录
export UV_CACHE_DIR=/path/to/cache

# 设置日志级别
export UV_VERBOSE=1
```

---

## 12. 对比其他工具

| 功能 | 传统工具 | uv 替代 |
|------|---------|---------|
| 安装包 | `pip install` | `uv pip install` / `uv add` |
| 虚拟环境 | `python -m venv` | `uv venv` |
| 锁定依赖 | `pip-tools` / `poetry lock` | `uv lock` |
| 运行工具 | `pipx run` | `uvx` / `uv run` |
| Python 版本 | `pyenv` | `uv python` |
| 项目管理 | `poetry` / `pipenv` | `uv` (一体化) |

---

## 13. 常见问题

### 如何加速安装？

```bash
# uv 默认使用全局缓存，无需额外配置
# 缓存位置:
# Linux:   ~/.cache/uv
# macOS:   ~/Library/Caches/uv
# Windows: %LOCALAPPDATA%\uv\Cache

# 手动清理缓存
uv cache clean
```

### 如何与现有 pip 项目兼容？

```bash
# 使用 pip 兼容模式
uv pip install -r requirements.txt
uv pip freeze > requirements.txt

# 推荐：迁移到 uv 项目管理
uv init
uv add -r requirements.txt  # 导入现有依赖
```

### 如何处理网络问题？

```bash
# 设置代理
export HTTP_PROXY=http://proxy:8080
export HTTPS_PROXY=http://proxy:8080

# 或使用 uv 参数
uv sync --index-url https://pypi.org/simple --retries 5
```

---

## 14. 最佳实践

### 1. 使用 uv add 而不是 uv pip install

```bash
# ✅ 推荐：使用项目管理
uv add requests
uv sync

# ❌ 避免：直接使用 pip（失去锁定优势）
uv pip install requests
```

### 2. 始终提交 uv.lock

```bash
# 确保团队依赖版本一致
git add pyproject.toml uv.lock
git commit -m "add requests dependency"
```

### 3. 使用 uv run 运行代码

```bash
# ✅ 推荐：自动使用虚拟环境
uv run python main.py

# ❌ 避免：手动激活虚拟环境
source .venv/bin/activate
python main.py
```

### 4. 定期更新依赖

```bash
# 每月更新依赖
uv lock --upgrade
uv sync

# 更新特定包
uv lock --upgrade-package requests
```

### 5. 使用 uvx 运行工具

```bash
# ✅ 推荐：一次性运行，不污染全局
uvx ruff check .
uvx black .

# ❌ 避免：全局安装工具
pip install ruff
```

---

## 15. 快速参考表

| 命令 | 说明 |
|------|------|
| `uv init <name>` | 创建新项目 |
| `uv add <pkg>` | 添加依赖 |
| `uv remove <pkg>` | 移除依赖 |
| `uv sync` | 安装所有依赖 |
| `uv lock` | 生成锁定文件 |
| `uv run <cmd>` | 在虚拟环境中运行 |
| `uvx <tool>` | 运行一次性工具 |
| `uv venv` | 创建虚拟环境 |
| `uv python install <ver>` | 安装 Python 版本 |
| `uv python pin <ver>` | 设置项目 Python 版本 |
| `uv tree` | 查看依赖树 |
| `uv pip list` | 列出已安装的包 |
| `uv cache clean` | 清理缓存 |

---

## 16. 学习资源

- **官方文档**: https://docs.astral.sh/uv/
- **GitHub 仓库**: https://github.com/astral-sh/uv
- **Discord 社区**: https://discord.gg/astral
- **迁移指南**: https://docs.astral.sh/uv/guides/migration/

---

> 💡 **提示**：uv 仍在快速开发中，建议定期更新到最新版本以获取新功能和性能改进。
> 
> `uv self update` — 一句话更新 uv
