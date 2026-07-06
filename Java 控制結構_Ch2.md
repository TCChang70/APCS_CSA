# 📚 第二單元：控制結構 - 詳細教學內容

## 🎯 單元學習目標
- 理解程式流程控制的重要性
- 掌握條件判斷語句的使用
- 學會各種迴圈結構的應用
- 能夠解決複雜的邏輯問題
- 熟悉 Java 各類運算子與運算子優先順序

---

## 🔢 2.0 Java 運算子總覽

運算子是對變數或值進行運算的符號。

### **運算子分類一覽表**

| 類別 | 運算子 | 說明 |
|------|--------|------|
| 算術 | `+ - * / %` | 基本數學運算 |
| 指派 | `= += -= *= /= %=` | 將值賦予變數 |
| 一元 | `++ -- + - !` | 單一運算元操作 |
| 關係 | `== != > < >= <=` | 比較兩個值 |
| 邏輯 | `&& \|\| !` | 布林邏輯運算 |
| 三元 | `? :` | 簡化 if-else |
| 位元 | `& \| ^ ~ << >> >>>` | 位元層級操作 |
| 型別檢查 | `instanceof` | 檢查物件型別 |

### **算術運算子**
```java
int a = 15, b = 4;
System.out.println(a + b);   // 19
System.out.println(a - b);   // 11
System.out.println(a * b);   // 60
System.out.println(a / b);   // 3 (整數除法)
System.out.println(a % b);   // 3 (取餘數)
String s = "Java" + 17;      // Java17 (字串串接)
```

### **指派與一元運算子**
```java name=UnaryOperators.java
public class UnaryOperators {
    public static void main(String[] args) {
        int a = 5;
        System.out.println(a++);  // 5 (先取再加)
        System.out.println(++a);  // 7 (先加再取)
        int x = 10;  x += 5;     // x = 15
        x *= 2;                  // x = 30
        boolean flag = false;
        System.out.println(!flag); // true
    }
}
```
**口訣：**「前++ 先加再用；後++ 先用再加」

### **三元運算子**
```java
int score = 75;
String r = (score >= 60) ? "及格" : "不及格";
// 巢狀三元 (不建議過度使用)
String level = (score >= 90) ? "優" : (score >= 60) ? "中" : "差";
```

### **運算子優先順序（由高至低）**

| 優先級 | 運算子 | 說明 |
|--------|--------|------|
| 1 | `()` | 括號 |
| 2 | `++ -- + - !` | 一元運算子 |
| 3 | `* / %` | 乘除取餘 |
| 4 | `+ -` | 加減 |
| 5 | `< > <= >= instanceof` | 關係 |
| 6 | `== !=` | 相等 |
| 7 | `&&` | 邏輯 AND |
| 8 | `\|\|` | 邏輯 OR |
| 9 | `? :` | 三元 |
| 10 | `= += -= *= /= %=` | 指派 |

```java
int r = 5 + 3 * 2;          // 11 (* 優先)
boolean b = 10 > 5 && 3 < 7; // true (關係優先於邏輯)
int safe = (5 + 3) * 2;     // 16 (不確定就加括號)
```

### **複習小站 1 — 運算子**
1. `11 % 3` 的輸出？　A) 3　B) 2　C) 1　D) 3.67
2. `int x=5; x++` 後 x 的值？　A) 4　B) 5　C) 6　D) 7
3. `5 + 3 * 4` 的結果？　A) 32　B) 17　C) 23　D) 12
4. 哪個是短路邏輯運算子？　A) `&`　B) `|`　C) `&&`　D) `^`
5. `(10 > 5) ? "Yes" : "No"` 結果？　A) Yes　B) No　C) true　D) 錯誤

> 答案：1. B　2. C　3. B　4. C　5. A

---

## 🔀 2.1 條件判斷

### **為什麼需要條件判斷？**
程式需要根據不同情況做出不同的決定。

**生活比喻：**
```
如果下雨 → 帶雨傘；否則 → 不帶雨傘
如果成績 >= 60 → 及格；否則 → 不及格
```

### **基本 if-else**
```java name=BasicIfElse.java
import java.util.Scanner;

public class BasicIfElse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("請輸入年齡：");
        int age = sc.nextInt();
        if (age >= 18) {
            System.out.println("您已成年，可以投票！");
        } else {
            System.out.println("您未成年，還不能投票。");
        }
        sc.close();
    }
}
```

### **多重條件 if-else if-else**
```java name=MultipleConditions.java
import java.util.Scanner;

public class MultipleConditions {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("請輸入分數 (0-100)：");
        int score = sc.nextInt();
        if (score >= 90) {
            System.out.println("等級 A+ 優秀！");
        } else if (score >= 80) {
            System.out.println("等級 A 良好！");
        } else if (score >= 70) {
            System.out.println("等級 B 普通");
        } else if (score >= 60) {
            System.out.println("等級 C 及格");
        } else {
            System.out.println("等級 F 不及格");
        }
        sc.close();
    }
}
```

### **switch 條件語句**
```java name=SwitchDemo.java
import java.util.Scanner;

public class SwitchDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("請輸入星期 (1-7)：");
        int day = sc.nextInt();
        String name;
        switch (day) {
            case 1: name = "星期一"; break;
            case 2: name = "星期二"; break;
            case 3: name = "星期三"; break;
            case 4: name = "星期四"; break;
            case 5: name = "星期五"; break;
            case 6: name = "星期六"; break;
            case 7: name = "星期日"; break;
            default: name = "無效數字"; break;
        }
        System.out.println(day + " 是 " + name);

        // 穿透範例：季節判斷
        System.out.print("請輸入月份 (1-12)：");
        int m = sc.nextInt();
        switch (m) {
            case 3: case 4: case 5: System.out.println("🌸 春天"); break;
            case 6: case 7: case 8: System.out.println("☀️ 夏天"); break;
            case 9: case 10: case 11: System.out.println("🍂 秋天"); break;
            case 12: case 1: case 2: System.out.println("❄️ 冬天"); break;
            default: System.out.println("❌ 無效月份");
        }
        sc.close();
    }
}
```

### **比較運算子與字串比較**
```java name=ComparisonOperators.java
public class ComparisonOperators {
    public static void main(String[] args) {
        int a = 10, b = 20;
        System.out.println("a == b: " + (a == b));
        System.out.println("a != b: " + (a != b));
        System.out.println("a > b: " + (a > b));
        System.out.println("a < b: " + (a < b));
        System.out.println("a >= b: " + (a >= b));
        System.out.println("a <= b: " + (a <= b));

        // 字串比較 (重要！)
        String s1 = "Hello", s2 = "Hello";
        String s3 = new String("Hello");
        System.out.println("s1 == s2: " + (s1 == s2));         // true
        System.out.println("s1 == s3: " + (s1 == s3));         // false
        System.out.println("s1.equals(s3): " + s1.equals(s3)); // true
    }
}
```

### **邏輯運算子**
```java name=LogicalOperators.java
import java.util.Scanner;

public class LogicalOperators {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("年齡："); int age = sc.nextInt();
        System.out.print("有駕照? (true/false)："); boolean lic = sc.nextBoolean();
        System.out.print("收入(萬)："); double inc = sc.nextDouble();

        if (age >= 18 && lic) System.out.println("✅ 可開車");
        else System.out.println("❌ 不能開車");

        if (age >= 65 || inc < 30) System.out.println("✅ 符合優惠");
        else System.out.println("❌ 不符合優惠");

        if (!lic) System.out.println("⚠️ 建議考駕照");

        if ((age >= 18 && age <= 65) && (inc >= 20 && inc <= 100))
            System.out.println("✅ 可申請貸款");
        sc.close();
    }
}
```

### **巢狀條件**
```java name=NestedConditions.java
import java.util.Scanner;

public class NestedConditions {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("天氣 (sunny/rainy)：");
        String w = sc.next();
        System.out.print("溫度："); int t = sc.nextInt();

        if (w.equals("sunny")) {
            if (t > 30) System.out.println("炎熱，穿短袖多喝水");
            else if (t > 20) System.out.println("舒適，適合戶外活動");
            else System.out.println("涼爽，穿長袖");
        } else if (w.equals("rainy")) {
            System.out.println("下雨，帶雨具");
            if (t < 15) System.out.println("穿保暖衣物");
        } else {
            System.out.println("陰天，穿適中衣物");
        }
        sc.close();
    }
}
```

### **複習小站 2 — 條件判斷**
1. switch 的 `break` 功能？　A) 結束程式　B) 跳出 switch　C) 跳到 default　D) 重新執行
2. `if (score = 100)` 錯在哪？　A) 沒問題　B) 應改用 `==`　C) 不能比 100　D) 名稱錯誤
3. 字串比較用哪個方法？　A) `==`　B) `equals()`　C) `compare()`　D) `match()`
4. `true && false` 結果？　A) true　B) false　C) 編譯錯誤　D) 0
5. switch 的 default 何時執行？　A) 永遠　B) 無 case 符合時　C) 最先　D) 最後

> 答案：1. B　2. B　3. B　4. B　5. B

---

## 🔄 2.2 迴圈結構

### **為什麼需要迴圈？**
重複執行相同動作時，迴圈可大幅簡化程式碼。
```
做 10 下伏地挺身 = 重複「做伏地挺身」10 次
倒數計時 = 從 N 開始重複「減 1」直到 0
```

### **for 迴圈 — 已知次數**
```java name=ForLoop.java
public class ForLoop {
    public static void main(String[] args) {
        System.out.println("=== 1 到 10 ===");
        for (int i = 1; i <= 10; i++)
            System.out.print(i + " ");
        System.out.println();

        System.out.println("=== 偶數 0 到 20 ===");
        for (int i = 0; i <= 20; i += 2)
            System.out.print(i + " ");
        System.out.println();

        System.out.println("=== 倒數 10 到 1 ===");
        for (int i = 10; i >= 1; i--)
            System.out.print(i + " ");
        System.out.println("\n發射！🚀");
    }
}
```

### **while 迴圈 — 條件在前**
```java name=WhileLoop.java
import java.util.Scanner;
import java.util.Random;

public class WhileLoop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random r = new Random();
        int secret = r.nextInt(100) + 1, guess = 0, attempts = 0;
        System.out.println("猜 1-100 的數字：");
        while (guess != secret) {
            guess = sc.nextInt(); attempts++;
            if (guess < secret) System.out.println("太小了");
            else if (guess > secret) System.out.println("太大了");
            else System.out.println("🎉 猜對了！共 " + attempts + " 次");
        }
        sc.close();
    }
}
```

### **do-while 迴圈 — 至少執行一次**
```java name=DoWhileLoop.java
import java.util.Scanner;

public class DoWhileLoop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;
        do {
            System.out.println("\n1. 查詢 2. 修改 3. 歷史 0. 離開");
            System.out.print("請選擇：");
            choice = sc.nextInt();
            switch (choice) {
                case 1: System.out.println("📋 查詢中..."); break;
                case 2: System.out.println("🔐 修改中..."); break;
                case 3: System.out.println("📚 歷史記錄"); break;
                case 0: System.out.println("👋 再見！"); break;
                default: System.out.println("❌ 無效選項");
            }
        } while (choice != 0);
        sc.close();
    }
}
```

### **迴圈控制：break 與 continue**
```java name=LoopControl.java
import java.util.Scanner;

public class LoopControl {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // break：提前結束
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) { System.out.println("首個偶數：" + i); break; }
        }
        // continue：跳過本次
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) continue;
            System.out.print(i + " ");
        }
        System.out.println();
        // 除法計算器
        while (true) {
            System.out.print("被除數 (0=結束)："); double a = sc.nextDouble();
            if (a == 0) break;
            System.out.print("除數："); double b = sc.nextDouble();
            if (b == 0) { System.out.println("❌ 不能為 0"); continue; }
            System.out.println(a + " ÷ " + b + " = " + (a / b));
        }
        sc.close();
    }
}
```

### **複習小站 3 — 迴圈**
1. `for (int i=1; i<=3; i++)` 執行幾次？　A) 2　B) 3　C) 4　D) 無限
2. while 與 do-while 最大差異？　A) while 較快　B) do-while 至少執行一次　C) 無差異　D) do-while 無條件
3. `break` 作用？　A) 跳過本次　B) 立即結束迴圈　C) 重開　D) 跳程式
4. `continue` 作用？　A) 跳過本次繼續下輪　B) 結束迴圈　C) 重開　D) 跳程式
5. 何時適合用 for？　A) 已知次數　B) 條件不確定　C) 至少要一次　D) 檔案讀取

> 答案：1. B　2. B　3. B　4. A　5. A

---

## 🛠️ 實作練習

### **練習 1：成績統計**
```java name=GradeStatistics.java
import java.util.Scanner;

public class GradeStatistics {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("學生人數："); int n = sc.nextInt();
        int total = 0, high = 0, low = 100, pass = 0;
        for (int i = 1; i <= n; i++) {
            System.out.print("第 " + i + " 位成績："); int s = sc.nextInt();
            total += s;
            if (s > high) high = s;
            if (s < low) low = s;
            if (s >= 60) pass++;
        }
        double avg = (double) total / n;
        System.out.printf("平均：%.2f 最高：%d 最低：%d 及格率：%.1f%%\n",
                          avg, high, low, (double) pass / n * 100);
        sc.close();
    }
}
```

### **練習 2：數字金字塔**
```java name=NumberPyramid.java
import java.util.Scanner;

public class NumberPyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("層數："); int lv = sc.nextInt();
        for (int i = 1; i <= lv; i++) {
            for (int j = 1; j <= lv - i; j++) System.out.print(" ");
            for (int j = 1; j <= i; j++) System.out.print(j + " ");
            System.out.println();
        }
        // 星號金字塔
        for (int i = 1; i <= lv; i++) {
            for (int j = 1; j <= lv - i; j++) System.out.print(" ");
            for (int j = 1; j <= 2 * i - 1; j++) System.out.print("*");
            System.out.println();
        }
        sc.close();
    }
}
```

### **練習 3：質數檢測器**
```java name=PrimeChecker.java
import java.util.Scanner;

public class PrimeChecker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.print("正整數 (0 結束)："); int n = sc.nextInt();
            if (n == 0) { System.out.println("結束"); break; }
            if (n < 2) { System.out.println(n + " 非質數"); continue; }
            boolean prime = true;
            for (int i = 2; i <= Math.sqrt(n); i++)
                if (n % i == 0) { prime = false; break; }
            System.out.println(n + (prime ? " 是質數 ✅" : " 非質數 ❌"));
        }
        sc.close();
    }
}
```

### **練習 4：運算子實戰**
```java name=OperatorPractice.java
import java.util.Scanner;

public class OperatorPractice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("整數 a："); int a = sc.nextInt();
        System.out.print("整數 b："); int b = sc.nextInt();
        System.out.println(a + " + " + b + " = " + (a + b));
        System.out.println(a + " - " + b + " = " + (a - b));
        System.out.println(a + " * " + b + " = " + (a * b));
        System.out.println(a + " / " + b + " = " + (a / b) + " 餘 " + (a % b));
        System.out.println(a + " > " + b + " ? " + (a > b));
        String cmp = (a > b) ? "a 較大" : (a < b) ? "b 較大" : "相等";
        System.out.println("比較：" + cmp);
        sc.close();
    }
}
```

---

## 📝 重點整理

### **運算子速記**
| 類別 | 關鍵運算子 | 口訣 |
|------|-----------|------|
| 算術 | `+ - * / %` | 加減乘除取餘數 |
| 指派 | `= += -= *= /= %=` | 等號與複合指派 |
| 一元 | `++ -- !` | 遞增遞減邏輯非 |
| 關係 | `== != > < >= <=` | 比較大小與相等 |
| 邏輯 | `&& \|\| !` | 且或非 |
| 三元 | `? :` | 問號冒號三條件 |

### **條件判斷語法**
```java
if (條件) { ... } else { ... }                    // 二選一
if (條件) { ... } else if (條件) { ... } else { ... } // 多選一
switch (變數) { case 值: ... break; default: ... }  // 多路分支
條件 ? 值A : 值B                                     // 三元簡化
```

### **三種迴圈比對**
| 類型 | 適用時機 | 特色 |
|------|---------|------|
| `for` | 已知執行次數 | 初始化、條件、更新在同一行 |
| `while` | 條件在前，可能不執行 | 先判斷再執行 |
| `do-while` | 至少需執行一次 | 先執行再判斷 |

### **迴圈控制關鍵字**
- `break` → 立即跳出迴圈
- `continue` → 跳過本次，繼續下一輪

---

## 📝 自我測驗

### **一、選擇題（每題 10 分）**
1. 哪個是短路且運算子？　A) `&`　B) `&&`　C) `|`　D) `||`
2. `int x = 3; x *= 2 + 1;` 後 x = ?　A) 7　B) 9　C) 6　D) 8
3. 下列輸出？
   ```java
   for (int i = 0; i < 5; i++) {
       if (i == 3) break; System.out.print(i);
   }
   ```
   A) 01234　B) 012　C) 0123　D) 012345
4. switch 省略 `break` 會？　A) 編譯錯誤　B) 穿透到下個 case　C) 跳出　D) 無窮迴圈
5. while 與 do-while 差異？　A) 語法不同　B) do-while 至少執行一次　C) 完全相同　D) while 只能用數字

### **二、填空題（每題 10 分）**
1. 取餘數的運算子是 ______。
2. `x += 5` 等同於 ______。
3. 三元運算子語法：`______ ? ______ : ______`。
4. switch 中跳出區塊的關鍵字是 ______。
5. 標記跳出外層迴圈使用 ______。

### **三、除錯練習（每題 10 分）**
```java
// 題目 1
public class Test {
    public static void main(String[] args) {
        int a = 5, b = 10;
        if (a = b) System.out.println("相等");
    }
}
```
```java
// 題目 2
public class Test {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++)
            System.out.println(i);
        System.out.println(i);
    }
}
```
```java
// 題目 3
public class Test {
    public static void main(String[] args) {
        int x = 1;
        while (x <= 5) System.out.println(x);
    }
}
```

### **答案**
**一、選擇題：** 1. B　2. B（`x *= 3` → 9）　3. B　4. B　5. B
**二、填空題：** 1. `%`　2. `x = x + 5`　3. `條件` `值1` `值2`　4. `break`　5. 標籤名稱
**三、除錯練習：** 1. `a = b` 應為 `a == b`（指派 vs 相等）　2. i 的作用域在 for 內，外部無法存取　3. 缺少 `x++`，造成無窮迴圈

---

## 🏠 課後作業

### **作業 1：BMI 計算與建議系統**
- 輸入身高體重，計算 BMI
- 根據 BMI 值給出健康建議
- 使用迴圈讓使用者可連續計算

### **作業 2：簡單 ATM 系統**
- 功能：查詢、存款、提款、轉帳
- 密碼驗證，選單迴圈

### **作業 3：數值分析**
- 輸入整數，判斷奇偶（`%`）
- 判斷是否為 3 和 5 的公倍數（`&&` + `%`）
- 計算階乘（迴圈 + `*=`）
- 從 1 加到該數（迴圈 + `+=`）

### **作業 4：switch 飲料點餐**
- 1.可樂($25) 2.雪碧($25) 3.果汁($40) 4.紅茶($20) 5.礦泉水($15)
- 顯示對應價格，do-while 連續點餐

---

## 🔍 除錯技巧

### **常見錯誤**
1. **無窮迴圈**：忘記更新迴圈變數
2. **條件錯誤**：用 `=` 代替 `==`
3. **邏輯混淆**：AND / OR 搞混
4. **邊界條件**：`<` 與 `<=` 差別
5. **switch 穿透**：忘記加 `break`
6. **變數範圍**：迴圈外使用迴圈內宣告的變數

### **除錯方法**
```java
System.out.println("Debug: i = " + i);
System.out.println("Debug: 條件 = " + (age >= 18));
```

### **優先順序檢查**
```java
int r1 = 10 + 2 * 5;       // 20
int r2 = (10 + 2) * 5;     // 60（加括號）
boolean r3 = 10 > 5 && 3 < 7; // true
```
