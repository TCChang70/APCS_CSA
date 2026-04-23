# 📚 AP Computer Science A - Unit 1 Practice Test
## Primitive Types and Variables

**Test Instructions:**
- Total Points: 100
- Time Limit: 90 minutes
- Multiple Choice: 50 points (25 questions, 2 points each)
- Free Response: 50 points (3 questions)
- Calculator: Not permitted
- Reference materials: None

---

## 📝 Section I: Multiple Choice Questions (50 points)
*Choose the best answer for each question. Mark your answer clearly.*

### **Questions 1-8: Java Fundamentals**

**1. Which of the following best describes the Java compilation and execution process?**
 ```  
   A) Java source code is directly interpreted by the operating system
   B) Java source code (.java) is compiled to bytecode (.class) and executed by the JVM
   C) Java programs are compiled to machine code specific to each processor
   D) Java uses only interpretation without any compilation step
   E) Java source code is converted to assembly language first
``` 
**2. What is the correct signature for the main method in a Java application?**
``` 
   A) public void main(String[] args)
   B) static void main(String args[])
   C) public static void main(String[] args)
   D) public static main(String[] args)
   E) public static void Main(String[] args)
```  

**3. Which of the following are valid Java comment styles?**
```     
   I.   `// Single line comment`
   II.  `/* Multi-line comment */`
   III. `/** Documentation comment */`
    
   A) I only
   B) II only  
   C) I and II only
   D) I and III only
   E) I, II, and III
```  

**4. Which of the following is NOT a Java reserved word?**
 ``` 
   A) public
   B) static
   C) main
   D) class
   E) void
```
**5. Which identifier is invalid in Java?**
``` 
   A) myVariable
   B) _count
   C) $amount
   D) my-variable
   E) value123
```
**6. Java is considered a hybrid language because:**
 ``` 
   A) It supports both procedural and object-oriented programming
   B) It can run on multiple operating systems
   C) It combines compilation to bytecode with JVM interpretation
   D) It supports both static and dynamic typing
   E) It includes features from C++ and Smalltalk
 ``` 
**7. Which statement correctly declares a package in Java?**
 ``` 
   A) import java.util.*
   B) package java.util
   C) using java.util
   D) include java.util
   E) namespace java.util
 ``` 
**8. What is the correct order for Java file structure?**
``` 
   A) import → package → class
   B) package → class → import
   C) class → package → import
   D) package → import → class
   E) import → class → package
``` 
### **Questions 9-16: Data Types and Variables**

**9. How much memory do the primitive types `byte` and `short` occupy respectively?**
``` 
   A) 1 byte, 1 byte
   B) 1 byte, 2 bytes
   C) 2 bytes, 2 bytes
   D) 1 byte, 4 bytes
   E) 2 bytes, 4 bytes
``` 
**10. Which variable declaration will cause a compilation error?**
``` 
   A) int number = 42;
   B) double value = 3.14f;
   C) char letter = 65;
   D) boolean flag = 1;
   E) float pi = 3.14f;
``` 
 
**11. What is true about the `char` data type in Java?**
``` 
   A) It can only store ASCII characters (0-127)
   B) It uses 8 bits to store character data
   C) It can store Unicode characters in the range 0 to 65535
   D) It cannot be used in arithmetic operations
   E) It must always be declared with single quotes
```  
**12. What is the result and data type of the expression `5 + 8.5f`?**
``` 
   A) 13, int type
   B) 13.0, double type
   C) 13.5, float type
   D) 13.5, double type
   E) Compilation error
``` 
**13. Which keyword is used to declare a constant in Java?**
```  
   A) const
   B) final
   C) static
   D) readonly
   E) constant
``` 
**14. Which literal representation is INVALID in Java?**
``` 
   A) int hex = 0xFF; (hexadecimal)
   B) int oct = 0777; (octal)
   C) int bin = 0b1010; (binary)
   D) int dec = 0d123; (decimal)
   E) long big = 1000L; (long)
```  
**15. What is true about variable scope in Java?**
``` 
   A) All variables are global by default
   B) Variables declared in a method can be used anywhere in the class
   C) Variables declared in a block can only be used within that block
   D) Local variables automatically become instance variables
   E) Variable scope is determined at runtime
``` 
**16. What happens when you try to declare a variable with the same name in nested blocks?**
``` 
   A) The inner variable overrides the outer variable
   B) Both variables coexist with different scopes
   C) Compilation error occurs
   D) The outer variable is automatically renamed
   E) A runtime warning is generated
``` 
### **Questions 17-25: Operators and Expressions**

**17. What is the value of the expression `true && false || true`?**
```  
   A) true
   B) false
   C) Compilation error
   D) Runtime error
   E) Cannot be determined
``` 
**18. What does the ternary operator `5 > 3 ? "greater" : "smaller"` evaluate to?**
``` 
   A) "greater"
   B) "smaller"
   C) true
   D) 5
   E) Compilation error
``` 
**19. Which operator has the highest precedence in Java?**
``` 
   A) `+` (addition)
   B) `*` (multiplication)
   C) `()` (parentheses)
   D) `=` (assignment)
   E) `&&` (logical AND)
``` 
**20. What is the result of the expression `15 % 4`?**
``` 
   A) 3
   B) 3.75
   C) 4
   D) 15
   E) 0
``` 
**21. Which of the following demonstrates short-circuit evaluation?**
``` 
   A) `false && (x/0 == 1)` will not cause an exception
   B) `true || (x/0 == 1)` will not cause an exception
   C) Both A and B
   D) Neither A nor B
   E) Only B causes an exception
``` 
**22. What is the value of `x` after executing: `int x = 10; x += x++ * 2;`?**
``` 
   A) 30
   B) 32
   C) 34
   D) 42
   E) Undefined behavior
``` 
**23. Which bitwise operation is equivalent to dividing by 2 for positive integers?**
```  
   A) x << 1
   B) x >> 1
   C) x & 1
   D) x | 1
   E) x ^ 1
``` 
**24. What is the result of `~0` (bitwise NOT of 0) in a 32-bit int?**
``` 
   A) 0
   B) 1
   C) -1
   D) 2147483647
   E) Compilation error
``` 
**25. Which expression correctly checks if a number is even?**
``` 
   A) number % 2 == 0
   B) (number & 1) == 0
   C) number / 2 * 2 == number
   D) All of the above
   E) A and B only
``` 
---

## 💻 Section II: Free Response Questions (50 points)

### **Question 1: Number Base Conversion System (15 points)**

Write a Java program that creates a comprehensive number base conversion system. Your program should:

**Requirements:**
1. Prompt the user to enter a decimal integer between 0 and 255
2. Convert and display the number in binary, octal, and hexadecimal formats
3. Display the ASCII character representation if applicable (printable range 32-126)
4. Show the memory representation in different primitive data types
5. Validate input and handle edge cases

**Expected Output Format:**
```
=== Number Base Conversion System ===
Enter a decimal number (0-255): 65

Conversion Results:
Decimal: 65
Binary: 01000001
Octal: 101
Hexadecimal: 41

ASCII Character: A (printable)

Memory Representation:
byte value: 65 (1 byte)
short value: 65 (2 bytes)
int value: 65 (4 bytes)
char value: A (2 bytes)

Range Analysis:
Within byte range (-128 to 127): Yes
Within printable ASCII range (32 to 126): Yes
```

**Grading Criteria:**
- Base conversion implementation (5 points)
- ASCII character handling (3 points)
- Memory representation display (3 points)
- Input validation and error handling (2 points)
- Code organization and documentation (2 points)

---

### **Question 2: Advanced Operator Calculator (20 points)**

Create a comprehensive calculator program that demonstrates the use of all Java operators. Your program should:

**Requirements:**
1. Accept two numeric inputs from the user
2. Perform all arithmetic operations (+, -, *, /, %)
3. Demonstrate comparison operators with boolean results
4. Show logical operations (treat non-zero as true)
5. For integer inputs, display bitwise operations with binary representation
6. Include examples of ternary operator usage
7. Demonstrate operator precedence with complex expressions

**Expected Functionality:**
```java
public class AdvancedCalculator {
    public static void main(String[] args) {
        // Your implementation here
        // Should include methods for:
        // - performArithmeticOperations()
        // - performComparisonOperations()
        // - performLogicalOperations()
        // - performBitwiseOperations()
        // - demonstrateTernaryOperators()
        // - demonstrateOperatorPrecedence()
    }
}
```

**Sample Output:**
```
=== Advanced Operator Calculator ===
Enter first number: 12
Enter second number: 5

Arithmetic Operations:
12 + 5 = 17
12 - 5 = 7
12 * 5 = 60
12 / 5 = 2.4 (floating-point)
12 / 5 = 2 (integer division)
12 % 5 = 2

Comparison Operations:
12 > 5: true
12 < 5: false
12 == 5: false
12 != 5: true

Bitwise Operations (Integer values):
12 & 5 = 4   (1100 & 0101 = 0100)
12 | 5 = 13  (1100 | 0101 = 1101)
12 ^ 5 = 9   (1100 ^ 0101 = 1001)  XOR  (exclusive or)
~12 = -13    (~1100 = ...11110011)

Ternary Operations:
Maximum: 12 > 5 ? 12 : 5 = 12
Minimum: 12 < 5 ? 12 : 5 = 5

Operator Precedence Example:
Expression: 12 + 5 * 2 - 3
Result: 19 (multiplication first: 12 + 10 - 3)
```

**Grading Criteria:**
- Arithmetic operations implementation (4 points)
- Comparison and logical operations (4 points)
- Bitwise operations with binary display (4 points)
- Ternary operator usage (3 points)
- Operator precedence demonstration (3 points)
- Code structure and error handling (2 points)

---

### **Question 3: Personal Data Management System (15 points)**

Design and implement a personal data management system that demonstrates proper use of variables, constants, and data validation.

**Requirements:**
1. Define appropriate constants for validation ranges and categories
2. Use all primitive data types appropriately
3. Implement data validation with meaningful error messages
4. Calculate BMI and provide health recommendations
5. Demonstrate variable scope and constant usage best practices

**Required Constants:**
```java
public static final int ADULT_AGE = 18;
public static final double BMI_UNDERWEIGHT = 18.5;
public static final double BMI_NORMAL = 24.9;
public static final double BMI_OVERWEIGHT = 29.9;
// Add other necessary constants
```

**Required Data Fields:**
- Name (String)
- Age (int) - validate range 1-120
- Height in meters (double) - validate range 0.5-3.0
- Weight in kg (float) - validate range 1.0-500.0
- Gender (char) - M/F
- Is student (boolean)

**Expected Output:**
```
=== Personal Data Management System ===
Enter your information:

Name: John Doe
Age: 25
Height (meters): 1.75
Weight (kg): 70.0
Gender (M/F): M
Are you a student (true/false): false

Data Analysis:
Name: John Doe
Age: 25 (Adult)
Height: 175.0 cm
Weight: 70.0 kg
Gender: Male
Student Status: No

Health Analysis:
BMI: 22.86
Status: Normal Range
Recommendation: Maintain your current healthy lifestyle

Data Validation Results:
✓ Age within valid range (1-120)
✓ Height within valid range (0.5-3.0 meters)
✓ Weight within valid range (1.0-500.0 kg)
✓ All data validated successfully

Constants Used:
- Adult age threshold: 18
- BMI categories: <18.5 (Underweight), 18.5-24.9 (Normal), 25.0-29.9 (Overweight), ≥30.0 (Obese)
```

**Grading Criteria:**
- Constant definitions and usage (3 points)
- Appropriate data type selection (3 points)
- BMI calculation and health analysis (3 points)
- Data validation implementation (3 points)
- Variable scope demonstration (2 points)
- Code organization and user experience (1 point)

---

## 🔍 Section III: Code Analysis and Debugging
*Note: These questions may appear in either section depending on the specific test format*

### **Variable Scope Analysis**

**Analyze the following code and predict the output. Identify any compilation errors:**

```java
public class ScopeDemo {
    static int globalVar = 100;
    
    public static void main(String[] args) {
        int localVar = 50;
        
        System.out.println("A: " + globalVar);
        System.out.println("B: " + localVar);
        
        {
            int blockVar = 25;
            localVar += blockVar;
            System.out.println("C: " + localVar);
            System.out.println("D: " + blockVar);
        }
        
        System.out.println("E: " + localVar);
        // System.out.println("F: " + blockVar); // What happens here?
        
        methodDemo();
    }
    
    public static void methodDemo() {
        int methodVar = globalVar - 25;
        System.out.println("G: " + (globalVar + methodVar));
        System.out.println("H: " + methodVar);
        // System.out.println("I: " + localVar); // What happens here?
    }
}
```

### **Type Conversion Debugging**

**Find and fix all compilation errors in the following code:**

```java
public class TypeConversionBug {
    public static void main(String[] args) {
        // Case 1: Numeric range issue
        byte smallNumber = 200; // Error?
        
        // Case 2: Precision loss
        int intValue = 123;
        float floatValue = 45.67f;
        int result1 = intValue + floatValue; // Error?
        
        // Case 3: Character conversion
        char letter = 'A';
        String word = letter + "BC"; // Error?
        
        // Case 4: Boolean conversion
        boolean flag = true;
        int boolToInt = flag; // Error?
        
        // Case 5: Division issue
        int a = 7, b = 3;
        double division = a / b; // Problem?
        
        // Case 6: Constant reassignment
        final double PI = 3.14;
        PI = 3.14159265; // Error?
        
        System.out.println("If this compiles, all errors are fixed!");
    }
}
```

---

## 📊 Answer Key and Scoring Guide

### **Multiple Choice Answer Key:**
1. B  2. C  3. E  4. C  5. D  6. C  7. B  8. D  
9. B  10. D  11. C  12. C  13. B  14. D  15. C  16. C  
17. A  18. A  19. C  20. A  21. C  22. B  23. B  24. C  25. E

### **Free Response Scoring Guidelines:**

**Question 1 (15 points):**
- Complete base conversion: 5 points
- ASCII handling: 3 points
- Memory representation: 3 points
- Validation: 2 points
- Code quality: 2 points

**Question 2 (20 points):**
- Arithmetic operations: 4 points
- Comparison/logical: 4 points
- Bitwise operations: 4 points
- Ternary operators: 3 points
- Precedence demo: 3 points
- Structure: 2 points

**Question 3 (15 points):**
- Constants: 3 points
- Data types: 3 points
- BMI calculation: 3 points
- Validation: 3 points
- Scope: 2 points
- Organization: 1 point

### **Grading Scale:**
- 90-100: Score 5
- 80-89: Score 4  
- 70-79: Score 3
- 60-69: Score 2
- Below 60: Score 1

---

## 📚 Study Resources

**Key Topics for Review:**
1. Java compilation and execution process
2. Primitive data types and memory allocation
3. Variable scope and lifetime
4. Operator precedence and associativity
5. Type conversion and casting rules
6. Constant declaration and usage
7. Bitwise operations and number systems
8. Expression evaluation and short-circuit logic

**Practice Recommendations:**
- Write programs using all primitive types
- Practice operator precedence with complex expressions
- Implement number base conversion algorithms
- Debug scope-related compilation errors
- Create validation systems with appropriate constants

**Common AP Exam Mistakes to Avoid:**
- Confusing operator precedence
- Incorrect variable scope understanding
- Type conversion errors
- Integer vs. floating-point division
- Bitwise vs. logical operators
- Constant reassignment attempts

---

*This practice test aligns with the College Board AP Computer Science A Course and Exam Description for Unit 1: Primitive Types.*