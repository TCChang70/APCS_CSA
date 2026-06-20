# Unit 01：while 迴圈基礎 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. while 迴圈執行次數
```java
int i = 5;
int count = 0;
while (i > 0) {
    count++;
    i -= 2;
}
```
執行後 `count` 的值為何？
(A) 2  (B) 3  (C) 4  (D) 5

### 2. 無限迴圈
下列哪個迴圈**不會**造成無限迴圈？
(A) `while (true) { }`
(B) `int x = 0; while (x < 10) { x--; }`
(C) `int x = 0; while (x < 10) { x++; }`
(D) `while (5 > 3) { }`

### 3. 哨兵值模式
關於哨兵值（sentinel value）模式的敘述，何者正確？
(A) 哨兵值必須是使用者不可能輸入的數值
(B) 哨兵值一定是 0
(C) 哨兵值模式只能用 while 迴圈實作
(D) 哨兵值一定要放在迴圈條件中

### 4. 程式輸出
```java
int n = 12345;
int sum = 0;
while (n > 0) {
    sum += n % 10;
    n /= 10;
}
System.out.println(sum);
```
輸出為何？
(A) 10  (B) 15  (C) 120  (D) 12345

### 5. 條件順序
```java
int i = 10;
while (i > 0) {
    if (i % 3 == 0) {
        System.out.print(i + " ");
    }
    i--;
}
```
輸出為何？
(A) 9 6 3  (B) 3 6 9  (C) 10 9 8 7 6 5 4 3 2 1  (D) 12 9 6 3

---

## 程式實作（5 分）

### FRQ：數位總和
撰寫方法使用 `while` 迴圈計算一個正整數的「數位總和」（所有位數相加）。

```java
public static int digitSum(int n)
```

**範例：**
- `digitSum(123)` → 1+2+3 = **6**
- `digitSum(9999)` → 9+9+9+9 = **36**
- `digitSum(7)` → **7**

---

> 解答請見：`answer-key.md`
