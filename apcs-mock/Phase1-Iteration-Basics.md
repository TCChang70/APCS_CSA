# APCS CSA 模擬練習 — Phase 1：Iteration 基礎

> **涵蓋單元：** Unit 01–05（while、for、控制變數、巢狀迴圈、String 遍歷）  
> **題型：** 選擇題 (MCQ) + 程式實作題 (FRQ)  
> **總分：** 40 分 | **建議時間：** 60 分鐘

---

## 第一部分：選擇題（每題 3 分，共 24 分）

---

### 1. while 迴圈執行次數

下列程式碼執行後，`count` 的值為何？

```java
int count = 0;
int i = 1;
while (i < 10) {
    count++;
    i += 2;
}

(A) 4  
(B) 5  
(C) 9  
(D) 10  
```
---

### 2. for 迴圈語法

下列哪個 for 迴圈的寫法會產生編譯錯誤？

```java
// I
for (int i = 0; i < 10; i++) { }

// II
for (int i = 0; i < 10; i--) { }

// III
for (int i = 0, j = 0; i < 10; i++) { }

// IV
for (int i = 0; i < 10; i++;) { }


(A) 只有 I  
(B) 只有 II  
(C) 只有 III  
(D) 只有 IV  
```
---

### 3. Off-by-one 錯誤

下列程式碼欲計算 `1 + 2 + ... + n`，其中 `n = 100`，但結果不正確。請問總和少了多少？

```java
int n = 100;
int sum = 0;
for (int i = 1; i < n; i++) {
    sum += i;
}

(A) 0  
(B) 50  
(C) 100  
(D) 101  
```
---

### 4. 巢狀迴圈追蹤

執行下列程式碼後，`count` 的值為何？

```java
int count = 0;
for (int i = 0; i < 5; i++) {
    for (int j = 0; j <= i; j++) {
        count++;
    }
}

(A) 10  
(B) 15  
(C) 20  
(D) 25  
```
---

### 5. String 遍歷

下列程式碼執行後的輸出為何？

```java
String s = "APCS";
String result = "";
for (int i = s.length() - 1; i >= 0; i--) {
    result += s.charAt(i);
}
System.out.println(result);

(A) "APCS"  
(B) "SCPA"  
(C) "APC"  
(D) "SPC"  
```
---

### 6. for-each vs 標準 for
```
關於 `for-each`（增強式 for 迴圈）的敘述，下列何者**錯誤**？

(A) 無法取得目前元素的索引位置  
(B) 無法修改陣列中的元素值  
(C) 可以逆向遍歷陣列  
(D) 語法比標準 for 更簡潔  
```
---

### 7. 跳出巢狀迴圈

執行下列程式碼後，`sum` 的值為何？

```java
int sum = 0;
outer:
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (i == j) break outer;
        sum += i * j;
    }
}

(A) 0  
(B) 1  
(C) 2  
(D) 4  
```
---

### 8. 方法 + 迴圈

```java
public static int mystery(int n) {
    int result = 0;
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            result += i;
        }
    }
    return result;
}

mystery(10) 的回傳值為何？

(A) 20  
(B) 25  
(C) 30  
(D) 55  
```
---

## 第二部分：程式實作題（共 16 分）

---

### FRQ 1：字串分析 (8 分)

撰寫完整方法：

```java
public static int countWordLength(String sentence, int n)
```

計算字串 `sentence` 中，長度「大於等於 n」的單字數量。

- 單字以空格分隔
- 假設句子中不會有連續空格
- 不考慮標點符號

**範例：**
- `countWordLength("Hello world Java", 4)` → 3（Hello=5, world=5, Java=4，全部 ≥ 4）
- `countWordLength("A B C D", 2)` → 0（全部長度為 1，小於 2）

---

### FRQ 2：密碼強度檢查 (8 分)

撰寫完整方法：

```java
public static String passwordStrength(String password)
```

根據以下規則回傳密碼強度等級：

| 條件 | 分數 |
|------|------|
| 長度 ≥ 8 | +1 分 |
| 含大寫字母 (A-Z) | +1 分 |
| 含小寫字母 (a-z) | +1 分 |
| 含數字 (0-9) | +1 分 |
| 含特殊符號（非字母數字）| +1 分 |

- 總分 0-2 分 → 回傳 `"Weak"`
- 總分 3-4 分 → 回傳 `"Medium"`
- 總分 5 分 → 回傳 `"Strong"`

**範例：**
- `passwordStrength("abc")` → "Weak"（長度不足，只有小寫：1 分）
- `passwordStrength("Abc123!")` → "Medium"（長度=7：0；大寫：1；小寫：1；數字：1；特殊：1 → 4 分）
- `passwordStrength("P@ssw0rd")` → "Strong"（長度≥8：1；大寫：1；小寫：1；數字：1；特殊：1 → 5 分）

---

> 解答請見：`apcs-mock/Phase1-AnswerKey.md`
