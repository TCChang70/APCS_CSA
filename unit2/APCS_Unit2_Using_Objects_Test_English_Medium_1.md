# APCS CSA Unit 2: Using Objects - Medium Level Test

**Total Points: 100**
- Multiple Choice: 25 questions (2 points each = 50 points)
- Free Response Questions: 4 questions (50 points total)

**Time Limit: 90 minutes**

---

## Section I: Multiple Choice Questions (50 points)

**Directions:** Choose the best answer for each question.

### Questions 1-25

**1. Which of the following statements about classes and objects is true?**

A) A class is an instance of an object  
B) An object is an instance of a class  
C) Classes and objects are the same thing  
D) Objects cannot be created from classes  
E) A class can only create one object

---

**2. Consider the following code segment:**
```java
String str = new String("Hello");
```
**What does the `new` keyword do in this statement?**

A) It creates a new class  
B) It creates a new instance of the String class  
C) It deletes the old string  
D) It modifies the existing string  
E) It compares two strings

---

**3. Which of the following is an example of constructor overloading?**

A) Having two methods with the same name but different return types  
B) Having two constructors with different parameter lists  
C) Having two methods with different names but same parameters  
D) Having a method and a constructor with the same name  
E) Having two methods that perform different operations

---

**4. What is the output of the following code segment?**
```java
public void printMessage() {
    System.out.println("Welcome");
}
```
**If this method is called using `printMessage();`**

A) Welcome  
B) void  
C) printMessage  
D) Nothing is printed  
E) Compilation error

---

**5. Consider the following code:**
```java
public void setAge(int age) {
    this.age = age;
}
```
**What type of parameter passing mechanism does Java use?**

A) Pass by reference  
B) Pass by value  
C) Pass by pointer  
D) Pass by object  
E) Pass by address

---

**6. What is the return type of the following method?**
```java
public int calculateSum(int a, int b) {
    return a + b;
}
```

A) void  
B) int  
C) double  
D) String  
E) boolean

---

**7. Which statement about String immutability is correct?**

A) Strings can be modified after creation  
B) Once created, a String object cannot be changed  
C) Strings are mutable in Java  
D) String values are stored in variables that can change  
E) Immutability only applies to empty strings

---

**8. What is the output of the following code?**
```java
String str = "Java Programming";
System.out.println(str.length());
```

A) 15  
B) 16  
C) 17  
D) 14  
E) Compilation error

---

**9. Given the following code:**
```java
String text = "Hello World";
char ch = text.charAt(6);
```
**What is the value of `ch`?**

A) 'W'  
B) 'o'  
C) 'H'  
D) ' ' (space)  
E) 'r'

---

**10. What does the following code print?**
```java
String s1 = "apple";
String s2 = "Apple";
System.out.println(s1.equals(s2));
```

A) true  
B) false  
C) 0  
D) 1  
E) Compilation error

---

**11. Consider the following code:**
```java
String text = "Programming";
String sub = text.substring(3, 7);
System.out.println(sub);
```
**What is printed?**

A) Prog  
B) gram  
C) ogra  
D) rogramm  
E) Programming

---

**12. What is the result of the following code?**
```java
String str = "Hello";
int index = str.indexOf("l");
System.out.println(index);
```

A) 1  
B) 2  
C) 3  
D) -1  
E) 0

---

**13. Which method converts a string to uppercase?**

A) `toUpper()`  
B) `upperCase()`  
C) `toUpperCase()`  
D) `convertToUpper()`  
E) `makeUpper()`

---

**14. What is autoboxing in Java?**

A) Converting a primitive type to its corresponding wrapper class automatically  
B) Converting a wrapper class to a primitive type automatically  
C) Creating a box around an object  
D) Storing objects in an array  
E) Converting strings to integers

---

**15. Which of the following creates an Integer wrapper object?**

A) `int x = 5;`  
B) `Integer x = new Integer(5);`  
C) `integer x = 5;`  
D) `Int x = new Int(5);`  
E) `INTEGER x = 5;`

---

**16. What is the output of the following code?**
```java
Integer num = 100;
int value = num; // unboxing
System.out.println(value);
```

A) 100  
B) null  
C) 0  
D) Compilation error  
E) Runtime error

---

**17. Which Math class method returns the absolute value of a number?**

A) `Math.absolute()`  
B) `Math.abs()`  
C) `Math.positive()`  
D) `Math.value()`  
E) `Math.absValue()`

---

**18. What does `Math.pow(2, 3)` return?**

A) 6  
B) 8  
C) 9  
D) 5  
E) 2.3

---

**19. Which statement about `Math.random()` is true?**

A) It returns a random integer between 0 and 100  
B) It returns a random double between 0.0 (inclusive) and 1.0 (exclusive)  
C) It returns a random boolean value  
D) It returns a random negative number  
E) It requires a parameter to specify the range

---

**20. What is the output of the following code?**
```java
System.out.println(Math.sqrt(16));
```

A) 4  
B) 4.0  
C) 256  
D) 8  
E) 2

---

**21. Consider the following code:**
```java
String s1 = "Hello";
String s2 = s1;
s1 = "World";
System.out.println(s2);
```
**What is printed?**

A) World  
B) Hello  
C) HelloWorld  
D) null  
E) Compilation error

---

**22. Which of the following correctly compares two strings for equality?**

A) `str1 == str2`  
B) `str1.equals(str2)`  
C) `str1.compareTo(str2) == true`  
D) `str1.compare(str2)`  
E) `equals(str1, str2)`

---

**23. What is the result of the following expression?**
```java
int result = (int)(Math.random() * 10);
```
**What range of values can `result` have?**

A) 0 to 9  
B) 1 to 10  
C) 0 to 10  
D) 1 to 9  
E) 0 to 100

---

**24. Given the following code:**
```java
Double d1 = 3.14;
Double d2 = 3.14;
System.out.println(d1 == d2);
```
**What is the output?**

A) true  
B) false  
C) 3.14  
D) Compilation error  
E) It depends on the JVM

---

**25. What does the following code print?**
```java
String str = "Java";
str.concat(" Programming");
System.out.println(str);
```

A) Java Programming  
B) Java  
C) Programming  
D) null  
E) Compilation error

---

## Section II: Free Response Questions (50 points)

### Question 1 (12 points)

A student is creating a `Book` class to represent books in a library system. The class should store information about a book's title, author, and number of pages.

**Part A (4 points):** Write the instance variables for the `Book` class.

**Part B (4 points):** Write a constructor that takes three parameters (title, author, and pages) and initializes all instance variables.

**Part C (4 points):** Write a method `getSummary()` that returns a String in the format: `"Title by Author - Pages pages"`. For example: `"1984 by George Orwell - 328 pages"`.

---

### Question 2 (13 points)

The `StringProcessor` class contains methods to manipulate strings.

```java
public class StringProcessor {
    // Part A
    
    // Part B
    
    // Part C
}
```

**Part A (4 points):** Write a method `countVowels` that takes a String parameter and returns the number of vowels (a, e, i, o, u, both uppercase and lowercase) in the string.

**Part B (5 points):** Write a method `reverseWords` that takes a String containing words separated by spaces and returns a new String with the words in reverse order. For example, `"Hello World Java"` should return `"Java World Hello"`.

**Part C (4 points):** Write a method `isPalindrome` that takes a String parameter and returns true if the string is a palindrome (reads the same forwards and backwards, ignoring case). For example, `"Racecar"` should return true.

---

### Question 3 (12 points)

A teacher wants to create a `GradeCalculator` class to help calculate student grades.

**Part A (4 points):** Write a method `calculateAverage` that takes an array of Integer objects representing test scores and returns the average as a double. If the array is empty, return 0.0.

**Part B (4 points):** Write a method `getLetterGrade` that takes a double parameter representing a percentage grade and returns a String representing the letter grade according to this scale:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: below 60

**Part C (4 points):** Write a method `findHighest` that takes an array of Integer objects and returns the highest value. If the array is empty, return null.

---

### Question 4 (13 points)

A programmer is developing a `Circle` class that uses the Math class for calculations.

```java
public class Circle {
    private double radius;
    
    // Part A
    
    // Part B
    
    // Part C
}
```

**Part A (4 points):** Write a constructor that takes a double parameter for the radius and initializes the instance variable. If the radius is negative, set it to 0.0.

**Part B (5 points):** Write a method `getArea()` that returns the area of the circle. The area formula is π × radius². Use `Math.PI` for the value of π.

**Part C (4 points):** Write a method `getCircumference()` that returns the circumference of the circle. The circumference formula is 2 × π × radius. Use `Math.PI` for the value of π.

---

## End of Exam

**Remember to:**
- Show all your work for Free Response Questions
- Use proper Java syntax and naming conventions
- Consider edge cases in your solutions
- Write clear and readable code with appropriate comments where necessary
