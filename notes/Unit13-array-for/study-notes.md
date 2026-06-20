# Unit 13：Array 遍歷 — 標準 `for` 迴圈

## 學習目標
- 使用標準 `for` 迴圈遍歷陣列
- 掌握累加、計數、搜尋等遍歷模式
- 能用索引進行相鄰元素比較

---

## 基本遍歷模式

```java
for (int i = 0; i < arr.length; i++) {
    // 使用 arr[i]
}
```

---

## 四大遍歷應用模式

| 模式 | 初始化 | 核心操作 |
|------|--------|---------|
| 印出所有元素 | — | `System.out.println(arr[i])` |
| 累加 / 平均 | `sum = 0` | `sum += arr[i]` |
| 計數（符合條件） | `count = 0` | `if (...) count++` |
| 找最大值 | `max = arr[0]` | `if (arr[i] > max) max = arr[i]` |

---

## 程式碼範例

```java
int[] scores = {85, 90, 78, 92, 88, 76, 95};

// 印出所有元素（含索引）
for (int i = 0; i < scores.length; i++) {
    System.out.println("scores[" + i + "] = " + scores[i]);
}

// 計算總和與平均
int sum = 0;
for (int i = 0; i < scores.length; i++) sum += scores[i];
double avg = (double) sum / scores.length;

// 找最大值（從索引 1 開始）
int max = scores[0];
for (int i = 1; i < scores.length; i++) {
    if (scores[i] > max) max = scores[i];
}

// 計算 80 分以上人數
int passCount = 0;
for (int i = 0; i < scores.length; i++) {
    if (scores[i] >= 80) passCount++;
}
```

### 索引的特殊用法
- 從索引 1 開始（最大值初始化後）
- 相鄰元素比較（`arr[i]` vs `arr[i+1]`）
- 反向遍歷（從 `arr.length - 1` 到 0）

---

## 練習題

### Easy：撰寫 `min(int[] arr)` 方法回傳最小值

### Hard：撰寫 `hasDuplicate(int[] arr)` 判斷是否有重複值

---

## 現在試試看
找最大值的索引（回傳索引不是值，多個最大值取第一個）
