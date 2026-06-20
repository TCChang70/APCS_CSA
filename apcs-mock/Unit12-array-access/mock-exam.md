# Unit 12：Array 元素存取與修改 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. 修改元素
```java
int[] arr = {1, 2, 3};
arr[1] = 99;
System.out.println(arr[1]);
```
輸出為何？
(A) 1  (B) 2  (C) 99  (D) 3

### 2. 參考型別
```java
public static void change(int[] x) {
    x[0] = 100;
}

public static void main(String[] args) {
    int[] a = {1, 2, 3};
    change(a);
    System.out.println(a[0]);
}
```
輸出為何？
(A) 1  (B) 100  (C) 2  (D) 編譯錯誤

### 3. 賦值陷阱
```java
int[] original = {1, 2, 3};
int[] alias = original;
alias[0] = 99;
System.out.println(original[0]);
```
輸出為何？
(A) 1  (B) 99  (C) 0  (D) 編譯錯誤

### 4. 就地修改
```java
int[] nums = {3, -1, 5, -2, 0};
for (int i = 0; i < nums.length; i++) {
    if (nums[i] < 0) {
        nums[i] = 0;
    }
}
System.out.println(nums[1] + " " + nums[3]);
```
輸出為何？
(A) -1 -2  (B) 0 0  (C) 0 -2  (D) -1 0

### 5. 交換錯誤
```java
int[] arr = {5, 10};
arr[0] = arr[1];  // 想交換但寫錯了
arr[1] = arr[0];
System.out.println(arr[0] + " " + arr[1]);
```
輸出為何？
(A) 5 10  (B) 10 5  (C) 10 10  (D) 5 5

---

## 程式實作（5 分）

### FRQ：陣列平移
撰寫方法，將陣列中所有元素向右平移 k 個位置（最後 k 個元素移到開頭）。

```java
public static void shiftRight(int[] arr, int k)
```

**就地修改**，不要建立新陣列。

**提示：** 先將整個陣列反轉，再分段反轉。

**範例：**
- `shiftRight({1, 2, 3, 4, 5}, 2)` → `{4, 5, 1, 2, 3}`
- `shiftRight({1, 2, 3, 4, 5}, 1)` → `{5, 1, 2, 3, 4}`

> 解答請見：`answer-key.md`
