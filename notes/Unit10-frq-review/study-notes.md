# Unit 10：Iteration 綜合練習與 FRQ 準備

## 學習目標
- 整合 Unit 1-9 的所有迴圈技巧
- 練習 APCS CSA FRQ 格式的回答
- 掌握迴圈在 FRQ 中的常見應用模式

---

## Unit 01-09 快速複習

### `while` vs `for` 選擇原則
- 已知次數 → `for`
- 條件驅動（如哨兵值）→ `while`

### 迴圈次數計算公式
- `for (int i = a; i <= b; i++)` → `b - a + 1` 次
- `for (int i = a; i < b; i++)` → `b - a` 次

### break / continue / return 比較

| 關鍵字 | 跳出範圍 | 常見用途 |
|--------|---------|---------|
| `break` | 目前迴圈 | 搜尋找到後停止 |
| `continue` | 本次迭代 | 跳過不符條件的元素 |
| `return` | 整個方法 | 找到後直接回傳 |

---

## APCS FRQ 迴圈題型分類

| 題型 | 頻率 | 關鍵技巧 |
|------|------|---------|
| 累加/計數 | ⭐⭐⭐⭐⭐ | 初始化在迴圈外 |
| 搜尋（找第一個） | ⭐⭐⭐⭐ | `break` 或提早 `return` |
| 字串逐字元處理 | ⭐⭐⭐⭐ | `charAt()` + `length()` |
| 巢狀迴圈比對 | ⭐⭐⭐ | 內外層索引分工 |
| 數學計算（GCD、次方） | ⭐⭐⭐ | 累乘、輾轉相除 |

---

## FRQ 答題格式規範
- 存取修飾詞（`public static`）
- 回傳型別（`int`、`boolean`、`String`）
- 參數命名（有意義）
- 不遺漏 `return` 語句

---

## FRQ 範例：密碼驗證

```java
public static boolean isValidPassword(String password) {
    if (password.length() < 8) return false;

    boolean hasUpper = false;
    boolean hasDigit = false;

    for (int i = 0; i < password.length(); i++) {
        char c = password.charAt(i);
        if (c >= 'A' && c <= 'Z') hasUpper = true;
        if (c >= '0' && c <= '9') hasDigit = true;
    }

    return hasUpper && hasDigit;
}
```

---

## 里程碑自我檢查清單

- [ ] 能不看筆記寫出 `while` 和 `for` 迴圈
- [ ] 能計算任意 `for` 迴圈的執行次數
- [ ] 能追蹤巢狀迴圈的變數值
- [ ] 能用迴圈處理 `String` 的每個字元
- [ ] 能正確使用 `break` 和 `continue`
- [ ] 能識別並修正常見的迴圈 bug
- [ ] 能將迴圈邏輯封裝進方法

---

## 現在試試看
撰寫方法判斷一個字串是否為「強密碼」（含大寫、小寫、數字、特殊符號，長度 ≥ 8）
