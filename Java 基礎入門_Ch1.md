# 📚 第一單元：Java 基礎入門 - 詳細教學內容

## 🎯 單元學習目標
- 理解程式設計的基本概念
- 掌握 Java 語言的特色與優勢
- 學會基本的 Java 語法結構
- 能夠撰寫簡單的 Java 程式
- 熟悉 Java 各資料型別與型別轉換

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

### **複習小站 1 — 程式設計概念**
選擇正確答案：
1. Java 程式碼經過編譯後會產生什麼檔案？
   A) .exe　　B) .class　　C) .doc　　D) .txt

2. 下列哪一個不是 Java 的特性？
   A) 跨平台　　B) 物件導向　　C) 需要重新編譯才能在每個平台執行　　D) 安全性高

> 答案：1. B　2. C

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

#### **Java 資料型別總覽**

Java 的資料型別分為兩大類：**基本資料型別 (Primitive Types)** 和 **參考資料型別 (Reference Types)**。

##### **基本資料型別一覽表**

| 類別 | 關鍵字 | 佔用空間 | 數值範圍 | 預設值 | 範例 |
|------|--------|---------|---------|--------|------|
| 整數 | `byte` | 1 byte | -128 ~ 127 | 0 | `byte b = 100;` |
| 整數 | `short` | 2 bytes | -32,768 ~ 32,767 | 0 | `short s = 1000;` |
| 整數 | `int` | 4 bytes | -2^31 ~ 2^31-1 | 0 | `int i = 100000;` |
| 整數 | `long` | 8 bytes | -2^63 ~ 2^63-1 | 0L | `long l = 100000L;` |
| 浮點數 | `float` | 4 bytes | ±3.4E-38 ~ ±3.4E+38 | 0.0f | `float f = 3.14f;` |
| 浮點數 | `double` | 8 bytes | ±1.7E-308 ~ ±1.7E+308 | 0.0d | `double d = 3.14;` |
| 字元 | `char` | 2 bytes | 0 ~ 65,535 (Unicode) | '\u0000' | `char c = 'A';` |
| 布林 | `boolean` | 未明確定義 | true / false | false | `boolean b = true;` |

**記憶口訣：**「Byte Short Int Long 依序翻倍，Float Double 精準不同，Char 放字元，Boolean 真與假」

**重點提示：**
- `long` 型別的數值結尾要加 **L**（建議大寫）
- `float` 型別的數值結尾要加 **f**
- `double` 是 Java 預設的浮點數型別
- `char` 使用 Unicode 編碼，可存放中文
- `boolean` 只有 `true` 和 `false` 兩種值，不能用 0 或 1 代替

##### **參考資料型別 (Reference Types)**

參考資料型別不直接儲存數值，而是指向記憶體中的位置：

| 型別 | 說明 | 宣告範例 |
|------|------|---------|
| `String` | 字串 | `String name = "Hello";` |
| 陣列 | 相同型別的集合 | `int[] nums = {1, 2, 3};` |
| 類別 / 介面 | 自訂資料型別 | `Scanner sc = new Scanner(System.in);` |

##### **型別轉換**
```java
// 自動轉換 (隱式 / Widening) — 小範圍 → 大範圍，安全無損
int num = 100;
double d = num;               // int → double：OK
System.out.println(d);         // 輸出 100.0

// 強制轉換 (顯式 / Narrowing) — 大範圍 → 小範圍，可能遺失資料
double price = 99.99;
int p = (int) price;           // double → int：小數點被截斷
System.out.println(p);         // 輸出 99（小數遺失）

// 常見的型別轉換錯誤
int big = 300;
byte small = (byte) big;       // 資料溢位！
System.out.println(small);     // 輸出 44（非預期結果）
```

##### **完整資料型別範例**
```java name=DataTypes.java
public class DataTypes {
    public static void main(String[] args) {
        // ---- 整數型別 ----
        byte b = 100;
        short s = 10000;
        int age = 18;
        long population = 1000000L;

        // ---- 浮點數型別 ----
        float temperature = 36.5f;
        double price = 99.99;

        // ---- 字元與布林 ----
        char grade = 'A';
        boolean isStudent = true;

        // ---- 字串 (參考型別) ----
        String name = "張小明";

        // ---- 輸出變數 ----
        System.out.println("姓名：" + name);
        System.out.println("年齡：" + age);
        System.out.println("成績：" + grade);
        System.out.println("體溫：" + temperature);
        System.out.println("學生：" + isStudent);

        // ---- 型別轉換展示 ----
        int i = (int) price;        // double → int（強制）
        System.out.println("整數價格：" + i);
    }
}
```

#### **變數命名規則**
```java
// ✅ 正確的變數名稱（小駝峰式命名）
int studentAge;
String firstName;
double accountBalance;
boolean isReady;

// ❌ 錯誤的變數名稱
int 2students;        // 不能以數字開頭
String first-name;    // 不能包含連字號
boolean is ready;     // 不能包含空格
int class;            // 不能使用保留字 (class)
```

**命名慣例：**
- 變數與方法：小駝峰 (`myVariableName`)
- 類別名稱：大駝峰 (`MyClassName`)
- 常數：全大寫底線 (`MAX_VALUE`)
- 套件名稱：全小寫 (`com.example.myapp`)

### **運算子**
```java name=Operators.java
public class Operators {
    public static void main(String[] args) {
        int a = 10, b = 3;

        // 算術運算子
        System.out.println("加法：" + (a + b));    // 13
        System.out.println("減法：" + (a - b));    // 7
        System.out.println("乘法：" + (a * b));    // 30
        System.out.println("除法：" + (a / b));    // 3（整數除法）
        System.out.println("餘數：" + (a % b));    // 1

        // 複合指定運算子
        int c = 5;
        c += 3;  // 等同 c = c + 3
        System.out.println("c += 3：" + c);       // 8

        // 比較運算子
        System.out.println("a > b：" + (a > b));   // true
        System.out.println("a == b：" + (a == b)); // false

        // 邏輯運算子
        boolean x = true, y = false;
        System.out.println("x && y：" + (x && y)); // false
        System.out.println("x || y：" + (x || y)); // true
        System.out.println("!x：" + (!x));         // false

        // 遞增 / 遞減運算子
        int count = 0;
        System.out.println("count++：" + count++); // 0（先取值再 +1）
        System.out.println("++count：" + ++count); // 2（先 +1 再取值）
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

### **複習小站 2 — 資料型別與變數**
選擇正確答案：
1. `float f = 3.14;` 這行程式碼哪裡有問題？
   A) 沒有問題　　B) 3.14 預設是 double，需加 f　　C) 不能用 float　　D) 變數名稱錯誤

2. `int` 型別佔用多少 bytes？
   A) 1　　B) 2　　C) 4　　D) 8

3. 下列哪個是正確的變數名稱？
   A) 2name　　B) my-name　　C) myName　　D) class

4. 執行 `System.out.println(10 / 4);` 會輸出什麼？
   A) 2.5　　B) 2　　C) 2.0　　D) 編譯錯誤

5. `long` 型別的數值結尾應加上哪個字母？
   A) f　　B) d　　C) L　　D) l（都可以）

> 答案：1. B　2. C　3. C　4. B　5. C

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
        System.out.print("輸入一個字串（無空格）：");
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

### **複習小站 3 — 使用者輸入**
選擇正確答案：
1. 使用 Scanner 前需要加入什麼？
   A) `import java.util.*;`　　B) `import java.util.Scanner;`　　C) 兩者皆可　　D) 不需要 import

2. `scanner.nextInt()` 可以讀取哪種型別？
   A) String　　B) double　　C) int　　D) boolean

3. 使用完 Scanner 後應該做什麼？
   A) 重新啟動　　B) 呼叫 `scanner.close()`　　C) 什麼都不做　　D) 刪除變數

> 答案：1. C　2. C　3. B

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

### **練習 3：資料型別檢測器**
```java name=TypeChecker.java
import java.util.Scanner;

public class TypeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== 資料型別檢測 ===");

        System.out.print("請輸入一個整數：");
        int intValue = scanner.nextInt();

        System.out.print("請輸入一個小數：");
        double doubleValue = scanner.nextDouble();

        System.out.print("請輸入一個字元：");
        char charValue = scanner.next().charAt(0);

        // 型別轉換展示
        System.out.println("\n=== 型別轉換結果 ===");
        System.out.println("int 轉 double：" + (double) intValue);
        System.out.println("double 轉 int（截斷）：" + (int) doubleValue);
        System.out.println("字元 " + charValue + " 的 Unicode：" + (int) charValue);

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
   System.out.print("不換行輸出");
   System.out.printf("格式化輸出：%.2f", 數值);
   ```

4. **輸入語句**：
   ```java
   Scanner scanner = new Scanner(System.in);
   資料型別 變數 = scanner.next對應方法();
   ```

### **8 種基本資料型別速記表**
| 型別 | 大小 | 口訣 |
|------|------|------|
| `byte` | 1 byte | 位元組小整數 |
| `short` | 2 bytes | 短整數 |
| `int` | 4 bytes | 預設整數 (最常用) |
| `long` | 8 bytes | 長整數加 L |
| `float` | 4 bytes | 單精度浮點數加 f |
| `double` | 8 bytes | 預設浮點數 (最常用) |
| `char` | 2 bytes | 單一字元用單引號 |
| `boolean` | — | 真與假 |

### **常見錯誤**
1. **忘記分號**：每個語句結尾要加 `;`
2. **大小寫錯誤**：Java 區分大小寫（`String` 不是 `string`）
3. **忘記 import**：使用 Scanner 要加 `import java.util.Scanner;`
4. **類別名稱與檔案名稱不一致**
5. **型別範圍溢位**：將過大數值存入 `byte` 或 `short`
6. **浮點數未加後綴**：`float f = 3.14;` 應寫為 `float f = 3.14f;`

---

## 📝 自我測驗

### **一、選擇題（每題 10 分）**

1. 下列哪個是 Java 的參考資料型別？
   A) int　　B) double　　C) String　　D) boolean

2. `char` 在 Java 中佔用多少空間？
   A) 1 byte　　B) 2 bytes　　C) 4 bytes　　D) 8 bytes

3. 執行 `System.out.println("Hello" + 1 + 2);` 會輸出什麼？
   A) Hello3　　B) Hello12　　C) Hello 1 2　　D) 編譯錯誤

4. 下列何者不是合法的 Java 變數名稱？
   A) `_value`　　B) `$money`　　C) `1stPlace`　　D) `myVar`

5. `boolean` 型別的可能值為？
   A) 0 或 1　　B) true 或 false　　C) YES 或 NO　　D) ON 或 OFF

### **二、填空題（每題 10 分）**

1. Java 原始碼的副檔名為 ______，編譯後的副檔名為 ______。
2. `double` 轉 `int` 需要使用 ______ 轉換。
3. `long` 型別的數值結尾需加上字母 ______。
4. 輸出後換行的方法是 ______。
5. 建立 Scanner 物件的語法是 `Scanner sc = ______;`。

### **三、除錯練習（每題 10 分）**

找出下列程式碼的錯誤：

```java
// 題目 1
public class Test {
    public static void main(string[] args) {
        System.out.println("Hello")
    }
}
```

```java
// 題目 2
public class Test {
    public static void main(String[] args) {
        int num = 10.5;
        System.out.println(num);
    }
}
```

```java
// 題目 3
public class test {
    public static void main(String[] args) {
        scanner sc = new scanner(System.in);
        int age = sc.nextInt();
    }
}
```

### **自我測驗答案**
**一、選擇題：** 1. C　2. B　3. B（字串串接，`"Hello" + 1` → `"Hello1"`，再 `+ 2` → `"Hello12"`）　4. C　5. B

**二、填空題：** 1. `.java`、`.class`　2. 強制（顯式）　3. `L`　4. `System.out.println()`　5. `new Scanner(System.in)`

**三、除錯練習：**
1. `string` 應為 `String`（大寫 S）；結尾缺少分號 `;`
2. `int num = 10.5;` → `double` 不能直接存入 `int`，應改為 `double num = 10.5;` 或 `int num = (int) 10.5;`
3. `scanner` 和 `Scanner` 大小寫錯誤；缺少 `import java.util.Scanner;`

---

## 🏠 課後作業

### **作業 1：溫度轉換器**
撰寫程式將攝氏溫度轉換為華氏溫度
- 公式：華氏 = 攝氏 × 9/5 + 32
- 使用 `double` 型別
- 輸入攝氏溫度，輸出華氏溫度（取到小數第 2 位）

### **作業 2：購物清單**
輸入三件商品的單價與數量，計算總金額
- 使用 `int` 或 `double` 儲存單價與數量
- 使用 `String` 儲存商品名稱
- 輸出每件商品的小計與總金額

### **作業 3：學生成績**
輸入學生姓名和三科成績，計算平均分數
- 成績使用 `int` 型別
- 平均分數使用 `double` 型別（注意型別轉換）
- 輸出時顯示各科成績與平均分數

### **作業 4：型別轉換練習**
1. 宣告 `int a = 255;`，將其轉為 `byte` 後輸出，觀察結果
2. 宣告 `double d = 3.14159;`，將其轉為 `int` 後輸出
3. 宣告 `char c = 'A';`，將其轉為 `int` 後輸出 Unicode 編碼
4. 思考：為什麼 `byte b = (byte) 300;` 會得到 44？

---

## 🔍 進階補充：資料型別細節

### **整數型別比較**
```java
byte  b = 127;          // byte 最大值
b++;                    // 溢位！變成 -128（迴繞）
System.out.println(b);  // -128
```

### **浮點數精度注意**
```java
double result = 0.1 + 0.2;
System.out.println(result);       // 0.30000000000000004（非 0.3）
// 原因：浮點數二進位表示無法精確表達某些十進位小數
```

### **字串與 char 的區別**
```java
char c = 'A';           // 單一字元，使用單引號
String s = "Hello";     // 字串（多個字元），使用雙引號
// char c2 = "A";       // ❌ 編譯錯誤：型別不符
// String s2 = 'Hello'; // ❌ 編譯錯誤：型別不符
```

---

這樣的教學內容涵蓋了完整的 Java 資料型別介紹，並加入了複習小站、自我測驗與除錯練習，方便學生課後復習與練習！
