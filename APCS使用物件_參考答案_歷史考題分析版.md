# 📝 APCS 使用物件單元參考答案 - 歷史考題分析版

## 🎯 答案總覽與評分說明

本參考答案基於APCS五年歷史考題模式，提供詳細的解題思路和程式實作，幫助學生深入理解物件導向程式設計的核心概念和實際應用。

---

## 🏆 **第一部分：物件概念深度分析答案 (30分)**

### **💡 題目群 A：物件設計哲學答案 (每題3分，共15分)**

**1. 答案：B** - 選項 B - 完整的封裝和功能設計

**詳細解析：**
- **為何選B**：APCS強調實用性設計，選項B展現了完整的物件導向原則
  - 私有屬性保護資料安全性
  - 多科目成績管理符合實際需求
  - 提供計算GPA等實用功能
  - 符合封裝原則的完整設計

- **其他選項問題**：
  - A：公開屬性缺乏封裝性，只能處理單一成績
  - C：過於抽象，缺乏明確的資料結構
  - D：靜態設計限制了物件使用的彈性

**APCS出題邏輯**：考查學生對實用系統設計的理解能力

**2. 答案：B** - `false, true, true`

**詳細解析：**
```java
String password1 = "apcs2024";           // 字串常量池
String password2 = new String("apcs2024"); // 堆疊記憶體新物件  
String password3 = "apcs" + "2024";      // 編譯時常量摺疊

// 分析每個比較：
boolean result1 = (password1 == password2);  // false - 不同記憶體位址
boolean result2 = (password1 == password3);  // true - 同一常量池物件
boolean result3 = password1.equals(password2); // true - 內容相同
```

**APCS重點**：理解字串常量池與new關鍵字的記憶體配置差異

**3. 答案：A** - `Math.pow()`, `Math.sqrt()`, `Math.sin()`

**APCS歷史分析**：
- 科學計算器題型在APCS中頻繁出現
- `Math.pow()` - 乘方運算（工程計算核心）
- `Math.sqrt()` - 平方根（幾何問題常用）
- `Math.sin()` - 三角函數（物理模擬必備）

**出題趨勢**：結合實際應用情境，而非單純數學運算

**4. 答案：C** - `input != null && !input.trim().isEmpty()`

**最佳實作原理**：
```java
public boolean validateInput(String input) {
    return input != null && !input.trim().isEmpty();
}
```

**安全檢查順序**：
1. 先檢查 `null` 避免 NullPointerException
2. 使用 `trim()` 移除前後空白字元
3. 檢查是否為空字串

**APCS強調**：程式的健壯性和例外處理能力

**5. 答案：B** - `public double getAverage(ArrayList<Integer> scores)`

**可重用性原則**：
- **參數化設計**：接受任何成績列表作為參數
- **純函數特性**：不依賴外部狀態，結果可預測
- **型別安全**：使用泛型確保型別正確性
- **功能單一**：專注於計算平均值的核心邏輯

### **🔍 題目群 B：程式碼邏輯分析答案 (每題3分，共15分)**

**6. 答案：A** - `prograMMing : 2`

**逐步解析：**
```java
String text = "APCS Programming Contest";

// 步驟1：提取關鍵字 
String keyword = text.substring(5, 16); // "Programming"

// 步驟2：轉換處理
String processed = keyword.toLowerCase().replace("m", "M");
// "programming" -> "prograMMing"

// 步驟3：計算大寫字母數量
int count = 0;
// 'M' 在索引 7 和 8，共 2 個大寫字母
```

**APCS技巧**：字串處理的連鎖操作和字元統計

**7. 答案：A** - `5.0`

**數學運算分析：**
```java
public static double process(double x, double y) {
    double step1 = Math.pow(x, 2) + Math.pow(y, 2); // 3² + 4² = 25
    double step2 = Math.sqrt(step1);                 // √25 = 5.0
    double step3 = Math.round(step2 * 100.0) / 100.0; // 四捨五入到小數點後2位
    return step3; // 5.0
}
```

**功能識別**：計算兩點之間的歐幾里德距離（勾股定理）

**8. 答案：C** - `"hELLO wORLD!"`

**字元轉換邏輯：**
```java
// 對每個字元進行大小寫互換
// 'H' -> 'h', 'e' -> 'E', 'l' -> 'L', 等等
// 非字母字元保持不變（空格和驚嘆號）
```

**APCS模式**：字元級別的條件判斷和轉換操作

**9. 答案：B** - `2`

**ArrayList 操作分析：**
```java
ArrayList<String> names = ["Alice", "Bob", "Charlie", "Alice"];
// "Alice" 在索引 0 和 3，共出現 2 次
```

**重點**：增強型for迴圈的使用和字串比較

**10. 答案：C** - 第3行 - 除零操作未處理

**問題分析：**
```java
double result = calc.divide(10.0, 0.0); // 除零會產生 Infinity
```

**APCS重視**：
- 數學運算的邊界條件處理
- 例外情況的預防性程式設計
- 雖然Java不會拋出例外，但Infinity值會影響後續計算

---

## 🚀 **第二部分：實務程式設計答案 (70分)**

### **📊 題目 11：智慧文字分析系統答案 (25分)**

```java
import java.util.*;
import java.util.stream.Collectors;

public class TextAnalyzer {
    private String content;
    private Map<String, Integer> wordCount;
    
    // 建構子：初始化分析器
    public TextAnalyzer(String text) {
        this.content = text != null ? text : "";
        this.wordCount = new HashMap<>();
        preprocessText();
    }
    
    // 預處理文字
    private void preprocessText() {
        if (content.isEmpty()) return;
        
        // 將文字轉換為單字並統計頻率
        String[] words = content.toLowerCase()
                               .replaceAll("[^\\u4e00-\\u9fa5a-zA-Z0-9\\s]", " ")
                               .split("\\s+");
        
        for (String word : words) {
            if (!word.isEmpty()) {
                wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
            }
        }
    }
    
    // 方法1：基本統計 (8分)
    public String getBasicStats() {
        if (content.isEmpty()) return "字元: 0 | 單字: 0 | 行數: 0 | 段落: 0";
        
        // 字元數（包含空白）
        int charCount = content.length();
        
        // 單字數（所有有效單字）
        int wordTotal = wordCount.values().stream().mapToInt(Integer::intValue).sum();
        
        // 行數（以換行符分割）
        int lineCount = content.split("\n", -1).length;
        
        // 段落數（以空行分割的文字區塊）
        String[] paragraphs = content.trim().split("\n\\s*\n");
        int paragraphCount = paragraphs.length == 1 && paragraphs[0].isEmpty() ? 0 : paragraphs.length;
        
        return String.format("字元: %d | 單字: %d | 行數: %d | 段落: %d", 
                           charCount, wordTotal, lineCount, paragraphCount);
    }
    
    // 方法2：單字頻率分析 (10分)
    public Map<String, Integer> analyzeWordFrequency() {
        // 按頻率降序排列，頻率相同時按字典序
        return wordCount.entrySet().stream()
                       .sorted(Map.Entry.<String, Integer>comparingByValue().reversed()
                              .thenComparing(Map.Entry.comparingByKey()))
                       .collect(Collectors.toLinkedHashMap(
                           Map.Entry::getKey, 
                           Map.Entry::getValue,
                           (e1, e2) -> e1,
                           LinkedHashMap::new));
    }
    
    // 方法3：搜尋功能 (7分)
    public String searchAndHighlight(String keyword) {
        if (keyword == null || keyword.isEmpty()) return content;
        
        // 使用正規表示式進行不區分大小寫的替換
        String pattern = "(?i)" + Pattern.quote(keyword);
        String replacement = "[" + keyword + "]";
        
        return content.replaceAll(pattern, replacement);
    }
    
    // 額外功能：獲取最常見單字 (加分功能)
    public List<String> getTopWords(int count) {
        return analyzeWordFrequency().entrySet().stream()
                                    .limit(count)
                                    .map(Map.Entry::getKey)
                                    .collect(Collectors.toList());
    }
}
```

**評分標準：**
- **建構子設計** (2分)：正確初始化和空值處理
- **基本統計** (8分)：準確計算各項統計指標
- **頻率分析** (10分)：正確統計和排序邏輯
- **搜尋標記** (5分)：不區分大小寫的搜尋和替換

### **🔢 題目 12：科學計算引擎答案 (20分)**

```java
import java.util.*;

public class ScientificCalculator {
    private List<Double> history;
    private boolean isRadianMode;
    private static final int MAX_HISTORY = 50;
    
    // 建構子 (2分)
    public ScientificCalculator() {
        this.history = new ArrayList<>();
        this.isRadianMode = false; // 預設為度數模式
    }
    
    // 角度模式切換
    public void setRadianMode(boolean radianMode) {
        this.isRadianMode = radianMode;
    }
    
    // 基本數學運算 (6分)
    public double calculate(String operation, double... operands) {
        if (operands.length == 0) {
            throw new IllegalArgumentException("至少需要一個運算元");
        }
        
        double result = 0.0;
        
        switch (operation.toLowerCase()) {
            case "add":
                result = Arrays.stream(operands).sum();
                break;
                
            case "subtract":
                if (operands.length < 2) throw new IllegalArgumentException("減法需要兩個運算元");
                result = operands[0] - operands[1];
                break;
                
            case "multiply":
                result = Arrays.stream(operands).reduce(1.0, (a, b) -> a * b);
                break;
                
            case "divide":
                if (operands.length < 2) throw new IllegalArgumentException("除法需要兩個運算元");
                if (operands[1] == 0) throw new ArithmeticException("除數不能為零");
                result = operands[0] / operands[1];
                break;
                
            case "power":
                if (operands.length < 2) throw new IllegalArgumentException("乘方需要兩個運算元");
                result = Math.pow(operands[0], operands[1]);
                break;
                
            case "sqrt":
                if (operands[0] < 0) throw new ArithmeticException("無法計算負數的平方根");
                result = Math.sqrt(operands[0]);
                break;
                
            default:
                throw new IllegalArgumentException("不支援的運算：" + operation);
        }
        
        // 四捨五入到小數點後4位
        result = Math.round(result * 10000.0) / 10000.0;
        
        // 加入歷史記錄
        addToHistory(result);
        
        return result;
    }
    
    // 進階數學函數 (8分)
    public double advancedFunction(String function, double value) {
        double result = 0.0;
        
        switch (function.toLowerCase()) {
            case "sin":
                double sinValue = isRadianMode ? value : Math.toRadians(value);
                result = Math.sin(sinValue);
                break;
                
            case "cos":
                double cosValue = isRadianMode ? value : Math.toRadians(value);
                result = Math.cos(cosValue);
                break;
                
            case "tan":
                double tanValue = isRadianMode ? value : Math.toRadians(value);
                result = Math.tan(tanValue);
                break;
                
            case "log":
                if (value <= 0) throw new ArithmeticException("對數的真數必須大於0");
                result = Math.log10(value);
                break;
                
            case "ln":
                if (value <= 0) throw new ArithmeticException("自然對數的真數必須大於0");
                result = Math.log(value);
                break;
                
            case "abs":
                result = Math.abs(value);
                break;
                
            case "ceil":
                result = Math.ceil(value);
                break;
                
            case "floor":
                result = Math.floor(value);
                break;
                
            default:
                throw new IllegalArgumentException("不支援的函數：" + function);
        }
        
        // 四捨五入到小數點後4位
        result = Math.round(result * 10000.0) / 10000.0;
        
        // 加入歷史記錄
        addToHistory(result);
        
        return result;
    }
    
    // 歷史記錄管理
    private void addToHistory(double value) {
        history.add(value);
        // 維護最多50筆記錄
        if (history.size() > MAX_HISTORY) {
            history.remove(0);
        }
    }
    
    // 統計與分析 (4分)
    public String getCalculationSummary() {
        if (history.isEmpty()) {
            return "尚無計算記錄";
        }
        
        int count = history.size();
        double max = Collections.max(history);
        double min = Collections.min(history);
        double average = history.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
        
        // 計算標準差
        double variance = history.stream()
                                .mapToDouble(x -> Math.pow(x - average, 2))
                                .average().orElse(0.0);
        double standardDeviation = Math.sqrt(variance);
        
        return String.format(
            "計算統計摘要:\n" +
            "總計算次數: %d\n" +
            "最大值: %.4f\n" +
            "最小值: %.4f\n" +
            "平均值: %.4f\n" +
            "標準差: %.4f\n" +
            "角度模式: %s",
            count, max, min, average, standardDeviation,
            isRadianMode ? "弧度" : "度數"
        );
    }
    
    // 清除歷史記錄
    public void clearHistory() {
        history.clear();
    }
    
    // 獲取計算歷史
    public List<Double> getHistory() {
        return new ArrayList<>(history);
    }
}
```

**測試驗證：**
```java
public class CalculatorTest {
    public static void main(String[] args) {
        ScientificCalculator calc = new ScientificCalculator();
        
        // 基本運算測試
        System.out.println("Power: " + calc.calculate("power", 2.0, 3.0)); // 8.0000
        System.out.println("Sqrt: " + calc.calculate("sqrt", 16.0));       // 4.0000
        
        // 進階函數測試  
        System.out.println("Sin 90°: " + calc.advancedFunction("sin", 90.0)); // 1.0000
        System.out.println("Log 100: " + calc.advancedFunction("log", 100.0)); // 2.0000
        
        // 統計報告
        System.out.println("\n" + calc.getCalculationSummary());
    }
}
```

### **🎮 題目 13：遊戲角色管理系統答案 (25分)**

```java
import java.util.*;

// 角色類別 (15分)
public class GameCharacter {
    private String name;
    private int level;
    private int health;
    private int maxHealth;
    private int experience;
    private List<String> skills;
    private int totalBattles;
    private int victories;
    
    // 基本技能池
    private static final String[] SKILL_POOL = {
        "基礎攻擊", "防禦姿態", "快速移動", "集中精神", "強力打擊",
        "魔法護盾", "治療術", "火球術", "冰凍術", "雷電術",
        "隱身術", "狂暴", "反擊", "致命一擊", "復活術"
    };
    
    // 建構子 (3分)
    public GameCharacter(String name) {
        this.name = name;
        this.level = 1;
        this.health = 100;
        this.maxHealth = 100;
        this.experience = 0;
        this.skills = new ArrayList<>();
        this.totalBattles = 0;
        this.victories = 0;
        
        // 初始技能
        skills.add("基礎攻擊");
        skills.add("防禦姿態");
    }
    
    // 戰鬥系統 (5分)
    public String battle(GameCharacter opponent) {
        if (this.health <= 0 || opponent.health <= 0) {
            return "戰鬥失敗：參與者血量不足";
        }
        
        StringBuilder battleReport = new StringBuilder();
        battleReport.append(String.format("=== %s VS %s ===\n", this.name, opponent.name));
        
        Random random = new Random();
        int rounds = 0;
        int maxRounds = 10; // 防止無限戰鬥
        
        while (this.health > 0 && opponent.health > 0 && rounds < maxRounds) {
            rounds++;
            
            // 計算攻擊力（基於等級和隨機因子）
            int myAttack = calculateDamage(this, random);
            int opponentAttack = calculateDamage(opponent, random);
            
            // 應用傷害
            opponent.health = Math.max(0, opponent.health - myAttack);
            this.health = Math.max(0, this.health - opponentAttack);
            
            battleReport.append(String.format("第%d回合: %s造成%d傷害，%s造成%d傷害\n",
                rounds, this.name, myAttack, opponent.name, opponentAttack));
            
            if (opponent.health <= 0 || this.health <= 0) break;
        }
        
        // 判定勝負和獎勵
        GameCharacter winner = null;
        GameCharacter loser = null;
        
        if (this.health > opponent.health) {
            winner = this;
            loser = opponent;
            this.victories++;
        } else if (opponent.health > this.health) {
            winner = opponent;
            loser = this;
            opponent.victories++;
        }
        
        this.totalBattles++;
        opponent.totalBattles++;
        
        if (winner != null) {
            int expGain = Math.max(10, loser.level * 15);
            winner.experience += expGain;
            battleReport.append(String.format("\n🏆 勝利者：%s (獲得 %d 經驗值)\n", 
                winner.name, expGain));
            
            // 檢查是否升級
            if (winner.checkAndLevelUp()) {
                battleReport.append(String.format("🌟 %s 升級了！現在是 %d 級\n", 
                    winner.name, winner.level));
            }
        } else {
            battleReport.append("\n⚖️ 戰鬥平手！\n");
        }
        
        return battleReport.toString();
    }
    
    // 計算戰鬥傷害
    private int calculateDamage(GameCharacter character, Random random) {
        int baseDamage = character.level * 10;
        int skillBonus = character.skills.size() * 2;
        int randomFactor = random.nextInt(20) - 10; // -10 到 +10 的隨機值
        
        return Math.max(1, baseDamage + skillBonus + randomFactor);
    }
    
    // 升級系統 (4分)  
    public boolean levelUp() {
        return checkAndLevelUp();
    }
    
    private boolean checkAndLevelUp() {
        int requiredExp = level * 100;
        
        if (experience >= requiredExp) {
            level++;
            maxHealth += 20;
            health = maxHealth; // 升級時完全恢復
            experience -= requiredExp; // 扣除消耗的經驗值
            
            // 每5級學習新技能
            if (level % 5 == 0 && skills.size() < SKILL_POOL.length) {
                learnNewSkill();
            }
            
            return true;
        }
        
        return false;
    }
    
    // 學習新技能
    private void learnNewSkill() {
        Random random = new Random();
        for (int attempts = 0; attempts < 10; attempts++) {
            String newSkill = SKILL_POOL[random.nextInt(SKILL_POOL.length)];
            if (!skills.contains(newSkill)) {
                skills.add(newSkill);
                break;
            }
        }
    }
    
    // 角色狀態 (3分)
    public String getStatus() {
        double winRate = totalBattles > 0 ? (double) victories / totalBattles * 100 : 0.0;
        
        return String.format(
            "📊 角色狀態 📊\n" +
            "姓名: %s\n" +
            "等級: %d\n" +
            "血量: %d/%d\n" +
            "經驗值: %d/%d\n" +
            "技能: %s\n" +
            "戰鬥統計: %d勝/%d戰 (勝率: %.1f%%)\n" +
            "戰力評估: %s",
            name, level, health, maxHealth, experience, level * 100,
            String.join(", ", skills),
            victories, totalBattles, winRate,
            calculatePowerRating()
        );
    }
    
    // 計算戰力評估
    private String calculatePowerRating() {
        int totalPower = level * 100 + skills.size() * 50 + victories * 10;
        
        if (totalPower >= 1000) return "傳奇";
        if (totalPower >= 500) return "精英";
        if (totalPower >= 200) return "熟練";
        return "新手";
    }
    
    // Getter 方法
    public String getName() { return name; }
    public int getLevel() { return level; }
    public int getExperience() { return experience; }
    public List<String> getSkills() { return new ArrayList<>(skills); }
    public boolean isAlive() { return health > 0; }
    
    // 恢復血量
    public void heal() {
        this.health = this.maxHealth;
    }
    
    // 序列化為字串格式
    public String serialize() {
        return String.format("%s|%d|%d|%d|%d|%s|%d|%d",
            name, level, health, maxHealth, experience,
            String.join(",", skills), totalBattles, victories);
    }
    
    // 從字串格式還原
    public static GameCharacter deserialize(String data) {
        String[] parts = data.split("\\|");
        GameCharacter character = new GameCharacter(parts[0]);
        
        character.level = Integer.parseInt(parts[1]);
        character.health = Integer.parseInt(parts[2]);
        character.maxHealth = Integer.parseInt(parts[3]);
        character.experience = Integer.parseInt(parts[4]);
        
        character.skills.clear();
        if (!parts[5].isEmpty()) {
            character.skills.addAll(Arrays.asList(parts[5].split(",")));
        }
        
        character.totalBattles = Integer.parseInt(parts[6]);
        character.victories = Integer.parseInt(parts[7]);
        
        return character;
    }
}

// 遊戲管理系統 (10分)
public class GameManager {
    private Map<String, GameCharacter> characters;
    private List<String> battleLog;
    
    public GameManager() {
        this.characters = new HashMap<>();
        this.battleLog = new ArrayList<>();
    }
    
    // 角色管理 (5分)
    public void createCharacter(String name) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("角色姓名不能為空");
        }
        
        if (characters.containsKey(name)) {
            throw new IllegalArgumentException("角色姓名已存在：" + name);
        }
        
        characters.put(name, new GameCharacter(name));
    }
    
    public GameCharacter findCharacter(String name) {
        return characters.get(name);
    }
    
    public void removeCharacter(String name) {
        if (characters.remove(name) == null) {
            throw new IllegalArgumentException("找不到角色：" + name);
        }
    }
    
    // 戰鬥安排 (3分)
    public String arrangeBattle(String player1, String player2) {
        GameCharacter char1 = findCharacter(player1);
        GameCharacter char2 = findCharacter(player2);
        
        if (char1 == null) throw new IllegalArgumentException("找不到角色：" + player1);
        if (char2 == null) throw new IllegalArgumentException("找不到角色：" + player2);
        if (!char1.isAlive()) throw new IllegalStateException(player1 + " 已陣亡");
        if (!char2.isAlive()) throw new IllegalStateException(player2 + " 已陣亡");
        
        String battleResult = char1.battle(char2);
        battleLog.add(new Date() + ": " + battleResult);
        
        return battleResult;
    }
    
    // 排行榜系統 (2分)
    public List<GameCharacter> getLeaderboard() {
        return characters.values().stream()
                        .sorted((c1, c2) -> {
                            // 先按等級排序，再按經驗值排序
                            int levelCompare = Integer.compare(c2.getLevel(), c1.getLevel());
                            if (levelCompare != 0) return levelCompare;
                            return Integer.compare(c2.getExperience(), c1.getExperience());
                        })
                        .collect(Collectors.toList());
    }
    
    // 額外功能
    public void healAllCharacters() {
        characters.values().forEach(GameCharacter::heal);
    }
    
    public String getGameStatistics() {
        int totalCharacters = characters.size();
        int totalBattles = battleLog.size();
        OptionalDouble avgLevel = characters.values().stream()
                                           .mapToInt(GameCharacter::getLevel)
                                           .average();
        
        return String.format("遊戲統計:\n角色總數: %d\n戰鬥總數: %d\n平均等級: %.1f",
                           totalCharacters, totalBattles, avgLevel.orElse(0.0));
    }
    
    public List<String> getBattleLog() {
        return new ArrayList<>(battleLog);
    }
}
```

**完整測試程式：**
```java
public class GameTest {
    public static void main(String[] args) {
        GameManager game = new GameManager();
        
        // 創建角色
        game.createCharacter("勇者阿明");
        game.createCharacter("法師小美");
        game.createCharacter("戰士大力");
        
        // 提升等級進行測試
        GameCharacter hero = game.findCharacter("勇者阿明");
        for (int i = 0; i < 10; i++) {
            hero.experience += 150; // 手動增加經驗值
            hero.levelUp();
        }
        
        // 安排戰鬥
        String battleResult = game.arrangeBattle("勇者阿明", "法師小美");
        System.out.println(battleResult);
        
        // 顯示排行榜
        System.out.println("\n=== 排行榜 ===");
        List<GameCharacter> leaderboard = game.getLeaderboard();
        for (int i = 0; i < leaderboard.size(); i++) {
            System.out.printf("%d. %s (等級 %d)\n", 
                i + 1, leaderboard.get(i).getName(), leaderboard.get(i).getLevel());
        }
        
        // 遊戲統計
        System.out.println("\n" + game.getGameStatistics());
    }
}
```

---

## 🔧 **第三部分：程式碼最佳化與分析答案 (10分)**

### **⚡ 題目 14：效能分析與最佳化答案 (10分)**

**14.1** (3分) **效能最佳答案：版本 C (串流處理)**

**詳細分析：**
- **版本 A 問題**：字串連接會產生 O(n²) 時間複雜度
  - 每次 `+` 操作都會創建新的 String 物件
  - 處理1000個單字需要創建約1000個臨時字串物件
  
- **版本 B 優勢**：StringBuilder 提供 O(n) 時間複雜度
  - 內部使用可擴展的字元陣列
  - 避免重複的記憶體分配

- **版本 C 最優**：
  - 使用並行流處理能力（在多核心環境下）
  - JVM 內建最佳化
  - 函數式程式設計，易於最佳化

**14.2** (3分) **版本A的記憶體問題**

**記憶體使用分析：**
```java
String result = ""; // 初始字串
// 第1次：result = "" + "WORD1 "        -> 產生臨時物件1  
// 第2次：result = "WORD1 " + "WORD2 "  -> 產生臨時物件2
// 第n次：result = "..." + "WORDn "     -> 產生臨時物件n
```

**問題根源：**
- String 的不可變性 (immutable) 特質
- 每次字串操作都需要分配新記憶體
- 舊的字串物件成為垃圾，增加 GC 壓力
- 記憶體使用量： O(n²) 其中 n 是單字數量

**14.3** (2分) **APCS競賽環境推薦：版本 B**

**推薦理由：**
- **可讀性**：程式碼邏輯清晰，易於理解和除錯
- **效率**：O(n) 時間複雜度，記憶體使用穩定
- **相容性**：不依賴 Java 8+ 特性，相容性好
- **可控性**：程式執行流程明確，便於最佳化

**APCS考量：**
- 競賽環境可能限制 Java 版本
- 註重程式碼的穩定性和可預測性
- 平衡效能與程式碼複雜度

**14.4** (2分) **版本B增加過濾功能的最佳方式**

**最有效率的實作：**
```java
public String processText(List<String> words) {
    StringBuilder sb = new StringBuilder();
    for (String word : words) {
        if (word != null && !word.trim().isEmpty()) {  // 過濾空字串
            sb.append(word.toUpperCase()).append(" ");
        }
    }
    return sb.toString().trim();
}
```

**最佳化要點：**
- 在迴圈內部進行過濾，避免額外的遍歷
- 使用 `trim()` 處理只包含空白的字串
- 保持 StringBuilder 的效能優勢
- 最後使用 `trim()` 移除結尾空格

---

## 🏅 **加分題：創新應用設計答案 (10分)**

### **🌟 題目 15：APCS 智慧助教系統答案 (10分)**

```java
import java.util.*;
import java.util.regex.Pattern;

// 分析報告類別
class AnalysisReport {
    private Map<String, Integer> issues;
    private Map<String, String> suggestions;
    private int overallScore;
    private List<String> goodPractices;
    
    public AnalysisReport() {
        this.issues = new HashMap<>();
        this.suggestions = new HashMap<>();
        this.goodPractices = new ArrayList<>();
        this.overallScore = 0;
    }
    
    // Getters and setters...
    public Map<String, Integer> getIssues() { return issues; }
    public void addIssue(String type, int severity) { 
        issues.put(type, issues.getOrDefault(type, 0) + severity); 
    }
    public void addSuggestion(String category, String suggestion) { 
        suggestions.put(category, suggestion); 
    }
    public void setOverallScore(int score) { this.overallScore = score; }
    public int getOverallScore() { return overallScore; }
    public void addGoodPractice(String practice) { goodPractices.add(practice); }
}

// 建議類別
class Suggestion {
    private String category;
    private String description;
    private int priority; // 1-5，5最重要
    private String example;
    
    public Suggestion(String category, String description, int priority, String example) {
        this.category = category;
        this.description = description;
        this.priority = priority;
        this.example = example;
    }
    
    // Getters...
    public String getCategory() { return category; }
    public String getDescription() { return description; }
    public int getPriority() { return priority; }
    public String getExample() { return example; }
}

// 學習進度類別
class LearningProgress {
    private String studentId;
    private Map<String, Double> skillLevels;
    private List<String> improvementAreas;
    private double overallProgress;
    
    public LearningProgress(String studentId) {
        this.studentId = studentId;
        this.skillLevels = new HashMap<>();
        this.improvementAreas = new ArrayList<>();
    }
    
    // Getters and setters...
    public void setSkillLevel(String skill, double level) { skillLevels.put(skill, level); }
    public void addImprovementArea(String area) { improvementAreas.add(area); }
    public void setOverallProgress(double progress) { this.overallProgress = progress; }
    public Map<String, Double> getSkillLevels() { return skillLevels; }
}

// 主要的 APCS 智慧助教系統
public class APCSMentor {
    private Map<String, Pattern> codePatterns;
    private Map<String, List<String>> commonIssues;
    
    public APCSMentor() {
        initializePatterns();
        initializeCommonIssues();
    }
    
    // 初始化程式碼模式
    private void initializePatterns() {
        codePatterns = new HashMap<>();
        
        // 變數命名模式
        codePatterns.put("camelCase", Pattern.compile("[a-z][a-zA-Z0-9]*"));
        codePatterns.put("constantCase", Pattern.compile("[A-Z][A-Z0-9_]*"));
        
        // 方法命名模式
        codePatterns.put("methodName", Pattern.compile("[a-z][a-zA-Z0-9]*"));
        
        // 類別命名模式
        codePatterns.put("className", Pattern.compile("[A-Z][a-zA-Z0-9]*"));
    }
    
    // 初始化常見問題
    private void initializeCommonIssues() {
        commonIssues = new HashMap<>();
        
        List<String> namingIssues = Arrays.asList(
            "變數名稱使用拼音", "方法名稱不明確", "類別名稱不符合慣例"
        );
        commonIssues.put("命名規範", namingIssues);
        
        List<String> logicIssues = Arrays.asList(
            "未處理除零例外", "陣列索引可能越界", "無窮迴圈風險"
        );
        commonIssues.put("邏輯錯誤", logicIssues);
        
        List<String> performanceIssues = Arrays.asList(
            "字串連接效率問題", "巢狀迴圈複雜度過高", "重複計算"
        );
        commonIssues.put("效能問題", performanceIssues);
    }
    
    // 程式碼分析 (4分)
    public AnalysisReport analyzeCode(String sourceCode) {
        AnalysisReport report = new AnalysisReport();
        
        if (sourceCode == null || sourceCode.trim().isEmpty()) {
            report.addIssue("空程式碼", 5);
            return report;
        }
        
        // 1. 程式碼風格檢查
        analyzeCodeStyle(sourceCode, report);
        
        // 2. 邏輯錯誤偵測
        analyzeLogicErrors(sourceCode, report);
        
        // 3. 效能分析
        analyzePerformance(sourceCode, report);
        
        // 4. 計算整體評分
        calculateOverallScore(report);
        
        return report;
    }
    
    // 程式碼風格分析
    private void analyzeCodeStyle(String sourceCode, AnalysisReport report) {
        String[] lines = sourceCode.split("\n");
        
        // 檢查縮排一致性
        boolean hasInconsistentIndentation = false;
        for (String line : lines) {
            if (line.trim().isEmpty()) continue;
            // 簡化的縮排檢查
            if (line.startsWith("\t") && line.contains("    ")) {
                hasInconsistentIndentation = true;
                break;
            }
        }
        
        if (hasInconsistentIndentation) {
            report.addIssue("縮排不一致", 2);
        }
        
        // 檢查變數命名
        Pattern variablePattern = Pattern.compile("\\b(?:int|double|String|boolean)\\s+([a-zA-Z_][a-zA-Z0-9_]*)");
        java.util.regex.Matcher matcher = variablePattern.matcher(sourceCode);
        
        while (matcher.find()) {
            String varName = matcher.group(1);
            if (!codePatterns.get("camelCase").matcher(varName).matches()) {
                report.addIssue("變數命名不規範", 1);
            }
        }
        
        // 檢查註解覆蓋率
        long commentLines = Arrays.stream(sourceCode.split("\n"))
                                 .filter(line -> line.trim().startsWith("//") || 
                                              line.trim().startsWith("/*"))
                                 .count();
        long totalLines = sourceCode.split("\n").length;
        
        if (commentLines < totalLines * 0.1) {
            report.addIssue("註解不足", 2);
        } else {
            report.addGoodPractice("適當的註解覆蓋率");
        }
    }
    
    // 邏輯錯誤偵測
    private void analyzeLogicErrors(String sourceCode, AnalysisReport report) {
        // 檢查除零風險
        if (sourceCode.contains("/ ") && !sourceCode.contains("if") && !sourceCode.contains("!=")) {
            report.addIssue("潛在除零風險", 4);
        }
        
        // 檢查陣列使用
        if (sourceCode.contains("[") && !sourceCode.contains("length") && !sourceCode.contains("size()")) {
            report.addIssue("陣列索引未檢查", 3);
        }
        
        // 檢查字串比較
        if (sourceCode.contains("==") && sourceCode.contains("String")) {
            report.addIssue("字串使用==比較", 3);
        } else if (sourceCode.contains(".equals(")) {
            report.addGoodPractice("正確使用字串比較");
        }
        
        // 檢查例外處理
        if (sourceCode.contains("Scanner") && !sourceCode.contains("try")) {
            report.addIssue("缺乏輸入驗證", 2);
        }
    }
    
    // 效能分析
    private void analyzePerformance(String sourceCode, AnalysisReport report) {
        // 檢查字串連接
        long stringConcats = sourceCode.chars()
                                      .filter(ch -> ch == '+')
                                      .count();
        
        if (stringConcats > 5 && sourceCode.contains("String") && !sourceCode.contains("StringBuilder")) {
            report.addIssue("字串連接效率問題", 3);
        }
        
        // 檢查巢狀迴圈
        long forLoops = Arrays.stream(sourceCode.split("\n"))
                             .filter(line -> line.trim().startsWith("for"))
                             .count();
        
        if (forLoops >= 2) {
            // 簡化的巢狀檢查
            String[] lines = sourceCode.split("\n");
            int loopDepth = 0;
            int maxDepth = 0;
            
            for (String line : lines) {
                if (line.trim().startsWith("for")) {
                    loopDepth++;
                    maxDepth = Math.max(maxDepth, loopDepth);
                } else if (line.trim().equals("}")) {
                    loopDepth = Math.max(0, loopDepth - 1);
                }
            }
            
            if (maxDepth >= 3) {
                report.addIssue("迴圈巢狀過深", 4);
            }
        }
    }
    
    // 計算整體評分
    private void calculateOverallScore(AnalysisReport report) {
        int totalIssues = report.getIssues().values().stream().mapToInt(Integer::intValue).sum();
        int baseScore = 100;
        int finalScore = Math.max(0, baseScore - totalIssues * 5);
        report.setOverallScore(finalScore);
    }
    
    // 建議生成 (3分)
    public List<Suggestion> generateSuggestions(AnalysisReport report) {
        List<Suggestion> suggestions = new ArrayList<>();
        
        for (Map.Entry<String, Integer> issue : report.getIssues().entrySet()) {
            String issueType = issue.getKey();
            int severity = issue.getValue();
            
            switch (issueType) {
                case "變數命名不規範":
                    suggestions.add(new Suggestion(
                        "命名規範",
                        "使用駝峰式命名法，變數名稱應該具有描述性",
                        3,
                        "建議：studentName 而不是 sn 或 student_name"
                    ));
                    break;
                    
                case "字串使用==比較":
                    suggestions.add(new Suggestion(
                        "邏輯錯誤",
                        "字串比較應使用 .equals() 方法而不是 == 運算子",
                        5,
                        "正確：str1.equals(str2) 錯誤：str1 == str2"
                    ));
                    break;
                    
                case "字串連接效率問題":
                    suggestions.add(new Suggestion(
                        "效能最佳化",
                        "大量字串連接應使用 StringBuilder",
                        4,
                        "StringBuilder sb = new StringBuilder(); sb.append(str);"
                    ));
                    break;
                    
                case "潛在除零風險":
                    suggestions.add(new Suggestion(
                        "例外處理",
                        "在除法運算前檢查除數是否為零",
                        5,
                        "if (divisor != 0) { result = dividend / divisor; }"
                    ));
                    break;
                    
                default:
                    suggestions.add(new Suggestion(
                        "一般建議",
                        "請檢查並改進相關程式碼品質",
                        2,
                        "參考 APCS 程式設計規範"
                    ));
            }
        }
        
        // 按優先級排序
        suggestions.sort((s1, s2) -> Integer.compare(s2.getPriority(), s1.getPriority()));
        
        return suggestions;
    }
    
    // 學習追蹤 (3分)
    public LearningProgress trackProgress(String studentId, List<String> submittedCodes) {
        LearningProgress progress = new LearningProgress(studentId);
        
        if (submittedCodes == null || submittedCodes.isEmpty()) {
            progress.setOverallProgress(0.0);
            return progress;
        }
        
        // 分析各項技能水準
        Map<String, List<Double>> skillScores = new HashMap<>();
        skillScores.put("語法正確性", new ArrayList<>());
        skillScores.put("邏輯設計", new ArrayList<>());
        skillScores.put("程式品質", new ArrayList<>());
        skillScores.put("效能考量", new ArrayList<>());
        
        for (String code : submittedCodes) {
            AnalysisReport report = analyzeCode(code);
            
            // 計算各項技能得分
            double syntaxScore = calculateSyntaxScore(code, report);
            double logicScore = calculateLogicScore(code, report);  
            double qualityScore = calculateQualityScore(code, report);
            double performanceScore = calculatePerformanceScore(code, report);
            
            skillScores.get("語法正確性").add(syntaxScore);
            skillScores.get("邏輯設計").add(logicScore);
            skillScores.get("程式品質").add(qualityScore);
            skillScores.get("效能考量").add(performanceScore);
        }
        
        // 計算技能平均水準
        for (Map.Entry<String, List<Double>> entry : skillScores.entrySet()) {
            double avgScore = entry.getValue().stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
            progress.setSkillLevel(entry.getKey(), avgScore);
        }
        
        // 識別需改進領域
        for (Map.Entry<String, Double> skill : progress.getSkillLevels().entrySet()) {
            if (skill.getValue() < 70.0) {
                progress.addImprovementArea(skill.getKey());
            }
        }
        
        // 計算整體進度
        double overallScore = progress.getSkillLevels().values().stream()
                                     .mapToDouble(Double::doubleValue).average().orElse(0.0);
        progress.setOverallProgress(overallScore);
        
        return progress;
    }
    
    // 輔助計算方法
    private double calculateSyntaxScore(String code, AnalysisReport report) {
        // 基於語法錯誤數量計算
        int syntaxIssues = report.getIssues().getOrDefault("語法錯誤", 0);
        return Math.max(0, 100 - syntaxIssues * 10);
    }
    
    private double calculateLogicScore(String code, AnalysisReport report) {
        // 基於邏輯錯誤計算
        int logicIssues = report.getIssues().getOrDefault("邏輯錯誤", 0) +
                         report.getIssues().getOrDefault("潛在除零風險", 0) +
                         report.getIssues().getOrDefault("字串使用==比較", 0);
        return Math.max(0, 100 - logicIssues * 15);
    }
    
    private double calculateQualityScore(String code, AnalysisReport report) {
        // 基於程式品質指標
        int qualityIssues = report.getIssues().getOrDefault("變數命名不規範", 0) +
                           report.getIssues().getOrDefault("註解不足", 0) +
                           report.getIssues().getOrDefault("縮排不一致", 0);
        return Math.max(0, 100 - qualityIssues * 8);
    }
    
    private double calculatePerformanceScore(String code, AnalysisReport report) {
        // 基於效能問題
        int performanceIssues = report.getIssues().getOrDefault("字串連接效率問題", 0) +
                               report.getIssues().getOrDefault("迴圈巢狀過深", 0);
        return Math.max(0, 100 - performanceIssues * 12);
    }
}
```

**測試與演示：**
```java
public class APCSMentorDemo {
    public static void main(String[] args) {
        APCSMentor mentor = new APCSMentor();
        
        // 測試程式碼
        String testCode = """
            public class Student {
                String n;  // 變數命名不佳
                int score;
                
                public void calculate() {
                    String result = "";
                    for (int i = 0; i < 100; i++) {
                        result = result + "Grade: " + (score + i);  // 字串連接效率問題
                    }
                    
                    if (n == "John") {  // 字串比較錯誤
                        System.out.println("Found!");
                    }
                }
            }
            """;
        
        // 分析程式碼
        AnalysisReport report = mentor.analyzeCode(testCode);
        System.out.println("程式碼評分：" + report.getOverallScore());
        System.out.println("發現問題：" + report.getIssues());
        
        // 生成建議
        List<Suggestion> suggestions = mentor.generateSuggestions(report);
        System.out.println("\n改進建議：");
        for (Suggestion suggestion : suggestions) {
            System.out.printf("【%s】%s (優先級: %d)\n範例：%s\n\n",
                suggestion.getCategory(), suggestion.getDescription(),
                suggestion.getPriority(), suggestion.getExample());
        }
        
        // 學習進度追蹤
        List<String> studentCodes = Arrays.asList(testCode, 
            "public class Test { public static void main(String[] args) { System.out.println(\"Hello\"); } }");
        
        LearningProgress progress = mentor.trackProgress("student001", studentCodes);
        System.out.println("學習進度分析：");
        System.out.println("整體進度：" + progress.getOverallProgress() + "%");
        System.out.println("技能水準：" + progress.getSkillLevels());
        System.out.println("需改進領域：" + progress.getImprovementAreas());
    }
}
```

**創新特點評分：**
- **創新性** (4分)：結合靜態程式碼分析與學習軌跡追蹤
- **實用性** (3分)：直接針對 APCS 考試需求設計
- **技術深度** (3分)：使用正規表示式、串流處理、統計分析

---

## 📊 **完整評分標準與學習指導**

### **🎯 各部分評分細節**

#### **第一部分：概念分析 (30分)**
- **物件設計哲學** (15分)：深度理解封裝、實用性、可重用性
- **程式碼邏輯分析** (15分)：字串處理、數學運算、邏輯推理

#### **第二部分：實務設計 (70分)**
- **文字分析系統** (25分)：字串處理、資料結構、演算法設計
- **科學計算引擎** (20分)：Math類別應用、例外處理、系統設計
- **遊戲角色管理** (25分)：完整物件導向設計、系統架構思考

#### **第三部分：最佳化分析 (10分)**
- **效能分析能力** (6分)：理解不同實作方式的效能差異
- **實務建議能力** (4分)：在競賽環境中做出最佳選擇

#### **加分題：創新設計 (10分)**
- **創新思維** (4分)：獨特的解決方案設計
- **實際應用** (3分)：對APCS學習的實際幫助
- **技術實作** (3分)：程式設計技巧的綜合運用

### **🏆 APCS 高分策略總結**

1. **深度理解物件導向**
   - 封裝性：合理的 private/public 設計
   - 可重用性：通用化的方法設計
   - 實用性：解決真實世界問題

2. **熟練運用核心類別**
   - String：熟記常用方法，理解不可變性
   - Math：掌握各種數學函數和常數
   - ArrayList：靈活運用集合操作

3. **程式設計最佳實務**
   - 例外處理：預防性程式設計思維
   - 效能考量：選擇適當的資料結構和演算法
   - 程式品質：良好的命名、註解、結構

4. **系統性思考能力**
   - 需求分析：準確理解問題需求
   - 架構設計：合理的類別和方法設計
   - 測試驗證：完整的測試案例設計

### **📈 學習建議**

- **基礎夯實**：確實掌握每個物件和方法的用法
- **實作練習**：透過完整專案提升系統設計能力
- **模式學習**：研究APCS歷年考題的出題模式
- **效能意識**：培養對程式效率的敏感度

---

**答案製作完成！** ✅

本參考答案基於 APCS 五年歷史考題分析，提供了完整的解題思路和程式實作，涵蓋物件導向程式設計的核心概念，有助於學生在 APCS 競賽中取得優異成績。