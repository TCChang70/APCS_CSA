# Phase 1 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **B** | i = 1, 3, 5, 7, 9 → 共 5 次。條件 `i < 10`，當 i 變成 11 時停止。 |
| 2 | **D** | IV `for (int i = 0; i < 10; i++;)` 第三段 i++ 後面多了分號，編譯錯誤。 |
| 3 | **C** | `i < n` → i 只跑到 99，總和少了 100。正確應為 `i <= n`。 |
| 4 | **B** | i=0 內層 1 次 (j=0)，i=1 內層 2 次 (j=0,1)，依此類推。1+2+3+4+5 = 15。 |
| 5 | **B** | 從尾到頭遍歷：'S', 'C', 'P', 'A' → "SCPA"。 |
| 6 | **C** | for-each 無法逆向遍歷，因為無法控制索引。 |
| 7 | **A** | 當 i=0, j=0 時 `i == j` 成立，立即跳出 outer 標記的迴圈，sum 仍為 0。 |
| 8 | **C** | 1 到 10 的偶數總和：2+4+6+8+10 = 30。 |

---

## FRQ 解答

### FRQ 1：字串分析

```java
public static int countWordLength(String sentence, int n) {
    int count = 0;
    String currentWord = "";

    for (int i = 0; i < sentence.length(); i++) {
        char c = sentence.charAt(i);
        if (c == ' ') {
            if (currentWord.length() >= n) {
                count++;
            }
            currentWord = "";
        } else {
            currentWord += c;
        }
    }

    // 檢查最後一個單字
    if (currentWord.length() >= n) {
        count++;
    }

    return count;
}
```

**解題思路：**
- 逐字元遍歷字串，遇到空格時表示一個單字結束
- 判斷當前累積單字的長度是否 ≥ n
- 別忘了處理最後一個單字（句子結尾沒有空格）

---

### FRQ 2：密碼強度檢查

```java
public static String passwordStrength(String password) {
    int score = 0;

    if (password.length() >= 8) score++;

    boolean hasUpper = false;
    boolean hasLower = false;
    boolean hasDigit = false;
    boolean hasSpecial = false;

    for (int i = 0; i < password.length(); i++) {
        char c = password.charAt(i);
        if (c >= 'A' && c <= 'Z') hasUpper = true;
        else if (c >= 'a' && c <= 'z') hasLower = true;
        else if (c >= '0' && c <= '9') hasDigit = true;
        else hasSpecial = true;
    }

    if (hasUpper) score++;
    if (hasLower) score++;
    if (hasDigit) score++;
    if (hasSpecial) score++;

    if (score <= 2) return "Weak";
    else if (score <= 4) return "Medium";
    else return "Strong";
}
```

**解題思路：**
- 先檢查長度（最簡單的檢查，可先處理）
- 用四個 boolean flag 追蹤各類字元是否存在
- 遍歷一次字串即可設定所有 flag
- 避免巢狀 if-else 結構，使用 else if 確保每個字元只歸一類
