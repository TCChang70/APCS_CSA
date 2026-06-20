# Unit 05：String 字串遍歷

## 學習目標
- 使用迴圈逐一存取字串的每個字元
- 掌握 `charAt()`、`length()` 的用法
- 能進行字串搜尋、統計、反轉等操作

---

## 概念說明

字串索引從 **0** 開始。

```java
String s = "Hello";
// 索引：  0 1 2 3 4
// 字元：  H e l l o
```

### 關鍵方法

| 方法 | 說明 | 範例 |
|------|------|------|
| `s.length()` | 回傳字串長度 | `"Java".length()` → 4 |
| `s.charAt(i)` | 回傳索引 i 的字元 | `"Java".charAt(0)` → 'J' |
| `s.indexOf(c)` | 回傳字元第一次出現位置（找不到回傳 -1） | `"banana".indexOf('a')` → 1 |
| `s.substring(a,b)` | 回傳子字串（a 到 b-1） | `"Hello".substring(1,3)` → "el" |

---

## 程式碼範例

### 範例 1：印出每個字元
```java
String s = "Java";
for (int i = 0; i < s.length(); i++) {
    System.out.println(s.charAt(i));
}
```

### 範例 2：統計 'a' 出現次數
```java
String text = "banana";
int count = 0;
for (int i = 0; i < text.length(); i++) {
    if (text.charAt(i) == 'a') count++;
}
System.out.println("a 出現 " + count + " 次");  // 3
```

### 範例 3：反轉字串
```java
String original = "Hello";
String reversed = "";
for (int i = original.length() - 1; i >= 0; i--) {
    reversed += original.charAt(i);
}
System.out.println(reversed);  // olleH
```

### 範例 4：回文判斷
```java
String word = "racecar";
boolean isPalindrome = true;
for (int i = 0; i < word.length() / 2; i++) {
    if (word.charAt(i) != word.charAt(word.length() - 1 - i)) {
        isPalindrome = false;
    }
}
System.out.println(isPalindrome);  // true
```

---

## 常見錯誤

| 錯誤 | 說明 |
|------|------|
| `s.length()` vs `arr.length` | String 用 `length()`（有括號），Array 用 `length`（無括號）|
| 索引越界 | `s.charAt(s.length())` → 例外 |
| `==` 比較 String | `char` 可用 `==`，但 String 應用 `equals()` |

---

## 練習題

### Easy：統計字串中的大寫字母數
輸入：`"Hello World APCS"`，輸出：6

### Medium：移除字串中的所有母音（a,e,i,o,u，不分大小寫）
輸入：`"Hello World"`，輸出：`"Hll Wrld"`

---

## 現在試試看
撰寫方法判斷字串是否為回文（只考慮英文字母，忽略大小寫）
