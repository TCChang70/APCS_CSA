# Unit 09 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **C** | A 和 B 都正確，B 的 `== true` 雖多餘但語法無誤。 |
| 2 | **A** | 1%3=1, 2%3=2, 3%3=0 → return true。 |
| 3 | **C** | 3+4+5+6 = 18。 |
| 4 | **B** | 正數有 3 和 5，count = 2。0 不是正數。 |
| 5 | **B** | Part (b) 典型模式是呼叫 Part (a) 的方法，如 `sumArray()` 算完總和後算平均。 |

---

## FRQ 解答

### Part (a)：質數判斷
```java
public static boolean isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
```

### Part (b)：統計質數個數（呼叫 isPrime）
```java
public static int countPrimes(int n) {
    int count = 0;
    for (int i = 2; i <= n; i++) {
        if (isPrime(i)) {
            count++;
        }
    }
    return count;
}
```

**要點：** Part (b) 直接重複使用 Part (a) 的 `isPrime()`，這是 APCS FRQ 的重要設計模式。
