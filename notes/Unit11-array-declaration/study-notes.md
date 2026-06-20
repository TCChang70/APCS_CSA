# Unit 11：Array 宣告與初始化

## 學習目標
- 理解陣列的概念：連續記憶體、固定大小、同型別
- 掌握三種宣告與初始化方式
- 理解 `length` 屬性與預設值

---

## 概念說明

陣列是**相同型別**元素的**固定大小**有序集合，索引從 **0** 開始。

```
int[] scores = new int[5];
索引：      0    1    2    3    4
值：        0    0    0    0    0  （預設值）
```

### 各型別的預設值

| 型別 | 預設值 |
|------|--------|
| `int` | `0` |
| `double` | `0.0` |
| `boolean` | `false` |
| `String`/Object | `null` |

---

## 三種初始化方式

### 方式 1：只宣告大小
```java
int[] nums = new int[5];  // 元素使用預設值 0
```

### 方式 2：宣告並指定初始值
```java
int[] scores = {85, 90, 78, 92, 88};  // 大小自動為 5
```

### 方式 3：先宣告後賦值
```java
int[] data;
data = new int[]{10, 20, 30};
```

---

## 重要：`length` 屬性

```java
int[] arr = {10, 20, 30};
System.out.println(arr.length);    // 3（屬性，無括號）
// String 用 length()（方法，有括號）
String s = "Hello";
System.out.println(s.length());    // 5
// 最後一個元素
System.out.println(arr[arr.length - 1]);  // 30
```

### 有效索引範圍
- 第一個元素：`arr[0]`
- 最後一個元素：`arr[arr.length - 1]`
- 索引越界：`arr[arr.length]` → `ArrayIndexOutOfBoundsException`

---

## 練習題

### Easy：宣告陣列，印出首元素、末元素、長度
陣列：`{10, 20, 30, 40, 50}`

### Easy：用迴圈填入偶數到陣列
建立大小為 5 的陣列，填入 2, 4, 6, 8, 10

---

## 現在試試看
建立一個陣列儲存你的 5 門課成績，印出索引與成績對照
