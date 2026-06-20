# Unit 01：`while` 迴圈基礎

## 學習目標
- 理解 `while` 迴圈的執行流程（Entry Condition）
- 能正確設定迴圈條件與終止條件
- 辨別無限迴圈並修正

---

## 概念說明

`while` 迴圈在**條件為 true** 時持續執行，每次執行前先檢查條件。

```java
while (條件) {
    // 重複執行的程式碼（迴圈主體）
}
```

### 執行流程
1. 檢查條件 → 若 `false` 則跳出迴圈
2. 執行迴圈主體
3. 回到步驟 1

---

## 程式碼範例

### 範例 1：從 1 數到 5（基本計數）
```java
int i = 1;
while (i <= 5) {
    System.out.println(i);
    i++;  // 更新變數，避免無限迴圈
}
// 輸出：1 2 3 4 5
```

### 範例 2：計算 1 到 10 的總和（累加模式）
```java
int sum = 0;
int n = 1;
while (n <= 10) {
    sum += n;
    n++;
}
System.out.println("總和 = " + sum);  // 55
```

### 範例 3：讀取輸入直到輸入 0（哨兵值模式）
```java
// Scanner scanner = new Scanner(System.in);
// int num = scanner.nextInt();
// while (num != 0) {
//     System.out.println("輸入了：" + num);
//     num = scanner.nextInt();
// }
```

---

## 常見錯誤

| 錯誤類型 | 錯誤範例 | 說明 |
|---------|---------|------|
| 無限迴圈 | `while (i < 10)` 但忘記 `i++` | 條件永遠為 true |
| Off-by-one | `while (i < 10)` vs `while (i <= 10)` | 差一個數 |
| 賦值 vs 比較 | `while (i = 10)` | 應用 `==`，`=` 是賦值 |

---

## 練習題

### Easy：倒數計時
從 10 倒數到 1，每個數字各佔一行，最後印出 `"Go!"`

### Medium：找出第一個大於 50 且能被 7 整除的數

---

## 現在試試看
計算 1 到 100 中所有奇數的總和
