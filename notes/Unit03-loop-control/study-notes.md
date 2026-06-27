# Unit 03：迴圈控制變數與條件設計

## 學習目標
- 掌握迴圈變數的命名與作用域
- 能設計精確的起始值與終止條件
- 理解 Off-by-one Error 與複合條件的使用
- 認識浮點數在迴圈條件中的陷阱

---

## 概念說明

### Off-by-one Error（差一錯誤）
迴圈中最常見的 bug，多一次或少一次。

```java
// 問題：想印 1~10，但只印了 1~9
for (int i = 1; i < 10; i++) {   // ❌ 應用 <= 10
    System.out.println(i);
}

// 正確：
for (int i = 1; i <= 10; i++) {  // ✅
    System.out.println(i);
}
```

### 計算迴圈執行次數公式
- `for (int i = a; i <= b; i++)` → 執行 `b - a + 1` 次
- `for (int i = a; i < b; i++)` → 執行 `b - a` 次
- `for (int i = b; i >= a; i--)` → 執行 `b - a + 1` 次
- `for (int i = a; i <= b; i += step)` → 執行 `(b - a) / step + 1` 次

### 複合條件（Compound Condition）
使用 `&&`（且）與 `||`（或）組合多個條件：
```java
// 找出第一個 > 50 且能被 7 整除的數
int n = 1;
while (!(n > 50 && n % 7 == 0)) {
    n++;
}
System.out.println(n);  // 56
```

### 浮點數條件的陷阱
浮點數精度問題可能導致迴圈永不終止：
```java
// ❌ 危險：0.1 無法用二進位精確表示
double x = 0.0;
while (x != 1.0) {   // 可能無限迴圈！
    x += 0.1;
}

// ✅ 安全：改用整數計數
for (int i = 0; i <= 10; i++) {
    double x = i * 0.1;
}
```

### 迴圈變數作用域（Scope）
`for` 迴圈中宣告的變數只在迴圈內有效：
```java
for (int i = 0; i < 5; i++) { }
// System.out.println(i);  // ❌ 編譯錯誤：找不到 i

int i;
for (i = 0; i < 5; i++) { }
System.out.println(i);  // ✅ 在外部宣告即可使用
```

---

## 程式碼範例

### 範例 1：精確控制範圍（索引 2 到 7）
```java
for (int i = 2; i <= 7; i++) {
    System.out.print(i + " ");
}
// 輸出：2 3 4 5 6 7（執行 6 次）
```

### 範例 2：計算 1 到 100 總和（確認邊界）
```java
int total = 0;
for (int i = 1; i <= 100; i++) {
    total += i;
}
System.out.println(total);  // 5050
```

### 範例 3：String 長度作為終止條件
```java
String word = "hello";
for (int i = 0; i < word.length(); i++) {
    System.out.print(word.charAt(i) + " ");
}
// 輸出：h e l l o
```

### 範例 4：複合條件應用（&&）
找出 1-100 中同時能被 3 和 5 整除（即 15 的倍數）的數：
```java
for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
        System.out.print(i + " ");
    }
}
// 輸出：15 30 45 60 75 90
```

### 範例 5：boolean 旗標控制迴圈
使用 boolean 變數來控制迴圈是否繼續：
```java
int num = 2;
boolean found = false;
while (!found) {
    boolean isPrime = true;
    for (int d = 2; d < num; d++) {
        if (num % d == 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime && num > 10) {
        found = true;
    } else {
        num++;
    }
}
System.out.println("第一個大於 10 的質數：" + num);  // 11
```

### 範例 6：浮點數迴圈陷阱示範
```java
// 使用整數計數器避免精度問題
System.out.println("0.0 到 1.0 每次加 0.1：");
for (int i = 0; i <= 10; i++) {
    double val = i * 0.1;
    System.out.printf("%.1f ", val);
}
// 輸出：0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
```

---

## 條件設計技巧
- **複合條件**（`&&`、`||`）：同時滿足多項要求時使用 `&&`，滿足任一條件時使用 `||`
- **方法回傳值作為條件**：`i < s.length()`、`while (scanner.hasNextInt())`
- **boolean 旗標**：宣告 `boolean done = false`，滿足條件時設為 `true` 來跳出
- **浮點數迴圈**：永遠用整數計數，再換算為浮點數值

---

## 練習題

### Easy：計算執行次數
- (A) `for (int i = 0; i < 10; i++)`
- (B) `for (int i = 1; i <= 10; i++)`
- (C) `for (int i = 0; i < 10; i += 2)`
- (D) `for (int i = 10; i >= 1; i--)`

### Medium：FizzBuzz（1-30）
規則：3 的倍數印 "Fizz"，5 的倍數印 "Buzz"，15 的倍數印 "FizzBuzz"，否則印數字

---

## 實作練習

### Easy：找出同時能被 3 和 5 整除的數
給定 `N = 50`，使用 `for` 迴圈找出 1 到 N 之間**同時**能被 3 **和** 5 整除的數（即 15 的倍數），並輸出。

預期輸出：`15 30 45`

### Medium：計算字串中的大寫字母數
給定字串 `"Hello World! Java123"`，使用 `for` 迴圈搭配 `charAt()` 與 `length()`，
計算其中大寫字母（'A' ~ 'Z'）的個數。

提示：字元比較 `c >= 'A' && c <= 'Z'`

預期輸出：`大寫字母數量 = 3`（H, W, J）

### Hard：找出 1-100 的所有質數並計算總和
使用巢狀 `for` 迴圈找出 1 到 100 之間的所有質數，並計算這些質數的總和。

提示：
- 質數定義：大於 1 且只有 1 與自己兩個因數
- 對每個數 `n`，用內層迴圈檢查 2 到 `n-1` 是否有因數
- 使用 `break` 在找到因數時提前結束內層迴圈

預期輸出：
```
質數：2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
質數總和 = 1060
```

---

## 現在試試看
計算 1 到 50 中所有質數的個數
