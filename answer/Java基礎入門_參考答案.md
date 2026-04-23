# 📝 第一單元：Java 基礎入門 考題 - 參考答案

## 🎯 第一部分：基礎概念題參考答案 (30分)

### **題目 1：選擇題答案**

1. **B) .java → javac → .class → JVM**
   - 解析：Java 程式先由 javac 編譯器編譯成位元碼，再由 JVM 執行

2. **C) `int`**
   - 解析：`int` 是基本資料型別，`String` 和 `Integer` 是類別

3. **C) `student_age`**
   - 解析：變數名稱不能以數字開頭，不能包含連字號，`class` 是關鍵字

4. **B) `%`**
   - 解析：`%` 是取餘數運算子（模運算）

5. **A) `age` 和 `Age`**
   - 解析：Java 區分大小寫，所以這兩個是不同的變數

6. **B) `import java.util.Scanner;`**
   - 解析：Scanner 類別位於 java.util 套件中

7. **B) `public static void main(String[] args)`**
   - 解析：標準的程式進入點格式

8. **B) `//`**
   - 解析：`//` 用於單行註解，`/* */` 用於多行註解

### **題目 2：填空題答案**

```java
import java.util.Scanner;           // 填空 1

public class HelloWorld {           // 填空 2
    public static void main(String[] args) {    // 填空 3
        Scanner scanner = new Scanner(System.in);   // 填空 4, 5
        
        System.out.print("請輸入您的姓名：");    // 填空 6
        String name = scanner.nextLine();       // 填空 7
        
        scanner.close();                        // 填空 8
    }
}
```

---

## 💻 第二部分：程式設計題參考答案 (55分)

### **題目 3：個人資料登記系統完整解答**

```java
import java.util.Scanner;

public class PersonalInfo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== 個人資料登記系統 ===");
        
        // 輸入個人資料
        System.out.print("請輸入姓名：");
        String name = scanner.nextLine();
        
        System.out.print("請輸入年齡：");
        int age = scanner.nextInt();
        
        System.out.print("請輸入身高（公分）：");
        double height = scanner.nextDouble();
        
        System.out.print("請輸入體重（公斤）：");
        double weight = scanner.nextDouble();
        
        // 計算 BMI
        double heightInMeter = height / 100.0;  // 轉換為公尺
        double bmi = weight / (heightInMeter * heightInMeter);
        
        // 判定健康狀態
        String healthStatus;
        if (bmi < 18.5) {
            healthStatus = "體重過輕";
        } else if (bmi < 24) {
            healthStatus = "正常範圍";
        } else if (bmi < 27) {
            healthStatus = "過重";
        } else {
            healthStatus = "肥胖";
        }
        
        // 輸出結果
        System.out.println("\n=== 個人資料 ===");
        System.out.println("姓名：" + name);
        System.out.println("年齡：" + age + " 歲");
        System.out.println("身高：" + height + " 公分");
        System.out.println("體重：" + weight + " 公斤");
        System.out.printf("BMI：%.2f\n", bmi);
        System.out.println("健康狀態：" + healthStatus);
        
        scanner.close();
    }
}
```

**預期輸出：**
```
=== 個人資料登記系統 ===
請輸入姓名：張小明
請輸入年齡：25
請輸入身高（公分）：170
請輸入體重（公斤）：65

=== 個人資料 ===
姓名：張小明
年齡：25 歲
身高：170.0 公分
體重：65.0 公斤
BMI：22.49
健康狀態：正常範圍
```

### **題目 4：多功能計算機完整解答**

```java
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== 多功能計算機 ===");
        
        // 輸入兩個數字和運算符號
        System.out.print("請輸入第一個數字：");
        double num1 = scanner.nextDouble();
        
        System.out.print("請輸入運算符號 (+, -, *, /)：");
        char operator = scanner.next().charAt(0);
        
        System.out.print("請輸入第二個數字：");
        double num2 = scanner.nextDouble();
        
        // 進行運算
        double result = 0;
        boolean validOperation = true;
        String operatorSymbol = "";
        
        if (operator == '+') {
            result = num1 + num2;
            operatorSymbol = "+";
        } else if (operator == '-') {
            result = num1 - num2;
            operatorSymbol = "-";
        } else if (operator == '*') {
            result = num1 * num2;
            operatorSymbol = "×";
        } else if (operator == '/') {
            if (num2 == 0) {
                System.out.println("❌ 錯誤：除數不能為零！");
                validOperation = false;
            } else {
                result = num1 / num2;
                operatorSymbol = "÷";
            }
        } else {
            System.out.println("❌ 錯誤：無效的運算符號！請使用 +, -, *, /");
            validOperation = false;
        }
        
        // 輸出結果
        if (validOperation) {
            System.out.printf("計算結果：%.2f %s %.2f = %.2f\n", 
                            num1, operatorSymbol, num2, result);
        }
        
        scanner.close();
    }
}
```

**預期輸出範例：**
```
=== 多功能計算機 ===
請輸入第一個數字：10
請輸入運算符號 (+, -, *, /)：/
請輸入第二個數字：3
計算結果：10.00 ÷ 3.00 = 3.33
```

### **題目 5：學生成績統計系統完整解答**

```java
import java.util.Scanner;

public class GradeReport {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== 學生成績統計系統 ===");
        
        // 輸入學生資料
        System.out.print("請輸入學生姓名：");
        String name = scanner.nextLine();
        
        System.out.print("請輸入國文成績：");
        int chinese = scanner.nextInt();
        
        System.out.print("請輸入英文成績：");
        int english = scanner.nextInt();
        
        System.out.print("請輸入數學成績：");
        int math = scanner.nextInt();
        
        // 計算統計數據
        int total = chinese + english + math;
        double average = (double) total / 3;
        
        // 找出最高分和最低分科目
        String highestSubject, lowestSubject;
        int highestScore, lowestScore;
        
        if (chinese >= english && chinese >= math) {
            highestSubject = "國文";
            highestScore = chinese;
        } else if (english >= math) {
            highestSubject = "英文";
            highestScore = english;
        } else {
            highestSubject = "數學";
            highestScore = math;
        }
        
        if (chinese <= english && chinese <= math) {
            lowestSubject = "國文";
            lowestScore = chinese;
        } else if (english <= math) {
            lowestSubject = "英文";
            lowestScore = english;
        } else {
            lowestSubject = "數學";
            lowestScore = math;
        }
        
        // 輸出成績報表
        System.out.println("\n=== 成績報表 ===");
        System.out.println("學生姓名：" + name);
        System.out.println("國文成績：" + chinese + " 分");
        System.out.println("英文成績：" + english + " 分");
        System.out.println("數學成績：" + math + " 分");
        System.out.println("─────────────");
        System.out.println("總    分：" + total + " 分");
        System.out.printf("平均分數：%.2f 分\n", average);
        System.out.println("最高分科目：" + highestSubject + " (" + highestScore + " 分)");
        System.out.println("最低分科目：" + lowestSubject + " (" + lowestScore + " 分)");
        
        scanner.close();
    }
}
```

**預期輸出：**
```
=== 學生成績統計系統 ===
請輸入學生姓名：李小華
請輸入國文成績：85
請輸入英文成績：92
請輸入數學成績：78

=== 成績報表 ===
學生姓名：李小華
國文成績：85 分
英文成績：92 分
數學成績：78 分
─────────────
總    分：255 分
平均分數：85.00 分
最高分科目：英文 (92 分)
最低分科目：數學 (78 分)
```

---

## 🔍 第三部分：程式碼閱讀與分析參考答案 (15分)

### **題目 6：程式碼追蹤答案**

**程式執行結果：**
```
result1 = 3
result2 = 3.75
result3 = 3
flag1 = true
flag2 = true
```

**詳細解析：**

1. **`result1` 的值是 3**
   - 因為 `15 / 4` 是整數除法，結果只保留整數部分，所以是 3

2. **`result2` 的值是 3.75**
   - 因為將 `a` 強制轉換為 `double`，所以進行浮點數除法
   - `(double) 15 / 4` = `15.0 / 4` = `3.75`

3. **`result3` 的值是 3**
   - `%` 是取餘數運算子，`15 % 4` = 3（15 除以 4 的餘數）

4. **`flag1` 和 `flag2` 的值：**
   - `flag1 = (15 > 10) && (4 < 5)` = `true && true` = `true`
   - `flag2 = (15 == 15) || (4 > 10)` = `true || false` = `true`

### **題目 7：找出錯誤答案**

**錯誤列表：**

1. **第1行：** `import java.util.scanner;` 
   - 錯誤：`Scanner` 的 S 應該大寫
   - 修正：`import java.util.Scanner;`

2. **第3行：** `public class buggyProgram`
   - 錯誤：類別名稱應該遵循 Pascal 命名法
   - 修正：`public class BuggyProgram`

3. **第4行：** `public static void Main(String[] args)`
   - 錯誤：`Main` 的 M 應該小寫
   - 修正：`public static void main(String[] args)`

4. **第5行：** `Scanner input = new Scanner(System.in)`
   - 錯誤：缺少分號
   - 修正：`Scanner input = new Scanner(System.in);`

5. **第9行：** `System.out.println("請輸入您的姓名：")`
   - 錯誤：缺少分號
   - 修正：`System.out.println("請輸入您的姓名：");`

6. **第10行：** `String name = input.nextline();`
   - 錯誤：`nextline()` 應該是 `nextLine()` (L 大寫)
   - 修正：`String name = input.nextLine();`

7. **第12行：** `double result = Age * 12`
   - 錯誤：缺少分號
   - 修正：`double result = Age * 12;`

8. **第16行：** `input.close()`
   - 錯誤：缺少分號
   - 修正：`input.close();`

**修正後的完整程式碼：**

```java
import java.util.Scanner;

public class BuggyProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("請輸入您的年齡：");
        int Age = input.nextInt();
        
        System.out.println("請輸入您的姓名：");
        String name = input.nextLine();
        
        double result = Age * 12;
        
        System.out.println("姓名：" + name);
        System.out.println(Age + "歲等於" + result + "個月");
        
        input.close();
    }
}
```

**注意事項：**
- 還有一個潛在問題：`nextInt()` 後直接使用 `nextLine()` 可能會讀取到空字串，建議在中間加上 `input.nextLine();` 來清除緩衝區

---

## 📊 評分標準詳細說明

### **程式設計題評分細節：**

**題目 3 (15分)：**
- 正確輸入姓名、年齡、身高、體重 (4分)
- BMI 計算公式正確 (4分)
- 健康狀態判定邏輯正確 (4分)
- 輸出格式美觀完整 (3分)

**題目 4 (20分)：**
- 四則運算邏輯正確 (8分)
- 除零檢查機制 (4分)
- 無效運算符號處理 (4分)
- 輸出格式與使用者體驗 (4分)

**題目 5 (20分)：**
- 成績輸入正確 (5分)
- 總分與平均計算 (5分)
- 最高分最低分判定邏輯 (6分)
- 報表格式完整美觀 (4分)

---

## 🎯 學習重點提醒

1. **基本語法**：掌握 Java 程式基本結構
2. **變數與資料型別**：正確使用各種資料型別
3. **運算子**：熟悉算術、比較、邏輯運算子
4. **輸入輸出**：Scanner 的正確使用方法
5. **程式設計思維**：邏輯思考與問題分解能力

**總評：此考題全面涵蓋了 Java 基礎入門的核心概念，能夠有效評估學生的基礎程式設計能力。**