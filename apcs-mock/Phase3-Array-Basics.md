# APCS CSA 模擬練習 — Phase 3：Array 基礎

> **涵蓋單元：** Unit 11–15（宣告初始化、存取修改、標準 for、for-each、基礎演算法）  
> **題型：** 選擇題 (MCQ) + 程式實作題 (FRQ)  
> **總分：** 40 分 | **建議時間：** 60 分鐘

---

## 第一部分：選擇題（每題 3 分，共 24 分）

---

### 1. 陣列初始化

下列哪個陣列初始化方式會產生**編譯錯誤**？

```java
// I
int[] a = new int[5];

// II
int[] b = {1, 2, 3, 4, 5};

// III
int[] c;
c = {1, 2, 3};

// IV
int[] d;
d = new int[]{1, 2, 3};


(A) 只有 I  
(B) 只有 II  
(C) 只有 III  
(D) 只有 IV  
```
---

### 2. 陣列長度與索引

下列程式碼執行後的輸出為何？

```java
int[] arr = {10, 20, 30, 40, 50};
System.out.println(arr.length);
System.out.println(arr[arr.length - 2]);


(A) 5 然後 30  
(B) 5 然後 40  
(C) 4 然後 30  
(D) 4 然後 40  
```
---

### 3. 參考型別

執行下列程式碼後，`arr[0]` 的值為何？

```java
public static void modify(int[] x) {
    x[0] = 99;
}

public static void main(String[] args) {
    int[] arr = {1, 2, 3};
    modify(arr);
    System.out.println(arr[0]);
}


(A) 1  
(B) 2  
(C) 99  
(D) 編譯錯誤  
```
---

### 4. for-each 修改

執行下列程式碼後，`nums[0]` 的值為何？

```java
int[] nums = {5, 10, 15};
for (int n : nums) {
    n *= 2;
}
System.out.println(nums[0]);


(A) 5  
(B) 10  
(C) 15  
(D) 編譯錯誤  
```
---

### 5. 陣列遍歷 — 最大值

執行下列程式碼後，`max` 的值為何？

```java
int[] data = {3, 7, 2, 9, 4};
int max = data[0];
for (int i = 1; i < data.length; i++) {
    if (data[i] > max) {
        max = data[i];
    }
}


(A) 2  
(B) 3  
(C) 7  
(D) 9  
```
---

### 6. 線性搜尋

```java
public static int search(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

search({5, 3, 8, 1, 9}, 8) 的回傳值為何？

(A) 1  
(B) 2  
(C) 3  
(D) -1  
```
---

### 7. ArrayIndexOutOfBoundsException

下列哪行程式碼會拋出 `ArrayIndexOutOfBoundsException`？

```java
int[] nums = new int[4];
// I:  nums[0] = 10;
// II: nums[3] = 20;
// III: nums[4] = 30;
// IV: nums[-1] = 40;


(A) 只有 III  
(B) III 和 IV  
(C) 只有 IV  
(D) 都不會拋出例外  
```
---

### 8. 陣列預設值

```java
boolean[] flags = new boolean[3];
System.out.println(flags[0]);

輸出為何？

(A) 0  
(B) false  
(C) null  
(D) true  
```
---

## 第二部分：程式實作題（共 16 分）

---

### FRQ 1：陣列統計 (8 分)

撰寫完整方法：

```java
public static double analyzeGrades(int[] grades)


給定學生成績陣列（0-100 的整數），計算並回傳「高於平均分的成績之平均值」。

步驟：
1. 計算所有成績的平均值
2. 找出所有高於此平均值的成績
3. 計算這些成績的平均值並回傳

如果沒有任何成績高於平均，回傳 `0.0`。

**範例：**
- `analyzeGrades({80, 90, 70})` → 平均 = 80，高於 80 的有 {90} → 回傳 90.0
- `analyzeGrades({60, 60, 60})` → 平均 = 60，無成績高於 60 → 回傳 0.0
- `analyzeGrades({85, 90, 78, 92, 88})` → 平均 ≈ 86.6，高於的有 {90, 92, 88} → 回傳 90.0
```
---

### FRQ 2：陣列壓縮 (8 分)

撰寫完整方法：

```java
public static int[] compress(int[] arr, int k)

將陣列中每 `k` 個一組相加，產生一個新的較短陣列。

- 如果陣列長度不是 k 的倍數，最後一組可能不足 k 個元素
- 回傳的新陣列長度為 `(arr.length + k - 1) / k`

**範例：**
- `compress({1, 2, 3, 4, 5, 6}, 2)` → 每 2 個一組：(1+2)=3, (3+4)=7, (5+6)=11 → `{3, 7, 11}`
- `compress({1, 2, 3, 4, 5}, 3)` → 每 3 個一組：(1+2+3)=6, (4+5)=9 → `{6, 9}`
- `compress({1, 2, 3, 4}, 4)` → `{10}`
- `compress({1, 2, 3, 4, 5}, 5)` → `{15}`
```

---

> 解答請見：`apcs-mock/Phase3-AnswerKey.md`
