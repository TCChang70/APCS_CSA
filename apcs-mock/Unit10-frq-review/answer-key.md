# Unit 10 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **C** | `i%3==0 || i%5==0` 表示 3 或 5 的倍數。 |
| 2 | **B** | 外層 n 次 × 內層 n 次 = n² 次，時間複雜度 O(n²)。 |
| 3 | **A** | 迴圈執行 5 次，每次加一個 '*'，結果為 "*****"。 |
| 4 | **C** | "Abcd1234" 長度 8、含大寫 A、含數字 1234。A 無大寫，B 無數字，D 無大寫。 |
| 5 | **C** | 遞迴函數不在 Unit 4 Iteration 的範圍內（屬於 Unit 10 Recursion）。 |

---

## FRQ 解答

```java
public static boolean isValidPassword(String password) {
    // 規則 1：長度 8-20
    if (password.length() < 8 || password.length() > 20) return false;

    boolean hasUpper = false;
    boolean hasLower = false;
    boolean hasDigit = false;

    for (int i = 0; i < password.length(); i++) {
        char c = password.charAt(i);

        // 規則 5：不能有空格
        if (c == ' ') return false;

        if (c >= 'A' && c <= 'Z') hasUpper = true;
        else if (c >= 'a' && c <= 'z') hasLower = true;
        else if (c >= '0' && c <= '9') hasDigit = true;
    }

    return hasUpper && hasLower && hasDigit;
}
```

**要點：** 邊檢查邊遍歷，一發現空格就立即 `return false` 提早結束。
