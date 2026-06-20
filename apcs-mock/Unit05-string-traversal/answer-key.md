# Unit 05 解答與解析

---

## 選擇題解答

| 題號 | 答案 | 解析 |
|------|------|------|
| 1 | **A** | `"APCS".length()` = 4，`charAt(2)` = 第三個字元 'C'（索引 0=A,1=P,2=C,3=S）。 |
| 2 | **A** | 'l' 出現在索引 2 和 3。輸出：2 3。 |
| 3 | **C** | 有效索引為 0-3，`charAt(4)` 超出範圍，拋出 `StringIndexOutOfBoundsException`。 |
| 4 | **B** | 從尾到頭：'C'(2), 'B'(1), 'A'(0) → "CBA"。 |
| 5 | **C** | A, P, C, S 全部是大寫字母，count = 4。 |

---

## FRQ 解答

```java
public static String shiftOne(String text) {
    String result = "";
    for (int i = 0; i < text.length(); i++) {
        char c = text.charAt(i);
        if (c == 'z') {
            result += 'a';
        } else if (c == 'Z') {
            result += 'A';
        } else if ((c >= 'a' && c < 'z') || (c >= 'A' && c < 'Z')) {
            result += (char) (c + 1);
        } else {
            result += c;  // 非字母不變
        }
    }
    return result;
}
```

**要點：** 處理 'z'→'a' 和 'Z'→'A' 的循環邊界。非字母字元直接保留。
