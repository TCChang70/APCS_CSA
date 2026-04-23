# AP Computer Science A - Unit 1: Primitive Types
## Practice Test (Medium to Hard Difficulty)

**Time:** 45 minutes  
**Questions:** 20 multiple-choice questions  
**Instructions:** Choose the best answer for each question.

---

### Question 1
What is the output of the following code segment?

```java
int x = 15;
int y = 4;
double z = x / y;
System.out.println(z);
```

(A) 3.0  
(B) 3.75  
(C) 3  
(D) 4.0  
(E) Compile-time error

---

### Question 2
Consider the following code segment:

```java
int a = 7;
int b = 3;
a = a % b;
b = b % a;
System.out.println(a + " " + b);
```

What is printed as a result of executing this code segment?

(A) 1 0  
(B) 1 2  
(C) 2 1  
(D) 7 3  
(E) 0 1

---

### Question 3
Which of the following expressions evaluates to `true`?

```java
int p = 5;
int q = 12;
```

(A) `p + q == 17 && p * 2 > q`  
(B) `p * 3 > q || p < 0`  
(C) `q % p == 2 && q / p == 2`  
(D) `!(p > q) && p + q < 20`  
(E) `p == q / 2 || q % p != 2`

---

### Question 4
What is the result of the following code segment?

```java
double num = 17.0 / 5 + 3 * 2;
System.out.println(num);
```

(A) 6.0  
(B) 9.0  
(C) 9.4  
(D) 10.0  
(E) 12.4

---

### Question 5
Consider the following code segment:

```java
int x = 10;
int y = ++x + x++;
System.out.println(x + " " + y);
```

What is printed?

(A) 11 21  
(B) 12 22  
(C) 12 23  
(D) 11 22  
(E) 12 21

---

### Question 6
Which of the following will NOT cause a compile-time error?

(A) `int x = 2147483648;`  
(B) `double d = 3.14D;`  
(C) `boolean flag = 1;`  
(D) `char letter = "A";`  
(E) `int y = 5.0;`

---

### Question 7
What is the value of `result` after the following code executes?

```java
int a = 25;
int b = 7;
int result = a / b * b + a % b;
```

(A) 21  
(B) 25  
(C) 28  
(D) 32  
(E) 35

---

### Question 8
Consider the following code segment:

```java
int x = 5;
x += x++ - --x;
System.out.println(x);
```

What is the output?

(A) 4  
(B) 5  
(C) 6  
(D) 10  
(E) The code does not compile

---

### Question 9
What is stored in variable `c` after the following code executes?

```java
double a = 7.5;
double b = 2.0;
int c = (int)(a / b);
```

(A) 3  
(B) 3.0  
(C) 3.75  
(D) 4  
(E) Compile-time error

---

### Question 10
Which of the following correctly declares and initializes a variable to store the value 100000000000 (100 billion)?

(A) `int num = 100000000000;`  
(B) `long num = 100000000000;`  
(C) `long num = 100000000000L;`  
(D) `double num = 100000000000;`  
(E) Both (C) and (D)

---

### Question 11
What is the output of the following code?

```java
int a = 10;
int b = 20;
int c = 30;
a += b -= c /= 3;
System.out.println(a + " " + b + " " + c);
```

(A) 10 20 10  
(B) 20 10 10  
(C) 0 10 10  
(D) 10 10 10  
(E) 20 20 10

---

### Question 12
Consider the following code segment:

```java
double x = 8.0;
int y = (int)x / 3;
double z = x / 3;
System.out.println(y + " " + z);
```

What is printed?

(A) 2 2.666666666666667  
(B) 2 2.0  
(C) 2.666666666666667 2.666666666666667  
(D) 3 2.666666666666667  
(E) Compile-time error

---

### Question 13
What is the range of values that can be stored in a `byte` variable in Java?

(A) -128 to 127  
(B) 0 to 255  
(C) -32768 to 32767  
(D) -2147483648 to 2147483647  
(E) Any integer value

---

### Question 14
Which of the following expressions will produce a different result than the others?

(A) `x = x + 1;`  
(B) `x += 1;`  
(C) `x++;`  
(D) `++x;`  
(E) All produce the same result for the final value of x

---

### Question 15
What is the output of the following code segment?

```java
int num1 = 15;
int num2 = 4;
double result = (double)(num1 / num2);
System.out.println(result);
```

(A) 3.0  
(B) 3.75  
(C) 4.0  
(D) 15.0  
(E) Compile-time error

---

### Question 16
Consider the following code:

```java
int a = 5;
int b = 2;
double c = a / b + (double)a / b;
System.out.println(c);
```

What is printed?

(A) 2.5  
(B) 4.5  
(C) 5.0  
(D) 5.5  
(E) 7.5

---

### Question 17
What is the result after executing the following code?

```java
int x = 100;
x %= 30;
x /= 2;
x *= 3;
System.out.println(x);
```

(A) 15  
(B) 30  
(C) 45  
(D) 60  
(E) 90

---

### Question 18
Which of the following statements about primitive types in Java is FALSE?

(A) The `int` type can store values from approximately -2 billion to 2 billion  
(B) The `double` type provides more precision than the `float` type  
(C) Dividing two `int` values always produces an `int` result  
(D) A `char` variable can store any Unicode character  
(E) All primitive types are automatically initialized to zero in Java

---

### Question 19
What is printed by the following code segment?

```java
int x = 7;
int y = 3;
int z = x++ + ++y - x-- + --y;
System.out.println(z);
```

(A) 0  
(B) 2  
(C) 4  
(D) 6  
(E) 8

---

### Question 20
Consider the following code:

```java
double d1 = 0.1 + 0.1 + 0.1;
double d2 = 0.3;
boolean result = (d1 == d2);
System.out.println(result);
```

What is most likely to be printed?

(A) `true`, because 0.1 + 0.1 + 0.1 equals 0.3  
(B) `false`, because of floating-point precision issues  
(C) `true`, because Java automatically rounds the values  
(D) Compile-time error  
(E) Runtime error

---

## Part II: Free Response Questions (FRQs)

**Time:** 30 minutes  
**Instructions:** Write complete Java code to solve each problem. Show all your work.

---

### FRQ 1: Temperature Converter (8 points)

Write a method `convertTemperature` that takes a temperature value as a `double` and a `char` representing the scale ('C' for Celsius or 'F' for Fahrenheit), and converts it to the other scale.

**Conversion formulas:**
- Celsius to Fahrenheit: F = (C × 9/5) + 32
- Fahrenheit to Celsius: C = (F - 32) × 5/9

The method should return the converted temperature as a `double`, rounded to 2 decimal places.

**Method signature:**
```java
public static double convertTemperature(double temp, char scale)
```

**Examples:**
- `convertTemperature(0.0, 'C')` returns `32.0`
- `convertTemperature(100.0, 'C')` returns `212.0`
- `convertTemperature(32.0, 'F')` returns `0.0`
- `convertTemperature(98.6, 'F')` returns `37.0`

**Requirements:**
- Use appropriate primitive types
- Handle both uppercase and lowercase input ('C', 'c', 'F', 'f')
- Use proper type casting where necessary
- Round the result to 2 decimal places (Hint: multiply by 100, cast to int, divide by 100.0)

---

### FRQ 2: Digit Separator (9 points)

Write a method `separateDigits` that takes a three-digit positive integer and prints each digit on a separate line, along with its place value.

**Method signature:**
```java
public static void separateDigits(int number)
```

**Example:**
For input `745`, the output should be:
```
Hundreds: 7
Tens: 4
Ones: 5
```

For input `306`, the output should be:
```
Hundreds: 3
Tens: 0
Ones: 6
```

**Requirements:**
- Assume the input is always a three-digit number (100-999)
- Use integer division and modulus operations to extract each digit
- Do not use String methods or arrays
- Print output in the exact format shown

**Follow-up (2 additional points):**
Modify your method to also calculate and print the sum of the digits.

---

### FRQ 3: Time Calculator (10 points)

Write a method `calculateElapsedTime` that takes two time values in 24-hour format and calculates the elapsed time between them in hours and minutes.

**Method signature:**
```java
public static void calculateElapsedTime(int startHour, int startMinute, 
                                       int endHour, int endMinute)
```

**Examples:**

Input: `calculateElapsedTime(9, 30, 14, 45)`  
Output:
```
Elapsed time: 5 hours and 15 minutes
```

Input: `calculateElapsedTime(23, 45, 1, 15)`  
Output:
```
Elapsed time: 1 hours and 30 minutes
```

Input: `calculateElapsedTime(10, 50, 11, 5)`  
Output:
```
Elapsed time: 0 hours and 15 minutes
```

**Requirements:**
- Handle cases where end time is on the next day (e.g., start at 23:45, end at 1:15)
- Use only primitive types and arithmetic operations
- Assume all inputs are valid (0 ≤ hours ≤ 23, 0 ≤ minutes ≤ 59)
- Calculate total minutes first, then convert to hours and minutes
- Print output in the exact format shown

**Hint:** Convert both times to minutes since midnight, calculate the difference, handle the case where the difference is negative (next day).

---

### FRQ 4: Bill Splitter (12 points)

Write a complete program that helps split a restaurant bill among friends. The program should:

1. Prompt the user to enter the total bill amount (as a double)
2. Prompt for the number of people splitting the bill (as an int)
3. Prompt for the tip percentage (as an int, e.g., 15 for 15%)
4. Calculate and display:
   - The tip amount
   - The total bill including tip
   - The amount each person should pay
   - If the split is not even, show how many cents are left over

**Sample run:**
```
Enter the total bill: 87.50
Enter number of people: 4
Enter tip percentage: 18

--- Bill Summary ---
Subtotal: $87.50
Tip (18%): $15.75
Total: $103.25
Each person pays: $25.81
Remainder: 1 cent(s)
```

**Requirements:**
- Use appropriate primitive types
- Use compound assignment operators where appropriate
- Format currency to 2 decimal places
- Calculate the remainder in cents (use modulus operation)
- Include clear user prompts and output formatting

**Grading:**
- Correct calculations (5 points)
- Proper use of primitive types and operators (3 points)
- Handling of remainder calculation (2 points)
- Input/output formatting (2 points)

---

## End of Test

**Note:** Remember to review:
- Order of operations (PEMDAS)
- Integer vs. floating-point division
- Type casting (implicit and explicit)
- Pre-increment/post-increment operators
- Compound assignment operators
- Primitive type ranges and limitations
- Floating-point precision issues
- Scanner class for user input
- Modulus operator for extracting digits and remainders
