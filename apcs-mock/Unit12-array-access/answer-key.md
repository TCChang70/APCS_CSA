# Unit 12 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **C** | `arr[1] = 99` 將索引 1 的元素改為 99。 |
| 2 | **B** | 陣列是參考型別，方法內修改 `x[0]` = 100 影響原始陣列。 |
| 3 | **B** | `alias` 和 `original` 指向同一個陣列物件，透過 alias 修改會影響 original。 |
| 4 | **B** | 索引 1 的 -1 改為 0，索引 3 的 -2 改為 0。輸出 0 0。 |
| 5 | **C** | `arr[0]=arr[1]` → arr = {10,10}，然後 `arr[1]=arr[0]` → arr = {10,10}。忘記用 temp 變數。 |

---

## FRQ 解答

```java
public static void shiftRight(int[] arr, int k) {
    int n = arr.length;
    k = k % n;  // 處理 k ≥ n 的情況
    if (k == 0) return;

    // 反轉整個陣列
    reverse(arr, 0, n - 1);
    // 反轉前 k 個
    reverse(arr, 0, k - 1);
    // 反轉剩餘的
    reverse(arr, k, n - 1);
}

// 輔助方法：反轉陣列的指定範圍
public static void reverse(int[] arr, int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}
```

**要點：** 使用三段反轉法（0~n-1, 0~k-1, k~n-1）實現陣列平移。
