# Unit 07：`break` 與 `continue`

## 學習目標
- 理解 `break` 立即跳出迴圈的效果
- 理解 `continue` 跳過當次迭代的效果
- 辨別兩者在巢狀迴圈中的行為

---

## 概念說明

### `break`：立即離開整個迴圈
```java
for (int i = 0; i < 10; i++) {
    if (i == 5) break;  // i=5 時離開
    System.out.print(i + " ");
}
// 輸出：0 1 2 3 4
```

### `continue`：跳過本次迭代，繼續下一次
```java
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) continue;  // 跳過偶數
    System.out.print(i + " ");
}
// 輸出：1 3 5 7 9
```

---

## `break` vs `continue` vs `return` 比較

| 關鍵字 | 跳出範圍 | 常見用途 |
|--------|---------|---------|
| `break` | 目前迴圈 | 搜尋找到後停止 |
| `continue` | 本次迭代 | 跳過不符條件的元素 |
| `return` | 整個方法 | 找到後直接回傳 |

---

## 程式碼範例

### 範例 1：搜尋第一個負數（break）
```java
int[] nums = {4, 7, -2, 9, -5, 3};
int firstNeg = -1;
for (int i = 0; i < nums.length; i++) {
    if (nums[i] < 0) {
        firstNeg = nums[i];
        break;
    }
}
System.out.println("第一個負數：" + firstNeg);  // -2
```

### 範例 2：印出非空白字元（continue）
```java
String s = "A B C D";
for (int i = 0; i < s.length(); i++) {
    if (s.charAt(i) == ' ') continue;
    System.out.print(s.charAt(i));
}
// 輸出：ABCD
```

### 範例 3：break 在巢狀迴圈（只跳出內層）
```java
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (j == 1) break;  // 只跳出內層 for
        System.out.println("i=" + i + " j=" + j);
    }
}
```

---

## 練習題

### Easy：找 1-1000 中第一個大於 100 且能被 13 整除的數
輸出：104

### Hard：印出字串中每個字元的第一次出現位置
輸入：`"abcabc"`，只印出 a, b, c 首次出現的索引

---

## 現在試試看
改進質數判斷程式，找到因數後立即用 `break` 停止
