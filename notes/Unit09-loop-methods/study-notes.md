# Unit 09：迴圈與方法（Methods）整合

## 學習目標
- 將迴圈邏輯封裝進方法
- 理解方法回傳值與迴圈的配合
- 能分析含有方法呼叫的迴圈程式碼

---

## 方法設計原則
- 一個方法做一件事（Single Responsibility）
- 有意義的方法名稱（動詞 + 名詞）
- 參數設計：哪些值應作為參數

---

## 程式碼範例

### 範例 1：封裝累加邏輯
```java
public static int sum(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
        total += i;
    }
    return total;
}
// sum(10) → 55, sum(100) → 5050
```

### 範例 2：封裝質數判斷（在迴圈中呼叫）
```java
public static boolean isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

// 主程式中使用：
for (int i = 2; i <= 30; i++) {
    if (isPrime(i)) {
        System.out.print(i + " ");
    }
}
```

### 範例 3：封裝字串統計
```java
public static int countVowels(String s) {
    int count = 0;
    String vowels = "aeiouAEIOU";
    for (int i = 0; i < s.length(); i++) {
        if (vowels.indexOf(s.charAt(i)) >= 0) {
            count++;
        }
    }
    return count;
}
```

---

## 重要觀念

### 在迴圈中呼叫方法
- 可將方法呼叫放入迴圈條件或主體
- 注意每次呼叫的時間成本
- 避免在迴圈條件中做不必要的重複計算

### 提早 return 代替 break
在方法中，`return` 可以直接跳出整個方法，效果等同 `break` + 回傳值

---

## 練習題

### Medium：實作 `max(int a, int b, int c)`
回傳三個數中最大值，不使用 `Math.max()`

### Hard：實作整數反轉 `reverse(int n)`
輸入 12345 → 輸出 54321

---

## 現在試試看
撰寫 `sumOfSquares(int n)` 計算 1² + 2² + ... + n²
