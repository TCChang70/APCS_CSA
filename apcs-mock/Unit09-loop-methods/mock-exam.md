# Unit 09：迴圈與方法整合 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. 方法的回傳
```java
public static boolean isEven(int n) {
    return n % 2 == 0;
}
```
下列哪個 for 迴圈正確使用了此方法印出 1-10 的偶數？
(A) `for (int i = 1; i <= 10; i++) { if (isEven(i)) System.out.print(i); }`
(B) `for (int i = 1; i <= 10; i++) { if (isEven(i) == true) System.out.print(i); }`
(C) A 和 B 都可以
(D) 都不行

### 2. 方法中提早 return
```java
public static boolean hasFactor(int n, int factor) {
    for (int i = 1; i <= n; i++) {
        if (i % factor == 0) return true;
    }
    return false;
}
```
`hasFactor(10, 3)` 回傳值為何？
(A) true  (B) false  (C) 3  (D) 編譯錯誤

### 3. 方法封裝
```java
public static int sumRange(int a, int b) {
    int s = 0;
    for (int i = a; i <= b; i++) s += i;
    return s;
}
```
`sumRange(3, 6)` 回傳值為何？
(A) 12  (B) 15  (C) 18  (D) 21

### 4. 在迴圈中呼叫方法
```java
public static boolean isPositive(int n) {
    return n > 0;
}

public static int countPositive(int[] arr) {
    int count = 0;
    for (int v : arr) {
        if (isPositive(v)) count++;
    }
    return count;
}
```
`countPositive({3, -1, 0, 5, -2})` 回傳值為何？
(A) 1  (B) 2  (C) 3  (D) 4

### 5. FRQ 模式
APCS FRQ 中，若 Part (a) 實作了 `sumArray(int[] arr)`，Part (b) 最有可能要求？
(A) 重新寫一個不同的 sum 方法
(B) 使用 `sumArray()` 協助計算平均值
(C) 刪除 Part (a) 的程式碼
(D) 使用 while 而非 for

---

## 程式實作（5 分）

### FRQ：數字特性檢查
撰寫兩個方法，Part (b) 必須呼叫 Part (a)：

**(a)** 判斷一個數是否為質數：`public static boolean isPrime(int n)`
**(b)** 統計一個數以內有多少質數：`public static int countPrimes(int n)`

```java
// 你的解答
```

**範例：** `countPrimes(10)` → 4（質數：2,3,5,7）

> 解答請見：`answer-key.md`
