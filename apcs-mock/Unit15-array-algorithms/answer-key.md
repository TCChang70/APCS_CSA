# Unit 15 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **D** | for-each 可以實作找最大值：`for (int n : arr) { if (n > max) max = n; }`。 |
| 2 | **A** | 從索引 1 開始比較：3<8→min=3, 5>3, 1<3→min=1, 7>1。最終 min=1。 |
| 3 | **B** | 逐一檢查：arr[0]=4, arr[1]=2, arr[2]=7==7 → return 2。 |
| 4 | **B** | sum=100，`(double)100/4 = 25.0`。注意轉型避免整數除法。 |
| 5 | **C** | 最差情況：目標在最後一個或不存在，需檢查全部 n 個元素 → O(n)。 |

---

## FRQ 解答

```java
public static int secondLargest(int[] arr) {
    if (arr.length < 2) return Integer.MIN_VALUE;

    int max = Integer.MIN_VALUE;
    int second = Integer.MIN_VALUE;

    for (int val : arr) {
        if (val > max) {
            second = max;
            max = val;
        } else if (val > second && val < max) {
            second = val;
        }
    }

    return second;
}
```

**要點：**
- 初始化為 `Integer.MIN_VALUE` 能處理所有整數情況（包含負數）
- 當發現比目前最大值更大的值時，將舊 max 降為 second
- 用 `val < max` 確保相同最大值不會被當作第二大
