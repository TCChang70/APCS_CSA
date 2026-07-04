# 📝 第一單元：Java 基礎入門 考題

## 🎯 考試說明
- **考試時間**：80 分鐘
- **總分**：100 分
- **考試範圍**：Java 基礎語法、變數、運算子、輸入輸出
- **注意事項**：請仔細閱讀題目，程式碼需要完整且可執行

---

## 📚 第一部分：基礎概念題 (30分)

### **題目 1：選擇題 (每題 2 分，共 16 分)**

1. Java 程式的執行流程正確順序為：
   - A) .java → JVM → .class → javac
   - B) .java → javac → .class → JVM
   - C) .class → .java → javac → JVM
   - D) JVM → .java → javac → .class

2. 下列哪個是 Java 的基本資料型別？
   - A) `String`
   - B) `Integer`
   - C) `int`
   - D) `Array`

3. 在 Java 中，下列哪個變數名稱是合法的？
   - A) `2student`
   - B) `student-age`
   - C) `student_age`
   - D) `class`

4. 下列哪個運算子用於取餘數？
   - A) `/`
   - B) `%`
   - C) `*`
   - D) `+`

5. Java 區分大小寫，下列哪組變數名稱會被認為是不同的變數？
   - A) `age` 和 `Age`
   - B) `name` 和 `name`
   - C) `score` 和 `score`
   - D) 以上皆非

6. 要在 Java 中使用 Scanner 類別，需要加入哪個 import 語句？
   - A) `import java.io.Scanner;`
   - B) `import java.util.Scanner;`
   - C) `import java.lang.Scanner;`
   - D) `import Scanner;`

7. 下列哪個是正確的 Java 程式進入點？
   - A) `public static void main(String args)`
   - B) `public static void main(String[] args)`
   - C) `public void main(String[] args)`
   - D) `static void main(String[] args)`

8. 在 Java 中，單行註解使用什麼符號？
   - A) `/* */`
   - B) `//`
   - C) `#`
   - D) `--`

### **題目 2：填空題 (每空 2 分，共 14 分)**

請在空格中填入適當的程式碼：

```java
_______ java.util.Scanner;

public _______ HelloWorld {
    public static void main(_______[] args) {
        Scanner scanner = new _______(_______);
        
        System.out._______("請輸入您的姓名：");
        String name = scanner._______();
        
        scanner._______();
    }
}


## 💻 第二部分：程式設計題 (55分)

### **題目 3：個人資料登記系統 (15分)**

撰寫一個程式，要求使用者輸入個人資料並顯示結果：

**需求規格：**
- 輸入：姓名、年齡、身高(公分)、體重(公斤)
- 計算並顯示 BMI 值（保留兩位小數）
- BMI 公式：體重(kg) ÷ (身高(m))²
- 根據 BMI 值顯示健康狀態：
  - BMI < 18.5：體重過輕
  - 18.5 ≤ BMI < 24：正常範圍
  - 24 ≤ BMI < 27：過重
  - BMI ≥ 27：肥胖

**程式架構：**
```java
import java.util.Scanner;

public class PersonalInfo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 在此處實作您的程式碼
        
        scanner.close();
    }
}
```

**預期輸出範例：**
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

**評分標準：**
- 輸入處理 (4分)
- BMI 計算正確 (4分)
- 健康狀態判定 (4分)
- 輸出格式 (3分)

### **題目 4：多功能計算機 (20分)**

設計一個簡單的計算機程式，可以進行四則運算：

**需求規格：**
1. **輸入**：兩個數字和一個運算符號 (+, -, *, /)
2. **功能**：
   - 支援加法、減法、乘法、除法
   - 除法需要檢查除數是否為零
   - 結果保留兩位小數
3. **錯誤處理**：
   - 除數為零時顯示錯誤訊息
   - 無效運算符號時顯示錯誤訊息

**預期互動範例：**
```
=== 多功能計算機 ===
請輸入第一個數字：10
請輸入運算符號 (+, -, *, /)：/
請輸入第二個數字：3
計算結果：10.00 ÷ 3.00 = 3.33
```

**特殊情況範例：**
```
請輸入第一個數字：10
請輸入運算符號 (+, -, *, /)：/
請輸入第二個數字：0
❌ 錯誤：除數不能為零！
```

**評分標準：**
- 基本四則運算 (8分)
- 除零檢查 (4分)
- 錯誤處理 (4分)
- 輸出格式與使用者體驗 (4分)

### **題目 5：學生成績統計系統 (20分)**

撰寫一個程式計算學生的成績統計：

**需求規格：**
1. **輸入**：學生姓名和三科成績（國文、英文、數學）
2. **計算**：
   - 總分
   - 平均分數（保留兩位小數）
   - 最高分科目
   - 最低分科目
3. **輸出**：完整的成績報表

**程式架構：**
```java
import java.util.Scanner;

public class GradeReport {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 在此處實作您的程式碼
        
        scanner.close();
    }
}
```

**預期輸出範例：**
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

**評分標準：**
- 成績輸入與儲存 (5分)
- 總分與平均計算 (5分)
- 最高分最低分判定 (6分)
- 報表格式與完整性 (4分)

---

## 🔍 第三部分：程式碼閱讀與分析 (15分)

### **題目 6：程式碼追蹤 (8分)**

請閱讀下列程式碼並回答問題：

```java
public class CodeTrace {
    public static void main(String[] args) {
        int a = 15;
        int b = 4;
        
        int result1 = a / b;
        double result2 = (double) a / b;
        int result3 = a % b;
        
        boolean flag1 = (a > 10) && (b < 5);
        boolean flag2 = (a == 15) || (b > 10);
        
        System.out.println("result1 = " + result1);
        System.out.println("result2 = " + result2);
        System.out.println("result3 = " + result3);
        System.out.println("flag1 = " + flag1);
        System.out.println("flag2 = " + flag2);
    }
}
```

**問題：**
1. `result1` 的值是多少？為什麼？(2分)
2. `result2` 的值是多少？與 `result1` 有什麼差別？(2分)
3. `result3` 的值是多少？`%` 運算子的作用是什麼？(2分)
4. `flag1` 和 `flag2` 的值分別是多少？請說明邏輯運算的過程。(2分)

### **題目 7：找出錯誤 (7分)**

下列程式碼有多個錯誤，請找出並說明如何修正：

```java
import java.util.scanner;

public class buggyProgram {
    public static void Main(String[] args) {
        Scanner input = new Scanner(System.in)
        
        System.out.println("請輸入您的年齡：");
        int Age = input.nextInt();
        
        System.out.println("請輸入您的姓名：")
        String name = input.nextline();
        
        double result = Age * 12
        
        System.out.println("姓名：" + name);
        System.out.println(Age + "歲等於" + result + "個月");
        
        input.close()
    }
}
```

**要求：**
1. 列出所有錯誤 (4分)
2. 提供修正後的程式碼 (3分)



## 🎯 考試重點提醒

### **基礎語法重點：**
- 程式基本結構：`public class` 和 `main` 方法
- 變數宣告與命名規則
- 基本資料型別：`int`, `double`, `String`, `boolean`
- 輸入輸出：`System.out.println()` 和 `Scanner`

### **運算子重點：**
- 算術運算子：`+`, `-`, `*`, `/`, `%`
- 比較運算子：`==`, `!=`, `>`, `<`, `>=`, `<=`
- 邏輯運算子：`&&`, `||`, `!`
- 型別轉換：明確轉換和自動轉換

### **常見錯誤：**
- 忘記分號 `;`
- 大小寫錯誤
- Import 語句錯誤
- Scanner 方法使用錯誤
- 忘記關閉 Scanner

### **程式設計技巧：**
- 適當的變數命名
- 清楚的輸出格式
- 基本的錯誤處理
- 程式碼的可讀性

**祝考試順利！** 🍀