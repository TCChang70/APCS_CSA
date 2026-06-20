# Unit 13：Array 遍歷 — 標準 `for` 迴圈 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. 基本遍歷
```java
int[] arr = {2, 4, 6, 8};
int sum = 0;
for (int i = 0; i < arr.length; i++) {
    sum += arr[i];
}
System.out.println(sum);
```
輸出為何？
(A) 8  (B) 20  (C) 24  (D) 14

### 2. 找最大值
```java
int[] scores = {72, 85, 90, 68, 88};
int max = scores[0];
for (int i = 1; i < scores.length; i++) {
    if (scores[i] > max) {
        max = scores[i];
    }
}
System.out.println(max);
```
輸出為何？
(A) 72  (B) 85  (C) 90  (D) 88

### 3. 計數模式
```java
int[] data = {5, 12, 3, 18, 7, 15, 9};
int count = 0;
for (int i = 0; i < data.length; i++) {
    if (data[i] > 10) {
        count++;
    }
}
System.out.println(count);
```
輸出為何？
(A) 2  (B) 3  (C) 4  (D) 5

### 4. 反向遍歷
```java
int[] arr = {10, 20, 30, 40};
for (int i = arr.length - 1; i >= 0; i--) {
    System.out.print(arr[i] + " ");
}
```
輸出為何？
(A) 10 20 30 40  (B) 40 30 20 10  (C) 40 30 20 10 0  (D) 10 20 30

### 5. 相鄰比較
```java
int[] a = {1, 3, 2, 5, 4};
int count = 0;
for (int i = 0; i < a.length - 1; i++) {
    if (a[i] < a[i + 1]) {
        count++;
    }
}
System.out.println(count);
```
輸出為何？（計算相鄰遞增的次數）
(A) 1  (B) 2  (C) 3  (D) 4

---

## 程式實作（5 分）

### FRQ：陣列範圍
撰寫方法，回傳陣列中「最大值與最小值的差」。

```java
public static int range(int[] arr)
```

**範例：**
- `range({3, 7, 1, 9, 4})` → 9 - 1 = **8**
- `range({10, 20, 30})` → 30 - 10 = **20**
- `range({5})` → 5 - 5 = **0**

> 解答請見：`answer-key.md`
