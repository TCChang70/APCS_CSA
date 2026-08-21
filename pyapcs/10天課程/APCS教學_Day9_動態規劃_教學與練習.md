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
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)

# DP 陣列版：從小算到大，O(N) 一秒
def fib_dp(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

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
n = int(input())
# dp[i] = 走到第 i 階的方法數
dp = [0] * (n + 1)
dp[0] = 1                    # 初始：地面算 1 種
dp[1] = 1                    # 初始：第 1 階算 1 種
for i in range(2, n + 1):
    # 轉移：最後一步走 1 階（從 i-1 來）+ 走 2 階（從 i-2 來）
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
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
n, k = map(int, input().split())
dp = [0] * (n + 1)
dp[0] = 1                    # dp[0]=1 確保從原點出發的路徑都被計入
for i in range(1, n + 1):
    for j in range(1, min(i, k) + 1):
        dp[i] += dp[i - j]
print(dp[n])
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
coins = list(map(int, input().split()))
amount = int(input())
# dp[x] = 湊出金額 x 所需最少硬幣數
inf = 10 ** 9
dp = [inf] * (amount + 1)
dp[0] = 0                       # 金額 0 需要 0 個硬幣
for cur in range(1, amount + 1):
    for c in coins:
        if cur >= c:
            dp[cur] = min(dp[cur], dp[cur - c] + 1)
print(-1 if dp[amount] == inf else dp[amount])
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
coins = list(map(int, input().split()))
amount = int(input())
# dp[x] = 湊出金額 x 的方法數
dp = [0] * (amount + 1)
dp[0] = 1                       # 金額 0 有 1 種方法
for c in coins:                 # 先枚舉硬幣（組合）
    for x in range(c, amount + 1):
        dp[x] += dp[x - c]
print(dp[amount])
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
nums = list(map(int, input().split()))
# best_end_here = 以目前元素結尾的最大和
# best_overall = 全局最大和
best_end_here = nums[0]
best_overall = nums[0]
for x in nums[1:]:
    best_end_here = max(x, best_end_here + x)
    best_overall = max(best_overall, best_end_here)
print(best_overall)
```

### 測試資料
輸入：`-2 1 -3 4 -1 2 `
輸出：`6`
### 表格追蹤

| x | -2 | 1 | -3 | 4 | -1 | 2 | 1 | -5 | 4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| best_end_here | -2 | 1 | -2 | 4 | 3 | 5 | 6 | 1 | 5 |
| best_overall | -2 | 1 | 1 | 4 | 4 | 5 | 6 | 6 | 6 |

> 最大子陣列 = [4, -1, 2, 1]，和 = 6

### 要找出最大子陣列的起始位置和結束位置，我們需要在程式碼中加入幾個變數來追蹤索引（Index）的變化。關鍵邏輯是：
### 當 current_max 決定拋棄前面的累積，自己重新開始時，就代表找到了新的可能起點；而當 global_max 被更新時，就代表找到了目前為止最好的起點與終點。
```python
def maxSubArrayWithIndices(nums):
    # 初始狀態
    current_max = global_max = nums[0]
    
    # 追蹤索引的變數
    start = 0         # 最終最大子陣列的起點
    end = 0           # 最終最大子陣列的終點
    temp_start = 0    # 目前正在計算的子陣列起點

    for i in range(1, len(nums)):
        x = nums[i]
        
        # 決定要加入前面的序列，還是自己重新開始
        if x > current_max + x:
            current_max = x
            temp_start = i    # 自己重新開始，將暫時起點設為當前位置
        else:
            current_max = current_max + x
        
        # 當發現更大的總和時，更新全域最大值以及真正的起點、終點
        if current_max > global_max:
            global_max = current_max
            start = temp_start  # 紀錄真正的起點
            end = i             # 當前位置就是終點

    return global_max, start, end

### 測試前面用過的範例 [2, -3, 4, -1, 2]
nums = [2, -3, 4, -1, 2]
max_sum, start_idx, end_idx = maxSubArrayWithIndices(nums)

print(f"最大總和: {max_sum}")
print(f"起始索引: {start_idx}, 結束索引: {end_idx}")
print(f"最大子陣列: {nums[start_idx:end_idx+1]}")
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
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
capacity = int(input())
# dp[w] = 容量為 w 時的最大價值
dp = [0] * (capacity + 1)
for i in range(len(weights)):
    # ⚠️ 必須倒序！避免同一物品被重複選取
    for w in range(capacity, weights[i] - 1, -1):
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
print(dp[capacity])
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
# 唯一差別：正序更新
for w in range(weights[i], capacity + 1):
    dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
```

---

## 模型五：LIS 最長遞增子序列

### 問題
給定陣列，找最長的嚴格遞增子序列長度。

### 作法一：O(N²) DP

```python
nums = list(map(int, input().split()))
n = len(nums)
# dp[i] = 以 nums[i] 結尾的最長遞增子序列長度
dp = [1] * n
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
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

```python
from bisect import bisect_left

nums = list(map(int, input().split()))
tails = []                          # tails[k] = 長度 k+1 的遞增子序列最小結尾值
for x in nums:
    pos = bisect_left(tails, x)     # 二分搜找插入位置
    if pos == len(tails):
        tails.append(x)             # 可延伸
    else:
        tails[pos] = x              # 替換（用更小的值）
print(len(tails))
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

```python
a = input()
b = input()
if len(a) < len(b):
    short_s, long_s = a, b
else:
    short_s, long_s = b, a
# dp[j] = 目前列中 A[:i] 與 B[:j] 的 LCS 長度
dp = [0] * (len(short_s) + 1)
for ch in long_s:
    prev_diag = 0
    for j in range(1, len(short_s) + 1):
        old = dp[j]
        if ch == short_s[j - 1]:
            dp[j] = prev_diag + 1     # 對角線 +1
        else:
            dp[j] = max(dp[j], dp[j - 1])
        prev_diag = old
print(dp[-1])
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
word1 = input()
word2 = input()
n, m = len(word1), len(word2)
if n < m:
    word1, word2 = word2, word1
    n, m = m, n
# dp[j] = word1[:i] 轉為 word2[:j] 的最少步數
dp = list(range(m + 1))
for i in range(1, n + 1):
    prev_diag = dp[0]
    dp[0] = i
    for j in range(1, m + 1):
        temp = dp[j]
        if word1[i - 1] == word2[j - 1]:
            dp[j] = prev_diag              # 無需操作
        else:
            dp[j] = 1 + min(dp[j], dp[j - 1], prev_diag)
        prev_diag = temp
print(dp[m])
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
n = int(input())
dp = [0] * (n + 1)
dp[0] = 1                    # 地面 1 種
dp[1] = 1                    # 第 1 階 1 種
dp[2] = 2                    # 第 2 階：1+1、2
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
print(dp[n])
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
n = int(input())
a = list(map(int, input().split()))
# dp[i] = 前 i+1 個元素中，符合規則的最大和
dp = [0] * n
dp[0] = a[0]
if n >= 2:
    dp[1] = max(a[0], a[1])
for i in range(2, n):
    # 不取 a[i] → dp[i-1]；取 a[i] → dp[i-2] + a[i]
    dp[i] = max(dp[i - 1], dp[i - 2] + a[i])
print(dp[n - 1])
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
coins = list(map(int, input().split()))
amount = int(input())
inf = 10 ** 9
dp = [inf] * (amount + 1)
dp[0] = 0
for cur in range(1, amount + 1):
    for c in coins:
        if cur >= c:
            dp[cur] = min(dp[cur], dp[cur - c] + 1)
print(-1 if dp[amount] == inf else dp[amount])
```

**測試資料**：輸入 `2 5 7` 和 `11`，輸出 `3`（5+5+1... 不行！5+2+2+2=11 → 4 個。但 5+2+2+2=4個，其實 11=5+2+2+2 → 4 個硬幣）

</details>

---

### 練習 4：Kadane 最大子陣列和 ★★

> 給定陣列，找連續子陣列的最大總和。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
nums = list(map(int, input().split()))
best_end_here = nums[0]
best_overall = nums[0]
for x in nums[1:]:
    best_end_here = max(x, best_end_here + x)
    best_overall = max(best_overall, best_end_here)
print(best_overall)
```

**測試資料**：輸入 `-2 1 -3 4 -1 2 1 -5 4`，輸出 `6`

</details>

---

### 練習 5：0/1 背包 ★★

> 有 N 個物品和背包容量 W，每個物品只能選一次，求最大價值。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
capacity = int(input())
dp = [0] * (capacity + 1)
for i in range(len(weights)):
    for w in range(capacity, weights[i] - 1, -1):
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
print(dp[capacity])
```

**測試資料**：輸入 `2 3 4 5`、`3 4 5 6` 和 `5`，輸出 `7`

</details>

---

### 練習 6：LIS 最長遞增子序列 ★★

> 給定陣列，找最長嚴格遞增子序列長度。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
from bisect import bisect_left

nums = list(map(int, input().split()))
tails = []
for x in nums:
    pos = bisect_left(tails, x)
    if pos == len(tails):
        tails.append(x)
    else:
        tails[pos] = x
print(len(tails))
```

**測試資料**：輸入 `10 9 2 5 3 7 101 18`，輸出 `4`

</details>

---

### 練習 7：LCS 最長共同子序列 ★★

> 給定兩個字串，找最長共同子序列長度。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
a = input()
b = input()
if len(a) < len(b):
    short_s, long_s = a, b
else:
    short_s, long_s = b, a
dp = [0] * (len(short_s) + 1)
for ch in long_s:
    prev_diag = 0
    for j in range(1, len(short_s) + 1):
        old = dp[j]
        if ch == short_s[j - 1]:
            dp[j] = prev_diag + 1
        else:
            dp[j] = max(dp[j], dp[j - 1])
        prev_diag = old
print(dp[-1])
```

**測試資料**：輸入 `ABCDAB` 和 `BACB`，輸出 `3`

</details>

---

### 練習 8：分割等和子集 ★★★

> 給定陣列，判斷能否分成兩個總和相等的子集。

<details>
<summary>解答（先自己寫再打開）</summary>

```python
nums = list(map(int, input().split()))
total = sum(nums)
if total % 2 != 0:
    print(False)
else:
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]
    print(dp[target])
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
nums = list(map(int, input().split()))
total = sum(nums)
target = total // 2
dp = [False] * (target + 1)
dp[0] = True
for num in nums:
    for s in range(target, num - 1, -1):
        dp[s] = dp[s] or dp[s - num]
for s in range(target, -1, -1):
    if dp[s]:
        print(total - 2 * s)
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
