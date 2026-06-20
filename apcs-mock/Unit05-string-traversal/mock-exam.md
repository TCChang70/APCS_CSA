# Unit 05：String 字串遍歷 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. length() 與 charAt()
```java
String s = "APCS";
System.out.println(s.length());
System.out.println(s.charAt(2));
```
輸出為何？
(A) 4 和 C  (B) 4 和 S  (C) 3 和 C  (D) 4 和 A

### 2. 字串遍歷
```java
String s = "Hello";
for (int i = 0; i < s.length(); i++) {
    if (s.charAt(i) == 'l') {
        System.out.print(i + " ");
    }
}
```
輸出為何？
(A) 2 3  (B) 1 2  (C) 2  (D) 1

### 3. 索引越界
```java
String s = "Java";
System.out.println(s.charAt(4));
```
結果為何？
(A) 輸出 'a'  (B) 輸出空白  (C) 拋出例外  (D) 輸出 'v'

### 4. 反轉字串
```java
String s = "ABC";
String rev = "";
for (int i = s.length() - 1; i >= 0; i--) {
    rev += s.charAt(i);
}
System.out.println(rev);
```
輸出為何？
(A) "ABC"  (B) "CBA"  (C) "C"  (D) "ABCD"

### 5. 字元比較
```java
String s = "APCS";
int count = 0;
for (int i = 0; i < s.length(); i++) {
    if (s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') {
        count++;
    }
}
System.out.println(count);
```
輸出為何？
(A) 1  (B) 2  (C) 4  (D) 0

---

## 程式實作（5 分）

### FRQ：字元移位加密
撰寫方法，將字串中每個英文字母向後位移 1 個位置（a→b, b→c, ..., z→a），非字母字元不變。

```java
public static String shiftOne(String text)
```

**提示：** 注意邊界情況 'z' 和 'Z' 要循環回 'a' 和 'A'。

**範例：**
- `shiftOne("abc")` → "bcd"
- `shiftOne("zoo")` → "app"
- `shiftOne("Hello!")` → "Ifmmp!"

> 解答請見：`answer-key.md`
