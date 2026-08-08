# APCS 動態規劃 — 迴圈詳細說明

本文件搭配 [APCS動態規劃_練習程式.py](APCS動態規劃_練習程式.py)，逐行解析每個迴圈的運作邏輯。

---

## 題 1：爬樓梯 `p1_climb_stairs`

```python
a, b = 1, 2                      # (A)
for _ in range(3, n + 1):        # (B)
    a, b = b, a + b               # (C)
return b                          # (D)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `a, b = 1, 2` | 初始化：a=dp[1]=1, b=dp[2]=2，分別代表到第1階和第2階的方法數 |
| (B) | `for _ in range(3, n+1)` | 從第3階開始，逐一計算到第n階。`_` 表示不需要迴圈變數 |
| (C) | `a, b = b, a+b` | 同時更新：a 舊的 b（前一階的方法數），b = 前兩階方法數之和 |
| (D) | `return b` | b 永遠是「最新計算的結果」，即 dp[n] |

### 追蹤範例（n=5）

```
初始：a=1(dp[1]), b=2(dp[2])

i=3: a,b = 2, 1+2 = 2,3     → dp[3]=3
i=4: a,b = 3, 2+3 = 3,5     → dp[4]=5
i=5: a,b = 5, 3+5 = 5,8     → dp[5]=8

return 8 ✓
```

### 為什麼不用陣列？

dp[i] 只依賴 dp[i-1] 和 dp[i-2]，只需要記住前兩個值。空間從 O(N) 壓縮到 O(1)。

---

## 題 1b：爬樓梯進階 `p1b_climb_stairs_k`

```python
dp = [0] * (n + 1)               # (A)
dp[0] = 1                        # (B)
for i in range(1, n + 1):        # (C) 外層：逐階計算
    for j in range(1, min(i, k) + 1):  # (D) 內層：枚舉可走的步數
        dp[i] += dp[i - j]       # (E)
return dp[n]                     # (F)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `dp = [0] * (n + 1)` | 建立 n+1 長度的陣列，dp[i] = 到第 i 階的方法數 |
| (B) | `dp[0] = 1` | 初始條件：第0階有1種方法（什麼都不走）。**這是哨兵值，確保轉移正確** |
| (C) | `for i in range(1, n+1)` | 外層：從第1階到第n階，依序計算每個 dp[i] |
| (D) | `for j in range(1, min(i, k)+1)` | 內層：從第 i 階回頭看，j 表示「最後一步走了 j 階」。`min(i,k)` 避免 j>i 時負索引 |
| (E) | `dp[i] += dp[i-j]` | 轉移：從第 (i-j) 階走 j 步到第 i 階，把所有可能的方法數累加 |
| (F) | `return dp[n]` | 回傳到第 n 階的總方法數 |

### 追蹤範例（n=5, k=3）

```
初始：dp = [1, 0, 0, 0, 0, 0]

i=1: j=1 → dp[1] += dp[0] = 1
      dp = [1, 1, 0, 0, 0, 0]

i=2: j=1 → dp[2] += dp[1] = 1
      j=2 → dp[2] += dp[0] = 1+1 = 2
      dp = [1, 1, 2, 0, 0, 0]

i=3: j=1 → dp[3] += dp[2] = 2
      j=2 → dp[3] += dp[1] = 2+1 = 3
      j=3 → dp[3] += dp[0] = 3+1 = 4
      dp = [1, 1, 2, 4, 0, 0]

i=4: j=1 → dp[4] += dp[3] = 4
      j=2 → dp[4] += dp[2] = 4+2 = 6
      j=3 → dp[4] += dp[1] = 6+1 = 7
      dp = [1, 1, 2, 4, 7, 0]

i=5: j=1 → dp[5] += dp[4] = 7
      j=2 → dp[5] += dp[3] = 7+4 = 11
      j=3 → dp[5] += dp[2] = 11+2 = 13
      dp = [1, 1, 2, 4, 7, 13]

return 13 ✓
```

### 為什麼 dp[0]=1？

如果 dp[0]=0，那 dp[3] 的第三個加數 dp[3-3]=dp[0] 就是 0，等於忽略了「一次走 3 階」的那條路。dp[0]=1 代表「站在原地是一種方法」，這樣所有從原點出發的路徑才會被計入。

---

## 題 2：最少硬幣數 `p2_coin_change_min`

```python
inf = 10**9                      # (A)
dp = [inf] * (amount + 1)        # (B)
dp[0] = 0                        # (C)
for cur in range(1, amount + 1): # (D) 外層：逐金額計算
    for c in coins:              # (E) 內層：枚舉每個硬幣
        if cur >= c:             # (F)
            dp[cur] = min(dp[cur], dp[cur - c] + 1)  # (G)
return -1 if dp[amount] == inf else dp[amount]  # (H)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `inf = 10**9` | 代表「不可達」的超大值。amount 最多 10^4，用 10^9 足夠 |
| (B) | `dp = [inf] * (amount+1)` | 所有金額初始設為不可達 |
| (C) | `dp[0] = 0` | 金額 0 需要 0 個硬幣（唯一確定的起點） |
| (D) | `for cur in range(1, amount+1)` | 外層：依序計算 dp[1], dp[2], ..., dp[amount] |
| (E) | `for c in coins` | 內層：對每個金額 cur，嘗試所有可用的硬幣面額 |
| (F) | `if cur >= c` | 安全檢查：硬幣面額不能超過目前金額 |
| (G) | `dp[cur] = min(dp[cur], dp[cur-c]+1)` | **核心轉移**：「不選這枚硬幣 vs 選這枚硬幣（從 dp[cur-c] 跳過來）」取最小 |
| (H) | `return -1 if ...` | 最後判斷：如果 dp[amount] 仍是 inf，表示無法湊出 |

### 追蹤範例（coins=[1,2,5], amount=6）

```
初始：dp = [0, inf, inf, inf, inf, inf, inf]

cur=1: c=1 → dp[1] = min(inf, dp[0]+1) = 1
cur=2: c=1 → dp[2] = min(inf, dp[1]+1) = 2
       c=2 → dp[2] = min(2, dp[0]+1) = 1    ← 用1個2元硬幣
cur=3: c=1 → dp[3] = min(inf, dp[2]+1) = 2
       c=2 → dp[3] = min(2, dp[1]+1) = 2    ← 2+1 或 1+1+1，都是2個
cur=4: c=1 → dp[4] = min(inf, dp[3]+1) = 3
       c=2 → dp[4] = min(3, dp[2]+1) = 2    ← 2+2，2個硬幣
cur=5: c=1 → dp[5] = min(inf, dp[4]+1) = 3
       c=2 → dp[5] = min(3, dp[3]+1) = 3
       c=5 → dp[5] = min(3, dp[0]+1) = 1    ← 1個5元硬幣
cur=6: c=1 → dp[6] = min(inf, dp[5]+1) = 2
       c=2 → dp[6] = min(2, dp[4]+1) = 2    ← 2+4(=2+2+2)
       c=5 → dp[6] = min(2, dp[1]+1) = 2    ← 5+1

dp[6] = 2 ✓（5+1 或 2+2+2）
```

---

## 題 2b：零錢組合數 `p2b_coin_change_ways`

```python
dp = [0] * (amount + 1)          # (A)
dp[0] = 1                        # (B)
for c in coins:                  # (C) 外層：先枚舉物品（硬幣種類）
    for x in range(c, amount + 1):  # (D) 內層：後枚舉金額（正序！）
        dp[x] += dp[x - c]       # (E)
return dp[amount]                # (F)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `dp = [0] * (amount+1)` | dp[x] = 湊出金額 x 的方法數，初始全為 0 |
| (B) | `dp[0] = 1` | 金額 0 有 1 種方法（什麼都不選），作為計數的起點 |
| (C) | `for c in coins` | **外層枚舉硬幣**：一次只處理一種面額 |
| (D) | `for x in range(c, amount+1)` | **內層正序枚舉金額**：從面額 c 到 amount |
| (E) | `dp[x] += dp[x-c]` | 轉移：選了這枚硬幣後，把「湊出 x-c 的方法數」累加上去 |
| (F) | `return dp[amount]` | 回傳湊出 amount 的總方法數 |

### 追蹤範例（coins=[1,2], amount=4）

```
初始：dp = [1, 0, 0, 0, 0]

先處理硬幣 c=1（只有1元硬幣的組合）：
  x=1: dp[1] += dp[0] = 1       {1}
  x=2: dp[2] += dp[1] = 1       {1+1}
  x=3: dp[3] += dp[2] = 1       {1+1+1}
  x=4: dp[4] += dp[3] = 1       {1+1+1+1}
  dp = [1, 1, 1, 1, 1]

再處理硬幣 c=2（加入2元硬幣的組合）：
  x=2: dp[2] += dp[0] = 1+1 = 2    {1+1, 2}
  x=3: dp[3] += dp[1] = 1+1 = 2    {1+1+1, 1+2}
  x=4: dp[4] += dp[2] = 1+2 = 3    {1+1+1+1, 1+1+2, 2+2}
  dp = [1, 1, 2, 2, 3]

dp[4] = 3 ✓
```

### 為什麼迴圈順序是「先物品後金額」？

```
先物品後金額（組合數）：1+2 和 2+1 算同一種
先金額後物品（排列數）：1+2 和 2+1 算不同種
```

先物品時，每種硬幣只會被「按順序加入」，不會重複計入排列。

---

## 題 3：Kadane `p3_kadane`

```python
best_end_here = nums[0]          # (A)
best_overall = nums[0]           # (B)
for x in nums[1:]:               # (C)
    best_end_here = max(x, best_end_here + x)  # (D)
    best_overall = max(best_overall, best_end_here)  # (E)
return best_overall              # (F)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `best_end_here = nums[0]` | 以第 0 個元素結尾的最大子陣列和 |
| (B) | `best_overall = nums[0]` | 全局目前看到的最大值 |
| (C) | `for x in nums[1:]` | 從第 2 個元素開始逐一處理 |
| (D) | `best_end_here = max(x, best_end_here + x)` | **核心轉移**：「自己重開」vs「接在前面後面」取較大 |
| (E) | `best_overall = max(best_overall, best_end_here)` | 每一步都更新全局最大值 |
| (F) | `return best_overall` | 回傳整個陣列的最大子陣列和 |

### 追蹤範例（nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]）

```
初始：best_end_here=-2, best_overall=-2

x=1:  best_end_here = max(1, -2+1) = 1     → 放棄前面，從1重新開始
      best_overall = max(-2, 1) = 1

x=-3: best_end_here = max(-3, 1-3) = -2     → 接在後面（-2 > -3）
      best_overall = max(1, -2) = 1

x=4:  best_end_here = max(4, -2+4) = 4      → 放棄前面，從4重新開始
      best_overall = max(1, 4) = 4

x=-1: best_end_here = max(-1, 4-1) = 3      → 接在後面（3 > -1）
      best_overall = max(4, 3) = 4

x=2:  best_end_here = max(2, 3+2) = 5       → 接在後面
      best_overall = max(4, 5) = 5

x=1:  best_end_here = max(1, 5+1) = 6       → 接在後面
      best_overall = max(5, 6) = 6

x=-5: best_end_here = max(-5, 6-5) = 1      → 接在後面
      best_overall = max(6, 1) = 6

x=4:  best_end_here = max(4, 1+4) = 5       → 接在後面
      best_overall = max(6, 5) = 6

return 6 ✓（子陣列 [4,-1,2,1]）
```

### max(x, best_end_here + x) 的兩種情況

```
情况1: best_end_here + x > x
  → 表示前面的子陣列「還有價值」，值得繼續延伸

情况2: x > best_end_here + x  （即 best_end_here < 0）
  → 表示前面的子陣列是負擔，不如從 x 重新開始
```

---

## 題 3b：Kadane 帶索引 `p3b_kadane_with_indices`

```python
best_end_here = nums[0]
best_overall = nums[0]
start = temp_start = 0           # (A)
end = 0                          # (B)
for i in range(1, len(nums)):    # (C)
    if nums[i] > best_end_here + nums[i]:  # (D)
        best_end_here = nums[i]
        temp_start = i            # (E) 重設起點
    else:
        best_end_here += nums[i]
    if best_end_here > best_overall:  # (F)
        best_overall = best_end_here
        start = temp_start       # (G) 確認起點
        end = i                  # (H) 更新終點
return best_overall, start, end
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `start = temp_start = 0` | start = 最終答案的起始索引，temp_start = 當前子陣列的暫定起點 |
| (B) | `end = 0` | 最終答案的結束索引 |
| (C) | `for i in range(1, len(nums))` | 從第 2 個元素開始，i 是當前位置的索引 |
| (D) | `if nums[i] > best_end_here + nums[i]` | 判斷：是否應該放棄前面的子陣列 |
| (E) | `temp_start = i` | **關鍵**：如果決定重新開始，把暫定起點更新為 i |
| (F) | `if best_end_here > best_overall` | 如果當前子陣列比歷史最佳更好 |
| (G) | `start = temp_start` | **關鍵**：把暫定起點「確認」為正式起點 |
| (H) | `end = i` | 結束索引更新為當前位置 |

### 為什麼需要 temp_start？

```
temp_start 是「當前正在延伸的子陣列的起點」
start 是「歷史最佳子陣列的起點」

只有當 best_end_here 破紀錄時，才把 temp_start 確認為 start
```

---

## 題 4：0/1 背包 `p4_knapsack_01`

```python
dp = [0] * (capacity + 1)       # (A)
for i in range(len(weights)):   # (B) 外層：逐個物品處理
    for w in range(capacity, weights[i] - 1, -1):  # (C) 內層：倒序枚舉容量
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])  # (D)
return dp[capacity]             # (E)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `dp = [0] * (capacity+1)` | dp[w] = 容量為 w 時的最大價值 |
| (B) | `for i in range(len(weights))` | 外層：一個一個物品考慮是否放入 |
| (C) | `for w in range(capacity, weights[i]-1, -1)` | **倒序**：從 capacity 往下到 weights[i] |
| (D) | `dp[w] = max(dp[w], dp[w-w[i]]+v[i])` | 「不選物品 i」vs「選物品 i」取最大 |
| (E) | `return dp[capacity]` | 回傳容量用滿時的最大價值 |

### 為什麼必須倒序？

```
假設物品 1: w=2, v=3

正序更新（錯誤）：
  dp[2] = max(dp[2], dp[0]+3) = 3   ← 用物品1更新 dp[2]
  dp[4] = max(dp[4], dp[2]+3) = 6   ← dp[2] 已經包含物品1！
  → 同一物品被選了兩次 = 無限背包

倒序更新（正確）：
  dp[4] = max(dp[4], dp[2]+3) = ?    ← dp[2] 是上一輪的舊值
  dp[2] = max(dp[2], dp[0]+3) = 3   ← 本輪才更新 dp[2]
  → 每個物品最多只被選一次
```

### 追蹤範例（weights=[2,3], values=[3,4], capacity=5）

```
初始：dp = [0, 0, 0, 0, 0, 0]

物品 0: w=2, v=3
  w=5: dp[5] = max(0, dp[3]+3) = 0   (dp[3]=0，還沒選到)
  w=4: dp[4] = max(0, dp[2]+3) = 0   (dp[2]=0)
  w=3: dp[3] = max(0, dp[1]+3) = 0   (dp[1]=0)
  w=2: dp[2] = max(0, dp[0]+3) = 3   ← 選了物品0
  dp = [0, 0, 3, 0, 0, 0]

物品 1: w=3, v=4
  w=5: dp[5] = max(0, dp[2]+4) = 7   ← 物品0+物品1，價值3+4=7 ✓
  w=4: dp[4] = max(0, dp[1]+4) = 4   ← 只選物品1
  w=3: dp[3] = max(0, dp[0]+4) = 4   ← 只選物品1
  dp = [0, 0, 3, 4, 4, 7]

dp[5] = 7 ✓
```

---

## 題 4b：無限背包 `p4b_knapsack_unbounded`

```python
dp = [0] * (capacity + 1)       # (A)
for i in range(len(weights)):   # (B) 外層：逐個物品
    for w in range(weights[i], capacity + 1):  # (C) 正序！
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])  # (D)
return dp[capacity]             # (E)
```

### 與 0/1 背包的差異

唯一差別在第 (C) 行：

```
0/1 背包:  for w in range(capacity, weights[i]-1, -1)  # 倒序
無限背包:  for w in range(weights[i], capacity+1)       # 正序
```

### 為什麼正序就變成無限背包？

```
正序更新（無限背包）：
  w=2: dp[2] = max(0, dp[0]+3) = 3   ← 選了物品1(w=2,v=3)
  w=4: dp[4] = max(0, dp[2]+3) = 6   ← dp[2] 已含物品1，再選一次 = 6
  w=6: dp[6] = max(0, dp[4]+3) = 9   ← 又選了一次 = 9

  → 同一物品可以被重複選取！
```

---

## 題 5：LIS O(N^2) `p5_lis_dp`

```python
n = len(nums)
dp = [1] * n                     # (A)
for i in range(n):               # (B) 外層：以第 i 個元素結尾
    for j in range(i):           # (C) 內層：枚舉 i 之前的所有 j
        if nums[j] < nums[i]:    # (D)
            dp[i] = max(dp[i], dp[j] + 1)  # (E)
return max(dp)                   # (F)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `dp = [1] * n` | 每個元素自己就是長度 1 的子序列（最小情況） |
| (B) | `for i in range(n)` | 外層：依次處理每個元素作為「子序列的結尾」 |
| (C) | `for j in range(i)` | 內層：回頭看 i 之前的所有元素 |
| (D) | `if nums[j] < nums[i]` | 只有嚴格遞增才能接在後面 |
| (E) | `dp[i] = max(dp[i], dp[j]+1)` | 從所有合法的 j 中，取最長的延伸 |
| (F) | `return max(dp)` | LIS 可能以任何位置結尾，取最大值 |

### 追蹤範例（nums=[10, 9, 2, 5, 3, 7]）

```
初始：dp = [1, 1, 1, 1, 1, 1]

i=0 (nums[0]=10): 無 j 可看，dp[0]=1

i=1 (nums[1]=9):
  j=0: 10 < 9? 否
  dp[1]=1

i=2 (nums[2]=2):
  j=0: 10 < 2? 否
  j=1: 9 < 2? 否
  dp[2]=1

i=3 (nums[3]=5):
  j=0: 10 < 5? 否
  j=1: 9 < 5? 否
  j=2: 2 < 5? 是 → dp[3] = max(1, 1+1) = 2
  dp[3]=2（子序列 [2,5]）

i=4 (nums[4]=3):
  j=0: 10 < 3? 否
  j=1: 9 < 3? 否
  j=2: 2 < 3? 是 → dp[4] = max(1, 1+1) = 2
  j=3: 5 < 3? 否
  dp[4]=2（子序列 [2,3]）

i=5 (nums[5]=7):
  j=0: 10 < 7? 否
  j=1: 9 < 7? 否
  j=2: 2 < 7? 是 → dp[5] = max(1, 1+1) = 2
  j=3: 5 < 7? 是 → dp[5] = max(2, 2+1) = 3
  j=4: 3 < 7? 是 → dp[5] = max(3, 2+1) = 3
  dp[5]=3（子序列 [2,5,7] 或 [2,3,7]）

return max([1,1,1,2,2,3]) = 3 ✓
```

---

## 題 5：LIS O(N log N) `p5_lis_nlogn`

```python
tails: list[int] = []           # (A)
for x in nums:                  # (B)
    pos = bisect_left(tails, x) # (C)
    if pos == len(tails):       # (D)
        tails.append(x)         # (E)
    else:
        tails[pos] = x          # (F)
return len(tails)               # (G)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `tails = []` | tails[k] = 長度 k+1 的遞增子序列的最小結尾值 |
| (B) | `for x in nums` | 依序處理每個數字 |
| (C) | `pos = bisect_left(tails, x)` | 二分搜：找到 x 應該插入 tails 的位置（第一個 >= x 的位置） |
| (D) | `if pos == len(tails)` | x 比所有 tails 元素都大，可以延伸出更長的子序列 |
| (E) | `tails.append(x)` | 延伸：新結尾值就是 x |
| (F) | `tails[pos] = x` | **替換**：用 x 取代 tails[pos]，因為 x 更小，未來更容易延伸 |
| (G) | `return len(tails)` | tails 的長度 = LIS 長度 |

### 追蹤範例（nums=[10, 9, 2, 5, 3, 7, 101, 18]）

```
x=10: tails=[], pos=0 → tails.append(10) → tails=[10]
x=9:  tails=[10], pos=0 → 替換 → tails=[9]
       9 比 10 小，放這裡更容易接後面的數
x=2:  tails=[9], pos=0 → 替換 → tails=[2]
x=5:  tails=[2], pos=1 → append → tails=[2,5]
x=3:  tails=[2,5], pos=1 → 替換 → tails=[2,3]
       3 比 5 小，放這裡更容易接後面的數
x=7:  tails=[2,3], pos=2 → append → tails=[2,3,7]
x=101: tails=[2,3,7], pos=3 → append → tails=[2,3,7,101]
x=18: tails=[2,3,7,101], pos=3 → 替換 → tails=[2,3,7,18]
       18 比 101 小，放這裡更容易接後面的數

return len(tails) = 4 ✓
```

### bisect_left 的行為

```python
from bisect import bisect_left

tails = [2, 3, 7]
bisect_left(tails, 5)  # → 1（第一個 >= 5 的位置，即 tails[1]=3 的位置）
bisect_left(tails, 7)  # → 2（第一個 >= 7 的位置）
bisect_left(tails, 100) # → 3（比全部都大，返回 len(tails)）
```

---

## 題 6：LCS 1D 壓縮 `p6_lcs_length`

```python
if len(a) < len(b):             # (A)
    short_s, long_s = a, b
else:
    short_s, long_s = b, a
dp = [0] * (len(short_s) + 1)   # (B)
for ch in long_s:                # (C) 外層：掃描長字串的每個字元
    prev_diag = 0                # (D)
    for j in range(1, len(short_s) + 1):  # (E) 內層：掃描短字串
        old = dp[j]              # (F)
        if ch == short_s[j - 1]:  # (G)
            dp[j] = prev_diag + 1  # (H)
        else:
            dp[j] = max(dp[j], dp[j - 1])  # (I)
        prev_diag = old          # (J)
return dp[-1]                    # (K)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `if len(a) < len(b)` | 確保 short_s 是較短的，減少空間 |
| (B) | `dp = [0] * (len(short_s)+1)` | 一維陣列替代二維表，空間 O(min(N,M)) |
| (C) | `for ch in long_s` | 外層：處理長字串的每個字元（對應 2D 表的列） |
| (D) | `prev_diag = 0` | 每列開始時，左上角 dp[i-1][j-1] 的值是 0 |
| (E) | `for j in range(1, len(short_s)+1)` | 內層：處理短字串的每個字元（對應 2D 表的行） |
| (F) | `old = dp[j]` | **關鍵**：在覆蓋 dp[j] 之前，先暫存它的值（下一輪的左上角） |
| (G) | `if ch == short_s[j-1]` | 兩字元相同 |
| (H) | `dp[j] = prev_diag + 1` | 對角線 dp[i-1][j-1] 的值 +1 |
| (I) | `dp[j] = max(dp[j], dp[j-1])` | 取「上方」和「左方」的較大值 |
| (J) | `prev_diag = old` | 把剛才存的舊值傳給下一輪作為左上角 |
| (K) | `return dp[-1]` | dp 的最後一個元素就是完整 LCS 長度 |

### 2D -> 1D 壓縮圖解

```
2D 表：dp[i][j] 依賴三個位置
  dp[i-1][j-1]（左上）  dp[i-1][j]（上）
  dp[i][j-1]（左）      dp[i][j]（要算的）

一維壓縮後：
  dp[j]   = 原來的 dp[i-1][j]（上方，尚未被覆蓋）
  dp[j-1] = 原來的 dp[i][j-1]（左方，本輪已更新）
  prev_diag = 原來的 dp[i-1][j-1]（左上角，用 old 暫存）

所以：dp[j] = max(dp[j], dp[j-1]) 就是 max(上方, 左方)
```

### 追蹤範例（A="AB", B="AC"）

```
short_s="AB"(m=2), long_s="AC"(n=2)

初始：dp = [0, 0, 0]

第 1 列（ch='A'）：
  prev_diag = 0
  j=1: old=0, 'A'=='A' → dp[1] = 0+1 = 1, prev_diag=0
  j=2: old=0, 'A'=='B'? 否 → dp[2] = max(0, 1) = 1, prev_diag=0
  dp = [0, 1, 1]

第 2 列（ch='C'）：
  prev_diag = 0
  j=1: old=1, 'C'=='A'? 否 → dp[1] = max(1, 0) = 1, prev_diag=1
  j=2: old=1, 'C'=='B'? 否 → dp[2] = max(1, 1) = 1, prev_diag=1
  dp = [0, 1, 1]

return dp[2] = 1 ✓（LCS = "A"）
```

---

## 題 6b：LCS 回溯 `p6b_lcs_string`

```python
for i in range(1, n + 1):       # (A) 建表
    for j in range(1, m + 1):   # (B)
        if a[i - 1] == b[j - 1]:  # (C)
            dp[i][j] = dp[i - 1][j - 1] + 1  # (D)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # (E)

i, j = n, m                     # (F) 從右下角開始回溯
result = []                     # (G)
while i > 0 and j > 0:          # (H) 回溯迴圈
    if a[i - 1] == b[j - 1]:   # (I) 字元相同 → 屬於 LCS
        result.append(a[i - 1]) # (J)
        i -= 1                  # (K)
        j -= 1                  # (L)
    elif dp[i - 1][j] > dp[i][j - 1]:  # (M)
        i -= 1                  # (N) 往上走
    else:
        j -= 1                  # (O) 往左走
return ''.join(reversed(result))  # (P)
```

### 回溯迴圈逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (F) | `i, j = n, m` | 從 dp 表的右下角開始 |
| (H) | `while i > 0 and j > 0` | 離開表格邊界就停止 |
| (I) | `if a[i-1] == b[j-1]` | 字元相同 → 這個字元在 LCS 中 |
| (J) | `result.append(a[i-1])` | 收集字元 |
| (K)(L) | `i -= 1; j -= 1` | 往左上走（對角線方向） |
| (M) | `dp[i-1][j] > dp[i][j-1]` | 上方值更大 → 往上走（捨棄 a[i-1]） |
| (N) | `i -= 1` | 往上 |
| (O) | `j -= 1` | 否則往左走（捨棄 b[j-1]） |
| (P) | `reversed(result)` | 回溯是從尾到頭，需反轉 |

---

## 題 7：編輯距離 `p7_edit_distance`

```python
n, m = len(word1), len(word2)
if n < m:                       # (A)
    word1, word2 = word2, word1
    n, m = m, n
dp = list(range(m + 1))         # (B)
for i in range(1, n + 1):       # (C) 外層：word1 的每個字元
    prev_diag = dp[0]           # (D)
    dp[0] = i                   # (E)
    for j in range(1, m + 1):   # (F) 內層：word2 的每個字元
        temp = dp[j]            # (G)
        if word1[i - 1] == word2[j - 1]:  # (H)
            dp[j] = prev_diag   # (I)
        else:
            dp[j] = 1 + min(dp[j], dp[j - 1], prev_diag)  # (J)
        prev_diag = temp        # (K)
return dp[m]                    # (L)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `if n < m` | 確保 word1 是較長的，節省空間 |
| (B) | `dp = list(range(m+1))` | 初始化：dp[j] = word1[:0] 轉為 word2[:j] 需要 j 次插入 |
| (C) | `for i in range(1, n+1)` | 外層：處理 word1 的第 i 個字元 |
| (D) | `prev_diag = dp[0]` | 暫存左上角值（dp[i-1][j-1]） |
| (E) | `dp[0] = i` | word1[:i] 轉為空字串需要 i 次刪除 |
| (F) | `for j in range(1, m+1)` | 內層：處理 word2 的第 j 個字元 |
| (G) | `temp = dp[j]` | 暫存 dp[j] 的舊值（下輪的左上角） |
| (H) | `if word1[i-1] == word2[j-1]` | 字元相同 → 無需操作 |
| (I) | `dp[j] = prev_diag` | 直接繼承左上角的值（dp[i-1][j-1]） |
| (J) | `dp[j] = 1 + min(...)` | **三種操作取最小**：dp[j]=刪除, dp[j-1]=插入, prev_diag=替換 |
| (K) | `prev_diag = temp` | 傳遞舊值給下一輪 |
| (L) | `return dp[m]` | word1[:n] 轉為 word2[:m] 的最少步數 |

### 三種操作的對應

```
dp[j]（上一輪的 dp[j]）     = dp[i-1][j] → 刪除 word1[i-1]
dp[j-1]（本輪已更新的左邊） = dp[i][j-1] → 插入 word2[j-1]
prev_diag（暫存的舊值）      = dp[i-1][j-1] → 替換 word1[i-1] 為 word2[j-1]
```

### 追蹤範例（word1="ab", word2="ac"）

```
初始：dp = [0, 1, 2]   （word2=""→"a"→"ac"）

i=1 (word1[0]='a')：
  prev_diag = dp[0] = 0
  dp[0] = 1

  j=1: temp=1, 'a'=='a' → dp[1] = prev_diag = 0, prev_diag=1
  j=2: temp=2, 'a'=='c'? 否 → dp[2] = 1+min(2, 0, 1) = 1, prev_diag=2
  dp = [1, 0, 1]

i=2 (word1[1]='b')：
  prev_diag = dp[0] = 1
  dp[0] = 2

  j=1: temp=0, 'b'=='a'? 否 → dp[1] = 1+min(0, 2, 1) = 1, prev_diag=0
  j=2: temp=1, 'b'=='c'? 否 → dp[2] = 1+min(1, 1, 0) = 1, prev_diag=1
  dp = [2, 1, 1]

dp[2] = 1 ✓（'b' → 'c'，1次替換）
```

---

## 題 8a：分割等和子集 `p8_partition_equal_subset`

```python
total = sum(nums)
if total % 2 != 0:              # (A)
    return False
target = total // 2             # (B)
dp = [False] * (target + 1)     # (C)
dp[0] = True                    # (D)
for num in nums:                # (E) 外層：逐個物品
    for s in range(target, num - 1, -1):  # (F) 內層：倒序枚舉總和
        dp[s] = dp[s] or dp[s - num]     # (G)
return dp[target]               # (H)
```

### 逐行解說

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (A) | `if total % 2 != 0` | 總和為奇數，不可能平分 |
| (B) | `target = total // 2` | 只需判斷能否湊出總和的一半 |
| (C) | `dp = [False] * (target+1)` | dp[s] = 能否用某些元素湊出總和 s |
| (D) | `dp[0] = True` | 總和 0 一定可以（什麼都不選） |
| (E) | `for num in nums` | 外層：逐個元素決定要不要放入 |
| (F) | `for s in range(target, num-1, -1)` | **倒序**：避免同一元素被重複使用 |
| (G) | `dp[s] = dp[s] or dp[s-num]` | 轉移：「不選 num」or「選了 num（從 s-num 跳過來）」 |
| (H) | `return dp[target]` | 能否湊出 target |

### 為什麼要倒序？

```
正序（錯誤）：
  num=2, s=2: dp[2] = dp[2] or dp[0] = True
  num=2, s=4: dp[4] = dp[4] or dp[2] = True ← dp[2] 已含 num=2，等於用了兩次

倒序（正確）：
  num=2, s=4: dp[4] = dp[4] or dp[2] = ? ← dp[2] 是本輪尚未更新的舊值
  num=2, s=2: dp[2] = dp[2] or dp[0] = True ← 本輪才更新
  → 每個元素最多用一次（0/1 背包邏輯）
```

### 追蹤範例（nums=[1,5,11,5], target=11）

```
初始：dp = [T, F, F, F, F, F, F, F, F, F, F, F]

num=1（倒序 11→1）：
  s=1: dp[1] = F or dp[0]=T → dp[1]=T
  dp = [T, T, F, F, F, F, F, F, F, F, F, F]

num=5（倒序 11→5）：
  s=11: dp[11] = F or dp[6]=F → 不變
  s=10: dp[10] = F or dp[5]=F → 不變
  s=6: dp[6] = F or dp[1]=T → dp[6]=T
  s=5: dp[5] = F or dp[0]=T → dp[5]=T
  dp = [T, T, F, F, F, T, T, F, F, F, F, F]

num=11（倒序 11→11）：
  s=11: dp[11] = F or dp[0]=T → dp[11]=T
  dp = [T, T, F, F, F, T, T, F, F, F, F, T]

dp[11] = True ✓（子集 [1,5,5] 和 [11]，都是 11）
```

---

## 題 8b：分割最小差 `p8b_partition_diff_min`

```python
total = sum(nums)
target = total // 2             # (A)
dp = [False] * (target + 1)     # (B)
dp[0] = True                    # (C)
for num in nums:                # (D) 與 8a 相同的 0/1 背包
    for s in range(target, num - 1, -1):  # (E)
        dp[s] = dp[s] or dp[s - num]     # (F)
for s in range(target, -1, -1):  # (G) 從大到小找可達的最大 s
    if dp[s]:                   # (H)
        return total - 2 * s    # (I)
return total                    # (J)
```

### 追加解說（(A)-(F) 同 8a）

| 行 | 程式碼 | 意義 |
|----|--------|------|
| (G) | `for s in range(target, -1, -1)` | 從 target 往下找，第一個可達的 s 就是「最接近一半」的值 |
| (H) | `if dp[s]` | 確認 s 是可達的 |
| (I) | `return total - 2*s` | 兩組和分別是 s 和 total-s，差為 total-2s |
| (J) | `return total` | 防禦性回傳（理論上不會到這裡） |

### 追蹤範例（nums=[1,6,11,5], total=23, target=11）

```
經過 D-F 的 0/1 背包後：
dp = [T, T, F, F, F, F, T, T, F, F, F, T]

G-H 從大到小找：
  s=11: dp[11]=T → return 23 - 2*11 = 1 ✓

兩組：[1,5,6](=12) 和 [11](=11)，差 = 1
```

---

## 複雜度總覽

| 題目 | 迴圈結構 | 時間複雜度 | 空間複雜度 |
|------|----------|-----------|-----------|
| 1. 爬樓梯 | 單迴圈 | O(N) | O(1) |
| 1b. 爬樓梯(k) | 雙迴圈 | O(N*K) | O(N) |
| 2. 最少硬幣 | 雙迴圈 | O(amount*C) | O(amount) |
| 2b. 零錢組合 | 雙迴圈 | O(amount*C) | O(amount) |
| 3. Kadane | 單迴圈 | O(N) | O(1) |
| 4. 0/1 背包 | 雙迴圈 | O(N*W) | O(W) |
| 4b. 無限背包 | 雙迴圈 | O(N*W) | O(W) |
| 5. LIS DP | 雙迴圈 | O(N^2) | O(N) |
| 5. LIS BS | 單迴圈+二分搜 | O(N log N) | O(N) |
| 6. LCS 1D | 雙迴圈 | O(N*M) | O(min(N,M)) |
| 7. 編輯距離 | 雙迴圈 | O(N*M) | O(min(N,M)) |
| 8. 分割 | 雙迴圈+單搜 | O(N*target) | O(target) |
