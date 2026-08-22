# Day 9｜動態規劃（DP）教學與練習

> DP 是 APCS 高級題的**大魔王**，常落在第 3～4 題。
> 本文件是**完整的獨立教材**，包含概念、範例、表格追蹤、練習題與解答。
> 本日目標：掌握「狀態定義、轉移式、初始值」三步，能解爬樓梯、零錢、背包、LIS、LCS。

---

## 目錄

1. [DP 是什麼？](#dp-是什麼)
2. [三步驟：狀態、轉移、初始](#三步驟狀態轉移初始)
3. [五個基礎模型速覽](#五個基礎模型速覽)
4. [模型一：爬樓梯](#模型一爬樓梯)
5. [模型二：零錢問題](#模型二零錢問題)
6. [模型三：Kadane 最大子陣列和](#模型三kadane-最大子陣列和)
7. [模型四：0/1 背包](#模型四01-背包)
8. [模型五：LIS 最長遞增子序列](#模型五lis-最長遞增子序列)
9. [模型六：LCS 最長共同子序列](#模型六lcs-最長共同子序列)
10. [模型七：編輯距離](#模型七編輯距離)
11. [空間壓縮技巧](#空間壓縮技巧)
12. [常見錯誤檢查表](#常見錯誤檢查表)
13. [APCS 歷屆考古題](#apcs-歷屆考古題)
14. [練習題（含解答）](#練習題含解答)

---

## DP 是什麼？

> **動態規劃 = 把大問題拆成「有順序的小問題」，小問題的答案存起來重複用。**

關鍵字：**重複子問題**（同樣的小問題被問很多次）＋ **儲存**（算過就記下來）。

| 對比 | 遞迴（窮舉） | 動態規劃 |
| --- | --- | --- |
| 做法 | 每次都重算 | 算一次存起來 |
| 速度 | 指數級（很慢） | 多項式級（快） |
| 例子 | fib(40) 遞迴 → 極慢 | fib 用陣列存 → 一秒 |

### fib 遞迴 vs DP

```python
# 遞迴版：重複子問題爆炸，n=40 要好幾秒
def fib_recur(n):
    if n <= 1:                    # 基底條件：fib(0)=0, fib(1)=1
        return n                 # 直接回傳，不再展開
    return fib_recur(n - 1) + fib_recur(n - 2)  # 重複子問題：fib(3) 會被算很多次

# DP 陣列版：從小算到大，O(N) 一秒
def fib_dp(n):
    f = [0, 1]                   # 初始值：f[0]=0, f[1]=1
    for i in range(2, n + 1):    # 從第 2 項開始往上算
        f.append(f[i - 1] + f[i - 2])  # 第 i 項 = 前兩項相加（已算好，直接用）
    return f[n]                  # 答案存在 f[n] 裡

# 測試
print(fib_dp(10))   # 55
print(fib_dp(40))   # 102334155
```

---

## 三步驟：狀態、轉移、初始

寫 DP 一律問自己三件事：

| 步驟 | 問題 | 例：爬樓梯 |
| --- | --- | --- |
| 1. 狀態 | `dp[i]` 代表什麼？ | `dp[i]` = 走到第 i 階有幾種方法 |
| 2. 轉移式 | 小問題怎麼拼成大問題？ | `dp[i] = dp[i-1] + dp[i-2]` |
| 3. 初始值 | 最小問題是多少？ | `dp[0]=1`、`dp[1]=1` |

> 三步寫完 → 再想「答案要哪一格、迴圈怎麼跑」，程式就出來了。

---

## 五個基礎模型速覽

| 模型 | 狀態 | 轉移式 | 題型特徵 |
| --- | --- | --- | --- |
| 爬樓梯 | `dp[i]` = 走到 i 的方法數 | `dp[i] = dp[i-1] + dp[i-2]` | 每次走 1～k 步 |
| 零錢 | `dp[c]` = 湊 c 元的方法數/最少數 | `dp[c] += dp[c - coin]` | 硬幣組合 |
| Kadane | `dp[i]` = 以 i 結尾的最大和 | `dp[i] = max(a[i], dp[i-1]+a[i])` | 選或不選 |
| 背包 | `dp[w]` = 容量 w 最大價值 | 0-1：由大到小；無限：由小到大 | 容量限制選物 |
| LIS / LCS | `dp[i]` 前 i 個的最長 | `dp[i] = max(dp[j]+1)` / 雙層 | 子序列 |

---

## 模型一：爬樓梯

### 問題
每次走 1 或 2 階，走到第 n 階有幾種走法？

### 三步驟
| 步驟 | 內容 |
| --- | --- |
| 狀態 | `dp[i]` = 走到第 i 階的方法數 |
| 轉移 | `dp[i] = dp[i-1] + dp[i-2]` |
| 初始 | `dp[0] = 1`、`dp[1] = 1` |

### 完整程式

```python
n = int(input())                        # 讀入 n：目標階數
dp = [0] * (n + 1)                      # 建立長度 n+1 的陣列，dp[i] = 走到第 i 階的方法數
dp[0] = 1                               # 初始值：站在地面（第0階）算 1 種走法
dp[1] = 1                               # 初始值：走到第1階只有1種（走1步）
for i in range(2, n + 1):               # 從第2階開始，依序往上算每個 dp[i]
    dp[i] = dp[i - 1] + dp[i - 2]      # 轉移：最後一步走1階(i-1) + 走2階(i-2)的方法數相加
print(dp[n])                            # 答案：走到第 n 階的方法數
```

### 測試資料

輸入：`5`
輸出：`8`

### 表格追蹤（n = 5）

| i | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| dp[i] | 1 | 1 | 2 | 3 | 5 | 8 |

- dp[2] = dp[1]+dp[0] = 1+1 = 2（走法：1+1、2）
- dp[3] = dp[2]+dp[1] = 2+1 = 3
- dp[5] = dp[4]+dp[3] = 5+3 = **8**

> 看到「前一步的答案被後面一直重用」了嗎？這就是 DP 的核心。

### 進階：一次走 1~k 階

```python
n, k = map(int, input().split())        # 讀入 n（目標階數）、k（每次最多走幾步）
dp = [0] * (n + 1)                      # dp[i] = 走到第 i 階的方法數
dp[0] = 1                               # 初始值：站在地面算 1 種（哨兵值，確保轉移正確）
for i in range(1, n + 1):               # 外層：依序計算 dp[1] 到 dp[n]
    for j in range(1, min(i, k) + 1):   # 內層：枚舉「最後一步走了 j 階」
        dp[i] += dp[i - j]              # 從 (i-j) 階走 j 步到 i，把所有可能累加
print(dp[n])                            # 答案：走到第 n 階的總方法數
```

### 測試資料

輸入：`5 3`
輸出：`13`

### 表格追蹤（n=5, k=3）

| i | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| dp[i] | 1 | 1 | 2 | 4 | 7 | 13 |

- dp[3] = dp[2]+dp[1]+dp[0] = 2+1+1 = 4
- dp[5] = dp[4]+dp[3]+dp[2] = 7+4+2 = 13

---

## 模型二：零錢問題

### 問題 A：最少硬幣數
給定硬幣面額和目標金額，求湊出目標金額的**最少**硬幣數。

### 三步驟
| 步驟 | 內容 |
| --- | --- |
| 狀態 | `dp[x]` = 湊出金額 x 的最少硬幣數 |
| 轉移 | `dp[x] = min(dp[x - c] + 1)` for c in coins |
| 初始 | `dp[0] = 0`，其餘設為 INF |

### 完整程式

```python
coins = list(map(int, input().split()))  # 讀入硬幣面額，例如 [1,2,5]
amount = int(input())                    # 讀入目標金額，例如 6
inf = 10 ** 9                            # 用一個超大值代表「不可達」
dp = [inf] * (amount + 1)                # dp[x] = 湊出金額 x 的最少硬幣數，初始全部不可達
dp[0] = 0                               # 初始值：金額 0 需要 0 個硬幣（唯一確定的起點）
for cur in range(1, amount + 1):         # 外層：依序計算 dp[1] 到 dp[amount]
    for c in coins:                      # 內層：嘗試每一種硬幣面額
        if cur >= c:                     # 安全檢查：硬幣面額不能超過目前金額
            # 核心轉移：「不選這枚」vs「選這枚（從 dp[cur-c] 跳過來+1）」取最小
            dp[cur] = min(dp[cur], dp[cur - c] + 1)
print(-1 if dp[amount] == inf else dp[amount])  # 若仍為 inf 表示無法湊出，回傳 -1
```

### 測試資料

輸入：`1 2 5`
`6`
輸出：`2`

### 表格追蹤（coins=[1,2,5], amount=6）

| cur | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dp | 0 | 1 | 1 | 2 | 2 | 1 | 2 |

- dp[2]：用 1 個 2 元硬幣 = 1
- dp[5]：用 1 個 5 元硬幣 = 1
- dp[6]：5+1 = 2 個硬幣

### 問題 B：零錢組合數
給定硬幣面額和目標金額，求湊出目標金額的**組合數**（順序不同算同一種）。

```python
coins = list(map(int, input().split()))  # 讀入硬幣面額，例如 [1,2,5]
amount = int(input())                    # 讀入目標金額，例如 5
dp = [0] * (amount + 1)                 # dp[x] = 湊出金額 x 的組合數
dp[0] = 1                               # 初始值：金額 0 有 1 種方法（什麼都不選）
for c in coins:                         # 先枚舉硬幣種類（確保 1+2 和 2+1 算同一種）
    for x in range(c, amount + 1):      # 從面額 c 開始正序枚舉金額
        dp[x] += dp[x - c]             # 轉移：選了這枚硬幣後，累加「湊出 x-c 的方法數」
print(dp[amount])                       # 答案：湊出 amount 的總組合數
```

### 測試資料

輸入：`1 2 5`
`5`
輸出：`4`

### 表格追蹤（coins=[1,2,5], amount=5）

先處理 c=1：dp = [1,1,1,1,1,1]
再處理 c=2：dp = [1,1,2,2,3,3]
再處理 c=5：dp = [1,1,2,2,3,4]

組合：{1+1+1+1+1, 1+1+1+2, 1+2+2, 5} → 4 種

> **關鍵**：迴圈順序決定組合 vs 排列。先物品後金額 = 組合。

---

## 模型三：Kadane 最大子陣列和

### 問題
給定陣列，找連續子陣列的最大總和。

### 三步驟
| 步驟 | 內容 |
| --- | --- |
| 狀態 | `dp[i]` = 以第 i 個元素結尾的最大和 |
| 轉移 | `dp[i] = max(a[i], dp[i-1] + a[i])` |
| 初始 | `dp[0] = a[0]` |

### 完整程式

```python
nums = list(map(int, input().split()))  # 讀入陣列，例如 [-2,1,-3,4,-1,2,1,-5,4]
best_end_here = nums[0]                # 以目前元素結尾的最大和（從第一個元素開始）
best_overall = nums[0]                 # 全局目前看到的最大值
for x in nums[1:]:                     # 從第 2 個元素開始逐一處理
    # 核心轉移：「自己重開」vs「接在前面後面」取較大
    best_end_here = max(x, best_end_here + x)
    best_overall = max(best_overall, best_end_here)  # 每步更新全局最大值
print(best_overall)                    # 答案：整個陣列的最大連續子陣列和
```

### 測試資料

輸入：`-2 1 -3 4 -1 2 1 -5 4`
輸出：`6`

### 表格追蹤

| x | -2 | 1 | -3 | 4 | -1 | 2 | 1 | -5 | 4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| best_end_here | -2 | 1 | -2 | 4 | 3 | 5 | 6 | 1 | 5 |
| best_overall | -2 | 1 | 1 | 4 | 4 | 5 | 6 | 6 | 6 |

> 最大子陣列 = [4, -1, 2, 1]，和 = 6

### 逐步拆解：Kadane 演算法核心思路

以陣列 `[2, -3, 4, -1, 2]` 為例，追蹤兩個關鍵變數：

- **`current_max`**：**一定包含當前元素**的連續子陣列最大和（每步都強制納入 x）
- **`global_max`**：目前為止所見過的全局最大和

| 步驟 | 當前 x | 決策：max(x, current_max+x) | current_max | global_max |
| --- | --- | --- | --- | --- |
| 初始 | 2 | — | 2 | 2 |
| 1 | -3 | max(-3, 2-3=**-1**) → 接上 | -1 | 2 |
| 2 | 4 | max(**4**, -1+4=3) → 重新開始 | 4 | 4 |
| 3 | -1 | max(-1, 4-1=**3**) → 接上 | 3 | 4 |
| 4 | 2 | max(2, 3+2=**5**) → 接上 | 5 | **5** |

> 最大子陣列 = `[4, -1, 2]`，總和 = **5**

**核心決策**：`current_max = max(x, current_max + x)`
- 若 `x` 本身更大 → 前面的累積是「負擔」，從 x 重新開始新子陣列
- 若 `current_max + x` 更大 → 繼續把 x 接在前面的子陣列後面

### 進階：追蹤子陣列的起始與結束位置

若需要知道最大子陣列的**確切位置**，需額外記錄索引變化：

```python
def maxSubArray_with_indices(nums):
    current_max = global_max = nums[0]  # current_max=以目前元素結尾的最大和；global_max=全局最大
    temp_start = 0                     # 目前正在延伸的子陣列的暫定起點
    start = end = 0                    # 最終答案的起始與結束索引

    for i in range(1, len(nums)):      # 從第 2 個元素開始
        x = nums[i]
        if x > current_max + x:        # 情況1：x 本身比「接在後面」更大
            current_max = x            # → 前面的累積是負擔，從 x 重新開始
            temp_start = i             # 更新暫定起點為目前位置
        else:                          # 情況2：接在後面更划算
            current_max += x           # → 繼續延伸目前的子陣列

        if current_max > global_max:   # 若目前子陣列破了歷史紀錄
            global_max = current_max   # 更新全局最大值
            start = temp_start         # 把暫定起點「確認」為正式起點
            end = i                    # 結束索引更新為目前位置

    return global_max, start, end      # 回傳 (最大和, 起始索引, 結束索引)

# 測試
nums = [2, -3, 4, -1, 2]
max_sum, s, e = maxSubArray_with_indices(nums)
print(f"最大總和: {max_sum}")           # 5
print(f"子陣列索引: [{s}, {e}]")        # [2, 4]
print(f"最大子陣列: {nums[s:e+1]}")     # [4, -1, 2]
```

---

## 模型四：0/1 背包

### 問題
有 N 個物品（重量 weights[i]、價值 values[i]），背包容量 W，每個物品最多選一次，求最大價值。

### 三步驟
| 步驟 | 內容 |
| --- | --- |
| 狀態 | `dp[w]` = 容量 w 時的最大價值 |
| 轉移 | `dp[w] = max(dp[w], dp[w - weights[i]] + values[i])` |
| 初始 | `dp[0] = 0`，全陣列 0 |

### 完整程式

```python
weights = list(map(int, input().split()))  # 讀入每個物品的重量，例如 [2,3]
values = list(map(int, input().split()))   # 讀入每個物品的價值，例如 [3,4]
capacity = int(input())                    # 讀入背包容量，例如 5
dp = [0] * (capacity + 1)                 # dp[w] = 容量為 w 時的最大價值，初始全 0
for i in range(len(weights)):              # 外層：一個一個物品考慮是否放入
    # ⚠️ 必須倒序！從 capacity 往下到 weights[i]，避免同一物品被重複選取
    for w in range(capacity, weights[i] - 1, -1):
        # 核心轉移：「不選物品 i」vs「選物品 i（從 dp[w-weights[i]] 跳過來加 values[i]」
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
print(dp[capacity])                        # 答案：容量用滿時的最大價值
```

### 測試資料

輸入：
```
2 3
3 4
5
```
輸出：`7`

### 表格追蹤（weights=[2,3], values=[3,4], capacity=5）

| w | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 初始 | 0 | 0 | 0 | 0 | 0 | 0 |
| 物品0(w=2,v=3) | 0 | 0 | 3 | 3 | 3 | 3 |
| 物品1(w=3,v=4) | 0 | 0 | 3 | 4 | 4 | 7 |

- 物品1 更新 w=5：dp[5] = max(3, dp[2]+4) = max(3, 3+4) = 7
- 最大價值 = 7（物品0 + 物品1，3+4）

> **為什麼倒序？** 正序更新 dp[2] 後，dp[5] 會用到本輪的 dp[2]，等於物品0 被選了兩次。

### 無限背包（每個物品可選無限次）

```python
# 無限背包：唯一差別在迴圈改為正序更新
# 正序時，dp[w] 會用到本輪已更新的 dp[w-weights[i]]，等於物品可被重複選取
for w in range(weights[i], capacity + 1):                     # 正序：由小到大
    dp[w] = max(dp[w], dp[w - weights[i]] + values[i])       # 轉移式與 0/1 背包相同
```
```
物品 i：重量=3、價值=4
dp（上一輪）= [0, 0, 3, 3, 3, 3]    ← dp[2]=3 表示容量2最多值3

算到 w=5：
  dp[5] = max( dp[5], dp[5-3] + 4 )
             ↑       ↑
           不放      放（先查 dp[2]=3，再加價值4 → 3+4=7）
        = max(3, 7) = 7 ✓
```
---

## 模型五：LIS 最長遞增子序列

### 問題
給定陣列，找最長的嚴格遞增子序列長度。

### 作法一：O(N²) DP

> **容易簿清的寫法**，LIS 入門必學。外層 `i` 指「當前考慮到第 i 個元素」，內層 `j` 找「前面所有可以接就 i 的 j」。

```python
nums = list(map(int, input().split()))  # 讀入陣列，例如 [10,9,2,5,3,7,101,18]
n = len(nums)                          # 陣列長度
dp = [1] * n                           # dp[i] = 以 nums[i] 結尾的 LIS 長度，初始每個元素至少長度 1
for i in range(n):                     # 外層：以第 i 個元素作為子序列的結尾
    for j in range(i):                 # 內層：回頭看 i 之前的所有元素 j
        if nums[j] < nums[i]:         # 只有 nums[j] < nums[i] 才能接在後面（嚴格遞增）
            dp[i] = max(dp[i], dp[j] + 1)  # 從所有合法 j 中，取最長的延伸
print(max(dp))                        # 答案：dp 裡的最大值（LIS 可能以任何位置結尾）
```

### 測試資料

輸入：`10 9 2 5 3 7 101 18`
輸出：`4`

### 表格追蹤

| i | 0(10) | 1(9) | 2(2) | 3(5) | 4(3) | 5(7) | 6(101) | 7(18) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dp[i] | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 |

> LIS = [2,5,7,101] 或 [2,3,7,18]，長度 = 4

### 作法二：O(N log N) 二分搜

> **思路**：用 `tails` 陣列記錄「長度為 k+1 的 LIS 中、結尾元素最小可能是多少」。
> 這讓我們小走 `tails`，就能當來延伸的住點。

```python
from bisect import bisect_left          # bisect_left 用二分搜找插入位置

nums = list(map(int, input().split()))  # 讀入陣列，例如 [10,9,2,5,3,7,101,18]
tails = []                             # tails[k] = 長度 k+1 的遞增子序列的最小結尾值
for x in nums:                         # 依序處理每個數字
    pos = bisect_left(tails, x)        # 二分搜：找 tails 中第一個 >= x 的位置
    if pos == len(tails):              # x 比所有 tails 元素都大
        tails.append(x)                # → 可以延伸，LIS 長度 +1
    else:
        tails[pos] = x                 # → 替換：用更小的 x 取代，為未來延伸保留更大彈性
print(len(tails))                      # 答案：tails 長度 = LIS 長度
```

### 表格追蹤（nums=[10,9,2,5,3,7,101,18]）

| x | 10 | 9 | 2 | 5 | 3 | 7 | 101 | 18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tails | [10] | [9] | [2] | [2,5] | [2,3] | [2,3,7] | [2,3,7,101] | [2,3,7,18] |

> tails 長度 = LIS 長度 = 4

---

## 模型六：LCS 最長共同子序列

### 問題
給定兩個字串，找最長的共同子序列長度（子序列不必連續）。

### 完整程式（空間壓縮版）

> **為何被壓縮？** 原始 2D dp 表每個格子 `dp[i][j]` 只依賴上方（`dp[i-1][j]`）、左方（`dp[i][j-1]`）、對角（`dp[i-1][j-1]`）三格，因此可壓成一維。不過需用 `prev_diag` 對角小案來暫存左上角的舊値。

```python
a = input()                            # 讀入第一個字串，例如 "ABCDAB"
b = input()                            # 讀入第二個字串，例如 "BACB"
if len(a) < len(b):                    # 確保 short_s 是較短的字串，減少空間使用
    short_s, long_s = a, b             # 長的當外層迴圈，短的當內層（節省空間）
else:
    short_s, long_s = b, a
dp = [0] * (len(short_s) + 1)          # dp[j] = 目前處理到的列中，short_s[:j] 的 LCS 長度
for ch in long_s:                      # 外層：掃描長字串的每個字元（對應 2D 表的列）
    prev_diag = 0                      # 每列開始時，左上角 dp[i-1][j-1] 的值為 0
    for j in range(1, len(short_s) + 1):  # 內層：掃描短字串的每個字元（對應 2D 表的行）
        old = dp[j]                    # 關鍵：在覆蓋 dp[j] 之前先備份（下一輪要當 prev_diag 用）
        if ch == short_s[j - 1]:       # 兩字元相同 → 匹配
            dp[j] = prev_diag + 1      # 從左上角 dp[i-1][j-1] 的值 +1
        else:                          # 兩字元不同 → 不匹配
            dp[j] = max(dp[j], dp[j - 1])  # 取「上方」或「左方」的較大值
        prev_diag = old                # 把備份的舊值傳給下一輪作為左上角
print(dp[-1])                          # 答案：dp 最後一個元素 = 完整 LCS 長度
```

### 測試資料

輸入：
```
ABCDAB
BACB
```
輸出：`2`

### 2D 表格追蹤（A="ABCDAB", B="BACB"）

| | "" | B | A | C | B |
| --- | --- | --- | --- | --- | --- |
| "" | 0 | 0 | 0 | 0 | 0 |
| A | 0 | 0 | 1 | 1 | 1 |
| B | 0 | 1 | 1 | 1 | 2 |
| C | 0 | 1 | 1 | 2 | 2 |
| D | 0 | 1 | 1 | 2 | 2 |
| A | 0 | 1 | 2 | 2 | 2 |
| B | 0 | 1 | 2 | 2 | 3 |

> 最後答案 = 3（LCS = "ACB" 或 "BCB"）

---

## 模型七：編輯距離

### 問題
將 word1 轉換成 word2，每次可插入、刪除、替換一個字元，求最少操作數。

### 完整程式（空間壓縮版）

```python
word1 = input()                        # 讀入第一個字串，例如 "horse"
word2 = input()                        # 讀入第二個字串，例如 "ros"
n, m = len(word1), len(word2)          # 兩個字串的長度
if n < m:                              # 確保 word1 是較長的，節省空間
    word1, word2 = word2, word1        # 交換
    n, m = m, n
dp = list(range(m + 1))               # 初始值：dp[j] = word1[:0] 轉為 word2[:j] 需要 j 次插入
for i in range(1, n + 1):             # 外層：處理 word1 的第 i 個字元
    prev_diag = dp[0]                 # 暫存左上角值（dp[i-1][j-1]）
    dp[0] = i                        # word1[:i] 轉為空字串需要 i 次刪除
    for j in range(1, m + 1):         # 內層：處理 word2 的第 j 個字元
        temp = dp[j]                  # 備份 dp[j] 的舊值（下輪要當 prev_diag）
        if word1[i - 1] == word2[j - 1]:  # 兩字元相同 → 無需操作
            dp[j] = prev_diag         # 直接繼承左上角的值
        else:                         # 兩字元不同 → 三種操作取最小
            # dp[j]=刪除, dp[j-1]=插入, prev_diag=替換
            dp[j] = 1 + min(dp[j], dp[j - 1], prev_diag)
        prev_diag = temp              # 把備份傳給下一輪
print(dp[m])                          # 答案：word1[:n] 轉為 word2[:m] 的最少步數
```

### 測試資料

輸入：
```
horse
ros
```
輸出：`3`

### 表格追蹤（word1="horse", word2="ros"）

| | "" | r | o | s |
| --- | --- | --- | --- | --- |
| "" | 0 | 1 | 2 | 3 |
| h | 1 | 1 | 2 | 3 |
| o | 2 | 2 | 1 | 2 |
| r | 3 | 2 | 2 | 2 |
| s | 4 | 3 | 3 | 2 |
| e | 5 | 4 | 4 | 3 |

> horse → ros：h→r(替換)、刪除 h、e→s(替換) = 3 步

---

## 空間壓縮技巧

| 題型 | 原始空間 | 壓縮後 | 關鍵 |
| --- | --- | --- | --- |
| 爬樓梯 | O(N) | O(1) | 只需前兩項 |
| 0/1 背包 | O(N×W) | O(W) | 倒序更新 |
| 無限背包 | O(N×W) | O(W) | 正序更新 |
| LIS | O(N²) | O(N) | tails 陣列 |
| LCS | O(N×M) | O(min(N,M)) | prev_diag 暫存 |
| 編輯距離 | O(N×M) | O(min(N,M)) | prev_diag 暫存 |

### 什麼時候用壓縮？

- **遞迴**：`dp[i]` 只依賴 `dp[i-1]` 或 `dp[i-2]` → 只記前兩項
- **背包**：只依賴前一列 → 壓成一維
- **二維字串題**：只依賴上方、左方、左上角 → 一維 + prev_diag

---

## 常見錯誤檢查表

| # | 錯誤 | 為什麼錯 | 修正 |
| --- | --- | --- | --- |
| 1 | 陣列開太短（`[0]*n` 要 `dp[n]`） | 索引超界 | 開 `n+1` |
| 2 | 初始值設錯 | 第一格就錯，全盤皆錯 | 最小問題單獨驗證 |
| 3 | 迴圈方向錯（0/1 背包） | 同一物品被選兩次 | 0/1 由大到小、無限由小到大 |
| 4 | 忘了答案取哪一格 | 回傳錯位置 | 再讀題確認答案定義 |
| 5 | 題目要「最少」卻用 max | 求錯極值 | 先決定是 max 還是 min |
| 6 | 遞迴式 DP 沒記憶化 | 超慢 | 用 dict 或改迴圈 |
| 7 | dp[0] 沒設初始值 | 轉移式用到 dp[0] 時出錯 | 確認 dp[0] 的意義 |

---

## APCS 歷屆考古題

| 場次 | 題號 | 題名 | 考點 |
| --- | --- | --- | --- |
| 2024/6 | o079 | 最佳選擇 | 選或不選（一維 DP） |
| 2024/1 | m934 | 合併成本 | 石子合併（區間 DP） |
| 2023/10 | m373 | 投資遊戲 | DP |
| 2023/1 | j608 | 機器出租 | DP |
| 2021/9 | g278 | 美食博覽會 | DP |
| 2020/10 | f314 | 勇者修煉 | 二維 DP |
| 2020/7 | f582 | 病毒演化 | 樹＋DP |
| 2022/6 | i402 | 內積 | DP |

> 做法：每題先自己寫出「狀態、轉移、初始」三步，畫一張小表驗證，再寫程式。

---

## 練習題（含解答）

### 練習 1：爬樓梯變形 ★

> 每次可走 1、2 或 3 階，求到第 n 階的方法數。

**狀態、轉移、初始**：先自己寫出來，再看下方。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
n = int(input())                        # 讀入 n：目標階數
dp = [0] * (n + 1)                     # dp[i] = 走到第 i 階的方法數
dp[0] = 1                               # 初始：地面算 1 種
dp[1] = 1                               # 初始：第 1 階算 1 種
dp[2] = 2                               # 初始：第 2 階有 2 種（1+1、2）
for i in range(3, n + 1):               # 從第 3 階開始，考慮走 1、2、3 階
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]  # 轉移：走1階 + 走2階 + 走3階的方法數相加
print(dp[n])                            # 答案：走到第 n 階的總方法數
```

**測試資料**：輸入 `5`，輸出 `13`
**表格追蹤**：dp=[1,1,2,4,7,13]

</details>

---

### 練習 2：不取相鄰元素的最大和 ★

> 給定陣列，不取相鄰元素的最大和。

**狀態、轉移、初始**：先自己寫出來，再看下方。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
n = int(input())                        # 讀入元素個數
a = list(map(int, input().split()))     # 讀入陣列，例如 [3,2,7,9]
dp = [0] * n                            # dp[i] = 前 i+1 個元素中，符合規則的最大和
dp[0] = a[0]                            # 初始：只有一個元素，最大和就是它自己
if n >= 2:
    dp[1] = max(a[0], a[1])            # 兩個元素不能相鄰取 → 只能二選一
for i in range(2, n):                   # 從第 3 個元素開始推
    # 不取 a[i] → 答案維持 dp[i-1]；取 a[i] → 因不能相鄰，接 dp[i-2] 再加 a[i]
    dp[i] = max(dp[i - 1], dp[i - 2] + a[i])
print(dp[n - 1])                        # 答案：考慮完全部元素的最佳解
```

**測試資料**：輸入 `3 2 7 9`，輸出 `12`
**表格追蹤**：dp=[3,3,12,12]（取 3 和 9，或取 3 和 9）

</details>

---

### 練習 3：零錢最少硬幣 ★

> 給定硬幣面額和目標金額，求最少硬幣數。無法湊出回傳 -1。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
coins = list(map(int, input().split()))  # 讀入硬幣面額，例如 [2,5,7]
amount = int(input())                    # 讀入目標金額，例如 11
inf = 10 ** 9                            # 代表「不可達」的超大值
dp = [inf] * (amount + 1)               # dp[x] = 湊出 x 的最少硬幣數，初始全部不可達
dp[0] = 0                               # 金額 0 需要 0 個硬幣
for cur in range(1, amount + 1):         # 依序計算 dp[1] 到 dp[amount]
    for c in coins:                      # 嘗試每一種硬幣
        if cur >= c:                     # 硬幣面額不能超過目前金額
            dp[cur] = min(dp[cur], dp[cur - c] + 1)  # 取最小硬幣數
print(-1 if dp[amount] == inf else dp[amount])  # 無法湊出回傳 -1
```

**測試資料**：輸入 `2 5 7` 和 `11`，輸出 `3`（7+2+2=11，共 3 個硬幣）

</details>

---

### 練習 4：Kadane 最大子陣列和 ★★

> 給定陣列，找連續子陣列的最大總和。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
nums = list(map(int, input().split()))  # 讀入陣列，例如 [-2,1,-3,4,-1,2,1,-5,4]
best_end_here = nums[0]                # 以目前元素結尾的最大和
best_overall = nums[0]                 # 全局最大和
for x in nums[1:]:                     # 從第 2 個元素開始
    best_end_here = max(x, best_end_here + x)  # 「自己重開」vs「接在後面」取較大
    best_overall = max(best_overall, best_end_here)  # 更新全局最大值
print(best_overall)                    # 答案：最大連續子陣列和
```

**測試資料**：輸入 `-2 1 -3 4 -1 2 1 -5 4`，輸出 `6`

</details>

---

### 練習 5：0/1 背包 ★★

> 有 N 個物品和背包容量 W，每個物品只能選一次，求最大價值。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
weights = list(map(int, input().split()))  # 讀入物品重量
values = list(map(int, input().split()))   # 讀入物品價值
capacity = int(input())                    # 讀入背包容量
dp = [0] * (capacity + 1)                 # dp[w] = 容量 w 時的最大價值
for i in range(len(weights)):              # 外層：逐個物品
    for w in range(capacity, weights[i] - 1, -1):  # ⚠️ 倒序！避免同一物品被重複選取
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])  # 不選 vs 選，取較大
print(dp[capacity])                        # 答案：容量用滿時的最大價值
```

**測試資料**：輸入 `2 3 4 5`、`3 4 5 6` 和 `5`，輸出 `7`

</details>

---

### 練習 6：LIS 最長遞增子序列 ★★

> 給定陣列，找最長嚴格遞增子序列長度。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
from bisect import bisect_left          # 二分搜找插入位置

nums = list(map(int, input().split()))  # 讀入陣列，例如 [10,9,2,5,3,7,101,18]
tails = []                             # tails[k] = 長度 k+1 的 LIS 的最小結尾值
for x in nums:                         # 依序處理每個數字
    pos = bisect_left(tails, x)        # 二分搜：找第一個 >= x 的位置
    if pos == len(tails):              # x 比所有 tails 元素都大
        tails.append(x)                # → 可延伸 LIS
    else:
        tails[pos] = x                 # → 替換：用更小的 x 取代
print(len(tails))                      # 答案：tails 長度 = LIS 長度
```

**測試資料**：輸入 `10 9 2 5 3 7 101 18`，輸出 `4`

</details>

---

### 練習 7：LCS 最長共同子序列 ★★

> 給定兩個字串，找最長共同子序列長度。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
a = input()                            # 讀入第一個字串，例如 "ABCDAB"
b = input()                            # 讀入第二個字串，例如 "BACB"
if len(a) < len(b):                    # 確保 short_s 是較短的，減少空間
    short_s, long_s = a, b             # 長的當外層，短的當內層
else:
    short_s, long_s = b, a
dp = [0] * (len(short_s) + 1)          # dp[j] = 目前的 LCS 長度
for ch in long_s:                      # 外層：掃描長字串的每個字元
    prev_diag = 0                      # 每列開始：左上角初始為 0
    for j in range(1, len(short_s) + 1):  # 內層：掃描短字串的每個字元
        old = dp[j]                    # 備份舊值（下一輪要當 prev_diag）
        if ch == short_s[j - 1]:       # 兩字元相同 → 匹配
            dp[j] = prev_diag + 1      # 從左上角 +1
        else:                          # 兩字元不同
            dp[j] = max(dp[j], dp[j - 1])  # 取上方或左方較大值
        prev_diag = old                # 傳遞舊值給下一輪
print(dp[-1])                          # 答案：完整 LCS 長度
```

**測試資料**：輸入 `ABCDAB` 和 `BACB`，輸出 `3`

</details>

---

### 練習 8：分割等和子集 ★★★

> 給定陣列，判斷能否分成兩個總和相等的子集。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
nums = list(map(int, input().split()))  # 讀入陣列，例如 [1,5,11,5]
total = sum(nums)                      # 計算總和 = 22
if total % 2 != 0:                     # 總和為奇數，不可能平分
    print(False)
else:
    target = total // 2                 # 只需判斷能否湊出總和的一半 = 11
    dp = [False] * (target + 1)        # dp[s] = 能否用某些元素湊出總和 s
    dp[0] = True                       # 初始值：總和 0 一定可以（什麼都不選）
    for num in nums:                   # 外層：逐個元素決定要不要放入
        for s in range(target, num - 1, -1):  # ⚠️ 倒序：避免同一元素被重複使用
            dp[s] = dp[s] or dp[s - num]      # 轉移：「不選 num」or「選了 num」
    print(dp[target])                  # 答案：能否湊出 target
```

**測試資料**：輸入 `1 5 11 5`，輸出 `True`
**解釋**：[1,5,5] 和 [11]，都是 11

</details>

---

### 練習 9：分割兩子集最小差 ★★★

> 給定陣列，分成兩組使兩組和的差最小，回傳最小差。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
nums = list(map(int, input().split()))  # 讀入陣列，例如 [1,6,11,5]
total = sum(nums)                      # 總和 = 23
target = total // 2                     # 目標：找到最接近一半的可達總和 = 11
dp = [False] * (target + 1)            # dp[s] = 能否用某些元素湊出總和 s
dp[0] = True                           # 初始值：總和 0 一定可以
for num in nums:                       # 外層：逐個元素
    for s in range(target, num - 1, -1):  # ⚠️ 倒序：0/1 背包邏輯，元素只用一次
        dp[s] = dp[s] or dp[s - num]   # 轉移：不選 or 選
for s in range(target, -1, -1):        # 從大到小找可達的最大 s（最接近一半）
    if dp[s]:                          # 找到第一個可達的
        print(total - 2 * s)           # 兩組和為 s 與 total-s，差為 total-2s
        break
```

**測試資料**：輸入 `1 6 11 5`，輸出 `1`
**解釋**：[1,5,6](=12) 和 [11](=11)，差 = 1

</details>

---

## 通過標準

1. **爬樓梯**（含 k 階變形）：能自己寫出三步驟 + 程式
2. **零錢問題**（最少硬幣 + 組合數）：能區分 min vs 計數
3. **Kadane**：能解釋 max(x, best_end_here+x) 的兩種情況
4. **0/1 背包**：能解釋為什麼倒序更新
5. **LIS**：能用 O(N²) 和 O(N log N) 兩種方式解
6. **LCS**：能畫出 2D 表格並解釋空間壓縮
7. **歷屆題**：至少能寫出其中 2 題的三步驟

> 通過標準：能說出每題的「狀態、轉移、初始」各是什麼，且跑得出來。
