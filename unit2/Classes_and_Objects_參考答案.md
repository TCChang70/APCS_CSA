# 📝 Classes and Objects 考題 - 參考答案

## 🎯 第一部分：基礎概念題參考答案 (30分)

### **題目 1：選擇題答案**

1. **B) `class`**
   - 解析：在 Java 中使用 `class` 關鍵字來定義類別

2. **D) 編譯 (Compilation)**
   - 解析：物件導向三大特性為封裝、繼承、多型，編譯不是物件導向特性

3. **B) 建構子名稱必須與類別名稱相同**
   - 解析：建構子沒有回傳型別，名稱必須與類別相同，可以有多個（多載）

4. **D) `private`**
   - 解析：private 提供最嚴格的存取控制，只能在同一個類別內存取

5. **B) `new`**
   - 解析：使用 `new` 關鍵字來建立物件實例

### **題目 2：填空題答案**

```java
public class Student {        // 填空 1: class
    // 私有屬性
    private String name;      // 填空 2: private
    private int age;
    
    // 建構子
    public Student(String n, int a) {
        this.name = n;        // 填空 3: name
        this.age = a;
    }
    
    // Getter 方法
    public String getName() {
        return name;          // 填空 4: name
    }
    
    // Setter 方法
    public void setAge(int newAge) {
        this.age = newAge;    // 填空 5: age
    }
}
```

---

## 💻 第二部分：程式設計題參考答案 (70分)

### **題目 3：銀行帳戶類別完整解答**

```java
public class BankAccount {
    // 私有屬性
    private String accountNumber;
    private String holderName;
    private double balance;
    
    // 建構子
    public BankAccount(String accountNumber, String holderName) {
        this.accountNumber = accountNumber;
        this.holderName = holderName;
        this.balance = 0.0;
    }
    
    // 存款方法
    public boolean deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("存款成功！存入金額：" + amount);
            return true;
        } else {
            System.out.println("存款金額必須大於 0");
            return false;
        }
    }
    
    // 提款方法
    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("提款成功！提取金額：" + amount);
            return true;
        } else if (amount <= 0) {
            System.out.println("提款金額必須大於 0");
            return false;
        } else {
            System.out.println("餘額不足！目前餘額：" + balance);
            return false;
        }
    }
    
    // 查詢餘額
    public double getBalance() {
        return balance;
    }
    
    // 取得帳戶資訊
    public String getAccountInfo() {
        return "帳戶號碼：" + accountNumber + 
               "，持有人：" + holderName + 
               "，餘額：" + balance;
    }
}

// 測試程式
public class TestBankAccount {
    public static void main(String[] args) {
        // 建立帳戶
        BankAccount account = new BankAccount("123456", "張小明");
        
        // 測試存款
        account.deposit(1000);
        System.out.println("存款後餘額：" + account.getBalance());
        
        // 測試提款
        account.withdraw(500);
        System.out.println("提款後餘額：" + account.getBalance());
        
        // 顯示帳戶資訊
        System.out.println(account.getAccountInfo());
    }
}
```

**預期輸出：**
```
存款成功！存入金額：1000.0
存款後餘額：1000.0
提款成功！提取金額：500.0
提款後餘額：500.0
帳戶號碼：123456，持有人：張小明，餘額：500.0
```

### **題目 4：學生成績管理系統完整解答**

```java
// Course 類別
public class Course {
    private String courseCode;
    private String courseName;
    private int credits;
    
    // 建構子
    public Course(String courseCode, String courseName, int credits) {
        this.courseCode = courseCode;
        this.courseName = courseName;
        this.credits = credits;
    }
    
    // 顯示課程資訊
    public String getCourseInfo() {
        return "課程代碼：" + courseCode + 
               "，課程名稱：" + courseName + 
               "，學分數：" + credits;
    }
    
    // Getter 方法
    public String getCourseCode() { return courseCode; }
    public String getCourseName() { return courseName; }
    public int getCredits() { return credits; }
}

// Student 類別
public class Student {
    private String studentId;
    private String name;
    private double[] scores;
    private int scoreCount;
    private static final int MAX_COURSES = 5;
    
    // 建構子
    public Student(String studentId, String name) {
        this.studentId = studentId;
        this.name = name;
        this.scores = new double[MAX_COURSES];
        this.scoreCount = 0;
    }
    
    // 新增成績
    public boolean addScore(double score) {
        if (scoreCount < MAX_COURSES && score >= 0 && score <= 100) {
            scores[scoreCount] = score;
            scoreCount++;
            return true;
        }
        return false;
    }
    
    // 計算平均成績
    public double calculateAverage() {
        if (scoreCount == 0) return 0;
        
        double sum = 0;
        for (int i = 0; i < scoreCount; i++) {
            sum += scores[i];
        }
        return sum / scoreCount;
    }
    
    // 判斷是否及格
    public boolean isPass() {
        return calculateAverage() >= 60;
    }
    
    // 顯示學生資訊
    public String getStudentInfo() {
        return "學號：" + studentId + 
               "，姓名：" + name + 
               "，平均成績：" + String.format("%.2f", calculateAverage()) + 
               "，及格狀態：" + (isPass() ? "及格" : "不及格");
    }
}

// 測試程式
public class TestStudentCourse {
    public static void main(String[] args) {
        // 建立課程
        Course math = new Course("MATH101", "微積分", 3);
        Course prog = new Course("PROG101", "程式設計", 3);
        
        // 建立學生
        Student student = new Student("S001", "李小華");
        
        // 新增成績
        student.addScore(85);  // 微積分
        student.addScore(92);  // 程式設計
        student.addScore(78);  // 其他科目
        
        // 顯示結果
        System.out.println(math.getCourseInfo());
        System.out.println(prog.getCourseInfo());
        System.out.println(student.getStudentInfo());
    }
}
```

### **題目 5：圖書館管理系統完整解答**

```java
import java.util.ArrayList;
import java.util.List;

// Book 類別
public class Book {
    private String isbn;
    private String title;
    private String author;
    private boolean isCheckedOut;
    
    public Book(String isbn, String title, String author) {
        this.isbn = isbn;
        this.title = title;
        this.author = author;
        this.isCheckedOut = false;
    }
    
    // Getter 和 Setter 方法
    public String getIsbn() { return isbn; }
    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    public boolean isCheckedOut() { return isCheckedOut; }
    public void setCheckedOut(boolean checkedOut) { this.isCheckedOut = checkedOut; }
    
    public String getBookInfo() {
        return "ISBN：" + isbn + "，書名：" + title + "，作者：" + author + 
               "，狀態：" + (isCheckedOut ? "已借出" : "可借閱");
    }
}

// Member 類別
public class Member {
    private String memberId;
    private String name;
    private List<Book> borrowedBooks;
    
    public Member(String memberId, String name) {
        this.memberId = memberId;
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }
    
    // 借書
    public boolean borrowBook(Book book) {
        if (!book.isCheckedOut() && borrowedBooks.size() < 5) {  // 限制最多借5本
            borrowedBooks.add(book);
            book.setCheckedOut(true);
            return true;
        }
        return false;
    }
    
    // 還書
    public boolean returnBook(Book book) {
        if (borrowedBooks.remove(book)) {
            book.setCheckedOut(false);
            return true;
        }
        return false;
    }
    
    // 顯示借書記錄
    public void showBorrowedBooks() {
        System.out.println("會員 " + name + " 的借書記錄：");
        if (borrowedBooks.isEmpty()) {
            System.out.println("目前沒有借閱任何書籍");
        } else {
            for (Book book : borrowedBooks) {
                System.out.println("- " + book.getTitle());
            }
        }
    }
    
    public String getMemberId() { return memberId; }
    public String getName() { return name; }
}

// Library 類別
public class Library {
    private List<Book> books;
    private List<Member> members;
    
    public Library() {
        this.books = new ArrayList<>();
        this.members = new ArrayList<>();
    }
    
    // 新增書籍
    public void addBook(Book book) {
        books.add(book);
    }
    
    // 新增會員
    public void addMember(Member member) {
        members.add(member);
    }
    
    // 查詢可借書籍
    public void showAvailableBooks() {
        System.out.println("可借閱書籍：");
        boolean hasAvailable = false;
        for (Book book : books) {
            if (!book.isCheckedOut()) {
                System.out.println("- " + book.getBookInfo());
                hasAvailable = true;
            }
        }
        if (!hasAvailable) {
            System.out.println("目前沒有可借閱的書籍");
        }
    }
    
    // 根據 ISBN 找書
    public Book findBookByIsbn(String isbn) {
        for (Book book : books) {
            if (book.getIsbn().equals(isbn)) {
                return book;
            }
        }
        return null;
    }
    
    // 根據會員 ID 找會員
    public Member findMemberById(String memberId) {
        for (Member member : members) {
            if (member.getMemberId().equals(memberId)) {
                return member;
            }
        }
        return null;
    }
}

// 測試程式
public class TestLibrary {
    public static void main(String[] args) {
        // 建立圖書館
        Library library = new Library();
        
        // 新增書籍
        Book book1 = new Book("978-1234567890", "Java 程式設計", "張三");
        Book book2 = new Book("978-0987654321", "資料結構", "李四");
        library.addBook(book1);
        library.addBook(book2);
        
        // 新增會員
        Member member1 = new Member("M001", "王小明");
        library.addMember(member1);
        
        // 顯示可借書籍
        library.showAvailableBooks();
        
        // 會員借書
        System.out.println("\n=== 借書操作 ===");
        if (member1.borrowBook(book1)) {
            System.out.println("借書成功：" + book1.getTitle());
        }
        
        // 顯示會員借書記錄
        member1.showBorrowedBooks();
        
        // 再次顯示可借書籍
        System.out.println("\n=== 更新後的可借書籍 ===");
        library.showAvailableBooks();
        
        // 會員還書
        System.out.println("\n=== 還書操作 ===");
        if (member1.returnBook(book1)) {
            System.out.println("還書成功：" + book1.getTitle());
        }
        
        // 最終狀態
        member1.showBorrowedBooks();
    }
}
```

---

## 🔍 第三部分：程式碼除錯參考答案 (10分)

### **題目 6：程式錯誤分析與修正**

**錯誤列表：**

1. **錯誤 1：** `public car(String b)` 
   - **問題：** 建構子名稱首字母應大寫，必須與類別名稱完全相同
   - **修正：** `public Car(String b)`

2. **錯誤 2：** `speed =+ increase;`
   - **問題：** 運算子錯誤，`=+` 應該是 `+=`
   - **修正：** `speed += increase;`

3. **錯誤 3：** `private void getSpeed()`
   - **問題：** getter 方法應該是 public 且要有回傳值
   - **修正：** `public int getSpeed()`

4. **錯誤 4：** `myCar.getSpeed()` 無法存取
   - **問題：** getSpeed() 方法是 private，外部無法存取
   - **修正：** 將 getSpeed() 改為 public (已在錯誤 3 修正)

**修正後的完整程式碼：**

```java
public class Car {
    String brand;
    private int speed;
    
    public Car(String b) {  // 修正：建構子名稱大寫
        brand = b;
        speed = 0;
    }
    
    public void accelerate(int increase) {
        speed += increase;  // 修正：使用正確的運算子
    }
    
    public int getSpeed() {  // 修正：改為 public 並加上回傳型別
        return speed;
    }
    
    public String toString() {
        return "品牌：" + brand + "，速度：" + speed;
    }
}

public class TestCar {
    public static void main(String[] args) {
        Car myCar = new Car("Toyota");
        myCar.accelerate(50);
        System.out.println("目前速度：" + myCar.getSpeed());  // 現在可以正常存取
        System.out.println(myCar.toString());  // 額外測試
    }
}
```

**執行結果：**
```
目前速度：50
品牌：Toyota，速度：50
```

---

## 📊 評分標準詳細說明

### **程式設計題評分細節：**

**題目 3 (25分)：**
- 類別架構設計 (5分)：屬性宣告、存取修飾詞正確
- 建構子實作 (5分)：參數處理、初始化正確
- 存款方法 (5分)：輸入驗證、邏輯正確
- 提款方法 (5分)：餘額檢查、邏輯正確
- 其他方法 (5分)：getter、資訊顯示方法

**題目 4 (25分)：**
- Student 類別 (12分)：屬性設計、成績管理、平均計算
- Course 類別 (8分)：屬性設計、資訊顯示
- 整體邏輯 (5分)：方法互動、錯誤處理

**題目 5 (20分)：**
- 三個類別設計 (10分)：屬性合理、方法完整
- 借還書邏輯 (6分)：狀態管理、錯誤處理
- 物件互動 (4分)：類別間的協作關係

---

## 🎯 學習重點提醒

1. **封裝原則**：適當使用 private、public 修飾詞
2. **建構子設計**：參數驗證、初始化完整
3. **方法設計**：單一職責、錯誤處理
4. **物件協作**：類別間的合理互動關係
5. **程式碼品質**：命名規範、註解適當

**總評：此考題涵蓋了 Java 物件導向程式設計的核心概念，從基礎語法到實際應用，能夠全面評估學生的理解程度和實作能力。**