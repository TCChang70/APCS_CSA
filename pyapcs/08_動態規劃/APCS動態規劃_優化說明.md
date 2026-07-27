# APCS 動態規劃優化說明（Optimization Guide）

本文件聚焦在「如何把可過的 DP 寫成更快、更省、更穩」。

每個優化都附上 **Before / After 程式碼對比**，讓你一看就懂。

---

## 1. 優化總覽

| 優化方向 | 做法 | 常見題型 | 效果 |
|---|---|---|---|
| **空間壓縮** | 2D -> 1D、陣列 -> 滾動變數 | 背包、LCS、爬樓梯 | 空間大幅縮減 |
| **時間優化** | 用資料結構或二分搜尋 | LIS: O(N^2) -> O(N log N) | 時間從平方降到線性對數 |
| **常數因子** | 減少 Python 物件建立、重複判斷 | 幾乎所有題 | 2~5 倍加速 |
| **迴圈順序** | 正序 vs 倒序 | 背包問題 | 正確性關鍵 |
| **狀態設計** | 改定義讓轉移更短 | 區間 DP、路徑 DP | 減少轉移次數 |

---

## 2. 空間壓縮：最常見也最穩定

### 2.1 爬樓梯：O(N) -> O(1)

dp[i] 只依賴 dp[i-1] 和 dp[i-2]，不需要整個陣列。

```python
# Before：O(N) 空間
def climb_stairs_before(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# After：O(1) 空間
def climb_stairs_after(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

**判斷依據**：如果 dp[i] 只用到「固定少數個前項」，就能壓縮成 O(1)。

---

### 2.2 背包：O(N*W) 空間 -> O(W)

dp[i][w] 只依賴「上一列」dp[i-1][*]，不需要保留所有列。

```python
# Before：O(N*W) 空間
def knapsack_before(weights, values, W):
    N = len(weights)
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i-1][w]
            if w >= weights[i-1]:
                dp[i][w] = max(dp[i][w],
                    dp[i-1][w - weights[i-1]] + values[i-1])
    return dp[N][W]

# After：O(W) 空間
def knapsack_after(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]
```

**注意**：0/1 背包壓縮時**必須倒序**更新，詳見第 4 節。

---

### 2.3 LCS：O(N*M) -> O(min(N,M))

dp[i][j] 只依賴「上一列」dp[i-1][j]、左邊 dp[i][j-1]、和左上 dp[i-1][j-1]。

```python
# Before：O(N*M) 空間
def lcs_before(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

# After：O(min(N,M)) 空間
def lcs_after(a, b):
    if len(a) < len(b):
        a, b = b, a
    dp = [0] * (len(b) + 1)
    for ch in a:
        prev_diag = 0
        for j in range(1, len(b) + 1):
            old = dp[j]
            if ch == b[j-1]:
                dp[j] = prev_diag + 1
            else:
                dp[j] = max(dp[j], dp[j-1])
            prev_diag = old
    return dp[-1]
```

**陷阱**：忘記用 `old` 暫存 dp[j] 的舊值，會導致 left_diag 被覆蓋。

---

### 2.4 編輯距離：O(N*M) -> O(min(N,M))

與 LCS 相同壓縮邏輯，dp[i][j] 只依賴上一列和本列左側。

```python
# Before：O(N*M) 空間
def edit_distance_before(w1, w2):
    n, m = len(w1), len(w2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n][m]

# After：O(min(N,M)) 空間
def edit_distance_after(w1, w2):
    n, m = len(w1), len(w2)
    if n < m:
        w1, w2 = w2, w1
        n, m = m, n
    dp = list(range(m + 1))
    for i in range(1, n + 1):
        prev_diag = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            temp = dp[j]
            if w1[i-1] == w2[j-1]:
                dp[j] = prev_diag
            else:
                dp[j] = 1 + min(dp[j], dp[j-1], prev_diag)
            prev_diag = temp
    return dp[m]
```

---

## 3. 時間優化：LIS 經典升級

### 3.1 O(N^2) DP

```python
# Before：O(N^2)
def lis_dp(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

### 3.2 O(N log N) tails + 二分搜

```python
# After：O(N log N)
from bisect import bisect_left

def lis_bs(nums):
    tails = []
    for x in nums:
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)
```

**原理**：tails[k] 維護「長度 k+1 的遞增子序列的最小結尾值」。每次用二分搜決定 x 放入 tails 的哪個位置，保持 tails 單調遞增。

**時間對比**：

```
N = 100,000
  O(N^2) DP:  ~10,000,000 次運算  可能超時（Python 2~3 秒）
  O(NlogN):   ~1,700,000 次運算   通常 0.3 秒內
```

**注意**：tails 陣列本身**不是** LIS。例如 tails=[2,3,7,18]，但 LIS 可以是 [2,5,7,101]。tails 只是用來維持「未來更容易延伸」的狀態。

---

## 4. 迴圈順序優化：正序或倒序不是小事

以背包為例：

| 題型 | 迴圈方向 | 原因 |
|------|----------|------|
| 0/1 背包 | 倒序 `range(W, wi-1, -1)` | 避免同一輪重複使用物品 |
| 無限背包 | 正序 `range(wi, W+1)` | 允許同一物品重複選取 |
| 硬幣組合數 | 先物品、後金額 | 避免重複計入排列 |

```python
# 0/1 背包：倒序（每物品最多一次）
for i in range(len(weights)):
    for w in range(W, weights[i] - 1, -1):  # 從大到小
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

# 無限背包：正序（每物品可無限次）
for i in range(len(weights)):
    for w in range(weights[i], W + 1):       # 從小到大
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
```

**直覺理解**：
- 倒序更新 dp[w] 時，dp[w-w[i]] 仍是**上一輪**的值 → 代表「不重複選」
- 正序更新 dp[w] 時，dp[w-w[i]] 可能是**本輪**已更新的值 → 代表「可重複選」

**硬幣組合數 vs 排列數**：

```python
# 組合數（1+2 和 2+1 算同一種）：先物品後金額
for c in coins:
    for x in range(c, amount + 1):
        dp[x] += dp[x - c]

# 排列數（1+2 和 2+1 算不同種）：先金額後物品
for x in range(1, amount + 1):
    for c in coins:
        if x >= c:
            dp[x] += dp[x - c]
```

---

## 5. Python 實作層面的常數優化

### 5.1 區域變數快於全域變數

```python
# Before：每次迴圈都查 dict
def solve_slow(nums):
    dp = {}
    dp[0] = 0
    for i in range(1, len(nums)):
        dp[i] = dp.get(i-1, 0) + nums[i]
    return dp

# After：綁定到區域變數
def solve_fast(nums):
    dp = [0] * len(nums)
    prev = 0
    for i, v in enumerate(nums):
        prev = prev + v
        dp[i] = prev
    return dp
```

### 5.2 避免不必要的函式呼叫

```python
# Before：每次呼叫 min/max 外部函式
def kadane_slow(nums):
    def local_max(a, b):
        return a if a > b else b

    cur = best = nums[0]
    for v in nums[1:]:
        cur = local_max(v, cur + v)
        best = local_max(best, cur)
    return best

# After：直接用 Python 內建 max
def kadane_fast(nums):
    cur = best = nums[0]
    for v in nums[1:]:
        cur = max(v, cur + v)
        best = max(best, cur)
    return best
```

### 5.3 利用短路求值減少運算

```python
# Before：無條件計算
for c in coins:
    if cur >= c:
        dp[cur] = min(dp[cur], dp[cur - c] + 1)

# After：加上提前 break（若 coins 已排序，更大面額不用看）
coins_sorted = sorted(coins)
for c in coins_sorted:
    if c > cur:
        break  # 更大面額不可能用，直接跳過
    dp[cur] = min(dp[cur], dp[cur - c] + 1)
```

---

## 6. 常見誤區對照

| 誤區 | 錯誤做法 | 正確做法 |
|------|----------|----------|
| 狀態定義不清 | 直接寫轉移，不知道 dp[i] 代表什麼 | 先用一句話定義每個狀態意義 |
| 邊界初始化錯誤 | 不可達狀態設 0 → min 判斷永遠是 0 | 不可達用 INF / False，依題意設定 |
| 迴圈方向搞錯 | 0/1 背包正序 → 物品被重複選 | 0/1 背包倒序、無限背包正序 |
| 只背模板不驗證 | 套公式沒跑小測資 | 先手算 2-3 個小例子對照 |
| 忘了暫存舊值 | LCS 壓縮沒存 old → 值被覆蓋 | 用 `old = dp[j]` 暫存 |
| 混淆子序列/子字串 | 把 LCS 當成必須連續 | 子序列不連續，子字串必須連續 |

---

## 7. APCS 實戰建議（考場版）

### 第一步：90 秒內判斷是否 DP 題

```
符合以下特徵 = 大概率 DP：
  ✓ 求「最值」（最大/最小）
  ✓ 求「方案數」（幾種方法）
  ✓ 求「可行性」（能不能）
  ✓ 問題可分解成重疊的子問題
```

### 第二步：先寫可過版本

```
APCS 的策略：
  1. 先寫暴力 O(2^N) 或 O(N^2) 確認邏輯正確
  2. 用小測資手算驗證
  3. 再做空間或時間優化
  4. 檢查大測資的時間限制
```

### 第三步：根據 N 選擇算法

| N 的範圍 | 可接受的時間複雜度 | 適合的題型 |
|----------|--------------------|------------|
| N <= 20 | O(2^N) | 狀態壓縮 DP |
| N <= 500 | O(N^3) | 區間 DP |
| N <= 5000 | O(N^2) | 0/1 背包, LCS |
| N <= 10^5 | O(N log N) | LIS, 排序+DP |
| N <= 10^6 | O(N) | 爬樓梯, Kadane |

### 第四步：考場 Checklist

```
□ 狀態定義清楚了嗎？（一句話）
□ 轉移式寫出來了嗎？
□ 初始值設對了嗎？（特別是 INF 和 0）
□ 迴圈順序對嗎？（0/1 背包要倒序）
□ 手算了至少 1 個小測資嗎？
□ 時間複雜度符合限制嗎？
```

---

## 8. 練習升級路線

```
初級 ★
  ├── 爬樓梯        O(N)      O(1)
  ├── 最少硬幣數    O(A*C)    O(A)
  └── Kadane        O(N)      O(1)

中級 ★★
  ├── 0/1 背包      O(N*W)    O(W)
  ├── 無限背包      O(N*W)    O(W)
  ├── LIS           O(NlogN)  O(N)
  └── LCS           O(N*M)    O(min(N,M))

中高級 ★★★
  ├── 編輯距離      O(N*M)    O(min(N,M))
  ├── 分割等和子集  O(N*Sum)  O(Sum)
  └── 硬幣組合/排列  O(A*C)   O(A)
```

建議每題都完成三件事：
1. 寫出 state / transition / base case
2. 寫出時間與空間複雜度
3. 嘗試至少一種優化（空間壓縮或時間升級）
