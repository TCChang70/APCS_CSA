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

A) 2.5  
B) 2.0  
C) 2  
D) 3.0  
E) Compile-time error

```
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
---

### Question 3
What is the output of the following code?
```java
int a = 10;
int b = 3;
System.out.println(a % b + " " + a / b);

A) 1 3  
B) 3 1  
C) 1.0 3.0  
D) 3.333 3  
E) Compile-time error
```
---

### Question 4
Consider the following code:
```java
double x = 7.9;
int y = (int) x;
System.out.println(y);

What is printed?

A) 7  
B) 8  
C) 7.9  
D) 7.0  
E) Compile-time error
```
---

### Question 5
What is the result of the following expression?
```java
int result = 5 + 3 * 2 - 8 / 4;

A) 6  
B) 9  
C) 10  
D) 12  
E) 14
```
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

A) A  
B) B  
C) C  
D) AB  
E) No output
```
---

### Question 8
Consider the following code:
```java
Scanner scan = new Scanner(System.in);
int num = scan.nextInt();
String line = scan.nextLine();

If the input is "42 Hello World", what is stored in `line`?

A) "42 Hello World"  
B) "Hello World"  
C) " Hello World"  
D) ""  
E) "Hello"
```
---

### Question 9
What is the value of `result`?
```java
boolean a = true;
boolean b = false;
boolean result = a || b && !a;

A) true  
B) false  
C) Compile-time error  
D) Runtime error  
E) Depends on input
```
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

A) A  
B) B  
C) C  
D) BC  
E) ABC
```
---

### Question 12
What is the output?
```java
int x = 10;
x += 5;
x *= 2;
x -= 8;
System.out.println(x);

A) 22  
B) 27  
C) 30  
D) 32  
E) 42
```

---

### Question 13
Consider this code using Scanner:
```java
Scanner input = new Scanner(System.in);
double price = input.nextDouble();
int quantity = input.nextInt();

Which input would cause a runtime error?

A) 25.99 5  
B) 25 5  
C) 25.0 5  
D) ABC 5  
E) All of the above
```

---

### Question 14
What is the result?
```java
int a = 15;
int b = 4;
boolean result = (a > 10) && (b++ > 5);
System.out.println(b);

A) 4  
B) 5  
C) true  
D) false  
E) Compile-time error
```

---

### Question 15
Which expression correctly checks if a number `n` is between 10 and 20 (inclusive)?
```java
A) `10 <= n <= 20`  
B) `n >= 10 && n <= 20`  
C) `n => 10 && n =< 20`  
D) `10 <= n || n <= 20`  
E) `(n > 10) && (n < 20)`
```
---

### Question 16
What is the output?
```java
String str = "123";
int num = Integer.parseInt(str);
num += 7;
System.out.println(num);

A) 1237  
B) 130  
C) 123  
D) 7  
E) Compile-time error
```
---

### Question 17
Consider the following:
```java
int x = 5;
int y = 10;
int z = ++x + y++;
System.out.println(x + " " + y + " " + z);

What is printed?

A) 5 10 15  
B) 6 11 16  
C) 6 10 16  
D) 6 11 15  
E) 5 11 15
```
---

### Question 18
What happens when this code executes with input "Hello 123"?
```java
Scanner sc = new Scanner(System.in);
int number = sc.nextInt();

A) number = 123  
B) number = 0  
C) InputMismatchException  
D) Compile-time error  
E) NullPointerException
```

---

### Question 19
What is the value of `result`?
```java
int a = 5, b = 10, c = 15;
boolean result = (a < b) && (b < c) || (a > c);

A) true  
B) false  
C) Compile-time error  
D) Cannot be determined  
E) Runtime error
```
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
Enter operator (+, -, *, /, %): %
Result (int): 1

Enter first number: 10.5
Enter second number: 2
Enter operator (+, -, *, /, %): *
Result (double): 21.0
```

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

