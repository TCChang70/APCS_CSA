# 📚 AP Computer Science A - Practice Test
## Scanner Input and Conditional Statements (if/else)

**Test Instructions:**
- Total Points: 100
- Time Limit: 75 minutes
- Section I - Multiple Choice: 60 points (20 questions, 3 points each)
- Section II - Free Response: 40 points (2 questions)
- Calculator: Not permitted
- Reference materials: Java Quick Reference Guide provided

---

## 📝 Section I: Multiple Choice Questions (60 points)
*Select the best answer for each question.*

### **Question 1** (3 points)
What is the output of the following code when the user enters `5`?
```java
Scanner input = new Scanner(System.in);
int num = input.nextInt();
if (num > 3)
    System.out.print("High ");
if (num > 7)
       System.out.print("Very High");
else
       System.out.print("Medium");
```

A) `High Very High`  
B) `High Medium`  
C) `Medium`  
D) `High`  
E) `Very High`

---

### **Question 2** (3 points)
Consider the following code segment:
```java
Scanner scan = new Scanner(System.in);
String word = scan.next();
System.out.println(word);
```
If the user enters `Hello World`, what is printed?

A) `Hello World`  
B) `Hello`  
C) `World`  
D) `HelloWorld`  
E) Compilation error

---

### **Question 3** (3 points)
What is the output when the user enters `12`?
```java
Scanner input = new Scanner(System.in);
int x = input.nextInt();
if (x < 10)
    System.out.println("A");
else if (x < 20)
    System.out.println("B");
else if (x < 30)
    System.out.println("C");
else
    System.out.println("D");
```

A) `A`  
B) `B`  
C) `C`  
D) `D`  
E) No output

---

### **Question 4** (3 points)
Which of the following correctly reads a double value from the user?

A) `double value = input.nextDouble();`  
B) `double value = input.readDouble();`  
C) `double value = input.getDouble();`  
D) `double value = input.scanDouble();`  
E) `double value = input.nextdouble();`

---

### **Question 5** (3 points)
What happens when the following code executes and the user enters `3.5`?
```java
Scanner input = new Scanner(System.in);
int num = input.nextInt();
System.out.println(num);
```

A) Prints `3`  
B) Prints `3.5`  
C) Prints `4`  
D) Runtime exception (InputMismatchException)  
E) Compilation error

---

### **Question 6** (3 points)
What is the output when `score` is `85`?
```java
int score = 85;
if (score >= 90)
    System.out.print("A");
else if (score >= 80)
    System.out.print("B");
else if (score >= 70)
    System.out.print("C");
System.out.print("Pass");
```

A) `A`  
B) `B`  
C) `BPass`  
D) `Pass`  
E) `APass`

---

### **Question 7** (3 points)
Consider the following code:
```java
Scanner input = new Scanner(System.in);
String line = input.nextLine();
String word = input.next();
```
If the user enters:
```
Java Programming
Python
```
What is stored in `word`?

A) `Java Programming`  
B) `Java`  
C) `Python`  
D) `Programming`  
E) Runtime error

---

### **Question 8** (3 points)
What is the output when `x = 5` and `y = 10`?
```java
int x = 5, y = 10;
if (x > 3){
    if (y < 15)
        System.out.print("A");
    else
        System.out.print("B");
}
else
    System.out.print("C");
```

A) `A`  
B) `B`  
C) `C`  
D) `AB`  
E) No output

---

### **Question 9** (3 points)
Which method should be used to read an entire line of text including spaces?

A) `next()`  
B) `nextLine()`  
C) `nextString()`  
D) `readLine()`  
E) `getLine()`

---

### **Question 10** (3 points)
What is the output when the user enters `7`?
```java
Scanner input = new Scanner(System.in);
int num = input.nextInt();
if (num % 2 == 0) {
    System.out.println("Even");
} else {
    System.out.println("Odd");
}
```

A) `Even`  
B) `Odd`  
C) `7`  
D) `true`  
E) Compilation error

---

### **Question 11** (3 points)
Consider the following code:
```java
Scanner scan = new Scanner(System.in);
boolean flag = scan.nextBoolean();
```
Which input will cause an InputMismatchException?

A) `true`  
B) `false`  
C) `TRUE`  
D) `yes`  
E) Both C and D

---

### **Question 12** (3 points)
What is the output when `age = 17`?
```java
int age = 17;
if (age >= 18) {
    System.out.println("Adult");
} 
if (age < 18) {
    System.out.println("Minor");
}
```

A) `Adult`  
B) `Minor`  
C) `Adult` followed by `Minor`  
D) No output  
E) Compilation error

---

### **Question 13** (3 points)
What is printed when the user enters `apple banana`?
```java
Scanner input = new Scanner(System.in);
String first = input.next();
String second = input.next();
System.out.println(second + " " + first);
```

A) `apple banana`  
B) `banana apple`  
C) `apple`  
D) `banana`  
E) Runtime error

---

### **Question 14** (3 points)
What is the result when `x = 5`, `y = 5`?
```java
int x = 5, y = 5;
if (x == y) {
    if (x > 0) {
        System.out.print("Positive");
    }
    System.out.print(" Equal");
}
```

A) `Positive`  
B) `Equal`  
C) `Positive Equal`  
D) No output  
E) Compilation error

---

### **Question 15** (3 points)
Which of the following is the correct way to close a Scanner object?

A) `input.close();`  
B) `input.end();`  
C) `input.stop();`  
D) `Scanner.close(input);`  
E) `close(input);`

---

### **Question 16** (3 points)
What is the output when `num = 0`?
```java
int num = 0;
if (num > 0)
    System.out.print("Positive");
else if (num < 0)
    System.out.print("Negative");
else
    System.out.print("Zero");
```

A) `Positive`  
B) `Negative`  
C) `Zero`  
D) No output  
E) Compilation error

---

### **Question 17** (3 points)
Consider the following code:
```java
Scanner input = new Scanner(System.in);
System.out.print("Enter number: ");
int x = input.nextInt();
input.nextLine(); // Line X
String name = input.nextLine();
```
What is the purpose of Line X?

A) To read the next line  
B) To consume the newline character left by nextInt()  
C) To clear the Scanner buffer  
D) To reset the Scanner  
E) It serves no purpose

---

### **Question 18** (3 points)
What is the output when `a = 10`, `b = 20`, `c = 15`?
```java
int a = 10, b = 20, c = 15;
if (a < b && b > c) {
    System.out.print("X");
}
if (a < c || c > b) {
    System.out.print("Y");
}
```

A) `X`  
B) `Y`  
C) `XY`  
D) No output  
E) Compilation error

---

### **Question 19** (3 points)
What happens when the following code executes and the user enters nothing (just presses Enter)?
```java
Scanner input = new Scanner(System.in);
String text = input.nextLine();
System.out.println(text.length());
```

A) Prints `null`  
B) Prints `0`  
C) Runtime exception (NullPointerException)  
D) Runtime exception (NoSuchElementException)  
E) Compilation error

---

### **Question 20** (3 points)
What is the output when `grade = 'B'`?
```java
char grade = 'B';
if (grade == 'A' || grade == 'B') {
    System.out.print("Excellent");
} else if (grade == 'C') {
    System.out.print("Good");
} else {
    System.out.print("Needs Improvement");
}
```

A) `Excellent`  
B) `Good`  
C) `Needs Improvement`  
D) `B`  
E) Compilation error

---

## 💻 Section II: Free Response Questions (40 points)

### **Question 1: Grade Calculator with Multiple Conditions (20 points)**

Write a complete Java program that calculates a student's final grade based on multiple criteria. Your program should:

**Requirements:**
1. Use Scanner to prompt and read the following inputs:
   - Student name (String)
   - Homework average (double, 0-100)
   - Midterm exam score (double, 0-100)
   - Final exam score (double, 0-100)
   - Extra credit points (int, 0-10)

2. Calculate the final score using these weights:
   - Homework: 30%
   - Midterm: 30%
   - Final exam: 40%
   - Add extra credit points to the weighted average

3. Determine letter grade using this scale:
   - A: 90-100
   - B: 80-89
   - C: 70-79
   - D: 60-69
   - F: below 60

4. Display detailed results including:
   - Student name
   - Individual scores
   - Weighted average (before extra credit)
   - Final score (after extra credit)
   - Letter grade
   - Pass/Fail status (passing is C or better)

5. Use appropriate if-else statements for grade determination

**Sample Run:**
```
=== Grade Calculator ===
Enter student name: Alice Johnson
Enter homework average: 88.5
Enter midterm exam score: 92.0
Enter final exam score: 85.0
Enter extra credit points: 3

=== Grade Report for Alice Johnson ===
Homework Average: 88.5 (30%)
Midterm Exam: 92.0 (30%)
Final Exam: 85.0 (40%)
Weighted Average: 88.15
Extra Credit: +3.0
Final Score: 91.15
Letter Grade: A
Status: PASS
```

**Grading Criteria:**
- Correct Scanner usage for all inputs (4 points)
- Proper variable declarations and data types (2 points)
- Correct weighted average calculation (4 points)
- Correct if-else structure for grade determination (4 points)
- Complete and formatted output (3 points)
- Pass/Fail logic implementation (2 points)
- Code organization and comments (1 point)

---

### **Question 2: Number Classification System (20 points)**

Write a Java program that reads an integer from the user and performs comprehensive classification and analysis. Your program should:

**Requirements:**
1. Use Scanner to read an integer from the user
2. Determine and display ALL of the following properties that apply:
   - Sign: Positive, Negative, or Zero
   - Magnitude: Single-digit (0-9), Double-digit (10-99), Triple-digit (100-999), or Larger
   - Even or Odd (if not zero)
   - Divisibility: by 3, by 5, by both 3 and 5, or by neither
   - Range category: Small (1-50), Medium (51-200), Large (201-1000), Very Large (over 1000), or Negative range

3. Use nested if statements and logical operators appropriately
4. Format output clearly with labels
5. Handle edge cases (zero, negative numbers)

**Sample Run 1:**
```
Enter an integer: 45

=== Number Analysis for 45 ===
Sign: Positive
Magnitude: Double-digit
Parity: Odd
Divisibility: Divisible by 3 and 5 (multiple of 15)
Range: Small (1-50)
```

**Sample Run 2:**
```
Enter an integer: -128

=== Number Analysis for -128 ===
Sign: Negative
Magnitude: Triple-digit
Parity: Even
Divisibility: Not divisible by 3 or 5
Range: Negative number
```

**Sample Run 3:**
```
Enter an integer: 0

=== Number Analysis for 0 ===
Sign: Zero
Magnitude: Single-digit
Parity: Zero has no parity
Divisibility: Zero is divisible by all numbers
Range: Zero is neither positive nor negative
```

**Grading Criteria:**
- Correct Scanner usage and input (2 points)
- Sign determination (positive/negative/zero) (2 points)
- Magnitude classification (2 points)
- Even/odd determination with zero handling (3 points)
- Divisibility checks (3 and 5) (3 points)
- Range classification (3 points)
- Proper use of if-else and nested conditionals (3 points)
- Code clarity and comments (2 points)

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
- Write your code on separate paper or computer
- Include all necessary import statements
- Use proper indentation and comments
- Test your code with the given sample inputs

---

## 📖 Study Tips

**Key Topics to Review:**

**Scanner Class:**
1. Creating Scanner objects: `Scanner input = new Scanner(System.in);`
2. Reading different data types:
   - `nextInt()` - reads integer
   - `nextDouble()` - reads double
   - `next()` - reads next token (word)
   - `nextLine()` - reads entire line
   - `nextBoolean()` - reads boolean
3. Common pitfall: newline character after nextInt()/nextDouble()
4. Closing Scanner: `input.close();`

**Conditional Statements:**
1. Simple if statement
2. if-else statement
3. if-else-if ladder
4. Nested if statements
5. Logical operators: &&, ||, !
6. Comparison operators: ==, !=, <, >, <=, >=
7. Short-circuit evaluation

**Common Mistakes to Avoid:**
- Using `=` instead of `==` in conditions
- Forgetting braces {} for multi-line blocks
- nextInt() leaving newline in buffer
- InputMismatchException when types don't match
- Dangling else problem in nested ifs
- Not handling all possible cases
- Incorrect operator precedence in complex conditions

**Best Practices:**
- Always use braces {} even for single statements
- Use meaningful variable names
- Add comments for complex conditions
- Test edge cases (zero, negative, boundary values)
- Close Scanner when done
- Validate user input when possible

---

**Good luck on your test! Remember to read each question carefully and test your logic with different values.**
