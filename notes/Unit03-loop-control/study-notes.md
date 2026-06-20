# Unit 03：迴圈控制變數與條件設計

## 學習目標
- 掌握迴圈變數的命名與作用域
- 能設計精確的起始值與終止條件
- 理解常見的 Off-by-one Error

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

---

## 條件設計技巧
- 複合條件（`&&`、`||`）在迴圈中的應用
- 使用方法回傳值作為條件（`s.length()`）
- 浮點數條件的陷阱（精度問題導致無限迴圈）

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

## 現在試試看
計算 1 到 50 中所有質數的個數
