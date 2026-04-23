# 📚 第一單元：Java 基礎入門 - 詳細教學內容

## 🎯 單元學習目標
- 理解程式設計的基本概念
- 掌握 Java 語言的特色與優勢
- 學會基本的 Java 語法結構
- 能夠撰寫簡單的 Java 程式

---

## 📖 1.1 程式設計簡介

### **什麼是程式設計？**
程式設計就像是給電腦寫指令書，告訴電腦要做什麼事情。

**生活比喻：**
```
程式設計 = 寫食譜
- 食譜：一步步的烹飪指令
- 程式：一步步的電腦指令
- 廚師：電腦執行程式
```

### **為什麼選擇 Java？**
1. **跨平台性**：「Write Once, Run Anywhere」
2. **物件導向**：模擬真實世界的思維方式
3. **安全性**：內建安全機制
4. **豐富的函式庫**：功能強大的標準庫

### **Java 程式執行流程**
```
Java 原始碼 (.java) → 編譯器 (javac) → 位元碼 (.class) → JVM 執行
```

---

## 💻 1.2 基本語法

### **第一個 Java 程式**
```java name=HelloWorld.java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**程式結構解析：**
- `public class HelloWorld`：定義一個公開的類別
- `public static void main`：程式的入口點
- `System.out.println()`：在螢幕上顯示文字

### **變數宣告與賦值**

#### **基本資料型別**
```java name=DataTypes.java
public class DataTypes {
    public static void main(String[] args) {
        // 整數型別
        int age = 18;
        long population = 1000000L;
        
        // 浮點數型別
        double price = 99.99;
        float temperature = 36.5f;
        
        // 字元型別
        char grade = 'A';
        
        // 布林型別
        boolean isStudent = true;
        
        // 字串型別
        String name = "張小明";
        
        // 輸出變數
        System.out.println("姓名：" + name);
        System.out.println("年齡：" + age);
        System.out.println("成績：" + grade);
    }
}
```

#### **變數命名規則**
```java
// ✅ 正確的變數名稱
int studentAge;
String firstName;
double account_balance;
boolean isReady;

// ❌ 錯誤的變數名稱
int 2students;    // 不能以數字開頭
String first-name; // 不能包含連字號
boolean is ready; // 不能包含空格
```

### **運算子**
```java name=Operators.java
public class Operators {
    public static void main(String[] args) {
        int a = 10, b = 3;
        
        // 算術運算子
        System.out.println("加法：" + (a + b));    // 13
        System.out.println("減法：" + (a - b));    // 7
        System.out.println("乘法：" + (a * b));    // 30
        System.out.println("除法：" + (a / b));    // 3
        System.out.println("餘數：" + (a % b));    // 1
        
        // 比較運算子
        System.out.println("a > b：" + (a > b));   // true
        System.out.println("a == b：" + (a == b)); // false
        
        // 邏輯運算子
        boolean x = true, y = false;
        System.out.println("x && y：" + (x && y)); // false
        System.out.println("x || y：" + (x || y)); // true
        System.out.println("!x：" + (!x));         // false
    }
}
```

### **註解的使用**
```java name=Comments.java
public class Comments {
    public static void main(String[] args) {
        // 這是單行註解
        System.out.println("Hello"); // 行末註解
        
        /*
         * 這是多行註解
         * 可以寫很多行說明
         */
        System.out.println("World");
        
        /**
         * 這是文件註解 (JavaDoc)
         * 用於產生 API 文件
         * @author TCChang70
         * @version 1.0
         */
    }
}
```

---

## ⌨️ 1.3 使用者輸入

### **Scanner 類別基本使用**
```java name=UserInput.java
import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {
        // 建立 Scanner 物件
        Scanner scanner = new Scanner(System.in);
        
        // 讀取字串
        System.out.print("請輸入您的姓名：");
        String name = scanner.nextLine();
        
        // 讀取整數
        System.out.print("請輸入您的年齡：");
        int age = scanner.nextInt();
        
        // 讀取浮點數
        System.out.print("請輸入您的身高（公分）：");
        double height = scanner.nextDouble();
        
        // 輸出結果
        System.out.println("\n=== 個人資料 ===");
        System.out.println("姓名：" + name);
        System.out.println("年齡：" + age + " 歲");
        System.out.println("身高：" + height + " 公分");
        
        // 關閉 Scanner
        scanner.close();
    }
}
```

### **常見輸入方法**
```java name=ScannerMethods.java
import java.util.Scanner;

public class ScannerMethods {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 不同的輸入方法
        System.out.print("輸入一個字串：");
        String str = scanner.next();        // 讀取到空格為止
        
        System.out.print("輸入一整行：");
        String line = scanner.nextLine();   // 讀取整行
        
        System.out.print("輸入一個整數：");
        int num = scanner.nextInt();        // 讀取整數
        
        System.out.print("輸入一個小數：");
        double decimal = scanner.nextDouble(); // 讀取小數
        
        System.out.print("輸入 true 或 false：");
        boolean bool = scanner.nextBoolean();  // 讀取布林值
        
        scanner.close();
    }
}
```

---

## 🛠️ 實作練習

### **練習 1：個人資料輸入**
```java name=PersonalInfo.java
import java.util.Scanner;

public class PersonalInfo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== 個人資料登記系統 ===");
        
        System.out.print("請輸入姓名：");
        String name = scanner.nextLine();
        
        System.out.print("請輸入年齡：");
        int age = scanner.nextInt();
        
        System.out.print("請輸入身高（公分）：");
        double height = scanner.nextDouble();
        
        System.out.print("請輸入體重（公斤）：");
        double weight = scanner.nextDouble();
        
        // 計算 BMI
        double bmi = weight / ((height / 100) * (height / 100));
        
        // 輸出結果
        System.out.println("\n=== 登記完成 ===");
        System.out.println("姓名：" + name);
        System.out.println("年齡：" + age + " 歲");
        System.out.println("身高：" + height + " 公分");
        System.out.println("體重：" + weight + " 公斤");
        System.out.printf("BMI：%.2f\n", bmi);
        
        scanner.close();
    }
}
```

### **練習 2：簡單計算機**
```java name=SimpleCalculator.java
import java.util.Scanner;

public class SimpleCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== 簡單計算機 ===");
        
        System.out.print("請輸入第一個數字：");
        double num1 = scanner.nextDouble();
        
        System.out.print("請輸入運算符號 (+, -, *, /)：");
        char operator = scanner.next().charAt(0);
        
        System.out.print("請輸入第二個數字：");
        double num2 = scanner.nextDouble();
        
        double result = 0;
        
        // 簡單的運算（之後會學到更好的方法）
        if (operator == '+') {
            result = num1 + num2;
        } else if (operator == '-') {
            result = num1 - num2;
        } else if (operator == '*') {
            result = num1 * num2;
        } else if (operator == '/') {
            result = num1 / num2;
        }
        
        System.out.println("計算結果：" + num1 + " " + operator + " " + num2 + " = " + result);
        
        scanner.close();
    }
}
```

---

## 📝 重點整理

### **必記語法**
1. **基本程式結構**：
   ```java
   public class 類別名稱 {
       public static void main(String[] args) {
           // 程式碼
       }
   }
   ```

2. **變數宣告**：
   ```java
   資料型別 變數名稱 = 初始值;
   ```

3. **輸出語句**：
   ```java
   System.out.println("要顯示的內容");
   ```

4. **輸入語句**：
   ```java
   Scanner scanner = new Scanner(System.in);
   資料型別 變數 = scanner.next對應方法();
   ```

### **常見錯誤**
1. **忘記分號**：每個語句結尾要加 `;`
2. **大小寫錯誤**：Java 區分大小寫
3. **忘記 import**：使用 Scanner 要加 `import java.util.Scanner;`
4. **類別名稱與檔案名稱不一致**

---

## 🏠 課後作業

### **作業 1：溫度轉換器**
撰寫程式將攝氏溫度轉換為華氏溫度
- 公式：華氏 = 攝氏 × 9/5 + 32

### **作業 2：購物清單**
輸入商品名稱、單價、數量，計算總金額

### **作業 3：學生成績**
輸入學生姓名和三科成績，計算平均分數

---

這樣的詳細教學內容如何？我可以繼續為其他單元提供類似深度的教學材料，或者針對某個特定主題做更深入的講解！