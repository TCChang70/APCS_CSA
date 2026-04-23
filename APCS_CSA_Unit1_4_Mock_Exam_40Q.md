# 📝 AP Computer Science A — 前四單元模擬考試 (40題選擇題)

## 🎯 考試說明

| 項目 | 內容 |
|------|------|
| **考試範圍** | Unit 1：基本資料型別 / Unit 2：使用物件 / Unit 3：布林表達式與條件判斷 / Unit 4：迴圈 |
| **題型** | 單選題 (每題 2.5 分，共 100 分) |
| **考試時間** | 90 分鐘 |
| **建議** | 請仔細閱讀每段程式碼，注意型別與運算子的細節 |

---

## 🔵 Unit 1：基本資料型別 (Primitive Types) — Q1～Q10

---

**1.** 下列哪一個選項是 Java 中正確的整數變數宣告並賦值？

- A) `integer x = 5;`
- B) `int x = 5;`
- C) `Int x = 5;`
- D) `var int x = 5;`
- E) `declare int x = 5;`

---

**2.** 在 Java 中執行以下運算式，結果為何？

```java
System.out.println(17 / 4);
```

- A) 4.25
- B) 4.0
- C) 4
- D) 5
- E) 0.25

---

**3.** 執行以下運算式後，結果為何？

```java
System.out.println(17 % 4);
```

- A) 4
- B) 1
- C) 0
- D) 4.25
- E) 3

---

**4.** 執行以下程式碼後，輸出結果為何？

```java
int x = 5;
x += 3;
x *= 2;
System.out.println(x);
```

- A) 10
- B) 16
- C) 13
- D) 11
- E) 8

---

**5.** 執行以下程式碼後，輸出結果為何？

```java
System.out.println((double) 7 / 2);
```

- A) 3
- B) 3.5
- C) 3.0
- D) 4.0
- E) 0.0

---

**6.** 執行以下程式碼後，`x` 的值為何？

```java
int x = 10;
x -= 3;
x /= 2;
```

- A) 6
- B) 3
- C) 3.5
- D) 5
- E) 7

---

**7.** 執行以下程式碼後，輸出結果為何？

```java
double x = 1.0 / 3;
System.out.println(x);
```

- A) 0.0
- B) 0.333
- C) 0.3333333333333333
- D) 0
- E) 1

---

**8.** 下列哪一個**不是** Java 的基本資料型別 (primitive type)？

- A) `int`
- B) `double`
- C) `boolean`
- D) `String`
- E) `char`

---

**9.** 執行以下程式碼後，輸出結果為何？

```java
int a = 5;
int b = a++;
System.out.println(a + " " + b);
```

- A) 5 5
- B) 6 5
- C) 5 6
- D) 6 6
- E) 6 4

---

**10.** 下列哪一個選項可以正確地將 `double` 顯式轉換 (explicit cast) 為 `int`？

```java
double d = 3.99;
```

- A) `int x = d;`
- B) `int x = (int) d;`
- C) `int x = double(d);`
- D) `int x = int(d);`
- E) `int x = cast(d);`

---

## 🔵 Unit 2：使用物件 (Using Objects) — Q11～Q20

---

**11.** 執行以下程式碼後，輸出結果為何？

```java
String s = "Hello, World!";
System.out.println(s.length());
```

- A) 12
- B) 13
- C) 11
- D) 5
- E) 10

---

**12.** 執行以下程式碼後，輸出結果為何？

```java
String s = "Hello";
System.out.println(s.substring(1, 3));
```

- A) `"Hello"`
- B) `"He"`
- C) `"el"`
- D) `"ell"`
- E) `"ello"`

---

**13.** 執行以下程式碼後，輸出結果為何？

```java
String s = "Java";
System.out.println(s.charAt(2));
```

- A) `J`
- B) `a`
- C) `v`
- D) `A`
- E) `va`

---

**14.** 執行以下程式碼後，輸出結果為何？

```java
String s1 = "Hello";
String s2 = new String("Hello");
System.out.println(s1 == s2);
System.out.println(s1.equals(s2));
```

- A) `true` / `true`
- B) `false` / `true`
- C) `true` / `false`
- D) `false` / `false`
- E) 編譯錯誤

---

**15.** 執行以下程式碼後，輸出結果為何？

```java
System.out.println(Math.abs(-7.5));
```

- A) -7.5
- B) 7.5
- C) 7
- D) 8
- E) -7

---

**16.** 執行以下程式碼後，輸出結果為何？

```java
System.out.println(Math.pow(2, 10));
```

- A) 20.0
- B) 1024
- C) 1024.0
- D) 210.0
- E) 100.0

---

**17.** 執行以下程式碼後，輸出結果為何？

```java
String s = "Hello World";
System.out.println(s.indexOf("World"));
```

- A) 5
- B) 6
- C) 4
- D) 0
- E) -1

---

**18.** 執行以下程式碼後，輸出結果為何？

```java
double result = Math.sqrt(9 + 16);
System.out.println(result);
```

- A) 5
- B) 25.0
- C) 5.0
- D) 4.0
- E) 6.0

---

**19.** 下列哪一個選項可以正確地產生一個介於 **1 到 10（含）** 之間的隨機整數？

- A) `(int)(Math.random() * 10)`
- B) `(int)(Math.random() * 10) + 1`
- C) `Math.random() * 11`
- D) `(int)(Math.random() * 11)`
- E) `(int)(Math.random() + 10)`

---

**20.** 執行以下程式碼後，輸出結果為何？

```java
String s = "Programming";
System.out.println(s.substring(0, 7));
```

- A) `"Program"`
- B) `"Programm"`
- C) `"Programmi"`
- D) `"rogrammin"`
- E) `"program"`

---

## 🔵 Unit 3：布林表達式與條件判斷 (Boolean Expressions and if Statements) — Q21～Q30

---

**21.** 執行以下程式碼後，輸出結果為何？

```java
int x = 5;
if (x > 3) {
    System.out.println("A");
} else {
    System.out.println("B");
}
```

- A) A
- B) B
- C) AB
- D) BA
- E) 沒有輸出

---

**22.** 執行以下程式碼後，輸出結果為何？

```java
int x = 5, y = 10;
if (x > 3 && y < 8) {
    System.out.println("True");
} else {
    System.out.println("False");
}
```

- A) True
- B) False
- C) TrueFalse
- D) 編譯錯誤
- E) 沒有輸出

---

**23.** 在 Java 中，比較兩個 `String` 物件**內容**是否相等，下列哪一個寫法是正確的？

- A) `str1 == str2`
- B) `str1.equals(str2)`
- C) `str1.compare(str2)`
- D) `str1 = str2`
- E) `equals(str1, str2)`

---

**24.** 下列運算式的結果為何？

```java
!true || false
```

- A) true
- B) false
- C) null
- D) 編譯錯誤
- E) 0

---

**25.** 執行以下程式碼後，輸出結果為何？

```java
int score = 85;
if (score >= 90) {
    System.out.println("A");
} else if (score >= 80) {
    System.out.println("B");
} else if (score >= 70) {
    System.out.println("C");
} else {
    System.out.println("F");
}
```

- A) A
- B) B
- C) C
- D) F
- E) BC

---

**26.** 根據 De Morgan's Law，下列哪一個與 `!(a && b)` 等價？

- A) `!a && !b`
- B) `!a || !b`
- C) `a || b`
- D) `a && b`
- E) `!a && b`

---

**27.** 執行以下程式碼後，`x` 的值為何？

```java
int x = 10;
if (x % 2 == 0) {
    x = x / 2;
} else {
    x = x * 3 + 1;
}
```

- A) 10
- B) 5
- C) 31
- D) 6
- E) 0

---

**28.** 執行以下程式碼後，輸出結果為何？

```java
boolean a = true;
boolean b = false;
System.out.println(a || b);
System.out.println(a && b);
```

- A) `true` / `false`
- B) `false` / `true`
- C) `true` / `true`
- D) `false` / `false`
- E) `1` / `0`

---

**29.** 下列哪一個條件會因為**短路求值 (short-circuit evaluation)** 而使 `someMethod()` 不被執行？

- A) `false && someMethod()`
- B) `true && someMethod()`
- C) `false || someMethod()`
- D) `someMethod() && true`
- E) `someMethod() || false`

---

**30.** 執行以下程式碼後，輸出結果為何？

```java
int x = 5;
if (x > 10)
    System.out.println("A");
    System.out.println("B");
System.out.println("C");
```

- A) C
- B) B  
   C
- C) A  
   B  
   C
- D) A  
   C
- E) A  
   B

---

## 🔵 Unit 4：迴圈 (Iteration) — Q31～Q40

---

**31.** 執行以下程式碼後，輸出結果為何？

```java
for (int i = 0; i < 5; i++) {
    System.out.print(i + " ");
}
```

- A) `0 1 2 3 4 5`
- B) `1 2 3 4 5`
- C) `0 1 2 3 4`
- D) `0 1 2 3`
- E) `1 2 3 4`

---

**32.** 執行以下程式碼後，輸出結果為何？

```java
int sum = 0;
for (int i = 1; i <= 5; i++) {
    sum += i;
}
System.out.println(sum);
```

- A) 10
- B) 15
- C) 25
- D) 5
- E) 20

---

**33.** 以下迴圈總共執行幾次？

```java
for (int i = 10; i > 0; i -= 3) {
    System.out.println(i);
}
```

- A) 3
- B) 4
- C) 10
- D) 2
- E) 5

---

**34.** 執行以下程式碼後，輸出結果為何？

```java
int i = 1;
while (i <= 4) {
    System.out.print(i * 2 + " ");
    i++;
}
```

- A) `1 2 3 4`
- B) `2 4 6 8`
- C) `2 4 6 8 10`
- D) `1 3 5 7`
- E) `0 2 4 6`

---

**35.** 執行以下巢狀迴圈後，輸出結果為何？

```java
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        System.out.print(i * j + " ");
    }
    System.out.println();
}
```

- A) `1 1 1` / `2 2 2` / `3 3 3`
- B) `1 2 3` / `2 4 6` / `3 6 9`
- C) `1 2 3` / `2 3 4` / `3 4 5`
- D) `1 4 9` / `1 4 9` / `1 4 9`
- E) `1 2 3` / `4 5 6` / `7 8 9`

---

**36.** 執行以下程式碼後，輸出結果為何？

```java
String s = "Hello";
int count = 0;
for (int i = 0; i < s.length(); i++) {
    if (s.charAt(i) == 'l') {
        count++;
    }
}
System.out.println(count);
```

- A) 1
- B) 0
- C) 2
- D) 3
- E) 5

---

**37.** 執行以下程式碼後，`x` 的最終值為何？

```java
int x = 1;
while (x < 100) {
    x *= 2;
}
System.out.println(x);
```

- A) 64
- B) 100
- C) 128
- D) 256
- E) 99

---

**38.** 執行以下程式碼後，輸出結果為何？

```java
int result = 0;
for (int i = 0; i <= 10; i += 2) {
    result += i;
}
System.out.println(result);
```

- A) 20
- B) 25
- C) 30
- D) 55
- E) 10

---

**39.** 以下巢狀迴圈總共輸出幾次 `"Hello"`？

```java
for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 3; j++) {
        System.out.println("Hello");
    }
}
```

- A) 7
- B) 12
- C) 8
- D) 6
- E) 16

---

**40.** 執行以下程式碼後，輸出結果為何？

```java
int n = 1;
do {
    System.out.print(n + " ");
    n *= 3;
} while (n < 30);
```

- A) `1 3 9 27`
- B) `1 3 9`
- C) `3 9 27`
- D) `1 3 9 27 81`
- E) `1`

