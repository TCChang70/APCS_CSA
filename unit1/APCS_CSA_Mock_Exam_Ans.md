# APCS CSA 模擬考試
## 主題：Data Types, Operators, Scanner, If Statements

---

## 第一部分：選擇題 (Multiple Choice Questions) - 20 題

### Question 1
What is the result of the following code?
```java
int x = 5;
int y = 2;
double z = x / y;
System.out.println(z);
```
A) 2.5  
B) 2.0  
C) 2  
D) 3.0  
E) Compile-time error

**Answer: B**  
**Explanation:** Integer division (5/2) results in 2, which is then implicitly cast to double 2.0.

---

### Question 2
Which of the following correctly declares and initializes a constant in Java?
```java
A) const double PI = 3.14159;
B) final double PI = 3.14159;
C) static PI = 3.14159;
D) readonly double PI = 3.14159;
E) constant double PI = 3.14159;
```

**Answer: B**  
**Explanation:** Java uses `final` keyword to declare constants.

---

### Question 3
What is the output of the following code?
```java
int a = 10;
int b = 3;
System.out.println(a % b + " " + a / b);
```
A) 1 3  
B) 3 1  
C) 1.0 3.0  
D) 3.333 3  
E) Compile-time error

**Answer: A**  
**Explanation:** 10 % 3 = 1 (remainder), 10 / 3 = 3 (integer division).

---

### Question 4
Consider the following code:
```java
double x = 7.9;
int y = (int) x;
System.out.println(y);
```
What is printed?

A) 7  
B) 8  
C) 7.9  
D) 7.0  
E) Compile-time error

**Answer: A**  
**Explanation:** Casting double to int truncates the decimal part, not rounds.

---

### Question 5
What is the result of the following expression?
```java
int result = 5 + 3 * 2 - 8 / 4;
```
A) 6  
B) 9  
C) 10  
D) 12  
E) 14

**Answer: B**  
**Explanation:** Following order of operations: 5 + 6 - 2 = 9

---

### Question 6
Which Scanner method should be used to read a single word (token) from input?
```java
A) nextLine()
B) next()
C) nextWord()
D) readWord()
E) getWord()
```

**Answer: B**  
**Explanation:** `next()` reads a single token up to whitespace.

---

### Question 7
What is the output?
```java
int x = 5;
if (x > 3)
    if (x < 10)
        System.out.print("A");
    else
        System.out.print("B");
else
    System.out.print("C");
```
A) A  
B) B  
C) C  
D) AB  
E) No output

**Answer: A**  
**Explanation:** The nested if structure: x > 3 is true, x < 10 is true, so "A" is printed.

---

### Question 8
Consider the following code:
```java
Scanner scan = new Scanner(System.in);
int num = scan.nextInt();
String line = scan.nextLine();
```
If the input is "42 Hello World", what is stored in `line`?

A) "42 Hello World"  
B) "Hello World"  
C) " Hello World"  
D) ""  
E) "Hello"

**Answer: C**  
**Explanation:** `nextInt()` reads "42" but leaves the space. `nextLine()` reads from current position to end of line: " Hello World".

---

### Question 9
What is the value of `result`?
```java
boolean a = true;
boolean b = false;
boolean result = a || b && !a;
```
A) true  
B) false  
C) Compile-time error  
D) Runtime error  
E) Depends on input

**Answer: A**  
**Explanation:** && has higher precedence than ||. Expression: true || (false && false) = true || false = true

---

### Question 10
Which of the following will cause a compile-time error?
```java
A) int x = 5.0;
B) double y = 5;
C) char c = 65;
D) boolean b = true;
E) String s = "Hello";
```

**Answer: A**  
**Explanation:** Cannot assign double (5.0) to int without explicit cast.

---

### Question 11
What is printed?
```java
int score = 85;
if (score >= 90)
    System.out.print("A");
if (score >= 80)
    System.out.print("B");
if (score >= 70)
    System.out.print("C");
```
A) A  
B) B  
C) C  
D) BC  
E) ABC

**Answer: D**  
**Explanation:** These are three separate if statements, not else-if. Both second and third conditions are true.

---

### Question 12
What is the output?
```java
int x = 10;
x += 5;
x *= 2;
x -= 8;
System.out.println(x);
```
A) 22  
B) 27  
C) 30  
D) 32  
E) 42

**Answer: A**  
**Explanation:** x = 10 → x = 15 → x = 30 → x = 22

---

### Question 13
Consider this code using Scanner:
```java
Scanner input = new Scanner(System.in);
double price = input.nextDouble();
int quantity = input.nextInt();
```
Which input would cause a runtime error?

A) 25.99 5  
B) 25 5  
C) 25.0 5  
D) ABC 5  
E) All of the above

**Answer: D**  
**Explanation:** "ABC" cannot be parsed as a double, causing InputMismatchException.

---

### Question 14
What is the result?
```java
int a = 15;
int b = 4;
boolean result = (a > 10) && (b++ > 5);
System.out.println(b);
```
A) 4  
B) 5  
C) true  
D) false  
E) Compile-time error

**Answer: A**  
**Explanation:** (b++ > 5) is never evaluated due to short-circuit evaluation since (a > 10) is true but (4 > 5) would be false, so the && short-circuits. Wait, let me reconsider: (a > 10) is true (15 > 10), so it must evaluate the second part. b is 4, b++ > 5 means 4 > 5 which is false. But b++ means b becomes 5 AFTER the comparison. So b would be 5. Let me reconsider the logic again.

Actually, with &&, both sides must be evaluated (no short-circuit happens when first is true). So b++ > 5 means: compare current value 4 > 5 (false), then increment b to 5. So b = 5.

**Correction: Answer should be B (5)**

---

### Question 15
Which expression correctly checks if a number `n` is between 10 and 20 (inclusive)?

A) `10 <= n <= 20`  
B) `n >= 10 && n <= 20`  
C) `n => 10 && n =< 20`  
D) `10 <= n || n <= 20`  
E) `(n > 10) && (n < 20)`

**Answer: B**  
**Explanation:** Java requires separate boolean comparisons connected with &&.

---

### Question 16
What is the output?
```java
String str = "123";
int num = Integer.parseInt(str);
num += 7;
System.out.println(num);
```
A) 1237  
B) 130  
C) 123  
D) 7  
E) Compile-time error

**Answer: B**  
**Explanation:** parseInt converts "123" to integer 123, then 123 + 7 = 130.

---

### Question 17
Consider the following:
```java
int x = 5;
int y = 10;
int z = ++x + y++;
System.out.println(x + " " + y + " " + z);
```
What is printed?

A) 5 10 15  
B) 6 11 16  
C) 6 10 16  
D) 6 11 15  
E) 5 11 15

**Answer: B**  
**Explanation:** ++x increments x to 6 before use. y++ uses 10 then increments to 11. z = 6 + 10 = 16.

---

### Question 18
What happens when this code executes with input "Hello 123"?
```java
Scanner sc = new Scanner(System.in);
int number = sc.nextInt();
```
A) number = 123  
B) number = 0  
C) InputMismatchException  
D) Compile-time error  
E) NullPointerException

**Answer: C**  
**Explanation:** `nextInt()` tries to read "Hello" as an integer, causing InputMismatchException.

---

### Question 19
What is the value of `result`?
```java
int a = 5, b = 10, c = 15;
boolean result = (a < b) && (b < c) || (a > c);
```
A) true  
B) false  
C) Compile-time error  
D) Cannot be determined  
E) Runtime error

**Answer: A**  
**Explanation:** (5 < 10) && (10 < 15) = true && true = true. true || (5 > 15) = true || false = true.

---

### Question 20
Which of the following is NOT a valid way to check if two integers are equal?
```java
A) if (a == b)
B) if (a.equals(b))
C) if (!(a != b))
D) if (a - b == 0)
E) Both B and D
```

**Answer: B**  
**Explanation:** Primitive types (int) don't have methods. `equals()` is for objects only.

---

## 第二部分：Free Response Questions (FRQ) - 4 題

---

### FRQ 1: Grade Calculator (較高難度)
**難度：★★★★☆**

Write a complete Java program that:
1. Uses Scanner to read a student's name and five exam scores (as doubles)
2. Calculates the average of the scores
3. Determines the letter grade based on the following scale:
   - A: 90-100
   - B: 80-89
   - C: 70-79
   - D: 60-69
   - F: below 60
4. Handles invalid input (scores outside 0-100 range) by displaying an error message and using 0 for that score
5. Displays the student's name, average, and letter grade with exactly 2 decimal places

**Example Output:**
```
Enter student name: John Smith
Enter score 1: 95.5
Enter score 2: 88.0
Enter score 3: 92.5
Enter score 4: 110.0
Invalid score! Using 0.
Enter score 5: 87.5
Student: John Smith
Average: 72.70
Grade: C
```

**示範解答：**
```java
import java.util.Scanner;

public class GradeCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter student name: ");
        String name = input.nextLine();
        
        double sum = 0.0;
        int validScores = 5;
        
        for (int i = 1; i <= 5; i++) {
            System.out.print("Enter score " + i + ": ");
            double score = input.nextDouble();
            
            if (score < 0 || score > 100) {
                System.out.println("Invalid score! Using 0.");
                score = 0;
            }
            sum += score;
        }
        
        double average = sum / validScores;
        String grade;
        
        if (average >= 90) {
            grade = "A";
        } else if (average >= 80) {
            grade = "B";
        } else if (average >= 70) {
            grade = "C";
        } else if (average >= 60) {
            grade = "D";
        } else {
            grade = "F";
        }
        
        System.out.printf("Student: %s%n", name);
        System.out.printf("Average: %.2f%n", average);
        System.out.println("Grade: " + grade);
        
        input.close();
    }
}
```

**評分標準：**
- Scanner 正確使用和資源管理：2 分
- 正確讀取並儲存學生姓名：1 分
- 正確讀取五個分數：2 分
- 有效處理無效輸入（0-100 範圍外）：2 分
- 正確計算平均值：2 分
- 正確的 if-else 分級邏輯：3 分
- 正確格式化輸出（兩位小數）：2 分
- 總分：14 分

---

### FRQ 2: Advanced Calculator with Type Handling (較高難度)
**難度：★★★★★**

Write a Java program that implements a calculator with the following requirements:

1. Read two numbers from the user using Scanner
2. Read an operator (+, -, *, /, %, ^) where ^ means power
3. Handle both integer and floating-point operations:
   - If both inputs are integers AND the operator is +, -, *, or %, perform integer arithmetic
   - Otherwise, perform floating-point arithmetic
4. Handle division by zero with appropriate error message
5. For the power operator (^), calculate the first number raised to the power of the second
6. Display the result with appropriate type (int or double)

**Example Output:**
```
Enter first number: 10
Enter second number: 3
Enter operator (+, -, *, /, %, ^): %
Result (int): 1

Enter first number: 10.5
Enter second number: 2
Enter operator (+, -, *, /, %, ^): *
Result (double): 21.0
```

**示範解答：**
```java
import java.util.Scanner;

public class AdvancedCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter first number: ");
        String input1 = scanner.next();
        System.out.print("Enter second number: ");
        String input2 = scanner.next();
        System.out.print("Enter operator (+, -, *, /, %, ^): ");
        String operator = scanner.next();
        
        boolean isInt1 = isInteger(input1);
        boolean isInt2 = isInteger(input2);
        
        if (isInt1 && isInt2 && !operator.equals("/") && !operator.equals("^")) {
            // Integer arithmetic
            int num1 = Integer.parseInt(input1);
            int num2 = Integer.parseInt(input2);
            int result = 0;
            boolean validOperation = true;
            
            if (operator.equals("+")) {
                result = num1 + num2;
            } else if (operator.equals("-")) {
                result = num1 - num2;
            } else if (operator.equals("*")) {
                result = num1 * num2;
            } else if (operator.equals("%")) {
                if (num2 == 0) {
                    System.out.println("Error: Division by zero!");
                    validOperation = false;
                } else {
                    result = num1 % num2;
                }
            } else {
                System.out.println("Invalid operator!");
                validOperation = false;
            }
            
            if (validOperation) {
                System.out.println("Result (int): " + result);
            }
        } else {
            // Double arithmetic
            double num1 = Double.parseDouble(input1);
            double num2 = Double.parseDouble(input2);
            double result = 0.0;
            boolean validOperation = true;
            
            if (operator.equals("+")) {
                result = num1 + num2;
            } else if (operator.equals("-")) {
                result = num1 - num2;
            } else if (operator.equals("*")) {
                result = num1 * num2;
            } else if (operator.equals("/")) {
                if (num2 == 0.0) {
                    System.out.println("Error: Division by zero!");
                    validOperation = false;
                } else {
                    result = num1 / num2;
                }
            } else if (operator.equals("%")) {
                if (num2 == 0.0) {
                    System.out.println("Error: Division by zero!");
                    validOperation = false;
                } else {
                    result = num1 % num2;
                }
            } else if (operator.equals("^")) {
                result = Math.pow(num1, num2);
            } else {
                System.out.println("Invalid operator!");
                validOperation = false;
            }
            
            if (validOperation) {
                System.out.println("Result (double): " + result);
            }
        }
        
        scanner.close();
    }
    
    private static boolean isInteger(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}
```

**評分標準：**
- 正確讀取輸入：2 分
- 判斷數據類型（整數 vs 浮點數）：3 分
- 正確處理整數運算：3 分
- 正確處理浮點數運算：3 分
- 除零錯誤處理：2 分
- 冪運算實現：2 分
- 適當的輸出格式：2 分
- Helper 方法設計：2 分
- 總分：19 分

---

### FRQ 3: Smart Data Validator (較高難度)
**難度：★★★★☆**

Write a Java program that validates user registration data with the following requirements:

1. Read username (String), age (int), email (String), and password (String) using Scanner
2. Validate each field with the following rules:
   - Username: 5-15 characters, no spaces
   - Age: between 13 and 120
   - Email: must contain exactly one '@' symbol and at least one '.' after '@'
   - Password: at least 8 characters, contains at least one digit and one letter
3. Display specific error messages for each validation failure
4. Display "Registration successful!" only if all validations pass
5. Use appropriate data types and operators for all validations

**Example Output:**
```
Enter username: john_doe
Enter age: 25
Enter email: john@example.com
Enter password: Pass1234
Registration successful!

Enter username: jd
Enter age: 150
Enter email: invalidemail
Enter password: short
Errors:
- Username must be 5-15 characters
- Age must be between 13 and 120
- Email must contain @ and domain
- Password must be at least 8 characters and contain letters and digits
```

**示範解答：**
```java
import java.util.Scanner;

public class SmartDataValidator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter username: ");
        String username = scanner.nextLine();
        System.out.print("Enter age: ");
        int age = scanner.nextInt();
        scanner.nextLine(); // consume newline
        System.out.print("Enter email: ");
        String email = scanner.nextLine();
        System.out.print("Enter password: ");
        String password = scanner.nextLine();
        
        boolean valid = true;
        StringBuilder errors = new StringBuilder();
        
        // Validate username
        if (username.length() < 5 || username.length() > 15 || username.contains(" ")) {
            valid = false;
            errors.append("- Username must be 5-15 characters with no spaces\n");
        }
        
        // Validate age
        if (age < 13 || age > 120) {
            valid = false;
            errors.append("- Age must be between 13 and 120\n");
        }
        
        // Validate email
        int atCount = 0;
        int atPosition = -1;
        for (int i = 0; i < email.length(); i++) {
            if (email.charAt(i) == '@') {
                atCount++;
                atPosition = i;
            }
        }
        boolean hasDotAfterAt = false;
        if (atPosition != -1 && atPosition < email.length() - 2) {
            for (int i = atPosition + 1; i < email.length(); i++) {
                if (email.charAt(i) == '.') {
                    hasDotAfterAt = true;
                    break;
                }
            }
        }
        if (atCount != 1 || !hasDotAfterAt) {
            valid = false;
            errors.append("- Email must contain exactly one @ and at least one . after @\n");
        }
        
        // Validate password
        boolean hasDigit = false;
        boolean hasLetter = false;
        if (password.length() >= 8) {
            for (int i = 0; i < password.length(); i++) {
                char c = password.charAt(i);
                if (c >= '0' && c <= '9') {
                    hasDigit = true;
                }
                if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
                    hasLetter = true;
                }
            }
        }
        if (password.length() < 8 || !hasDigit || !hasLetter) {
            valid = false;
            errors.append("- Password must be at least 8 characters and contain letters and digits\n");
        }
        
        // Display result
        if (valid) {
            System.out.println("Registration successful!");
        } else {
            System.out.println("Errors:");
            System.out.print(errors.toString());
        }
        
        scanner.close();
    }
}
```

**評分標準：**
- Scanner 正確使用（包含 nextLine() 問題處理）：2 分
- Username 驗證邏輯：2 分
- Age 驗證邏輯：2 分
- Email 驗證邏輯（@ 和 . 檢查）：4 分
- Password 驗證邏輯（長度、數字、字母）：4 分
- 錯誤訊息收集和顯示：2 分
- 整體邏輯流程：2 分
- 總分：18 分

---

### FRQ 4: Triangle Type Classifier (較高難度)
**難度：★★★★★**

Write a complete Java program that:

1. Uses Scanner to read three side lengths (as doubles) of a potential triangle
2. Determines if the three sides can form a valid triangle (triangle inequality theorem)
3. If valid, classifies the triangle as:
   - **Equilateral**: all three sides equal
   - **Isosceles**: exactly two sides equal
   - **Scalene**: no sides equal
4. Additionally classifies by angles (using Pythagorean theorem):
   - **Right triangle**: a² + b² = c² (for the longest side c)
   - **Acute triangle**: a² + b² > c²
   - **Obtuse triangle**: a² + b² < c²
5. Handles invalid inputs (negative numbers, zero, non-numeric input)
6. Uses appropriate comparison operators accounting for floating-point precision (use tolerance of 0.0001)

**Example Output:**
```
Enter side 1: 3.0
Enter side 2: 4.0
Enter side 3: 5.0
Valid triangle: Yes
Type by sides: Scalene
Type by angles: Right

Enter side 1: 5.0
Enter side 2: 5.0
Enter side 3: 5.0
Valid triangle: Yes
Type by sides: Equilateral
Type by angles: Acute

Enter side 1: 1.0
Enter side 2: 2.0
Enter side 3: 10.0
Valid triangle: No
These sides cannot form a triangle.
```

**示範解答：**
```java
import java.util.Scanner;

public class TriangleClassifier {
    private static final double EPSILON = 0.0001;
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            System.out.print("Enter side 1: ");
            double side1 = scanner.nextDouble();
            System.out.print("Enter side 2: ");
            double side2 = scanner.nextDouble();
            System.out.print("Enter side 3: ");
            double side3 = scanner.nextDouble();
            
            // Validate input
            if (side1 <= 0 || side2 <= 0 || side3 <= 0) {
                System.out.println("Error: All sides must be positive numbers.");
                return;
            }
            
            // Check triangle inequality
            boolean isValid = (side1 + side2 > side3) && 
                            (side1 + side3 > side2) && 
                            (side2 + side3 > side1);
            
            if (!isValid) {
                System.out.println("Valid triangle: No");
                System.out.println("These sides cannot form a triangle.");
                return;
            }
            
            System.out.println("Valid triangle: Yes");
            
            // Classify by sides
            String sideType;
            if (areEqual(side1, side2) && areEqual(side2, side3)) {
                sideType = "Equilateral";
            } else if (areEqual(side1, side2) || areEqual(side2, side3) || areEqual(side1, side3)) {
                sideType = "Isosceles";
            } else {
                sideType = "Scalene";
            }
            System.out.println("Type by sides: " + sideType);
            
            // Classify by angles using Pythagorean theorem
            // First, find the longest side
            double a = side1;
            double b = side2;
            double c = side3;
            
            // Sort to get c as longest side
            if (a > c) {
                double temp = a;
                a = c;
                c = temp;
            }
            if (b > c) {
                double temp = b;
                b = c;
                c = temp;
            }
            
            double sumOfSquares = a * a + b * b;
            double longestSquared = c * c;
            
            String angleType;
            if (areEqual(sumOfSquares, longestSquared)) {
                angleType = "Right";
            } else if (sumOfSquares > longestSquared) {
                angleType = "Acute";
            } else {
                angleType = "Obtuse";
            }
            System.out.println("Type by angles: " + angleType);
            
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please enter numeric values.");
        } finally {
            scanner.close();
        }
    }
    
    private static boolean areEqual(double a, double b) {
        return Math.abs(a - b) < EPSILON;
    }
}
```

**評分標準：**
- Scanner 正確使用和異常處理：2 分
- 輸入驗證（正數檢查）：2 分
- 三角形不等式定理正確實現：3 分
- 邊分類邏輯（等邊、等腰、不等邊）：3 分
- 找到最長邊的邏輯：2 分
- 畢氏定理計算：2 分
- 角度分類邏輯（直角、銳角、鈍角）：3 分
- 浮點數比較（使用容差）：2 分
- Helper 方法和代碼組織：2 分
- 總分：21 分

---

## 附錄：重要概念複習

### Data Types 重點
- **Primitive types**: byte, short, int, long, float, double, boolean, char
- **Type casting**: implicit (widening) vs explicit (narrowing)
- **Integer division** vs floating-point division
- **Overflow** considerations

### Operators 重點
- **Arithmetic**: +, -, *, /, %
- **Assignment**: =, +=, -=, *=, /=, %=
- **Relational**: ==, !=, >, <, >=, <=
- **Logical**: &&, ||, !
- **Increment/Decrement**: ++, -- (prefix vs postfix)
- **Operator precedence**: PEMDAS + logical operators

### Scanner 重點
- **Methods**: next(), nextLine(), nextInt(), nextDouble(), nextBoolean()
- **Delimiter issues**: nextInt() followed by nextLine()
- **Exception handling**: InputMismatchException
- **Resource management**: close() method

### If Statement 重點
- **Single if**: condition checking
- **If-else**: two-way branching
- **If-else-if**: multi-way branching
- **Nested if**: complex decision structures
- **Short-circuit evaluation**: && and || optimization
- **Common pitfalls**: = vs ==, semicolon after if condition

---

## 考試策略建議

1. **時間管理**
   - 選擇題：平均每題 1.5 分鐘
   - FRQ：每題 15-20 分鐘
   
2. **選擇題技巧**
   - 先做確定的題目
   - 手動追蹤變數值
   - 注意運算子優先順序
   - 小心型別轉換陷阱

3. **FRQ 技巧**
   - 先寫主要邏輯框架
   - 注意邊界條件
   - 適當的錯誤處理
   - 代碼要有可讀性
   - 測試極端案例

4. **常見錯誤**
   - 整數除法截斷
   - Scanner 的 nextLine() 問題
   - 浮點數比較
   - if-else 結構混淆
   - 運算子優先級錯誤

祝你考試順利！🎯
