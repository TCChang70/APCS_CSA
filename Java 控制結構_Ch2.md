# 📚 第二單元：控制結構 - 詳細教學內容

## 🎯 單元學習目標
- 理解程式流程控制的重要性
- 掌握條件判斷語句的使用
- 學會各種迴圈結構的應用
- 能夠解決複雜的邏輯問題

---

## 🔀 2.1 條件判斷

### **為什麼需要條件判斷？**
程式就像人的思考過程，需要根據不同情況做出不同的決定。

**生活比喻：**
```
如果下雨 → 帶雨傘
否則 → 不帶雨傘

如果考試成績 >= 60 → 及格
否則 → 不及格
```

### **基本 if-else 語句**
```java name=BasicIfElse.java
import java.util.Scanner;

public class BasicIfElse {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("請輸入您的年齡：");
        int age = scanner.nextInt();
        
        // 基本 if-else
        if (age >= 18) {
            System.out.println("您已成年，可以投票！");
        } else {
            System.out.println("您未成年，還不能投票。");
        }
        
        scanner.close();
    }
}
```

### **多重條件判斷 (if-else if-else)**
```java name=MultipleConditions.java
import java.util.Scanner;

public class MultipleConditions {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("請輸入考試分數（0-100）：");
        int score = scanner.nextInt();
        
        // 多重條件判斷
        if (score >= 90) {
            System.out.println("等級：A+ 優秀！");
        } else if (score >= 80) {
            System.out.println("等級：A 良好！");
        } else if (score >= 70) {
            System.out.println("等級：B 普通");
        } else if (score >= 60) {
            System.out.println("等級：C 及格");
        } else {
            System.out.println("等級：F 不及格");
        }
        
        scanner.close();
    }
}
```

### **比較運算子詳解**
```java name=ComparisonOperators.java
public class ComparisonOperators {
    public static void main(String[] args) {
        int a = 10, b = 20;
        
        System.out.println("a = " + a + ", b = " + b);
        System.out.println();
        
        // 各種比較運算子
        System.out.println("a == b: " + (a == b));  // 等於
        System.out.println("a != b: " + (a != b));  // 不等於
        System.out.println("a > b: " + (a > b));    // 大於
        System.out.println("a < b: " + (a < b));    // 小於
        System.out.println("a >= b: " + (a >= b));  // 大於等於
        System.out.println("a <= b: " + (a <= b));  // 小於等於
        
        // 字串比較（重要！）
        String str1 = "Hello";
        String str2 = "Hello";
        String str3 = new String("Hello");
        
        System.out.println("\n=== 字串比較 ===");
        System.out.println("str1 == str2: " + (str1 == str2));         // true
        System.out.println("str1 == str3: " + (str1 == str3));         // false
        System.out.println("str1.equals(str3): " + str1.equals(str3)); // true（正確方法）
    }
}
```

### **邏輯運算子**
```java name=LogicalOperators.java
import java.util.Scanner;

public class LogicalOperators {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("請輸入年齡：");
        int age = scanner.nextInt();
        
        System.out.print("是否有駕照？(true/false)：");
        boolean hasLicense = scanner.nextBoolean();
        
        System.out.print("請輸入收入（萬元）：");
        double income = scanner.nextDouble();
        
        // && (AND) 邏輯且
        if (age >= 18 && hasLicense) {
            System.out.println("✅ 可以開車");
        } else {
            System.out.println("❌ 不能開車");
        }
        
        // || (OR) 邏輯或
        if (age >= 65 || income < 30) {
            System.out.println("✅ 符合優惠條件");
        } else {
            System.out.println("❌ 不符合優惠條件");
        }
        
        // ! (NOT) 邏輯非
        if (!hasLicense) {
            System.out.println("⚠️ 建議考取駕照");
        }
        
        // 複合條件
        if ((age >= 18 && age <= 65) && (income >= 20 && income <= 100)) {
            System.out.println("✅ 符合貸款申請條件");
        }
        
        scanner.close();
    }
}
```

### **巢狀條件**
```java name=NestedConditions.java
import java.util.Scanner;

public class NestedConditions {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("請輸入天氣狀況 (sunny/rainy/cloudy)：");
        String weather = scanner.next();
        
        System.out.print("請輸入溫度（攝氏）：");
        int temperature = scanner.nextInt();
        
        // 巢狀條件判斷
        if (weather.equals("sunny")) {
            if (temperature > 30) {
                System.out.println("🌞 天氣炎熱，建議：");
                System.out.println("- 穿短袖衣物");
                System.out.println("- 多喝水");
                System.out.println("- 避免長時間曝曬");
            } else if (temperature > 20) {
                System.out.println("☀️ 天氣舒適，建議：");
                System.out.println("- 穿輕便衣物");
                System.out.println("- 適合戶外活動");
            } else {
                System.out.println("🌤️ 天氣涼爽，建議：");
                System.out.println("- 穿長袖衣物");
                System.out.println("- 享受陽光");
            }
        } else if (weather.equals("rainy")) {
            System.out.println("🌧️ 下雨天，建議：");
            System.out.println("- 攜帶雨具");
            System.out.println("- 注意路面濕滑");
            if (temperature < 15) {
                System.out.println("- 穿保暖衣物");
            }
        } else {
            System.out.println("☁️ 陰天，建議穿適中衣物");
        }
        
        scanner.close();
    }
}
```

---

## 🔄 2.2 迴圈結構

### **為什麼需要迴圈？**
當我們需要重複執行相同的動作時，迴圈可以大大簡化程式碼。

**生活比喻：**
```
做 10 個伏地挺身 = 重複「做伏地挺身」這個動作 10 次
倒數計時 = 從某個數字開始，重複「減 1」直到 0
```

### **for 迴圈**
```java name=ForLoop.java
public class ForLoop {
    public static void main(String[] args) {
        // 基本 for 迴圈
        System.out.println("=== 數數 1 到 10 ===");
        for (int i = 1; i <= 10; i++) {
            System.out.println("第 " + i + " 次");
        }
        
        // 倒數計時
        System.out.println("\n=== 倒數計時 ===");
        for (int i = 10; i >= 1; i--) {
            System.out.println(i);
        }
        System.out.println("發射！🚀");
        
        // 步進值不是 1
        System.out.println("\n=== 偶數 0 到 20 ===");
        for (int i = 0; i <= 20; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        // 九九乘法表
        System.out.println("\n=== 九九乘法表 ===");
        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                System.out.printf("%d x %d = %2d  ", i, j, i * j);
            }
            System.out.println(); // 換行
        }
    }
}
```

### **while 迴圈**
```java name=WhileLoop.java
import java.util.Scanner;
import java.util.Random;

public class WhileLoop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        // 基本 while 迴圈
        System.out.println("=== 數數遊戲 ===");
        int count = 1;
        while (count <= 5) {
            System.out.println("計數：" + count);
            count++;
        }
        
        // 猜數字遊戲
        System.out.println("\n=== 猜數字遊戲 ===");
        int secretNumber = random.nextInt(100) + 1; // 1-100
        int guess = 0;
        int attempts = 0;
        
        System.out.println("我想了一個 1-100 的數字，你能猜到嗎？");
        
        while (guess != secretNumber) {
            System.out.print("請輸入你的猜測：");
            guess = scanner.nextInt();
            attempts++;
            
            if (guess < secretNumber) {
                System.out.println("太小了！再試試看。");
            } else if (guess > secretNumber) {
                System.out.println("太大了！再試試看。");
            } else {
                System.out.println("🎉 恭喜！你猜對了！");
                System.out.println("你總共猜了 " + attempts + " 次。");
            }
        }
        
        // 帳號密碼驗證
        System.out.println("\n=== 登入系統 ===");
        String correctPassword = "java123";
        String inputPassword = "";
        
        while (!inputPassword.equals(correctPassword)) {
            System.out.print("請輸入密碼：");
            inputPassword = scanner.next();
            
            if (!inputPassword.equals(correctPassword)) {
                System.out.println("❌ 密碼錯誤，請重新輸入！");
            }
        }
        System.out.println("✅ 登入成功！");
        
        scanner.close();
    }
}
```

### **do-while 迴圈**
```java name=DoWhileLoop.java
import java.util.Scanner;

public class DoWhileLoop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // do-while 特色：至少執行一次
        System.out.println("=== 簡單選單系統 ===");
        
        int choice;
        do {
            // 顯示選單
            System.out.println("\n請選擇功能：");
            System.out.println("1. 查看個人資料");
            System.out.println("2. 修改密碼");
            System.out.println("3. 查看歷史記錄");
            System.out.println("0. 離開程式");
            System.out.print("請輸入選項 (0-3)：");
            
            choice = scanner.nextInt();
            
            // 處理選擇
            switch (choice) {
                case 1:
                    System.out.println("📋 顯示個人資料...");
                    break;
                case 2:
                    System.out.println("🔐 修改密碼...");
                    break;
                case 3:
                    System.out.println("📚 查看歷史記錄...");
                    break;
                case 0:
                    System.out.println("👋 感謝使用，再見！");
                    break;
                default:
                    System.out.println("❌ 無效選項，請重新選擇！");
            }
            
        } while (choice != 0);
        
        // 另一個範例：輸入驗證
        System.out.println("\n=== 年齡輸入驗證 ===");
        int age;
        do {
            System.out.print("請輸入您的年齡 (1-120)：");
            age = scanner.nextInt();
            
            if (age < 1 || age > 120) {
                System.out.println("❌ 年齡必須在 1-120 之間！");
            }
        } while (age < 1 || age > 120);
        
        System.out.println("✅ 年齡輸入成功：" + age + " 歲");
        
        scanner.close();
    }
}
```

### **迴圈控制 (break 和 continue)**
```java name=LoopControl.java
import java.util.Scanner;

public class LoopControl {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // break 範例：提前結束迴圈
        System.out.println("=== break 範例：找到第一個偶數就停止 ===");
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) {
                System.out.println("找到第一個偶數：" + i);
                break; // 立即結束迴圈
            }
            System.out.println("檢查數字：" + i);
        }
        
        // continue 範例：跳過某些迭代
        System.out.println("\n=== continue 範例：只顯示奇數 ===");
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) {
                continue; // 跳過這次迭代，繼續下一次
            }
            System.out.print(i + " ");
        }
        System.out.println();
        
        // 實際應用：安全的除法計算
        System.out.println("\n=== 除法計算器 ===");
        while (true) {
            System.out.print("請輸入被除數 (輸入 0 結束)：");
            double dividend = scanner.nextDouble();
            
            if (dividend == 0) {
                System.out.println("程式結束！");
                break;
            }
            
            System.out.print("請輸入除數：");
            double divisor = scanner.nextDouble();
            
            if (divisor == 0) {
                System.out.println("❌ 除數不能為 0，請重新輸入！");
                continue;
            }
            
            double result = dividend / divisor;
            System.out.printf("%.2f ÷ %.2f = %.2f\n", dividend, divisor, result);
        }
        
        // 巢狀迴圈中的 break 和 continue
        System.out.println("\n=== 巢狀迴圈控制 ===");
        outerLoop: // 標籤
        for (int i = 1; i <= 3; i++) {
            System.out.println("外層迴圈：" + i);
            
            for (int j = 1; j <= 5; j++) {
                if (j == 3) {
                    System.out.println("  跳過 j = 3");
                    continue;
                }
                
                if (i == 2 && j == 4) {
                    System.out.println("  遇到特殊條件，結束所有迴圈");
                    break outerLoop; // 跳出外層迴圈
                }
                
                System.out.println("  內層迴圈：" + j);
            }
        }
        
        scanner.close();
    }
}
```

---

## 🛠️ 實作練習

### **練習 1：成績統計系統**
```java name=GradeStatistics.java
import java.util.Scanner;

public class GradeStatistics {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("請輸入學生人數：");
        int studentCount = scanner.nextInt();
        
        int totalScore = 0;
        int highestScore = 0;
        int lowestScore = 100;
        int passCount = 0;
        
        for (int i = 1; i <= studentCount; i++) {
            System.out.print("請輸入第 " + i + " 位學生的成績：");
            int score = scanner.nextInt();
            
            // 累加總分
            totalScore += score;
            
            // 更新最高分
            if (score > highestScore) {
                highestScore = score;
            }
            
            // 更新最低分
            if (score < lowestScore) {
                lowestScore = score;
            }
            
            // 計算及格人數
            if (score >= 60) {
                passCount++;
            }
        }
        
        double average = (double) totalScore / studentCount;
        double passRate = (double) passCount / studentCount * 100;
        
        System.out.println("\n=== 成績統計結果 ===");
        System.out.println("學生人數：" + studentCount);
        System.out.printf("平均分數：%.2f\n", average);
        System.out.println("最高分數：" + highestScore);
        System.out.println("最低分數：" + lowestScore);
        System.out.println("及格人數：" + passCount);
        System.out.printf("及格率：%.1f%%\n", passRate);
        
        scanner.close();
    }
}
```

### **練習 2：數字金字塔**
```java name=NumberPyramid.java
import java.util.Scanner;

public class NumberPyramid {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("請輸入金字塔的層數：");
        int levels = scanner.nextInt();
        
        // 數字金字塔
        System.out.println("\n=== 數字金字塔 ===");
        for (int i = 1; i <= levels; i++) {
            // 印空格
            for (int j = 1; j <= levels - i; j++) {
                System.out.print(" ");
            }
            
            // 印數字
            for (int j = 1; j <= i; j++) {
                System.out.print(j + " ");
            }
            
            System.out.println(); // 換行
        }
        
        // 星號金字塔
        System.out.println("\n=== 星號金字塔 ===");
        for (int i = 1; i <= levels; i++) {
            // 印空格
            for (int j = 1; j <= levels - i; j++) {
                System.out.print(" ");
            }
            
            // 印星號
            for (int j = 1; j <= 2 * i - 1; j++) {
                System.out.print("*");
            }
            
            System.out.println(); // 換行
        }
        
        scanner.close();
    }
}
```

### **練習 3：質數檢測器**
```java name=PrimeChecker.java
import java.util.Scanner;

public class PrimeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.print("請輸入一個正整數 (輸入 0 結束)：");
            int number = scanner.nextInt();
            
            if (number == 0) {
                System.out.println("程式結束！");
                break;
            }
            
            if (number < 2) {
                System.out.println(number + " 不是質數");
                continue;
            }
            
            boolean isPrime = true;
            
            // 檢查是否為質數
            for (int i = 2; i <= Math.sqrt(number); i++) {
                if (number % i == 0) {
                    isPrime = false;
                    break;
                }
            }
            
            if (isPrime) {
                System.out.println(number + " 是質數 ✅");
            } else {
                System.out.println(number + " 不是質數 ❌");
            }
            
            // 列出範圍內的質數
            System.out.println("1 到 " + number + " 之間的質數：");
            for (int num = 2; num <= number; num++) {
                boolean isCurrentPrime = true;
                
                for (int i = 2; i <= Math.sqrt(num); i++) {
                    if (num % i == 0) {
                        isCurrentPrime = false;
                        break;
                    }
                }
                
                if (isCurrentPrime) {
                    System.out.print(num + " ");
                }
            }
            System.out.println("\n");
        }
        
        scanner.close();
    }
}
```

---

## 📝 重點整理

### **條件判斷語法**
```java
// 基本 if-else
if (條件) {
    // 條件為真時執行
} else {
    // 條件為假時執行
}

// 多重條件
if (條件1) {
    // 執行程式碼1
} else if (條件2) {
    // 執行程式碼2
} else {
    // 執行程式碼3
}
```

### **迴圈語法**
```java
// for 迴圈
for (初始化; 條件; 更新) {
    // 重複執行的程式碼
}

// while 迴圈
while (條件) {
    // 重複執行的程式碼
}

// do-while 迴圈
do {
    // 至少執行一次的程式碼
} while (條件);
```

### **迴圈控制**
- `break`：立即結束迴圈
- `continue`：跳過本次迭代，繼續下次迭代

### **常見應用場景**
1. **條件判斷**：成績評級、年齡分組、權限控制
2. **for 迴圈**：已知次數的重複動作、陣列遍歷
3. **while 迴圈**：條件未知的重複動作、遊戲主迴圈
4. **do-while 迴圈**：選單系統、輸入驗證

---

## 🏠 課後作業

### **作業 1：BMI 計算與建議系統**
- 輸入身高體重
- 計算 BMI
- 根據 BMI 值給出健康建議
- 使用迴圈讓使用者可以連續計算

### **作業 2：簡單的ATM系統**
- 模擬提款機操作
- 功能：查詢餘額、存款、提款、轉帳
- 使用密碼驗證
- 使用選單迴圈

### **作業 3：數學小遊戲**
- 隨機產生加減乘除題目
- 記錄答對答錯次數
- 計算正確率
- 可選擇難度等級

---

## 🔍 除錯技巧

### **常見錯誤**
1. **無窮迴圈**：忘記更新迴圈變數
2. **條件錯誤**：使用 `=` 而不是 `==`
3. **邏輯錯誤**：AND 和 OR 的混淆
4. **邊界條件**：`<` 和 `<=` 的差別

### **除錯方法**
```java
// 在關鍵位置加入除錯輸出
System.out.println("Debug: i = " + i);
System.out.println("Debug: 條件結果 = " + (age >= 18));
```

