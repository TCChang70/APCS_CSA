# Unit 06：迴圈與數學計算 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. 累加器初始值
計算 1 到 10 總和的累加器應初始化為？
(A) 0  (B) 1  (C) -1  (D) 任意值

### 2. 階乘計算
```java
int n = 5;
long fact = 1;
for (int i = 1; i <= n; i++) {
    fact *= i;
}
System.out.println(fact);
```
輸出為何？
(A) 24  (B) 120  (C) 15  (D) 0

### 3. GCD 追蹤
```java
int a = 36, b = 24;
while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
}
System.out.println(a);
```
輸出為何？
(A) 6  (B) 12  (C) 18  (D) 24

### 4. 平均值陷阱
```java
int[] nums = {3, 4, 5};
int sum = 0;
for (int n : nums) sum += n;
double avg = sum / nums.length;
System.out.println(avg);
```
輸出為何？
(A) 4.0  (B) 4  (C) 3.0  (D) 3

### 5. Fibonacci
```java
int a = 1, b = 1;
for (int i = 3; i <= 7; i++) {
    int c = a + b;
    a = b;
    b = c;
}
System.out.println(b);
```
輸出為何？
(A) 5  (B) 8  (C) 13  (D) 21

---

## 程式實作（5 分）

### FRQ：質因數分解
撰寫方法，印出 n 的所有質因數（可重複，如 12 = 2 × 2 × 3）。

```java
public static void primeFactors(int n)
```

使用 while 迴圈從最小的質數 2 開始試除。

**範例：**
- `primeFactors(12)` → 輸出：`2 2 3`
- `primeFactors(100)` → 輸出：`2 2 5 5`
- `primeFactors(17)` → 輸出：`17`（質數本身）

> 解答請見：`answer-key.md`
