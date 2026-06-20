# Unit 14：Array 遍歷 — 增強式 `for` 迴圈 (for-each) — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. for-each 語法
下列哪個 for-each 語法是正確的？
(A) `for (int i : arr) { }`
(B) `for (int i : arr[]) { }`
(C) `for (int i : int[] arr) { }`
(D) `for (int[] i : arr) { }`

### 2. for-each 計算總和
```java
int[] nums = {2, 4, 6, 8};
int total = 0;
for (int n : nums) {
    total += n;
}
System.out.println(total);
```
輸出為何？
(A) 10  (B) 18  (C) 20  (D) 24

### 3. for-each 修改（陷阱題）
```java
int[] data = {1, 2, 3};
for (int x : data) {
    x *= 2;
}
System.out.println(data[0]);
```
輸出為何？
(A) 0  (B) 1  (C) 2  (D) 編譯錯誤

### 4. for-each vs 標準 for
下列哪種情況「不適合」使用 for-each？
(A) 計算陣列中所有元素的總和
(B) 將陣列中每個元素乘以 2
(C) 印出陣列中所有元素
(D) 判斷陣列中是否有負數

### 5. for-each 字串陣列
```java
String[] words = {"A", "B", "C"};
for (String w : words) {
    System.out.print(w + w + " ");
}
```
輸出為何？
(A) A B C  (B) AA BB CC  (C) ABC  (D) A B C A B C

---

## 程式實作（5 分）

### FRQ：總和大於門檻值
給定整數陣列，使用 for-each 判斷陣列中是否有「連續兩個元素」的和大於門檻值 `threshold`。

```java
public static boolean hasAdjacentSumGreaterThan(int[] arr, int threshold)
```

**限制：** 必須使用 for-each 迴圈。（提示：需要追蹤前一個元素）

**範例：**
- `hasAdjacentSumGreaterThan({3, 7, 9, 1, 4}, 15)` → true（7+9=16>15）
- `hasAdjacentSumGreaterThan({3, 7, 1, 9, 4}, 20)` → false
- `hasAdjacentSumGreaterThan({5, 5}, 9)` → true（5+5=10>9）

> 解答請見：`answer-key.md`
