# Unit 14 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **A** | 正確語法：`for (型別 變數 : 陣列)`。A 是最標準的寫法。 |
| 2 | **C** | 2+4+6+8 = 20。 |
| 3 | **B** | `x` 是元素的副本，修改 `x` 不影響原始陣列，`data[0]` 仍為 1。 |
| 4 | **B** | 修改元素需要索引（`arr[i]=值`），for-each 無法做到。其餘選項都是純讀取。 |
| 5 | **B** | 對每個 w：輸出 w+w+空格 → "AA BB CC "。 |

---

## FRQ 解答

```java
public static boolean hasAdjacentSumGreaterThan(int[] arr, int threshold) {
    if (arr.length < 2) return false;

    int prev = arr[0];
    boolean first = true;

    for (int current : arr) {
        if (first) {
            first = false;
            continue;  // 跳過第一個元素
        }
        if (prev + current > threshold) {
            return true;
        }
        prev = current;
    }

    return false;
}
```

**要點：** 用 `prev` 變數追蹤前一個元素的值。第一個元素先存到 prev，從第二個元素開始比較。

**另一種寫法（用 index）：** 因為需要追蹤相鄰元素，本題使用標準 for 更自然。但題目要求 for-each，所以用 `prev` 變數追蹤。
