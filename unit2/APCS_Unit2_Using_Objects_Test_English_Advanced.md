# APCS Unit 2: Using Objects - Advanced Level Test (English Version)

**Instructions:**
- This exam consists of two sections: Multiple Choice (25 questions) and Free Response (4 questions)
- For multiple choice questions, select the best answer
- For free response questions, show all your work and write complete, compilable Java code
- Time limit: 90 minutes
- No calculators permitted

---

## Section I: Multiple Choice Questions (25 questions)

### Questions 1-25

**Question 1:** What is the output of the following code?
```java
String s1 = "Hello";
String s2 = "Hello";
String s3 = new String("Hello");
System.out.println(s1 == s2);
System.out.println(s1 == s3);
System.out.println(s1.equals(s3));
```

(A) `true false true`  
(B) `true true true`  
(C) `false false true`  
(D) `true false false`  
(E) `false true true`

---

**Question 2:** Consider the following code segment:
```java
Integer x = 127;
Integer y = 127;
Integer a = 128;
Integer b = 128;
System.out.println(x == y);
System.out.println(a == b);
```

What is printed as a result of executing the code segment?

(A) `true true`  
(B) `true false`  
(C) `false true`  
(D) `false false`  
(E) The code will not compile

---

**Question 3:** What is the result of executing the following code?
```java
String str = "Programming";
System.out.println(str.substring(3, 7) + str.charAt(0));
```

(A) `gramP`  
(B) `PramP`  
(C) `ograP`  
(D) `gramming`  
(E) An IndexOutOfBoundsException is thrown

---

**Question 4:** Which of the following statements about method overloading is FALSE?

(A) Overloaded methods must have different parameter lists  
(B) Overloaded methods can have different return types  
(C) Overloaded methods must have different return types  
(D) Overloaded methods can be in the same class  
(E) Constructors can be overloaded

---

**Question 5:** Given the following class:
```java
public class Point {
    private int x;
    private int y;
    
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    public void setLocation(int newX, int newY) {
        x = newX;
        y = newY;
    }
}
```

Which of the following correctly creates a Point object and sets its location to (5, 10)?

(A) `Point p = Point(5, 10);`  
(B) `Point p = new Point(); p.setLocation(5, 10);`  
(C) `Point p = new Point(0, 0); p.setLocation(5, 10);`  
(D) `Point p; p.setLocation(5, 10);`  
(E) `Point p = new Point(5, 10); setLocation(5, 10);`

---

**Question 6:** What is the output of the following code?
```java
String s = "Computer Science";
System.out.println(s.indexOf("Science") - s.indexOf("Science", 5));
```

(A) `0`  
(B) `9`  
(C) `-9`  
(D) `5`  
(E) `16`

---

**Question 7:** Consider the following code:
```java
double x = Math.pow(2, 3);
int y = (int) Math.sqrt(64);
double z = Math.abs(-5.5);
System.out.println(x + y + z);
```

What is printed?

(A) `21.5`  
(B) `21.0`  
(C) `13.5`  
(D) `19.5`  
(E) `20.5`

---

**Question 8:** Which of the following will generate a random integer between 10 and 50, inclusive?

(A) `(int)(Math.random() * 41) + 10`  
(B) `(int)(Math.random() * 40) + 10`  
(C) `(int)(Math.random() * 50) + 10`  
(D) `(int)(Math.random() * 41) + 9`  
(E) `(int)(Math.random() * 40) + 11`

---

**Question 9:** What is the output of the following code?
```java
String str1 = "APCS";
String str2 = str1.substring(1, 3);
String str3 = str1.toLowerCase();
System.out.println(str1 + str2 + str3);
```

(A) `APCSPCapcs`  
(B) `APCSpcapcs`  
(C) `APCSAPCapcs`  
(D) `apcspcapcs`  
(E) The code will not compile

---

**Question 10:** Consider the following method:
```java
public void mystery(String s) {
    s = s + "!";
    System.out.println(s);
}
```

What is the result of executing the following code segment?
```java
String word = "Hello";
mystery(word);
System.out.println(word);
```

(A) `Hello! Hello!`  
(B) `Hello! Hello`  
(C) `Hello Hello`  
(D) `Hello Hello!`  
(E) A compile-time error occurs

---

**Question 11:** Which of the following statements about wrapper classes is TRUE?

(A) Wrapper classes are mutable  
(B) Autoboxing converts a primitive to a wrapper object automatically  
(C) `Integer.MAX_VALUE` is an instance method  
(D) Wrapper classes cannot be used in collections  
(E) Unboxing must be done explicitly using cast operators

---

**Question 12:** What is the output of the following code?
```java
String s = "Java Programming";
System.out.println(s.replace("a", "o").substring(0, 4));
```

(A) `Java`  
(B) `Jovo`  
(C) `Jova`  
(D) `Jav`  
(E) `ava `

---

**Question 13:** Consider the following code:
```java
Integer num1 = 100;
Integer num2 = 100;
Integer num3 = num1;
num1++;
System.out.println(num1 == num2);
System.out.println(num1 == num3);
System.out.println(num1.equals(num3));
```

What is the output?

(A) `true true true`  
(B) `false false true`  
(C) `false false false`  
(D) `true false true`  
(E) `false true false`

---

**Question 14:** What is the value of `result` after the following code executes?
```java
String s1 = "Hello";
String s2 = "World";
String result = s1.compareTo(s2) < 0 ? s1 : s2;
```

(A) `Hello`  
(B) `World`  
(C) `true`  
(D) `false`  
(E) The code will not compile

---

**Question 15:** Which of the following code segments correctly demonstrates method chaining?

(A) `String s = "test"; s.toUpperCase(); s.substring(0, 2);`  
(B) `String s = "test".toUpperCase().substring(0, 2);`  
(C) `String s = "test"; s = toUpperCase().substring(0, 2);`  
(D) `String s = new String("test"); toUpperCase(); substring(0, 2);`  
(E) `String s = "test"; String t = s.toUpperCase(); t.substring(0, 2);`

---

**Question 16:** What is the output of the following code?
```java
Double d1 = 3.14;
Double d2 = 3.14;
System.out.println(d1 == d2);
System.out.println(d1.equals(d2));
```

(A) `true true`  
(B) `true false`  
(C) `false true`  
(D) `false false`  
(E) The code will not compile

---

**Question 17:** Consider the following code:
```java
String str = "ABCDEFGH";
int x = str.indexOf("DEF");
int y = str.lastIndexOf("C");
System.out.println(str.substring(x, y + 1));
```

What is printed?

(A) `DE`  
(B) `DEF`  
(C) An IndexOutOfBoundsException is thrown  
(D) `C`  
(E) The code will not compile

---

**Question 18:** What is the result of the following expression?
```java
(int) (Math.random() * 5 + 1) + (int) (Math.random() * 5 + 1)
```

(A) A random integer from 0 to 10  
(B) A random integer from 1 to 10  
(C) A random integer from 2 to 12  
(D) A random integer from 2 to 10  
(E) A random integer from 0 to 12

---

**Question 19:** Consider the following class definition:
```java
public class Student {
    private String name;
    
    public Student(String n) {
        name = n;
    }
    
    public Student(String firstName, String lastName) {
        name = firstName + " " + lastName;
    }
}
```

Which of the following statements about this class is TRUE?

(A) The class will not compile because constructors cannot be overloaded  
(B) The class demonstrates constructor overloading  
(C) Both constructors must have the same number of parameters  
(D) The constructors must have different return types  
(E) The second constructor should call the first constructor

---

**Question 20:** What is the output of the following code?
```java
String s = "hello";
s.toUpperCase();
System.out.println(s);
```

(A) `HELLO`  
(B) `hello`  
(C) `Hello`  
(D) A NullPointerException is thrown  
(E) The code will not compile

---

**Question 21:** Which of the following correctly converts a String to an int and then to an Integer?

(A) `Integer num = Integer.parseInt("123");`  
(B) `int num = (int) "123";`  
(C) `Integer num = "123".toInt();`  
(D) `int num = new Integer("123");`  
(E) Both A and D are correct

---

**Question 22:** What is the output of the following code?
```java
String s1 = "Test";
String s2 = "Test";
String s3 = s1.concat(s2);
System.out.println(s1 + " " + s3);
```

(A) `TestTest TestTest`  
(B) `Test Test`  
(C) `Test TestTest`  
(D) `TestTest Test`  
(E) The code will not compile

---

**Question 23:** Consider the following code:
```java
public void process(int x) {
    x = x * 2;
}

int value = 5;
process(value);
System.out.println(value);
```

What is printed?

(A) `5`  
(B) `10`  
(C) `0`  
(D) A compile-time error occurs  
(E) A runtime error occurs

---

**Question 24:** What is the value of `result` after executing the following code?
```java
String s = "Programming";
int result = s.indexOf("ram") + s.lastIndexOf("ing");
```

(A) `10`  
(B) `11`  
(C) `12`  
(D) `13`  
(E) `14`

---

**Question 25:** Which of the following statements about the `Math` class is FALSE?

(A) All methods in the Math class are static  
(B) The Math class is in the java.lang package  
(C) Math.PI is a constant representing π  
(D) You must create a Math object before using its methods  
(E) Math.random() returns a value in the range [0.0, 1.0)

---

## Section II: Free Response Questions (4 questions)

### Question 1: String Manipulation (10 points)

Write a method `isPalindrome` that takes a String parameter and returns `true` if the string is a palindrome (reads the same forwards and backwards, ignoring case and spaces) and `false` otherwise.

For example:
- `isPalindrome("Racecar")` returns `true`
- `isPalindrome("A man a plan a canal Panama")` returns `true`
- `isPalindrome("Hello")` returns `false`

**Requirements:**
- Use only String methods (no arrays or loops allowed)
- Handle both uppercase and lowercase letters
- Ignore spaces in the comparison

Write your complete method below:

```java
// Write your isPalindrome method here
```

---

### Question 2: Temperature Converter Class (15 points)

Design and implement a `TemperatureConverter` class that can convert temperatures between Celsius and Fahrenheit.

**Class specifications:**
- The class should have two overloaded constructors:
  - One that takes no parameters (default temperature is 0°C)
  - One that takes a double parameter representing Celsius temperature
  
- Implement the following methods:
  - `void setCelsius(double temp)` - sets the temperature in Celsius
  - `void setFahrenheit(double temp)` - sets the temperature by converting from Fahrenheit to Celsius
  - `double getCelsius()` - returns the temperature in Celsius
  - `double getFahrenheit()` - returns the temperature in Fahrenheit
  - `String getTemperatureInfo()` - returns a string in the format: "Temperature: XX.X°C / YY.Y°F"

**Formulas:**
- Celsius to Fahrenheit: F = (C × 9/5) + 32
- Fahrenheit to Celsius: C = (F - 32) × 5/9

Write your complete class below:

```java
// Write your TemperatureConverter class here
```

---

### Question 3: Password Validator (15 points)

Write a class `PasswordValidator` that validates passwords according to specific rules.

**Class specifications:**
- Constructor: `PasswordValidator(String password)` - stores the password to validate

- Implement the following methods:
  - `boolean hasMinimumLength()` - returns true if password has at least 8 characters
  - `boolean hasUpperCase()` - returns true if password contains at least one uppercase letter
  - `boolean hasLowerCase()` - returns true if password contains at least one lowercase letter
  - `boolean hasDigit()` - returns true if password contains at least one digit (0-9)
  - `boolean hasSpecialChar()` - returns true if password contains at least one special character (!@#$%^&*)
  - `boolean isValid()` - returns true if ALL of the above conditions are met
  - `String getStrength()` - returns "Strong" if all conditions are met, "Medium" if 3-4 conditions are met, "Weak" if fewer than 3 conditions are met

**Requirements:**
- Use String methods to implement the validation logic
- You may use the `charAt()` method and iterate through the string
- Use wrapper class methods where appropriate

Write your complete class below:

```java
// Write your PasswordValidator class here
```

---

### Question 4: Statistical Calculator (20 points)

Write a class `StatCalculator` that performs statistical calculations on a set of numbers.

**Class specifications:**
- Instance variable: Store a list of numbers as a String (e.g., "10 20 30 40 50")
- Constructor: `StatCalculator(String numbers)` - takes a space-separated string of integers

- Implement the following methods:
  - `int getCount()` - returns the count of numbers
  - `double getSum()` - returns the sum of all numbers
  - `double getMean()` - returns the average (mean) of the numbers
  - `int getMax()` - returns the maximum value
  - `int getMin()` - returns the minimum value
  - `double getRange()` - returns the difference between max and min
  - `String getSummary()` - returns a formatted string with all statistics

**Example:**
```java
StatCalculator calc = new StatCalculator("10 20 30 40 50");
System.out.println(calc.getSummary());
```

**Output:**
```
Count: 5
Sum: 150.0
Mean: 30.0
Max: 50
Min: 10
Range: 40.0
```

**Requirements:**
- Parse the input string to extract individual numbers
- Use Integer wrapper class methods for conversion
- Use Math class methods where appropriate
- Format the output string properly with line breaks

Write your complete class below:

```java
// Write your StatCalculator class here
```

---

## End of Exam

**Scoring Guide:**
- Section I (Multiple Choice): 50 points (2 points each)
- Section II (Free Response): 60 points total
  - Question 1: 10 points
  - Question 2: 15 points
  - Question 3: 15 points
  - Question 4: 20 points
- **Total: 110 points**

**Grading Scale:**
- A: 99-110 points
- B: 88-98 points
- C: 77-87 points
- D: 66-76 points
- F: Below 66 points
