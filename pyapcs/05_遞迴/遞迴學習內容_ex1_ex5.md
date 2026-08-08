# 遞迴學習內容：ex1 ~ ex5

這份筆記以五支 Python 遞迴範例為主，幫助你理解「遞迴」的三個核心要素：

- 基底條件（Base Case）：問題縮小到最小時停止
- 遞迴步驟（Recursive Step）：把大問題拆成更小的相同問題
- 收斂方向：每次呼叫都朝向更接近基底條件的方向前進

---

## 1. ex1_階乘與費氏.py

### 1-1 這支程式在做什麼？
這支程式展示兩個最基本的遞迴例子：

- 階乘：$n! = n \times (n-1)!$
- 費氏數列：$F(n) = F(n-1) + F(n-2)$

### 1-2 核心觀念
#### 遞迴的兩個重要部分
1. 基底條件
   - `factorial(n)` 中，當 `n <= 1` 時直接回傳 `1`
   - `fibonacci(n)` 中，當 `n <= 1` 時直接回傳 `n`
2. 遞迴呼叫
   - `factorial(n - 1)` 會把問題縮小成更小的階乘
   - `fibonacci(n - 1)` 與 `fibonacci(n - 2)` 會把問題縮小成更小的費氏問題

### 1-3 程式碼解析
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

這段程式的執行方式是：
- 先判斷 `n` 是否已經很小
- 若不是，就呼叫自己處理 `n - 1`
- 等結果回來後再做乘法

### 1-4 執行流程（以 `factorial(5)` 為例）
```text
factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * 1)))
= 120
```

### 1-5 觀念重點
- 遞迴不是「無限自己呼叫自己」，而是要有一個會終止的條件
- 每次呼叫都要讓問題變小
- 遞迴常常和「函式呼叫堆疊」有關

### 1-6 常見錯誤
❌ 錯誤：忘記寫基底條件
```python
def factorial(n):
    return n * factorial(n - 1)
```
這樣會一直呼叫下去，最後造成 `RecursionError`

✅ 正確：先設計終止條件

### 1-7 執行結果
```text
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2
factorial(3) = 6
factorial(4) = 24
factorial(5) = 120
...
```

---

## 2. ex2_數位操作.py

### 2-1 這支程式在做什麼？
這支程式展示三種常見的數位操作：

- 數位和：把一個整數的每一位數字加起來
- 數字反轉：把整數倒過來
- 十進位轉二進位

### 2-2 核心觀念
這些題目最常用的技巧是：
- `n % 10`：取出最後一位數字
- `n // 10`：去掉最後一位數字

這兩個操作讓問題逐步縮小，適合用遞迴來處理。

### 2-3 程式碼解析
#### 2-3-1 數位和
```python
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)
```

執行流程：
```text
sum_digits(12345)
= 5 + sum_digits(1234)
= 5 + (4 + sum_digits(123))
= 5 + (4 + (3 + sum_digits(12)))
= 5 + (4 + (3 + (2 + sum_digits(1))))
= 5 + (4 + (3 + (2 + 1)))
= 15
```

#### 2-3-2 數字反轉
```python
def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)
```

這裡使用了「參數累積」的方式，把結果一路帶到最外層。

執行流程：
```text
reverse_num(12345)
= reverse_num(1234, 5)
= reverse_num(123, 54)
= reverse_num(12, 543)
= reverse_num(1, 5432)
= reverse_num(0, 54321)
= 54321
```

#### 2-3-3 十進位轉二進位
```python
def to_binary(n):
    if n <= 1:
        return str(n)
    return to_binary(n // 2) + str(n % 2)
```

### 2-4 觀念重點
- 遞迴不一定只靠「縮小數字大小」，也可以靠「縮小字串長度」或「縮小問題範圍」
- 在數位題中，`//` 與 `%` 是非常重要的拆解工具

### 2-5 執行結果
```text
15
54321
101010
```

---

## 3. ex3_字串回文.py

### 3-1 這支程式在做什麼？
這支程式判斷一個字串是否為回文。

- 回文：正著讀、反著讀都一樣
- 例如：`racecar`、`level`

### 3-2 核心觀念
判斷回文時，最簡單的遞迴策略是：
1. 比較第一個字元與最後一個字元
2. 如果不同，直接回傳 `False`
3. 如果相同，就縮小問題：去掉頭尾，再判斷內部字串

### 3-3 程式碼解析
```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
```

### 3-4 執行流程（以 `"racecar"` 為例）
```text
is_palindrome("racecar")
=> 比較 r 與 r 相同
=> 呼叫 is_palindrome("aceca")
=> 比較 a 與 a 相同
=> 呼叫 is_palindrome("cec")
=> 比較 c 與 c 相同
=> 呼叫 is_palindrome("e")
=> 長度 <= 1，回傳 True
```

### 3-5 反轉字串的寫法
```python
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
```

這個版本的思路是：
- 先把後面一部分反轉
- 再把第一個字元加到最後面

### 3-6 觀念重點
- 字串也可以用遞迴處理，重點是「縮小字串長度」
- `s[1:-1]` 的意思是：去掉頭尾，保留中間部分

### 3-7 執行結果
```text
is_palindrome('racecar') = True
is_palindrome('hello') = False
is_palindrome('level') = True
is_palindrome('python') = False
reverse_string('APCS') = 'SCPA'
```

---

## 4. ex4_子集合.py

### 4-1 這支程式在做什麼？
這支程式展示了「子集合」與「回溯（Backtracking）」的概念。

- 給定一組數字，列出所有可能的子集合
- 也可以判斷是否存在某個子集合總和等於目標值

### 4-2 核心觀念
這類問題常見的思路是：
- 對每個元素都有兩種選擇：取或不取
- 這會形成一棵「決策樄」
- 走到樹的每個葉節點時，就得到一個子集合

### 4-3 程式碼解析
#### 4-3-1 列出所有子集合
```python
def subsets(nums):
    ans = []

    def backtrack(start, path):
        ans.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return ans
```

這裡的 `path` 會像一個走訪路徑。
每次選擇一個元素後，就往下一層遞迴，回來之後再把它拿掉。

#### 4-3-2 子集合總和判斷
```python
def subset_sum(nums, target):
    def dfs(i, cur):
        if cur == target:
            return True
        if i == len(nums) or cur > target:
            return False
        return dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)
```

這支函式的思路是：
- `cur` 表示目前累積的總和
- 兩種選擇：
  - 取目前數字
  - 不取目前數字

### 4-4 執行流程（以 `subsets([1, 2, 3])` 為例）
```text
第一層：空集合
選 1：得到 [1]
選 1,2：得到 [1,2]
選 1,2,3：得到 [1,2,3]
選 2：得到 [2]
選 2,3：得到 [2,3]
選 3：得到 [3]
```

最後會得到：
```text
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

### 4-5 觀念重點
- 這是典型的「枚舉所有可能性」問題
- 遞迴常會配合「回溯」使用
- `path.pop()` 的作用是回復狀態，避免前一次選擇影響下一次

### 4-6 執行結果
```text
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
True
```

---

## 5. ex5_迷宮DFS.py

### 5-1 這支程式在做什麼？
這支程式用遞迴深度優先搜尋（DFS）來判斷：
- 某個迷宮中，從起點是否能走到終點
- 或者地圖中有多少個島嶼（連通區塊）

### 5-2 核心觀念
#### 5-2-1 迷宮路徑
```python
def has_path(grid, sr, sc, er, ec):
```
這個函式會從起點開始，依序向上下左右走，直到找到終點。

#### 5-2-2 訪問標記
```python
visited = [[False] * cols for _ in range(rows)]
```
這個陣列用來記錄哪些位置已經走過，避免無限循環。

### 5-3 程式碼解析
```python
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False
    if grid[r][c] == 1 or visited[r][c]:
        return False
    if r == er and c == ec:
        return True
    visited[r][c] = True
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if dfs(r + dr, c + dc):
            return True
    return False
```

這段程式的流程是：
1. 先確認位置是否合法
2. 如果是牆或已走過，就直接返回
3. 如果到達終點，就成功
4. 否則標記為已走過，向四個方向繼續探索

### 5-4 執行流程（以迷宮為例）
假設迷宮如下：
```text
0 0 1 0
1 0 1 0
0 0 0 0
0 1 1 0
```

從 `(0,0)` 開始，程式會依序往上下左右試探，直到找到 `(3,3)`。

### 5-5 島嶼數量的概念
```python
def count_islands(grid):
```
這個版本把 `1` 視為島嶼中的土地，
只要相鄰的 `1` 連在一起，就算同一個島嶼。

### 5-6 觀念重點
- DFS 很適合用來找「是否可達」與「可達區域」
- `visited` 是 DFS 很重要的概念，避免重複走同一格
- 這種題目很常出現在 APCS 的地圖與搜尋題

### 5-7 執行結果
```text
True
3
```

---

## 6. 這五支程式共同學到的觀念

### 6-1 遞迴三步驟
1. 找到基底條件
2. 設計縮小問題的方法
3. 讓每次呼叫都更接近終止條件

### 6-2 遞迴與函式呼叫
遞迴其實就是函式自己呼叫自己，只是每次呼叫的參數不同。

### 6-3 遞迴常見應用
- 數學問題：階乘、費氏數列
- 數位處理：數位和、反轉數字、轉二進位
- 字串問題：回文檢查、反轉字串
- 搜索問題：子集合、迷宮路徑、島嶼數量

---

## 7. 常見陷阱與練習建議

### ❌ 常見錯誤
- 忘記基底條件
- 遞迴沒有收斂
- 參數沒有變小
- 忘記回復狀態（例如 `path.pop()`）

### ✅ 建議練習
1. 試著把 `factorial(6)` 的流程畫出來
2. 自己寫一個 `sum_digits` 的非遞迴版本
3. 修改 `is_palindrome`，讓它能判斷空白字串
4. 嘗試把 `subset_sum` 改成回傳所有可行解
5. 把迷宮題改成找最短路徑

---

## 8. 總結
這五支程式讓你看到遞迴的完整面貌：
- 從最簡單的數學遞迴開始
- 再延伸到數位、字串、枚舉與搜尋問題
- 最後理解遞迴與回溯、DFS 的關聯

只要記住一句話：
> 遞迴的核心不是「一直重複」，而是「每次都把問題縮小，最後終止」。
