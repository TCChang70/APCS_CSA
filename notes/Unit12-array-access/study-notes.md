# Unit 12：Array 元素存取與修改

## 學習目標
- 正確讀取與修改陣列元素
- 理解 `ArrayIndexOutOfBoundsException`
- 理解陣列是參考型別（Reference Type）

---

## 概念說明

### 讀取與修改
```java
int[] nums = {5, 10, 15, 20, 25};
nums[2] = 99;                          // 修改
System.out.println(nums[2]);           // 99
System.out.println(nums[nums.length - 1]);  // 最後一個
```

### 參考型別（Reference Type）
陣列是參考型別，傳入方法時傳的是**記憶體位址**。

```java
public static void doubleAll(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        arr[i] *= 2;
    }
}

int[] scores = {10, 20, 30};
doubleAll(scores);
System.out.println(scores[0]);  // 20（已被修改！）
```

### 賦值不是複製！
```java
int[] alias = original;            // ❌ 同一個陣列（別名）
int[] copy = original.clone();     // ✅ 獨立副本
```

---

## 程式碼範例

### 批量修改（將負數改為 0）
```java
int[] data = {3, -1, 7, -4, 0, -2};
for (int i = 0; i < data.length; i++) {
    if (data[i] < 0) {
        data[i] = 0;
    }
}
// data = {3, 0, 7, 0, 0, 0}
```

### 元素交換（Swap）
```java
int temp = arr[0];
arr[0] = arr[arr.length - 1];
arr[arr.length - 1] = temp;
```

---

## 練習題

### Easy：交換首尾元素
輸入 `{1, 2, 3, 4, 5}` → 輸出 `{5, 2, 3, 4, 1}`

### Medium：將所有元素加上偏移量
撰寫 `addOffset(int[] arr, int offset)` 就地修改

---

## 現在試試看
撰寫 `reverse(int[] arr)` 原地反轉陣列（不建立新陣列）
