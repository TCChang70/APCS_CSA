# AP Computer Science A - Expert Level Practice Test
## Unit 1: Primitive Types + Scanner Input + Conditional Logic

**Test Information:**
- **Total Questions:** 25 (20 Multiple Choice + 5 Free Response)
- **Time Allocation:** 50 minutes
- **Difficulty Level:** Expert/Advanced
- **Topics:** Type conversion, Scanner advanced usage, nested conditionals, boolean algebra, operator precedence
- **Calculator:** Not permitted

---

## Section I: Multiple Choice Questions (20 questions)

### **Question 1**
Consider the following code segment:

```java
int num = 128;
byte b = (byte) num;
System.out.println(b);
```

What will be printed?

A) `128`  
B) `127`  
C) `-128`  
D) `0`  
E) Compile-time error

---

### **Question 2**
What is the output of the following code?

```java
double x = 0.1 + 0.1 + 0.1;
double y = 0.3;
System.out.println(x == y);
```

A) `true`  
B) `false`  
C) `0.3`  
D) `0.30000000000000004`  
E) Compile-time error

---

### **Question 3**
Given the following input: `ABC 123 45.6 XYZ`

```java
Scanner scan = new Scanner(System.in);
String word = scan.next();
int num = scan.nextInt();
double dec = scan.nextDouble();
String last = scan.next();
System.out.println(word + num + dec + last);
```

What is printed?

A) `ABC12345.6XYZ`  
B) `ABC 123 45.6 XYZ`  
C) `ABC12345.6 XYZ`  
D) InputMismatchException  
E) `ABC` followed by InputMismatchException

---

### **Question 4**
What is the result of this expression?

```java
int result = 5 + 3 * 2 - 8 / 4 % 3;
System.out.println(result);
```

A) `7`  
B) `9`  
C) `11`  
D) `13`  
E) `9.0`

---

### **Question 5**
Consider the following code:

```java
int a = 15;
int b = 4;
double c = a / b;
double d = (double) a / b;
double e = a / (double) b;
System.out.println(c + " " + d + " " + e);
```

What is printed?

A) `3.75 3.75 3.75`  
B) `3.0 3.75 3.75`  
C) `3 3.75 3.75`  
D) `3.0 3.0 3.75`  
E) Compile-time error

---

### **Question 6**
What is the output?

```java
int x = 10;
boolean result = x > 5 && x < 15 && x % 2 == 0;
if (result) {
    x += 5;
} else {
    x -= 5;
}
x *= 2;
System.out.println(x);
```

A) `10`  
B) `20`  
C) `30`  
D) `40`  
E) `50`

---

### **Question 7**
Given input: `7 apple banana`

```java
Scanner input = new Scanner(System.in);
int n = input.nextInt();
String s1 = input.next();
String s2 = input.next();

if (n > 5 && s1.compareTo(s2) < 0) {
    System.out.print("X");
} else if (n <= 5 || s1.length() < s2.length()) {
    System.out.print("Y");
} else {
    System.out.print("Z");
}
```

What is printed?

A) `X`  
B) `Y`  
C) `Z`  
D) `XY`  
E) Nothing is printed

---

### **Question 8**
What is the value of `z` after execution?

```java
int x = 7;
int y = 3;
int z = 0;

if (x / y > 2)
    z = x % y;
else if (x % y == 1)
    z = x / y;
else
    z = x + y;
    
System.out.println(z);
```

A) `1`  
B) `2`  
C) `3`  
D) `10`  
E) `0`

---

### **Question 9**
What is printed?

```java
Scanner sc = new Scanner(System.in);
double temp = sc.nextDouble();

if (temp >= 100)
    System.out.print("Hot");
if (temp >= 70)
    System.out.print("Warm");
if (temp >= 32)
    System.out.print("Cold");
```

If the user enters: `85`

A) `Hot`  
B) `Warm`  
C) `Cold`  
D) `WarmCold`  
E) `HotWarmCold`

---

### **Question 10**
Consider this code:

```java
int x = 20;
int y = 30;
int z = 40;

boolean test = (x < y && y < z) || (x > z && y > z);
System.out.println(test);
```

What is printed?

A) `true`  
B) `false`  
C) `1`  
D) `0`  
E) Compile-time error

---

### **Question 11**
What is the output?

```java
int a = 25;
int b = 12;

if (a > 20) {
    if (b > 10) {
        System.out.print("P");
    }
} else {
    System.out.print("Q");
}

if (a % 5 == 0 && b % 3 == 0) {
    System.out.print("R");
}
```

A) `P`  
B) `Q`  
C) `R`  
D) `PR`  
E) `PQR`

---

### **Question 12**
Given the following code and input: `word 25 50`

```java
Scanner scan = new Scanner(System.in);

if (scan.hasNext()) {
    String s = scan.next();
    if (scan.hasNextInt()) {
        int x = scan.nextInt();
        int y = scan.nextInt();
        System.out.println(s.length() + x + y);
    }
}
```

What is printed?

A) `79`  
B) `word75`  
C) `4 25 50`  
D) `42550`  
E) Runtime error

---

### **Question 13**
What is the value of `result`?

```java
int a = 18;
int b = 5;
int result = a / b + a % b * b - b;
```

A) `13`  
B) `15`  
C) `18`  
D) `20`  
E) `23`

---

### **Question 14**
Consider the following code:

```java
boolean p = true;
boolean q = false;
boolean r = true;

boolean result = (p || q) && (!q && r) || (p && !r);
System.out.println(result);
```

What is printed?

A) `true`  
B) `false`  
C) Cannot be determined  
D) Compile-time error  
E) Runtime error

---

### **Question 15**
What is the output if the user enters: `42 HELLO`?

```java
Scanner input = new Scanner(System.in);
int age = input.nextInt();
input.nextLine();
String name = input.nextLine();

if (age >= 18 && name.length() > 3) {
    System.out.println("Adult: " + name);
} else if (age >= 13) {
    System.out.println("Teen: " + name);
} else {
    System.out.println("Child: " + name);
}
```

A) `Adult: HELLO`  
B) `Adult: `  
C) `Teen: HELLO`  
D) `Child: HELLO`  
E) Runtime error

---

### **Question 16**
What value is stored in `x`?

```java
int x = 5;
x = x++ + ++x + x++;
System.out.println(x);
```

A) `17`  
B) `18`  
C) `19`  
D) `20`  
E) `21`

---

### **Question 17**
Consider the following code:

```java
int num = 47;

if (num > 50) {
    System.out.print("A");
} else if (num > 40) {
    System.out.print("B");
} else if (num > 30) {
    System.out.print("C");
}

if (num % 10 == 7) {
    System.out.print("D");
}
```

What is printed?

A) `A`  
B) `B`  
C) `BD`  
D) `CD`  
E) `ABCD`

---

### **Question 18**
What is the minimum value that can be assigned to a variable of type `short`?

A) `-32768`  
B) `-32767`  
C) `-128`  
D) `0`  
E) `-2147483648`

---

### **Question 19**
Given this code:

```java
double x = 9.7;
int y = (int) (x + 0.5);
int z = (int) x + 1;
System.out.println(y + " " + z);
```

What is printed?

A) `9 9`  
B) `10 10`  
C) `9 10`  
D) `10 11`  
E) `10.2 10`

---

### **Question 20**
What is the output?

```java
int x = 15;
int y = 4;

if (x > 10)
    if (y > 5)
        System.out.println("A");
    else
        System.out.println("B");
else if (x > 5)
    System.out.println("C");
else
    System.out.println("D");
```

A) `A`  
B) `B`  
C) `C`  
D) `D`  
E) Nothing is printed

---

## Section II: Free Response Questions (5 questions)

### **Question 21 (8 points)**
Write a complete Java program called `QuadraticChecker` that:

1. Uses Scanner to read three double values: `a`, `b`, and `c` (coefficients of a quadratic equation ax² + bx + c = 0)
2. Validates that `a` is not zero (if zero, print "Not a quadratic equation" and exit)
3. Calculates the discriminant: `b² - 4ac`
4. Based on the discriminant value:
   - If positive: print "Two real roots"
   - If zero: print "One real root"
   - If negative: print "Two complex roots"
5. Additionally, if the equation has two real roots, print whether they are both positive, both negative, or of different signs

**Example Output 1:**
```
Enter coefficients a, b, c: 1 -5 6
Discriminant: 1.0
Two real roots
Both roots are positive
```

**Example Output 2:**
```
Enter coefficients a, b, c: 1 2 5
Discriminant: -16.0
Two complex roots
```

---

### **Question 22 (7 points)**
Analyze the following code segment:

```java
Scanner input = new Scanner(System.in);
System.out.print("Enter age: ");
int age = input.nextInt();
System.out.print("Enter height in cm: ");
double height = input.nextDouble();

String category;
if (age < 13)
    category = "Child";
else if (age < 18)
    category = "Teen";
else if (age < 65)
    category = "Adult";
else
    category = "Senior";

if (height < 150)
    category = category + " - Short";
else if (height > 180)
    category = category + " - Tall";

System.out.println("Category: " + category);
```

**Part A (3 points):** If the user enters age `16` and height `185`, what will be printed? Show your work.

**Part B (2 points):** What is the purpose of the String variable `category` being reassigned with concatenation?

**Part C (2 points):** Suggest one improvement to make this code more maintainable, explaining why it would be better.

---

### **Question 23 (8 points)**
Write a complete Java method called `validatePassword` with the following signature:

```java
public static boolean validatePassword(String password)
```

The method should return `true` if the password meets ALL of the following criteria:
- Length is between 8 and 20 characters (inclusive)
- Contains at least one digit (0-9)
- Contains at least one uppercase letter (A-Z)
- Contains at least one lowercase letter (a-z)
- Does not contain spaces

**Note:** Use only concepts from Unit 1 (primitive types, variables, conditionals, String methods). Do not use loops or arrays.

**Example test cases:**
- `validatePassword("Abc12345")` → returns `true`
- `validatePassword("abc123")` → returns `false` (too short, no uppercase)
- `validatePassword("ABCD1234")` → returns `false` (no lowercase)
- `validatePassword("Abc 1234")` → returns `false` (contains space)

---

### **Question 24 (9 points)**
Consider the following program that calculates BMI (Body Mass Index):

```java
import java.util.Scanner;

public class BMICalculator {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Enter weight in kg: ");
        double weight = scan.nextDouble();
        
        System.out.print("Enter height in meters: ");
        double height = scan.nextDouble();
        
        double bmi = weight / (height * height);
        
        String category;
        if (bmi < 18.5) {
            category = "Underweight";
        } else if (bmi < 25) {
            category = "Normal";
        } else if (bmi < 30) {
            category = "Overweight";
        } else {
            category = "Obese";
        }
        
        System.out.println("BMI: " + bmi);
        System.out.println("Category: " + category);
    }
}
```

**Part A (3 points):** What will be printed if the user enters weight `70` and height `1.75`?

**Part B (3 points):** Identify two potential problems with this code when handling user input (e.g., invalid data). For each problem, explain what could go wrong.

**Part C (3 points):** Add input validation to ensure that:
- Weight is between 20 and 300 kg
- Height is between 0.5 and 2.5 meters
- If either value is invalid, print an error message and use a default "Invalid input" category

Write only the modified code section that includes the validation logic.

---

### **Question 25 (8 points)**
Write a complete Java program called `TaxCalculator` that:

1. Prompts the user to enter their annual income (as a double)
2. Prompts the user to enter their filing status using a single character:
   - 'S' or 's' for Single
   - 'M' or 'm' for Married
   - 'H' or 'h' for Head of Household
3. Calculates the tax based on the following rules:

**Single (S):**
- Income ≤ $50,000: 10% tax
- Income > $50,000 and ≤ $100,000: 15% tax
- Income > $100,000: 20% tax

**Married (M):**
- Income ≤ $75,000: 8% tax
- Income > $75,000 and ≤ $150,000: 12% tax
- Income > $150,000: 18% tax

**Head of Household (H):**
- Income ≤ $60,000: 9% tax
- Income > $60,000 and ≤ $120,000: 13% tax
- Income > $120,000: 19% tax

4. If an invalid filing status is entered, print "Invalid status" and set tax to 0
5. Display the results showing:
   - Filing status (full name)
   - Annual income
   - Tax rate percentage
   - Total tax amount

**Example Output:**
```
Enter annual income: 85000
Enter filing status (S/M/H): M
Filing Status: Married
Annual Income: $85000.00
Tax Rate: 12%
Total Tax: $10200.00
```

**Grading Rubric:**
- Correct Scanner usage (1 point)
- Input validation for filing status (2 points)
- Correct tax calculation logic (3 points)
- Proper output formatting (2 points)

---

## Answer Key - Multiple Choice

1. **C** - Byte overflow: 128 exceeds byte range (127), wraps to -128
2. **B** - Floating-point precision error: 0.1 + 0.1 + 0.1 ≠ 0.3 exactly
3. **A** - next() reads tokens, concatenation without spaces
4. **B** - 5 + 6 - 2 % 3 = 5 + 6 - 2 = 9
5. **B** - Integer division gives 3.0, casting gives 3.75
6. **C** - result is true, x becomes 15, then doubled to 30
7. **A** - 7 > 5 and "apple" < "banana" (alphabetically)
8. **A** - 7/3 = 2 > 2 is false, 7%3 = 1 is true, z = 7/3 = 2... wait, let me recalculate. 7/3 = 2 (integer division), 2 > 2 is false. Then check 7%3 == 1 which is true, so z = 7/3 = 2. Actually, the condition is checked again. Let me trace: x/y = 7/3 = 2, 2 > 2 is false. Then else if: x%y = 7%3 = 1, 1 == 1 is true, so z = x/y = 2. Answer is B: 2.
9. **D** - All three if statements are independent; 85 ≥ 70 and 85 ≥ 32
10. **A** - (20 < 30 && 30 < 40) = true || false = true
11. **D** - First nested if prints "P", second independent if prints "R"
12. **A** - "word".length() = 4, 4 + 25 + 50 = 79
13. **C** - 18/5 + 18%5*5 - 5 = 3 + 3*5 - 5 = 3 + 15 - 5 = 13. Answer is A: 13.
14. **A** - (true || false) && (true && true) || (true && false) = true && true || false = true
15. **A** - nextLine() after nextInt() consumes empty line, age 42 ≥ 18 and "HELLO".length() = 5 > 3
16. **C** - x=5, x++ gives 5 (x becomes 6), ++x gives 7 (x becomes 7), x++ gives 7 (x becomes 8), x = 5+7+7 = 19
17. **C** - 47 > 40 prints "B", 47 % 10 = 7 prints "D"
18. **A** - Short range: -32768 to 32767
19. **B** - (int)(9.7+0.5) = (int)10.2 = 10, (int)9.7 + 1 = 9 + 1 = 10
20. **B** - x > 10 is true, y > 5 is false, prints "B"

---

## Scoring Guide

**Multiple Choice:** 20 questions × 2 points = 40 points  
**Free Response Questions:**
- Q21: 8 points
- Q22: 7 points
- Q23: 8 points
- Q24: 9 points
- Q25: 8 points
- **Total FRQ:** 40 points

**Total Test Score:** 80 points

**Grade Scale:**
- 72-80: A (90-100%)
- 64-71: B (80-89%)
- 56-63: C (70-79%)
- 48-55: D (60-69%)
- Below 48: F

---

## Key Concepts Tested

**Advanced Topics:**
- Byte overflow and data type ranges
- Floating-point precision issues
- Scanner buffer management with mixed input
- Complex boolean expressions and operator precedence
- Nested conditionals and dangling else
- Type casting nuances
- Pre/post increment in complex expressions
- Independent vs. dependent if statements
- String comparison and manipulation
- Input validation techniques

**Skills Assessed:**
- Trace code execution mentally
- Understand operator precedence and associativity
- Apply De Morgan's laws and boolean algebra
- Handle edge cases in numeric computations
- Debug common Scanner input errors
- Design robust input validation
- Write maintainable conditional logic

---

**Good luck on your AP Computer Science A preparation!**
