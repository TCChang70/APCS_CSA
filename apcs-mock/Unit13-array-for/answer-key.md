# Unit 13 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **B** | 2+4+6+8 = 20。基本累加遍歷。 |
| 2 | **C** | 從索引 1 開始比較：85>72→max=85, 90>85→max=90, 68<90, 88<90。最終 max=90。 |
| 3 | **B** | 大於 10 的有：12, 18, 15 → count=3。 |
| 4 | **B** | 從索引 3 到 0：40, 30, 20, 10。 |
| 5 | **C** | 比較：1<3→count++, 3>2→不計, 2<5→count++, 5>4→不計。count=2。 |

---

## FRQ 解答

```java
public static int range(int[] arr) {
    int max = arr[0];
    int min = arr[0];
    for (int i = 1; i < arr.length; i++) {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
    }
    return max - min;
}
```

**要點：** 一次遍歷同時找最大值和最小值，再回傳兩者差。
