# 📚 AP Computer Science A - Unit 1 Practice Test
## Primitive Types, Variables, and Operators

**Test Instructions:**
- Total Points: 100
- Time Limit: 80 minutes
- Section I - Multiple Choice: 60 points (20 questions, 3 points each)
- Section II - Free Response: 40 points (2 questions)
- Calculator: Not permitted
- Reference materials: Java Quick Reference Guide provided

---

## 📝 Section I: Multiple Choice Questions (60 points)
*Select the best answer for each question.*

### **Question 1** (3 points)
What is the output of the following code segment?
```java
int x = 17;
int y = 5;
int z = x / y + x % y * 2;
System.out.println(z);
```

A) `7`  
B) `8`  
C) `9`  
D) `10`  
E) `11`

---

### **Question 2** (3 points)
Consider the following code segment:
```java
double a = 7.8;
double b = 3.2;
int result = (int) a + (int) b - (int) (a + b);
```
What is the value of `result`?

A) `0`  
B) `-1`  
C) `1`  
D) `10`  
E) `11`

---

### **Question 3** (3 points)
Consider the following code segment:
```java
int x = 5;
int y = x++ * 2 + ++x;
```
What is the value of `y`?

A) `15`  
B) `16`  
C) `17`  
D) `18`  
E) `19`

---

### **Question 4** (3 points)
What is the output of the following code?
```java
int a = 15;
int b = 4;
double c = a / b * 1.0;
double d = 1.0 * a / b;
System.out.println(c + " " + d);
```

A) `3.75 3.75`  
B) `3.0 3.75`  
C) `3.0 3.0`  
D) `4.0 3.75`  
E) `3.75 3.0`

---

### **Question 5** (3 points)
Consider the following code segment:
```java
int m = 10;
int n = --m + m++ + ++m;
```
What is the value of `n`?

A) `27`  
B) `28`  
C) `29`  
D) `30`  
E) `31`

---

### **Question 6** (3 points)
What is the value of the following expression?
```java
int result = 100 / 10 % 3 * 2 + 5;
```

A) `5`  
B) `7`  
C) `9`  
D) `10`  
E) `11`

---

### **Question 7** (3 points)
What is the output of the following code?
```java
int a = 25;
int b = 3;
double result = (double) (a / b) + a % b / 2.0;
System.out.println(result);
```

A) `8.333333333333334`  
B) `8.0`  
C) `9.0`  
D) `9.5`  
E) `8.5`

---

### **Question 8** (3 points)
Consider the following code segment:
```java
int x = 7;
int y = 3;
int z = x / ++y + y * x--;
```
What is the value of `z`?

A) `21`  
B) `27`  
C) `28`  
D) `29`  
E) `30`

---

### **Question 9** (3 points)
What is the output of the following code?
```java
int num = 12345;
int sum = num % 10 + num / 10 % 10 + num / 100 % 10;
System.out.println(sum);
```

A) `9`  
B) `10`  
C) `12`  
D) `15`  
E) `18`

---

### **Question 10** (3 points)
Consider the following code segment:
```java
double x = 9.7;
double y = 5.3;
int result = (int) (x + y) - (int) x - (int) y;
```
What is the value of `result`?

A) `-1`  
B) `0`  
C) `1`  
D) `14`  
E) `15`

---

### **Question 11** (3 points)
What is the output of the following code?
```java
int x = 5;
int y = 10;
int z = ++x * y-- - --y + x++;
System.out.println(x + " " + y + " " + z);
```

A) `7 8 52`  
B) `7 8 54`  
C) `6 9 52`  
D) `7 9 52`  
E) `6 8 54`

---

### **Question 12** (3 points)
Consider the following code segment:
```java
int a = 8;
int b = 3;
double result = a++ / b + a / ++b;
```
What is the value of `result`?

A) `2.0`  
B) `3.0`  
C) `4.0`  
D) `4.25`  
E) `4.666666666666667`

---

### **Question 13** (3 points)
What is the output of the following code?
```java
int x = 256;
byte b = (byte) x;
System.out.println(b);
```

A) `256`  
B) `0`  
C) `-128`  
D) `127`  
E) Compilation error

---

### **Question 14** (3 points)
Consider the following code segment:
```java
int num = 4567;
int digit = num / 100 % 10;
System.out.println(digit);
```
What is printed?

A) `4`  
B) `5`  
C) `6`  
D) `7`  
E) `45`

---

### **Question 15** (3 points)
What is the value of the following expression?
```java
int result = (int) (15.9 + 14.1) - ((int) 15.9 + (int) 14.1);
```

A) `0`  
B) `1`  
C) `29`  
D) `30`  
E) `2`

---

### **Question 16** (3 points)
Consider the following code segment:
```java
int x = 123;
int reversed = x % 10 * 100 + x / 10 % 10 * 10 + x / 100;
```
What is the value of `reversed`?

A) `123`  
B) `321`  
C) `312`  
D) `213`  
E) `132`

---

### **Question 17** (3 points)
What is the output of the following code?
```java
int a = 20;
int b = 15;
boolean result = (a > b) && (a / b > 0) || (b % a == 0);
System.out.println(result);
```

A) `true`  
B) `false`  
C) Compilation error  
D) Runtime error (division by zero)  
E) Cannot be determined

---

### **Question 18** (3 points)
Consider the following code segment:
```java
int x = 0xF;  // hexadecimal
int y = 017;  // octal
int z = 0b1010;  // binary
int sum = x + y + z;
```
What is the value of `sum`?

A) `24`  
B) `35`  
C) `40`  
D) `1027`  
E) Compilation error

---

### **Question 19** (3 points)
What is the output of the following code?
```java
int x = 7;
int y = 3;
double result = (x + y) / 2 + (x + y) / 2.0;
System.out.println(result);
```

A) `5.0`  
B) `10.0`  
C) `7.5`  
D) `10.5`  
E) `15.0`

---

### **Question 20** (3 points)
Consider the following code segment:
```java
int a = 12;
int b = 7;
int c = 5;
boolean result = (a > b + c) || (a < b) && (c < b);
```
What is the value of `result`?

A) `true`  
B) `false`  
C) Compilation error  
D) Cannot be determined  
E) Runtime error

---

## 💻 Section II: Free Response Questions (40 points)

### **Question 1: Enhanced Calculator with Mixed Operations (20 points)**

Write a complete Java program that performs complex calculations involving both integer and floating-point arithmetic. Your program should:

**Requirements:**
1. Prompt the user to enter three integer values (a, b, c)
2. Calculate and display the following results with proper formatting:
   - Integer division: a / b and the remainder a % b
   - Floating-point division: a / (double) b
   - Mixed expression: (a + b) / c vs. (a + b) / (double) c
   - Complex calculation: (a * b + c) / (a - b) as both int and double
   - Percentage: what percentage is a of (b + c)?
3. Handle type casting properly for all calculations
4. Format decimal numbers to 2 decimal places
5. Include appropriate labels and comments

**Sample Run:**
```
Enter first integer (a): 23
Enter second integer (b): 7
Enter third integer (c): 5

=== Calculation Results ===
Integer Division: 23 / 7 = 3 remainder 2
Floating-Point Division: 23 / 7 = 3.29
Mixed Expression: (23 + 7) / 5 = 6 (integer) vs 6.00 (double)
Complex Calculation: (23 * 7 + 5) / (23 - 7) = 10 (integer) vs 10.25 (double)
Percentage: 23 is 76.67% of (7 + 5)
```

**Grading Criteria:**
- Correct import statements and class structure (2 points)
- Proper Scanner usage and variable declarations (3 points)
- Correct integer and modulus operations (3 points)
- Proper type casting for floating-point operations (4 points)
- Correct complex expression calculations (4 points)
- Formatted output with 2 decimal places (2 points)
- Code organization and comments (2 points)

---

### **Question 2: Number Manipulation and Analysis (20 points)**

Write a Java program that performs digit manipulation and mathematical analysis on a 4-digit integer. Your program should:

**Requirements:**
1. Prompt the user to enter a 4-digit positive integer (1000-9999)
2. Extract and display each individual digit (thousands, hundreds, tens, ones)
3. Calculate and display:
   - Sum of all digits
   - Product of all digits
   - The number with digits reversed
   - The number formed by only even digits (left to right)
   - The number formed by only odd digits (left to right)
   - Average of all digits (as a double, 2 decimal places)
4. Use only arithmetic operations (/, %, +, -, *) - no String methods
5. Properly format all output

**Sample Run:**
```
Enter a 4-digit integer: 4267

=== Digit Analysis for 4267 ===
Digit Breakdown:
  Thousands: 4
  Hundreds: 2
  Tens: 6
  Ones: 7

Calculations:
  Sum of digits: 4 + 2 + 6 + 7 = 19
  Product of digits: 4 × 2 × 6 × 7 = 336
  Reversed number: 7624
  Even digits only: 426
  Odd digits only: 47
  Average of digits: 4.75
```

**Grading Criteria:**
- Correct import statements and class structure (2 points)
- Proper Scanner usage and input handling (2 points)
- Correct digit extraction using / and % (4 points)
- Correct sum and product calculations (2 points)
- Correct reversal algorithm (3 points)
- Correct even/odd digit filtering (4 points)
- Proper formatting and output display (2 points)
- Code clarity and comments (1 point)

---

## 📋 Answer Sheet

### Section I: Multiple Choice
Mark your answers clearly:

1. _____ 6. _____ 11. _____ 16. _____
2. _____ 7. _____ 12. _____ 17. _____
3. _____ 8. _____ 13. _____ 18. _____
4. _____ 9. _____ 14. _____ 19. _____
5. _____ 10. _____ 15. _____ 20. _____

### Section II: Free Response
- Write your code on separate paper
- Include all necessary import statements
- Use proper indentation and comments
- Test your code with the given sample inputs

---

## 📖 Study Tips

**Key Topics to Review:**
1. Primitive data types (int, double, boolean, char)
2. Variable declaration and initialization
3. Type casting (explicit and implicit)
4. Arithmetic operators (+, -, *, /, %)
5. Compound assignment operators (+=, -=, *=, /=, %=)
6. Increment/decrement operators (++, --)
7. Order of operations (precedence)
8. Integer vs. floating-point division
9. Constants using `final` keyword
10. Scanner class for user input

**Common Mistakes to Avoid:**
- Forgetting type casting when needed
- Integer division when decimal result is expected
- Using = instead of == for comparison
- Incorrect operator precedence
- Not handling Scanner properly
- Using reserved words as identifiers

---

**Good luck on your test! Remember to show all your work and check your answers.**
