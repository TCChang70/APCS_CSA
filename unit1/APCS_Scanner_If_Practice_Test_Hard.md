# 📚 AP Computer Science A - Advanced Practice Test
## Scanner Input and Conditional Statements (High Difficulty)

**測驗說明:**
- **總分:** 100 分
- **時間限制:** 90 分鐘
- **第一部分 - 選擇題 (Multiple Choice):** 60 分 (15 題，每題 4 分)
- **第二部分 - 非選擇題 (Free Response):** 40 分 (2 題)
- **計算機:** 不允許使用
- **重點考核:** 複合布林邏輯 (De Morgan's Laws)、短路求值 (Short-circuit)、Dangling Else、Scanner 緩衝區問題、字串比較、邊界條件。

---

## 📝 Section I: Multiple Choice Questions (60 points)
*Select the best answer for each question. Be careful with syntax traps and logic nuances.*

### **Question 1: The "Dangling Else" Trap**
Consider the following code segment. What is printed if `x = 5` and `y = 10`?

```java
int x = 5;
int y = 10;
if (x > 5)
    if (y > 5)
        System.out.println("A");
else
    System.out.println("B");
```

A) `A`  
B) `B`  
C) `A` and `B`  
D) Nothing is printed  
E) Compile-time error

---

### **Question 2: Scanner Buffer Handling**
A user enters the following input at the console (pressing Enter after each line):
```text
42
Hello World
```
Consider the code:
```java
Scanner sc = new Scanner(System.in);
int num = sc.nextInt();
String text = sc.nextLine();
System.out.println(num + "-" + text);
```
What is the output?

A) `42-Hello World`  
B) `42-Hello`  
C) `42-` (followed by an empty line)  
D) `42- World`  
E) InputMismatchException

---

### **Question 3: Boolean Logic & De Morgan's Laws**
Which of the following expressions is equivalent to `!(a || b) && c`?

A) `!a || !b && c`  
B) `(!a && !b) && c`  
C) `!a && !b || c`  
D) `!(a && b) && c`  
E) `!a || (!b && c)`

---

### **Question 4: String Comparison**
The user enters `STOP` when prompted. What is the output?

```java
Scanner sc = new Scanner(System.in);
System.out.print("Enter command: ");
String cmd = sc.next();

if (cmd == "STOP") {
    System.out.print("Stopped");
} else if (cmd.equals("STOP")) {
    System.out.print("Terminated");
} else {
    System.out.print("Continuing");
}
```

A) `Stopped`  
B) `Terminated`  
C) `StoppedTerminated`  
D) `Continuing`  
E) Runtime Error

---

### **Question 5: Short-Circuit Evaluation**
Assume `String s = null;`. What is the result of executing the following statement?

```java
if (s != null && s.length() > 0) {
    System.out.println("Valid");
} else {
    System.out.println("Invalid");
}
```

A) Prints `Valid`  
B) Prints `Invalid`  
C) Throws `NullPointerException`  
D) Throws `StringIndexOutOfBoundsException`  
E) Compile-time error

---

### **Question 6: Integer Division & Casting in Conditions**
What is printed when `val = 11`?

```java
int val = 11;
if (val / 2 == 5.5) {
    System.out.print("Exact");
} else if (val / 2 == 5) {
    System.out.print("Floor");
} else {
    System.out.print("None");
}
```

A) `Exact`  
B) `Floor`  
C) `None`  
D) `ExactFloor`  
E) Compile error due to type mismatch

---

### **Question 7: Nested Logic Tracing**
What is the final value of `result`?

```java
boolean a = true;
boolean b = false;
boolean c = true;
int result = 0;

if (a && !b) {
    result += 1;
    if (b || !c) {
        result += 2;
    } else if (a) {
        result += 4;
    }
}
if (c && (a || b)) {
    result += 8;
}
```

A) 1  
B) 5  
C) 9  
D) 13  
E) 15

---

### **Question 8: The `next()` vs `nextBoolean()` Trap**
User input: `true false`

```java
Scanner sc = new Scanner(System.in);
boolean b1 = false;
if (sc.hasNextBoolean()) {
    b1 = sc.nextBoolean();
}
String s1 = sc.next();
System.out.println(b1 + " " + s1);
```

A) `true false`  
B) `true true`  
C) `false false`  
D) `false true`  
E) InputMismatchException

---

### **Question 9: Complex Boolean Assignment**
What is the value of `ticket` after execution?

```java
int age = 16;
boolean hasID = false;
boolean withParent = true;
boolean ticket = (age >= 18 && hasID) || (age < 18 && withParent);
```

A) `true`  
B) `false`  
C) `null`  
D) Syntax error  
E) Runtime error

---

### **Question 10: Scope and Initialization**
Consider the following code:

```java
int x = 10;
if (x > 5) {
    int y = 20;
    x = y + x;
}
// Line A
System.out.println(x + y);
```
What happens at **Line A** (or the print statement)?

A) Prints `30`  
B) Prints `20`  
C) Prints `10`  
D) Compile-time error: `y` cannot be resolved to a variable  
E) Compile-time error: `x` is not initialized

---

### **Question 11: Modulo and Negative Numbers**
What is printed?
```java
int k = -7;
if (k % 2 == 1)
    System.out.print("Odd");
else
    System.out.print("Even/NegativeOdd");
```

A) `Odd`  
B) `Even/NegativeOdd`  
C) Runtime Error  
D) No Output  
E) `OddEven/NegativeOdd`

---

### **Question 12: Floating Point Equality**
Why is the following code considered bad practice or potentially incorrect?
```java
double d = 1.0 / 3.0;
if (d * 3 == 1.0) { ... }
```

A) `d * 3` will result in an integer `1`.  
B) Floating point arithmetic may result in precision errors, making strict equality `==` unreliable.  
C) `1.0` is a float, not a double.  
D) The code will throw an ArithmeticException.  
E) It is perfectly fine and correct.

---

### **Question 13: Precedence of Operators**
Evaluate the condition: `true || false && false`.

A) `true`  
B) `false`  
C) Syntax Error  
D) Depends on compiler  
E) `null`

---

### **Question 14: Else-If Logic Gap**
What range of `n` prints "C"?
```java
if (n < 10) System.out.print("A");
else if (n > 20) System.out.print("B");
else System.out.print("C");
```

A) `n` is between 10 and 20 (exclusive)  
B) `n` is between 10 and 20 (inclusive)  
C) `n` >= 10 and `n` <= 20  
D) `n` > 10 and `n` < 20  
E) `n` >= 20

---

### **Question 15: Scanner Delimiters**
By default, `Scanner` separates tokens using:

A) Only spaces  
B) Only newlines  
C) Any whitespace (space, tab, newline)  
D) Commas  
E) Semicolons

---

## 💻 Section II: Free Response Questions (40 points)

### **FRQ 1: The Advanced Ticket Kiosk (20 points)**
Write a complete Java program (class `TicketKiosk`) that calculates the price of a movie ticket based on complex rules.

**Requirements:**
1.  Create a `Scanner` to read input.
2.  Prompt the user for their **age** (int), **day of week** (1=Mon, 7=Sun) (int), and whether they are a **member** (boolean, user enters `true`/`false`).
3.  **Base Price:** $15.00.
4.  **Discounts (Applied in order, non-cumulative unless specified):**
    -   **Age Rule:** Children (< 12) and Seniors (>= 65) get a 50% discount on the *base price*.
    -   **Day Rule:** On Tuesdays (Day 2), everyone gets $2.00 off the price *after* age discount is applied.
    -   **Member Rule:** Members get an additional 10% off the *final* price (after age and day discounts).
5.  **Validation:**
    -   If age is negative or day is not 1-7, print "Invalid Input" and terminate (or set price to 0).
6.  **Output:** Print the final price formatted to 2 decimal places (e.g., `$6.50`). You can use `System.out.printf` or just print the double.

**Example Run:**
```text
Enter Age: 70
Enter Day (1-7): 2
Is Member (true/false): true

Calculation:
Base: 15.0
Age Discount (Senior): 15.0 * 0.5 = 7.5
Day Discount (Tuesday): 7.5 - 2.0 = 5.5
Member Discount: 5.5 * 0.9 = 4.95
Output: $4.95
```

---

### **FRQ 2: The Secure Login Validator (20 points)**
Write a code segment (or method) that validates a user's new password based on strict security policies using `Scanner` and `if/else` logic.

**Scenario:**
You need to read a username and a password from the console.

**Rules:**
1.  **Username** cannot be empty (use `length()`).
2.  **Password** must meet **ALL** of the following criteria:
    -   At least 8 characters long.
    -   Cannot contain the username (case-sensitive check is fine).
    -   Must not be the same as a "forbidden" password: `"password123"`.
    -   **Special Rule:** If the password is exactly "admin", it is allowed ONLY if the username is "sysadmin". Otherwise, "admin" is rejected as too short.

**Logic Flow:**
-   Read username.
-   Read password.
-   Check conditions using nested or compound `if/else` statements.
-   Print exactly one of the following messages:
    -   `"Registration Successful"`
    -   `"Error: Password too short"`
    -   `"Error: Password contains username"`
    -   `"Error: Password is forbidden"`
    -   `"Error: Invalid Admin Access"` (Specific to the admin/sysadmin rule)

**Note:** You do not need to check for uppercase/lowercase/numbers (unless you want to use String methods like `indexOf`, but stick to logic flow primarily).

```java
// Write your code below
Scanner scan = new Scanner(System.in);
// ...
```

---

## 🔑 Answer Key (For Teacher Use Only)

### Section I Answers
1.  **D** - Dangling Else. The `else` belongs to the *inner* `if`. Since `x (5) > 5` is false, the inner block is skipped entirely. Nothing prints.
2.  **C** - `nextInt()` reads `42` but leaves the newline `\n` in the buffer. `nextLine()` immediately reads that empty string (from 42 to newline). `num` is 42, `text` is empty. Output: `42-`.
3.  **B** - De Morgan's Law: `!(A || B)` becomes `!A && !B`. So `(!a && !b) && c`.
4.  **B** - `==` compares references. Scanner creates new String objects. `equals()` compares content.
5.  **B** - Short-circuit. `s != null` is false. The second part `s.length()` is NOT evaluated. No exception. Prints "Invalid".
6.  **B** - `11 / 2` is integer division, result is `5`. `5 == 5.5` is false. `5 == 5` is true. Prints "Floor".
7.  **D** -
    -   `if (a && !b)` -> `true && true` -> Enter block. `result` = 1.
    -   Inner: `if (b || !c)` -> `false || false` -> False.
    -   Inner `else if (a)` -> `true`. `result` += 4. `result` is 5.
    -   Second block: `if (c && (a || b))` -> `true && (true || false)` -> `true`. `result` += 8.
    -   Total: 5 + 8 = 13.
8.  **A** - `hasNextBoolean()` checks "true". `nextBoolean()` consumes "true". `next()` consumes "false".
9.  **A** - `(16 >= 18 && false)` is false. `(16 < 18 && true)` is true. `false || true` is true.
10. **D** - Variable `y` is declared inside the `if` block. It is out of scope at Line A.
11. **B** - `-7 % 2` is `-1` in Java. `-1 == 1` is false. Goes to else.
12. **B** - Floating point precision. `1.0/3.0` is `0.3333...`. Multiplying by 3 might be `0.9999...` or `1.0` depending on precision, but relying on `==` is dangerous.
13. **A** - `&&` has higher precedence than `||`. Evaluated as `true || (false && false)` -> `true || false` -> `true`.
14. **C** - `else` covers everything not `< 10` and not `> 20`. So `10 <= n <= 20`.
15. **C** - Whitespace.

### Section II Solution Sketches

**FRQ 1 (TicketKiosk)**
```java
Scanner sc = new Scanner(System.in);
System.out.print("Enter Age: ");
int age = sc.nextInt();
System.out.print("Enter Day (1-7): ");
int day = sc.nextInt();
System.out.print("Is Member (true/false): ");
boolean isMember = sc.nextBoolean();

if (age < 0 || day < 1 || day > 7) {
    System.out.println("Invalid Input");
} else {
    double price = 15.0;
    // Age Rule
    if (age < 12 || age >= 65) {
        price = price * 0.5;
    }
    // Day Rule
    if (day == 2) {
        price = price - 2.0;
    }
    // Member Rule
    if (isMember) {
        price = price * 0.9;
    }
    System.out.printf("Output: $%.2f\n", price);
}
```

**FRQ 2 (Secure Login)**
```java
Scanner scan = new Scanner(System.in);
String user = scan.next();
String pass = scan.next();

if (user.length() == 0) {
    System.out.println("Error: Empty username");
} else {
    // Special Admin Rule
    if (pass.equals("admin")) {
        if (user.equals("sysadmin")) {
            System.out.println("Registration Successful");
        } else {
            System.out.println("Error: Invalid Admin Access");
        }
    } else {
        // Standard Rules
        if (pass.length() < 8) {
            System.out.println("Error: Password too short");
        } else if (pass.contains(user)) {
            System.out.println("Error: Password contains username");
        } else if (pass.equals("password123")) {
            System.out.println("Error: Password is forbidden");
        } else {
            System.out.println("Registration Successful");
        }
    }
}
```
