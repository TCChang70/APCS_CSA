# APCS CSA Scanner In-Depth Assessment - Complete Answer Key

## Comprehensive Test Based on CodeHS Textbook Chapters 1, 2, 3

---

## Quick Answer Index

### Part I: Scanner Fundamentals (20 points)
1. B  2. C  3. B  4. B  5. B  6. D  7. C  8. C  9. B  10. C

### Part II: Scanner Methods In-Depth Application (30 points)
11. B  12. B  13. B  14. C  15. C  16. C  17. B  18. C  19. A  20. A

---

## Detailed Solutions

## Part I: Scanner Fundamentals (20 points)

### 1. Scanner Class Basics (2 points)
**Answer: B**

**Detailed Explanation:**
```java
Scanner scanner = new Scanner(System.in);
```
- (A) ✗ Scanner is a reference type, not a primitive type
- (B) ✓ System.in indeed represents the standard input stream (keyboard input)
- (C) ✗ scanner is a variable name, Scanner is the class name
- (D) ✗ new keyword creates object instances, not for calling methods

**Key Concepts:**
- Scanner is a class in the java.util package
- System.in is an InputStream type object
- Variable names use camelCase (lowercase first letter)

---

### 2. Scanner Method Selection (2 points)
**Answer: C**

**Detailed Explanation:**
- (A) ✗ next() returns String, reads next string
- (B) ✗ nextLine() returns String, reads entire line
- (C) ✓ nextInt() returns int, reads an integer
- (D) ✗ read() is not a Scanner method

**Method Mapping Table:**
| Data Type | Scanner Method | Return Type |
|-----------|---------------|-------------|
| Integer | nextInt() | int |
| Decimal | nextDouble() | double |
| String | next() | String |
| Full Line | nextLine() | String |
| Boolean | nextBoolean() | boolean |

---

### 3. Scanner Import Statement (2 points)
**Answer: B**

**Detailed Explanation:**
```java
import java.util.Scanner;  // ✓ Correct

// Wrong examples:
include java.util.Scanner;  // C/C++ syntax
using java.util.Scanner;    // C# syntax
package java.util.Scanner;  // This defines a package, not imports
```

**Java Import Syntax Rules:**
1. Use `import` keyword
2. Full package path: `java.util.Scanner`
3. Place before class definition
4. End with semicolon

---

### 4. Scanner Resource Management (2 points)
**Answer: B**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);
int num = input.nextInt();
input.close();  // ✓ Best practice
```

**Why Close Scanner?**
- Scanner uses system resources
- Prevents resource leaks
- Prevents other programs from accessing the same resource

**Proper Closing Methods:**
```java
// Method 1: Manual closing
Scanner input = new Scanner(System.in);
// Use Scanner...
input.close();

// Method 2: try-with-resources (Java 7+)
try (Scanner input = new Scanner(System.in)) {
    // Use Scanner...
} // Automatically closed
```

---

### 5. Scanner Objects and Variables (2 points)
**Answer: B**

**Detailed Explanation:**
```java
Scanner sc1 = new Scanner(System.in);
Scanner sc2 = sc1;  // sc2 references the same object
sc1.close();        // Closes that object
// sc2 can no longer be used!
```

**Reference Type Characteristics:**
```java
// Memory diagram
[sc1] ----> [Scanner Object]
             ↑
[sc2] -------
// sc1 and sc2 point to the same object
// Closing either one closes the object
```

**Difference from Primitive Types:**
```java
// Primitive type
int a = 5;
int b = a;  // b copies a's value
a = 10;     // changing a doesn't affect b

// Reference type
Scanner s1 = new Scanner(System.in);
Scanner s2 = s1;  // s2 references same object
s1.close();       // s2 is affected too
```

---

### 6. Scanner Method Return Types (2 points)
**Answer: D**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);

// Methods returning String
String line = input.nextLine();  // ✓
String word = input.next();      // ✓

// Methods returning other types
int num = input.nextInt();          // returns int
double d = input.nextDouble();      // returns double
boolean b = input.hasNext();        // returns boolean
```

**Method Categories:**
- **Input methods**: next(), nextLine(), nextInt(), nextDouble()...
- **Checking methods**: hasNext(), hasNextInt(), hasNextDouble()... (return boolean)

---

### 7. Scanner Method Characteristics (2 points)
**Answer: C**

**Detailed Explanation:**
```java
int x = input.nextInt();  // non-void method, has return value
```

**Method Type Comparison:**

**Void Methods (no return value):**
```java
System.out.println("Hello");  // only performs action
input.close();                 // only performs action
```

**Non-void Methods (has return value):**
```java
int value = input.nextInt();      // returns int
String text = input.nextLine();   // returns String
boolean hasMore = input.hasNext(); // returns boolean
```

---

### 8. Scanner Class Properties (2 points)
**Answer: C**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);
// Scanner is a Reference Class
```

**Java Type Classification:**

**1. Primitive Types:**
- int, double, boolean, char, byte, short, long, float
- Store values directly

**2. Reference Types:**
- Classes: Scanner, String, Math...
- Arrays: int[], String[]...
- Interfaces: List, Set...
- Store object references (memory addresses)

**3. Wrapper Classes:**
- Integer, Double, Boolean, Character...
- A type of reference type, corresponding to primitive types

---

### 9. Scanner Constructor (2 points)
**Answer: B**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);
//              ^^^ using new keyword
//                  ^^^^^^^ calling constructor
```

**Constructor Characteristics:**
1. Name is same as class name
2. Used to initialize objects
3. Called with new keyword
4. No return type (not even void)

**Constructor Examples:**
```java
// Scanner has multiple constructors (Overloading)
Scanner s1 = new Scanner(System.in);      // read from keyboard
Scanner s2 = new Scanner("Hello World");  // read from string
Scanner s3 = new Scanner(new File("data.txt")); // read from file
```

---

### 10. Scanner and Reference Types (2 points)
**Answer: C**

**Detailed Explanation:**
```java
Scanner input = null;          // ✓ Legal, input doesn't reference any object
input = new Scanner(System.in); // ✓ Now input references an object
```

**The Concept of null:**
```java
// null means "references no object"
Scanner s1 = null;  // s1 exists but points to no object
// s1.nextInt();    // Error! NullPointerException

s1 = new Scanner(System.in);  // Now can be used
int num = s1.nextInt();       // ✓ Correct
```

**Usage Scenarios:**
```java
Scanner input = null;
if (useKeyboard) {
    input = new Scanner(System.in);
} else {
    input = new Scanner(new File("input.txt"));
}
// Decide Scanner source based on condition
```

---

## Part II: Scanner Methods In-Depth Application (30 points)

### 11. nextInt() vs next() (3 points)
**Answer: B**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);
// User input: 42 Hello
int num = input.nextInt();    // reads 42
String word = input.next();   // reads Hello
System.out.println(num + " " + word);
// Output: 42 Hello
```

**Execution Process:**
```
Input buffer: [42 Hello\n]
               ↑
nextInt() reads 42, stops at space
Input buffer: [42 Hello\n]
                  ↑
next() reads Hello
Input buffer: [42 Hello\n]
                       ↑
```

---

### 12. nextLine() Newline Issue I (3 points)
**Answer: B**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter a number:");
int age = input.nextInt();        // reads 25, leaves \n
System.out.println("Enter your name:");
String name = input.nextLine();   // reads empty string!
System.out.println("Name: " + name);
// Output: Name: 
```

**Problem Analysis:**
```
User input: 25[Enter]
Input buffer: [25\n]
               ↑
nextInt() only reads number 25
Input buffer: [25\n]
                 ↑
nextLine() reads to newline and stops
Result: name = "" (empty string)
```

**This is the most common Scanner trap!**

---

### 13. Fixing the nextLine() Problem (3 points)
**Answer: B**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter a number:");
int age = input.nextInt();
input.nextLine();  // ✓ Clear the newline character
System.out.println("Enter your name:");
String name = input.nextLine();  // Now reads correctly
```

**Correct Patterns:**
```java
// Pattern 1: nextInt() + nextLine()
int age = input.nextInt();
input.nextLine();  // clear buffer
String name = input.nextLine();

// Pattern 2: All nextLine() + parseInt()
String ageStr = input.nextLine();
int age = Integer.parseInt(ageStr);
String name = input.nextLine();

// Pattern 3: Use next() instead of nextLine()
int age = input.nextInt();
String name = input.next();  // Only reads one word (no spaces)
```

---

### 14. hasNext() Method (3 points)
**Answer: C**

**Detailed Explanation:**
```java
Scanner input = new Scanner("10 20 30");
int sum = 0;
while (input.hasNextInt()) {  // Check if more integers exist
    sum += input.nextInt();   // Read and accumulate
}
System.out.println(sum);  // Output: 60
```

**Execution Flow:**
```
Loop 1:
  hasNextInt() → true (has 10)
  sum = 0 + 10 = 10

Loop 2:
  hasNextInt() → true (has 20)
  sum = 10 + 20 = 30

Loop 3:
  hasNextInt() → true (has 30)
  sum = 30 + 30 = 60

Loop 4:
  hasNextInt() → false (no more integers)
  exit loop

Final: sum = 60
```

**hasNext Series Methods:**
```java
Scanner input = new Scanner("10 3.14 true Hello");

input.hasNextInt()     // true
input.hasNextDouble()  // true (int can also be double)
input.hasNextBoolean() // false
input.hasNext()        // true (has any token)
```

---

### 15. Scanner String Delimiter (3 points)
**Answer: C**

**Detailed Explanation:**
```java
Scanner input = new Scanner("apple,banana,cherry");
input.useDelimiter(",");  // Set comma as delimiter
while (input.hasNext()) {
    System.out.println(input.next());
}
```

**Output:**
```
apple
banana
cherry
```

**useDelimiter() Explanation:**
```java
// Default delimiter is whitespace and newline
Scanner s1 = new Scanner("a b c");
// s1.next() reads in order: a, b, c

// Custom delimiter
Scanner s2 = new Scanner("a:b:c");
s2.useDelimiter(":");
// s2.next() reads in order: a, b, c

// Multiple delimiters (using regex)
Scanner s3 = new Scanner("a,b;c:d");
s3.useDelimiter("[,:;]");
// s3.next() reads in order: a, b, c, d
```

---

### 16. nextDouble() Precision (3 points)
**Answer: C**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter a decimal:");
double value = input.nextDouble();  // reads 3.14159
System.out.println("Value: " + value);
// Output: Value: 3.14159
```

**Important Concepts:**
- double type can accurately store the input value
- Java's double is 64-bit (IEEE 754 standard)
- About 15-17 significant digits

**Precision Testing:**
```java
double d1 = 3.14159;
double d2 = 3.141592653589793;
double d3 = 3.14159265358979323846;  // exceeds precision

System.out.println(d1);  // 3.14159
System.out.println(d2);  // 3.141592653589793
System.out.println(d3);  // 3.141592653589793 (truncated)
```

---

### 17. Scanner and Type Conversion (3 points)
**Answer: B**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);
// User input: 100
String text = input.next();            // text = "100"
int number = Integer.parseInt(text);   // number = 100
System.out.println(number * 2);        // 100 * 2 = 200
```

**String to Number Conversion Methods:**
```java
// String → int
String s1 = "123";
int i = Integer.parseInt(s1);

// String → double
String s2 = "3.14";
double d = Double.parseDouble(s2);

// String → boolean
String s3 = "true";
boolean b = Boolean.parseBoolean(s3);

// String → long
String s4 = "999999999";
long l = Long.parseLong(s4);
```

**Error Handling:**
```java
try {
    int num = Integer.parseInt("abc");
} catch (NumberFormatException e) {
    System.out.println("Invalid number format!");
}
```

---

### 18. Scanner Exception Handling (3 points)
**Answer: C**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter a number:");
int num = input.nextInt();  // if input is "abc"
// Throws: InputMismatchException
```

**Common Scanner Exceptions:**

**1. InputMismatchException**
```java
Scanner input = new Scanner(System.in);
int num = input.nextInt();
// Input "abc" → InputMismatchException
```

**2. NoSuchElementException**
```java
Scanner input = new Scanner("");
int num = input.nextInt();
// No input → NoSuchElementException
```

**3. IllegalStateException**
```java
Scanner input = new Scanner(System.in);
input.close();
int num = input.nextInt();
// Scanner already closed → IllegalStateException
```

**Proper Exception Handling:**
```java
Scanner input = new Scanner(System.in);
try {
    System.out.println("Enter a number:");
    int num = input.nextInt();
    System.out.println("You entered: " + num);
} catch (InputMismatchException e) {
    System.out.println("Error: Please enter a valid integer!");
    input.nextLine();  // clear bad input
}
```

---

### 19. Scanner Multiple Parameter Reading (3 points)
**Answer: A**

**Detailed Explanation:**
```java
Scanner input = new Scanner(System.in);
// User input: 5 3.14 Hello
int a = input.nextInt();       // a = 5
double b = input.nextDouble(); // b = 3.14
String c = input.next();       // c = "Hello"
System.out.println(a + " " + b + " " + c);
// Output: 5 3.14 Hello
```

**Reading Process:**
```
Input buffer: [5 3.14 Hello]
               ↑
nextInt() reads 5

Input buffer: [5 3.14 Hello]
                 ↑
nextDouble() reads 3.14

Input buffer: [5 3.14 Hello]
                      ↑
next() reads Hello

Result: a=5, b=3.14, c="Hello"
Output: 5 3.14 Hello
```

**Note String Concatenation:**
```java
// + is concatenation operator in strings
System.out.println(a + " " + b + " " + c);
// Equivalent to:
System.out.println("5" + " " + "3.14" + " " + "Hello");
// Result: "5 3.14 Hello"
```

---

### 20. Scanner and Boolean Values (3 points)
**Answer: A**

**Detailed Explanation:**
```java
Scanner input = new Scanner("true false TRUE");
boolean b1 = input.nextBoolean();  // b1 = true
boolean b2 = input.nextBoolean();  // b2 = false
boolean b3 = input.nextBoolean();  // b3 = true
System.out.println(b1 + " " + b2 + " " + b3);
// Output: true false true
```

**nextBoolean() Characteristics:**
1. **Case-insensitive**: true, True, TRUE, TrUe are all recognized as true
2. **Only accepts true or false**: other inputs throw InputMismatchException
3. **Output is always lowercase**: true or false

**Test Examples:**
```java
Scanner s1 = new Scanner("true");
System.out.println(s1.nextBoolean());  // true

Scanner s2 = new Scanner("TRUE");
System.out.println(s2.nextBoolean());  // true

Scanner s3 = new Scanner("False");
System.out.println(s3.nextBoolean());  // false

Scanner s4 = new Scanner("yes");
// s4.nextBoolean();  // InputMismatchException!
```

**Boolean Output:**
```java
boolean b = true;
System.out.println(b);        // true
System.out.println(!b);       // false
System.out.println(b + b);    // Compile error! booleans can't be added
System.out.println("" + b);   // "true" (string concatenation)
```

---

## Scanner Best Practices Summary

### 1. Basic Usage Template
```java
import java.util.Scanner;

public class Example {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // Use Scanner...
        
        input.close();  // Remember to close
    }
}
```

### 2. Avoid nextLine() Trap
```java
// ✗ Wrong
int age = input.nextInt();
String name = input.nextLine();  // reads empty string

// ✓ Correct
int age = input.nextInt();
input.nextLine();  // clear newline character
String name = input.nextLine();
```

### 3. Exception Handling
```java
try {
    int num = input.nextInt();
} catch (InputMismatchException e) {
    System.out.println("Invalid input!");
    input.nextLine();  // clear bad input
}
```

### 4. Input Validation
```java
if (input.hasNextInt()) {
    int num = input.nextInt();
} else {
    System.out.println("Not a valid integer!");
    input.next();  // skip invalid input
}
```

---

## Grading Rubric

### Multiple Choice Questions
- Points for correct answer
- No deduction for wrong answers
- No points for unanswered

### Programming Questions Grading Criteria
1. **Program Correctness (60%)**
   - Correctly implements functional requirements
   - Output format is correct

2. **Code Quality (20%)**
   - Clear variable naming
   - Readable code

3. **Scanner Usage (20%)**
   - Correct use of Scanner methods
   - Proper input handling
   - Remember to close resources

---

**Assessment Complete!**
**Total Score: 100 points**
**Passing Score: 60 points**
