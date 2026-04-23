# APCS Computer Science A - FRQ Practice Test
## Classes and Objects

**Time**: 90 minutes  
**Total Points**: 100 points  
**Instructions**: Answer all 4 questions. Write your solutions clearly and make sure your code compiles and runs correctly.

---

## Question 1: Student Grade Management System (25 points)

A school needs a system to manage student grades. You will implement a `Student` class that stores student information and calculates their GPA.

### Part A (10 points)

Write the complete `Student` class that includes:
- Private instance variables for `name` (String), `id` (int), and `grades` (ArrayList of Double)
- A constructor that takes the student's name and id, and initializes an empty grades list
- A method `addGrade(double grade)` that adds a grade to the student's grade list (grades are between 0.0 and 100.0)
- A method `getName()` that returns the student's name
- A method `getId()` that returns the student's id

### Part B (10 points)

Add the following methods to your `Student` class:
- `calculateGPA()` - returns the GPA on a 4.0 scale. Use the following conversion:
  - 90-100: 4.0
  - 80-89: 3.0
  - 70-79: 2.0
  - 60-69: 1.0
  - Below 60: 0.0
  
  The GPA is the average of all converted grades. If there are no grades, return 0.0.

- `getLetterGrade()` - returns the overall letter grade (A, B, C, D, or F) based on the average of all numeric grades

### Part C (5 points)

Write a `ClassRoster` class that:
- Contains an ArrayList of `Student` objects
- Has a constructor that initializes an empty roster
- Has a method `addStudent(Student s)` that adds a student to the roster
- Has a method `getTopStudent()` that returns the Student with the highest GPA. If the roster is empty, return null.

---

## Question 2: Bank Account System (25 points)

You will create a banking system with different types of accounts.

### Part A (12 points)

Write a `BankAccount` class with the following:
- Private instance variables: `accountNumber` (String), `balance` (double), and `owner` (String)
- A constructor that takes accountNumber and owner, and sets the initial balance to 0.0
- A method `deposit(double amount)` that adds the amount to the balance and returns true if successful (amount must be positive), false otherwise
- A method `withdraw(double amount)` that subtracts the amount from the balance if there are sufficient funds and returns true; otherwise returns false and does not change the balance
- Methods `getBalance()`, `getAccountNumber()`, and `getOwner()` that return the respective values

### Part B (8 points)

Write a `SavingsAccount` class that extends `BankAccount` with:
- A private instance variable `interestRate` (double) representing the annual interest rate
- A constructor that takes accountNumber, owner, and interestRate
- A method `applyInterest()` that adds interest to the balance based on the interest rate (balance = balance * (1 + interestRate))
- Override the `withdraw` method to charge a $2.00 fee for each withdrawal. The withdrawal should only succeed if the account has enough money for both the withdrawal amount and the fee.

### Part C (5 points)

Explain in 2-3 sentences:
1. What is the benefit of having `SavingsAccount` extend `BankAccount`?
2. What is the difference between overriding and overloading a method?

---

## Question 3: Library Book Management (25 points)

A library needs a system to manage its book collection.

### Part A (10 points)

Write a `Book` class that includes:
- Private instance variables: `title` (String), `author` (String), `isbn` (String), `isCheckedOut` (boolean)
- A constructor that takes title, author, and isbn. Set isCheckedOut to false initially
- A method `checkOut()` that sets isCheckedOut to true and returns true if the book was available (previously not checked out), returns false if already checked out
- A method `returnBook()` that sets isCheckedOut to false
- Getter methods for all instance variables
- A method `toString()` that returns a String in the format: "Title: [title], Author: [author], ISBN: [isbn], Available: [true/false]"

### Part B (10 points)

Write a `Library` class that:
- Has a private ArrayList of `Book` objects called `catalog`
- Has a constructor that initializes an empty catalog
- Has a method `addBook(Book book)` that adds a book to the catalog
- Has a method `findBookByISBN(String isbn)` that returns the Book object with the matching ISBN, or null if not found
- Has a method `getAvailableBooks()` that returns an ArrayList of all books that are not currently checked out
- Has a method `checkOutBook(String isbn)` that attempts to check out the book with the given ISBN. Returns true if successful, false if the book doesn't exist or is already checked out.

### Part C (5 points)

Write a test class `LibraryTest` with a main method that:
- Creates a Library object
- Adds at least 3 Book objects to the library
- Checks out one book
- Prints all available books
- Attempts to check out the same book again and prints the result

---

## Question 4: Rectangle Class with Comparison (25 points)

You will implement a `Rectangle` class that can be compared and manipulated.

### Part A (10 points)

Write a `Rectangle` class that includes:
- Private instance variables: `length` (double) and `width` (double)
- A constructor that takes length and width. If either value is negative or zero, set it to 1.0
- Methods `getLength()` and `getWidth()` that return the respective values
- A method `calculateArea()` that returns the area of the rectangle
- A method `calculatePerimeter()` that returns the perimeter of the rectangle
- A method `isSquare()` that returns true if the rectangle is a square (length equals width), false otherwise

### Part B (10 points)

Add the following methods to the `Rectangle` class:
- `equals(Rectangle other)` - returns true if both rectangles have the same length and width (in any order). For example, a 3x5 rectangle equals a 5x3 rectangle.
- `compareTo(Rectangle other)` - returns a negative number if this rectangle's area is less than the other's area, 0 if equal, and a positive number if greater
- `scale(double factor)` - multiplies both length and width by the given factor (if factor is positive). Returns true if scaling was successful, false otherwise.

### Part C (5 points)

Write a static method `findLargestRectangle(Rectangle[] rectangles)` that:
- Takes an array of Rectangle objects
- Returns the Rectangle with the largest area
- Returns null if the array is empty or null

Include a main method that tests this functionality with at least 4 Rectangle objects.

---

## Grading Rubric

For each question:
- **Correct syntax and compilation**: 30% of question points
- **Correct logic and functionality**: 50% of question points  
- **Code style and documentation**: 10% of question points
- **Edge case handling**: 10% of question points

**Good luck!**
