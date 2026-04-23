# AP Computer Science A - Unit 1 Advanced Practice Test
## Primitive Types, Scanner, and Conditional Statements

**Total Questions: 25 | Time Limit: 45 minutes | Difficulty: Advanced**

---

## Part I: Multiple Choice Questions (20 questions)

### **Question 1**
What is the output of the following code segment?

```java
int x = 7;
double y = 3;
System.out.println(x / y);
System.out.println((double) x / (int) y);
```

A) `2.333333333333333` followed by `2.333333333333333`  
B) `2.0` followed by `2.333333333333333`  
C) `2` followed by `2.333333333333333`  
D) `2.333333333333333` followed by `2.0`  
E) Compile-time error

---

### **Question 2**
Consider the following code segment:

```java
Scanner scan = new Scanner(System.in);
int a = scan.nextInt();
int b = scan.nextInt();
scan.nextLine();
String str = scan.nextLine();
```

If the input is:
```
15 20
Hello World
```

What will be stored in the variable `str`?

A) `"15"`  
B) `"20"`  
C) `"Hello World"`  
D) `"Hello"`  
E) An empty string `""`

---

### **Question 3**
What is the result of the following expression?

```java
int result = 17 % 5 * 3 + 12 / 5;
System.out.println(result);
```

A) `2`  
B) `6`  
C) `8`  
D) `10`  
E) `11`

---

### **Question 4**
Which of the following expressions evaluates to `true`?

```java
int x = 5, y = 10, z = 5;
```

A) `x == z && y > x || z < y`  
B) `!(x != z) && (y <= x)`  
C) `x > y || z >= y && x == z`  
D) `(x + z == y) && !(y < x)`  
E) All of the above

---

### **Question 5**
Consider the following code segment:

```java
double a = 5.0;
double b = 9.0;
a += b;
b -= a;
a *= 2;
System.out.println(a + " " + b);
```

What is printed?

A) `14.0 -14.0`  
B) `28.0 -5.0`  
C) `28.0 -14.0`  
D) `14.0 -5.0`  
E) `10.0 4.0`

---

### **Question 6**
What is the value of `x` after the following code executes?

```java
int x = 10;
if (x > 5 && ++x > 10) {
    x += 5;
} else if (x < 15 || x-- < 10) {
    x *= 2;
}
System.out.println(x);
```

A) `10`  
B) `11`  
C) `15`  
D) `22`  
E) `32`

---

### **Question 7**
Which of the following code segments correctly reads an integer, a double, and a String (including spaces) from user input in that order?

```java
Scanner input = new Scanner(System.in);
```

A)
```java
int num = input.nextInt();
double dec = input.nextDouble();
String text = input.nextLine();
```

B)
```java
int num = input.nextInt();
double dec = input.nextDouble();
input.nextLine();
String text = input.nextLine();
```

C)
```java
int num = input.nextInt();
input.nextLine();
double dec = input.nextDouble();
String text = input.nextLine();
```

D)
```java
int num = input.nextInt();
double dec = input.nextDouble();
String text = input.next();
```

E)
```java
String text = input.nextLine();
int num = input.nextInt();
double dec = input.nextDouble();
```

---

### **Question 8**
Consider the following code:

```java
int a = 15;
int b = 20;
boolean result = a++ > 15 || ++b < 21;
System.out.println(a + " " + b + " " + result);
```

What is printed?

A) `15 20 false`  
B) `16 21 true`  
C) `16 20 true`  
D) `16 20 false`  
E) `15 21 true`

---

### **Question 9**
What is the maximum value that can be stored in a variable of type `byte` in Java?

A) `127`  
B) `128`  
C) `255`  
D) `256`  
E) `32767`

---

### **Question 10**
Consider the following code segment:

```java
int x = 25;
int y = 40;

if (x < 30 && y > 35) {
    if (x % 5 == 0) {
        System.out.println("A");
    } else {
        System.out.println("B");
    }
} else if (y % 10 == 0) {
    System.out.println("C");
} else {
    System.out.println("D");
}
```

What is printed?

A) `A`  
B) `B`  
C) `C`  
D) `D`  
E) Nothing is printed

---

### **Question 11**
What is the output of the following code?

```java
double x = 7.5;
int y = (int) x;
x = y++;
System.out.println(x + " " + y);
```

A) `7.0 7`  
B) `7.0 8`  
C) `7.5 8`  
D) `8.0 8`  
E) Compile-time error

---

### **Question 12**
Consider the following code segment:

```java
Scanner input = new Scanner(System.in);
int count = 0;

if (input.hasNextInt()) {
    int num = input.nextInt();
    if (num > 0) {
        count++;
    }
}
if (input.hasNextInt()) {
    int num = input.nextInt();
    if (num > 0) {
        count++;
    }
}
System.out.println(count);
```

If the user enters: `10 -5 20`

What is printed?

A) `0`  
B) `1`  
C) `2`  
D) `3`  
E) Runtime error

---

### **Question 13**
Which of the following expressions will evaluate to `true` if `x` is between 10 and 20 (inclusive)?

A) `x >= 10 && x <= 20`  
B) `!(x < 10 || x > 20)`  
C) `x >= 10 || x <= 20`  
D) Both A and B  
E) All of the above

---

### **Question 14**
What is the output of the following code?

```java
int x = 5;
int y = 10;
int z = ++x + y++ + x++;
System.out.println(x + " " + y + " " + z);
```

A) `6 10 21`  
B) `7 11 21`  
C) `7 11 22`  
D) `7 11 23`  
E) `6 11 21`

---

### **Question 15**
Consider the following code segment:

```java
double a = 10.0;
double b = 3.0;
int c = (int) (a / b);
double d = a / b - c;
System.out.println(d);
```

What is printed?

A) `0.0`  
B) `0.3333333333333333`  
C) `3.0`  
D) `3.3333333333333335`  
E) Compile-time error

---

### **Question 16**
What is the result of the following code segment?

```java
int x = 8;
int y = 5;

if (x > y) {
    if (x % 2 == 0)
        System.out.print("A");
    else
        System.out.print("B");
    System.out.print("C");
} else {
    System.out.print("D");
}
System.out.print("E");
```

A) `ACE`  
B) `BCE`  
C) `DE`  
D) `AE`  
E) `CE`

---

### **Question 17**
Consider the following code:

```java
Scanner scan = new Scanner(System.in);
double num1 = scan.nextDouble();
double num2 = scan.nextDouble();
double avg = (num1 + num2) / 2;

if (avg >= 90)
    System.out.println("A");
else if (avg >= 80)
    System.out.println("B");
else if (avg >= 70)
    System.out.println("C");
else
    System.out.println("F");
```

If the user enters: `85.5 94.5`

What is printed?

A) `A`  
B) `B`  
C) `C`  
D) `F`  
E) Nothing is printed

---

### **Question 18**
What is the value of `result` after the following code executes?

```java
int a = 12;
int b = 7;
int result = a / b * b + a % b;
```

A) `11`  
B) `12`  
C) `13`  
D) `14`  
E) `19`

---

### **Question 19**
Consider the following code segment:

```java
boolean x = true;
boolean y = false;
boolean z = (x && !y) || (!x && y);
System.out.println(z);
```

What is printed?

A) `true`  
B) `false`  
C) `0`  
D) `1`  
E) Compile-time error

---

### **Question 20**
What is the output of the following code?

```java
int x = 10;
int y = 20;
int z = 30;

if (x < y)
    if (y < z)
        System.out.println("A");
    else
        System.out.println("B");
else if (x < z)
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

## Part II: Free Response Questions (5 questions)

### **Question 21 (Programming Problem)**
Write a complete Java program that does the following:

1. Prompts the user to enter three integer values
2. Reads the three integers using Scanner
3. Determines and prints which value is the largest and which is the smallest
4. If all three values are equal, print "All values are equal"
5. Calculate and print the average of the three numbers as a double value

**Example Output 1:**
```
Enter three integers: 45 23 67
Largest: 67
Smallest: 23
Average: 45.0
```

**Example Output 2:**
```
Enter three integers: 10 10 10
All values are equal
Average: 10.0
```

---

### **Question 22 (Code Analysis)**
Consider the following code segment:

```java
Scanner input = new Scanner(System.in);
System.out.print("Enter a number: ");
int num = input.nextInt();

int result = 0;
if (num > 0) {
    result = num % 10;
} else if (num < 0) {
    result = -(num % 10);
} else {
    result = 0;
}
System.out.println("Result: " + result);
```

**Part A:** What does this code segment do? Explain in 1-2 sentences.

**Part B:** What will be printed if the user enters `-37`?

**Part C:** Identify and explain one potential issue with this code if the user enters non-integer input.

---

### **Question 23 (Programming Problem)**
Write a Java method called `calculateGrade` that takes a Scanner object as a parameter and does the following:

1. Prompts the user to enter a numerical score (0-100)
2. Validates that the score is within the valid range (0-100)
3. If invalid, prints an error message and returns "Invalid"
4. If valid, determines the letter grade based on:
   - 90-100: A
   - 80-89: B
   - 70-79: C
   - 60-69: D
   - 0-59: F
5. Returns the letter grade as a String

**Method signature:**
```java
public static String calculateGrade(Scanner input)
```

---

### **Question 24 (Data Type Understanding)**
Answer the following questions about Java primitive data types:

**Part A:** Explain why the following code produces unexpected results and how to fix it:
```java
int total = 100;
int count = 3;
double average = total / count;
System.out.println(average);  // Prints 33.0 instead of 33.333...
```

**Part B:** What is the difference between the following two code segments in terms of their output?
```java
// Segment 1
int x = 5;
System.out.println(x++ + ++x);

// Segment 2  
int x = 5;
System.out.println(++x + x++);
```

**Part C:** Explain why `byte` and `short` data types are less commonly used than `int` in Java programming.

---

### **Question 25 (Complex Problem Solving)**
Write a complete Java program that simulates a simple temperature converter. The program should:

1. Display a menu with three options:
   - 1: Convert Fahrenheit to Celsius
   - 2: Convert Celsius to Fahrenheit  
   - 3: Exit
2. Use Scanner to read the user's choice
3. Based on the choice:
   - For option 1: Read a Fahrenheit temperature and convert to Celsius using the formula: `C = (F - 32) * 5/9`
   - For option 2: Read a Celsius temperature and convert to Fahrenheit using the formula: `F = C * 9/5 + 32`
   - For option 3: Print "Goodbye!" and end the program
   - For any other input: Print "Invalid choice"
4. Display the result with 2 decimal places
5. Validate that the temperature is above absolute zero:
   - Fahrenheit: must be >= -459.67
   - Celsius: must be >= -273.15

**Sample Run:**
```
Temperature Converter
1. Fahrenheit to Celsius
2. Celsius to Fahrenheit
3. Exit
Enter your choice: 1
Enter temperature in Fahrenheit: 98.6
98.60°F = 37.00°C
```

**Grading Criteria:**
- Correct menu display (2 points)
- Proper Scanner usage (2 points)
- Correct conversion formulas (3 points)
- Input validation for temperature (2 points)
- Formatted output with 2 decimal places (1 point)

---

## Additional Resources

**Practice Topics:**
- Operator precedence and associativity
- Scanner input handling with mixed data types
- Short-circuit evaluation in boolean expressions
- Nested conditional statements
- Type casting and data type ranges
- Pre/post increment/decrement operators
- Compound assignment operators
- Input validation techniques

**Common Mistakes to Avoid:**
1. Integer division truncation
2. Forgetting to consume newline after nextInt()/nextDouble()
3. Incorrect operator precedence assumptions
4. Misunderstanding short-circuit evaluation
5. Confusing assignment (=) with comparison (==)
6. Off-by-one errors in range checking
7. Not validating user input
8. Confusion between pre-increment and post-increment

---


