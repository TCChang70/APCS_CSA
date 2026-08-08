# Day 8｜遞迴、DFS 與 BFS（樹與圖）

> 對應學習計畫 Day 8。第 3、4 題常考「連鎖反應、走迷宮、樹的走訪」。
> 本日目標：① 看懂遞迴（自己呼叫自己）；② 會寫 DFS（深度優先）；③ 會寫 BFS（廣度優先，配佇列）。

---

## 目錄

1. [遞迴是什麼？三步驟寫法](#遞迴是什麼三步驟寫法)
2. [樹與圖：先認得長相](#樹與圖先認得長相)
3. [DFS：深度優先搜尋](#dfs深度優先搜尋)
4. [BFS：廣度優先搜尋](#bfs廣度優先搜尋)
5. [DFS 還是 BFS？決策表](#dfs-還是-bfs決策表)
6. [範例逐行拆解](#範例逐行拆解)
7. [常見錯誤檢查表](#常見錯誤檢查表)
8. [練習習題與提示](#練習習題與提示)
9. [自我評量](#自我評量)

---

## 遞迴是什麼？三步驟寫法

遞迴 = 函式呼叫自己。關鍵三步：

1. **終止條件**（什麼時候停、直接給答案）
2. **拆小**（把問題變成「更小的自己」）
3. **組合**（用小問題的答案拼出大問題的答案）

```python
def fact(n):              # 計算 n!（n 的階乘）
    if n <= 1:            # 1. 終止條件：n 已經夠小（0 或 1），直接給答案
        return 1          #    0! = 1、1! = 1
    return n * fact(n - 1)   # 2+3. 拆小＋組合：n! = n × (n-1)!
# 執行過程（fact(3)）：3 * fact(2) → 3 * (2 * fact(1)) → 3 * (2 * 1) = 6
# 看遞迴的要領：不要一直展開，只要「相信」fact(n-1) 會回傳對的答案即可
```

> 看遞迴的方法：**不要一直想「裡面展開多少層」，只要相信「小一號的呼叫會回傳對的答案」。**
> 費波那契是經典範例：

```python
def fib(n):               # 第 n 個費波那契數
    if n <= 1:            # 終止條件：fib(0)=0、fib(1)=1
        return n
    return fib(n - 1) + fib(n - 2)   # 拆小：第 n 項 = 前兩項相加
# 注意：這種「純遞迴」會大量重複計算（fib(40) 就會非常慢），
# 要加速需「記憶化」存下算過的答案，或改用迴圈（就是 Day 9 的 DP 精神）
```

> 注意：這種直接遞迴很慢（重複算）。要加速：記憶化（字典存算過的）或改迴圈（Day 9 的 DP 精神）。

---

## 樹與圖：先認得長相

| 結構 | 定義 | 例子 |
| --- | --- | --- |
| 樹 | 無環、連通；n 點 n-1 條邊 | 家譜、資料夾、階級 |
| 圖 | 點＋邊，可能有環 | 地圖、朋友關係、電路 |

樹的表示（用「鄰接表」最常用）：

```python
# 每個節點記錄「它跟誰相鄰」→ 鄰接表
n = int(input())                          # 節點數量（編號 1~n）
adj = [[] for _ in range(n + 1)]          # 長度 n+1：adj[u] 放「所有跟 u 相鄰的節點」
                                          # 多開一格是為了讓 adj[1] 對應到編號 1 的節點
for _ in range(n - 1):                    # 樹的定義：n 個點、恰好 n-1 條邊
    u, v = map(int, input().split())      # 讀一條邊：u 和 v 相鄰
    adj[u].append(v)                      # u 的鄰居清單加入 v
    adj[v].append(u)                      # 無向圖：v 的鄰居清單也要加入 u（兩邊都記）
```

| 表示法 | 何時用 |
| --- | --- |
| `adj[u].append(v)` 鄰接表 | 幾乎都是（省記憶體） |
| 矩陣 `g[u][v]` | 節點很少（≤1000）時 |

---

## DFS：深度優先搜尋

「一路走到黑，走不動就回頭」。用遞迴最直觀：

```python
visited = [False] * (n + 1)   # visited[u] = 節點 u 有沒有走訪過（先全部設 False）

def dfs(u):                       # 從節點 u 出發的深度優先搜尋
    visited[u] = True          # 1. 進入就先「標記來過」（重要！不標記會無限迴圈）
    for v in adj[u]:           # 2. 依序看 u 的所有鄰居
        if not visited[v]:     # 3. 只有「沒去過」的鄰居才走
            dfs(v)             # 4. 遞迴深入那一層，一路走到底再回頭
```

### 樹上的 DFS（算高度／算子樹大小）

```python
def dfs(u, parent):        # 計算以 u 為根的子樹「高度」；parent = u 的上一層節點
    h = 0                  # 目前看到的最大子樹高度
    for v in adj[u]:       # 走過 u 的所有鄰居
        if v != parent:    # 關鍵：樹是無向的，鄰居包含「爸爸」；
                           # 只要 v 不是爸爸，就一定是 u 的「子節點」
            h = max(h, dfs(v, u) + 1)   # 子節點高度 +1，取最大的
    return h               # 回傳這棵子樹的高度
# 用 parent 防走回頭，就不需要 visited 陣列（樹沒有環）
```

> 樹沒有環，但無向圖的「鄰居」包含爸爸。用 `parent` 參數防止走回去，就不需要 visited。

### 矩陣上的 DFS（連鎖反應／數島嶼）

```python
def dfs(i, j):              # 從格子 (i, j) 出發做 DFS（ex：連鎖反應／數島嶼）
    if not (0 <= i < n and 0 <= j < m):   # 越界檢查：走出矩陣就停
        return
    if grid[i][j] == 0:     # 這格不是「目標格」（0 代表非目標/已走過）→ 停
        return
    grid[i][j] = 0          # 走過就把這格「改成 0」：順便當成 visited 標記，防重複走
    for di, dj in dirs:     # 往 4 個方向擴散
        dfs(i + di, j + dj) # 遞迴走訪鄰居
# 技巧：直接在原地把走過的格子改掉，可以省一個額外的 visited 矩陣
```

> 矩陣走訪常見做法：走過就把格子改掉，避免再走（省一個 visited 陣列）。

---

## BFS：廣度優先搜尋

「一層一層往外擴散」。用佇列（deque）＋「記錄步數」：

```python
from collections import deque   # 高效能的佇列

dist = [-1] * (n + 1)         # dist[v] = 起點到 v 的最短步數；-1 表示「還沒到」
q = deque()                   # 建立空佇列
dist[1] = 0                   # 起點（編號 1）距離 0
q.append(1)                   # 起點放進佇列

while q:                      # 佇列不空就一直擴散
    u = q.popleft()           # 從「前面」取出（先進先出 FIFO）
    for v in adj[u]:          # 看 u 的所有鄰居
        if dist[v] == -1:     # 第一次到達的節點 → 這條路徑就是「最短」
            dist[v] = dist[u] + 1   # 步數 = 上一層 + 1
            q.append(v)             # 放進佇列，下次擴散它
# BFS 一層一層往外擴散，先到的一定最短；
# 目標一旦第一次被碰到，就可以直接停（就是答案）
```

| 部分 | 意義 |
| --- | --- |
| `deque()` | 高效能的佇列 |
| `q.popleft()` | 取出最前面的 |
| `dist[v] == -1` | 還沒到過 |
| `dist[v] = dist[u] + 1` | 步數 = 上一層 +1 |

> 為什麼 BFS 能找到「最短步數」？因為它一層一層擴散，先到的一定是最短。
> **第一次碰到目標時就可以停。**

### 矩陣版 BFS（最短步數走出迷宮）

```python
from collections import deque
dist = [[-1] * m for _ in range(n)]   # dist[i][j] = 起點到 (i,j) 的最短步數，-1 = 未到
q = deque()
dist[si][sj] = 0                      # 起點距離 0
q.append((si, sj))                    # 起點座標放入佇列
while q:
    i, j = q.popleft()                # 取出「最早進佇列」的格子（FIFO）
    if (i, j) == (ti, tj):            # 已經到達終點
        print(dist[i][j]); break      # 第一次到就是最短步數 → 印出並結束
    for di, dj in dirs:               # 往 4 個方向擴散
        ni, nj = i + di, j + dj       # 鄰居座標
        # 四個條件都成立才能走：在矩陣內 且 沒走過 且 不是牆壁 '#'
        if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == -1 and grid[ni][nj] != '#':
            dist[ni][nj] = dist[i][j] + 1   # 步數 +1
            q.append((ni, nj))              # 放入佇列等下一輪擴散
```

---

## DFS 還是 BFS？決策表

| 題目想要 | 用 |
| --- | --- |
| 「所有可能」「能走到嗎」 | DFS（遞迴好寫） |
| 「最短步數」 | BFS（一定要 BFS！） |
| 樹的高度／子樹大小 | DFS |
| 連鎖反應／擴散次數 | BFS（一層層數）或 DFS 皆可 |
| 排列／組合窮舉 | DFS 遞迴 |

> 口訣：**要最短 → BFS；要全部 → DFS。**

---

## 範例逐行拆解

### 範例 1：血緣關係（ZJ b967，2016/3 第 4 題）概念

> 題目大意：家譜樹，求「最深的祖孫距離」= 樹的直徑或最深距離。
> 做法：DFS 從根出發，每層深度 +1，紀錄最大深度。

```python
import sys
sys.setrecursionlimit(10**6)      # 行1：Python 遞迴預設上限 1000 層；樹很深時調大避免
                                  #     RecursionError（改成一百萬層）

def dfs(u, parent, depth):        # 從 u 往下走，depth 是目前深度
    global ans                    # 宣告要修改全域變數 ans
    ans = max(ans, depth)         # 行2：沿途記錄最大深度
    for v in adj[u]:              # 走所有鄰居
        if v != parent:           # 只往「子節點」走（不要走回爸爸）
            dfs(v, u, depth + 1)  # 行3：深入一層，深度 +1
```

| 行 | 意義 |
| --- | --- |
| 1 | Python 遞迴預設深度 1000，大樹要調大 |
| 2 | 沿途記錄最大深度 |
| 3 | 往子節點走，深度 +1 |

### 範例 2：樹的高度完整範例（可跑）

> 輸入：n（節點數），接著 n-1 條邊。輸出：以 1 為根的高度。

```python
import sys
sys.setrecursionlimit(10**6)      # 調高遞迴深度上限，防止大樹 RecursionError
n = int(input())                  # 讀節點數 n
adj = [[] for _ in range(n + 1)]  # 鄰接表（節點編號 1~n）
for _ in range(n - 1):            # 樹：n-1 條邊
    u, v = map(int, input().split())
    adj[u].append(v)              # 記錄 u 的鄰居 v
    adj[v].append(u)              # 無向：也記錄 v 的鄰居 u

def height(u, parent):            # 回傳以 u 為根的子樹高度
    h = 0                         # 目前最大的子樹高度
    for v in adj[u]:              # 走 u 的所有鄰居
        if v != parent:           # 排除爸爸 → 剩下的都是子節點
            h = max(h, height(v, u) + 1)   # 子樹高度 +1，取最大
    return h                      # 回傳高度

print(height(1, 0))               # 以節點 1 為根（0 當虛擬父節點）算高度
```

### 範例 3：矩陣連鎖反應概念（ZJ o713，2024/10 第 3 題）

> 點燃的格子會讓鄰居也燒起來。問全部燒完要燒幾次／要多久。
> 若問「最短時間」→ BFS 一層層擴散；若只問「能不能全燒到」→ DFS。

---

## 常見錯誤檢查表

| # | 錯誤 | 為什麼錯 | 修正 |
| --- | --- | --- | --- |
| 1 | DFS 忘了標記 visited | 無限遞迴當掉 / 重複走 | 進函式第一件事標記 |
| 2 | 樹的 DFS 忘了傳 parent | 走回爸爸無限繞 | `if v != parent:` |
| 3 | BFS 用 `q.pop()` 不是 `popleft()` | list.pop() 從後面拿 = 變 DFS 亂序 | 用 `deque.popleft()` |
| 4 | 遞迴深度爆掉（RecursionError） | 預設深度 1000 | `sys.setrecursionlimit(10**6)` |
| 5 | 遞迴沒寫終止條件 | 無限呼叫 | 第一個 if 一定要 return |
| 6 | 矩陣越界沒檢查就走 | IndexError | 先 `0 <= i < n and 0 <= j < m` |
| 7 | 求最短用 DFS | DFS 不保證最短 | 換 BFS |
| 8 | 佇列推進前沒設 dist | 同一格進隊很多次 | 第一次碰到就設 dist |

---

## 練習習題與提示

### 題 1：樹狀圖分析（ZJ c463，2017/10 第 3 題）★★

**題目大意**：多棵樹，算每棵樹的深度與總節點數。

**提示**：建立鄰接表，找出「沒有父節點」的根，DFS 數深度與節點數。

### 題 2：血緣關係（ZJ b967，2016/3 第 4 題）★★

**提示**：樹的最長距離：任取一點 DFS 找最遠點 A，再從 A DFS 找最遠距離 = 答案。

### 題 3：石窟探險（ZJ j124，2022/10 第 3 題）★★

**題目大意**：走進石窟，某些岔路要選，統計走了多少步。

**提示**：遞迴 DFS，把「每層的選擇規則」翻譯成程式。注意題目的樹結構描述方式。

### 題 4：連鎖反應（ZJ o713，2024/10 第 3 題）★★

**提示**：判斷「點燃的格子能不能燒到全部」用 DFS/BFS；若問「最快燒完」用 BFS。

### 題 5：邏輯電路（ZJ m933，2024/1 第 3 題）★★★

**提示**：把電路看成「節點依賴圖」，用「拜訪順序」（拓樸排序：先處理依賴都算完的節點）。

### 題 6：闖關路線（ZJ f166，2019/10）★★

**提示**：BFS 找最短步數。

---

## 自我評量

**限時 60 分鐘，不查筆記**，完成：

1. 寫出「以 1 為根的樹，計算每個節點的子樹大小」的 DFS 函式。
2. 寫出「n×m 迷宮（# 是牆）從 (0,0) 到 (n-1,m-1) 最短步數」的 BFS。

作答完再對照下方解答。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
# 題1：子樹大小（遞迴回傳）
import sys
sys.setrecursionlimit(10**6)      # 調高遞迴深度上限
n = int(input())
adj = [[] for _ in range(n + 1)]  # 鄰接表
for _ in range(n - 1):            # 樹的 n-1 條邊
    u, v = map(int, input().split())
    adj[u].append(v); adj[v].append(u)   # 無向圖兩邊都記

size = [0] * (n + 1)              # size[u] = 以 u 為根的子樹有幾個節點
def dfs(u, parent):               # 算以 u 為根的子樹大小
    size[u] = 1                   # 先算上自己
    for v in adj[u]:              # 走所有子節點
        if v != parent:           # 排除爸爸
            size[u] += dfs(v, u)  # 加上每個子節點的子樹大小（遞迴）
    return size[u]                # 回傳這棵子樹的節點數

dfs(1, 0)                         # 從根節點 1 開始算
print(size[1:])                   # 印出節點 1~n 各自的子樹大小（去掉索引 0）
```

```python
# 題2：BFS 最短步數（迷宮起點 (0,0) → 終點 (n-1,m-1)）
from collections import deque
n, m = map(int, input().split())          # 迷宮列數、行數
grid = [list(input().strip()) for _ in range(n)]   # 逐列讀入，每格一個字元（'#' 是牆）
dist = [[-1] * m for _ in range(n)]       # 步數表：-1 = 還沒走到
q = deque()
dist[0][0] = 0                            # 起點步數 0
q.append((0, 0))                          # 起點放進佇列
dirs = [(-1,0),(1,0),(0,-1),(0,1)]        # 上、下、左、右
while q:                                  # 佇列非空就繼續擴散
    i, j = q.popleft()                    # 取出最前面的格子
    if (i, j) == (n - 1, m - 1):          # 走到終點了
        print(dist[i][j])                 # 第一次到終點 = 最短步數 → 印出
        break                             # 結束搜尋
    for di, dj in dirs:                   # 往 4 個方向走
        ni, nj = i + di, j + dj
        # 四個條件：在矩陣內 且 未走過 且 不是牆壁
        if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == -1 and grid[ni][nj] != '#':
            dist[ni][nj] = dist[i][j] + 1 # 步數 +1
            q.append((ni, nj))            # 放入佇列
```

</details>

> 通過標準：60 分鐘內兩題都寫對。若 DFS 常忘 visited/parent，把「進函式先標記、樹走訪帶 parent」寫在筆記第一行。
