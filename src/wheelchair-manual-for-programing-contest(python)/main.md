# DSA 竞赛极速学习手册

> 适用：有 Python 基础、算法学过一遍但不够熟练，下午即将比赛。
> 目标：快速判断题型 → 调用什么算法 → 用什么 Python 内置函数 → 套模板解题。

---

## 1. 滑动窗口

### 1.1 定长滑动窗口

#### 如何判断

看到以下关键词，优先想定长滑动窗口：

- "固定长度 k 的子数组/子串"
- "每 k 个连续元素的xxx"
- "所有长度为 k 的窗口的xxx"

核心特征：**窗口大小固定不变**，窗口整体向右滑动一步。

#### Python 内置函数

- `sum(window)` — 求窗口和（维护变量更优）
- `collections.Counter(window)` — 统计窗口内元素频率

#### 模板

```python
# 定长滑动窗口模板
# 求：所有长度为 k 的窗口中，xxx 的最大/最小值

n = len(arr)
ans = -inf  # 或 inf，取决于求最大还是最小

# Step1: 初始化窗口 [0, k-1]
window_sum = sum(arr[:k])  # 或用其他统计量
ans = max(ans, window_sum)  # 更新答案

# Step2: 窗口向右滑动，每次移出左端、移入右端
for i in range(k, n):
    window_sum += arr[i]      # 右端进入
    window_sum -= arr[i - k]  # 左端离开
    ans = max(ans, window_sum)

print(ans)
```

**关键思想**：不重新计算整个窗口，只做增量更新（O(1) 而非 O(k))。

#### 常见变种

| 变种 | 说明 |
|------|------|
| 求窗口最大值 | 用变量维护，或用单调队列 |
| 求窗口平均值 | 维护 window_sum / k |
| 窗口内元素频率 | 用 dict/Counter 维护 |
| 窗口内不同元素数 | 维护 freq dict + distinct_count 变量 |

---

### 1.2 不定长滑动窗口

#### 如何判断

看到以下关键词，优先想不定长滑动窗口：

- "最长/最短的子数组/子串，满足某条件"
- "恰好包含xxx的最短子串"
- "最多包含 k 个不同字符的最长子串"

核心特征：**窗口大小可变**，左端和右端独立移动。

#### 两大类型

| 类型 | 左端移动条件 | 典型题 |
|------|--------------|--------|
| 求最长 | 窗口不满足条件时收缩左端 | 最长无重复子串 |
| 求最短 | 窗口满足条件时收缩左端 | 最短覆盖子串 |

#### 模板（求最长）

```python
# 不定长滑动窗口 - 求最长
# 求：满足条件的最长子数组长度

left = 0
ans = 0
freq = {}  # 或 set，取决于需要统计什么

for right in range(n):
    # 右端元素进入窗口
    freq[arr[right]] = freq.get(arr[right], 0) + 1

    # 当窗口不满足条件时，收缩左端
    while 不满足条件(freq):  # 例：while freq[arr[right]] > 1
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            del freq[arr[left]]
        left += 1

    # 更新答案
    ans = max(ans, right - left + 1)

print(ans)
```

#### 模板（求最短）

```python
# 不定长滑动窗口 - 求最短
# 求：满足条件的最短子数组长度

left = 0
ans = inf
freq = {}  # 或其他统计量

for right in range(n):
    # 右端元素进入窗口
    freq[arr[right]] = freq.get(arr[right], 0) + 1

    # 当窗口满足条件时，尝试收缩左端（贪心求最短）
    while 满足条件(freq):
        ans = min(ans, right - left + 1)
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            del freq[arr[left]]
        left += 1

print(ans if ans != inf else -1)
```

#### Python 内置函数

- `collections.Counter` — 统计频率
- `defaultdict(int)` — 比 Counter 更快的频率统计
- 用 dict 手动维护频率是竞赛中最常用的方式

---

## 2. 二分算法

### 2.1 二分查找

#### 如何判断

看到以下关键词，优先想二分：

- "在有序数组中查找xxx"
- "寻找满足条件的最小值/最大值"
- "答案具有单调性"（即：若 x 满足条件，则 x+1 也满足）
- "时间复杂度要求 O(log n)"

核心特征：**答案空间有序/有单调性**，可以每次排除一半。

#### Python 内置函数

```python
import bisect

# 在有序列表 a 中：
bisect.bisect_left(a, x)   # 第一个 >= x 的位置
bisect.bisect_right(a, x)  # 第一个 > x 的位置（等同于 bisect）
bisect.bisect_left(a, x, lo=0, hi=len(a))  # 可以指定范围

# 插入：
bisect.insort_left(a, x)   # 在合适位置插入 x（保持有序）
```

**竞赛中常用**：`bisect_left` 找下界，`bisect_right` 找上界。

#### 模板（寻找满足条件的最小值）

```python
# 二分查找模板 - 寻找满足条件的最小值
# 条件：check(x) 返回 True 表示 x 满足要求
# 单调性：若 check(x) 为 True，则 check(x+1) 也为 True

def check(x):
    # 判断 x 是否满足条件
    return ...  # True 或 False

lo = 0          # 答案下界
hi = n          # 答案上界（取一个一定满足的值）

while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid     # 满足条件，尝试更小
    else:
        lo = mid + 1 # 不满足，需要更大

print(lo)  # lo 是最小满足条件的值
```

#### 模板（寻找满足条件的最大值）

```python
# 二分查找模板 - 寻找满足条件的最大值
# 条件：check(x) 返回 True 表示 x 满足要求
# 单调性：若 check(x) 为 True，则 check(x-1) 也为 True

def check(x):
    return ...  # True 或 False

lo = 0
hi = n  # 取一个一定不满足的值

while lo < hi:
    mid = (lo + hi + 1) // 2  # 注意 +1，避免死循环
    if check(mid):
        lo = mid     # 满足条件，尝试更大
    else:
        hi = mid - 1 # 不满足，需要更小

print(lo)
```

#### 浮点数二分

```python
# 浮点数二分模板
lo = 0.0
hi = 1e9

for _ in range(100):  # 固定迭代次数，精度足够
    mid = (lo + hi) / 2
    if check(mid):
        hi = mid
    else:
        lo = mid

print(lo)  # 或 hi，两者差距极小
```

#### 常见应用场景

| 场景 | 说明 |
|------|------|
| 在有序数组中找值 | 直接 bisect |
| 找最小满足条件的整数 | 模板1 |
| 找最大满足条件的整数 | 模板2 |
| 二分答案 + 贪心验证 | "最小化最大值"类问题 |

---

## 3. 数据结构

### 3.1 常用枚举技巧

#### 如何判断

- 需要遍历所有子集 → **位运算枚举子集**
- 需要遍历所有组合 → **枚举 + 剪枝**
- 需要遍历所有排列 → **itertools.permutations**
- 需要遍历所有长度为 k 的组合 → **itertools.combinations**

#### Python 内置函数

```python
import itertools

# 排列：从 n 个元素中选 k 个排列
itertools.permutations(arr, k)  # 返回元组的迭代器

# 组合：从 n 个元素中选 k 个组合
itertools.combinations(arr, k)

# 笛卡尔积
itertools.product(arr1, arr2)

# 带重复的组合
itertools.combinations_with_replacement(arr, k)
```

#### 位运算枚举子集

```python
# 枚举 {0, 1, ..., n-1} 的所有子集
n = len(arr)
for mask in range(1 << n):  # 0 到 2^n - 1
    subset = []
    for i in range(n):
        if mask & (1 << i):  # 第 i 位为 1
            subset.append(arr[i])
    # 处理 subset

# 枚举某个子集 mask 的所有子子集
sub = mask
while sub:
    # 处理 sub
    sub = (sub - 1) & mask
# 注意：空子集 sub=0 不会被处理，需要单独考虑
```

### 3.2 前缀和

#### 如何判断

- "区间求和"（多次查询某区间的和）
- "子数组之和等于 k"
- 频繁询问区间统计量

核心特征：**多次区间查询，O(1) 回答每次查询**。

#### 模板（一维前缀和）

```python
# 一维前缀和模板
n = len(arr)
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

# 查询区间 [l, r] 的和（0-indexed，闭区间）
def range_sum(l, r):
    return prefix[r + 1] - prefix[l]
```

#### 模板（二维前缀和）

```python
# 二维前缀和模板
# 输入：matrix 为 m x n 的矩阵
m, n = len(matrix), len(matrix[0])
prefix = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m):
    for j in range(n):
        prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + matrix[i][j]

# 查询子矩阵 (r1,c1) 到 (r2,c2) 的和（闭区间）
def matrix_sum(r1, c1, r2, c2):
    return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]
```

#### 差分（前缀和的逆运算）

```python
# 差分模板 - 对区间 [l, r] 同时加减 val
n = len(arr)
diff = [0] * (n + 1)

# 区间加法：[l, r] 每个元素加 val
diff[l] += val
diff[r + 1] -= val

# 恢复原数组
result = [0] * n
cur = 0
for i in range(n):
    cur += diff[i]
    result[i] = arr[i] + cur  # 或直接 result[i] = cur（如果原数组为 0）
```

### 3.3 栈

#### 如何判断

- "最近的大/小元素" → **单调栈**
- "括号匹配" → **栈**
- "表达式求值" → **栈**
- "后进先出" 的操作序列

#### Python 内置函数

Python 列表本身就是栈：

```python
stack = []
stack.append(x)   # push
stack.pop()       # pop（弹出栈顶）
stack[-1]         # peek（查看栈顶）
len(stack) == 0   # 是否为空
```

#### 模板（单调递减栈 — 找每个元素右侧第一个更小的元素）

```python
# 单调栈模板 - 找右侧第一个更小元素
# 结果：right_smaller[i] = arr[i] 右侧第一个 < arr[i] 的下标
# 若不存在则为 -1

n = len(arr)
right_smaller = [-1] * n
stack = []  # 存下标，栈中元素对应的值单调递增

for i in range(n):
    while stack and arr[stack[-1]] > arr[i]:
        idx = stack.pop()
        right_smaller[idx] = i
    stack.append(i)

# 类似：单调递增栈找右侧第一个更大元素
# 类似：从右向左遍历找左侧第一个更小/更大元素
```

### 3.4 队列

#### 如何判断

- "先进先出" 的操作序列
- BFS（广度优先搜索） → **队列**
- "层序遍历" → **队列**

#### Python 内置函数

```python
from collections import deque

q = deque()
q.append(x)        # 右端入队
q.appendleft(x)    # 左端入队
q.pop()            # 右端出队
q.popleft()        # 左端出队（BFS常用）
q[0]               # 队首
len(q) == 0        # 是否为空
```

**竞赛中**：`deque` 比 `list` 做 pop(0) 快很多（O(1) vs O(n))。

#### 模板（BFS 队列）

```python
from collections import deque

def bfs(start):
    q = deque([start])
    visited = {start}

    while q:
        cur = q.popleft()
        for nxt in get_neighbors(cur):
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
```

### 3.5 堆（优先队列）

#### 如何判断

- "动态维护前 k 大/小元素"
- "每次取最小/最大的元素进行处理"
- "合并 k 个有序序列"
- "贪心需要每次选最优"

核心特征：**需要频繁取极值并动态更新**。

#### Python 内置函数

```python
import heapq

# Python 的 heapq 是小顶堆！
heap = []
heapq.heappush(heap, x)    # 入堆
heapq.heappop(heap)        # 弹出最小元素
heap[0]                    # 查看最小元素（不弹出）
heapq.heapify(arr)         # 将列表原地变为堆

# 大顶堆技巧：存负数
heapq.heappush(heap, -x)   # 存 -x，弹出时取负即最大值
top = -heapq.heappop(heap)

# 合并 k 个有序序列
heapq.merge(a, b, c)       # 返回合并后的迭代器
```

#### 模板（求前 k 大元素）

```python
# 模板：求前 k 大元素（用小顶堆，空间 O(k)）
import heapq

def top_k_large(arr, k):
    heap = []
    for x in arr:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)  # 弹出最小的，保留大的
    return sorted(heap, reverse=True)

# 模板：求前 k 小元素（用大顶堆存负数，或直接小顶堆）
def top_k_small(arr, k):
    heap = []
    for x in arr:
        heapq.heappush(heap, -x)  # 大顶堆
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted([-x for x in heap])
```

#### 模板（多路归并）

```python
# 模板：合并 k 个有序列表
import heapq

def merge_k_sorted(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (值, 列表编号, 下标)

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            nxt = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (nxt, list_idx, elem_idx + 1))

    return result
```

---

## 4. 链表、树、回溯 — 二叉树 DFS

#### 如何判断

- 输入是二叉树 → **DFS（递归）**
- "所有路径" → DFS
- "深度" → DFS
- "子树" → DFS

核心特征：**树的问题几乎都可以用递归 DFS**。

#### Python 内置函数

树一般用自定义类表示，没有直接内置函数。但可以利用：

- `defaultdict` — 存树结构
- `enumerate` — 遍历时带索引

#### 树的定义（竞赛常见输入格式）

竞赛中树通常不是用 TreeNode 类，而是用**边列表**或**父节点数组**：

```python
# 边列表格式：n 个节点，n-1 条边
n = int(input())
children = [[] for _ in range(n)]  # 或 defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    children[u].append(v)
    children[v].append(u)  # 无向边

# 父节点数组格式
parent = list(range(n))  # parent[i] = i 的父节点
```

如果题目用 TreeNode 类：

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

#### 模板（二叉树 DFS — 递归）

```python
# 模板：二叉树 DFS（递归）
# 三种遍历顺序

def dfs(node):
    if node is None:
        return  # 或返回特定值

    # ---- 前序位置 ----
    # 处理：进入节点时做的事

    dfs(node.left)

    # ---- 中序位置 ----
    # 处理：左子树处理完，右子树还没处理时做的事

    dfs(node.right)

    # ---- 后序位置 ----
    # 处理：离开节点时做的事（最常用！）
    # 后序 = 左右子树的结果已经算好了，可以合并
```

#### 常见题型与对应位置

| 题型 | 用什么位置 | 说明 |
|------|-----------|------|
| 求深度 | 后序 | `max(left_depth, right_depth) + 1` |
| 求路径和 | 前序 | 进入时累加，离开时减去 |
| 翻转树 | 后序 | 先翻转子树，再交换左右 |
| 判断平衡 | 后序 | 需要子树深度才能判断 |
| 最近公共祖先 | 后序 | 需要知道子树是否包含目标 |

#### 模板（带返回值的 DFS）

```python
# 模板：带返回值的 DFS
# 子树返回值给父节点用

def dfs(node):
    if node is None:
        return 0  # 基础情况

    left_result = dfs(node.left)
    right_result = dfs(node.right)

    # 后序位置：合并左右子树的结果
    result = max(left_result, right_result) + 1  # 例：求深度
    return result
```

#### 模板（用全局变量记录答案）

```python
# 模板：DFS + 全局变量
# DFS 返回子树信息，全局变量记录最终答案

ans = 0  # 或 inf, -inf

def dfs(node):
    if node is None:
        return 0

    left = dfs(node.left)
    right = dfs(node.right)

    # 更新全局答案
    ans = max(ans, left + right + node.val)  # 例：最大路径和

    return max(left, right) + node.val  # 返回值给父节点用

dfs(root)
print(ans)
```

---

## 5. 网格图 — 网格图 DFS

#### 如何判断

- 输入是二维字符矩阵或数字矩阵 → **网格 DFS/BFS**
- "岛屿数量" → 网格 DFS
- "连通区域" → 网格 DFS/BFS
- "从某点出发能到达的所有位置" → 网格 BFS
- "最短路径" → 网格 BFS（DFS 不适合求最短路径）

核心特征：**在二维网格上搜索连通区域或路径**。

#### Python 内置函数

- 网格图通常直接用二维列表，无特殊内置函数
- `enumerate` 可以同时获取行和列索引

#### 模板（网格 DFS — 连通区域）

```python
# 模板：网格 DFS - 求连通区域数量（如岛屿数量）
# grid: 二维矩阵，'#' 表示目标区域，'.' 表示非目标

def dfs(grid, i, j):
    # 边界检查 + 是否已访问 + 是否是目标区域
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    if grid[i][j] != '目标字符':  # 例：grid[i][j] != '1'
        return

    # 标记已访问（原地修改，省空间）
    grid[i][j] = '已访问标记'  # 例：grid[i][j] = '0' 或 '2'

    # 四方向扩展
    dfs(grid, i - 1, j)  # 上
    dfs(grid, i + 1, j)  # 下
    dfs(grid, i, j - 1)  # 左
    dfs(grid, i, j + 1)  # 右

# 主函数
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '目标字符':
            dfs(grid, i, j)
            count += 1

print(count)
```

#### 模板（网格 BFS — 最短路径）

```python
from collections import deque

# 模板：网格 BFS - 求最短路径长度
def bfs_shortest_path(grid, start, end):
    m, n = len(grid), len(grid[0])
    si, sj = start
    ei, ej = end

    q = deque([(si, sj, 0)])  # (行, 列, 距离)
    visited = set([(si, sj)])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 四方向

    while q:
        i, j, d = q.popleft()
        if (i, j) == (ei, ej):
            return d  # 到达终点

        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and grid[ni][nj] != '障碍':
                visited.add((ni, nj))
                q.append((ni, nj, d + 1))

    return -1  # 无法到达
```

#### 模板（网格 DFS — 路径搜索）

```python
# 模板：网格 DFS - 搜索所有路径（或判断路径是否存在）

def dfs(grid, i, j, target_i, target_j, visited):
    if i == target_i and j == target_j:
        return True  # 找到路径

    visited.add((i, j))
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited:
            if grid[ni][nj] != '障碍':
                if dfs(grid, ni, nj, target_i, target_j, visited):
                    return True

    # visited.remove((i, j))  # 如果需要回溯（找所有路径），要撤销标记
    return False
```

#### 八方向扩展（国王移动）

```python
dirs8 = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
```

---

## 6. 链表、树、回溯 — 各种

### 6.1 链表

#### 如何判断

- 输入是链表 → 链表题
- "反转链表" → **迭代/递归**
- "合并两个有序链表" → **双指针**
- "找中间节点" → **快慢指针**
- "判断环" → **快慢指针**

#### Python 内置函数

链表用自定义类，无内置函数。

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

#### 模板（反转链表）

```python
# 模板：反转链表（迭代）
def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next  # 先保存下一个
        cur.next = prev # 反转指向
        prev = cur      # prev 前进
        cur = nxt       # cur 前进
    return prev
```

#### 模板（快慢指针 — 找中间节点/判断环）

```python
# 模板：快慢指针 - 找中间节点
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # slow 就是中间节点

# 模板：快慢指针 - 判断是否有环
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

#### 模板（合并两个有序链表）

```python
# 模板：合并两个有序链表
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    cur = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 or l2  # 接上剩余部分
    return dummy.next
```

### 6.2 回溯

#### 如何判断

- "所有可能的组合/排列/子集" → **回溯**
- "所有可行解" → **回溯**
- "n皇后" → **回溯**
- 问题的解可以一步步构建，每步有多个选择

核心特征：**枚举所有可能性，尝试 → 不行就撤销 → 再尝试**。

#### 模板（子集型回溯）

```python
# 模板：子集型回溯 - 枚举所有子集
# 从 arr 中选若干元素

ans = []

def backtrack(i, path):
    # 每个位置都记录答案（子集可以不选任何元素）
    ans.append(path[:])  # 注意要拷贝！

    if i == len(arr):
        return

    for j in range(i, len(arr)):
        path.append(arr[j])       # 选 arr[j]
        backtrack(j + 1, path)    # 从 j+1 开始继续选
        path.pop()                # 撤销选择
```

#### 模板（组合型回溯）

```python
# 模板：组合型回溯 - 从 arr 中选 k 个元素
ans = []

def backtrack(i, path):
    if len(path) == k:
        ans.append(path[:])
        return

    if i == len(arr):
        return

    for j in range(i, len(arr)):
        path.append(arr[j])
        backtrack(j + 1, path)
        path.pop()
```

#### 模板（排列型回溯）

```python
# 模板：排列型回溯 - 枚举所有排列
ans = []

def backtrack(path, used):
    if len(path) == len(arr):
        ans.append(path[:])
        return

    for i in range(len(arr)):
        if used[i]:
            continue
        used[i] = True
        path.append(arr[i])
        backtrack(path, used)
        path.pop()
        used[i] = False

backtrack([], [False] * len(arr))
```

#### 剪枝技巧

```python
# 剪枝1：排序 + 跳过重复
arr.sort()
for j in range(i, len(arr)):
    if j > i and arr[j] == arr[j - 1]:
        continue  # 跳过重复元素
    ...

# 剪枝2：排序 + 提前终止
arr.sort()
for j in range(i, len(arr)):
    if arr[j] > target:  # 当前元素已经太大
        break            # 后面的更大，直接跳过
    ...

# 剪枝3：可行性剪枝
if 当前路径已经不满足条件:
    return  # 直接返回，不再深入
```

---

## 7. 动态规划

#### 如何判断

看到以下关键词，优先想 DP：

- "最大/最小/最多/最少" + "子数组/子序列/路径"
- "有多少种方式"
- "能否到达/能否组成"
- "最优解"

核心特征：**大问题的最优解可以由小问题的最优解推导出来**。

#### 判断步骤

1. 能否把问题分解为子问题？→ 可以的话考虑 DP
2. 子问题是否有重叠？→ 有重叠才值得用 DP（否则直接递归）
3. 子问题的最优解能否推导出大问题的最优解？→ 可以就是最优化 DP

#### Python 内置函数

- DP 主要靠手动维护数组/矩阵，无特殊内置函数
- `max()`, `min()` — 合并子问题结果
- `float('inf')`, `float('-inf')` — 初始化极值

#### DP 分类速查

| 类型 | 特征 | 状态表示 |
|------|------|----------|
| 线性 DP | 单序列/双序列 | dp[i] 或 dp[i][j] |
| 背包 DP | 选物品，有容量限制 | dp[i][w] |
| 区间 DP | 区间上的最优解 | dp[l][r] |
| 树形 DP | 在树上做最优决策 | dfs 返回 dp 值 |
| 状态压缩 DP | 状态空间大但可用整数编码 | dp[mask] |

### 7.1 线性 DP

#### 模板（最长递增子序列 LIS）

```python
# LIS - O(n^2) 版本
n = len(arr)
dp = [1] * n  # dp[i] = 以 arr[i] 结尾的 LIS 长度

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# LIS - O(n log n) 版本（贪心 + 二分）
import bisect
tails = []  # tails[k] = 长度为 k+1 的 LIS 的最小末尾元素
for x in arr:
    pos = bisect.bisect_left(tails, x)
    if pos == len(tails):
        tails.append(x)
    else:
        tails[pos] = x
print(len(tails))
```

#### 模板（最长公共子序列 LCS）

```python
# LCS 模板
s, t = input1, input2
m, n = len(s), len(t)
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[m][n])
```

#### 模板（编辑距离）

```python
# 编辑距离模板
s, t = input1, input2
m, n = len(s), len(t)
dp = [[0] * (n + 1) for _ in range(m + 1)]

# 初始化
for i in range(m + 1):
    dp[i][0] = i  # s 变成空串需要删 i 次
for j in range(n + 1):
    dp[0][j] = j  # 空串变成 t 需要插 j 次

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]  # 字符相同，不操作
        else:
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # 删除 s[i-1]
                dp[i][j - 1] + 1,      # 插入 t[j-1]
                dp[i - 1][j - 1] + 1   # 替换
            )

print(dp[m][n])
```

### 7.2 背包 DP

#### 模板（0-1 背包）

```python
# 0-1 背包模板
# n 个物品，容量为 W，每个物品只能选一次
# dp[w] = 容量为 w 时的最大价值

n, W = len(items), max_weight
dp = [0] * (W + 1)

for weight, value in items:
    for w in range(W, weight - 1, -1):  # 从大到小！避免重复选取
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[W])
```

#### 模板（完全背包）

```python
# 完全背包模板
# n 个物品，容量为 W，每个物品可以选多次
# dp[w] = 容量为 w 时的最大价值

n, W = len(items), max_weight
dp = [0] * (W + 1)

for weight, value in items:
    for w in range(weight, W + 1):  # 从小到大！允许重复选取
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[W])
```

**注意**：0-1 背包从大到小遍历，完全背包从小到大遍历 — 这是核心区别！

### 7.3 区间 DP

#### 如何判断

- "合并相邻元素的最小代价"
- "矩阵链乘法"
- "戳气球"类问题

#### 模板

```python
# 区间 DP 模板
# dp[l][r] = 区间 [l, r] 上的最优解

n = len(arr)
dp = [[0] * n for _ in range(n)]

# 区间长度从短到长
for length in range(2, n + 1):  # 区间长度
    for l in range(n - length + 1):
        r = l + length - 1
        dp[l][r] = inf
        for k in range(l, r):  # 分割点
            dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + 合并代价)

print(dp[0][n - 1])
```

### 7.4 树形 DP

#### 如何判断

- 在树上求最优解 → **树形 DP**
- "树的最大独立集"
- "树的直径"
- "节点选或不选"

#### 模板

```python
# 树形 DP 模板
# 以 u 为根的子树，返回 (选u的最优值, 不选u的最优值)

def dfs(u, parent):
    select = value[u]  # 选 u
    not_select = 0     # 不选 u

    for v in children[u]:
        if v == parent:
            continue
        s, ns = dfs(v, u)
        select += ns        # 选了 u，子节点不能选
        not_select += max(s, ns)  # 不选 u，子节点可选可不选

    return select, not_select

s, ns = dfs(0, -1)
print(max(s, ns))
```

### 7.5 状态压缩 DP

#### 如何判断

- n 很小（≤20），但状态空间巨大 → **状压 DP**
- "每行/每列的选择是一个组合问题"
- "旅行商问题"（TSP）

#### 模板（TSP）

```python
# 状压 DP - TSP 模板
# n 个城市，dist[i][j] 为城市间距离
# dp[mask][i] = 已访问城市集合 mask，当前在城市 i 的最短路径

n = len(dist)
inf = float('inf')
dp = [[inf] * n for _ in range(1 << n)]
dp[1][0] = 0  # 从城市 0 出发，只访问了 0

for mask in range(1 << n):
    for i in range(n):
        if not (mask & (1 << i)):
            continue
        for j in range(n):
            if mask & (1 << j):
                continue
            new_mask = mask | (1 << j)
            dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + dist[i][j])

# 回到起点
ans = min(dp[(1 << n) - 1][i] + dist[i][0] for i in range(n))
print(ans)
```

---

## 速查表：题目关键词 → 算法

| 关键词 | 算法 |
|--------|------|
| 固定长度 k 的子数组 | 定长滑动窗口 |
| 最长/最短子数组满足xx | 不定长滑动窗口 |
| 有序数组查找 | 二分 |
| 最小化最大值 / 最大化最小值 | 二分答案 |
| 区间求和（多次） | 前缀和 |
| 区间加减 | 差分 |
| 最近更大/更小元素 | 单调栈 |
| 最短路径（网格） | BFS |
| 连通区域/岛屿 | 网格 DFS |
| 所有组合/子集/排列 | 回溯 |
| 链表反转/找中间/判断环 | 快慢指针/双指针 |
| 二叉树深度/路径/子树 | 二叉树 DFS |
| 最大/最小子序列 | 线性 DP |
| 选物品有容量限制 | 背包 DP |
| 合并相邻区间 | 区间 DP |
| 树上最优解 | 树形 DP |
| n小但状态多 | 状压 DP |

---

## Python 竞赛常用技巧速查

```python
# 输入加速
import sys
input = sys.stdin.readline  # 比 input() 快很多

# 快速读多行
n = int(input())
arr = list(map(int, input().split()))

# 读二维矩阵
grid = [list(input().strip()) for _ in range(n)]

# 输出
print(ans)
# 多个值
print(a, b, c)
# 列表
print(*arr)  # 用空格分隔输出

# 常用数学
abs(x)          # 绝对值
max(arr)        # 最大值
min(arr)        # 最小值
sum(arr)        # 求和
math.gcd(a, b)  # 最大公约数
math.inf        # 无穷大

# 常用集合操作
set(a) & set(b)  # 交集
set(a) | set(b)  # 并集
set(a) - set(b)  # 差集

# 排序
arr.sort()               # 升序
arr.sort(reverse=True)   # 降序
arr.sort(key=lambda x: x[1])  # 按第二个元素排序

# 常用数据结构
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop
import bisect

# Counter 用法
cnt = Counter(arr)
cnt[x]       # x 出现次数
cnt.most_common(k)  # 前 k 个最常见元素

# defaultdict 用法
d = defaultdict(int)   # 默认值为 0
d = defaultdict(list)  # 默认值为 []
```