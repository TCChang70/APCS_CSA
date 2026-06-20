# Phase 2 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **B** | `product` 應初始化為 1，初始化為 0 會導致所有乘積結果都是 0。 |
| 2 | **A** | i=1,2 正常輸出；i=3 被 continue 跳過；i=4,5 正常；i=6 被 continue；i=7 正常輸出；i=8 時 `i > 7` 成立→break 終止。輸出：1 2 4 5 7 |
| 3 | **C** | 兩個錯誤：(1)`total=1` 應為 0（多算 1）；(2)`k<10` 應為 `k<=10`（少算 10）。 |
| 4 | **B** | 函數反轉整數：12345 → 54321（`r = r*10 + n%10` 逐位取出再重組）。 |
| 5 | **C** | gcd(54,24)：54%24=6 → gcd(24,6)：24%6=0 → 回傳 6。 |
| 6 | **A** | 第 3-10 項偶數和：2(Fib#3)+8(#6)+34(#9)=44。 |
| 7 | **B** | APCS FRQ 設計模式：Part (b) 通常可呼叫 Part (a) 的結果，避免重複實作。 |
| 8 | **B** | Off-by-one 最常見原因就是 `<` 與 `<=` 的混淆，檢查條件設計是最有效的除錯方式。 |

---

## FRQ 解答

### FRQ 1：完美數判斷

```java
public static boolean isPerfectNumber(int n) {
    if (n <= 1) return false;

    int sum = 0;
    for (int i = 1; i < n; i++) {
        if (n % i == 0) {
            sum += i;
        }
    }

    return sum == n;
}
```

**解題思路：**
- 從 1 到 n-1 找出所有因數（n % i == 0）
- 累加因數總和
- 比較總和是否等於 n
- 優化：因數成對出現，可只跑到 sqrt(n) 來提升效率

---

### FRQ 2：Caesar 密碼加密

```java
public static String caesarCipher(String text, int shift) {
    String result = "";
    shift = shift % 26;  // 處理超過 26 的位移量

    for (int i = 0; i < text.length(); i++) {
        char c = text.charAt(i);

        if (c >= 'A' && c <= 'Z') {
            c = (char) ((c - 'A' + shift) % 26 + 'A');
        } else if (c >= 'a' && c <= 'z') {
            c = (char) ((c - 'a' + shift) % 26 + 'a');
        }
        // 非英文字母保持不變

        result += c;
    }

    return result;
}
```

**解題思路：**
- 先對 shift 取 mod 26，處理大幅位移的情況
- 分別處理大寫 (A-Z) 和小寫 (a-z)
- 使用公式 `(c - base + shift) % 26 + base` 實現循環位移
- 非英文字元直接保留，不做處理
