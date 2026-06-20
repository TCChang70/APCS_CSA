# Unit 04：巢狀迴圈 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. 巢狀迴圈追蹤
```java
int total = 0;
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
        total++;
    }
}
```
`total` 的最終值為何？
(A) 7  (B) 10  (C) 12  (D) 14

### 2. 三角形迴圈
```java
int count = 0;
for (int i = 1; i <= 5; i++) {
    for (int j = 1; j < i; j++) {
        count++;
    }
}
```
`count` 的最終值為何？
(A) 5  (B) 10  (C) 15  (D) 20

### 3. 內外層索引
```java
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 2; j++) {
        System.out.println("(" + i + "," + j + ")");
    }
}
```
共輸出幾行？
(A) 4  (B) 5  (C) 6  (D) 9

### 4. 圖形輸出
```java
for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++) {
        System.out.print("*");
    }
    System.out.println();
}
```
輸出的圖形為何？
(A) 4×4 正方形  (B) 上三角形  (C) 下三角形  (D) 菱形

### 5. 變數遮蔽
```java
int i = 99;
for (int i = 0; i < 3; i++) {  // 此行？
    System.out.print(i + " ");
}
```
(A) 輸出 99  (B) 輸出 0 1 2  (C) 輸出 99 0 1 2  (D) 編譯錯誤

---

## 程式實作（5 分）

### FRQ：乘法表列印
撰寫方法，使用巢狀迴圈印出 n×n 乘法表（n×n 的整數矩陣）。

```java
public static void printMultiplicationTable(int n)
```

**範例：** `printMultiplicationTable(3)` 輸出：
```
1 2 3
2 4 6
3 6 9
```
每個數字以空格分隔，每行結尾換行。

> 解答請見：`answer-key.md`
