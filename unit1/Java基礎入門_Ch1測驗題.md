# Java 基礎入門 Ch1 - AP CSA 測驗題

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



---

### Question 2
Which of the following variable declarations will cause a compile-time error?

(A) `int age = 18;`  
(B) `double price = 19.99;`  
(C) `String name = "John";`  
(D) `int 2students = 30;`  

 
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

 
**Explanation:** Integer division results in 2, which is then converted to 2.0 when assigned to double.

---

### Question 4
Which of the following statements about Java is FALSE?

(A) Java is case-sensitive  
(B) Java programs must have a main method to execute  
(C) Java variables must be declared before use  
(D) Java automatically converts int to String when needed  

  
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

 
**Explanation:** `false || true` evaluates to `true`.

---

### Question 6
Which of the following correctly declares and initializes a String variable?

(A) `String name = John;`  
(B) `String name = 'John';`  
(C) `String name = "John";`  
(D) `string name = "John";`  

 
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

  
**Explanation:** x becomes 15 after `x += 5`, then 30 after `x *= 2`.

---

### Question 8
Which of the following is a valid comment in Java?

(A) `# This is a comment`  
(B) `// This is a comment`  
(C) `<!-- This is a comment -->`  
(D) `' This is a comment`  



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

  
**Explanation:** 7 % 3 = 1 (remainder of 7 divided by 3).

---

### Question 10
Which of the following best describes the purpose of the `System.out.println()` method?

(A) To read input from the user  
(B) To print output to the console with a new line  
(C) To declare a new variable  
(D) To perform mathematical calculations  



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



---

### Question 12
Which of the following data types can store the value 3.14159?

(A) int  
(B) boolean  
(C) char  
(D) double  



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

 
**Explanation:** x++ uses 5 (then becomes 6), ++y becomes 11 first, so 5 + 11 = 16.

---

### Question 14
Which of the following Scanner methods should be used to read an entire line of text including spaces?

(A) `scanner.next()`  
(B) `scanner.nextLine()`  
(C) `scanner.nextInt()`  
(D) `scanner.nextDouble()`  



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

 
**Explanation:** `10 > 20` is false, so the entire expression is false.

---

### Question 16
Which of the following is the correct way to declare a constant in Java?

(A) `const int MAX = 100;`  
(B) `final int MAX = 100;`  
(C) `constant int MAX = 100;`  
(D) `readonly int MAX = 100;`  



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


**Explanation:** Casting double to int truncates the decimal part.

---

### Question 18
Which of the following expressions evaluates to true?

(A) `5 == 5.0`  
(B) `"5" == 5`  
(C) `'5' == 5`  
(D) `true == 1`  

 
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



---

### Question 20
Which of the following will NOT compile?

(A) `int x = 5; double y = x;`  
(B) `double x = 5.5; int y = (int) x;`  
(C) `int x = 5; String y = x;`  
(D) `String x = "5"; String y = x;`  

 
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
 
**Explanation:** 15/4 = 3, 15%4 = 3, so 3 + 3 = 6. Wait, let me recalculate: 15/4 = 3 (integer division), 15%4 = 3, so 3 + 3 = 6. The answer should be 6, not 7. Let me correct this.

 
**Explanation:** 15/4 = 3 (integer division), 15%4 = 3, so 3 + 3 = 6.

---

### Question 22
Which of the following is the correct syntax for importing the Scanner class?

(A) `include java.util.Scanner;`  
(B) `import java.util.Scanner;`  
(C) `using java.util.Scanner;`  
(D) `require java.util.Scanner;`  



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

  
**Explanation:** !true = false, false || false = false.

---

### Question 24
Which primitive data type has the largest range of values?

(A) int  
(B) long  
(C) float  
(D) double  

 
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

 
**Explanation:** Ternary operator: condition is true, so "Yes" is printed.



## 💡 Study Tips

1. **Practice Code Tracing**: Follow code execution step by step
2. **Memorize Data Types**: Know the range and use cases for each type
3. **Understand Operators**: Learn operator precedence and associativity
4. **Master Scanner**: Know when to use each input method
5. **Debug Common Errors**: Practice identifying and fixing compilation errors



# Part B: Free Response Questions (36 points)

**Time Allocation**: Approximately 60 minutes for all Free Response questions.

## Question 1: Rectangle Calculator (9 points)

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

## Question 2: GPA Calculator (9 points)

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

## Question 3: Shopping Cart Total (9 points)

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


