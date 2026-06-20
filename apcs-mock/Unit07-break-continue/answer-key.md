# Unit 07 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **A** | i=0,1,2,3 正常輸出；i=4 時 break 跳出，輸出 0 1 2 3。 |
| 2 | **A** | i=1,3,5 時輸出（i%2≠0），i=2,4,6 被 continue 跳過。 |
| 3 | **A** | 外層 i=0：內層 j=0 輸出"00"，j=1 時 break→結束內層。同理 i=1→"10"，i=2→"20"。 |
| 4 | **B** | arr[0]=3≠2, arr[1]=7≠2, arr[2]=2==2 → return 2。 |
| 5 | **C** | i=1:sum=1, i=2:sum=3, i=3:sum=6, i=4:continue, i=5:sum=11, i=6:sum=17, i=7:sum=24, i=8:continue, i=9:sum=33>30→break。sum=33。 |

---

## FRQ 解答

```java
public static int nextPerfectSquare(int n) {
    int result = 0;
    for (int i = 1; ; i++) {
        result = i * i;
        if (result > n) {
            break;
        }
    }
    return result;
}
```

**要點：** 使用無限迴圈（或 `for (int i = 1; ; i++)`），當找到第一個大於 n 的完全平方數時用 break 終止。
