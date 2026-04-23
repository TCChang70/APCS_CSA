# 📝 Classes and Objects 考題

## 🎯 考試說明
- **考試時間**：90 分鐘
- **總分**：100 分
- **考試範圍**：Java 類別與物件程式設計
- **注意事項**：請仔細閱讀題目，程式碼需要完整且可執行

---

## 📚 第一部分：基礎概念題 (30分)

### **題目 1：選擇題 (每題 3 分，共 15 分)**

1. 在 Java 中，下列哪個關鍵字用來定義類別？
   - A) `object`
   - B) `class`
   - C) `method`
   - D) `function`

2. 物件導向程式設計的三大特性不包括下列哪一項？
   - A) 封裝 (Encapsulation)
   - B) 繼承 (Inheritance)
   - C) 多型 (Polymorphism)
   - D) 編譯 (Compilation)

3. 在 Java 中，建構子的特性是什麼？
   - A) 建構子必須有回傳型別
   - B) 建構子名稱必須與類別名稱相同
   - C) 一個類別只能有一個建構子
   - D) 建構子不能有參數

4. 下列哪個存取修飾詞提供最嚴格的存取控制？
   - A) `public`
   - B) `protected`
   - C) `default` (package-private)
   - D) `private`

5. 在 Java 中，使用哪個關鍵字來建立物件實例？
   - A) `create`
   - B) `new`
   - C) `instance`
   - D) `make`

### **題目 2：填空題 (每空 3 分，共 15 分)**

請填入適當的關鍵字或程式碼片段：

```java
public _______ Student {
    // 私有屬性
    _______ String name;
    private int age;
    
    // 建構子
    public Student(String n, int a) {
        this._______ = n;
        this.age = a;
    }
    
    // Getter 方法
    public String getName() {
        return _______;
    }
    
    // Setter 方法
    public void setAge(int newAge) {
        this._______ = newAge;
    }
}
```

---

## 💻 第二部分：程式設計題 (70分)

### **題目 3：設計銀行帳戶類別 (25分)**

設計一個 `BankAccount` 類別，需要滿足以下需求：

**需求規格：**
1. 私有屬性：帳戶號碼 (`accountNumber`)、持有人姓名 (`holderName`)、餘額 (`balance`)
2. 建構子：接受帳戶號碼和持有人姓名，餘額初始為 0
3. 方法：
   - `deposit(double amount)`：存款，金額必須大於 0
   - `withdraw(double amount)`：提款，金額必須大於 0 且不能超過餘額
   - `getBalance()`：查詢餘額
   - `getAccountInfo()`：返回帳戶資訊字串

**評分標準：**
- 類別設計正確 (10分)
- 建構子實作 (5分)
- 存款方法實作 (5分)
- 提款方法實作 (5分)

**程式架構：**
```java
public class BankAccount {
    // 在此處實作您的程式碼
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

### **題目 4：學生成績管理系統 (25分)**

設計一個學生成績管理系統，包含 `Student` 類別和 `Course` 類別：

**Student 類別需求：**
- 屬性：學號、姓名、成績陣列 (最多 5 科)
- 方法：新增成績、計算平均成績、判斷是否及格 (平均 >= 60)

**Course 類別需求：**
- 屬性：課程代碼、課程名稱、學分數
- 方法：顯示課程資訊

**評分標準：**
- Student 類別設計 (12分)
- Course 類別設計 (8分)
- 方法邏輯正確性 (5分)

### **題目 5：進階物件互動 (20分)**

設計一個簡單的圖書館管理系統：

**需求：**
1. `Book` 類別：書籍資訊 (ISBN、書名、作者、是否被借出)
2. `Library` 類別：管理多本書籍
3. `Member` 類別：會員資訊和借書記錄

**功能需求：**
- 會員可以借書和還書
- 圖書館可以查詢可借書籍
- 系統可以顯示會員的借書記錄

**評分標準：**
- 三個類別設計完整 (10分)
- 借還書邏輯正確 (6分)
- 物件間互動適當 (4分)

---

## 🔍 第三部分：程式碼閱讀與除錯 (附加題，10分)

### **題目 6：找出程式錯誤**

下列程式碼有多個錯誤，請找出並說明如何修正：

```java
public class Car {
    String brand;
    private int speed;
    
    public car(String b) {  // 錯誤 1
        brand = b;
        speed = 0;
    }
    
    public void accelerate(int increase) {
        speed =+ increase;  // 錯誤 2
    }
    
    private void getSpeed() {  // 錯誤 3
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
        System.out.println("目前速度：" + myCar.getSpeed());  // 錯誤 4
    }
}
```

請列出所有錯誤並提供正確的程式碼。

---

## 📋 評分標準總覽

| 題目類型 | 分數分配 | 評分重點 |
|---------|---------|----------|
| 基礎概念題 | 30分 | 理論知識掌握程度 |
| 程式設計題 | 70分 | 實作能力與邏輯思維 |
| 附加題 | 10分 | 程式碼閱讀與除錯能力 |

**總分：100分 + 10分附加題**

**及格標準：60分**

---

## ⏰ 時間分配建議

- 基礎概念題：20 分鐘
- 程式設計題 3：25 分鐘
- 程式設計題 4：25 分鐘
- 程式設計題 5：20 分鐘
- 檢查與附加題：剩餘時間

---

## 📖 參考答案與解析

> **注意：**參考答案請另外提供，此處僅為考題內容。

**祝考試順利！** 🍀