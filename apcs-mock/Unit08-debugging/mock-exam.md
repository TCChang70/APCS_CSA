# Unit 08：常見迴圈錯誤與除錯技巧 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. 找出 Bug
```java
int sum = 0;
for (int i = 0; i <= 10; i++) {
    sum += i;
}
double avg = sum / 10;
System.out.println(avg);
```
此程式計算 0-10 的平均值。結果為何？
(A) 5.0  (B) 5.5  (C) 5  (D) 6

### 2. 無限迴圈原因
```java
int i = 0;
while (i < 10) {
    System.out.println(i);
}
```
此為無限迴圈，原因為何？
(A) 條件錯誤  (B) 缺少 i++  (C) 缺少 System.out.println  (D) while 不能印數字

### 3. 初始化錯誤
```java
int prod = 0;
for (int i = 1; i <= 5; i++) {
    prod *= i;
}
System.out.println(prod);
```
輸出為何？
(A) 0  (B) 120  (C) 15  (D) 編譯錯誤

### 4. 邊界測試
若方法 `sum(int n)` 要計算 `1+2+...+n`，當 `n=0` 時應回傳？
(A) 0  (B) 1  (C) -1  (D) 拋出例外

### 5. 追蹤 Bug
```java
int total = 0;
for (int k = 1; k < 5; k++) {
    total += k * k;
}
System.out.println(total);
```
此程式原本想計算 1²+2²+3²+4²+5² = 55，但結果不對。少了多少？
(A) 5  (B) 10  (C) 25  (D) 0

---

## 程式實作（5 分）

### FRQ：除錯修正
以下程式碼包含**兩個錯誤**，請找出並寫出修正後的完整方法。

```java
public static int factorial(int n) {
    int product = 0;
    for (int i = 1; i < n; i++) {
        product *= i;
    }
    return product;
}
```

預期行為：回傳 `n!`（n 的階乘）。例如 `factorial(5)` 應回傳 120。

> 解答請見：`answer-key.md`
