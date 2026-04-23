# 📝 AP Computer Science A Practice Test - Unit 1: Primitive Types

## 🎯 Test Information
- **Duration**: 75 minutes
- **Total Points**: 100 points
- **Difficulty Level**: Medium (AP Standard)
- **Format**: Multiple Choice Questions (MCQ) + Free Response Questions (FRQ)
- **Coverage**: Variables, data types, operators, expressions, type casting, Scanner input, compound operators

---

## 📚 Section I: Multiple Choice Questions (60 points)
**Instructions**: Choose the best answer for each question. Mark your answer clearly.

### **Question 1** (3 points)
Which of the following variable declarations will cause a compilation error?

A) `int score = 95;`
B) `double price = 19.99;`
C) `boolean isValid = true;`
D) `char grade = "A";`
E) `final int MAX_SIZE = 100;`

### **Question 2** (3 points)
What is the output of the following code segment?
```java
int x = 15;
int y = 4;
System.out.println(x / y + " " + x % y);
```

A) `3.75 3`
B) `3 3`
C) `4 3`
D) `3.75 15`
E) `3 15`

### **Question 3** (3 points)
Consider the following code segment:
```java
double result = 7 / 2 * 3.0;
```
What value is stored in `result`?

A) `10.5`
B) `9.0`
C) `1.17` (approximately)
D) `10.0`
E) `1.0`

### **Question 4** (3 points)
Which of the following expressions evaluates to `true`?

A) `5 + 3 * 2 == 11`
B) `10 / 3 == 3.33`
C) `15 % 4 == 3`
D) `2.0 == 2`
E) Both C and D

### **Question 5** (3 points)
What happens when the following code is executed?
```java
int value = (int) 7.9;
System.out.println(value);
```

A) Prints `8`
B) Prints `7`
C) Prints `7.9`
D) Compilation error
E) Runtime error

### **Question 6** (3 points)
Consider the following code segment:
```java
int a = 10;
int b = ++a * 2;
```
After execution, what are the values of `a` and `b`?

A) `a = 10, b = 20`
B) `a = 11, b = 20`
C) `a = 11, b = 22`
D) `a = 10, b = 22`
E) `a = 12, b = 22`

### **Question 7** (3 points)
Which of the following is the correct way to declare a constant in Java?

A) `constant double PI = 3.14159;`
B) `final double PI = 3.14159;`
C) `const double PI = 3.14159;`
D) `static double PI = 3.14159;`
E) `readonly double PI = 3.14159;`

### **Question 8** (3 points)
What is the result of the following expression?
```java
int result = 20 - 3 * 4 + 8 / 2;
```

A) `70`
B) `12`
C) `16`
D) `8`
E) `32`

### **Question 9** (3 points)
Consider the following code:
```java
Scanner input = new Scanner(System.in);
int num = input.nextInt();
```
If the user enters `3.14`, what happens?

A) `num` stores `3`
B) `num` stores `3.14`
C) A runtime exception occurs
D) A compilation error occurs
E) `num` stores `4`

### **Question 10** (3 points)
Which of the following about primitive data types is TRUE?

A) `char` can store multiple characters
B) `boolean` can have three possible values: `true`, `false`, and `null`
C) `double` has higher precision than `float`
D) `int` and `Integer` are the same data type
E) Variables of type `String` are primitive types

### **Question 11** (3 points)
What is the output of this code segment?
```java
int x = 5;
int y = x++ + ++x;
System.out.println(x + " " + y);
```

A) `6 11`
B) `7 12`
C) `6 12`
D) `7 11`
E) `5 12`

### **Question 12** (3 points)
Which expression correctly calculates the area of a circle with radius `r`?

A) `Math.PI * r * r`
B) `3.14 * r^2`
C) `Math.pi * r * r`
D) `PI * r * r`
E) `Math.PI * r * 2`

### **Question 13** (3 points)
Consider the following code:
```java
double x = 5.7;
double y = 3.2;
int sum = (int)(x + y);
```
What is the value of `sum`?

A) `8`
B) `9`
C) `8.9`
D) Compilation error
E) `8.0`

### **Question 14** (3 points)
Which of the following is a valid Java identifier?

A) `2ndPlace`
B) `second-place`
C) `second_place`
D) `class`
E) `second place`

### **Question 15** (3 points)
What is the result of the following code?
```java
int a = 8;
a += 3;
a *= 2;
System.out.println(a);
```

A) `19`
B) `22`
C) `14`
D) `16`
E) `11`

### **Question 16** (3 points)
Consider this code segment:
```java
char letter = 'B';
int code = letter;
System.out.println(code);
```
What is the output?

A) `B`
B) `66`
C) `2`
D) Compilation error
E) `'B'`

### **Question 17** (3 points)
Which of the following expressions will NOT compile?

A) `int x = 5 + 3 * 2;`
B) `double y = 10 / 4;`
C) `boolean z = 5 > 3 && 2 < 4;`
D) `String s = 5 + 3;`
E) `char c = 'A' + 1;`

### **Question 18** (3 points)
What is the value of `result` after this code executes?
```java
int result = 0;
result += 5;
result -= 2;
result *= 3;
```

A) `6`
B) `9`
C) `15`
D) `11`
E) `3`

### **Question 19** (3 points)
Which statement about operator precedence is correct?

A) Addition has higher precedence than multiplication
B) Assignment has higher precedence than arithmetic operations
C) Multiplication and division have the same precedence
D) Parentheses have lower precedence than multiplication
E) Modulus has lower precedence than addition

### **Question 20** (3 points)
Consider the following code:
```java
final int BASE = 10;
int value = 5;
BASE = value + 3; // Line of code in question
```
What happens at the marked line?

A) `BASE` becomes `8`
B) `BASE` remains `10`
C) Compilation error
D) Runtime error
E) `value` becomes `13`

---

## 📝 Section II: Free Response Questions (40 points)

### **Question 1: Temperature Converter** (20 points)

Write a complete Java program that converts temperatures between Celsius and Fahrenheit. Your program should:

1. **Prompt the user** to enter a temperature in Celsius (as a double)
2. **Calculate** the equivalent temperature in Fahrenheit using the formula: F = (9.0/5.0) * C + 32
3. **Display** both temperatures with appropriate labels
4. **Calculate and display** the difference between the freezing point of water (32°F) and the entered Fahrenheit temperature
5. **Use proper variable names** and include comments explaining your calculations

**Sample Run:**
```
Enter temperature in Celsius: 25.0
25.0°C = 77.0°F
Difference from freezing point: 45.0°F
```

**Grading Criteria:**
- Correct input handling (4 points)
- Accurate temperature conversion formula (6 points)
- Proper calculation of difference from freezing point (4 points)
- Appropriate output formatting (3 points)
- Code style and comments (3 points)

### **Question 2: Payroll Calculator** (20 points)

Write a Java program segment that calculates an employee's pay information. Given the following variables:
- `hoursWorked` (double) - number of hours worked this week
- `hourlyRate` (double) - employee's hourly pay rate
- `overtimeRate` (double) - overtime pay rate (1.5 times regular rate)

Your program should:

1. **Calculate regular pay** (for first 40 hours at regular rate)
2. **Calculate overtime pay** (hours over 40 at overtime rate)
3. **Calculate total gross pay**
4. **Determine if the employee worked overtime** (boolean variable)
5. **Display all calculated values** with appropriate formatting

**Assumptions:**
- Overtime applies to any hours worked over 40
- Use appropriate data types for all calculations
- Regular hours are capped at 40 maximum

**Sample Calculation:**
- Hours worked: 45.5
- Hourly rate: $15.00
- Regular pay: 40.0 × $15.00 = $600.00
- Overtime pay: 5.5 × $22.50 = $123.75
- Total gross pay: $723.75
- Worked overtime: true

**Grading Criteria:**
- Correct variable declarations and types (4 points)
- Accurate regular pay calculation (4 points)
- Accurate overtime pay calculation (6 points)
- Proper boolean overtime determination (3 points)
- Clear output formatting (3 points)

---

## 🔍 Additional Practice Problems

### **Bonus Challenge** (+5 points)
Write a single line of code that swaps the values of two integer variables `a` and `b` without using a temporary variable. Explain how your solution works.


**Good luck with your AP Computer Science A preparation!** 🚀

*This practice test aligns with College Board AP CSA Course and Exam Description standards for Unit 1: Primitive Types.*