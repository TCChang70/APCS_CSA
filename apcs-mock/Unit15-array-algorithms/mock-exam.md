# Unit 15：Array 基礎演算法 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. 最大值演算法
關於找陣列最大值，下列敘述何者**錯誤**？
(A) 應初始化 `max` 為陣列第一個元素
(B) 可從索引 0 開始遍歷
(C) 初始化 `max = 0` 在陣列全為負數時會出錯
(D) 使用 for-each 無法實作找最大值

### 2. 最小值
```java
int[] arr = {8, 3, 5, 1, 7};
int min = arr[0];
for (int i = 1; i < arr.length; i++) {
    if (arr[i] < min) {
        min = arr[i];
    }
}
System.out.println(min);
```
輸出為何？
(A) 1  (B) 3  (C) 5  (D) 8

### 3. 線性搜尋
```java
public static int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```
`linearSearch({4, 2, 7, 1, 9}, 7)` 回傳值為何？
(A) 1  (B) 2  (C) 3  (D) -1

### 4. 總和與平均
```java
int[] vals = {10, 20, 30, 40};
int sum = 0;
for (int v : vals) sum += v;
double avg = (double) sum / vals.length;
System.out.println(avg);
```
輸出為何？
(A) 20.0  (B) 25.0  (C) 30.0  (D) 100.0

### 5. 時間複雜度
線性搜尋在最差情況下的時間複雜度為何？
(A) O(1)  (B) O(log n)  (C) O(n)  (D) O(n²)

---

## 程式實作（5 分）

### FRQ：第二大的值
撰寫方法，找出陣列中「第二大的值」。如果陣列長度小於 2，回傳 `Integer.MIN_VALUE`。

```java
public static int secondLargest(int[] arr)
```

**範例：**
- `secondLargest({5, 3, 9, 1, 7})` → **7**
- `secondLargest({1, 2})` → **1**
- `secondLargest({10, 10, 9})` → **9**（最大值是 10，第二大是 9）
- `secondLargest({5})` → `Integer.MIN_VALUE`

> 解答請見：`answer-key.md`
