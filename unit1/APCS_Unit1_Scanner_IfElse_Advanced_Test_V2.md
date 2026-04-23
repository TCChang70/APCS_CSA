# AP Computer Science A - Unit 1 Advanced Practice Test (Version 2)
## Primitive Types, Scanner, and Conditional Statements

**Total Questions: 20 | Time Limit: 40 minutes | Difficulty: Advanced**

---

## Part I: Multiple Choice Questions (15 questions)

### **Question 1**
What is the output of the following code?
```java
int a = 12;
double b = 4.5;
System.out.println(a / b + b / a);
```
A) 2.666...  
B) 3.75  
C) 3.0  
D) 2.5  
E) 2.0

---

### **Question 2**
Given the following input:
```
8
hello world
```
What will be the value of `str` after executing this code?
```java
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
String str = sc.nextLine();
```
A) "hello world"  
B) ""  
C) " world"  
D) "\n"  
E) "8"

---

### **Question 3**
Which of the following statements about primitive types is true?
A) `boolean` can only be 0 or 1
B) `char` can store negative values
C) `double` has higher precision than `float`
D) `int` can store decimal values
E) `byte` is unsigned

---

### **Question 4**
What is the result of the following code?
```java
int x = 3;
int y = 7;
if (x * 2 == y - 1) {
    System.out.print("A");
} else {
    System.out.print("B");
}
System.out.print("C");
```
A) AC  
B) BC  
C) AB  
D) CB  
E) BA

---

### **Question 5**
Which of the following best describes the effect of the following code?
```java
int x = 10;
if (x++ > 10) {
    x += 2;
} else {
    x -= 2;
}
System.out.println(x);
```
A) 8  
B) 9  
C) 10  
D) 11  
E) 12

---

### **Question 6**
What is the output?
```java
int a = 5;
int b = 2;
double c = a / b;
System.out.println(c);
```
A) 2.5  
B) 2.0  
C) 2  
D) 2.00  
E) Compile error

---

### **Question 7**
Which Scanner method would you use to read a single word (no spaces) from user input?
A) nextInt()  
B) nextLine()  
C) next()  
D) nextWord()  
E) read()

---

### **Question 8**
What is the output?
```java
int x = 4;
if (x % 2 == 0 && x > 0) {
    System.out.print("Even");
} else {
    System.out.print("Odd");
}
```
A) Even  
B) Odd  
C) 4  
D) 0  
E) No output

---

### **Question 9**
Which of the following is NOT a valid Java variable name?
A) _score  
B) $amount  
C) 2ndPlace  
D) totalSum  
E) value2

---

### **Question 10**
What is the output?
```java
int a = 6;
int b = 3;
if (a / b == 2 && a % b == 0) {
    System.out.print("Yes");
} else {
    System.out.print("No");
}
```
A) Yes  
B) No  
C) 2  
D) 0  
E) Compile error

---

### **Question 11**
What is the value of `result` after this code?
```java
int x = 7;
int y = 2;
int result = x % y + y * x;
```
A) 15  
B) 14  
C) 13  
D) 12  
E) 9

---

### **Question 12**
Which code correctly checks if a number is both positive and even?
A) `if (num > 0 && num % 2 == 0)`  
B) `if (num > 0 || num % 2 == 0)`  
C) `if (num % 2 == 0 && num < 0)`  
D) `if (num > 0 && num % 2 != 0)`  
E) `if (num < 0 && num % 2 == 0)`

---

### **Question 13**
What is the output?
```java
int n = 5;
System.out.println(++n + n++);
```
A) 10  
B) 11  
C) 12  
D) 13  
E) 14

---

### **Question 14**
Which of the following is the correct way to declare and initialize a double variable to 3.14?
A) `double pi = 3.14;`  
B) `double pi = "3.14";`  
C) `double pi = 3,14;`  
D) `double pi = 3;14;`  
E) `double pi = 3:14;`

---

### **Question 15**
What is the output?
```java
int x = 2;
if (x > 1)
    if (x < 3)
        System.out.print("A");
    else
        System.out.print("B");
System.out.print("C");
```
A) AC  
B) BC  
C) AB  
D) CB  
E) BA

---

## Part II: Free Response Questions (5 questions)

### **Question 16 (Programming)**
Write a Java program that prompts the user to enter two integers, then prints the larger value. If the values are equal, print "Equal".

---

### **Question 17 (Code Analysis)**
Given the following code:
```java
Scanner sc = new Scanner(System.in);
System.out.print("Enter a number: ");
int n = sc.nextInt();
if (n % 2 == 0 && n > 10) {
    System.out.println("Even and greater than 10");
} else if (n % 2 == 0) {
    System.out.println("Even and not greater than 10");
} else {
    System.out.println("Odd");
}
```
Explain what the code does and give the output if the user enters 12, 8, and 7.

---

### **Question 18 (Programming)**
Write a method called `isTeenager` that takes an integer age and returns `true` if the age is between 13 and 19 (inclusive), otherwise returns `false`.

---

### **Question 19 (Short Answer)**
Explain the difference between `=` and `==` in Java. Give an example for each.

---

### **Question 20 (Programming)**
Write a Java program that uses Scanner to read a double value representing a temperature in Celsius, checks if the value is above absolute zero (-273.15), and if so, converts it to Fahrenheit and prints the result with two decimal places. If not, print "Invalid temperature".

---

## Answer Key

### Multiple Choice Answers:
1. B
2. B
3. C
4. A
5. A
6. B
7. C
8. A
9. C
10. A
11. B
12. A
13. D
14. A
15. A

---

**Good luck!**
