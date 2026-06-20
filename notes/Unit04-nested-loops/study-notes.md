# Unit 04：巢狀迴圈（Nested Loops）

## 學習目標
- 理解巢狀迴圈的執行順序
- 能追蹤每次外/內層迴圈的變數值
- 應用巢狀迴圈印出二維圖形

---

## 概念說明

巢狀迴圈 = 迴圈裡面還有迴圈。外層每執行一次，內層完整執行一輪。

```java
for (外層初始; 外層條件; 外層更新) {
    for (內層初始; 內層條件; 內層更新) {
        // 最內部的程式碼
    }
}
```

**總執行次數 = 外層次數 × 內層次數**

---

## 程式碼範例

### 範例 1：追蹤 (i, j) 組合
```java
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        System.out.println("i=" + i + ", j=" + j);
    }
}
// 共 9 次輸出
```

### 範例 2：乘法表（9×9）
```java
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= 9; j++) {
        System.out.printf("%4d", i * j);
    }
    System.out.println();
}
```

### 範例 3：矩形圖案（4 行 6 列）
```java
for (int row = 0; row < 4; row++) {
    for (int col = 0; col < 6; col++) {
        System.out.print("* ");
    }
    System.out.println();
}
```

---

## 常見錯誤

| 錯誤 | 說明 |
|------|------|
| 變數同名 | 內外層都用 `i`，內層遮蔽外層 |
| 誤解順序 | 不是外層先跑完再內層，而是外層一次內層一圈 |
| 效能 | 三層巢狀迴圈時需注意時間複雜度 |

---

## 練習題

### Easy：追蹤 count 最終值
```java
int count = 0;
for (int i = 0; i < 4; i++) {
    for (int j = 0; j < i; j++) {
        count++;
    }
}
System.out.println(count);  // ?
```

### Medium：印出數字三角形（n=5）
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### Hard：用巢狀迴圈找出 2-50 的所有質數

---

## 現在試試看
印出完整九九乘法表（格式化輸出）
