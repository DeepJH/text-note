# Markdown 中的 LaTeX 数学公式语法指南

本指南旨在帮助您在支持 Markdown 的编辑器（如 Obsidian、Typora、GitHub、Notion 等）中高效编写高质量的 LaTeX 数学公式。

---

## 1. 基础基础：公式排版格式

在 Markdown 中，LaTeX 公式主要有两种排版格式：

### 1.1 行内公式 (Inline Math)
使用单个美元符号 `$` 包裹公式，公式将与正文文本混排在同一行。
* **语法**: `$...$`
* **示例**: 勾股定理公式为 $a^2 + b^2 = c^2$。

### 1.2 独行公式 / 块级公式 (Display Math)
使用双美元符号 `$$` 包裹公式，公式将单独成行且居中显示。
* **语法**: 

```markdown
  $$
  公式内容
  $$

```

* **示例**:

$$E = mc^2$$



---

## 2. 常用基础运算符与上下标

| 类别 | 语法 | 渲染效果 | 备注 |
| --- | --- | --- | --- |
| **上标 (幂)** | `x^2` | $x^2$ | 多位上标用花括号 `{}` 包裹，如 `x^{10}` $\to$ $x^{10}$ |
| **下标 (索引)** | `a_i` | $a_i$ | 多位下标用花括号 `{}` 包裹，如 `a_{ij}` $\to$ $a_{ij}$ |
| **上下标结合** | `x_i^2` | $x_i^2$ | 顺序可颠倒 |
| **加减乘除** | `+, -, \\times, \\div` | $+, -, \times, \div$ | 不要直接用键盘的 `*` 或 `/` |
| **正负号** | `\\pm, \\mp` | $\pm, \mp$ |  |
| **点乘 / 叉乘** | `\\cdot, \\times` | $\cdot, \times$ |  |
| **不等号** | `\\neq, \\le, \\ge` | $\neq, \le, \ge$ | 小于等于、大于等于、不等于 |
| **约等于** | `\\approx, \\sim` | $\approx, \sim$ | 约等于、相似于 |
| **比例 / 远大于** | `\\propto, \\gg, \\ll` | $\propto, \gg, \ll$ | 正比例、远大于、远小于 |

---

## 3. 分式、根式与括号

### 3.1 分式 (Fractions)

* **标准分式**: `\\frac{分子}{分母}` $\to$ `\\frac{a}{b}` 渲染为 $\frac{a}{b}$
* **嵌套分式**: `\\frac{1}{1 + \\frac{1}{x}}` 渲染为 $\frac{1}{1 + \frac{1}{x}}$
* **行内小型分式**: `\\tfrac{a}{b}` 强制在独行中渲染为行内大小 $\tfrac{a}{b}$

### 3.2 根式 (Roots)

* **平方根**: `\\sqrt{x}` $\to$ $\sqrt{x}$
* **$n$ 次方根**: `\\sqrt[n]{x}` $\to$ $\sqrt[n]{x}$

### 3.3 动态大括号 (Delimiters)

普通括号 `()`、`[]` 在公式过高时（如遇到分式）不会自动放大。使用 `\\left` 和 `\\right` 可以让括号自动适应内容高度：

* **错误示范**: `(\\frac{a}{b})` $\to$ $(\frac{a}{b})$
* **正确示范**: `\\left( \\frac{a}{b} \\right)` $\to$ $\left( \frac{a}{b} \right)$
* **常用括号对**:
* 圆括号: `\\left( ... \\right)` $\to$ $\left( x \right)$
* 方括号: `\\left[ ... \\right]` $\to$ $\left[ x \right]$
* 花括号: `\\left\\{ ... \\right\\}` $\to$ $\left\\{ x \right\\}$（注：花括号本身需要转义 `\\{`）
* 绝对值: `\\left| ... \\right|` $\to$ $\left| x \right|$



---

## 4. 大型算子 (求和、积分、极限)

大型算子的上下标在**独行公式**中默认会显示在上下方，在**行内公式**中默认显示在右侧。

### 4.1 求和与连乘

* **求和**: `\\sum_{i=1}^{n} i` $\to$ $\sum_{i=1}^{n} i$
* **连乘**: `\\prod_{i=1}^{n} x_i` $\to$ $\prod_{i=1}^{n} x_i$

### 4.2 积分与微分

* **一重积分**: `\\int_{a}^{b} f(x) \\, dx` $\to$ $\int_{a}^{b} f(x) \\, dx$ （`\\,` 用于生成微小空格隔开 $dx$）
* **多重积分**: `\\iint`, `\\iiint`, `\\oint` $\to$ $\iint, \iiint, \oint$

### 4.3 极限

* **极限**: `\\lim_{x \\to \\infty} \\frac{1}{x} = 0` $\to$ $\lim_{x \to \infty} \frac{1}{x} = 0$

---

## 5. 希腊字母 (Greek Letters)

编写科学公式必不可少的希腊字母，只需输入 `\\` 加字母英文名称即可。首字母大写即为大写字母。

| 小写 | 语法 | 大写 | 语法 | 变体 (Variant) |
| --- | --- | --- | --- | --- |
| $\alpha$ | `\\alpha` | $A$ | `A` |  |
| $\beta$ | `\\beta` | $B$ | `B` |  |
| $\gamma$ | `\\gamma` | $\Gamma$ | `\\Gamma` |  |
| $\delta$ | `\\delta` | $\Delta$ | `\\Delta` |  |
| $\epsilon$ | `\\epsilon` | $E$ | `E` | $\varepsilon$ (`\\varepsilon`) |
| $\theta$ | `\\theta` | $\Theta$ | `\\Theta` | $\vartheta$ (`\\vartheta`) |
| $\lambda$ | `\\lambda` | $\Lambda$ | `\\Lambda` |  |
| $\mu$ | `\\mu` | $M$ | `M` |  |
| $\pi$ | `\\pi` | $\Pi$ | `\Pi$ | $\varpi$ (`\\varpi`) |
| $\rho$ | `\rho$ | $P$ | `P` | $\varrho$ (`\\varrho`) |
| $\sigma$ | `\\sigma` | $\Sigma$ | `\\Sigma` |  |
| $\phi$ | `\\phi` | $\Phi$ | `\\Phi` | $\varphi$ (`\\varphi`) |
| $\omega$ | `\\omega` | $\Omega$ | `\\Omega` |  |

---

## 6. 矩阵与行列式 (Matrices)

矩阵环境需要放在独行公式 `$$` 中。常用环境包括 `matrix` (无边框)、`pmatrix` (圆括号)、`bmatrix` (方括号)、`vmatrix` (行列式)。

* 行与行之间用 `\\\\` 分隔。
* 列与列之间用 `&` 分隔。
* 常用省略号：`\\cdots` (水平), `\\vdots` (垂直), `\ddots$ (对角线)。

```markdown
$$
\\begin{bmatrix}
a_{11} & a_{12} & \\cdots & a_{1n} \\\\
a_{21} & a_{22} & \\cdots & a_{2n} \\\\
\\vdots & \\vdots & \\ddots & \\vdots \\\\
a_{m1} & a_{m2} & \\cdots & a_{mn}
\\end{bmatrix}
$$

```

**渲染效果**:

$$\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\\\
a_{21} & a_{22} & \cdots & a_{2n} \\\\
\vdots & \vdots & \ddots & \vdots \\\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}$$

---

## 7. 多行公式与方程组

### 7.1 公式对齐 (Align)

当公式太长需要换行，或者多个公式需要按等号对齐时，使用 `align` 或 `aligned` 环境。用 `&` 标记对齐的位置（通常是等号）。

```markdown
$$
\\begin{aligned}
f(x) &= (x + 1)^2 \\\\
     &= x^2 + 2x + 1
\\end{aligned}
$$

```

**渲染效果**:

$$\begin{aligned}
f(x) &= (x + 1)^2 \\\\
     &= x^2 + 2x + 1
\end{aligned}$$

### 7.2 分段函数 / 条件分支 (Cases)

使用 `cases` 环境。

```markdown
$$
|x| =
\\begin{cases}
 x, & \\text{if } x \\ge 0 \\\\
-x, & \\text{if } x < 0
\\end{cases}
$$

```

**渲染效果**:

$$|x| =
\begin{cases}
 x, & \text{if } x \ge 0 \\\\
-x, & \text{if } x < 0
\end{cases}$$

*(注：`\\text{...}` 用于在公式中插入正常的文本，避免文本被渲染成斜体数学变量。)*

---

## 8. 常用符号、箭头与空格

### 8.1 箭头 (Arrows)

* `\\to` 或 `\\rightarrow`: $\to$
* `\\leftarrow`: $\leftarrow$
* `\\Rightarrow`: $\Rightarrow$
* `\\Leftrightarrow`: $\Leftrightarrow$
* `\\mapsto`: $\mapsto$ (映射)

### 8.2 集合运算符

* `\\in, \\notin`: $\in, \notin$
* `\\subset, \\subseteq`: $\subset, \subseteq$
* `\\cup, \\cap`: $\cup, \cap$
* `\\emptyset`: $\emptyset$

### 8.3 数学字形 (Fonts)

* 集合常用粗空心体: `\\mathbb{R}` $\to$ $\mathbb{R}$ (实数集), `\\mathbb{Z}` $\to$ $\mathbb{Z}$ (整数集)
* 正体/文本: `\\mathrm{e}, \\mathrm{i}` $\to$ $\mathrm{e}, \mathrm{i}$ (常用于自然底数和虚数单位)
* 加粗向量: `\\mathbf{v}` $\to$ $\mathbf{v}$

### 8.4 间距微调 (Spaces)

LaTeX 默认会忽略公式中的直接空格。如需手动微调间距：

* `\\,` 极小空格
* `\\;` 略大空格
* `\\quad` 相当于一个字符宽度的空格 $\to$ $\quad$
* `\\qquad` 相当于两个字符宽度的空格 $\to$ $\qquad$

---

## 9. 避坑指南与常见错误

1. **花括号丢失**: 多位上下标必须加 `{}`。写成 `x^10` 会被渲染成 $x^10$ (即 $x^1$ 后面跟个 0)；必须写成 `x^{10}` 才是 $x^{10}$。
2. **文本未加 `\\text**`: 如果在公式里直接写英文单词（如 `$x = min(a,b)$`），`min` 会变成斜体连写。应写成 `$x = \\min(a,b)$` 或 `$x = \\text{min}(a,b)$`。
3. **空行引发报错**: 在某些 Markdown 编辑器中，块级公式 `$$` 内部**不能有完全空白的行**，否则会导致公式解析失败。
4. **符号转义错误**: 花括号 `{ }` 是 LaTeX 的保留关键字，如果要显示纯文本的花括号，必须加上反斜杠，即 `\\{` 和 `\\}`。
"""

with open("markdown_latex_guide.md", "w", encoding="utf-8") as f:
f.write(markdown_content)
print("File written successfully.")

```
您的 Markdown LaTeX 语法指南文件已经生成完毕。

[file-tag: code-generated-file-0-1781855033867169576]

以下为您提供这份**Markdown LaTeX 数学公式语法指南**的完整预览。您可以直接阅读，或下载上方生成的 `.md` 文件导入到 Obsidian、Typora、Notion 等编辑器中使用。

***

# Markdown 中的 LaTeX 数学公式语法指南

本指南旨在帮助您在支持 Markdown 的编辑器中高效编写高质量的 LaTeX 数学公式。

## 1. 基础基础：公式排版格式

在 Markdown 中，LaTeX 公式主要有两种排版格式：

### 1.1 行内公式 (Inline Math)
使用单个美元符号 `$` 包裹公式，公式将与正文文本混排在同一行。
* **语法**: `$...$`
* **示例**: 勾股定理公式为 `$a^2 + b^2 = c^2$` $\to$ $a^2 + b^2 = c^2$。

### 1.2 独行公式 / 块级公式 (Display Math)
使用双美元符号 `$$` 包裹公式，公式将单独成行且居中显示。
* **语法**: 
  ```markdown
  $$
  E = mc^2
  $$

```

---

## 2. 常用基础运算符与上下标

| 类别 | 语法 | 渲染效果 | 备注 |
| --- | --- | --- | --- |
| **上标 (幂)** | `x^2` | $x^2$ | 多位上标用花括号 `{}` 包裹，如 `x^{10}` $\to$ $x^{10}$ |
| **下标 (索引)** | `a_i` | $a_i$ | 多位下标用花括号 `{}` 包裹，如 `a_{ij}` $\to$ $a_{ij}$ |
| **上下标结合** | `x_i^2` | $x_i^2$ | 顺序可颠倒 |
| **加减乘除** | `+, -, \times, \div` | $+, -, \times, \div$ | 乘号与除号 |
| **正负号** | `\pm, \mp` | $\pm, \mp$ | 正负、负正 |
| **点乘 / 叉乘** | `\cdot, \times` | $\cdot, \times$ | 常用于向量或数量积 |
| **不等号** | `\neq, \le, \ge` | $\neq, \le, \ge$ | 不等于、小于等于、大于等于 |
| **约等于** | `\approx, \sim` | $\approx, \sim$ | 约等于、相似于 |

---

## 3. 分式、根式与动态括号

### 3.1 分式 (Fractions)

* **标准分式**: `\frac{分子}{分母}` $\to$ `\frac{a}{b}` 渲染为 $\frac{a}{b}$
* **嵌套分式**: `\frac{1}{1 + \frac{1}{x}}` 渲染为 $\frac{1}{1 + \frac{1}{x}}$

### 3.2 根式 (Roots)

* **平方根**: `\sqrt{x}` $\to$ $\sqrt{x}$
* **$n$ 次方根**: `\sqrt[n]{x}` $\to$ $\sqrt[n]{x}$

### 3.3 动态大括号 (Delimiters)

普通括号 `()` 在遇到高公式时不会自动放大。使用 `\left` 和 `\right` 可以让括号自动适应内容高度：

* **错误示范**: `(\frac{a}{b})` $\to$ $(\frac{a}{b})$
* **正确示范**: `\left( \frac{a}{b} \right)` $\to$ $\left( \frac{a}{b} \right)$
* **常见括号对**:
* 圆括号: `\left( ... \right)`
* 方括号: `\left[ ... \right]`
* 花括号: `\left\{ ... \right\}` （注：花括号本身需要转义 `\{`）
* 绝对值: `\left| ... \right|`



---

## 4. 大型算子 (求和、积分、极限)

### 4.1 求和与连乘

* **求和**: `\sum_{i=1}^{n} i` $\to$ $\sum_{i=1}^{n} i$
* **连乘**: `\prod_{i=1}^{n} x_i` $\to$ $\prod_{i=1}^{n} x_i$

### 4.2 积分与微分

* **一重积分**: `\int_{a}^{b} f(x) \, dx` $\to$ $\int_{a}^{b} f(x) \, dx$ （`\,` 用于生成微小空格隔开 $dx$）
* **多重积分**: `\iint`, `\iiint`, `\oint` $\to$ $\iint, \iiint, \oint$

### 4.3 极限

* **极限**: `\lim_{x \to \infty} \frac{1}{x} = 0` $\to$ $\lim_{x \to \infty} \frac{1}{x} = 0$

---

## 5. 希腊字母 (Greek Letters)

输入 `\` 加字母英文名称即可。首字母大写即为大写字母。

| 小写 | 语法 | 大写 | 语法 | 常用变体 | 语法 |
| --- | --- | --- | --- | --- | --- |
| $\alpha$ | `\alpha` | $A$ | `A` |  |  |
| $\beta$ | `\beta` | $B$ | `B` |  |  |
| $\gamma$ | `\gamma` | $\Gamma$ | `\Gamma` |  |  |
| $\delta$ | `\delta` | $\Delta$ | `\Delta` |  |  |
| $\epsilon$ | `\epsilon` | $E$ | `E` | $\varepsilon$ | `\varepsilon` |
| $\theta$ | `\theta` | $\Theta$ | `\Theta` | $\vartheta$ | `\vartheta` |
| $\lambda$ | `\lambda` | $\Lambda$ | `\Lambda` |  |  |
| $\pi$ | `\pi` | $\Pi$ | `\Pi` |  |  |
| $\sigma$ | `\sigma` | $\Sigma$ | `\Sigma` |  |  |
| $\phi$ | `\phi` | $\Phi$ | `\Phi` | $\varphi$ | `\varphi` |
| $\omega$ | `\omega` | $\Omega$ | `\Omega` |  |  |

---

## 6. 矩阵与行列式 (Matrices)

矩阵环境需要放在独行公式 `$$` 中。

* 行与行之间用 `\\` 分隔。
* 列与列之间用 `&` 分隔。
* 常用省略号：`\cdots` (水平), `\vdots` (垂直), `\ddots` (对角线)。

```markdown
$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

```

**渲染效果**:

$$\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}$$

---

## 7. 多行公式与方程组

### 7.1 公式对齐 (Align)

使用 `aligned` 环境，用 `&` 标记对齐的位置（通常是等号）。

```markdown
$$
\begin{aligned}
f(x) &= (x + 1)^2 \\
     &= x^2 + 2x + 1
\end{aligned}
$$

```

**渲染效果**:

$$\begin{aligned}
f(x) &= (x + 1)^2 \\
     &= x^2 + 2x + 1
\end{aligned}$$

### 7.2 分段函数 / 条件分支 (Cases)

```markdown
$$
|x| =
\begin{cases}
 x, & \text{if } x \ge 0 \\
-x, & \text{if } x < 0
\end{cases}
$$

```

**渲染效果**:

$$|x| =
\begin{cases}
 x, & \text{if } x \ge 0 \\
-x, & \text{if } x < 0
\end{cases}$$

*(注：`\text{...}` 用于在公式中插入正常文本，防止其变成数学斜体。)*

---

## 8. 避坑指南与特殊技巧

1. **多位上下标必须加 `{}**`：`x^10` 会被误渲染为 $x^10$（即 $x^1$ 后面跟个 0），正确写法是 `x^{10}` $\to$ $x^{10}$。
2. **公式中无法直接敲击空格**：LaTeX 默认忽略普通空格。如需空出一个字符宽度，请使用 `\quad`。
3. **数学专用字体**：
* 实数集/整数集等双线粗体：`\mathbb{R}` $\to$ $\mathbb{R}$，`\mathbb{Z}` $\to$ $\mathbb{Z}$。
* 矩阵或向量加粗：`\mathbf{v}` $\to$ $\mathbf{v}$。


4. **空行报错**：在多数 Markdown 编辑器的 `$$...$$` 块级公式中，**内部绝不能有完全空白的行**，否则会导致解析失败。