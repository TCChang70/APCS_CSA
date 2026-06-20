# APCS CSA 模擬練習 — Phase 2：Iteration 進階

> **涵蓋單元：** Unit 06–10（數學計算、break/continue、除錯、方法整合、FRQ）  
> **題型：** 選擇題 (MCQ) + 程式實作題 (FRQ)  
> **總分：** 40 分 | **建議時間：** 60 分鐘

---

## 第一部分：選擇題（每題 3 分，共 24 分）

---

### 1. 累乘初始值

下列程式碼計算 5!（階乘），但結果錯誤。錯誤原因是什麼？

```java
int product = 0;
for (int i = 1; i <= 5; i++) {
    product *= i;
}
System.out.println(product);


(A) 迴圈條件錯誤  
(B) `product` 初始化錯誤  
(C) 運算子錯誤  
(D) 變數型別錯誤  
```
---

### 2. break 與 continue

執行下列程式碼後，輸出為何？

```java
for (int i = 1; i <= 10; i++) {
    if (i % 3 == 0) continue;
    if (i > 7) break;
    System.out.print(i + " ");
}

(A) 1 2 4 5 7  
(B) 1 2 4 5 7 8 10  
(C) 1 2 3 4 5 6 7  
(D) 1 2 4 5 7 8  
```
---

### 3. 迴圈錯誤識別

下列程式碼有哪些錯誤？（選出**最完整**的選項）

```java
int total = 1;
for (int k = 1; k < 10; k++) {
    total = total + k;
}
System.out.println("Sum = " + total);


(A) 只有 Off-by-one 錯誤  
(B) 只有初始化錯誤  
(C) Off-by-one 錯誤和初始化錯誤  
(D) 無限迴圈  
```
---

### 4. 方法回傳值追蹤

```java
public static int doSomething(int n) {
    int r = 0;
    while (n > 0) {
        r = r * 10 + n % 10;
        n /= 10;
    }
    return r;
}

doSomething(12345) 的回傳值為何？

(A) 12345  
(B) 54321  
(C) 15  
(D) 12345  
```
---

### 5. GCD 演算法

```java
public static int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}


gcd(54, 24) 的回傳值為何？

(A) 2  
(B) 3  
(C) 6  
(D) 12  
```
---

### 6. Fibonacci 數列

下列程式碼執行後，`sum` 的值為何？

```java
int a = 1, b = 1, sum = 0;
for (int i = 3; i <= 10; i++) {
    int c = a + b;
    if (c % 2 == 0) sum += c;
    a = b;
    b = c;
}
System.out.println(sum);

(A) 44  
(B) 88  
(C) 143  
(D) 231  
```
---

### 7. FRQ 模式識別

APCS FRQ 中，若 Part (a) 實作 `average(int[] arr)`，Part (b) 通常會如何利用 Part (a)？

(A) Part (b) 重新實作平均計算  
(B) Part (b) 直接呼叫 `average()` 來取得平均值  
(C) Part (b) 只能使用 while 迴圈  
(D) Part (b) 不使用陣列  

---

### 8. 除錯技巧
```
當迴圈發生 Off-by-one 錯誤時，最有效的除錯方法是？

(A) 刪除所有 print 語句  
(B) 檢查迴圈條件中的 `<` 與 `<=` 以及初始值  
(C) 將 `int` 改為 `double`  
(D) 將 `for` 改為 `while`  
```
---

## 第二部分：程式實作題（共 16 分）

---

### FRQ 1：完美數判斷 (8 分)

撰寫完整方法：

```java
public static boolean isPerfectNumber(int n)


一個正整數如果是「完美數」，代表它所有正因數（除了自己）的總和等於自己。

例如：
- 6 = 1 + 2 + 3（因數：1, 2, 3）→ 是完美數 → 回傳 `true`
- 28 = 1 + 2 + 4 + 7 + 14 → 是完美數 → 回傳 `true`
- 12（因數和 1+2+3+4+6=16 ≠ 12）→ 不是完美數 → 回傳 `false`

請使用迴圈找出 n 的所有因數並計算總和。
```
---

### FRQ 2：Caesar 密碼加密 (8 分)

撰寫完整方法：

```java
public static String caesarCipher(String text, int shift)


實作 Caesar 密碼加密：將字串中的每個英文字母依照 `shift` 向後位移，非英文字母保持不變。

- 'a' → shift 3 → 'd'，'z' → shift 1 → 'a'（循環）
- 大小寫各自保持（大寫位移後仍為大寫，小寫位移後仍為小寫）
- 非英文字母（空格、數字、標點符號）不變

**提示：** `char` 可以進行算術運算，`'a' + 1` → `'b'`（值為 98）

**範例：**
- `caesarCipher("abc", 3)` → "def"
- `caesarCipher("xyz", 3)` → "abc"
- `caesarCipher("Hello World!", 5)` → "Mjqqt Btwqi!"
```
---

> 解答請見：`apcs-mock/Phase2-AnswerKey.md`
