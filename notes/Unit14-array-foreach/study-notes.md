# Unit 14：Array 遍歷 — 增強式 `for` 迴圈（for-each）

## 學習目標
- 掌握增強式 for 迴圈（Enhanced for loop / for-each）
- 理解 for-each 的使用限制
- 能判斷何時用 for-each，何時用標準 for

---

## 概念說明

**增強式 for 迴圈**語法更簡潔，適合**唯讀遍歷**。

```java
for (型別 變數 : 陣列) {
    // 使用 變數
}
```

範例：
```java
int[] nums = {3, 7, 1, 9, 4};
for (int n : nums) {
    System.out.print(n + " ");
}
// 輸出：3 7 1 9 4
```

---

## for-each vs 標準 for 比較

| 比較項目 | 標準 for | for-each |
|---------|---------|---------|
| 取得索引 | ✅ | ❌ |
| 修改元素 | ✅（`arr[i]=`）| ❌（修改變數不影響陣列）|
| 逆向遍歷 | ✅ | ❌ |
| 語法複雜度 | 較高 | 較低 |
| 適用場景 | 需索引/修改 | 純讀取 |

---

## for-each 修改失效的原因

迭代變數是元素的**副本**（primitive type），修改副本不影響原始陣列。

```java
// ❌ 不會影響原始陣列
for (int n : nums) {
    n *= 2;  // 只修改了本地變數 n
}

// ✅ 必須用標準 for
for (int i = 0; i < nums.length; i++) {
    nums[i] *= 2;
}
```

---

## 程式碼範例

```java
// for-each 計算總和（✅ 正確用法）
int sum = 0;
for (int n : nums) {
    sum += n;
}

// String 陣列 for-each
String[] names = {"Alice", "Bob", "Charlie"};
for (String name : names) {
    System.out.println("Hello, " + name + "!");
}
```

---

## 練習題

### Easy：用 for-each 找最大值
陣列：`{15, 42, 8, 27, 99, 3}` → 99

### Easy：用 for-each 判斷所有元素是否為正數
撰寫方法 `allPositive(int[] arr)` 回傳 `boolean`

---

## 現在試試看
使用 for-each 計算 `double[]` 陣列中所有元素的乘積
