# 📚 第三單元：方法與函數 - 詳細教學內容

## 🎯 單元學習目標
- 理解方法的概念與重要性
- 掌握方法的定義與呼叫
- 學會參數傳遞與回傳值的使用
- 了解方法重載與遞迴的應用
- 培養模組化程式設計思維

---

## 🧩 3.1 方法基礎

### **什麼是方法（Method）？**
方法就像是一個「功能盒子」，你給它一些材料（參數），它會為你完成特定的工作，並可能給你一個結果（回傳值）。

**生活比喻：**
```
方法 = 廚房裡的烤箱
- 輸入：麵包材料（參數）
- 處理：烘烤過程（方法內容）
- 輸出：香噴噴的麵包（回傳值）

方法 = 數學函數
f(x) = x + 1
- 輸入：x = 5
- 處理：加 1
- 輸出：6
```

### **為什麼需要方法？**
1. **避免重複代碼**：寫一次，用多次
2. **程式模組化**：將複雜問題分解成小問題
3. **易於維護**：修改功能只需改一個地方
4. **提高可讀性**：讓程式更容易理解

### **方法的基本語法**
```java name=MethodBasics.java
public class MethodBasics {
    
    // 方法語法結構
    // 修飾符 回傳型別 方法名稱(參數列表) {
    //     方法內容
    //     return 回傳值; // 如果有回傳值
    // }
    
    // 1. 無參數、無回傳值的方法
    public static void sayHello() {
        System.out.println("Hello, World!");
        System.out.println("歡迎來到 Java 世界！");
    }
    
    // 2. 有參數、無回傳值的方法
    public static void greetUser(String name) {
        System.out.println("您好，" + name + "！");
        System.out.println("今天過得如何？");
    }
    
    // 3. 無參數、有回傳值的方法
    public static int getCurrentYear() {
        return 2025;
    }
    
    // 4. 有參數、有回傳值的方法
    public static double calculateCircleArea(double radius) {
        double area = Math.PI * radius * radius;
        return area;
    }
    
    // 主方法
    public static void main(String[] args) {
        System.out.println("=== 方法呼叫示範 ===");
        
        // 呼叫無參數方法
        sayHello();
        System.out.println();
        
        // 呼叫有參數方法
        greetUser("TCChang70");
        greetUser("小明");
        System.out.println();
        
        // 呼叫有回傳值方法
        int year = getCurrentYear();
        System.out.println("目前年份：" + year);
        
        // 呼叫有參數和回傳值的方法
        double area = calculateCircleArea(5.0);
        System.out.printf("半徑 5.0 的圓面積：%.2f\n", area);
        
        // 直接在輸出中使用方法回傳值
        System.out.printf("半徑 3.0 的圓面積：%.2f\n", calculateCircleArea(3.0));
    }
}
```

### **方法的命名規則**
```java name=MethodNaming.java
public class MethodNaming {
    
    // ✅ 好的方法命名
    public static double calculateTax(double income) {
        return income * 0.1;
    }
    
    public static boolean isValidEmail(String email) {
        return email.contains("@") && email.contains(".");
    }
    
    public static void printStudentInfo(String name, int age) {
        System.out.println("姓名：" + name + "，年齡：" + age);
    }
    
    public static String getUserInput() {
        // 實際會使用 Scanner
        return "example input";
    }
    
    // ❌ 不好的方法命名
    public static void method1() { } // 名稱不清楚
    public static void CALCULATE() { } // 全大寫
    public static void calculate_tax() { } // 使用底線（Java 慣例使用駝峰命名）
    
    public static void main(String[] args) {
        // 方法名稱應該：
        // 1. 使用駝峰命名法（camelCase）
        // 2. 動詞開頭，描述動作
        // 3. 清楚表達功能
        // 4. 不要太長，但要有意義
        
        double tax = calculateTax(50000);
        System.out.println("稅額：" + tax);
        
        boolean valid = isValidEmail("user@example.com");
        System.out.println("Email 有效：" + valid);
    }
}
```

---

## 📥📤 3.2 參數傳遞與回傳值

### **參數傳遞詳解**
```java name=ParameterPassing.java
import java.util.Scanner;

public class ParameterPassing {
    
    // 單一參數
    public static void displayMessage(String message) {
        System.out.println("📢 " + message);
    }
    
    // 多個參數
    public static void calculateRectangle(double length, double width) {
        double area = length * width;
        double perimeter = 2 * (length + width);
        
        System.out.println("=== 長方形計算結果 ===");
        System.out.printf("長度：%.2f\n", length);
        System.out.printf("寬度：%.2f\n", width);
        System.out.printf("面積：%.2f\n", area);
        System.out.printf("周長：%.2f\n", perimeter);
    }
    
    // 不同資料型別的參數
    public static void displayStudentInfo(String name, int age, double gpa, boolean isGraduated) {
        System.out.println("=== 學生資料 ===");
        System.out.println("姓名：" + name);
        System.out.println("年齡：" + age + " 歲");
        System.out.printf("GPA：%.2f\n", gpa);
        System.out.println("已畢業：" + (isGraduated ? "是" : "否"));
    }
    
    // Java 中的參數傳遞是「傳值」（Pass by Value）
    public static void tryToChangeValue(int number) {
        System.out.println("方法內，修改前：" + number);
        number = 100; // 這不會影響原本的變數
        System.out.println("方法內，修改後：" + number);
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 單一參數呼叫
        displayMessage("歡迎使用參數傳遞示範程式");
        
        // 多個參數呼叫
        calculateRectangle(5.5, 3.2);
        System.out.println();
        
        // 不同型別參數
        displayStudentInfo("張小明", 20, 3.75, false);
        System.out.println();
        
        // 參數傳遞示範
        int originalValue = 50;
        System.out.println("呼叫方法前：" + originalValue);
        tryToChangeValue(originalValue);
        System.out.println("呼叫方法後：" + originalValue); // 值不會改變
        
        // 互動式參數輸入
        System.out.println("\n=== 互動式計算 ===");
        System.out.print("請輸入長方形的長度：");
        double userLength = scanner.nextDouble();
        System.out.print("請輸入長方形的寬度：");
        double userWidth = scanner.nextDouble();
        
        calculateRectangle(userLength, userWidth);
        
        scanner.close();
    }
}
```

### **回傳值詳解**
```java name=ReturnValues.java
import java.util.Scanner;

public class ReturnValues {
    
    // 回傳整數
    public static int add(int a, int b) {
        return a + b;
    }
    
    // 回傳浮點數
    public static double calculateBMI(double weight, double height) {
        double bmi = weight / (height * height);
        return bmi;
    }
    
    // 回傳字串
    public static String getBMICategory(double bmi) {
        if (bmi < 18.5) {
            return "體重過輕";
        } else if (bmi < 24) {
            return "正常體重";
        } else if (bmi < 27) {
            return "體重過重";
        } else {
            return "肥胖";
        }
    }
    
    // 回傳布林值
    public static boolean isPasswordStrong(String password) {
        if (password.length() < 8) {
            return false;
        }
        
        boolean hasUpperCase = false;
        boolean hasLowerCase = false;
        boolean hasDigit = false;
        
        for (int i = 0; i < password.length(); i++) {
            char c = password.charAt(i);
            if (Character.isUpperCase(c)) {
                hasUpperCase = true;
            } else if (Character.isLowerCase(c)) {
                hasLowerCase = true;
            } else if (Character.isDigit(c)) {
                hasDigit = true;
            }
        }
        
        return hasUpperCase && hasLowerCase && hasDigit;
    }
    
    // 早期回傳（Early Return）
    public static String validateAge(int age) {
        if (age < 0) {
            return "年齡不能為負數";
        }
        
        if (age > 150) {
            return "年齡不能超過 150 歲";
        }
        
        if (age < 18) {
            return "未成年";
        }
        
        return "年齡有效";
    }
    
    // 複雜計算回傳
    public static double calculateCompoundInterest(double principal, double rate, int years) {
        double amount = principal * Math.pow(1 + rate / 100, years);
        return amount - principal; // 只回傳利息部分
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 基本回傳值使用
        int sum = add(15, 25);
        System.out.println("15 + 25 = " + sum);
        
        // BMI 計算系統
        System.out.println("\n=== BMI 計算系統 ===");
        System.out.print("請輸入體重（公斤）：");
        double weight = scanner.nextDouble();
        System.out.print("請輸入身高（公尺）：");
        double height = scanner.nextDouble();
        
        double bmi = calculateBMI(weight, height);
        String category = getBMICategory(bmi);
        
        System.out.printf("您的 BMI：%.2f\n", bmi);
        System.out.println("體重狀態：" + category);
        
        // 密碼強度檢測
        System.out.println("\n=== 密碼強度檢測 ===");
        System.out.print("請輸入密碼：");
        String password = scanner.next();
        
        boolean isStrong = isPasswordStrong(password);
        System.out.println("密碼強度：" + (isStrong ? "強" : "弱"));
        
        if (!isStrong) {
            System.out.println("建議：密碼應包含大小寫字母、數字，且長度至少 8 位");
        }
        
        // 年齡驗證
        System.out.println("\n=== 年齡驗證 ===");
        System.out.print("請輸入年齡：");
        int age = scanner.nextInt();
        
        String ageValidation = validateAge(age);
        System.out.println("驗證結果：" + ageValidation);
        
        // 複利計算
        System.out.println("\n=== 複利計算 ===");
        System.out.print("請輸入本金：");
        double principal = scanner.nextDouble();
        System.out.print("請輸入年利率（%）：");
        double rate = scanner.nextDouble();
        System.out.print("請輸入投資年數：");
        int years = scanner.nextInt();
        
        double interest = calculateCompoundInterest(principal, rate, years);
        System.out.printf("%.0f 年後的利息收入：%.2f 元\n", (double)years, interest);
        System.out.printf("總金額：%.2f 元\n", principal + interest);
        
        scanner.close();
    }
}
```

---

## 🔄 3.3 方法重載（Method Overloading）

### **什麼是方法重載？**
方法重載允許我們定義多個同名的方法，但參數列表必須不同。Java 會根據呼叫時提供的參數來決定使用哪個方法。

```java name=MethodOverloading.java
public class MethodOverloading {
    
    // 重載方法 1：兩個整數相加
    public static int add(int a, int b) {
        System.out.println("呼叫了 add(int, int)");
        return a + b;
    }
    
    // 重載方法 2：三個整數相加
    public static int add(int a, int b, int c) {
        System.out.println("呼叫了 add(int, int, int)");
        return a + b + c;
    }
    
    // 重載方法 3：兩個浮點數相加
    public static double add(double a, double b) {
        System.out.println("呼叫了 add(double, double)");
        return a + b;
    }
    
    // 重載方法 4：一個整數和一個浮點數相加
    public static double add(int a, double b) {
        System.out.println("呼叫了 add(int, double)");
        return a + b;
    }
    
    // 重載方法 5：一個浮點數和一個整數相加
    public static double add(double a, int b) {
        System.out.println("呼叫了 add(double, int)");
        return a + b;
    }
    
    // 打印方法的重載
    public static void print(String message) {
        System.out.println("字串：" + message);
    }
    
    public static void print(int number) {
        System.out.println("整數：" + number);
    }
    
    public static void print(double number) {
        System.out.printf("浮點數：%.2f\n", number);
    }
    
    public static void print(boolean value) {
        System.out.println("布林值：" + value);
    }
    
    // 計算面積的重載方法
    // 圓形面積
    public static double calculateArea(double radius) {
        System.out.println("計算圓形面積");
        return Math.PI * radius * radius;
    }
    
    // 長方形面積
    public static double calculateArea(double length, double width) {
        System.out.println("計算長方形面積");
        return length * width;
    }
    
    // 三角形面積
    public static double calculateArea(double base, double height, boolean isTriangle) {
        if (isTriangle) {
            System.out.println("計算三角形面積");
            return 0.5 * base * height;
        }
        return 0;
    }
    
    // 格式化輸出的重載
    public static void displayInfo(String name) {
        System.out.println("姓名：" + name);
    }
    
    public static void displayInfo(String name, int age) {
        System.out.println("姓名：" + name + "，年齡：" + age);
    }
    
    public static void displayInfo(String name, int age, String city) {
        System.out.println("姓名：" + name + "，年齡：" + age + "，城市：" + city);
    }
    
    public static void main(String[] args) {
        System.out.println("=== 方法重載示範 ===");
        
        // 測試 add 方法的重載
        System.out.println("結果：" + add(5, 3));           // int, int
        System.out.println("結果：" + add(5, 3, 2));        // int, int, int
        System.out.println("結果：" + add(5.5, 3.2));       // double, double
        System.out.println("結果：" + add(5, 3.2));         // int, double
        System.out.println("結果：" + add(5.5, 3));         // double, int
        System.out.println();
        
        // 測試 print 方法的重載
        print("Hello World");
        print(42);
        print(3.14159);
        print(true);
        System.out.println();
        
        // 測試面積計算的重載
        System.out.printf("圓形面積：%.2f\n", calculateArea(5.0));
        System.out.printf("長方形面積：%.2f\n", calculateArea(4.0, 6.0));
        System.out.printf("三角形面積：%.2f\n", calculateArea(8.0, 5.0, true));
        System.out.println();
        
        // 測試資訊顯示的重載
        displayInfo("張小明");
        displayInfo("李小華", 25);
        displayInfo("王大明", 30, "台北");
    }
}
```

### **重載的規則與注意事項**
```java name=OverloadingRules.java
public class OverloadingRules {
    
    // ✅ 有效的重載：參數數量不同
    public static void method1(int a) { }
    public static void method1(int a, int b) { }
    
    // ✅ 有效的重載：參數型別不同
    public static void method2(int a) { }
    public static void method2(double a) { }
    
    // ✅ 有效的重載：參數順序不同
    public static void method3(int a, String b) { }
    public static void method3(String a, int b) { }
    
    // ❌ 無效的重載：只有回傳型別不同
    // public static void method4(int a) { }
    // public static int method4(int a) { return 0; } // 編譯錯誤
    
    // ❌ 無效的重載：只有參數名稱不同
    // public static void method5(int a) { }
    // public static void method5(int b) { } // 編譯錯誤
    
    // 實際應用：搜尋功能的重載
    public static void search(String keyword) {
        System.out.println("搜尋關鍵字：" + keyword);
    }
    
    public static void search(String keyword, String category) {
        System.out.println("在 " + category + " 類別中搜尋：" + keyword);
    }
    
    public static void search(String keyword, int maxResults) {
        System.out.println("搜尋 " + keyword + "，最多顯示 " + maxResults + " 筆結果");
    }
    
    public static void search(String keyword, String category, int maxResults) {
        System.out.println("在 " + category + " 類別中搜尋 " + keyword + 
                         "，最多顯示 " + maxResults + " 筆結果");
    }
    
    public static void main(String[] args) {
        System.out.println("=== 搜尋功能重載示範 ===");
        
        search("Java");
        search("Java", "程式設計");
        search("Java", 10);
        search("Java", "程式設計", 5);
    }
}
```

---

## 🔁 3.4 遞迴（Recursion）

### **什麼是遞迴？**
遞迴是一種方法呼叫自己的程式設計技巧。就像俄羅斯娃娃一樣，一層套一層，直到最小的娃娃。

**遞迴的組成要素：**
1. **基本情況（Base Case）**：停止遞迴的條件
2. **遞迴情況（Recursive Case）**：方法呼叫自己

```java name=RecursionBasics.java
public class RecursionBasics {
    
    // 經典範例：計算階乘
    // n! = n × (n-1) × (n-2) × ... × 1
    // 5! = 5 × 4 × 3 × 2 × 1 = 120
    public static long factorial(int n) {
        // 基本情況：0! = 1, 1! = 1
        if (n <= 1) {
            return 1;
        }
        
        // 遞迴情況：n! = n × (n-1)!
        return n * factorial(n - 1);
    }
    
    // 費波納契數列
    // F(0) = 0, F(1) = 1
    // F(n) = F(n-1) + F(n-2)
    // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    public static long fibonacci(int n) {
        // 基本情況
        if (n <= 1) {
            return n;
        }
        
        // 遞迴情況
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    
    // 計算數字的位數
    public static int countDigits(int number) {
        // 基本情況
        if (number < 10) {
            return 1;
        }
        
        // 遞迴情況
        return 1 + countDigits(number / 10);
    }
    
    // 反轉字串
    public static String reverseString(String str) {
        // 基本情況
        if (str.length() <= 1) {
            return str;
        }
        
        // 遞迴情況：最後一個字元 + 反轉其餘部分
        return str.charAt(str.length() - 1) + 
               reverseString(str.substring(0, str.length() - 1));
    }
    
    // 計算冪次方 (x^n)
    public static double power(double x, int n) {
        // 基本情況
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return x;
        }
        
        // 處理負指數
        if (n < 0) {
            return 1.0 / power(x, -n);
        }
        
        // 遞迴情況：x^n = x × x^(n-1)
        return x * power(x, n - 1);
    }
    
    // 最大公因數（歐幾里得演算法）
    public static int gcd(int a, int b) {
        // 基本情況
        if (b == 0) {
            return a;
        }
        
        // 遞迴情況
        return gcd(b, a % b);
    }
    
    public static void main(String[] args) {
        System.out.println("=== 遞迴示範 ===");
        
        // 階乘計算
        System.out.println("=== 階乘計算 ===");
        for (int i = 0; i <= 10; i++) {
            System.out.println(i + "! = " + factorial(i));
        }
        System.out.println();
        
        // 費波納契數列
        System.out.println("=== 費波納契數列 ===");
        System.out.print("前 15 項：");
        for (int i = 0; i < 15; i++) {
            System.out.print(fibonacci(i) + " ");
        }
        System.out.println("\n");
        
        // 計算位數
        System.out.println("=== 計算數字位數 ===");
        int[] numbers = {5, 42, 123, 9876, 12345};
        for (int num : numbers) {
            System.out.println(num + " 有 " + countDigits(num) + " 位數");
        }
        System.out.println();
        
        // 反轉字串
        System.out.println("=== 反轉字串 ===");
        String[] strings = {"hello", "world", "java", "recursion"};
        for (String str : strings) {
            System.out.println(str + " -> " + reverseString(str));
        }
        System.out.println();
        
        // 冪次方計算
        System.out.println("=== 冪次方計算 ===");
        System.out.println("2^5 = " + power(2, 5));
        System.out.println("3^4 = " + power(3, 4));
        System.out.println("5^0 = " + power(5, 0));
        System.out.println("2^(-3) = " + power(2, -3));
        System.out.println();
        
        // 最大公因數
        System.out.println("=== 最大公因數 ===");
        System.out.println("gcd(48, 18) = " + gcd(48, 18));
        System.out.println("gcd(100, 75) = " + gcd(100, 75));
        System.out.println("gcd(17, 13) = " + gcd(17, 13));
    }
}
```

### **遞迴 vs 迴圈比較**
```java name=RecursionVsLoop.java
public class RecursionVsLoop {
    
    // 階乘：遞迴版本
    public static long factorialRecursive(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorialRecursive(n - 1);
    }
    
    // 階乘：迴圈版本
    public static long factorialIterative(int n) {
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
    
    // 費波納契：遞迴版本（效率較低）
    public static long fibonacciRecursive(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
    }
    
    // 費波納契：迴圈版本（效率較高）
    public static long fibonacciIterative(int n) {
        if (n <= 1) {
            return n;
        }
        
        long prev1 = 0, prev2 = 1;
        long current = 0;
        
        for (int i = 2; i <= n; i++) {
            current = prev1 + prev2;
            prev1 = prev2;
            prev2 = current;
        }
        
        return current;
    }
    
    // 測試執行時間
    public static void timeTest() {
        int n = 40;
        
        // 測試費波納契遞迴版本
        long startTime = System.currentTimeMillis();
        long result1 = fibonacciRecursive(n);
        long endTime = System.currentTimeMillis();
        System.out.println("遞迴版本 fibonacci(" + n + ") = " + result1);
        System.out.println("執行時間：" + (endTime - startTime) + " 毫秒");
        
        // 測試費波納契迴圈版本
        startTime = System.currentTimeMillis();
        long result2 = fibonacciIterative(n);
        endTime = System.currentTimeMillis();
        System.out.println("迴圈版本 fibonacci(" + n + ") = " + result2);
        System.out.println("執行時間：" + (endTime - startTime) + " 毫秒");
    }
    
    public static void main(String[] args) {
        System.out.println("=== 遞迴 vs 迴圈比較 ===");
        
        // 階乘比較
        int n = 10;
        System.out.println("階乘比較 (" + n + "!)：");
        System.out.println("遞迴版本：" + factorialRecursive(n));
        System.out.println("迴圈版本：" + factorialIterative(n));
        System.out.println();
        
        // 效能測試
        System.out.println("=== 效能測試 ===");
        timeTest();
        
        System.out.println("\n=== 何時使用遞迴？ ===");
        System.out.println("✅ 適合使用遞迴的情況：");
        System.out.println("  - 問題本身具有遞迴性質（如樹狀結構）");
        System.out.println("  - 程式碼簡潔清晰");
        System.out.println("  - 效能不是主要考量");
        System.out.println();
        System.out.println("❌ 不適合使用遞迴的情況：");
        System.out.println("  - 有重複子問題（如費波納契）");
        System.out.println("  - 深度過深可能造成堆疊溢位");
        System.out.println("  - 效能要求很高");
    }
}
```

---

## 🔧 3.5 變數作用域（Variable Scope）

```java name=VariableScope.java
public class VariableScope {
    
    // 類別變數（靜態變數）- 整個類別都可以存取
    public static int classCounter = 0;
    
    // 實例變數 - 物件的屬性（下個單元會詳細講解）
    public String instanceVariable = "實例變數";
    
    // 方法中的區域變數示範
    public static void demonstrateLocalScope() {
        // 區域變數 - 只在這個方法內有效
        int localVariable = 10;
        String message = "這是區域變數";
        
        System.out.println("方法內的區域變數：" + localVariable);
        System.out.println("方法內的訊息：" + message);
        
        // 在方法內的區塊作用域
        if (localVariable > 5) {
            // 區塊內的變數
            int blockVariable = 20;
            System.out.println("區塊內的變數：" + blockVariable);
            System.out.println("可以存取外層變數：" + localVariable);
        }
        
        // System.out.println(blockVariable); // 錯誤！區塊外無法存取
    }
    
    // 參數作用域
    public static void demonstrateParameterScope(int parameter) {
        // 參數在整個方法內都有效
        System.out.println("參數值：" + parameter);
        
        // 可以修改參數值（但不會影響呼叫者的變數）
        parameter = 100;
        System.out.println("修改後的參數值：" + parameter);
    }
    
    // 變數遮蔽（Variable Shadowing）
    public static void demonstrateShadowing(int classCounter) {
        // 參數名稱與類別變數同名，會遮蔽類別變數
        System.out.println("參數 classCounter：" + classCounter);
        System.out.println("類別變數 classCounter：" + VariableScope.classCounter);
        
        // 區域變數遮蔽
        String message = "區域訊息";
        {
            String message2 = "區塊訊息"; // 不同名稱，沒問題
            System.out.println("區塊內的 message2：" + message2);
            System.out.println("仍可存取外層 message：" + message);
        }
    }
    
    // 方法間的變數傳遞
    public static int calculateSum(int a, int b) {
        int sum = a + b; // 區域變數
        classCounter++; // 修改類別變數
        return sum;
    }
    
    public static void displayResult(int result) {
        // 不能存取其他方法的區域變數
        // System.out.println(sum); // 錯誤！
        
        System.out.println("計算結果：" + result);
        System.out.println("類別計數器：" + classCounter);
    }
    
    // 迴圈變數作用域
    public static void demonstrateLoopScope() {
        System.out.println("=== 迴圈變數作用域 ===");
        
        // for 迴圈變數只在迴圈內有效
        for (int i = 0; i < 3; i++) {
            System.out.println("迴圈變數 i：" + i);
        }
        // System.out.println(i); // 錯誤！迴圈外無法存取
        
        // 在不同迴圈中可以重複使用相同變數名
        for (int i = 10; i < 13; i++) {
            System.out.println("另一個迴圈的 i：" + i);
        }
        
        // while 迴圈
        int j = 0;
        while (j < 3) {
            System.out.println("while 迴圈變數 j：" + j);
            j++;
        }
        System.out.println("while 迴圈外的 j：" + j); // 可以存取，因為 j 宣告在外面
    }
    
    public static void main(String[] args) {
        System.out.println("=== 變數作用域示範 ===");
        
        // 類別變數存取
        System.out.println("初始類別計數器：" + classCounter);
        
        // 區域變數示範
        demonstrateLocalScope();
        System.out.println();
        
        // 參數作用域示範
        int originalValue = 50;
        System.out.println("呼叫前的原始值：" + originalValue);
        demonstrateParameterScope(originalValue);
        System.out.println("呼叫後的原始值：" + originalValue); // 不會改變
        System.out.println();
        
        // 變數遮蔽示範
        demonstrateShadowing(99);
        System.out.println();
        
        // 方法間變數傳遞
        int result = calculateSum(10, 20);
        displayResult(result);
        System.out.println();
        
        // 迴圈作用域
        demonstrateLoopScope();
        
        // 最佳實踐
        System.out.println("\n=== 變數作用域最佳實踐 ===");
        System.out.println("1. 盡量縮小變數的作用域");
        System.out.println("2. 避免變數名稱遮蔽");
        System.out.println("3. 使用有意義的變數名稱");
        System.out.println("4. 在最接近使用位置的地方宣告變數");
    }
}
```

---

## 🛠️ 綜合實作練習

### **練習 1：數學工具類別**
```java name=MathUtils.java
import java.util.Scanner;

public class MathUtils {
    
    // 判斷是否為質數
    public static boolean isPrime(int number) {
        if (number < 2) {
            return false;
        }
        
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        
        return true;
    }
    
    // 找出範圍內的所有質數
    public static void printPrimesInRange(int start, int end) {
        System.out.println(start + " 到 " + end + " 之間的質數：");
        int count = 0;
        
        for (int i = start; i <= end; i++) {
            if (isPrime(i)) {
                System.out.print(i + " ");
                count++;
                if (count % 10 == 0) { // 每 10 個換行
                    System.out.println();
                }
            }
        }
        
        if (count % 10 != 0) {
            System.out.println();
        }
        System.out.println("總共找到 " + count + " 個質數");
    }
    
    // 計算數字的所有因數
    public static void printFactors(int number) {
        System.out.println(number + " 的所有因數：");
        
        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }
    
    // 最大公因數（遞迴版本）
    public static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
    
    // 最小公倍數
    public static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }
    
    // 完全數檢查
    public static boolean isPerfectNumber(int number) {
        if (number <= 1) {
            return false;
        }
        
        int sum = 1; // 1 是所有數的因數
        
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                sum += i;
                if (i != number / i) { // 避免重複加入平方根
                    sum += number / i;
                }
            }
        }
        
        return sum == number;
    }
    
    // 數字反轉
    public static int reverseNumber(int number) {
        int reversed = 0;
        
        while (number != 0) {
            reversed = reversed * 10 + number % 10;
            number /= 10;
        }
        
        return reversed;
    }
    
    // 回文數檢查
    public static boolean isPalindrome(int number) {
        return number == reverseNumber(number);
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("\n=== 數學工具程式 ===");
            System.out.println("1. 質數檢查");
            System.out.println("2. 範圍內質數列表");
            System.out.println("3. 因數分解");
            System.out.println("4. 最大公因數和最小公倍數");
            System.out.println("5. 完全數檢查");
            System.out.println("6. 回文數檢查");
            System.out.println("0. 離開程式");
            System.out.print("請選擇功能：");
            
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    System.out.print("請輸入數字：");
                    int num = scanner.nextInt();
                    System.out.println(num + (isPrime(num) ? " 是質數" : " 不是質數"));
                    break;
                    
                case 2:
                    System.out.print("請輸入起始數字：");
                    int start = scanner.nextInt();
                    System.out.print("請輸入結束數字：");
                    int end = scanner.nextInt();
                    printPrimesInRange(start, end);
                    break;
                    
                case 3:
                    System.out.print("請輸入數字：");
                    int factorNum = scanner.nextInt();
                    printFactors(factorNum);
                    break;
                    
                case 4:
                    System.out.print("請輸入第一個數字：");
                    int a = scanner.nextInt();
                    System.out.print("請輸入第二個數字：");
                    int b = scanner.nextInt();
                    System.out.println("最大公因數：" + gcd(a, b));
                    System.out.println("最小公倍數：" + lcm(a, b));
                    break;
                    
                case 5:
                    System.out.print("請輸入數字：");
                    int perfectNum = scanner.nextInt();
                    System.out.println(perfectNum + (isPerfectNumber(perfectNum) ? " 是完全數" : " 不是完全數"));
                    break;
                    
                case 6:
                    System.out.print("請輸入數字：");
                    int palindromeNum = scanner.nextInt();
                    System.out.println(palindromeNum + (isPalindrome(palindromeNum) ? " 是回文數" : " 不是回文數"));
                    break;
                    
                case 0:
                    System.out.println("感謝使用，再見！");
                    scanner.close();
                    return;
                    
                default:
                    System.out.println("無效選擇，請重新輸入！");
            }
        }
    }
}
```

### **練習 2：字串處理工具**
```java name=StringUtils.java
import java.util.Scanner;

public class StringUtils {
    
    // 字串反轉（迴圈版本）
    public static String reverseString(String str) {
        String reversed = "";
        for (int i = str.length() - 1; i >= 0; i--) {
            reversed += str.charAt(i);
        }
        return reversed;
    }
    
    // 字串反轉（遞迴版本）
    public static String reverseStringRecursive(String str) {
        if (str.length() <= 1) {
            return str;
        }
        return str.charAt(str.length() - 1) + 
               reverseStringRecursive(str.substring(0, str.length() - 1));
    }
    
    // 回文檢查
    public static boolean isPalindrome(String str) {
        // 移除空格並轉為小寫
        str = str.replaceAll("\\s+", "").toLowerCase();
        return str.equals(reverseString(str));
    }
    
    // 統計字元出現次數
    public static void countCharacters(String str) {
        int letters = 0, digits = 0, spaces = 0, others = 0;
        
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            
            if (Character.isLetter(c)) {
                letters++;
            } else if (Character.isDigit(c)) {
                digits++;
            } else if (Character.isWhitespace(c)) {
                spaces++;
            } else {
                others++;
            }
        }
        
        System.out.println("字串分析結果：");
        System.out.println("總長度：" + str.length());
        System.out.println("字母：" + letters);
        System.out.println("數字：" + digits);
        System.out.println("空格：" + spaces);
        System.out.println("其他：" + others);
    }
    
    // 首字母大寫
    public static String capitalizeWords(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        
        String[] words = str.split("\\s+");
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < words.length; i++) {
            if (!words[i].isEmpty()) {
                words[i] = Character.toUpperCase(words[i].charAt(0)) + 
                          words[i].substring(1).toLowerCase();
            }
            
            result.append(words[i]);
            if (i < words.length - 1) {
                result.append(" ");
            }
        }
        
        return result.toString();
    }
    
    // 移除重複字元
    public static String removeDuplicates(String str) {
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < str.length(); i++) {
            char currentChar = str.charAt(i);
            
            // 檢查這個字元是否已經在結果中
            boolean isDuplicate = false;
            for (int j = 0; j < result.length(); j++) {
                if (result.charAt(j) == currentChar) {
                    isDuplicate = true;
                    break;
                }
            }
            
            if (!isDuplicate) {
                result.append(currentChar);
            }
        }
        
        return result.toString();
    }
    
    // 字串壓縮
    public static String compressString(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        
        StringBuilder compressed = new StringBuilder();
        int count = 1;
        
        for (int i = 0; i < str.length(); i++) {
            if (i + 1 < str.length() && str.charAt(i) == str.charAt(i + 1)) {
                count++;
            } else {
                compressed.append(str.charAt(i)).append(count);
                count = 1;
            }
        }
        
        return compressed.length() < str.length() ? compressed.toString() : str;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("\n=== 字串處理工具 ===");
            System.out.println("1. 字串反轉");
            System.out.println("2. 回文檢查");
            System.out.println("3. 字元統計");
            System.out.println("4. 首字母大寫");
            System.out.println("5. 移除重複字元");
            System.out.println("6. 字串壓縮");
            System.out.println("0. 離開程式");
            System.out.print("請選擇功能：");
            
            int choice = scanner.nextInt();
            scanner.nextLine(); // 消費換行符
            
            switch (choice) {
                case 1:
                    System.out.print("請輸入字串：");
                    String str1 = scanner.nextLine();
                    System.out.println("迴圈版本：" + reverseString(str1));
                    System.out.println("遞迴版本：" + reverseStringRecursive(str1));
                    break;
                    
                case 2:
                    System.out.print("請輸入字串：");
                    String str2 = scanner.nextLine();
                    System.out.println(str2 + (isPalindrome(str2) ? " 是回文" : " 不是回文"));
                    break;
                    
                case 3:
                    System.out.print("請輸入字串：");
                    String str3 = scanner.nextLine();
                    countCharacters(str3);
                    break;
                    
                case 4:
                    System.out.print("請輸入字串：");
                    String str4 = scanner.nextLine();
                    System.out.println("結果：" + capitalizeWords(str4));
                    break;
                    
                case 5:
                    System.out.print("請輸入字串：");
                    String str5 = scanner.nextLine();
                    System.out.println("結果：" + removeDuplicates(str5));
                    break;
                    
                case 6:
                    System.out.print("請輸入字串：");
                    String str6 = scanner.nextLine();
                    System.out.println("結果：" + compressString(str6));
                    break;
                    
                case 0:
                    System.out.println("感謝使用，再見！");
                    scanner.close();
                    return;
                    
                default:
                    System.out.println("無效選擇，請重新輸入！");
            }
        }
    }
}
```

---

## 📝 重點整理

### **方法語法結構**
```java
修飾符 回傳型別 方法名稱(參數型別 參數名稱, ...) {
    // 方法內容
    return 回傳值; // 如果有回傳值
}
```

### **方法的好處**
1. **代碼重用**：避免重複撰寫相同代碼
2. **模組化**：將複雜問題分解
3. **易於測試**：單獨測試各個功能
4. **提高可讀性**：程式結構更清晰

### **重要概念**
- **參數傳遞**：Java 使用傳值方式
- **方法重載**：同名方法，不同參數
- **遞迴**：方法呼叫自己，需要基本情況
- **作用域**：變數的可見範圍

### **最佳實踐**
1. **方法應該只做一件事**
2. **使用有意義的方法名稱**
3. **保持方法簡短**（一般不超過 20-30 行）
4. **避免過深的參數列表**
5. **適當使用註解說明複雜邏輯**

---

## 🏠 課後作業

### **作業 1：遊戲分數系統**
設計一個遊戲分數管理系統：
- 計算單局分數
- 計算平均分數
- 找出最高/最低分
- 判斷是否達到升級條件

### **作業 2：文字分析器**
創建文字分析工具：
- 統計單字數量
- 找出最長/最短單字
- 計算平均單字長度
- 檢查文法錯誤（簡單版本）

### **作業 3：數學計算機**
實作科學計算機：
- 基本四則運算
- 三角函數
- 對數運算
- 冪次方計算
- 使用方法重載處理不同精度

---

## 🔍 除錯技巧

### **常見錯誤**
1. **遺漏 return 語句**
2. **無窮遞迴**（缺少基本情況）
3. **參數型別不匹配**
4. **變數作用域錯誤**

### **除錯方法**
```java
// 在方法開始和結束加入除錯訊息
public static int myMethod(int param) {
    System.out.println("DEBUG: 進入 myMethod，參數 = " + param);
    
    // 方法邏輯
    int result = param * 2;
    
    System.out.println("DEBUG: 離開 myMethod，回傳 = " + result);
    return result;
}
```

這樣的第三單元教學內容涵蓋了方法的所有重要概念，從基礎到進階，並提供了豐富的實例和練習。學生通過這個單元能夠掌握模組化程式設計的思維，為後續的物件導向程式設計打下堅實的基礎。

需要我繼續第四單元或針對某個特定概念做更深入的講解嗎？