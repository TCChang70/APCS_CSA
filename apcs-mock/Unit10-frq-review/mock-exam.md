# Unit 10：Iteration 綜合練習與 FRQ 準備 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. 總和計算
```java
int sum = 0;
for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
        sum += i;
    }
}
此程式計算的是？
(A) 1-100 中 3 的倍數和
(B) 1-100 中 5 的倍數和
(C) 1-100 中 3 或 5 的倍數和
(D) 1-100 中所有數的和
```

### 2. 巢狀迴圈效能
若外層迴圈執行 n 次，內層也執行 n 次，時間複雜度為？
(A) O(n)  (B) O(n²)  (C) O(log n)  (D) O(2ⁿ)

### 3. 方法回傳值
```java
public static String repeat(char c, int n) {
    String result = "";
    for (int i = 0; i < n; i++) {
        result += c;
    }
    return result;
}

repeat('*', 5) 回傳值為何？
(A) "*****"  (B) "*"  (C) "******"  (D) "5"
```
### 4. 密碼驗證
```
下列密碼符合「長度≥8、含大寫、含數字」規則的是？
(A) "abcdefgh"  (B) "Abcdefgh"  (C) "Abcd1234"  (D) "abcd1234"
```
### 5. 綜合 FRQ 題型
```
APCS FRQ 中，關於迭代（Iteration）最常見的題型不包括？
(A) 累加/計數  (B) 字串逐字元處理  (C) 遞迴函數  (D) 搜尋（找第一個）
```
---

## 程式實作（5 分）

### FRQ：密碼驗證（綜合題）
撰寫方法驗證密碼是否符合以下所有規則：

```java
public static boolean isValidPassword(String password)
```

規則：
1. 長度介於 8 到 20 個字元之間（含）
2. 至少包含一個大寫字母
3. 至少包含一個小寫字母
4. 至少包含一個數字
5. **不能**包含空格

全部符合回傳 `true`，否則回傳 `false`。

**範例：**
- `isValidPassword("P@ssw0rd")` → true
- `isValidPassword("pass word")` → false（含空格）
- `isValidPassword("ABC12345")` → false（無小寫）

> 解答請見：`answer-key.md`
