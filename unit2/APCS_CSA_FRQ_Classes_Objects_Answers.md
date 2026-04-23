# APCS Computer Science A - FRQ Practice Test
## Classes and Objects - ANSWER KEY

---

## Question 1: Student Grade Management System - SOLUTION

### Part A Solution (10 points)

```java
import java.util.ArrayList;

public class Student {
    private String name;
    private int id;
    private ArrayList<Double> grades;
    
    // Constructor
    public Student(String name, int id) {
        this.name = name;
        this.id = id;
        this.grades = new ArrayList<Double>();
    }
    
    // Add a grade to the student's grade list
    public void addGrade(double grade) {
        if (grade >= 0.0 && grade <= 100.0) {
            grades.add(grade);
        }
    }
    
    // Getter for name
    public String getName() {
        return name;
    }
    
    // Getter for id
    public int getId() {
        return id;
    }
}
```

**Grading Notes:**
- Constructor properly initializes all instance variables (3 points)
- Correct access modifiers (private for variables, public for methods) (2 points)
- addGrade validates input range (2 points)
- Getter methods implemented correctly (3 points)

---

### Part B Solution (10 points)

```java
// Add these methods to the Student class above

public double calculateGPA() {
    if (grades.isEmpty()) {
        return 0.0;
    }
    
    double totalGPA = 0.0;
    for (double grade : grades) {
        if (grade >= 90) {
            totalGPA += 4.0;
        } else if (grade >= 80) {
            totalGPA += 3.0;
        } else if (grade >= 70) {
            totalGPA += 2.0;
        } else if (grade >= 60) {
            totalGPA += 1.0;
        } else {
            totalGPA += 0.0;
        }
    }
    
    return totalGPA / grades.size();
}

public String getLetterGrade() {
    if (grades.isEmpty()) {
        return "F";
    }
    
    double total = 0.0;
    for (double grade : grades) {
        total += grade;
    }
    double average = total / grades.size();
    
    if (average >= 90) {
        return "A";
    } else if (average >= 80) {
        return "B";
    } else if (average >= 70) {
        return "C";
    } else if (average >= 60) {
        return "D";
    } else {
        return "F";
    }
}
```

**Grading Notes:**
- calculateGPA handles empty list correctly (2 points)
- Correct GPA conversion logic (4 points)
- getLetterGrade calculates average correctly (2 points)
- Correct letter grade assignment (2 points)

---

### Part C Solution (5 points)

```java
import java.util.ArrayList;

public class ClassRoster {
    private ArrayList<Student> students;
    
    public ClassRoster() {
        students = new ArrayList<Student>();
    }
    
    public void addStudent(Student s) {
        students.add(s);
    }
    
    public Student getTopStudent() {
        if (students.isEmpty()) {
            return null;
        }
        
        Student topStudent = students.get(0);
        double highestGPA = topStudent.calculateGPA();
        
        for (int i = 1; i < students.size(); i++) {
            Student current = students.get(i);
            double currentGPA = current.calculateGPA();
            if (currentGPA > highestGPA) {
                highestGPA = currentGPA;
                topStudent = current;
            }
        }
        
        return topStudent;
    }
}
```

**Grading Notes:**
- Constructor initializes ArrayList (1 point)
- addStudent works correctly (1 point)
- getTopStudent handles empty roster (1 point)
- Correct logic to find highest GPA (2 points)

---

## Question 2: Bank Account System - SOLUTION

### Part A Solution (12 points)

```java
public class BankAccount {
    private String accountNumber;
    private double balance;
    private String owner;
    
    // Constructor
    public BankAccount(String accountNumber, String owner) {
        this.accountNumber = accountNumber;
        this.owner = owner;
        this.balance = 0.0;
    }
    
    // Deposit money
    public boolean deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            return true;
        }
        return false;
    }
    
    // Withdraw money
    public boolean withdraw(double amount) {
        if (amount > 0 && balance >= amount) {
            balance -= amount;
            return true;
        }
        return false;
    }
    
    // Getter methods
    public double getBalance() {
        return balance;
    }
    
    public String getAccountNumber() {
        return accountNumber;
    }
    
    public String getOwner() {
        return owner;
    }
}
```

**Grading Notes:**
- Proper instance variables and constructor (3 points)
- deposit validates amount and returns correctly (3 points)
- withdraw checks both amount validity and sufficient funds (4 points)
- Getter methods (2 points)

---

### Part B Solution (8 points)

```java
public class SavingsAccount extends BankAccount {
    private double interestRate;
    
    // Constructor
    public SavingsAccount(String accountNumber, String owner, double interestRate) {
        super(accountNumber, owner);
        this.interestRate = interestRate;
    }
    
    // Apply interest to balance
    public void applyInterest() {
        double currentBalance = getBalance();
        double interest = currentBalance * interestRate;
        deposit(interest);
    }
    
    // Override withdraw to include $2 fee
    @Override
    public boolean withdraw(double amount) {
        double totalNeeded = amount + 2.00;
        if (amount > 0 && getBalance() >= totalNeeded) {
            super.withdraw(totalNeeded);
            return true;
        }
        return false;
    }
}
```

**Grading Notes:**
- Proper use of extends keyword (1 point)
- Constructor calls super correctly (2 points)
- applyInterest calculates and applies interest correctly (2 points)
- Override withdraw with fee logic (3 points)

---

### Part C Solution (5 points)

**Answer:**

1. **Benefit of inheritance:** Having `SavingsAccount` extend `BankAccount` allows code reuse and promotes the "is-a" relationship. The SavingsAccount inherits all the functionality of BankAccount (deposit, withdraw, getters) without duplicating code, and can add specialized behavior (interest rate) or modify existing behavior (withdrawal fee).

2. **Overriding vs Overloading:** 
   - **Overriding** occurs when a subclass provides a specific implementation of a method that is already defined in its parent class (same method signature). Example: SavingsAccount overrides the withdraw method.
   - **Overloading** occurs when multiple methods in the same class have the same name but different parameters (different signatures). Example: having multiple constructors with different parameter lists.

**Grading Notes:**
- Clear explanation of inheritance benefit (2.5 points)
- Correct distinction between overriding and overloading (2.5 points)

---

## Question 3: Library Book Management - SOLUTION

### Part A Solution (10 points)

```java
public class Book {
    private String title;
    private String author;
    private String isbn;
    private boolean isCheckedOut;
    
    // Constructor
    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.isCheckedOut = false;
    }
    
    // Check out the book
    public boolean checkOut() {
        if (!isCheckedOut) {
            isCheckedOut = true;
            return true;
        }
        return false;
    }
    
    // Return the book
    public void returnBook() {
        isCheckedOut = false;
    }
    
    // Getter methods
    public String getTitle() {
        return title;
    }
    
    public String getAuthor() {
        return author;
    }
    
    public String getIsbn() {
        return isbn;
    }
    
    public boolean isCheckedOut() {
        return isCheckedOut;
    }
    
    // toString method
    @Override
    public String toString() {
        return "Title: " + title + ", Author: " + author + 
               ", ISBN: " + isbn + ", Available: " + !isCheckedOut;
    }
}
```

**Grading Notes:**
- Proper constructor initialization (2 points)
- checkOut logic checks availability first (2 points)
- returnBook implementation (1 point)
- All getter methods (2 points)
- toString formatted correctly with @Override (3 points)

---

### Part B Solution (10 points)

```java
import java.util.ArrayList;

public class Library {
    private ArrayList<Book> catalog;
    
    // Constructor
    public Library() {
        catalog = new ArrayList<Book>();
    }
    
    // Add book to catalog
    public void addBook(Book book) {
        catalog.add(book);
    }
    
    // Find book by ISBN
    public Book findBookByISBN(String isbn) {
        for (Book book : catalog) {
            if (book.getIsbn().equals(isbn)) {
                return book;
            }
        }
        return null;
    }
    
    // Get all available books
    public ArrayList<Book> getAvailableBooks() {
        ArrayList<Book> available = new ArrayList<Book>();
        for (Book book : catalog) {
            if (!book.isCheckedOut()) {
                available.add(book);
            }
        }
        return available;
    }
    
    // Check out book by ISBN
    public boolean checkOutBook(String isbn) {
        Book book = findBookByISBN(isbn);
        if (book == null) {
            return false;
        }
        return book.checkOut();
    }
}
```

**Grading Notes:**
- Constructor and addBook (2 points)
- findBookByISBN searches correctly and returns null if not found (2 points)
- getAvailableBooks filters correctly (3 points)
- checkOutBook uses findBookByISBN and handles edge cases (3 points)

---

### Part C Solution (5 points)

```java
public class LibraryTest {
    public static void main(String[] args) {
        // Create a Library
        Library library = new Library();
        
        // Add books to the library
        Book book1 = new Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5");
        Book book2 = new Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4");
        Book book3 = new Book("1984", "George Orwell", "978-0-452-28423-4");
        
        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);
        
        // Check out one book
        System.out.println("Checking out '1984': " + library.checkOutBook("978-0-452-28423-4"));
        
        // Print all available books
        System.out.println("\nAvailable books:");
        ArrayList<Book> availableBooks = library.getAvailableBooks();
        for (Book book : availableBooks) {
            System.out.println(book);
        }
        
        // Attempt to check out the same book again
        System.out.println("\nAttempting to check out '1984' again: " + 
                          library.checkOutBook("978-0-452-28423-4"));
    }
}
```

**Expected Output:**
```
Checking out '1984': true

Available books:
Title: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 978-0-7432-7356-5, Available: true
Title: To Kill a Mockingbird, Author: Harper Lee, ISBN: 978-0-06-112008-4, Available: true

Attempting to check out '1984' again: false
```

**Grading Notes:**
- Creates Library and adds 3+ books (2 points)
- Checks out a book and prints available books (2 points)
- Attempts second checkout and prints result (1 point)

---

## Question 4: Rectangle Class with Comparison - SOLUTION

### Part A Solution (10 points)

```java
public class Rectangle {
    private double length;
    private double width;
    
    // Constructor with validation
    public Rectangle(double length, double width) {
        this.length = (length > 0) ? length : 1.0;
        this.width = (width > 0) ? width : 1.0;
    }
    
    // Getter methods
    public double getLength() {
        return length;
    }
    
    public double getWidth() {
        return width;
    }
    
    // Calculate area
    public double calculateArea() {
        return length * width;
    }
    
    // Calculate perimeter
    public double calculatePerimeter() {
        return 2 * (length + width);
    }
    
    // Check if square
    public boolean isSquare() {
        return length == width;
    }
}
```

**Grading Notes:**
- Constructor validates inputs correctly (3 points)
- Getter methods (1 point)
- calculateArea correct (2 points)
- calculatePerimeter correct (2 points)
- isSquare logic correct (2 points)

---

### Part B Solution (10 points)

```java
// Add these methods to the Rectangle class above

public boolean equals(Rectangle other) {
    if (other == null) {
        return false;
    }
    
    // Check if dimensions match in either order
    return (this.length == other.length && this.width == other.width) ||
           (this.length == other.width && this.width == other.length);
}

public int compareTo(Rectangle other) {
    double thisArea = this.calculateArea();
    double otherArea = other.calculateArea();
    
    if (thisArea < otherArea) {
        return -1;
    } else if (thisArea > otherArea) {
        return 1;
    } else {
        return 0;
    }
}

public boolean scale(double factor) {
    if (factor > 0) {
        this.length *= factor;
        this.width *= factor;
        return true;
    }
    return false;
}
```

**Grading Notes:**
- equals checks both orientations and handles null (4 points)
- compareTo compares areas correctly and returns proper values (3 points)
- scale validates factor and modifies dimensions (3 points)

---

### Part C Solution (5 points)

```java
public class RectangleTest {
    
    public static Rectangle findLargestRectangle(Rectangle[] rectangles) {
        if (rectangles == null || rectangles.length == 0) {
            return null;
        }
        
        Rectangle largest = rectangles[0];
        for (int i = 1; i < rectangles.length; i++) {
            if (rectangles[i].compareTo(largest) > 0) {
                largest = rectangles[i];
            }
        }
        
        return largest;
    }
    
    public static void main(String[] args) {
        // Create test rectangles
        Rectangle rect1 = new Rectangle(5.0, 3.0);
        Rectangle rect2 = new Rectangle(4.0, 4.0);
        Rectangle rect3 = new Rectangle(6.0, 2.0);
        Rectangle rect4 = new Rectangle(3.0, 7.0);
        
        Rectangle[] rectangles = {rect1, rect2, rect3, rect4};
        
        // Find largest rectangle
        Rectangle largest = findLargestRectangle(rectangles);
        
        // Display results
        System.out.println("Testing rectangles:");
        for (int i = 0; i < rectangles.length; i++) {
            System.out.println("Rectangle " + (i+1) + ": " + 
                             rectangles[i].getLength() + " x " + 
                             rectangles[i].getWidth() + 
                             " (Area: " + rectangles[i].calculateArea() + ")");
        }
        
        System.out.println("\nLargest rectangle: " + 
                          largest.getLength() + " x " + 
                          largest.getWidth() + 
                          " (Area: " + largest.calculateArea() + ")");
        
        // Test other methods
        System.out.println("\nTesting equals method:");
        Rectangle rect5 = new Rectangle(3.0, 5.0);
        System.out.println("rect1 (5x3) equals rect5 (3x5): " + rect1.equals(rect5));
        
        System.out.println("\nTesting scale method:");
        rect1.scale(2.0);
        System.out.println("rect1 after scaling by 2: " + 
                          rect1.getLength() + " x " + rect1.getWidth());
    }
}
```

**Expected Output:**
```
Testing rectangles:
Rectangle 1: 5.0 x 3.0 (Area: 15.0)
Rectangle 2: 4.0 x 4.0 (Area: 16.0)
Rectangle 3: 6.0 x 2.0 (Area: 12.0)
Rectangle 4: 3.0 x 7.0 (Area: 21.0)

Largest rectangle: 3.0 x 7.0 (Area: 21.0)

Testing equals method:
rect1 (5x3) equals rect5 (3x5): true

Testing scale method:
rect1 after scaling by 2: 10.0 x 6.0
```

**Grading Notes:**
- findLargestRectangle handles null/empty array (1 point)
- Correctly finds largest using compareTo (2 points)
- Main method creates 4+ rectangles and tests functionality (2 points)

---

## Summary

**Total Points: 100**

**Key Concepts Tested:**
- Class design and encapsulation
- Constructors and instance variables
- Getter and setter methods
- Method implementation and logic
- Inheritance and method overriding
- ArrayLists and iteration
- Object comparison and equals method
- Static methods
- Input validation and edge case handling
- toString method overriding

**Common Mistakes to Avoid:**
1. Forgetting to initialize instance variables in constructor
2. Not validating input parameters
3. Not handling empty collections (returning null or 0)
4. Forgetting to use `super()` in subclass constructors
5. Using `==` instead of `.equals()` for String comparison
6. Not checking for null references before using objects
7. Incorrect access modifiers (using public for instance variables)
8. Forgetting the `@Override` annotation when overriding methods
