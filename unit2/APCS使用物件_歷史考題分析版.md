# 📝 APCS 使用物件單元考題 - 歷史考題分析版

## 🎯 考試說明
- **考試範圍**：使用物件 (11個課程) - 類別、物件、字串、Math類別
- **考試時間**：120 分鐘
- **總分**：110 分 (包含10分加分題)
- **考試特色**：基於APCS五年歷史考題分析，強調實用性程式設計
- **評量目標**：物件導向思維、字串處理能力、數學運算應用、系統設計思考

---

## 🏆 **第一部分：物件概念深度分析 (30分)**

### **💡 題目群 A：物件設計哲學 (每題3分，共15分)**

**1.** 在設計一個「學生成績管理系統」時，下列哪種物件設計最符合APCS實用性原則？
```java
// 選項 A
class Student {
    public String name;
    public int score;
}

// 選項 B  
class Student {
    private String name;
    private ArrayList<Integer> scores;
    private double gpa;
    
    public void addScore(int score) { /* 實作 */ }
    public double calculateGPA() { /* 實作 */ }
}

// 選項 C
class Student {
    String studentData;
    void processData(String input) { /* 實作 */ }
}

// 選項 D
class Student {
    static String allStudents = "";
    static void addStudent(String name) { /* 實作 */ }
}
```
- A) 選項 A - 簡單直接的資料結構
- B) 選項 B - 完整的封裝和功能設計
- C) 選項 C - 彈性的字串處理方式
- D) 選項 D - 靜態方法的統一管理

**2.** 在APCS考題中，字串比較經常出現的陷阱情境是：
```java
String password1 = "apcs2024";
String password2 = new String("apcs2024");
String password3 = "apcs" + "2024";

// 下列比較結果的組合何者正確？
boolean result1 = (password1 == password2);
boolean result2 = (password1 == password3);  
boolean result3 = password1.equals(password2);
```
- A) `false, false, true`
- B) `false, true, true`
- C) `true, true, true`
- D) `true, false, false`

**3.** 根據APCS歷史考題分析，下列哪個Math類別方法組合最常出現在「科學計算器」類型題目中？
- A) `Math.pow()`, `Math.sqrt()`, `Math.sin()`
- B) `Math.random()`, `Math.round()`, `Math.max()`
- C) `Math.abs()`, `Math.floor()`, `Math.PI`
- D) `Math.log()`, `Math.exp()`, `Math.ceil()`

**4.** 在APCS實作題中，處理「使用者輸入驗證」時，最佳的字串方法組合是：
```java
public boolean validateInput(String input) {
    // 請選擇最適合的實作方式
}
```
- A) `input != null && input.length() > 0`
- B) `input.trim().isEmpty() == false`  
- C) `input != null && !input.trim().isEmpty()`
- D) `input.equals("") == false`

**5.** 基於APCS考題模式，下列哪種方法設計最符合「可重用性」原則？
```java
// 計算學生平均分數的方法設計
```
- A) `public static void calculateAverage() { /* 固定處理特定陣列 */ }`
- B) `public double getAverage(ArrayList<Integer> scores)`
- C) `public void printAverage(int[] scores) { /* 直接輸出 */ }`
- D) `public String averageReport() { /* 回傳格式化字串 */ }`

### **🔍 題目群 B：程式碼邏輯分析 (每題3分，共15分)**

**6.** 分析下列程式碼，預測輸出結果：
```java
public class StringAnalyzer {
    public static void main(String[] args) {
        String text = "APCS Programming Contest";
        
        // 步驟1：提取關鍵字
        String keyword = text.substring(5, 16);
        
        // 步驟2：轉換處理
        String processed = keyword.toLowerCase().replace("m", "M");
        
        // 步驟3：計算統計
        int count = 0;
        for (int i = 0; i < processed.length(); i++) {
            if (Character.isUpperCase(processed.charAt(i))) {
                count++;
            }
        }
        
        System.out.println(processed + " : " + count);
    }
}
```
- A) `prograMMing : 2`
- B) `programMing : 1` 
- C) `prograMMing : 3`
- D) `Programming : 1`

**7.** 根據APCS數學應用題模式，分析此程式的功能：
```java
public class MathProcessor {
    public static double process(double x, double y) {
        double step1 = Math.pow(x, 2) + Math.pow(y, 2);
        double step2 = Math.sqrt(step1);
        double step3 = Math.round(step2 * 100.0) / 100.0;
        return step3;
    }
}
```
當呼叫 `process(3.0, 4.0)` 時，回傳值是：
- A) `5.0`
- B) `5.00`  
- C) `25.0`
- D) `7.0`

**8.** 在APCS字串處理題型中，下列程式碼的功能是：
```java
public static String mysteryMethod(String input) {
    StringBuilder result = new StringBuilder();
    
    for (int i = 0; i < input.length(); i++) {
        char current = input.charAt(i);
        if (Character.isLetter(current)) {
            if (Character.isUpperCase(current)) {
                result.append(Character.toLowerCase(current));
            } else {
                result.append(Character.toUpperCase(current));
            }
        } else {
            result.append(current);
        }
    }
    
    return result.toString();
}
```
對輸入 `"Hello World!"` 的處理結果是：
- A) `"hello world!"`
- B) `"HELLO WORLD!"`
- C) `"hELLO wORLD!"`
- D) `"HeLLo WoRLd!"`

**9.** 分析這個APCS典型的「資料統計」程式片段：
```java
ArrayList<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");  
names.add("Charlie");
names.add("Alice");

// 統計程式碼
int count = 0;
String target = "Alice";
for (String name : names) {
    if (name.equals(target)) {
        count++;
    }
}
```
變數 `count` 的最終值是：
- A) `1`
- B) `2`
- C) `3` 
- D) `4`

**10.** 根據APCS考題邏輯，判斷此程式的錯誤：
```java
public class Calculator {
    public double divide(double a, double b) {
        return a / b;  // 第1行
    }
    
    public String formatResult(Double result) {
        return "結果: " + result.toString();  // 第2行
    }
    
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        double result = calc.divide(10.0, 0.0);  // 第3行
        String output = calc.formatResult(result);  // 第4行
        System.out.println(output);
    }
}
```
最可能造成問題的是：
- A) 第1行 - 除法運算語法錯誤
- B) 第2行 - 包裝類別使用錯誤
- C) 第3行 - 除零操作未處理
- D) 第4行 - 方法呼叫語法錯誤

---

## 🚀 **第二部分：實務程式設計 (70分)**

### **📊 題目 11：智慧文字分析系統 (25分)**

設計一個文字分析系統，模擬APCS實際應用情境。

**系統需求：**
1. **文字統計功能** - 分析文章的基本統計資訊
2. **關鍵字搜尋** - 提供智慧搜尋和高亮顯示
3. **格式化輸出** - 生成專業的分析報告

**核心功能規格：**

```java
public class TextAnalyzer {
    private String content;
    private Map<String, Integer> wordCount;
    
    // 建構子：初始化分析器
    public TextAnalyzer(String text) {
        // TODO: 實作內容初始化和預處理
    }
    
    // 方法1：基本統計 (8分)
    public String getBasicStats() {
        // 計算並回傳：字元數、單字數、行數、段落數
        // 格式："字元: X | 單字: Y | 行數: Z | 段落: W"
    }
    
    // 方法2：單字頻率分析 (10分)
    public Map<String, Integer> analyzeWordFrequency() {
        // 分析每個單字出現次數（忽略大小寫和標點符號）
        // 回傳排序後的單字頻率對應表
    }
    
    // 方法3：搜尋功能 (7分)
    public String searchAndHighlight(String keyword) {
        // 搜尋關鍵字並用 [關鍵字] 格式標記
        // 不區分大小寫，回傳標記後的完整文字
    }
}
```

**測試用例：**
```java
String sampleText = "APCS程式設計競賽是培養程式設計能力的重要競賽。\n" +
                   "透過APCS，學生可以提升邏輯思考和程式設計技巧。\n" +
                   "程式設計不僅是技術，更是解決問題的藝術。";

TextAnalyzer analyzer = new TextAnalyzer(sampleText);

// 預期輸出範例
System.out.println(analyzer.getBasicStats());
// 輸出：字元: 67 | 單字: 23 | 行數: 3 | 段落: 1

Map<String, Integer> frequency = analyzer.analyzeWordFrequency();
// 預期：程式設計=3, APCS=2, 競賽=2, 等等...

String highlighted = analyzer.searchAndHighlight("程式設計");
// 預期：將所有"程式設計"標記為"[程式設計]"
```

### **🔢 題目 12：科學計算引擎 (20分)**

基於APCS歷史考題中的數學應用模式，實作一個科學計算引擎。

**引擎規格：**
```java
public class ScientificCalculator {
    private List<Double> history;
    private boolean isRadianMode;
    
    // 建構子 (2分)
    public ScientificCalculator() {
        // 初始化歷史記錄和角度模式（預設為度數）
    }
    
    // 基本數學運算 (6分)
    public double calculate(String operation, double... operands) {
        // 支援運算：add, subtract, multiply, divide, power, sqrt
        // 將結果加入歷史記錄並回傳
        // 處理除零和負數開根號等例外情況
    }
    
    // 進階數學函數 (8分)
    public double advancedFunction(String function, double value) {
        // 支援函數：sin, cos, tan, log, ln, abs, ceil, floor
        // 三角函數需考慮角度模式（度數/弧度）
        // 對數函數需處理非正數輸入
    }
    
    // 統計與分析 (4分)
    public String getCalculationSummary() {
        // 回傳計算歷史的統計資訊
        // 包含：總計算次數、最大值、最小值、平均值、標準差
    }
}
```

**實作要求：**
1. **例外處理**：所有數學錯誤都必須適當處理
2. **精確度**：計算結果保留到小數點後4位
3. **模式切換**：提供度數/弧度模式切換功能
4. **歷史管理**：維護最近50筆計算記錄

**測試情境：**
```java
ScientificCalculator calc = new ScientificCalculator();

// 基本運算測試
double result1 = calc.calculate("power", 2.0, 3.0);  // 8.0
double result2 = calc.calculate("sqrt", 16.0);       // 4.0

// 進階函數測試
double result3 = calc.advancedFunction("sin", 90.0); // 1.0 (度數模式)
double result4 = calc.advancedFunction("log", 100.0); // 2.0

// 統計報告
String summary = calc.getCalculationSummary();
```

### **🎮 題目 13：遊戲角色管理系統 (25分)**

設計一個RPG遊戲的角色管理系統，展現完整的物件導向設計能力。

**系統架構：**
```java
// 角色類別 (15分)
public class GameCharacter {
    private String name;
    private int level;
    private int health;
    private int maxHealth;
    private int experience;
    private List<String> skills;
    
    // 建構子 (3分)
    public GameCharacter(String name) {
        // 初始化新角色：等級1，血量100，經驗值0，基本技能
    }
    
    // 戰鬥系統 (5分)
    public String battle(GameCharacter opponent) {
        // 實作戰鬥邏輯：
        // 1. 計算傷害值（基於等級和隨機因子）
        // 2. 更新雙方血量
        // 3. 判斷戰鬥結果
        // 4. 勝利者獲得經驗值
        // 回傳戰鬥報告
    }
    
    // 升級系統 (4分)
    public boolean levelUp() {
        // 檢查經驗值是否足夠升級（需要 level * 100 經驗值）
        // 升級時：等級+1，最大血量+20，學習新技能
        // 回傳是否成功升級
    }
    
    // 角色狀態 (3分)
    public String getStatus() {
        // 回傳完整的角色資訊，包括：
        // 姓名、等級、血量、經驗值、技能列表
    }
}

// 遊戲管理系統 (10分)
public class GameManager {
    private List<GameCharacter> characters;
    private String battleLog;
    
    // 角色管理 (5分)
    public void createCharacter(String name) { }
    public GameCharacter findCharacter(String name) { }
    public void removeCharacter(String name) { }
    
    // 戰鬥安排 (3分)
    public String arrangeBattle(String player1, String player2) {
        // 安排兩個角色戰鬥，更新戰鬥記錄
    }
    
    // 排行榜系統 (2分)
    public List<GameCharacter> getLeaderboard() {
        // 按等級和經驗值排序回傳角色列表
    }
}
```

**特殊功能需求：**
1. **技能系統**：每5級學會新技能，技能影響戰鬥力
2. **平衡機制**：高等級角色對低等級有優勢，但有機率逆轉
3. **持久化**：角色資料需要能夠序列化為字串格式
4. **統計功能**：追蹤勝率、總戰鬥次數等統計資料

---

## 🔧 **第三部分：程式碼最佳化與分析 (10分)**

### **⚡ 題目 14：效能分析與最佳化 (10分)**

分析下列三個版本的字串處理程式，並回答相關問題：

**版本 A：基礎實作**
```java
public String processText(List<String> words) {
    String result = "";
    for (String word : words) {
        result = result + word.toUpperCase() + " ";
    }
    return result.trim();
}
```

**版本 B：StringBuilder 最佳化**
```java
public String processText(List<String> words) {
    StringBuilder sb = new StringBuilder();
    for (String word : words) {
        sb.append(word.toUpperCase()).append(" ");
    }
    return sb.toString().trim();
}
```

**版本 C：串流處理**
```java
public String processText(List<String> words) {
    return words.stream()
                .map(String::toUpperCase)
                .collect(Collectors.joining(" "));
}
```

**分析問題：**

**14.1** (3分) 當處理1000個單字時，哪個版本的效能最佳？說明原因。

**14.2** (3分) 版本A有什麼效能問題？從記憶體使用角度分析。

**14.3** (2分) 在APCS競賽環境中，推薦使用哪個版本？考慮程式碼可讀性和執行效率。

**14.4** (2分) 如果要在版本B的基礎上增加「過濾空字串」功能，如何修改最有效率？

---

## 🏅 **加分題：創新應用設計 (10分)**

### **🌟 題目 15：APCS 智慧助教系統 (10分)**

設計一個「APCS智慧助教」程式，幫助學生分析和改進程式碼。

**系統功能需求：**
1. **程式碼風格檢查** - 分析變數命名、縮排、註解
2. **邏輯錯誤偵測** - 識別常見的程式邏輯問題  
3. **效能建議** - 提供程式最佳化建議
4. **學習進度追蹤** - 記錄學生的程式設計進步情況

**核心介面設計：**
```java
public class APCSMentor {
    // 程式碼分析 (4分)
    public AnalysisReport analyzeCode(String sourceCode) {
        // 分析程式碼並回傳詳細報告
    }
    
    // 建議生成 (3分) 
    public List<Suggestion> generateSuggestions(AnalysisReport report) {
        // 基於分析結果提供改進建議
    }
    
    // 學習追蹤 (3分)
    public LearningProgress trackProgress(String studentId, 
                                        List<String> submittedCodes) {
        // 分析學生的程式設計能力發展軌跡
    }
}
```

**評分重點：**
- **創新性** (4分)：演算法設計的獨創性
- **實用性** (3分)：功能對APCS學習的實際幫助
- **技術深度** (3分)：程式設計技巧的運用程度

---

## 📋 **評分標準與學習指導**

### **📊 分數分佈**
- **概念分析** (30分)：深度理解物件導向思維
- **實務設計** (70分)：完整的系統開發能力
- **創新加分** (10分)：超越基本要求的創新思考

### **🎯 APCS 成功策略**
1. **重視實用性**：所有程式都要能解決實際問題
2. **注重效率**：考慮時間和空間複雜度
3. **完整測試**：考慮邊界條件和例外情況
4. **清晰設計**：程式架構要易於理解和維護

### **⭐ 高分技巧**
- 熟練運用 String、Math、ArrayList 等核心類別
- 掌握物件導向設計原則（封裝、繼承、多型）
- 具備系統性思考能力，能設計複雜的程式架構
- 注意程式碼品質，包括命名、註解、錯誤處理

---

**考試時間：120分鐘 | 總分：110分**
**建議答題時間分配：概念題 30分鐘、設計題 80分鐘、加分題 10分鐘**

> 本考題基於APCS五年歷史考題模式分析製作，強調實務應用和系統性思考，旨在培養學生的程式設計綜合能力。