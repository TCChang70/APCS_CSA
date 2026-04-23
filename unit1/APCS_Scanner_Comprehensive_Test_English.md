# APCS CSA Scanner In-Depth Assessment

## Part I: Scanner Fundamentals (20 points)

### 1. Scanner Class Basics (2 points)
```java
Scanner scanner = new Scanner(System.in);

Which statement about the above code is correct?
(A) Scanner is a primitive data type
(B) System.in represents the standard input stream
(C) scanner is a class name
(D) The new keyword is used to call a method
```

---

### 2. Scanner Method Selection (2 points)
```
Which method should be used to read an integer input from the user?
(A) scanner.next()
(B) scanner.nextLine()
(C) scanner.nextInt()
(D) scanner.read()
```

---

### 3. Scanner Import Statement (2 points)
```java
// Line 1
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
    }
}

What statement should be added at Line 1 for the code to compile correctly?
(A) include java.util.Scanner;
(B) import java.util.Scanner;
(C) using java.util.Scanner;
(D) package java.util.Scanner;
```
---

### 4. Scanner Resource Management (2 points)
```java
Scanner input = new Scanner(System.in);
int num = input.nextInt();
// Program continues...

Regarding best practices for Scanner objects, which statement is correct?
(A) Scanner objects close automatically, no manual handling needed
(B) You should call input.close() after use
(C) Scanner can only be used once before becoming invalid
(D) No need to close Scanner since it doesn't use resources
```
---

### 5. Scanner Objects and Variables (2 points)
```java
Scanner sc1 = new Scanner(System.in);
Scanner sc2 = sc1;
sc1.close();

After sc1.close() executes, which statement is correct?
(A) sc2 can still be used normally
(B) sc2 is also closed because sc1 and sc2 reference the same object
(C) This will cause a compilation error
(D) sc2 will automatically point to a new Scanner object
```
---

### 6. Scanner Method Return Types (2 points)
```
Which Scanner method has a return type of String?
(A) nextInt()
(B) nextDouble()
(C) hasNext()
(D) nextLine()
```
---

### 7. Scanner Method Characteristics (2 points)
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter a number: ");
int x = input.nextInt();
System.out.println("You entered: " + x);

Regarding the nextInt() method, which statement is correct?
(A) nextInt() is a void method
(B) nextInt() reads the entire line including the newline character
(C) nextInt() is a non-void method that returns an int value
(D) nextInt() can read decimal numbers
```

---

### 8. Scanner Class Properties (2 points)
```
Scanner class belongs to which type of class?
(A) Primitive Class
(B) Wrapper Class
(C) Reference Class
(D) Static Class
```

---

### 9. Scanner Constructor (2 points)
```java
Scanner input = new Scanner(System.in);

In this line of code, new Scanner(System.in) calls a:
(A) method
(B) constructor
(C) function
(D) variable
```

---

### 10. Scanner and Reference Types (2 points)
```java
Scanner input = null;
input = new Scanner(System.in);

Regarding the above code, which statement is correct?
(A) The first line will cause a compilation error
(B) null can only be used with primitive types
(C) input initially doesn't reference any object
(D) The second line will cause a runtime error
```

---

## Part II: Scanner Methods In-Depth Application (30 points)

### 11. nextInt() vs next() (3 points)
```java
Scanner input = new Scanner(System.in);
// User input: 42 Hello
int num = input.nextInt();
String word = input.next();
System.out.println(num + " " + word);

What is the output?
(A) 42Hello
(B) 42 Hello
(C) Compilation error
(D) Runtime error
```
---

### 12. nextLine() Newline Issue I (3 points)
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter a number:");
int age = input.nextInt();
System.out.println("Enter your name:");
String name = input.nextLine();
System.out.println("Name: " + name);

If the user enters:

25
John

What will the value of name be?
(A) "John"
(B) "" (empty string)
(C) "25"
(D) null
```

**Explanation: nextInt() doesn't consume the newline character, so nextLine() reads an empty line**

---

### 13. Fixing the nextLine() Problem (3 points)
To fix the problem in the previous question, what should be added?
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter a number:");
int age = input.nextInt();
// What should be added here?
System.out.println("Enter your name:");
String name = input.nextLine();

(A) input.next();
(B) input.nextLine();
(C) input.skip();
(D) input.clear();
```

---

### 14. hasNext() Method (3 points)
```java
Scanner input = new Scanner("10 20 30");
int sum = 0;
while (input.hasNextInt()) {
    sum += input.nextInt();
}
System.out.println(sum);

What is the output?
(A) 10
(B) 30
(C) 60
(D) Compilation error
```
---

### 15. Scanner String Delimiter (3 points)
```java
Scanner input = new Scanner("apple,banana,cherry");
input.useDelimiter(",");
while (input.hasNext()) {
    System.out.println(input.next());
}

How many lines will this code output?
(A) 1 line
(B) 2 lines
(C) 3 lines
(D) Compilation error
```
---

### 16. nextDouble() Precision (3 points)
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter a decimal:");
double value = input.nextDouble();
System.out.println("Value: " + value);

If the user enters "3.14159", what will be output?
(A) Value: 3
(B) Value: 3.14
(C) Value: 3.14159
(D) Runtime error
```
---

### 17. Scanner and Type Conversion (3 points)
```java
Scanner input = new Scanner(System.in);
// User input: 100
String text = input.next();
int number = Integer.parseInt(text);
System.out.println(number * 2);

What is the output?
(A) 100100
(B) 200
(C) Compilation error
(D) Runtime error
```

---

### 18. Scanner Exception Handling (3 points)
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter a number:");
int num = input.nextInt();

What happens if the user enters "abc"?
(A) num will be 0
(B) num will be -1
(C) Throws InputMismatchException
(D) Compilation error
```

---

### 19. Scanner Multiple Parameter Reading (3 points)
```java
Scanner input = new Scanner(System.in);
// User input: 5 3.14 Hello
int a = input.nextInt();
double b = input.nextDouble();
String c = input.next();
System.out.println(a + " " + b + " " + c);

What is the output?
(A) 5 3.14 Hello
(B) 8.14 Hello
(C) Compilation error
(D) Runtime error
```

---

### 20. Scanner and Boolean Values (3 points)
```java
Scanner input = new Scanner("true false TRUE");
boolean b1 = input.nextBoolean();
boolean b2 = input.nextBoolean();
boolean b3 = input.nextBoolean();
System.out.println(b1 + " " + b2 + " " + b3);

What is the output?
(A) true false true
(B) true false TRUE
(C) 1 0 1
(D) Compilation error
```

**Explanation: nextBoolean() is case-insensitive**

---

## Part III: Scanner Integration with Control Structures (25 points)

### 21. Scanner with if Statement (5 points)
Complete the following program to determine if a user can vote based on their age (18 or older):
```java
import java.util.Scanner;

public class VotingAge {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your age:");
        // Complete the code here
        
    }
}
```

**Reference Answer:**
```java
int age = input.nextInt();
if (age >= 18) {
    System.out.println("You can vote!");
} else {
    System.out.println("You cannot vote yet.");
}
input.close();
```

---

### 22. Scanner Data Validation (5 points)
Write a program that asks the user to enter a number between 1-100, and displays an error message if the input is out of range:
```java
import java.util.Scanner;

public class NumberValidation {
    public static void main(String[] args) {
        // Complete the code
      
        
    }
}
```

**Reference Answer:**
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter a number between 1 and 100:");
int num = input.nextInt();
if (num >= 1 && num <= 100) {
    System.out.println("Valid number: " + num);
} else {
    System.out.println("Error: Number out of range!");
}
input.close();
```

---

### 23. Scanner with else if (5 points)
Complete the grade level program (A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: <60):
```java
import java.util.Scanner;

public class GradeLevel {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your score:");
        // Complete the code
        
        
    }
}
```

**Reference Answer:**
```java
int score = input.nextInt();
if (score >= 90 && score <= 100) {
    System.out.println("Grade: A");
} else if (score >= 80) {
    System.out.println("Grade: B");
} else if (score >= 70) {
    System.out.println("Grade: C");
} else if (score >= 60) {
    System.out.println("Grade: D");
} else {
    System.out.println("Grade: F");
}
input.close();
```

---

### 24. Scanner with Compound Boolean Expressions (5 points)
Write a program to determine amusement park ticket prices:
- Under 13: $10
- 13-64: $20
- 65 and over: $15
```java
import java.util.Scanner;

public class TicketPrice {
    public static void main(String[] args) {
        // Complete the code
        
        
    }
}
```

**Reference Answer:**
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter your age:");
int age = input.nextInt();
if (age < 13) {
    System.out.println("Ticket price: $10");
} else if (age >= 13 && age <= 64) {
    System.out.println("Ticket price: $20");
} else {
    System.out.println("Ticket price: $15");
}
input.close();
```

---

### 25. Scanner String Comparison (5 points)
Complete a program that asks the user to enter a password. The password is "Java2024" (case-sensitive):
```java
import java.util.Scanner;

public class PasswordCheck {
    public static void main(String[] args) {
        // Complete the code
        
        
    }
}
```

**Reference Answer:**
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter password:");
String password = input.nextLine();
String correctPassword = "Java2024";
if (password.equals(correctPassword)) {
    System.out.println("Access granted!");
} else {
    System.out.println("Access denied!");
}
input.close();
```

---

## Part IV: Scanner Advanced Applications (25 points)

### 26. Calculator Program (5 points)
Complete a simple calculator that reads two numbers and an operator (+, -, *, /):
```java
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter first number:");
        // Complete the code
        
    }
}
```

**Reference Answer:**
```java
double num1 = input.nextDouble();
System.out.println("Enter operator (+, -, *, /):");
String operator = input.next();
System.out.println("Enter second number:");
double num2 = input.nextDouble();

if (operator.equals("+")) {
    System.out.println("Result: " + (num1 + num2));
} else if (operator.equals("-")) {
    System.out.println("Result: " + (num1 - num2));
} else if (operator.equals("*")) {
    System.out.println("Result: " + (num1 * num2));
} else if (operator.equals("/")) {
    System.out.println("Result: " + (num1 / num2));
} else {
    System.out.println("Invalid operator!");
}
input.close();
```

---

### 27. BMI Calculator Program (5 points)
Write a program to calculate BMI (Body Mass Index):
- BMI = weight (kg) / (height (m))²
- BMI < 18.5: Underweight
- 18.5 <= BMI < 25: Normal
- 25 <= BMI < 30: Overweight
- BMI >= 30: Obese

```java
import java.util.Scanner;

public class BMICalculator {
    public static void main(String[] args) {
        // Complete the code
       
        
    }
}
```

**Reference Answer:**
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter your weight in kg:");
double weight = input.nextDouble();
System.out.println("Enter your height in meters:");
double height = input.nextDouble();

double bmi = weight / (height * height);
System.out.println("Your BMI: " + bmi);

if (bmi < 18.5) {
    System.out.println("Category: Underweight");
} else if (bmi < 25) {
    System.out.println("Category: Normal");
} else if (bmi < 30) {
    System.out.println("Category: Overweight");
} else {
    System.out.println("Category: Obese");
}
input.close();
```

---

### 28. Temperature Conversion Program (5 points)
Complete a temperature conversion program that lets the user choose the conversion direction:
- C to F: F = C * 9/5 + 32
- F to C: C = (F - 32) * 5/9

```java
import java.util.Scanner;

public class TemperatureConverter {
    public static void main(String[] args) {
        // Complete the code
        
        
        
    }
}
```

**Reference Answer:**
```java
Scanner input = new Scanner(System.in);
System.out.println("Choose conversion:");
System.out.println("1. Celsius to Fahrenheit");
System.out.println("2. Fahrenheit to Celsius");
int choice = input.nextInt();

if (choice == 1) {
    System.out.println("Enter temperature in Celsius:");
    double celsius = input.nextDouble();
    double fahrenheit = celsius * 9.0 / 5.0 + 32;
    System.out.println(celsius + "°C = " + fahrenheit + "°F");
} else if (choice == 2) {
    System.out.println("Enter temperature in Fahrenheit:");
    double fahrenheit = input.nextDouble();
    double celsius = (fahrenheit - 32) * 5.0 / 9.0;
    System.out.println(fahrenheit + "°F = " + celsius + "°C");
} else {
    System.out.println("Invalid choice!");
}
input.close();
```

---

### 29. Multi-line Input Processing (5 points)
Write a program that reads three lines of user input (name, city, country), then outputs them in a formatted manner:
```java
import java.util.Scanner;

public class UserProfile {
    public static void main(String[] args) {
        // Complete the code
        
    }
}
```

**Reference Answer:**
```java
Scanner input = new Scanner(System.in);
System.out.println("Enter your name:");
String name = input.nextLine();
System.out.println("Enter your city:");
String city = input.nextLine();
System.out.println("Enter your country:");
String country = input.nextLine();

System.out.println("\n=== User Profile ===");
System.out.println("Name: " + name);
System.out.println("City: " + city);
System.out.println("Country: " + country);
input.close();
```

---

### 30. Scanner Comprehensive Application - Restaurant Order System (5 points)
Complete a simple restaurant ordering system:
- Burger: $5.99
- Pizza: $8.99
- Salad: $4.99
- Drink: $1.99
Calculate the total and ask if they want to add a tip (15% or 20%)

```java
import java.util.Scanner;

public class RestaurantOrder {
    public static void main(String[] args) {
        // Complete the code
        
        
    }
}
```

**Reference Answer:**
```java
Scanner input = new Scanner(System.in);
double total = 0;

System.out.println("=== Menu ===");
System.out.println("1. Burger ($5.99)");
System.out.println("2. Pizza ($8.99)");
System.out.println("3. Salad ($4.99)");
System.out.println("4. Drink ($1.99)");

System.out.println("\nHow many burgers?");
int burgers = input.nextInt();
total += burgers * 5.99;

System.out.println("How many pizzas?");
int pizzas = input.nextInt();
total += pizzas * 8.99;

System.out.println("How many salads?");
int salads = input.nextInt();
total += salads * 4.99;

System.out.println("How many drinks?");
int drinks = input.nextInt();
total += drinks * 1.99;

System.out.println("\nSubtotal: $" + total);
System.out.println("Add tip? (15 or 20 for percent, 0 for no tip):");
int tipPercent = input.nextInt();

double tip = total * tipPercent / 100.0;
double finalTotal = total + tip;

System.out.println("Tip: $" + tip);
System.out.println("Total: $" + finalTotal);
input.close();
```

---

## Appendix: Scanner Common Methods Summary

### Input Methods
- `nextInt()` - Read an integer
- `nextDouble()` - Read a double
- `nextBoolean()` - Read a boolean
- `next()` - Read the next string (space-delimited)
- `nextLine()` - Read the entire line
- `nextByte()` - Read a byte
- `nextShort()` - Read a short
- `nextLong()` - Read a long
- `nextFloat()` - Read a float

### Checking Methods
- `hasNext()` - Check if there's more input
- `hasNextInt()` - Check if next is an integer
- `hasNextDouble()` - Check if next is a double
- `hasNextBoolean()` - Check if next is a boolean
- `hasNextLine()` - Check if there's another line

### Other Common Methods
- `useDelimiter(String pattern)` - Set delimiter
- `close()` - Close the Scanner
- `reset()` - Reset the Scanner

---

## Scanner Usage Important Notes

1. **Remember to import**: `import java.util.Scanner;`
2. **Create object**: `Scanner input = new Scanner(System.in);`
3. **nextInt() with nextLine() issue**: nextInt() doesn't consume newline, need extra nextLine() to clear
4. **Close resources**: Call `input.close()` after use
5. **Exception handling**: Type mismatch throws InputMismatchException
6. **String comparison**: Use `.equals()` not `==`
7. **Whitespace handling**: next() stops at whitespace, nextLine() reads entire line

---

