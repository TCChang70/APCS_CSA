# Unit 11：Array 宣告與初始化 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. 三種初始化
下列哪個陣列初始化會造成編譯錯誤？
(A) `int[] a = new int[5];`
(B) `int[] b = {1, 2, 3};`
(C) `int[] c; c = {1, 2, 3};`
(D) `int[] d; d = new int[]{1, 2, 3};`

### 2. 預設值
```java
double[] arr = new double[3];
System.out.println(arr[1]);
```
輸出為何？
(A) 0  (B) 0.0  (C) null  (D) 編譯錯誤

### 3. length 屬性
```java
int[] arr = {2, 4, 6, 8};
System.out.println(arr.length);
System.out.println(arr[arr.length - 1]);
```
輸出為何？
(A) 3 和 6  (B) 4 和 8  (C) 4 和 6  (D) 3 和 8

### 4. 索引範圍
給定 `int[] nums = new int[10];`，最後一個元素的索引為何？
(A) 9  (B) 10  (C) 0  (D) 11

### 5. ArrayIndexOutOfBoundsException
```java
int[] data = {5, 10, 15};
for (int i = 0; i <= data.length; i++) {
    System.out.println(data[i]);
}
```
此程式會發生什麼？
(A) 輸出 5 10 15  (B) 拋出 ArrayIndexOutOfBoundsException  (C) 輸出 5 10 15 0  (D) 編譯錯誤

---

## 程式實作（5 分）

### FRQ：建立遞增陣列
撰寫方法，建立一個大小為 `n` 的整數陣列，內容從 `start` 開始每次增加 `step`。

```java
public static int[] generateArray(int n, int start, int step)
```

**範例：**
- `generateArray(5, 1, 2)` → `{1, 3, 5, 7, 9}`
- `generateArray(4, 10, -1)` → `{10, 9, 8, 7}`
- `generateArray(3, 0, 5)` → `{0, 5, 10}`

> 解答請見：`answer-key.md`
