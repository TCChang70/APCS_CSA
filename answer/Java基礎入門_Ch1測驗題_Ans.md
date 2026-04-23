# Java 基礎入門 Ch1 - AP CSA 風格測驗題

## 📝 測驗說明
- 本測驗模擬美國 AP Computer Science A 考試風格
- 共 25 題選擇題，每題 4 分
- 測驗時間：45 分鐘
- 涵蓋內容：Java 基礎語法、變數、資料型別、運算子、輸入輸出

---

## Section 1: Multiple Choice Questions (選擇題)

### Question 1
Consider the following code segment:
```java
int x = 10;
int y = 3;
System.out.println(x / y);
```
What is printed as a result of executing this code segment?

(A) 3  
(B) 3.0  
(C) 3.333...  
(D) 3.3333333333333335  

**Answer: A**

---

### Question 2
Which of the following variable declarations will cause a compile-time error?

(A) `int age = 18;`  
(B) `double price = 19.99;`  
(C) `String name = "John";`  
(D) `int 2students = 30;`  

**Answer: D**  
**Explanation:** Variable names cannot start with a digit.

---

### Question 3
Consider the following code segment:
```java
int a = 5;
int b = 2;
double result = a / b;
System.out.println(result);
```
What is printed as a result of executing this code segment?

(A) 2  
(B) 2.0  
(C) 2.5  
(D) 2.50  

**Answer: B**  
**Explanation:** Integer division results in 2, which is then converted to 2.0 when assigned to double.

---

### Question 4
Which of the following statements about Java is FALSE?

(A) Java is case-sensitive  
(B) Java programs must have a main method to execute  
(C) Java variables must be declared before use  
(D) Java automatically converts int to String when needed  

**Answer: D**  
**Explanation:** Java does not automatically convert int to String; explicit conversion or concatenation is needed.

---

### Question 5
Consider the following code segment:
```java
boolean x = true;
boolean y = false;
System.out.println(x && y || x);
```
What is printed as a result of executing this code segment?

(A) true  
(B) false  
(C) 1  
(D) 0  

**Answer: A**  
**Explanation:** `false || true` evaluates to `true`.

---

### Question 6
Which of the following correctly declares and initializes a String variable?

(A) `String name = John;`  
(B) `String name = 'John';`  
(C) `String name = "John";`  
(D) `string name = "John";`  

**Answer: C**  
**Explanation:** Strings must be enclosed in double quotes, and String is capitalized.

---

### Question 7
Consider the following code segment:
```java
int x = 10;
x += 5;
x *= 2;
System.out.println(x);
```
What is printed as a result of executing this code segment?

(A) 20  
(B) 25  
(C) 30  
(D) 40  

**Answer: C**  
**Explanation:** x becomes 15 after `x += 5`, then 30 after `x *= 2`.

---

### Question 8
Which of the following is a valid comment in Java?

(A) `# This is a comment`  
(B) `// This is a comment`  
(C) `<!-- This is a comment -->`  
(D) `' This is a comment`  

**Answer: B**

---

### Question 9
Consider the following code segment:
```java
int a = 7;
int b = 3;
System.out.println(a % b);
```
What is printed as a result of executing this code segment?

(A) 0  
(B) 1  
(C) 2  
(D) 3  

**Answer: B**  
**Explanation:** 7 % 3 = 1 (remainder of 7 divided by 3).

---

### Question 10
Which of the following best describes the purpose of the `System.out.println()` method?

(A) To read input from the user  
(B) To print output to the console with a new line  
(C) To declare a new variable  
(D) To perform mathematical calculations  

**Answer: B**

---

### Question 11
Consider the following code segment:
```java
String str1 = "Hello";
String str2 = "World";
System.out.println(str1 + " " + str2);
```
What is printed as a result of executing this code segment?

(A) HelloWorld  
(B) Hello World  
(C) Hello + World  
(D) Compilation error  

**Answer: B**

---

### Question 12
Which of the following data types can store the value 3.14159?

(A) int  
(B) boolean  
(C) char  
(D) double  

**Answer: D**

---

### Question 13
Consider the following code segment:
```java
int x = 5;
int y = 10;
int z = x++ + ++y;
System.out.println(z);
```
What is printed as a result of executing this code segment?

(A) 15  
(B) 16  
(C) 17  
(D) 18  

**Answer: B**  
**Explanation:** x++ uses 5 (then becomes 6), ++y becomes 11 first, so 5 + 11 = 16.

---

### Question 14
Which of the following Scanner methods should be used to read an entire line of text including spaces?

(A) `scanner.next()`  
(B) `scanner.nextLine()`  
(C) `scanner.nextInt()`  
(D) `scanner.nextDouble()`  

**Answer: B**

---

### Question 15
Consider the following code segment:
```java
int a = 10;
int b = 20;
int c = 30;
System.out.println(a > b && b < c);
```
What is printed as a result of executing this code segment?

(A) true  
(B) false  
(C) 1  
(D) Compilation error  

**Answer: B**  
**Explanation:** `10 > 20` is false, so the entire expression is false.

---

### Question 16
Which of the following is the correct way to declare a constant in Java?

(A) `const int MAX = 100;`  
(B) `final int MAX = 100;`  
(C) `constant int MAX = 100;`  
(D) `readonly int MAX = 100;`  

**Answer: B**

---

### Question 17
Consider the following code segment:
```java
double x = 10.5;
int y = (int) x;
System.out.println(y);
```
What is printed as a result of executing this code segment?

(A) 10  
(B) 10.5  
(C) 11  
(D) Compilation error  

**Answer: A**  
**Explanation:** Casting double to int truncates the decimal part.

---

### Question 18
Which of the following expressions evaluates to true?

(A) `5 == 5.0`  
(B) `"5" == 5`  
(C) `'5' == 5`  
(D) `true == 1`  

**Answer: A**  
**Explanation:** Java automatically converts int to double for comparison.

---

### Question 19
Consider the following code segment:
```java
String s = "Java";
System.out.println(s.length());
```
What is printed as a result of executing this code segment?

(A) 3  
(B) 4  
(C) 5  
(D) Compilation error  

**Answer: B**

---

### Question 20
Which of the following will NOT compile?

(A) `int x = 5; double y = x;`  
(B) `double x = 5.5; int y = (int) x;`  
(C) `int x = 5; String y = x;`  
(D) `String x = "5"; String y = x;`  

**Answer: C**  
**Explanation:** Cannot directly assign int to String without conversion.

---

### Question 21
Consider the following code segment:
```java
int x = 15;
int y = 4;
System.out.println(x / y + x % y);
```
What is printed as a result of executing this code segment?

(A) 6  
(B) 6.75  
(C) 7  
(D) 8  

**Answer: C**  
**Explanation:** 15/4 = 3, 15%4 = 3, so 3 + 3 = 6. Wait, let me recalculate: 15/4 = 3 (integer division), 15%4 = 3, so 3 + 3 = 6. The answer should be 6, not 7. Let me correct this.

**Answer: A (6)**  
**Explanation:** 15/4 = 3 (integer division), 15%4 = 3, so 3 + 3 = 6.

---

### Question 22
Which of the following is the correct syntax for importing the Scanner class?

(A) `include java.util.Scanner;`  
(B) `import java.util.Scanner;`  
(C) `using java.util.Scanner;`  
(D) `require java.util.Scanner;`  

**Answer: B**

---

### Question 23
Consider the following code segment:
```java
boolean a = true;
boolean b = false;
System.out.println(!a || b);
```
What is printed as a result of executing this code segment?

(A) true  
(B) false  
(C) !true  
(D) Compilation error  

**Answer: B**  
**Explanation:** !true = false, false || false = false.

---

### Question 24
Which primitive data type has the largest range of values?

(A) int  
(B) long  
(C) float  
(D) double  

**Answer: D**  
**Explanation:** double has the largest range and precision.

---

### Question 25
Consider the following code segment:
```java
int x = 10;
System.out.println(x == 10 ? "Yes" : "No");
```
What is printed as a result of executing this code segment?

(A) Yes  
(B) No  
(C) true  
(D) Compilation error  

**Answer: A**  
**Explanation:** Ternary operator: condition is true, so "Yes" is printed.

---

## 📊 Answer Key

| Question | Answer | Question | Answer | Question | Answer |
|----------|--------|----------|--------|----------|--------|
| 1 | A | 10 | B | 19 | B |
| 2 | D | 11 | B | 20 | C |
| 3 | B | 12 | D | 21 | A |
| 4 | D | 13 | B | 22 | B |
| 5 | A | 14 | B | 23 | B |
| 6 | C | 15 | B | 24 | D |
| 7 | C | 16 | B | 25 | A |
| 8 | B | 17 | A | | |
| 9 | B | 18 | A | | |

---

## 🎯 Scoring Guide

| Score | Grade | Description |
|-------|-------|-------------|
| 92-100 | 5 | Extremely well qualified |
| 84-91 | 4 | Well qualified |
| 68-83 | 3 | Qualified |
| 52-67 | 2 | Possibly qualified |
| 0-51 | 1 | No recommendation |

---

## 📝 Common Mistakes to Avoid

1. **Integer Division**: Remember that `int / int` results in `int`, not `double`
2. **Variable Naming**: Cannot start with digits, cannot contain spaces or hyphens
3. **String vs char**: Use double quotes `"` for String, single quotes `'` for char
4. **Case Sensitivity**: `String` vs `string`, `System` vs `system`
5. **Operator Precedence**: `&&` has higher precedence than `||`
6. **Type Casting**: Explicit cast needed when converting from larger to smaller type
7. **Scanner Methods**: `next()` vs `nextLine()` - understand the difference
8. **Post/Pre Increment**: `x++` vs `++x` - timing of increment matters

---

## 💡 Study Tips

1. **Practice Code Tracing**: Follow code execution step by step
2. **Memorize Data Types**: Know the range and use cases for each type
3. **Understand Operators**: Learn operator precedence and associativity
4. **Master Scanner**: Know when to use each input method
5. **Debug Common Errors**: Practice identifying and fixing compilation errors

---

## 🔗 Related Topics for Further Study

- Chapter 2: Control Structures (if-else, loops)
- Chapter 3: Methods and Parameters
- Chapter 4: Arrays and ArrayLists
- Chapter 5: Classes and Objects

---

# Part B: Free Response Questions (36 points)

**Instructions**: Answer all 4 questions. Write your solution in Java. Each question is worth 9 points.

**Time Allocation**: Approximately 60 minutes for all Free Response questions.

---

## Question 1: Temperature Converter (9 points)

### Problem Statement

Write a complete Java program called `TemperatureConverter` that:
1. Prompts the user to enter a temperature in Fahrenheit
2. Converts the temperature to Celsius using the formula: C = (F - 32) × 5 / 9
3. Displays the result with exactly 2 decimal places
4. Uses appropriate variable types and proper formatting

### Example Output

```
Enter temperature in Fahrenheit: 98.6
98.6°F = 37.00°C
```

### Complete Solution

```java
import java.util.Scanner;

public class TemperatureConverter {
    public static void main(String[] args) {
        // Create Scanner object for input
        Scanner scanner = new Scanner(System.in);
        
        // Prompt user for Fahrenheit temperature
        System.out.print("Enter temperature in Fahrenheit: ");
        double fahrenheit = scanner.nextDouble();
        
        // Convert to Celsius using the formula
        double celsius = (fahrenheit - 32) * 5 / 9;
        
        // Display result with 2 decimal places
        System.out.printf("%.1f°F = %.2f°C%n", fahrenheit, celsius);
        
        // Close scanner
        scanner.close();
    }
}
```

### Scoring Rubric (9 points)

| Points | Criteria |
|--------|----------|
| 1 | Correct class declaration with proper naming |
| 1 | Correct main method signature |
| 1 | Scanner object creation and proper import |
| 1 | Prompts user for input with appropriate message |
| 2 | Correctly reads double value using `nextDouble()` |
| 2 | Correctly implements conversion formula with proper order of operations |
| 1 | Uses `printf` or `String.format()` to display result with 2 decimal places |
| 0.5 | Bonus: Closes Scanner resource |

**Common Mistakes to Avoid**:
- Using integer division (5 / 9 = 0 instead of 5.0 / 9)
- Incorrect order of operations in formula
- Not using `double` for decimal values
- Forgetting to import `java.util.Scanner`

---

## Question 2: Rectangle Calculator (9 points)

### Problem Statement

Write a complete Java program called `RectangleCalculator` that:
1. Prompts the user to enter the length of a rectangle
2. Prompts the user to enter the width of a rectangle
3. Calculates and displays:
   - The area (length × width)
   - The perimeter (2 × (length + width))
4. All measurements should be handled as `double` values
5. Results should be displayed with 2 decimal places

### Example Output

```
Enter the length of the rectangle: 5.5
Enter the width of the rectangle: 3.2
Area: 17.60
Perimeter: 17.40
```

### Complete Solution

```java
import java.util.Scanner;

public class RectangleCalculator {
    public static void main(String[] args) {
        // Create Scanner for user input
        Scanner scanner = new Scanner(System.in);
        
        // Get length from user
        System.out.print("Enter the length of the rectangle: ");
        double length = scanner.nextDouble();
        
        // Get width from user
        System.out.print("Enter the width of the rectangle: ");
        double width = scanner.nextDouble();
        
        // Calculate area and perimeter
        double area = length * width;
        double perimeter = 2 * (length + width);
        
        // Display results with 2 decimal places
        System.out.printf("Area: %.2f%n", area);
        System.out.printf("Perimeter: %.2f%n", perimeter);
        
        // Close scanner
        scanner.close();
    }
}
```

### Scoring Rubric (9 points)

| Points | Criteria |
|--------|----------|
| 1 | Correct class and main method structure |
| 1 | Scanner object creation with proper import |
| 1.5 | Correctly prompts for and reads length as `double` |
| 1.5 | Correctly prompts for and reads width as `double` |
| 2 | Correctly calculates area (length × width) |
| 2 | Correctly calculates perimeter (2 × (length + width)) |
| 1 | Displays both results with 2 decimal places using `printf` |
| 0.5 | Bonus: Proper variable naming and code organization |

**Common Mistakes to Avoid**:
- Using `int` instead of `double` for measurements
- Incorrect perimeter formula: 2 * length + width (missing parentheses)
- Not formatting output to 2 decimal places
- Declaring variables before Scanner is created

---

## Question 3: GPA Calculator (9 points)

### Problem Statement

Write a complete Java program called `GPACalculator` that:
1. Prompts the user to enter the number of courses (as an integer)
2. Prompts the user to enter the total grade points earned (as a double)
3. Calculates the GPA by dividing total grade points by number of courses
4. Displays the GPA with exactly 2 decimal places
5. Includes appropriate prompts and output messages

### Example Output

```
Enter number of courses: 5
Enter total grade points earned: 18.5
Your GPA is: 3.70
```

### Complete Solution

```java
import java.util.Scanner;

public class GPACalculator {
    public static void main(String[] args) {
        // Create Scanner for input
        Scanner scanner = new Scanner(System.in);
        
        // Get number of courses
        System.out.print("Enter number of courses: ");
        int numCourses = scanner.nextInt();
        
        // Get total grade points
        System.out.print("Enter total grade points earned: ");
        double totalGradePoints = scanner.nextDouble();
        
        // Calculate GPA
        double gpa = totalGradePoints / numCourses;
        
        // Display result with 2 decimal places
        System.out.printf("Your GPA is: %.2f%n", gpa);
        
        // Close scanner
        scanner.close();
    }
}
```

### Scoring Rubric (9 points)

| Points | Criteria |
|--------|----------|
| 1 | Correct program structure (class and main method) |
| 1 | Scanner creation with proper import statement |
| 2 | Correctly prompts for and reads number of courses as `int` |
| 2 | Correctly prompts for and reads total grade points as `double` |
| 2 | Correctly calculates GPA (total grade points / number of courses) |
| 1 | Displays GPA with 2 decimal places using formatted output |
| 0.5 | Bonus: Uses descriptive variable names and proper output message |

**Common Mistakes to Avoid**:
- Integer division issue (if both operands are int)
- Reading values in wrong order
- Not using appropriate data types (`int` for courses, `double` for grade points)
- Missing `%n` or `\n` for newline in output

---

## Question 4: Shopping Cart Total (9 points)

### Problem Statement

Write a complete Java program called `ShoppingCart` that:
1. Prompts the user to enter the price of item 1
2. Prompts the user to enter the price of item 2
3. Prompts the user to enter the price of item 3
4. Calculates the subtotal (sum of all three prices)
5. Calculates the tax amount (8% of subtotal)
6. Calculates the final total (subtotal + tax)
7. Displays all three values (subtotal, tax, total) with 2 decimal places

### Example Output

```
Enter price of item 1: 29.99
Enter price of item 2: 15.50
Enter price of item 3: 42.00
Subtotal: $87.49
Tax (8%): $7.00
Total: $94.49
```

### Complete Solution

```java
import java.util.Scanner;

public class ShoppingCart {
    public static void main(String[] args) {
        // Create Scanner for input
        Scanner scanner = new Scanner(System.in);
        
        // Define tax rate as a constant
        final double TAX_RATE = 0.08;
        
        // Get prices for three items
        System.out.print("Enter price of item 1: ");
        double item1 = scanner.nextDouble();
        
        System.out.print("Enter price of item 2: ");
        double item2 = scanner.nextDouble();
        
        System.out.print("Enter price of item 3: ");
        double item3 = scanner.nextDouble();
        
        // Calculate subtotal, tax, and total
        double subtotal = item1 + item2 + item3;
        double tax = subtotal * TAX_RATE;
        double total = subtotal + tax;
        
        // Display results with 2 decimal places
        System.out.printf("Subtotal: $%.2f%n", subtotal);
        System.out.printf("Tax (8%%): $%.2f%n", tax);
        System.out.printf("Total: $%.2f%n", total);
        
        // Close scanner
        scanner.close();
    }
}
```

### Scoring Rubric (9 points)

| Points | Criteria |
|--------|----------|
| 1 | Correct program structure with appropriate class name |
| 1 | Scanner object creation and import statement |
| 2 | Correctly reads all three item prices as `double` values |
| 2 | Correctly calculates subtotal (sum of three prices) |
| 1 | Correctly calculates tax (8% of subtotal) |
| 1 | Correctly calculates total (subtotal + tax) |
| 1 | Displays all three results with proper formatting (2 decimal places) |
| 0.5 | Bonus: Uses constant for tax rate and includes $ in output |

**Common Mistakes to Avoid**:
- Not using `double` for price values
- Incorrect tax calculation (multiplying by 8 instead of 0.08)
- Forgetting to add subtotal and tax for total
- Not displaying % symbol correctly in printf (`%%` is needed to display %)
- Poor variable naming (using x, y, z instead of descriptive names)

---

## Free Response Scoring Summary

| Question | Topic | Points |
|----------|-------|--------|
| Q1 | Temperature Converter | 9 |
| Q2 | Rectangle Calculator | 9 |
| Q3 | GPA Calculator | 9 |
| Q4 | Shopping Cart Total | 9 |
| **Total** | | **36** |

---

## Free Response Tips for Success

### Before Writing Code:
1. **Read the entire problem** carefully
2. **Identify required inputs** and their data types
3. **List the calculations** needed
4. **Plan the output format**

### While Writing Code:
1. **Start with the basic structure** (class and main method)
2. **Import necessary classes** (Scanner)
3. **Declare variables** with appropriate types
4. **Write clear prompts** for user input
5. **Implement calculations** step by step
6. **Format output** as specified

### Common AP CSA Free Response Guidelines:
- **Assume all input is valid** unless stated otherwise
- **Show all work** - partial credit is awarded
- **Use proper Java syntax** - semicolons, braces, parentheses
- **Follow naming conventions** - classes start with uppercase, variables with lowercase
- **Comment complex logic** (optional but helpful)
- **Test with example data** mentally

### Time Management:
- Spend approximately **15 minutes per question**
- Leave time to **review your code**
- If stuck, **move to next question** and return later
- **Write something** - blank answers get 0 points

---

Good luck with your studies! 🎓
