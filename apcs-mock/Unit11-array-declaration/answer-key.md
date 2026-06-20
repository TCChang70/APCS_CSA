# Unit 11 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **C** | 變數宣告後不能直接用 `{}` 賦值，必須用 `new int[]{1,2,3}`。 |
| 2 | **B** | `double` 陣列預設值為 `0.0`。 |
| 3 | **B** | `arr.length` = 4（陣列長度），`arr[3]` = 8（最後一個元素）。 |
| 4 | **A** | 長度 10，索引 0-9，最後一個是 `nums[9]`。 |
| 5 | **B** | `i <= data.length` 使 i 跑 0,1,2,3，當 i=3 時 `data[3]` 超出索引範圍（有效 0-2）。 |

---

## FRQ 解答

```java
public static int[] generateArray(int n, int start, int step) {
    int[] result = new int[n];
    int value = start;
    for (int i = 0; i < n; i++) {
        result[i] = value;
        value += step;
    }
    return result;
}
```

**要點：** 先配置長度 n 的陣列，再用迴圈依序填入數值。
