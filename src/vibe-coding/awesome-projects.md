# awesome-projects

## catlog

- [awesome-projects](#awesome-projects)
  - [catlog](#catlog)
  - [key words](#key-words)
  - [projects](#projects)
    - [learning resource](#learning-resource)
      - [\[-\]microsoft courses](#-microsoft-courses)
    - [token saving](#token-saving)
      - [\[-\]caveman](#-caveman)
      - [\[x\]ponytail](#xponytail)
      - [\[x\]headroom](#xheadroom)
    - [ability enhancing](#ability-enhancing)
      - [\[x\]ECC](#xecc)
      - [\[x\]superpowers](#xsuperpowers)
      - [\[x\]openspec](#xopenspec)
      - [\[x\]taste-skill](#xtaste-skill)
    - [workspace handling](#workspace-handling)
      - [\[x\]codegraph](#xcodegraph)
      - [\[x\]graphify](#xgraphify)
    - [other](#other)
      - [autoresearch](#autoresearch)
      - [awesome-llm-apps](#awesome-llm-apps)

## key words

<https://github.com/search?q=ai&type=repositories&s=stars&o=desc>  
<https://github.com/search?q=agent&type=repositories&s=stars&o=desc>  
<https://github.com/search?q=assistant&type=repositories&s=stars&o=desc>  
<https://github.com/search?q=llm&type=repositories&s=stars&o=desc>  
<https://github.com/search?q=tokens&type=repositories&s=stars&o=desc>  

## projects

### learning resource

---

#### [-]microsoft courses

<https://github.com/microsoft/AI-For-Beginners/blob/main/translations/zh-CN/README.md>

---

### token saving

---

#### [-]caveman

把话变简单

<https://github.com/JuliusBrussee/caveman>

- use

#### [x]ponytail

把代码变简洁

<https://github.com/DietrichGebert/ponytail>

- use

    ```bash
    codex plugin marketplace add DietrichGebert/ponytail
    codex plugin add ponytail@ponytail
    
    ```

#### [x]headroom

压缩后按需暴露原始内容

<https://github.com/headroomlabs-ai/headroom>

- use

    ```bash
    sudo pacman -S python-pipx
    pipx install "headroom-ai[proxy]"
    npm install headroom-ai
    headroom update  
    headroom proxy --port 8787
    ANTHROPIC_BASE_URL=http://localhost:8787 claude
    curl http://localhost:8787/stats

    ```

---

### ability enhancing

---

#### [x]ECC

<https://github.com/affaan-m/ECC>

- use

    ```bash
    [auto use after install. see README](https://github.com/affaan-m/ECC)
    
    ```

#### [x]superpowers

<https://github.com/obra/superpowers>

- use(ECC)

    ```bash
    auto use after install. see README

    ```

#### [x]openspec

<https://github.com/Fission-AI/OpenSpec>

- philosophy

    ```text
    → fluid not rigid
    → iterative not waterfall
    → easy not complex
    → built for brownfield not just greenfield
    → scalable from personal projects to enterprises

    ```

- use

    ```bash
    cd your-project
    openspec init

    /opsx:explore
    /opsx:propose add-dark-mode
    /opsx:apply
    /opsx:sync
    /opsx:archive

    openspec update
    
    ```

#### [x]taste-skill

<https://github.com/Leonxlnx/taste-skill>

- use

    ```bash
    npx skills add https://github.com/Leonxlnx/taste-skill

    ```

---

### workspace handling

---

#### [x]codegraph

<https://github.com/colbymchenry/codegraph>

- use

    ```bash
    codegraph install
    codegraph init
    
    ```

#### [x]graphify

<https://github.com/graphify-Labs/graphify>

- use

    ```bash
    pipx install graphifyy
    graphify install --platform codex
    graphify codex install

    $graphify .                        # build graph for current folder
    $graphify ./docs --update          # re-extract only changed files
    $graphify . --cluster-only         # rerun clustering without re-extracting
    $graphify . --cluster-only --resolution 1.5      # more granular communities
    $graphify . --cluster-only --exclude-hubs 99     # suppress utility super-hubs from god-node rankings
    $graphify . --no-viz               # skip the HTML, just the report + JSON
    $graphify . --wiki                 # build a markdown wiki from the graph
    graphify export callflow-html      # Mermaid architecture/call-flow HTML (auto-regenerates on every git commit if hook is installed)

    $graphify query "what connects auth to the database?"
    $graphify path "UserService" "DatabasePool"
    $graphify explain "RateLimiter"

    $graphify add https://arxiv.org/abs/1706.03762   # fetch a paper and add it
    $graphify add <youtube-url>                       # transcribe and add a video

    graphify hook install              # auto-rebuild on git commit
    graphify merge-graphs a.json b.json              # combine two graphs

    graphify prs                       # PR dashboard: CI state, review status, worktree mapping
    graphify prs 42                    # deep dive on PR #42 with graph impact
    graphify prs --triage              # AI ranks your review queue (uses whatever backend is configured)
    graphify prs --conflicts           # PRs sharing graph communities — merge-order risk
    
    ```

---

### other

#### autoresearch

<https://github.com/karpathy/autoresearch>

#### awesome-llm-apps

<https://github.com/Shubhamsaboo/awesome-llm-apps>
