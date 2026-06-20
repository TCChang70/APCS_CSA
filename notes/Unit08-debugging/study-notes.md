# Unit 08：常見迴圈錯誤與除錯技巧

## 學習目標
- 識別並修正 5 種常見迴圈錯誤
- 使用 `System.out.println()` 追蹤迴圈狀態
- 理解 APCS 考試中的迴圈陷阱題

---

## 5 大常見迴圈錯誤

| # | 錯誤類型 | 描述 | 修正方法 |
|---|---------|------|---------|
| 1 | Off-by-one | 多一次或少一次 | 確認 `<` vs `<=` |
| 2 | 無限迴圈 | 條件永不為 false | 確認更新邏輯 |
| 3 | 初始化錯誤 | 累加從非 0 / 累乘從非 1 開始 | 根據操作選擇初始值 |
| 4 | 作用域問題 | 迴圈外使用 for 的控制變數 | 在迴圈外宣告 |
| 5 | 意外覆蓋 | 在迴圈內重複宣告累計變數 | 移到迴圈外宣告 |

---

## 除錯技巧

### 1. Print Debugging
```java
for (int i = 0; i < 5; i++) {
    System.out.println("DEBUG: i = " + i + ", sum = " + sum);
    sum += i;
}
```

### 2. 手動追蹤（Trace Table）
用紙筆列出每次迭代的變數值變化

### 3. 邊界測試
測試 n=0、n=1、n=max 的情況

### 4. 二分法定位
縮小 print 語句範圍找到 bug 位置

---

## 錯誤分析範例

```java
// 錯誤版 1：Off-by-one
int sum = 0;
for (int i = 1; i < n; i++) {  // ❌ 少算 n=10
    sum += i;
}
// 修正：i <= n

// 錯誤版 2：累乘初始化錯誤
int product = 0;  // ❌ 應為 1
for (int i = 1; i <= 5; i++) {
    product *= i;
}
// 結果永遠是 0

// 錯誤版 3：無限迴圈
int i = 0;
while (i < 10) {
    System.out.println(i);
    // ❌ 忘記 i++
}

// 錯誤版 4：作用域問題
for (int j = 0; j < 10; j++) { }
System.out.println(j);  // ❌ j 超出作用域
```

---

## 練習題：找 Bug

```java
// 此程式碼有哪些錯誤？
int total = 1;
for (int k = 1; k < 10; k++) {
    total = total + k;
}
System.out.println("1 to 10 sum = " + total);
```

---

## 現在試試看
撰寫一個計算方法，加入 print debug 觀察執行過程
