# Unit 07：break 與 continue — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. break 行為
```java
for (int i = 0; i < 10; i++) {
    if (i == 4) break;
    System.out.print(i + " ");
}
```
輸出為何？
(A) 0 1 2 3  (B) 0 1 2 3 4  (C) 0 1 2 3 4 5  (D) 4

### 2. continue 行為
```java
for (int i = 1; i <= 6; i++) {
    if (i % 2 == 0) continue;
    System.out.print(i + " ");
}
```
輸出為何？
(A) 1 3 5  (B) 2 4 6  (C) 1 2 3 4 5 6  (D) 1 3 5 6

### 3. break 在巢狀迴圈
```java
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (j == 1) break;
        System.out.print(i + "" + j + " ");
    }
}
```
輸出為何？
(A) 00 10 20  (B) 00 01 10 11 20 21  (C) 00 01 02 10 11 12 20 21 22  (D) 00

### 4. break vs return
```java
public static int find(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```
若 `arr = {3, 7, 2, 9}`，`find(arr, 2)` 回傳值為何？
(A) 1  (B) 2  (C) 3  (D) -1

### 5. 綜合
```java
int sum = 0;
for (int i = 1; i <= 20; i++) {
    if (i % 4 == 0) continue;
    if (sum > 30) break;
    sum += i;
}
System.out.println(sum);
```
輸出為何？
(A) 30  (B) 37  (C) 34  (D) 31

---

## 程式實作（5 分）

### FRQ：第一個完全平方數
撰寫方法，從 1 開始找到第一個大於 `n` 且為完全平方數（某整數的平方）的數。

```java
public static int nextPerfectSquare(int n)
```

使用 `break` 在找到答案後立即終止迴圈。

**範例：**
- `nextPerfectSquare(10)` → 16（4²）
- `nextPerfectSquare(50)` → 64（8²）
- `nextPerfectSquare(100)` → 121（11² 而不是 100，因為必須大於 n）

> 解答請見：`answer-key.md`
