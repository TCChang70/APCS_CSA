# Phase 3 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **C** | III 錯誤：在宣告變數之後不能使用 `{}` 初始化，必須用 `new int[]{1, 2, 3}`。 |
| 2 | **B** | `arr.length` = 5（長度），`arr[arr.length-2]` = `arr[3]` = 40（倒數第二個）。 |
| 3 | **C** | 陣列是參考型別，方法內修改 `x[0]` 會直接影響原始陣列 `arr`。 |
| 4 | **A** | for-each 的迭代變數 n 是元素的「副本」，修改 n 不影響原始陣列 `nums[0]` 仍為 5。 |
| 5 | **D** | 初始化 max=3，遍歷：7>3→max=7，2 不變，9>7→max=9，4 不變。最終 max=9。 |
| 6 | **B** | 線性搜尋從索引 0 開始：arr[0]=5≠8, arr[1]=3≠8, arr[2]=8==8 → 回傳 2。 |
| 7 | **B** | III `nums[4]` 超出範圍 (0-3)，IV 負數索引也無效。I 和 II 都合法。 |
| 8 | **B** | `boolean` 陣列預設值為 `false`。 |

---

## FRQ 解答

### FRQ 1：陣列統計

```java
public static double analyzeGrades(int[] grades) {
    // 步驟 1：計算總平均值
    double sum = 0;
    for (int grade : grades) {
        sum += grade;
    }
    double average = sum / grades.length;

    // 步驟 2：找出高於平均的成績
    double aboveSum = 0;
    int aboveCount = 0;
    for (int grade : grades) {
        if (grade > average) {
            aboveSum += grade;
            aboveCount++;
        }
    }

    // 步驟 3：計算高於平均的成績的平均值
    if (aboveCount == 0) return 0.0;
    return aboveSum / aboveCount;
}
```

**解題思路：**
- 需兩次遍歷：第一次算總平均，第二次找出高於平均的成績
- 注意 type casting：`sum` 用 `double` 避免整數除法
- 邊界情況：所有成績相同 → aboveCount=0 → 回傳 0.0

---

### FRQ 2：陣列壓縮

```java
public static int[] compress(int[] arr, int k) {
    int newLength = (arr.length + k - 1) / k;
    int[] result = new int[newLength];

    int index = 0;
    for (int i = 0; i < arr.length; i += k) {
        int sum = 0;
        int count = 0;
        for (int j = i; j < i + k && j < arr.length; j++) {
            sum += arr[j];
            count++;
        }
        result[index] = sum;
        index++;
    }

    return result;
}
```

**解題思路：**
- 新陣列長度公式：`(arr.length + k - 1) / k`（無條件進位）
- 外層迴圈以 `k` 為步進，每組的起始索引
- 內層迴圈加總當前組的元素，需檢查 `j < arr.length` 避免最後一組越界
- `count` 變數記錄實際加了幾個元素（可選，本題不需要平均值）

**另一種寫法（不使用巢狀迴圈）：**

```java
public static int[] compress(int[] arr, int k) {
    int newLength = (arr.length + k - 1) / k;
    int[] result = new int[newLength];

    for (int i = 0; i < arr.length; i++) {
        result[i / k] += arr[i];
    }

    return result;
}
```

這個寫法更簡潔：`i / k` 自動決定每個元素屬於第幾組（整數除法），不需要巢狀迴圈。
