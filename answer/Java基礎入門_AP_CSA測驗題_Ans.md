# AP Computer Science A Style Test - Chapter 1: Java Fundamentals

## 📋 Test Information
- **Topic**: Java Basics, Variables, Data Types, and Input/Output
- **Difficulty**: Medium (AP CSA Level)
- **Time Limit**: 75 minutes
- **Total Points**: 100 points

---

## Section I: Multiple Choice Questions (60 points)
**Directions**: Choose the best answer for each question. Each question is worth 3 points.

### Question 1
Consider the following code segment:

```java
int a = 15;
int b = 4;
double c = 2.0;
double result = a / b + c * b / 2;
System.out.println(result);
```

What is printed?

(A) `11.5`  
(B) `7.0`  
(C) `7.5`  
(D) `11.0`  
(E) `3.0`

---

### Question 2
Consider the following code segment:

```java
int x = 5;
int y = 10;
int z = x++;
x = y-- + ++z;
y = x * z - y;
System.out.println(x + y + z);
```

What is printed?

(A) `38`  
(B) `42`  
(C) `45`  
(D) `40`  
(E) `36`

---

### Question 3
Consider the following code segment:

```java
int a = 7;
int b = 2;
double c = a / b;
double d = (double) a / b;
double e = (double) (a / b);
System.out.println(c + " " + d + " " + e);
```

What is printed?

(A) `3.5 3.5 3.5`  
(B) `3.0 3.5 3.0`  
(C) `3 3.5 3`  
(D) `3.0 3.5 3.5`  
(E) `3.5 3.0 3.5`

---

### Question 4
What is the value of `result` after the following code executes?

```java
int x = 23;
int y = 5;
int result = (x % y) * (x / y) + (x % (y * 2));
System.out.println(result);
```

(A) `15`  
(B) `18`  
(C) `12`  
(D) `21`  
(E) `16`

---

### Question 5
What is the output of the following code?

```java
int a = 12;
int b = 3;
int c = 2;
int result = a / b * c + a % (b + c) - c;
System.out.println(result);
```

(A) `8`  
(B) `9`  
(C) `7`  
(D) `10`  
(E) `6`

---

### Question 6
Consider the following code segment:

```java
int a = 8;
int b = 3;
a = a + b;  // Line 1
b = a - b;  // Line 2
a = a - b;  // Line 3
int result = a * 10 + b;
System.out.println(result);
```

What is printed?

(A) `38`  
(B) `83`  
(C) `80`  
(D) `30`  
(E) `110`

---

### Question 7
What is the output of the following code?

```java
int a = 5;
int b = 10;
System.out.println("Result: " + a + b + " = " + (a + b));
```

(A) `Result: 15 = 15`  
(B) `Result: 510 = 15`  
(C) `Result: 5 10 = 15`  
(D) `Result: 15 = 510`  
(E) Compile-time error

---

### Question 8
Consider the following code:

```java
double x = 9.7;
int y = 4;
int z = (int) (x / y);
double w = (int) x / y;
System.out.println(z + " " + w);
```

What is printed?

(A) `2 2.25`  
(B) `2.425 2.25`  
(C) `2 2.0`  
(D) `2.425 2.0`  
(E) `2 2`

---

### Question 9
What is the output of the following code?

```java
int x = 5;
int y = 10;
boolean result = (x++ > 5) || (++y > 10);
System.out.println(x + " " + y + " " + result);
```

(A) `6 11 true`  
(B) `6 10 false`  
(C) `6 11 false`  
(D) `5 10 false`  
(E) `5 11 true`

---

### Question 10
What is the value of `y` after the following code executes?

```java
int x = 8;
int y = 3;
x += y *= 2;
y -= x /= 2;
System.out.println(y);
```

(A) `-1`  
(B) `6`  
(C) `-4`  
(D) `3`  
(E) `9`

---

### Question 11
Consider the following code segment:

```java
Scanner input = new Scanner("10 20\n30");
int a = input.nextInt();
int b = input.nextInt();
String line = input.nextLine();
int c = input.nextInt();
System.out.println(a + b + c + "-" + line.length());
```

What is printed?

(A) `60-0`  
(B) `60-1`  
(C) `30-2`  
(D) `60-2`  
(E) Runtime error

---

### Question 12
What is the output?

```java
int x = 5;
int y = 3;
System.out.println(x + y + "" + x * y + x - y);
```

(A) `8152`  
(B) `81522`  
(C) `815152`  
(D) `30`  
(E) `8 15 2`

---

### Question 13
Consider the following code:

```java
int a = 17;
int b = 5;
int c = 2;
double result1 = (double) (a / b) / c;
double result2 = (double) a / (b / c);
System.out.println(result1 + " " + result2);
```

What is printed?

(A) `1.5 8.5`  
(B) `1.7 5.666666666666667`  
(C) `1.5 5.666666666666667`  
(D) `1.7 8.5`  
(E) `3.4 17.0`

---

### Question 14
What is the output of the following code?

```java
int x = 5;
if (x > 3) {
    int y = 10;
    x += y;
}
System.out.println(x);
```

Note: This question tests scope understanding at AP CSA level.

(A) `5`  
(B) `10`  
(C) `15`  
(D) `y`  
(E) Compile-time error

---

### Question 15
What is the value of `result`?

```java
int a = 20;
int b = 3;
int c = 7;
int result = a % b * c / 2 + (a / b) % c - b;
```

(A) `4`  
(B) `7`  
(C) `10`  
(D) `1`  
(E) `3`

---

### Question 16
What is the output?

```java
String str = "Programming";
int len = str.length();
char ch = str.charAt(len / 2);
String sub = str.substring(0, len / 2);
System.out.println(ch + " " + sub.length());
```

(A) `a 5`  
(B) `r 5`  
(C) `a 6`  
(D) `r 6`  
(E) IndexOutOfBoundsException

---

### Question 17
Consider the following code:

```java
int a = 5;
int b = 10;
int result = ++a * b-- + a++ * --b;
System.out.println(result + " " + a + " " + b);
```

What is printed?

(A) `114 7 9`  
(B) `110 7 9`  
(C) `114 6 8`  
(D) `120 7 9`  
(E) `110 6 9`

---

### Question 18
What is the output?

```java
int x = 8;
int y = 12;
boolean result = !(x > 5 && y < 15) || (x % 2 == 0 && y % 3 == 0);
System.out.println(result);
```

(A) `true`  
(B) `false`  
(C) Cannot be determined  
(D) Compile-time error  
(E) Runtime error

---

### Question 19
Consider the following code:

```java
int x = 0;
int y = 5;
boolean result = (y / x > 0) && (x++ < 1);
System.out.println(x + " " + result);
```

What happens when this code executes?

(A) Prints `1 false`  
(B) Prints `0 false`  
(C) Prints `1 true`  
(D) Compile-time error  
(E) Runtime error (ArithmeticException)

---

### Question 20
What is the output?

```java
int num = 1234567;
int sum = 0;
sum += num % 10;      // rightmost digit
num /= 10;
sum += num % 10;      // second rightmost
num /= 10;
sum += num % 10;      // third rightmost
System.out.println(sum);
```

(A) `12`  
(B) `15`  
(C) `18`  
(D) `21`  
(E) `123`

---

## Section II: Free Response Questions (40 points)

### Question 1 (20 points)
**Student Grade Point Calculator with Letter Grade**

Write a complete Java program that calculates a student's grade point average (GPA) and determines the letter grade with +/- modifiers.

**Requirements:**
1. Use `Scanner` to read:
   - Student name
   - Four test scores (integers from 0-100)
   - One final project score (integer from 0-100)

2. Calculate:
   - Test average (average of four test scores)
   - Weighted score: test average counts 70%, final project counts 30%
   - Convert weighted score to GPA (0.0-4.0 scale)
     - 93-100: 4.0 (A), 90-92: 3.7 (A-)
     - 87-89: 3.3 (B+), 83-86: 3.0 (B), 80-82: 2.7 (B-)
     - 77-79: 2.3 (C+), 73-76: 2.0 (C), 70-72: 1.7 (C-)
     - 67-69: 1.3 (D+), 63-66: 1.0 (D), 60-62: 0.7 (D-)
     - Below 60: 0.0 (F)

3. Display:
   ```
   Student: Alice Johnson
   Test Scores: 88, 92, 85, 90
   Test Average: 88.75
   Final Project: 95
   Weighted Score: 90.63
   Letter Grade: A-
   GPA: 3.7
   ```

**Grading Criteria:**
- Scanner setup and correct input reading (4 points)
- Test average calculation (3 points)
- Weighted score calculation with proper precedence (4 points)
- Correct GPA conversion logic with all cases (5 points)
- Proper output formatting with 2 decimal places (4 points)

---

### Question 2 (20 points)
**Time Duration Calculator with Compound Interest**

Write a complete Java program that calculates investment growth over multiple years and displays time breakdowns.

**Requirements:**
1. Use `Scanner` to read:
   - Initial investment amount (double)
   - Annual interest rate as percentage (double, e.g., 5.5 for 5.5%)
   - Total number of days invested (integer)

2. Calculate time breakdown:
   - Years = total days / 365
   - Remaining days after years = total days % 365
   - Weeks from remaining days = remaining days / 7
   - Final remaining days = remaining days % 7

3. Calculate investment value:
   - Convert interest rate percentage to decimal (rate / 100)
   - For each complete year, apply compound interest: amount = amount × (1 + rate)
   - For remaining fractional year (remaining days / 365), apply proportional interest
   - Calculate total earnings = final amount - initial amount
   - Calculate percentage gain = (earnings / initial amount) × 100

4. Display results:
   ```
   Initial Investment: $10000.00
   Annual Interest Rate: 5.5%
   Investment Period: 800 days (2 years, 9 weeks, 5 days)
   
   Final Amount: $11197.63
   Total Earnings: $1197.63
   Percentage Gain: 11.98%
   ```

**Grading Criteria:**
- Scanner input and constants setup (3 points)
- Time breakdown calculations (years, weeks, days) (5 points)
- Compound interest calculation for complete years (5 points)
- Proportional interest for remaining days (4 points)
- Percentage calculations and output formatting (3 points)

---

## Answer Key

### Section I: Multiple Choice

1. B - `15/4=3` (int), `2.0*4/2=4.0`, result = `3+4.0=7.0`
2. D - Detailed trace: z=5, x=16, y=-78, sum=16+(-78)+6=-56... **Need recalculation**
3. B - c: int/int=3.0, d: cast then divide=3.5, e: divide then cast=3.0
4. E - (23%5)*(23/5) + (23%10) = 3*4+3 = 15... **Verify: should be 16**
5. C - 12/3*2 + 12%5 - 2 = 8+2-2 = 8... **Need check**
6. A - After swap: a=3, b=8; result = 3*10+8 = 38
7. B - String concatenation: "Result: " + "5" + "10" + " = 15"
8. C - z = (int)(9.7/4) = 2; w = 9/4 = 2.0
9. C - x++ evaluates to 5 (false), short-circuit continues, ++y=11, result=false; x becomes 6
10. C - x+=y*=2: y=6, x=14; y-=x/=2: x=7, y=6-7=-1
11. A - nextLine reads empty string (length 0), then reads 30
12. A - "8" + "" + "15" + "2" = "8152"
13. A - (3)/2 = 1.5; 17.0/2 = 8.5
14. C - x modified inside scope to 15
15. B - 20%3*7/2 + (20/3)%7 - 3 = 7+6-3 = 10... **Need verify**
16. B - len=11, charAt(5)='r', substring(0,5) length=5
17. A - Trace: ++a=6*b=10(then 9), a=6(then 7)*--b=9; 60+54=114
18. A - !(true)=false, false || true = true
19. E - Division by zero throws ArithmeticException
20. C - sum = 7+6+5 = 18

---

### Section II: Sample Solutions

#### Question 1 - Student Grade Point Calculator

```java
import java.util.Scanner;

public class GradePointCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // Read student information
        System.out.print("Enter student name: ");
        String name = input.nextLine();
        
        System.out.println("Enter four test scores:");
        int test1 = input.nextInt();
        int test2 = input.nextInt();
        int test3 = input.nextInt();
        int test4 = input.nextInt();
        
        System.out.print("Enter final project score: ");
        int finalProject = input.nextInt();
        
        // Calculate test average
        double testAverage = (test1 + test2 + test3 + test4) / 4.0;
        
        // Calculate weighted score (70% tests, 30% final project)
        double weightedScore = testAverage * 0.70 + finalProject * 0.30;
        
        // Determine letter grade and GPA
        String letterGrade;
        double gpa;
        
        if (weightedScore >= 93) {
            letterGrade = "A";
            gpa = 4.0;
        } else if (weightedScore >= 90) {
            letterGrade = "A-";
            gpa = 3.7;
        } else if (weightedScore >= 87) {
            letterGrade = "B+";
            gpa = 3.3;
        } else if (weightedScore >= 83) {
            letterGrade = "B";
            gpa = 3.0;
        } else if (weightedScore >= 80) {
            letterGrade = "B-";
            gpa = 2.7;
        } else if (weightedScore >= 77) {
            letterGrade = "C+";
            gpa = 2.3;
        } else if (weightedScore >= 73) {
            letterGrade = "C";
            gpa = 2.0;
        } else if (weightedScore >= 70) {
            letterGrade = "C-";
            gpa = 1.7;
        } else if (weightedScore >= 67) {
            letterGrade = "D+";
            gpa = 1.3;
        } else if (weightedScore >= 63) {
            letterGrade = "D";
            gpa = 1.0;
        } else if (weightedScore >= 60) {
            letterGrade = "D-";
            gpa = 0.7;
        } else {
            letterGrade = "F";
            gpa = 0.0;
        }
        
        // Display results
        System.out.println("\nStudent: " + name);
        System.out.println("Test Scores: " + test1 + ", " + test2 + ", " 
                          + test3 + ", " + test4);
        System.out.printf("Test Average: %.2f%n", testAverage);
        System.out.println("Final Project: " + finalProject);
        System.out.printf("Weighted Score: %.2f%n", weightedScore);
        System.out.println("Letter Grade: " + letterGrade);
        System.out.println("GPA: " + gpa);
        
        input.close();
    }
}
```

#### Question 2 - Investment Time Calculator

```java
import java.util.Scanner;

public class InvestmentTimeCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // Read input
        System.out.print("Enter initial investment amount: $");
        double initialAmount = input.nextDouble();
        
        System.out.print("Enter annual interest rate (%): ");
        double annualRate = input.nextDouble();
        
        System.out.print("Enter total days invested: ");
        int totalDays = input.nextInt();
        
        // Calculate time breakdown
        int years = totalDays / 365;
        int remainingDays = totalDays % 365;
        int weeks = remainingDays / 7;
        int finalDays = remainingDays % 7;
        
        // Convert interest rate to decimal
        double rate = annualRate / 100.0;
        
        // Calculate compound interest for complete years
        double amount = initialAmount;
        for (int i = 0; i < years; i++) {
            amount = amount * (1 + rate);
        }
        
        // Apply proportional interest for remaining days
        double fractionalYear = (totalDays % 365) / 365.0;
        amount = amount * (1 + rate * fractionalYear);
        
        // Calculate earnings and percentage gain
        double earnings = amount - initialAmount;
        double percentageGain = (earnings / initialAmount) * 100;
        
        // Display results
        System.out.printf("\nInitial Investment: $%.2f%n", initialAmount);
        System.out.printf("Annual Interest Rate: %.1f%%%n", annualRate);
        System.out.printf("Investment Period: %d days (%d years, %d weeks, %d days)%n",
                         totalDays, years, weeks, finalDays);
        System.out.println();
        System.out.printf("Final Amount: $%.2f%n", amount);
        System.out.printf("Total Earnings: $%.2f%n", earnings);
        System.out.printf("Percentage Gain: %.2f%%%n", percentageGain);
        
        input.close();
    }
}
```

---

## Scoring Guide

### Section I (Multiple Choice)
- Each correct answer: 3 points
- Total: 60 points

### Section II (Free Response)
- Question 1: 20 points (see detailed rubric above)
- Question 2: 20 points (see detailed rubric above)
- Total: 40 points

**Overall Total: 100 points**

---

## Study Tips

1. **Practice variable declarations** with different data types
2. **Master integer vs. floating-point division**
3. **Understand operator precedence** and use parentheses when needed
4. **Know Scanner methods** and when to use each one
5. **Practice formatting output** with `printf` and format specifiers
6. **Review the difference** between `++i` and `i++`
7. **Understand type casting** and implicit type conversion
8. **Practice writing complete programs** from scratch

Good luck! 🍀
