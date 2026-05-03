# APCS CSA — Iteration & Array 完整學習路線圖

> **語言：** Java｜**主題：** Unit 4 Iteration + Unit 6  Array  
> **總學習單元：** 20 單元｜**每單元時間：** 1.5 小時｜**總計：** 30 小時

---

## 路線圖總覽

```
Phase 1：Iteration 基礎      Unit 01 ~ 05   (7.5 小時)
Phase 2：Iteration 進階      Unit 06 ~ 10   (7.5 小時)
Phase 3：Array 基礎          Unit 11 ~ 15   (7.5 小時)
Phase 4：Array 進階 + 2D     Unit 16 ~ 20   (7.5 小時)
```

| 階段 | 主題 | 里程碑 |
|------|------|--------|
| Phase 1 | while / for / 巢狀迴圈 | 能用迴圈解決累加、計數、字串處理 |
| Phase 2 | break/continue、常見錯誤、FRQ | 能獨立解出 Iteration 類 FRQ |
| Phase 3 | Array 宣告、遍歷、基礎演算法 | 能操作一維陣列完成搜尋與統計 |
| Phase 4 | 排序、2D Array、綜合 FRQ | 能解出 Array + 2D Array 類 FRQ |

---

## Phase 1 — Iteration 基礎

---

### Unit 01：`while` 迴圈基礎

> **預估時間：** 1.5 小時｜**難度：** ⭐☆☆☆☆

#### 學習目標
- 理解 `while` 迴圈的執行流程（Entry Condition）
- 能正確設定迴圈條件與終止條件
- 辨別無限迴圈（Infinite Loop）並修正

#### 概念說明

`while` 迴圈（while loop）在**條件為 true** 時持續執行，每次執行前先檢查條件。

```
while (條件) {
    // 重複執行的程式碼
}
```

執行流程：
1. 檢查條件 → 若 false 則跳出
2. 執行迴圈主體
3. 回到步驟 1

#### 程式碼範例

```java
// 範例 1：從 1 數到 5
int i = 1;
while (i <= 5) {
    System.out.println(i);
    i++;  // 更新變數，避免無限迴圈
}
// 輸出：1 2 3 4 5

// 範例 2：計算 1 + 2 + ... + 10
int sum = 0;
int n = 1;
while (n <= 10) {
    sum += n;
    n++;
}
System.out.println("總和 = " + sum);  // 總和 = 55

// 範例 3：使用者輸入直到輸入 0（常見情境）
// int num = scanner.nextInt();
// while (num != 0) {
//     System.out.println("輸入了：" + num);
//     num = scanner.nextInt();
// }
```

#### 練習題

---

**練習題 1：倒數計時**
**難度：** Easy｜**主題：** while 基礎

**題目說明**  
從 10 倒數到 1，每個數字各佔一行，最後印出 `"Go!"`

**輸出範例**
```
10
9
8
...
1
Go!
```

<details>
<summary>顯示解答</summary>

```java
int count = 10;
while (count >= 1) {
    System.out.println(count);
    count--;
}
System.out.println("Go!");
```

**說明：** 起始值 10，條件 `count >= 1`，每次遞減 1，迴圈結束後印出 "Go!"
</details>

---

**練習題 2：找出第一個能被 7 整除的數**
**難度：** Medium｜**主題：** while + 條件

**題目說明**  
從 1 開始，找出第一個同時滿足「大於 50 且能被 7 整除」的整數並印出。

**輸出範例**
```
56
```

<details>
<summary>顯示解答</summary>

```java
int n = 1;
while (!(n > 50 && n % 7 == 0)) {
    n++;
}
System.out.println(n);  // 56
```
</details>

---

#### 常見錯誤

| 錯誤類型 | 錯誤範例 | 說明 |
|---------|---------|------|
| 無限迴圈 | `while (i < 10)` 但忘記 `i++` | 條件永遠為 true |
| Off-by-one | `while (i < 10)` vs `while (i <= 10)` | 差一個數 |
| 條件寫反 | `while (i = 10)` | 應用 `==`，`=` 是賦值 |

#### 現在試試看
> 修改範例 2，改為計算 1 到 100 中所有奇數的總和。

---

### Unit 02：`for` 迴圈基礎

> **預估時間：** 1.5 小時｜**難度：** ⭐☆☆☆☆

#### 學習目標
- 理解 `for` 迴圈的三段結構
- 能與 `while` 迴圈互相轉換
- 掌握迴圈計數的各種方向（遞增、遞減、步進）

#### 概念說明

`for` 迴圈（for loop）將**初始化、條件、更新**整合在一行，適合已知次數的迴圈。

```java
for (初始化; 條件; 更新) {
    // 迴圈主體
}
```

三段對應：
- **初始化** (`int i = 0`)：執行一次，設定起始值
- **條件** (`i < 10`)：每次迴圈前檢查
- **更新** (`i++`)：每次迴圈結束後執行

#### 程式碼範例

```java
// 範例 1：基本計數（遞增）
for (int i = 1; i <= 5; i++) {
    System.out.print(i + " ");
}
// 輸出：1 2 3 4 5

// 範例 2：遞減計數
for (int i = 5; i >= 1; i--) {
    System.out.print(i + " ");
}
// 輸出：5 4 3 2 1

// 範例 3：步進 2
for (int i = 0; i <= 10; i += 2) {
    System.out.print(i + " ");
}
// 輸出：0 2 4 6 8 10

// 範例 4：計算乘法表
for (int i = 1; i <= 9; i++) {
    System.out.println("7 x " + i + " = " + (7 * i));
}
```

#### `for` vs `while` 對照

```java
// for 寫法
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// 等價的 while 寫法
int i = 0;
while (i < 5) {
    System.out.println(i);
    i++;
}
```

#### 練習題

---

**練習題 1：印出偶數**
**難度：** Easy｜**主題：** for 基礎

**題目說明**  
使用 `for` 迴圈，印出 1 到 20 之間（含）所有偶數，每個數字以空格分隔。

**輸出範例**
```
2 4 6 8 10 12 14 16 18 20
```

<details>
<summary>顯示解答</summary>

```java
for (int i = 2; i <= 20; i += 2) {
    System.out.print(i + " ");
}
```
</details>

---

**練習題 2：星號三角形**
**難度：** Medium｜**主題：** for + String 重複

**題目說明**  
印出以下圖形（5 行）：

```
*
**
***
****
*****
```

<details>
<summary>顯示解答</summary>

```java
for (int i = 1; i <= 5; i++) {
    for (int j = 0; j < i; j++) {
        System.out.print("*");
    }
    System.out.println();
}
```

**說明：** 外層迴圈控制行數，內層迴圈控制每行星號數量。
</details>

---

#### 常見錯誤

| 錯誤 | 範例 | 正確 |
|------|------|------|
| 分號錯誤 | `for (int i=0, i<5, i++)` | 用分號 `;` 分隔 |
| 變數作用域 | 在迴圈外使用 `i` | `i` 只在 for 迴圈內有效 |
| 無窮迴圈 | `for (int i=0; i<5; i--)` | 更新方向要與條件一致 |

#### 現在試試看
> 印出 1 到 100 中所有能被 3 整除的數，統計共有幾個。

---

### Unit 03：迴圈控制變數與條件設計

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐☆☆☆

#### 學習目標
- 掌握迴圈變數（loop variable）的命名與作用域
- 能設計精確的起始值與終止條件
- 理解常見的 off-by-one error（差一錯誤）

#### 概念說明

**Off-by-one Error（差一錯誤）** 是迴圈中最常見的 bug。

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

**計算迴圈執行次數公式：**
- `for (int i = a; i <= b; i++)` → 執行 `b - a + 1` 次
- `for (int i = a; i < b; i++)` → 執行 `b - a` 次

#### 程式碼範例

```java
// 範例 1：精確控制範圍
// 問題：印出索引 2 到 7（共 6 個數）
for (int i = 2; i <= 7; i++) {
    System.out.print(i + " ");
}
// 輸出：2 3 4 5 6 7（執行 7-2+1 = 6 次）

// 範例 2：計算某範圍的總和
int total = 0;
for (int i = 1; i <= 100; i++) {
    total += i;
}
System.out.println(total);  // 5050

// 範例 3：條件中使用方法
String word = "hello";
for (int i = 0; i < word.length(); i++) {  // length() 決定次數
    System.out.print(word.charAt(i) + " ");
}
// 輸出：h e l l o
```

#### 練習題

---

**練習題 1：計算執行次數**
**難度：** Easy｜**主題：** 迴圈次數分析

**題目說明**  
以下迴圈各執行幾次？不執行程式，直接計算。
```java
// (A) for (int i = 0; i < 10; i++)
// (B) for (int i = 1; i <= 10; i++)
// (C) for (int i = 0; i < 10; i += 2)
// (D) for (int i = 10; i >= 1; i--)
```

<details>
<summary>顯示解答</summary>

- (A) 10 次（0,1,...,9）
- (B) 10 次（1,2,...,10）
- (C) 5 次（0,2,4,6,8）
- (D) 10 次（10,9,...,1）
</details>

---

**練習題 2：FizzBuzz**
**難度：** Medium｜**主題：** for + 條件判斷

**題目說明**  
印出 1 到 30，規則：
- 能被 3 整除 → 印 `Fizz`
- 能被 5 整除 → 印 `Buzz`
- 能被 15 整除 → 印 `FizzBuzz`
- 否則印數字

<details>
<summary>顯示解答</summary>

```java
for (int i = 1; i <= 30; i++) {
    if (i % 15 == 0) {
        System.out.println("FizzBuzz");
    } else if (i % 3 == 0) {
        System.out.println("Fizz");
    } else if (i % 5 == 0) {
        System.out.println("Buzz");
    } else {
        System.out.println(i);
    }
}
```

**重點：** 必須先檢查 15，否則被 15 整除的數會被 3 或 5 先截走。
</details>

---

#### 常見錯誤

- `i < n` vs `i <= n`：差一個數，最常見錯誤
- 在迴圈內修改控制變數：`i` 在迴圈體內被改動會造成非預期行為
- 條件使用浮點數比較：`double i = 0; i != 1.0` 可能因精度問題造成無限迴圈

#### 現在試試看
> 計算 1 到 n 中，所有質數的個數（n 自行定義為 50）。

---

### Unit 04：巢狀迴圈（Nested Loops）

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐☆☆

#### 學習目標
- 理解巢狀迴圈（nested loop）的執行順序
- 能追蹤每次外/內層迴圈的變數值
- 應用巢狀迴圈印出二維圖形

#### 概念說明

**巢狀迴圈** = 迴圈裡面還有迴圈。外層每執行一次，內層完整執行一輪。

```java
for (外層初始; 外層條件; 外層更新) {
    for (內層初始; 內層條件; 內層更新) {
        // 最內部的程式碼
    }
}
```

**總執行次數 = 外層次數 × 內層次數**

#### 程式碼範例

```java
// 範例 1：追蹤執行順序
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        System.out.println("i=" + i + ", j=" + j);
    }
}
// 輸出：
// i=1, j=1 → i=1, j=2 → i=1, j=3
// i=2, j=1 → i=2, j=2 → i=2, j=3
// i=3, j=1 → i=3, j=2 → i=3, j=3（共 9 次）

// 範例 2：乘法表
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= 9; j++) {
        System.out.printf("%4d", i * j);
    }
    System.out.println();
}

// 範例 3：矩形圖案（4 行 6 列）
for (int row = 0; row < 4; row++) {
    for (int col = 0; col < 6; col++) {
        System.out.print("* ");
    }
    System.out.println();
}
```

#### 練習題

---

**練習題 1：追蹤執行次數**
**難度：** Easy｜**主題：** 巢狀迴圈分析

**題目說明**  
下面的巢狀迴圈，`count` 最後的值是多少？
```java
int count = 0;
for (int i = 0; i < 4; i++) {
    for (int j = 0; j < i; j++) {
        count++;
    }
}
System.out.println(count);
```

<details>
<summary>顯示解答</summary>

```
i=0：內層執行 0 次
i=1：內層執行 1 次
i=2：內層執行 2 次
i=3：內層執行 3 次
count = 0 + 1 + 2 + 3 = 6
```
</details>

---

**練習題 2：直角三角形**
**難度：** Medium｜**主題：** 巢狀迴圈 + 圖形

**題目說明**  
使用巢狀迴圈印出（n=5）：
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

<details>
<summary>顯示解答</summary>

```java
int n = 5;
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        System.out.print(j + " ");
    }
    System.out.println();
}
```
</details>

---

**練習題 3：質數篩選**
**難度：** Hard｜**主題：** 巢狀迴圈 + 邏輯

**題目說明**  
印出 2 到 50 之間所有質數。

<details>
<summary>顯示解答</summary>

```java
for (int n = 2; n <= 50; n++) {
    boolean isPrime = true;
    for (int d = 2; d < n; d++) {
        if (n % d == 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        System.out.print(n + " ");
    }
}
// 輸出：2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```
</details>

---

#### 常見錯誤

- 內外層變數名稱衝突：都用 `i`，內層會遮蔽外層
- 誤解執行順序：外層先走完再換下一輪（錯誤），實際是外層一次內層一圈
- 效能：n=1000 的三層巢狀迴圈 = 10 億次，要注意效能

#### 現在試試看
> 印出九九乘法表，每行格式為 `1x1=1 1x2=2 ...`

---

### Unit 05：String 字串遍歷（String Traversal）

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐☆☆☆

#### 學習目標
- 使用迴圈逐一存取字串的每個字元（character）
- 掌握 `charAt()`、`length()` 的用法
- 能進行字串搜尋、統計、反轉等操作

#### 概念說明

字串（String）可以透過索引（index）存取每個字元，索引從 **0** 開始。

```java
String s = "Hello";
// 索引：  0 1 2 3 4
// 字元：  H e l l o
s.length()   // 5（字串長度）
s.charAt(0)  // 'H'
s.charAt(4)  // 'o'
```

#### 程式碼範例

```java
// 範例 1：印出每個字元
String s = "Java";
for (int i = 0; i < s.length(); i++) {
    System.out.println(s.charAt(i));
}
// 輸出：J a v a（每行一個）

// 範例 2：統計某字元出現次數
String text = "banana";
int count = 0;
for (int i = 0; i < text.length(); i++) {
    if (text.charAt(i) == 'a') {
        count++;
    }
}
System.out.println("a 出現 " + count + " 次");  // 3 次

// 範例 3：反轉字串
String original = "Hello";
String reversed = "";
for (int i = original.length() - 1; i >= 0; i--) {
    reversed += original.charAt(i);
}
System.out.println(reversed);  // olleH

// 範例 4：判斷是否為回文（Palindrome）
String word = "racecar";
boolean isPalindrome = true;
for (int i = 0; i < word.length() / 2; i++) {
    if (word.charAt(i) != word.charAt(word.length() - 1 - i)) {
        isPalindrome = false;
    }
}
System.out.println(isPalindrome);  // true
```

#### 練習題

---

**練習題 1：統計大寫字母**
**難度：** Easy｜**主題：** charAt + 條件

**題目說明**  
給定字串 `"Hello World APCS"`，統計大寫字母（A-Z）的個數。

**輸出：** `5`

<details>
<summary>顯示解答</summary>

```java
String s = "Hello World APCS";
int count = 0;
for (int i = 0; i < s.length(); i++) {
    char c = s.charAt(i);
    if (c >= 'A' && c <= 'Z') {
        count++;
    }
}
System.out.println(count);  // 5 (H, W, A, P, C, S → 6)
```

**說明：** 用字元比較（`char` 可以用 `>=` 比較 ASCII 值）。`H, W, A, P, C, S` = 6 個大寫。
</details>

---

**練習題 2：刪除母音**
**難度：** Medium｜**主題：** 字串建構 + charAt

**題目說明**  
給定字串，回傳移除所有母音（a, e, i, o, u，大小寫均算）後的字串。
- 輸入：`"Hello World"`
- 輸出：`"Hll Wrld"`

<details>
<summary>顯示解答</summary>

```java
String s = "Hello World";
String result = "";
String vowels = "aeiouAEIOU";
for (int i = 0; i < s.length(); i++) {
    if (vowels.indexOf(s.charAt(i)) == -1) {
        result += s.charAt(i);
    }
}
System.out.println(result);  // Hll Wrld
```
</details>

---

#### 常見錯誤

| 錯誤 | 說明 |
|------|------|
| `s.length()` vs `s.length` | String 用 `length()`（有括號），Array 用 `length`（無括號）|
| 索引越界 | `s.charAt(s.length())` → StringIndexOutOfBoundsException |
| `==` 比較字元 | `charAt()` 回傳 `char`，比較用 `==` 是正確的（`char` 是基本型別）|

#### 現在試試看
> 撰寫一個方法判斷字串是否為回文（只考慮英文字母，忽略大小寫）。

---

## Phase 2 — Iteration 進階

---

### Unit 06：迴圈與數學計算

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐☆☆☆

#### 學習目標
- 使用迴圈計算累加、累乘、平均
- 理解 running total / running product 模式
- 能結合 `Math` 類別方法

#### 程式碼範例

```java
// 範例 1：累加（Running Total）
int sum = 0;
for (int i = 1; i <= 100; i++) {
    sum += i;
}
System.out.println("Sum = " + sum);  // 5050

// 範例 2：累乘（Factorial 階乘）
int n = 10;
long factorial = 1;
for (int i = 1; i <= n; i++) {
    factorial *= i;
}
System.out.println(n + "! = " + factorial);  // 3628800

// 範例 3：平均值
int[] data = {85, 90, 78, 92, 88};
double total = 0;
for (int i = 0; i < data.length; i++) {
    total += data[i];
}
double avg = total / data.length;
System.out.printf("平均：%.2f%n", avg);

// 範例 4：最大公因數（GCD）using while
int a = 48, b = 18;
while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
}
System.out.println("GCD = " + a);  // 6
```

#### 練習題

---

**練習題 1：計算次方**
**難度：** Easy｜**主題：** 累乘

計算 `base^exp`（不使用 `Math.pow()`），base=3, exp=5。

<details>
<summary>顯示解答</summary>

```java
int base = 3, exp = 5;
int result = 1;
for (int i = 0; i < exp; i++) {
    result *= base;
}
System.out.println(result);  // 243
```
</details>

---

**練習題 2：Fibonacci 數列**
**難度：** Medium｜**主題：** 迴圈 + 前兩值追蹤

印出 Fibonacci 數列前 15 項（1, 1, 2, 3, 5, 8, 13, ...）。

<details>
<summary>顯示解答</summary>

```java
int a = 1, b = 1;
System.out.print(a + " " + b + " ");
for (int i = 3; i <= 15; i++) {
    int c = a + b;
    System.out.print(c + " ");
    a = b;
    b = c;
}
```
</details>

---

#### 現在試試看
> 計算 1² + 2² + 3² + ... + n² 的總和（n=20）。

---

### Unit 07：`break` 與 `continue`

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐☆☆

#### 學習目標
- 理解 `break` 立即跳出迴圈的效果
- 理解 `continue` 跳過當次迭代的效果
- 辨別兩者在巢狀迴圈中的行為（只影響最內層）

#### 概念說明

```java
// break：遇到條件立即離開迴圈
for (int i = 0; i < 10; i++) {
    if (i == 5) break;  // i=5 時離開
    System.out.print(i + " ");
}
// 輸出：0 1 2 3 4

// continue：跳過這次，繼續下一次
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) continue;  // 跳過偶數
    System.out.print(i + " ");
}
// 輸出：1 3 5 7 9
```

#### 程式碼範例

```java
// 範例 1：搜尋第一個負數
int[] nums = {4, 7, -2, 9, -5, 3};
int firstNeg = -1;
for (int i = 0; i < nums.length; i++) {
    if (nums[i] < 0) {
        firstNeg = nums[i];
        break;  // 找到後立即停止
    }
}
System.out.println("第一個負數：" + firstNeg);  // -2

// 範例 2：印出非空白字元（continue 應用）
String s = "A B C D";
for (int i = 0; i < s.length(); i++) {
    if (s.charAt(i) == ' ') continue;
    System.out.print(s.charAt(i));
}
// 輸出：ABCD

// 範例 3：break 在巢狀迴圈（只跳出內層）
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (j == 1) break;  // 只跳出內層 for
        System.out.println("i=" + i + " j=" + j);
    }
}
```

#### 練習題

---

**練習題 1：找到第一個能被 13 整除的數**
**難度：** Easy｜**主題：** break

在 1 到 1000 中找到第一個能被 13 整除且大於 100 的數。

<details>
<summary>顯示解答</summary>

```java
for (int i = 101; i <= 1000; i++) {
    if (i % 13 == 0) {
        System.out.println(i);
        break;
    }
}
// 輸出：104
```
</details>

---

**練習題 2：印出非重複字元**
**難度：** Hard｜**主題：** continue + 巢狀邏輯

給定字串 `"abcabc"`，印出每個字元第一次出現的位置（跳過重複的）。

<details>
<summary>顯示解答</summary>

```java
String s = "abcabc";
for (int i = 0; i < s.length(); i++) {
    boolean seen = false;
    for (int j = 0; j < i; j++) {
        if (s.charAt(j) == s.charAt(i)) {
            seen = true;
            break;
        }
    }
    if (seen) continue;
    System.out.println("'" + s.charAt(i) + "' 首次出現在索引 " + i);
}
```
</details>

---

#### 現在試試看
> 使用 `break` 改進質數判斷程式（找到因數後立即停止）。

---

### Unit 08：常見迴圈錯誤與除錯技巧

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐☆☆

#### 學習目標
- 識別並修正 5 種常見迴圈錯誤
- 使用 `System.out.println()` 追蹤迴圈狀態
- 理解 APCS CSA 考試中常見的迴圈陷阱題

#### 5 大常見迴圈錯誤

| 錯誤類型 | 說明 | 修正方式 |
|---------|------|---------|
| Off-by-one | 多一次或少一次 | 仔細確認 `<` 或 `<=` |
| 無限迴圈 | 條件永遠為 true | 確認更新邏輯 |
| 變數初始化錯誤 | 累計變數從錯誤的值開始 | 累加從 0，累乘從 1 |
| 作用域問題 | 迴圈外存取 `i` | 在迴圈外宣告需要保留的值 |
| 意外覆蓋 | 在迴圈內重複宣告變數 | 避免在迴圈內宣告累計變數 |

#### 程式碼範例（錯誤分析）

```java
// 錯誤 1：Off-by-one（計算 1~n 總和）
int n = 10;
int sum = 0;
for (int i = 1; i < n; i++) {  // ❌ 少算了 n=10
    sum += i;
}
// 修正：i <= n

// 錯誤 2：累計變數初始化錯誤
int product = 0;  // ❌ 應初始化為 1
for (int i = 1; i <= 5; i++) {
    product *= i;
}
// 結果永遠是 0！修正：product = 1

// 錯誤 3：無限迴圈
int i = 0;
while (i < 10) {
    System.out.println(i);
    // ❌ 忘記寫 i++
}

// 錯誤 4：迴圈後還想用控制變數
for (int j = 0; j < 10; j++) { ... }
System.out.println(j);  // ❌ j 已超出作用域

// 修正：在迴圈外宣告
int j;
for (j = 0; j < 10; j++) { ... }
System.out.println(j);  // ✅ j = 10
```

#### 除錯技巧

```java
// 技巧：在關鍵位置加入 debug 輸出
for (int i = 0; i < 5; i++) {
    System.out.println("DEBUG: i = " + i + ", sum = " + sum);
    sum += i;
}
```

#### 練習題：找出 Bug

```java
// 練習：以下程式碼有哪些錯誤？
int total = 1;
for (int k = 1; k < 10; k++) {
    total = total + k;
}
System.out.println("1 to 10 sum = " + total);
```

<details>
<summary>顯示解答</summary>

**兩個錯誤：**
1. `total = 1`：應初始化為 `0`（會多算 1）
2. `k < 10`：應為 `k <= 10`（少算了 10）

**正確版本：**
```java
int total = 0;
for (int k = 1; k <= 10; k++) {
    total += k;
}
System.out.println("Sum = " + total);  // 55
```
</details>

---

### Unit 09：迴圈與方法（Methods）整合

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐☆☆

#### 學習目標
- 將迴圈邏輯封裝進方法（method）
- 理解方法回傳值與迴圈的配合
- 能分析含有方法呼叫的迴圈程式碼

#### 程式碼範例

```java
// 範例 1：封裝計算方法
public static int sum(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
        total += i;
    }
    return total;
}

// 使用：
System.out.println(sum(10));   // 55
System.out.println(sum(100));  // 5050

// 範例 2：在迴圈中呼叫方法
public static boolean isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

// 主程式中呼叫：
for (int i = 2; i <= 30; i++) {
    if (isPrime(i)) {
        System.out.print(i + " ");
    }
}

// 範例 3：String 處理方法
public static int countVowels(String s) {
    int count = 0;
    String vowels = "aeiouAEIOU";
    for (int i = 0; i < s.length(); i++) {
        if (vowels.indexOf(s.charAt(i)) >= 0) {
            count++;
        }
    }
    return count;
}
```

#### 練習題

---

**練習題 1：實作 `max` 方法**
**難度：** Medium

撰寫方法 `public static int max(int a, int b, int c)` 回傳三個數中最大值，不使用 `Math.max()`。

<details>
<summary>顯示解答</summary>

```java
public static int max(int a, int b, int c) {
    int m = a;
    if (b > m) m = b;
    if (c > m) m = c;
    return m;
}
```
</details>

---

**練習題 2：數字反轉**
**難度：** Hard

撰寫方法接受整數，回傳數字反轉後的值。
- 輸入：`12345` → 輸出：`54321`

<details>
<summary>顯示解答</summary>

```java
public static int reverse(int n) {
    int result = 0;
    while (n != 0) {
        result = result * 10 + n % 10;
        n /= 10;
    }
    return result;
}
System.out.println(reverse(12345));  // 54321
```
</details>

---

### Unit 10：Iteration 綜合練習與 FRQ 準備

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐⭐☆

#### 學習目標
- 整合 Unit 1-9 的所有迴圈技巧
- 練習 APCS CSA FRQ 格式的回答
- 掌握迴圈在 FRQ 中的常見應用模式

#### APCS CSA FRQ 常見迴圈模式

| 模式 | 說明 | 關鍵技巧 |
|------|------|---------|
| 累加/計數 | Running total, count | 初始化在迴圈外 |
| 搜尋 | 找第一個/最後一個 | `break` 或 flag 變數 |
| 遍歷 | 處理每個元素 | `for (int i=0; i<n; i++)` |
| 字串處理 | 逐字元操作 | `charAt()` + `length()` |
| 巢狀 | 二維資料或比較 | 內外層變數區分 |

#### FRQ 練習題

---

**FRQ 練習：密碼驗證方法**
**難度：** Hard

撰寫方法 `public static boolean isValidPassword(String password)`，驗證密碼必須：
1. 長度至少 8 個字元
2. 包含至少一個大寫字母（A-Z）
3. 包含至少一個數字（0-9）

```java
// 完整回答：
public static boolean isValidPassword(String password) {
    if (password.length() < 8) return false;
    
    boolean hasUpper = false;
    boolean hasDigit = false;
    
    for (int i = 0; i < password.length(); i++) {
        char c = password.charAt(i);
        if (c >= 'A' && c <= 'Z') hasUpper = true;
        if (c >= '0' && c <= '9') hasDigit = true;
    }
    
    return hasUpper && hasDigit;
}
```

---

#### Phase 1 & 2 里程碑自我檢查

- [ ] 能不看筆記寫出 `while` 和 `for` 迴圈
- [ ] 能計算任意 `for` 迴圈的執行次數
- [ ] 能追蹤巢狀迴圈的變數值
- [ ] 能用迴圈處理 `String` 的每個字元
- [ ] 能正確使用 `break` 和 `continue`
- [ ] 能識別並修正常見的迴圈 bug

---

## Phase 3 — Array 基礎

---

### Unit 11：Array 宣告與初始化

> **預估時間：** 1.5 小時｜**難度：** ⭐☆☆☆☆

#### 學習目標
- 理解陣列（Array）的概念：連續記憶體、固定大小、同型別
- 掌握三種宣告與初始化方式
- 理解 `length` 屬性與預設值

#### 概念說明

陣列（Array）是**相同型別**元素的**固定大小**有序集合，索引從 **0** 開始。

```
int[] scores = new int[5];
索引：           0    1    2    3    4
值：             0    0    0    0    0  （預設值）
```

#### 三種初始化方式

```java
// 方式 1：只宣告大小（元素使用預設值）
int[] nums = new int[5];
// int 預設值 = 0, boolean = false, double = 0.0, String/Object = null

// 方式 2：宣告並指定初始值（initializer list）
int[] scores = {85, 90, 78, 92, 88};
// 大小自動為 5

// 方式 3：宣告變數後再初始化
int[] data;
data = new int[]{10, 20, 30};

// 取得長度
System.out.println(scores.length);  // 5（注意：不是 length()）

// 存取元素
System.out.println(scores[0]);  // 85（第一個）
System.out.println(scores[4]);  // 88（最後一個）
```

#### 程式碼範例

```java
// 範例：建立並修改陣列
String[] fruits = {"apple", "banana", "cherry"};
System.out.println(fruits[1]);  // banana

fruits[1] = "blueberry";  // 修改索引 1
System.out.println(fruits[1]);  // blueberry

// 最後一個元素的通用寫法
System.out.println(fruits[fruits.length - 1]);  // cherry
```

#### 練習題

---

**練習題 1：陣列基本操作**
**難度：** Easy

建立整數陣列 `{10, 20, 30, 40, 50}`，印出第一個元素、最後一個元素及陣列長度。

<details>
<summary>顯示解答</summary>

```java
int[] arr = {10, 20, 30, 40, 50};
System.out.println("第一個：" + arr[0]);              // 10
System.out.println("最後一個：" + arr[arr.length-1]); // 50
System.out.println("長度：" + arr.length);            // 5
```
</details>

---

**練習題 2：填入偶數**
**難度：** Easy

建立大小為 5 的整數陣列，用迴圈填入 2, 4, 6, 8, 10，然後印出所有元素。

<details>
<summary>顯示解答</summary>

```java
int[] evens = new int[5];
for (int i = 0; i < evens.length; i++) {
    evens[i] = (i + 1) * 2;
}
for (int i = 0; i < evens.length; i++) {
    System.out.print(evens[i] + " ");
}
```
</details>

---

#### 常見錯誤

| 錯誤 | 說明 |
|------|------|
| `arr.length()` | 陣列用 `length`（屬性），不是 `length()` 方法 |
| `arr[arr.length]` | 超出索引，最後一個是 `arr[arr.length - 1]` |
| 宣告後未初始化就存取 | 編譯錯誤（NullPointerException）|
| 混淆陣列大小與最大索引 | 大小 n → 索引 0 ~ n-1 |

#### 現在試試看
> 建立一個陣列儲存你的 5 門課成績，印出每門成績及其索引。

---

### Unit 12：Array 元素存取與修改

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐☆☆☆

#### 學習目標
- 正確讀取與修改陣列元素
- 理解 `ArrayIndexOutOfBoundsException`
- 能在方法中操作陣列（陣列是 reference type）

#### 概念說明

陣列是**參考型別（Reference Type）**，傳入方法時傳的是參考（記憶體位址），方法內修改會影響原始陣列。

```java
// 值型別 vs 參考型別
int x = 5;
modifyInt(x);  // x 不會被改變（傳值）

int[] arr = {1, 2, 3};
modifyArray(arr);  // arr 內容會被改變！（傳參考）
```

#### 程式碼範例

```java
// 範例 1：存取與修改
int[] nums = {5, 10, 15, 20, 25};
nums[2] = 99;  // 修改索引 2
System.out.println(nums[2]);  // 99

// 範例 2：條件修改（將負數改為 0）
int[] data = {3, -1, 7, -4, 0, -2};
for (int i = 0; i < data.length; i++) {
    if (data[i] < 0) {
        data[i] = 0;
    }
}
// data = {3, 0, 7, 0, 0, 0}

// 範例 3：陣列是參考型別（傳入方法後修改）
public static void doubleAll(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        arr[i] *= 2;
    }
}

int[] scores = {10, 20, 30};
doubleAll(scores);
System.out.println(scores[0]);  // 20（已被修改！）
```

#### 練習題

---

**練習題 1：交換首尾元素**
**難度：** Easy

撰寫方法將陣列第一個和最後一個元素交換。
- 輸入：`{1, 2, 3, 4, 5}` → 輸出：`{5, 2, 3, 4, 1}`

<details>
<summary>顯示解答</summary>

```java
public static void swapEnds(int[] arr) {
    int temp = arr[0];
    arr[0] = arr[arr.length - 1];
    arr[arr.length - 1] = temp;
}
```
</details>

---

**練習題 2：將所有元素加上指定偏移量**
**難度：** Medium

撰寫方法接受陣列和偏移量 `offset`，將每個元素加上 `offset`（就地修改）。

<details>
<summary>顯示解答</summary>

```java
public static void addOffset(int[] arr, int offset) {
    for (int i = 0; i < arr.length; i++) {
        arr[i] += offset;
    }
}
```
</details>

---

#### 現在試試看
> 撰寫方法 `reverse(int[] arr)` 原地反轉陣列（不建立新陣列）。

---

### Unit 13：Array 遍歷 — 標準 `for` 迴圈

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐☆☆☆

#### 學習目標
- 使用標準 `for` 迴圈遍歷陣列
- 掌握累加、計數、搜尋等遍歷模式
- 能用索引進行相鄰元素比較

#### 遍歷模式

```java
// 基本遍歷模式
for (int i = 0; i < arr.length; i++) {
    // 使用 arr[i]
}
```

#### 程式碼範例

```java
int[] scores = {85, 90, 78, 92, 88, 76, 95};

// 模式 1：印出所有元素
for (int i = 0; i < scores.length; i++) {
    System.out.println("scores[" + i + "] = " + scores[i]);
}

// 模式 2：計算總和與平均
int sum = 0;
for (int i = 0; i < scores.length; i++) {
    sum += scores[i];
}
double avg = (double) sum / scores.length;
System.out.printf("平均：%.2f%n", avg);

// 模式 3：找最大值
int max = scores[0];  // 初始化為第一個元素
for (int i = 1; i < scores.length; i++) {  // 從索引 1 開始
    if (scores[i] > max) {
        max = scores[i];
    }
}
System.out.println("最高分：" + max);  // 95

// 模式 4：計數（幾個及格）
int passCount = 0;
for (int i = 0; i < scores.length; i++) {
    if (scores[i] >= 80) {
        passCount++;
    }
}
System.out.println("80 分以上：" + passCount + " 人");
```

#### 練習題

---

**練習題 1：找最小值**
**難度：** Easy

撰寫方法 `public static int min(int[] arr)` 回傳陣列中最小值。

<details>
<summary>顯示解答</summary>

```java
public static int min(int[] arr) {
    int min = arr[0];
    for (int i = 1; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}
```
</details>

---

**練習題 2：判斷是否有重複**
**難度：** Hard

撰寫方法 `public static boolean hasDuplicate(int[] arr)` 判斷陣列中是否有重複值。

<details>
<summary>顯示解答</summary>

```java
public static boolean hasDuplicate(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        for (int j = i + 1; j < arr.length; j++) {
            if (arr[i] == arr[j]) return true;
        }
    }
    return false;
}
```
</details>

---

#### 現在試試看
> 找出陣列中最大值的**索引**（不是值本身），若有多個最大值回傳第一個的索引。

---

### Unit 14：Array 遍歷 — 增強式 `for` 迴圈（for-each）

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐☆☆☆

#### 學習目標
- 掌握增強式 for 迴圈（enhanced for loop / for-each）
- 理解 for-each 的使用限制
- 能判斷何時用 for-each，何時用標準 for

#### 概念說明

**增強式 for 迴圈**（Enhanced For Loop）語法更簡潔，適合**唯讀遍歷**。

```java
for (型別 變數 : 陣列) {
    // 使用 變數
}
```

#### for-each vs 標準 for

| 比較項目 | 標準 for | for-each |
|---------|---------|---------|
| 使用索引 | ✅ 可以 | ❌ 無法取得索引 |
| 修改元素 | ✅ 可以（`arr[i]=`）| ❌ 修改變數不影響陣列 |
| 語法 | 較複雜 | 較簡潔 |
| 適用場景 | 需要索引/修改元素 | 純讀取遍歷 |

#### 程式碼範例

```java
int[] nums = {3, 7, 1, 9, 4};

// for-each 讀取（✅ 正確用法）
for (int n : nums) {
    System.out.print(n + " ");
}
// 輸出：3 7 1 9 4

// for-each 計算總和（✅）
int sum = 0;
for (int n : nums) {
    sum += n;
}
System.out.println("Sum = " + sum);

// for-each 修改（❌ 不會影響原始陣列）
for (int n : nums) {
    n *= 2;  // 只修改了 n 這個本地變數
}
System.out.println(nums[0]);  // 仍然是 3，沒有被改變

// 需要修改時，必須用標準 for
for (int i = 0; i < nums.length; i++) {
    nums[i] *= 2;  // ✅ 真正修改陣列
}

// String 陣列 for-each
String[] names = {"Alice", "Bob", "Charlie"};
for (String name : names) {
    System.out.println("Hello, " + name + "!");
}
```

#### 練習題

---

**練習題 1：計算陣列最大值**
**難度：** Easy｜**主題：** for-each

使用 for-each 迴圈找出 `{15, 42, 8, 27, 99, 3}` 的最大值。

<details>
<summary>顯示解答</summary>

```java
int[] nums = {15, 42, 8, 27, 99, 3};
int max = nums[0];
for (int n : nums) {
    if (n > max) max = n;
}
System.out.println("最大值：" + max);  // 99
```
</details>

---

**練習題 2：判斷所有元素是否為正**
**難度：** Easy｜**主題：** for-each + boolean flag

撰寫方法判斷整數陣列中是否所有元素都大於 0。

<details>
<summary>顯示解答</summary>

```java
public static boolean allPositive(int[] arr) {
    for (int n : arr) {
        if (n <= 0) return false;
    }
    return true;
}
```
</details>

---

#### 現在試試看
> 使用 for-each 計算 `double[]` 陣列中所有元素的乘積。

---

### Unit 15：Array 演算法：最大值、最小值、總和、搜尋

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐☆☆

#### 學習目標
- 熟練實作陣列的 4 大基礎演算法
- 理解線性搜尋（Linear Search）
- 掌握 APCS CSA 常考的陣列操作題型

#### 4 大基礎演算法

```java
int[] arr = {64, 25, 12, 22, 11};

// 1. 最大值（Maximum）
int max = arr[0];
for (int i = 1; i < arr.length; i++) {
    if (arr[i] > max) max = arr[i];
}
System.out.println("Max: " + max);  // 64

// 2. 最小值（Minimum）
int min = arr[0];
for (int i = 1; i < arr.length; i++) {
    if (arr[i] < min) min = arr[i];
}
System.out.println("Min: " + min);  // 11

// 3. 總和與平均（Sum & Average）
int sum = 0;
for (int val : arr) {
    sum += val;
}
double avg = (double) sum / arr.length;
System.out.printf("Sum: %d, Avg: %.2f%n", sum, avg);

// 4. 線性搜尋（Linear Search）
int target = 22;
int index = -1;
for (int i = 0; i < arr.length; i++) {
    if (arr[i] == target) {
        index = i;
        break;
    }
}
if (index != -1) {
    System.out.println(target + " 在索引 " + index);
} else {
    System.out.println(target + " 不存在");
}
```

#### 練習題

---

**練習題 1：找最大值的索引**
**難度：** Medium

撰寫方法 `public static int indexOfMax(int[] arr)` 回傳最大值的索引，若有相同最大值回傳第一個。

<details>
<summary>顯示解答</summary>

```java
public static int indexOfMax(int[] arr) {
    int maxIndex = 0;
    for (int i = 1; i < arr.length; i++) {
        if (arr[i] > arr[maxIndex]) {
            maxIndex = i;
        }
    }
    return maxIndex;
}
```
</details>

---

**練習題 2：統計在平均值以上的個數**
**難度：** Hard

給定整數陣列，回傳值大於等於平均值的元素個數。

<details>
<summary>顯示解答</summary>

```java
public static int countAboveAverage(int[] arr) {
    double sum = 0;
    for (int val : arr) sum += val;
    double avg = sum / arr.length;
    
    int count = 0;
    for (int val : arr) {
        if (val >= avg) count++;
    }
    return count;
}
```
</details>

---

## Phase 4 — Array 進階 + 2D Array

---

### Unit 16：Array 排序演算法

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐☆☆

#### 學習目標
- 理解並實作氣泡排序（Bubble Sort）
- 理解並實作選擇排序（Selection Sort）
- 分析排序演算法的時間複雜度

#### 程式碼範例

```java
// 氣泡排序（Bubble Sort）
// 概念：相鄰元素比較，大的往右移（泡泡往上浮）
public static void bubbleSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                // 交換
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// 選擇排序（Selection Sort）
// 概念：每輪找最小值，放到前面
public static void selectionSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // 將最小值換到索引 i
        int temp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }
}

// 使用 Java 內建排序
import java.util.Arrays;
int[] data = {5, 2, 8, 1, 9};
Arrays.sort(data);  // 升序排序
System.out.println(Arrays.toString(data));  // [1, 2, 5, 8, 9]
```

#### 排序演算法比較

| 演算法 | 時間複雜度 | 空間複雜度 | APCS 重要度 |
|--------|-----------|-----------|------------|
| Bubble Sort | O(n²) | O(1) | ⭐⭐⭐ |
| Selection Sort | O(n²) | O(1) | ⭐⭐⭐ |
| Arrays.sort() | O(n log n) | O(log n) | ⭐⭐⭐⭐⭐ |

#### 練習題

---

**練習題 1：手動追蹤排序過程**
**難度：** Medium

對 `{5, 3, 8, 1, 4}` 執行選擇排序，寫出每輪結束後的陣列狀態。

<details>
<summary>顯示解答</summary>

```
初始：[5, 3, 8, 1, 4]
第1輪（最小值1，換到索引0）：[1, 3, 8, 5, 4]
第2輪（最小值3，已在索引1）：[1, 3, 8, 5, 4]
第3輪（最小值4，換到索引2）：[1, 3, 4, 5, 8]
第4輪（最小值5，已在索引3）：[1, 3, 4, 5, 8]
結果：[1, 3, 4, 5, 8]
```
</details>

---

**練習題 2：排序後找中位數**
**難度：** Hard

撰寫方法回傳陣列的中位數（排序後的中間值，若為偶數個取中間兩個的平均）。

<details>
<summary>顯示解答</summary>

```java
public static double median(int[] arr) {
    int[] sorted = arr.clone();
    Arrays.sort(sorted);
    int n = sorted.length;
    if (n % 2 == 1) {
        return sorted[n / 2];
    } else {
        return (sorted[n / 2 - 1] + sorted[n / 2]) / 2.0;
    }
}
```
</details>

---

### Unit 17：Array 進階應用與 FRQ 技巧

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐⭐☆

#### 學習目標
- 能建立並回傳新陣列的方法
- 掌握陣列複製（`clone()` vs 手動複製）
- 練習 APCS CSA Array FRQ 格式

#### 程式碼範例

```java
// 範例 1：回傳新陣列的方法
public static int[] doubledArray(int[] arr) {
    int[] result = new int[arr.length];
    for (int i = 0; i < arr.length; i++) {
        result[i] = arr[i] * 2;
    }
    return result;
}

// 範例 2：正確複製陣列（淺複製）
int[] original = {1, 2, 3, 4, 5};
int[] copy = original.clone();  // ✅ 建立獨立副本
int[] alias = original;          // ❌ 只是另一個名字，指向同一個陣列

// 範例 3：合併兩個陣列
public static int[] merge(int[] a, int[] b) {
    int[] result = new int[a.length + b.length];
    for (int i = 0; i < a.length; i++) {
        result[i] = a[i];
    }
    for (int i = 0; i < b.length; i++) {
        result[a.length + i] = b[i];
    }
    return result;
}

// 範例 4：移除指定索引（建立新陣列）
public static int[] removeAt(int[] arr, int index) {
    int[] result = new int[arr.length - 1];
    for (int i = 0, j = 0; i < arr.length; i++) {
        if (i != index) {
            result[j++] = arr[i];
        }
    }
    return result;
}
```

#### FRQ 練習

**FRQ 格式練習：成績分析**

```java
/**
 * 給定學生成績陣列，完成以下三個方法：
 * (a) 計算平均分
 * (b) 回傳高於平均的成績陣列
 * (c) 判斷成績是否為遞增順序
 */
public static double average(int[] grades) {
    int sum = 0;
    for (int g : grades) sum += g;
    return (double) sum / grades.length;
}

public static int[] aboveAverage(int[] grades) {
    double avg = average(grades);
    int count = 0;
    for (int g : grades) {
        if (g > avg) count++;
    }
    int[] result = new int[count];
    int j = 0;
    for (int g : grades) {
        if (g > avg) result[j++] = g;
    }
    return result;
}

public static boolean isIncreasing(int[] grades) {
    for (int i = 0; i < grades.length - 1; i++) {
        if (grades[i] >= grades[i + 1]) return false;
    }
    return true;
}
```

---

### Unit 18：2D Array 基礎

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐☆☆

#### 學習目標
- 理解二維陣列（2D Array）的結構：row（列）× column（欄）
- 掌握宣告、初始化與存取 2D 陣列
- 使用 `arr.length` 和 `arr[0].length` 取得維度

#### 概念說明

2D Array 是**陣列的陣列**，可視為表格（矩陣）。

```
int[][] matrix = new int[3][4];
// 3 列（row）× 4 欄（column）

      col0  col1  col2  col3
row0:   0     0     0     0
row1:   0     0     0     0
row2:   0     0     0     0

matrix[1][2] = 存取第 2 列（row1）、第 3 欄（col2）
```

#### 程式碼範例

```java
// 宣告方式 1：指定大小
int[][] grid = new int[3][4];
grid[0][0] = 1;
grid[1][2] = 7;

// 宣告方式 2：初始化清單
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// 取得維度
int rows = matrix.length;       // 3（列數）
int cols = matrix[0].length;    // 3（欄數）

// 存取元素
System.out.println(matrix[1][2]);  // 6（第2列第3欄）
System.out.println(matrix[0][0]);  // 1（左上角）
System.out.println(matrix[2][2]);  // 9（右下角）

// String[][] 範例（APCS CSA 常用）
String[][] table = {
    {"Name", "Score", "Grade"},
    {"Alice", "95", "A"},
    {"Bob",   "82", "B"}
};
System.out.println(table[1][0]);  // Alice
```

#### 練習題

---

**練習題 1：建立身份矩陣（Identity Matrix）**
**難度：** Medium

建立 n×n 的二維陣列，對角線為 1，其餘為 0。

<details>
<summary>顯示解答</summary>

```java
int n = 4;
int[][] identity = new int[n][n];
for (int i = 0; i < n; i++) {
    identity[i][i] = 1;
}

// 印出
for (int[] row : identity) {
    for (int val : row) {
        System.out.print(val + " ");
    }
    System.out.println();
}
```
</details>

---

**練習題 2：2D 陣列對角線總和**
**難度：** Hard

計算方陣（n×n）主對角線與反對角線的總和。

<details>
<summary>顯示解答</summary>

```java
public static int diagonalSum(int[][] matrix) {
    int sum = 0;
    int n = matrix.length;
    for (int i = 0; i < n; i++) {
        sum += matrix[i][i];              // 主對角線
        sum += matrix[i][n - 1 - i];     // 反對角線
    }
    // 若 n 為奇數，中心點被加兩次，需減掉
    if (n % 2 == 1) {
        sum -= matrix[n / 2][n / 2];
    }
    return sum;
}
```
</details>

---

### Unit 19：2D Array 遍歷與演算法

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐⭐☆

#### 學習目標
- 使用巢狀迴圈遍歷 2D 陣列（row-major order）
- 能對 2D 陣列進行搜尋、統計、轉置等操作
- 掌握 APCS CSA 2D Array FRQ 常見模式

#### 程式碼範例

```java
int[][] matrix = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// 模式 1：標準遍歷（row-major order，逐列）
for (int r = 0; r < matrix.length; r++) {
    for (int c = 0; c < matrix[r].length; c++) {
        System.out.printf("%4d", matrix[r][c]);
    }
    System.out.println();
}

// 模式 2：for-each 遍歷（唯讀）
for (int[] row : matrix) {
    for (int val : row) {
        System.out.print(val + " ");
    }
    System.out.println();
}

// 模式 3：計算總和
int sum = 0;
for (int[] row : matrix) {
    for (int val : row) {
        sum += val;
    }
}
System.out.println("Total = " + sum);  // 78

// 模式 4：找最大值
int max = matrix[0][0];
for (int r = 0; r < matrix.length; r++) {
    for (int c = 0; c < matrix[r].length; c++) {
        if (matrix[r][c] > max) max = matrix[r][c];
    }
}

// 模式 5：矩陣轉置（Transpose）
int rows = matrix.length;
int cols = matrix[0].length;
int[][] transposed = new int[cols][rows];
for (int r = 0; r < rows; r++) {
    for (int c = 0; c < cols; c++) {
        transposed[c][r] = matrix[r][c];
    }
}
```

#### 練習題

---

**練習題 1：每列最大值**
**難度：** Medium

給定 2D 陣列，印出每列的最大值。

<details>
<summary>顯示解答</summary>

```java
public static void printRowMax(int[][] arr) {
    for (int r = 0; r < arr.length; r++) {
        int max = arr[r][0];
        for (int c = 1; c < arr[r].length; c++) {
            if (arr[r][c] > max) max = arr[r][c];
        }
        System.out.println("Row " + r + " max: " + max);
    }
}
```
</details>

---

**練習題 2：FRQ — 2D 陣列旋轉 90 度**
**難度：** Hard

給定 n×n 的 2D 陣列，順時針旋轉 90 度回傳新陣列。

<details>
<summary>顯示解答</summary>

```java
public static int[][] rotate90(int[][] matrix) {
    int n = matrix.length;
    int[][] result = new int[n][n];
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            result[c][n - 1 - r] = matrix[r][c];
        }
    }
    return result;
}
```
</details>

---

### Unit 20：Array + Iteration 綜合練習與 FRQ 衝刺

> **預估時間：** 1.5 小時｜**難度：** ⭐⭐⭐⭐⭐

#### 學習目標
- 整合所有 Array 與 Iteration 知識
- 完成 APCS CSA 考試等級的完整 FRQ
- 進行最終自我評估

#### APCS CSA Array FRQ 高頻題型

| 題型 | 頻率 | 關鍵技巧 |
|------|------|---------|
| 找最大/最小值及其索引 | ⭐⭐⭐⭐⭐ | 初始化 `maxIndex = 0` |
| 計算符合條件的元素數 | ⭐⭐⭐⭐⭐ | counter pattern |
| 建立並回傳新陣列 | ⭐⭐⭐⭐ | 先計算大小，再填入 |
| 2D 陣列逐列/欄處理 | ⭐⭐⭐⭐ | row/col 雙層迴圈 |
| 陣列排序後操作 | ⭐⭐⭐ | `Arrays.sort()` |

#### 完整 FRQ 練習

**FRQ：學生成績管理系統**

以下程式模擬 APCS CSA FRQ Part (a)(b)(c) 格式：

```java
public class GradeAnalyzer {
    private int[] grades;  // 儲存成績的陣列

    public GradeAnalyzer(int[] grades) {
        this.grades = grades;
    }

    // Part (a)：計算平均成績
    public double getAverage() {
        double sum = 0;
        for (int g : grades) {
            sum += g;
        }
        return sum / grades.length;
    }

    // Part (b)：回傳高於平均的成績陣列
    public int[] getAboveAverage() {
        double avg = getAverage();
        int count = 0;
        for (int g : grades) {
            if (g > avg) count++;
        }
        int[] result = new int[count];
        int j = 0;
        for (int g : grades) {
            if (g > avg) result[j++] = g;
        }
        return result;
    }

    // Part (c)：統計各等第人數（A:90+, B:80+, C:70+, D:60+, F:<60）
    public int[] getGradeDistribution() {
        int[] dist = new int[5];  // [A, B, C, D, F]
        for (int g : grades) {
            if (g >= 90)      dist[0]++;
            else if (g >= 80) dist[1]++;
            else if (g >= 70) dist[2]++;
            else if (g >= 60) dist[3]++;
            else              dist[4]++;
        }
        return dist;
    }
}
```

#### 模擬考題

**2D Array FRQ（模擬 APCS CSA 格式）**

```
給定二維整數陣列 grid，完成以下方法：

(a) public static int rowSum(int[][] grid, int row)
    回傳指定列的總和

(b) public static int[] allRowSums(int[][] grid)
    回傳每列總和組成的陣列

(c) public static boolean isMagicSquare(int[][] grid)
    判斷是否為魔法方陣（每列、每欄、兩對角線的總和相等）
```

<details>
<summary>顯示完整解答</summary>

```java
// Part (a)
public static int rowSum(int[][] grid, int row) {
    int sum = 0;
    for (int val : grid[row]) {
        sum += val;
    }
    return sum;
}

// Part (b)
public static int[] allRowSums(int[][] grid) {
    int[] sums = new int[grid.length];
    for (int r = 0; r < grid.length; r++) {
        sums[r] = rowSum(grid, r);  // 呼叫 Part (a)
    }
    return sums;
}

// Part (c)
public static boolean isMagicSquare(int[][] grid) {
    int n = grid.length;
    int target = rowSum(grid, 0);  // 以第一列為基準

    // 檢查每列
    for (int r = 0; r < n; r++) {
        if (rowSum(grid, r) != target) return false;
    }

    // 檢查每欄
    for (int c = 0; c < n; c++) {
        int colSum = 0;
        for (int r = 0; r < n; r++) colSum += grid[r][c];
        if (colSum != target) return false;
    }

    // 檢查主對角線
    int diag1 = 0;
    for (int i = 0; i < n; i++) diag1 += grid[i][i];
    if (diag1 != target) return false;

    // 檢查反對角線
    int diag2 = 0;
    for (int i = 0; i < n; i++) diag2 += grid[i][n - 1 - i];
    if (diag2 != target) return false;

    return true;
}
```
</details>

---

## 最終里程碑自我評估

### Iteration 能力指標

| 技能 | 已掌握 | 需複習 |
|------|:------:|:------:|
| while 迴圈語法與執行流程 | ☐ | ☐ |
| for 迴圈三段結構 | ☐ | ☐ |
| 計算迴圈執行次數 | ☐ | ☐ |
| 巢狀迴圈追蹤 | ☐ | ☐ |
| String charAt() 遍歷 | ☐ | ☐ |
| break / continue 應用 | ☐ | ☐ |
| 常見迴圈 Bug 識別 | ☐ | ☐ |
| 方法與迴圈整合 | ☐ | ☐ |

### Array 能力指標

| 技能 | 已掌握 | 需複習 |
|------|:------:|:------:|
| 陣列宣告與初始化（3 種方式）| ☐ | ☐ |
| 索引存取與修改元素 | ☐ | ☐ |
| 標準 for 遍歷 | ☐ | ☐ |
| for-each 遍歷與限制 | ☐ | ☐ |
| 最大值、最小值、總和 | ☐ | ☐ |
| 線性搜尋 | ☐ | ☐ |
| 氣泡排序 / 選擇排序 | ☐ | ☐ |
| 建立並回傳新陣列 | ☐ | ☐ |
| 2D Array 宣告與存取 | ☐ | ☐ |
| 2D Array 雙層迴圈遍歷 | ☐ | ☐ |
| FRQ 多部分格式回答 | ☐ | ☐ |

---

## 推薦學習資源

| 資源 | 類型 | 說明 |
|------|------|------|
| [AP Classroom](https://myap.collegeboard.org) | 官方 | APCS CSA 官方題庫與影片 |
| [CodingBat Java](https://codingbat.com/java) | 練習平台 | 分主題的 Java 互動練習 |
| [W3Schools Java Array](https://www.w3schools.com/java/java_arrays.asp) | 參考文件 | 陣列語法快速查詢 |
| [LeetCode Easy](https://leetcode.com/problemset/?difficulty=EASY&topicSlugs=array) | 進階練習 | Array 類 Easy 題（考前衝刺用）|
| [Past FRQ - CollegeBoard](https://apcentral.collegeboard.org/courses/ap-computer-science-a/exam/past-exam-questions) | 考古題 | 歷年 FRQ 完整題目與評分標準 |

---

## 學習時間規劃建議

| 週次 | 單元 | 建議完成時間 |
|------|------|------------|
| 第 1 週 | Unit 01-05（Iteration 基礎）| 7.5 小時 |
| 第 2 週 | Unit 06-10（Iteration 進階）| 7.5 小時 |
| 第 3 週 | Unit 11-15（Array 基礎）| 7.5 小時 |
| 第 4 週 | Unit 16-20（Array 進階）| 7.5 小時 |
| **總計** | **20 單元** | **30 小時** |

> **每日學習建議（以每天 1.5 小時計算）：**
> - 每日完成 1 個單元
> - 週末複習當週內容並完成額外練習題
> - 每週末做 1 份 FRQ 模擬練習

---

*製作日期：2026-05-03 ｜ 版本：1.0*  
*涵蓋範圍：APCS CSA Unit 4（Iteration）、Unit 6（Array）、Unit 8（2D Array）*
