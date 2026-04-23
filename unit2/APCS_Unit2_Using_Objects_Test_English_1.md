# 📝 AP Computer Science A - Using Objects Unit Test

## 🎯 Test Information
- **Test Coverage**: Unit 2 - Using Objects
- **Test Duration**: 90 minutes
- **Total Points**: 100 points
- **Test Content**: Classes and Objects, String Operations, Math Class, Method Invocation
- **Instructions**: This test is designed according to AP CSA standards. Please read each question carefully.

---

## 📚 Part I: Multiple Choice Questions - 45 points

### **Questions 1-9: Object-Oriented Fundamentals (2.5 points each, 22.5 points total)**

**1.** Which of the following statements about classes and objects in Java is correct?
- A) A class is an instance of an object
- B) An object is an instance of a class
- C) Classes and objects are the same concept
- D) A class can only create one object

**2.** Which of the following is the correct syntax for creating an object?
- A) `String name = String();`
- B) `String name = new String("John");`
- C) `String name = create String("John");`
- D) `String name = String.new("John");`

**3.** In Java, which symbol is used to call a method on an object?
- A) Colon (:)
- B) Double colon (::)
- C) Dot (.)
- D) Arrow (->)

**4.** Regarding method parameters and arguments, which statement is correct?
- A) Parameters and arguments are exactly the same concept
- B) Parameters are variables in method definitions, arguments are values passed during invocation
- C) Arguments are variables in method definitions, parameters are values passed during invocation
- D) Java does not distinguish between parameters and arguments

**5.** Which of the following is a Java wrapper class?
- A) `int`
- B) `Integer`
- C) `string`
- D) `boolean`

**6.** Regarding method return values, which statement is correct?
- A) All methods must have a return value
- B) void methods can use return statements to return values
- C) Non-void methods must return a value of the corresponding type
- D) Methods can only return primitive data types

**7.** In Java, which method should be used for string comparison?
- A) `==` operator
- B) `.equals()` method
- C) `.compare()` method
- D) `.same()` method

**8.** Which Math class method is used to calculate absolute value?
- A) `Math.absolute()`
- B) `Math.abs()`
- C) `Math.positive()`
- D) `Math.value()`

**9.** Regarding Java autoboxing, which statement is correct?
- A) Automatically converts objects to primitive types
- B) Automatically converts primitive types to their corresponding wrapper classes
- C) Automatically creates new objects
- D) Automatically deletes unnecessary objects

### **Questions 10-18: Code Analysis (2.5 points each, 22.5 points total)**

**10.** What is the output after executing the following code?
```java
String str = "Hello";
System.out.println(str.length());
```
- A) Hello
- B) 5
- C) 4
- D) Compilation error

**11.** What is the result of executing the following code?
```java
String s1 = "Java";
String s2 = "Java";
System.out.println(s1 == s2);
```
- A) true
- B) false
- C) Java
- D) Compilation error

**12.** What is the output of executing the following code?
```java
String text = "Programming";
System.out.println(text.substring(3, 7));
```
- A) Prog
- B) gram
- C) Programming
- D) ramm

**13.** What is the output of the following code?
```java
int x = (int)(Math.random() * 10);
```
What is the range of possible values for x?
- A) 0 to 9
- B) 1 to 10
- C) 0 to 10
- D) 1 to 9

**14.** What is the result of executing the following code?
```java
String str = "COMPUTER";
System.out.println(str.toLowerCase().charAt(0));
```
- A) C
- B) c
- C) COMPUTER
- D) computer

**15.** Which of the following will cause a compilation error?
```java
Integer num1 = 10;
int num2 = num1;
double num3 = num1;
String num4 = num1;
```
- A) Line 1
- B) Line 2
- C) Line 3
- D) Line 4

**16.** What is the output of the following code?
```java
String s = "Hello";
s.concat(" World");
System.out.println(s);
```
- A) Hello
- B) Hello World
- C) World
- D) Compilation error

**17.** What is the result of executing the following code?
```java
double result = Math.pow(2, 3);
System.out.println(result);
```
- A) 6.0
- B) 8.0
- C) 9.0
- D) 2.3

**18.** What is the output of the following code?
```java
String text = "Java Programming";
int index = text.indexOf("Pro");
System.out.println(index);
```
- A) -1
- B) 4
- C) 5
- D) 0

---

## 💻 Part II: Free Response Questions (FRQs) - 40 points

### **Question 19: String Processing Application (15 points)**

Write a Java program that analyzes text input by the user and provides various statistics and format transformations.

**Requirements:**
- Read a text string from user input
- Calculate and display the following statistics:
  1. Total length (including spaces)
  2. Length without spaces
  3. Number of uppercase letters
  4. Number of lowercase letters
  5. Number of digit characters
  6. Number of special characters
- Provide format transformations:
  1. All uppercase
  2. All lowercase
  3. Title case (first letter of each word capitalized)

**Program Structure:**
```java
import java.util.Scanner;

public class TextAnalyzer {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Write your code here
        
        scanner.close();
    }
}
```

**Expected Output Example:**
```
Enter text to analyze: Hello World 123!

=== Text Analysis Results ===
Total length (with spaces): 17
Length (without spaces): 15
Uppercase letters: 2
Lowercase letters: 8
Digit characters: 3
Special characters: 2

=== Format Transformations ===
All uppercase: HELLO WORLD 123!
All lowercase: hello world 123!
Title case: Hello World 123!
```

**Grading Rubric:**
- Correctly reading input and calculating statistics (8 points)
- Character classification logic is correct (4 points)
- Format transformation features complete (3 points)

### **Question 20: Math Class Application (12 points)**

Write a mathematical calculator program that provides various mathematical operations.

**Requirements:**
- Read two numeric values (double)
- Provide the following calculation features:
  1. Basic operations: addition, subtraction, multiplication, division
  2. Advanced operations: power, square root, absolute value
  3. Trigonometric functions: sine, cosine, tangent (angle input in degrees)
  4. Logarithmic operations: natural logarithm, common logarithm
- Use a menu system to let users select operation type
- Properly handle special cases such as division by zero and square root of negative numbers

**Program Structure:**
```java
import java.util.Scanner;

public class MathCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Write your code here
        
        scanner.close();
    }
}
```

**Expected Output Example:**
```
=== Math Calculator ===
Enter first number: 5.0
Enter second number: 3.0

Select operation type:
1. Basic Operations    2. Advanced Operations
3. Trigonometric       4. Logarithmic
Your choice: 2

Advanced Operations:
1. Power (a^b)    2. Square Root
3. Absolute Value 4. Return to Main Menu
Your choice: 1

Result: 5.0^3.0 = 125.0
```

**Grading Rubric:**
- Menu system design (3 points)
- Correct use of Math class methods (6 points)
- Special case handling (3 points)

### **Question 21: Object-Oriented Design (13 points)**

Design a simple student information management system using existing classes to create and manipulate student objects.

**Requirements:**
- Create a Student class with the following properties:
  - Student ID (String)
  - Name (String)
  - Age (int)
  - Score (double)
- Provide the following methods:
  - Constructor (initialize all properties)
  - Getter and setter methods
  - toString() method (formatted output of student information)
  - Grade level determination method getGradeLevel()
- In the main program, create multiple student objects and demonstrate various operations

**Grade Level Standards:**
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- 0-59: F

**Program Structure:**
```java
public class Student {
    // Define properties and methods here
}

public class StudentManager {
    public static void main(String[] args) {
        // Write main program logic here
    }
}
```

**Expected Output Example:**
```
=== Student Information Management System ===

Student 1 Information:
Student ID: S001
Name: John Smith
Age: 20
Score: 85.5
Grade: B

Student 2 Information:
Student ID: S002
Name: Emily Chen
Age: 19
Score: 92.0
Grade: A

Updating Student 1 score to 95.0
Updated Student 1 Information:
Student ID: S001
Name: John Smith
Age: 20
Score: 95.0
Grade: A
```

**Grading Rubric:**
- Correct class design (5 points)
- Complete method implementation (5 points)
- Object manipulation demonstration (3 points)

---








