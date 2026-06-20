# Unit 02：for 迴圈基礎 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. for 迴圈語法
下列 for 迴圈的輸出為何？
```java
for (int i = 0; i < 5; i++) {
    System.out.print(i + " ");
}
```
(A) 0 1 2 3 4  (B) 1 2 3 4 5  (C) 0 1 2 3 4 5  (D) 1 2 3 4

### 2. 遞減計數
```java
for (int i = 10; i >= 0; i -= 3) {
    System.out.print(i + " ");
}
```
輸出為何？
(A) 10 7 4 1  (B) 10 7 4 1 -2  (C) 10 7 4  (D) 10 8 6 4 2 0

### 3. for 迴圈執行次數
```java
for (int i = 0; i <= 10; i += 2) {
    System.out.println(i);
}
```
此迴圈執行幾次？
(A) 4  (B) 5  (C) 6  (D) 10

### 4. for vs while
下列哪個 for 迴圈與以下 while 迴圈**不等價**？
```java
int i = 0;
while (i < 10) {
    System.out.println(i);
    i++;
}
(A) for (int i = 0; i < 10; i++) { System.out.println(i); }
(B) for (int i = 0; i <= 9; i++) { System.out.println(i); }
(C) for (int i = 1; i <= 10; i++) { System.out.println(i); }
(D) for (int i = 0; i < 10; ++i) { System.out.println(i); }

```
### 5. 變數作用域
```java
for (int i = 0; i < 5; i++) {
    int x = i * 2;
}
System.out.println(x);  // 此行結果為何？
```
(A) 輸出 8  (B) 輸出 10  (C) 編譯錯誤  (D) 輸出 0

---

## 程式實作（5 分）

### FRQ：累加公式
撰寫方法，使用 `for` 迴圈計算 `1² - 2² + 3² - 4² + ... ± n²`（n 為正整數，正負號交替）。

```java
public static int alternatingSquareSum(int n)
```

**範例：**
- `alternatingSquareSum(4)` → 1² - 2² + 3² - 4² = 1 - 4 + 9 - 16 = **-10**
- `alternatingSquareSum(5)` → 1² - 2² + 3² - 4² + 5² = 1 - 4 + 9 - 16 + 25 = **15**

> 解答請見：`answer-key.md`
