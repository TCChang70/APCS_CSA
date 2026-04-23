# 📚 第四單元：陣列與資料結構 - 詳細教學內容

## 🎯 單元學習目標
- 理解陣列的概念與重要性
- 掌握一維和二維陣列的操作
- 學會 ArrayList 動態陣列的使用
- 了解常見的陣列演算法
- 培養資料結構思維

---

## 📊 4.1 一維陣列

### **什麼是陣列（Array）？**
陣列就像是一排有編號的儲物櫃，每個櫃子可以放相同類型的物品，而且可以透過編號（索引）快速找到特定櫃子裡的東西。

**生活比喻：**
```
陣列 = 停車場
- 每個車位有固定編號（索引：0, 1, 2, ...）
- 每個車位只能停一輛車（一個數值）
- 可以直接根據編號找到車位

陣列 = 教室座位
- 每個座位有固定位置（索引）
- 每個座位坐一個學生（一個元素）
- 老師可以說「第5號同學請起立」
```

### **陣列的基本操作**
```java name=ArrayBasics.java
public class ArrayBasics {
    
    public static void main(String[] args) {
        System.out.println("=== 陣列基礎操作 ===");
        
        // 1. 陣列宣告與初始化的不同方式
        
        // 方式一：宣告後初始化
        int[] numbers1 = new int[5]; // 建立長度為5的整數陣列，預設值為0
        System.out.println("空陣列長度：" + numbers1.length);
        
        // 方式二：宣告時直接賦值
        int[] numbers2 = {10, 20, 30, 40, 50};
        
        // 方式三：使用 new 關鍵字賦值
        int[] numbers3 = new int[]{1, 2, 3, 4, 5};
        
        // 方式四：分別宣告和初始化
        int[] numbers4;
        numbers4 = new int[]{100, 200, 300};
        
        // 2. 存取陣列元素
        System.out.println("\n=== 存取陣列元素 ===");
        
        // 讀取元素（索引從 0 開始）
        System.out.println("第一個元素：" + numbers2[0]); // 10
        System.out.println("最後一個元素：" + numbers2[numbers2.length - 1]); // 50
        
        // 修改元素
        numbers2[0] = 99;
        System.out.println("修改後第一個元素：" + numbers2[0]); // 99
        
        // 3. 遍歷陣列
        System.out.println("\n=== 遍歷陣列 ===");
        
        // 傳統 for 迴圈
        System.out.print("傳統for迴圈：");
        for (int i = 0; i < numbers2.length; i++) {
            System.out.print(numbers2[i] + " ");
        }
        System.out.println();
        
        // 增強型 for 迴圈（for-each）
        System.out.print("增強型for迴圈：");
        for (int number : numbers2) {
            System.out.print(number + " ");
        }
        System.out.println();
        
        // 4. 不同資料型別的陣列
        System.out.println("\n=== 不同資料型別陣列 ===");
        
        // 字串陣列
        String[] names = {"Alice", "Bob", "Charlie", "Diana"};
        System.out.println("姓名陣列：");
        for (String name : names) {
            System.out.println("- " + name);
        }
        
        // 布林陣列
        boolean[] flags = {true, false, true, false, true};
        System.out.print("布林陣列：");
        for (boolean flag : flags) {
            System.out.print(flag + " ");
        }
        System.out.println();
        
        // 浮點數陣列
        double[] prices = {19.99, 29.50, 15.00, 99.95};
        System.out.println("價格陣列：");
        for (int i = 0; i < prices.length; i++) {
            System.out.printf("商品 %d：$%.2f\n", i + 1, prices[i]);
        }
    }
}
```

### **陣列的常用操作**
```java name=ArrayOperations.java
import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

public class ArrayOperations {
    
    // 顯示陣列內容
    public static void displayArray(int[] array, String title) {
        System.out.println(title + "：");
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]);
            if (i < array.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
    
    // 計算陣列總和
    public static int calculateSum(int[] array) {
        int sum = 0;
        for (int number : array) {
            sum += number;
        }
        return sum;
    }
    
    // 計算陣列平均值
    public static double calculateAverage(int[] array) {
        if (array.length == 0) {
            return 0;
        }
        return (double) calculateSum(array) / array.length;
    }
    
    // 找出最大值
    public static int findMax(int[] array) {
        if (array.length == 0) {
            throw new IllegalArgumentException("陣列不能為空");
        }
        
        int max = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }
        return max;
    }
    
    // 找出最小值和其索引
    public static int[] findMinWithIndex(int[] array) {
        if (array.length == 0) {
            return new int[]{0, -1}; // 值，索引
        }
        
        int min = array[0];
        int minIndex = 0;
        
        for (int i = 1; i < array.length; i++) {
            if (array[i] < min) {
                min = array[i];
                minIndex = i;
            }
        }
        
        return new int[]{min, minIndex};
    }
    
    // 搜尋元素
    public static int linearSearch(int[] array, int target) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) {
                return i; // 回傳找到的索引
            }
        }
        return -1; // 沒找到
    }
    
    // 計算出現次數
    public static int countOccurrences(int[] array, int target) {
        int count = 0;
        for (int number : array) {
            if (number == target) {
                count++;
            }
        }
        return count;
    }
    
    // 反轉陣列
    public static void reverseArray(int[] array) {
        int start = 0;
        int end = array.length - 1;
        
        while (start < end) {
            // 交換元素
            int temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            
            start++;
            end--;
        }
    }
    
    // 複製陣列
    public static int[] copyArray(int[] original) {
        int[] copy = new int[original.length];
        for (int i = 0; i < original.length; i++) {
            copy[i] = original[i];
        }
        return copy;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        // 建立測試陣列
        int[] testArray = {15, 3, 9, 15, 7, 1, 15, 22, 8};
        displayArray(testArray, "原始陣列");
        
        // 基本統計
        System.out.println("\n=== 基本統計 ===");
        System.out.println("陣列長度：" + testArray.length);
        System.out.println("總和：" + calculateSum(testArray));
        System.out.printf("平均值：%.2f\n", calculateAverage(testArray));
        System.out.println("最大值：" + findMax(testArray));
        
        int[] minResult = findMinWithIndex(testArray);
        System.out.println("最小值：" + minResult[0] + "（索引：" + minResult[1] + "）");
        
        // 搜尋功能
        System.out.println("\n=== 搜尋功能 ===");
        int searchTarget = 15;
        int foundIndex = linearSearch(testArray, searchTarget);
        if (foundIndex != -1) {
            System.out.println("數字 " + searchTarget + " 第一次出現在索引：" + foundIndex);
        } else {
            System.out.println("數字 " + searchTarget + " 不存在於陣列中");
        }
        
        int occurrences = countOccurrences(testArray, searchTarget);
        System.out.println("數字 " + searchTarget + " 總共出現 " + occurrences + " 次");
        
        // 陣列操作
        System.out.println("\n=== 陣列操作 ===");
        int[] copyArray = copyArray(testArray);
        displayArray(copyArray, "複製的陣列");
        
        reverseArray(copyArray);
        displayArray(copyArray, "反轉後的陣列");
        displayArray(testArray, "原始陣列（未改變）");
        
        // 使用 Arrays 類別的內建方法
        System.out.println("\n=== Arrays 類別方法 ===");
        int[] sortArray = copyArray(testArray);
        Arrays.sort(sortArray);
        displayArray(sortArray, "排序後的陣列");
        
        // 二分搜尋（需要先排序）
        int binarySearchResult = Arrays.binarySearch(sortArray, searchTarget);
        System.out.println("二分搜尋結果（索引）：" + binarySearchResult);
        
        // 比較陣列
        boolean isEqual = Arrays.equals(testArray, copyArray);
        System.out.println("原始陣列與反轉陣列相等：" + isEqual);
        
        // 填充陣列
        int[] fillArray = new int[10];
        Arrays.fill(fillArray, 99);
        displayArray(fillArray, "填充後的陣列");
        
        // 互動式操作
        System.out.println("\n=== 互動式操作 ===");
        System.out.print("請輸入要搜尋的數字：");
        int userTarget = scanner.nextInt();
        
        int userResult = linearSearch(testArray, userTarget);
        if (userResult != -1) {
            System.out.println("找到了！位於索引：" + userResult);
        } else {
            System.out.println("沒有找到數字 " + userTarget);
        }
        
        scanner.close();
    }
}
```

### **成績處理系統實例**
```java name=GradeManager.java
import java.util.Scanner;
import java.util.Arrays;

public class GradeManager {
    
    // 輸入成績
    public static double[] inputGrades(Scanner scanner) {
        System.out.print("請輸入學生人數：");
        int studentCount = scanner.nextInt();
        
        double[] grades = new double[studentCount];
        
        for (int i = 0; i < studentCount; i++) {
            System.out.print("請輸入第 " + (i + 1) + " 位學生的成績：");
            grades[i] = scanner.nextDouble();
            
            // 驗證成績範圍
            while (grades[i] < 0 || grades[i] > 100) {
                System.out.print("成績必須在 0-100 之間，請重新輸入：");
                grades[i] = scanner.nextDouble();
            }
        }
        
        return grades;
    }
    
    // 顯示成績統計
    public static void displayStatistics(double[] grades) {
        System.out.println("\n=== 成績統計報告 ===");
        
        // 基本統計
        double sum = 0;
        double max = grades[0];
        double min = grades[0];
        
        for (double grade : grades) {
            sum += grade;
            if (grade > max) max = grade;
            if (grade < min) min = grade;
        }
        
        double average = sum / grades.length;
        
        System.out.printf("學生人數：%d\n", grades.length);
        System.out.printf("總分：%.1f\n", sum);
        System.out.printf("平均分：%.2f\n", average);
        System.out.printf("最高分：%.1f\n", max);
        System.out.printf("最低分：%.1f\n", min);
        
        // 等級分布
        int[] gradeDistribution = new int[5]; // A, B, C, D, F
        
        for (double grade : grades) {
            if (grade >= 90) {
                gradeDistribution[0]++; // A
            } else if (grade >= 80) {
                gradeDistribution[1]++; // B
            } else if (grade >= 70) {
                gradeDistribution[2]++; // C
            } else if (grade >= 60) {
                gradeDistribution[3]++; // D
            } else {
                gradeDistribution[4]++; // F
            }
        }
        
        System.out.println("\n=== 等級分布 ===");
        String[] gradeLabels = {"A (90-100)", "B (80-89)", "C (70-79)", "D (60-69)", "F (0-59)"};
        
        for (int i = 0; i < gradeLabels.length; i++) {
            double percentage = (double) gradeDistribution[i] / grades.length * 100;
            System.out.printf("%s：%d 人 (%.1f%%)\n", 
                gradeLabels[i], gradeDistribution[i], percentage);
        }
    }
    
    // 顯示詳細成績單
    public static void displayDetailedGrades(double[] grades) {
        System.out.println("\n=== 詳細成績單 ===");
        
        // 建立索引陣列來追蹤原始順序
        Integer[] indices = new Integer[grades.length];
        for (int i = 0; i < indices.length; i++) {
            indices[i] = i;
        }
        
        // 根據成績排序索引（降序）
        Arrays.sort(indices, (a, b) -> Double.compare(grades[b], grades[a]));
        
        System.out.println("排名\t學號\t成績\t等級");
        System.out.println("--------------------------------");
        
        for (int rank = 0; rank < indices.length; rank++) {
            int studentIndex = indices[rank];
            double grade = grades[studentIndex];
            String gradeLevel = getGradeLevel(grade);
            
            System.out.printf("%d\tS%03d\t%.1f\t%s\n", 
                rank + 1, studentIndex + 1, grade, gradeLevel);
        }
    }
    
    // 獲取等級
    private static String getGradeLevel(double grade) {
        if (grade >= 90) return "A";
        else if (grade >= 80) return "B";
        else if (grade >= 70) return "C";
        else if (grade >= 60) return "D";
        else return "F";
    }
    
    // 搜尋功能
    public static void searchGrades(double[] grades, Scanner scanner) {
        System.out.println("\n=== 成績搜尋 ===");
        System.out.println("1. 搜尋特定分數");
        System.out.println("2. 搜尋分數範圍");
        System.out.print("請選擇搜尋方式：");
        
        int choice = scanner.nextInt();
        
        switch (choice) {
            case 1:
                System.out.print("請輸入要搜尋的分數：");
                double targetScore = scanner.nextDouble();
                
                System.out.println("搜尋結果：");
                boolean found = false;
                for (int i = 0; i < grades.length; i++) {
                    if (Math.abs(grades[i] - targetScore) < 0.1) { // 允許小數點誤差
                        System.out.printf("學號 S%03d：%.1f 分\n", i + 1, grades[i]);
                        found = true;
                    }
                }
                
                if (!found) {
                    System.out.println("沒有找到 " + targetScore + " 分的學生");
                }
                break;
                
            case 2:
                System.out.print("請輸入最低分數：");
                double minScore = scanner.nextDouble();
                System.out.print("請輸入最高分數：");
                double maxScore = scanner.nextDouble();
                
                System.out.printf("%.1f - %.1f 分範圍內的學生：\n", minScore, maxScore);
                int count = 0;
                for (int i = 0; i < grades.length; i++) {
                    if (grades[i] >= minScore && grades[i] <= maxScore) {
                        System.out.printf("學號 S%03d：%.1f 分\n", i + 1, grades[i]);
                        count++;
                    }
                }
                
                System.out.println("總共找到 " + count + " 位學生");
                break;
                
            default:
                System.out.println("無效選擇");
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== 學生成績管理系統 ===");
        
        // 輸入成績
        double[] grades = inputGrades(scanner);
        
        while (true) {
            System.out.println("\n=== 主選單 ===");
            System.out.println("1. 顯示統計報告");
            System.out.println("2. 顯示詳細成績單");
            System.out.println("3. 搜尋成績");
            System.out.println("4. 重新輸入成績");
            System.out.println("0. 離開程式");
            System.out.print("請選擇功能：");
            
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    displayStatistics(grades);
                    break;
                    
                case 2:
                    displayDetailedGrades(grades);
                    break;
                    
                case 3:
                    searchGrades(grades, scanner);
                    break;
                    
                case 4:
                    grades = inputGrades(scanner);
                    break;
                    
                case 0:
                    System.out.println("感謝使用成績管理系統！");
                    scanner.close();
                    return;
                    
                default:
                    System.out.println("無效選擇，請重新輸入！");
            }
        }
    }
}
```

---

## 🏢 4.2 二維陣列

### **什麼是二維陣列？**
二維陣列就像是一個表格或矩陣，有行（row）和列（column），可以用來存放表格形式的資料。

**生活比喻：**
```
二維陣列 = 電影院座位
- 每一排是一個一維陣列（row）
- 每個座位有 [排數][座位號] 的位置

二維陣列 = Excel 試算表
- 行：A, B, C, D...
- 列：1, 2, 3, 4...
- 每個儲存格：[列][行]
```

### **二維陣列基礎操作**
```java name=TwoDimensionalArray.java
import java.util.Scanner;
import java.util.Random;

public class TwoDimensionalArray {
    
    // 顯示二維陣列
    public static void display2DArray(int[][] array, String title) {
        System.out.println(title + "：");
        
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                System.out.printf("%4d ", array[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }
    
    // 填充隨機數字
    public static void fillRandomNumbers(int[][] array, int min, int max) {
        Random random = new Random();
        
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                array[i][j] = random.nextInt(max - min + 1) + min;
            }
        }
    }
    
    // 計算行總和
    public static int[] calculateRowSums(int[][] array) {
        int[] rowSums = new int[array.length];
        
        for (int i = 0; i < array.length; i++) {
            int sum = 0;
            for (int j = 0; j < array[i].length; j++) {
                sum += array[i][j];
            }
            rowSums[i] = sum;
        }
        
        return rowSums;
    }
    
    // 計算列總和
    public static int[] calculateColumnSums(int[][] array) {
        if (array.length == 0) return new int[0];
        
        int[] columnSums = new int[array[0].length];
        
        for (int j = 0; j < array[0].length; j++) {
            int sum = 0;
            for (int i = 0; i < array.length; i++) {
                sum += array[i][j];
            }
            columnSums[j] = sum;
        }
        
        return columnSums;
    }
    
    // 找出最大值及其位置
    public static int[] findMaxWithPosition(int[][] array) {
        if (array.length == 0 || array[0].length == 0) {
            return new int[]{0, -1, -1}; // 值, 行, 列
        }
        
        int max = array[0][0];
        int maxRow = 0;
        int maxCol = 0;
        
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                if (array[i][j] > max) {
                    max = array[i][j];
                    maxRow = i;
                    maxCol = j;
                }
            }
        }
        
        return new int[]{max, maxRow, maxCol};
    }
    
    // 轉置矩陣
    public static int[][] transpose(int[][] array) {
        int rows = array.length;
        int cols = array[0].length;
        
        int[][] transposed = new int[cols][rows];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                transposed[j][i] = array[i][j];
            }
        }
        
        return transposed;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== 二維陣列操作示範 ===");
        
        // 1. 不同的宣告方式
        System.out.println("=== 陣列宣告方式 ===");
        
        // 方式一：直接初始化
        int[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        display2DArray(matrix1, "直接初始化的矩陣");
        
        // 方式二：先宣告大小再賦值
        int[][] matrix2 = new int[3][4];
        int value = 1;
        for (int i = 0; i < matrix2.length; i++) {
            for (int j = 0; j < matrix2[i].length; j++) {
                matrix2[i][j] = value++;
            }
        }
        display2DArray(matrix2, "3x4 矩陣");
        
        // 方式三：不規則陣列（Jagged Array）
        int[][] jaggedArray = new int[3][];
        jaggedArray[0] = new int[]{1, 2};
        jaggedArray[1] = new int[]{3, 4, 5, 6};
        jaggedArray[2] = new int[]{7, 8, 9};
        
        System.out.println("不規則陣列：");
        for (int i = 0; i < jaggedArray.length; i++) {
            System.out.print("第 " + i + " 行：");
            for (int j = 0; j < jaggedArray[i].length; j++) {
                System.out.print(jaggedArray[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
        
        // 2. 隨機填充矩陣
        System.out.print("請輸入矩陣的行數：");
        int rows = scanner.nextInt();
        System.out.print("請輸入矩陣的列數：");
        int cols = scanner.nextInt();
        
        int[][] randomMatrix = new int[rows][cols];
        fillRandomNumbers(randomMatrix, 1, 99);
        display2DArray(randomMatrix, "隨機生成的 " + rows + "x" + cols + " 矩陣");
        
        // 3. 矩陣統計
        System.out.println("=== 矩陣統計 ===");
        
        int[] rowSums = calculateRowSums(randomMatrix);
        System.out.println("各行總和：");
        for (int i = 0; i < rowSums.length; i++) {
            System.out.println("第 " + i + " 行：" + rowSums[i]);
        }
        
        int[] columnSums = calculateColumnSums(randomMatrix);
        System.out.println("\n各列總和：");
        for (int j = 0; j < columnSums.length; j++) {
            System.out.println("第 " + j + " 列：" + columnSums[j]);
        }
        
        int[] maxInfo = findMaxWithPosition(randomMatrix);
        System.out.printf("\n最大值：%d，位置：[%d][%d]\n", 
            maxInfo[0], maxInfo[1], maxInfo[2]);
        
        // 4. 矩陣轉置
        if (rows <= 5 && cols <= 5) { // 只有小矩陣才顯示轉置
            int[][] transposedMatrix = transpose(randomMatrix);
            display2DArray(transposedMatrix, "轉置後的矩陣");
        }
        
        scanner.close();
    }
}
```

### **井字遊戲實例**
```java name=TicTacToe.java
import java.util.Scanner;

public class TicTacToe {
    private char[][] board;
    private char currentPlayer;
    private Scanner scanner;
    
    public TicTacToe() {
        board = new char[3][3];
        currentPlayer = 'X';
        scanner = new Scanner(System.in);
        initializeBoard();
    }
    
    // 初始化棋盤
    private void initializeBoard() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = ' ';
            }
        }
    }
    
    // 顯示棋盤
    private void displayBoard() {
        System.out.println("\n   0   1   2");
        System.out.println("  -----------");
        
        for (int i = 0; i < 3; i++) {
            System.out.print(i + " | ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " | ");
            }
            System.out.println();
            System.out.println("  -----------");
        }
        System.out.println();
    }
    
    // 檢查位置是否有效
    private boolean isValidMove(int row, int col) {
        return row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == ' ';
    }
    
    // 執行移動
    private void makeMove(int row, int col) {
        board[row][col] = currentPlayer;
    }
    
    // 檢查遊戲是否結束
    private boolean checkWin() {
        // 檢查行
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == currentPlayer && 
                board[i][1] == currentPlayer && 
                board[i][2] == currentPlayer) {
                return true;
            }
        }
        
        // 檢查列
        for (int j = 0; j < 3; j++) {
            if (board[0][j] == currentPlayer && 
                board[1][j] == currentPlayer && 
                board[2][j] == currentPlayer) {
                return true;
            }
        }
        
        // 檢查對角線
        if (board[0][0] == currentPlayer && 
            board[1][1] == currentPlayer && 
            board[2][2] == currentPlayer) {
            return true;
        }
        
        if (board[0][2] == currentPlayer && 
            board[1][1] == currentPlayer && 
            board[2][0] == currentPlayer) {
            return true;
        }
        
        return false;
    }
    
    // 檢查是否平局
    private boolean checkDraw() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == ' ') {
                    return false;
                }
            }
        }
        return true;
    }
    
    // 切換玩家
    private void switchPlayer() {
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }
    
    // 玩家輸入
    private int[] getPlayerInput() {
        while (true) {
            System.out.print("玩家 " + currentPlayer + "，請輸入位置 (行 列)：");
            
            try {
                int row = scanner.nextInt();
                int col = scanner.nextInt();
                
                if (isValidMove(row, col)) {
                    return new int[]{row, col};
                } else {
                    System.out.println("❌ 無效位置，請重新輸入！");
                }
            } catch (Exception e) {
                System.out.println("❌ 請輸入有效的數字！");
                scanner.nextLine(); // 清除輸入緩衝
            }
        }
    }
    
    // 顯示遊戲說明
    private void showInstructions() {
        System.out.println("=== 井字遊戲 ===");
        System.out.println("遊戲規則：");
        System.out.println("1. 輪流在棋盤上放置 X 或 O");
        System.out.println("2. 先連成一條線（橫、直、斜）的玩家獲勝");
        System.out.println("3. 棋盤填滿且無人獲勝則為平局");
        System.out.println("\n座標說明：");
        System.out.println("輸入格式：行號 列號（例如：1 2）");
        System.out.println("座標範圍：0-2");
    }
    
    // 主要遊戲循環
    public void playGame() {
        showInstructions();
        
        while (true) {
            displayBoard();
            
            // 獲取玩家輸入
            int[] move = getPlayerInput();
            makeMove(move[0], move[1]);
            
            // 檢查遊戲狀態
            if (checkWin()) {
                displayBoard();
                System.out.println("🎉 恭喜！玩家 " + currentPlayer + " 獲勝！");
                break;
            }
            
            if (checkDraw()) {
                displayBoard();
                System.out.println("🤝 平局！棋逢對手！");
                break;
            }
            
            // 切換玩家
            switchPlayer();
        }
        
        // 詢問是否再玩一局
        System.out.print("要再玩一局嗎？(y/n)：");
        String playAgain = scanner.next();
        
        if (playAgain.toLowerCase().equals("y")) {
            initializeBoard();
            currentPlayer = 'X';
            playGame();
        } else {
            System.out.println("感謝遊玩！");
        }
    }
    
    public static void main(String[] args) {
        TicTacToe game = new TicTacToe();
        game.playGame();
    }
}
```

---

## 📈 4.3 ArrayList（動態陣列）

### **什麼是 ArrayList？**
ArrayList 是 Java 提供的動態陣列，可以自動調整大小，比傳統陣列更靈活。

**ArrayList vs 傳統陣列：**
```
傳統陣列：
- 固定大小，宣告後不能改變
- 效能較好
- 可以存放基本資料型別

ArrayList：
- 動態大小，可以自由增減元素
- 提供豐富的方法
- 只能存放物件（包裝類別）
```

### **ArrayList 基本操作**
```java name=ArrayListBasics.java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class ArrayListBasics {
    
    // 顯示 ArrayList 內容
    public static void displayList(ArrayList<Integer> list, String title) {
        System.out.println(title + "：");
        if (list.isEmpty()) {
            System.out.println("（空列表）");
        } else {
            System.out.print("[");
            for (int i = 0; i < list.size(); i++) {
                System.out.print(list.get(i));
                if (i < list.size() - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println("]");
        }
        System.out.println("大小：" + list.size());
        System.out.println();
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== ArrayList 基本操作 ===");
        
        // 1. 建立 ArrayList
        ArrayList<Integer> numbers = new ArrayList<>();
        ArrayList<String> names = new ArrayList<>();
        
        // 也可以指定初始容量
        ArrayList<Double> prices = new ArrayList<>(10);
        
        // 2. 添加元素
        System.out.println("=== 添加元素 ===");
        
        // add() - 在末尾添加
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        displayList(numbers, "添加元素後");
        
        // add(index, element) - 在指定位置插入
        numbers.add(1, 15); // 在索引 1 插入 15
        displayList(numbers, "插入元素後");
        
        // 3. 存取元素
        System.out.println("=== 存取元素 ===");
        System.out.println("第一個元素：" + numbers.get(0));
        System.out.println("最後一個元素：" + numbers.get(numbers.size() - 1));
        
        // 4. 修改元素
        System.out.println("=== 修改元素 ===");
        System.out.println("修改前：" + numbers.get(0));
        numbers.set(0, 99); // 將索引 0 的元素改為 99
        System.out.println("修改後：" + numbers.get(0));
        displayList(numbers, "修改元素後");
        
        // 5. 刪除元素
        System.out.println("=== 刪除元素 ===");
        
        // remove(index) - 根據索引刪除
        int removedElement = numbers.remove(1);
        System.out.println("刪除的元素：" + removedElement);
        displayList(numbers, "根據索引刪除後");
        
        // remove(Object) - 根據值刪除
        boolean removed = numbers.remove(Integer.valueOf(30));
        System.out.println("是否成功刪除 30：" + removed);
        displayList(numbers, "根據值刪除後");
        
        // 6. 搜尋功能
        System.out.println("=== 搜尋功能 ===");
        
        // 重新填充列表
        numbers.clear();
        Collections.addAll(numbers, 5, 10, 15, 10, 25, 10);
        displayList(numbers, "重新填充的列表");
        
        // contains() - 檢查是否包含某元素
        boolean contains15 = numbers.contains(15);
        System.out.println("是否包含 15：" + contains15);
        
        // indexOf() - 找到第一個匹配的索引
        int firstIndex = numbers.indexOf(10);
        System.out.println("10 第一次出現的索引：" + firstIndex);
        
        // lastIndexOf() - 找到最後一個匹配的索引
        int lastIndex = numbers.lastIndexOf(10);
        System.out.println("10 最後一次出現的索引：" + lastIndex);
        
        // 7. 列表操作
        System.out.println("=== 列表操作 ===");
        
        // 排序
        ArrayList<Integer> sortedNumbers = new ArrayList<>(numbers);
        Collections.sort(sortedNumbers);
        displayList(sortedNumbers, "排序後");
        
        // 反轉
        ArrayList<Integer> reversedNumbers = new ArrayList<>(numbers);
        Collections.reverse(reversedNumbers);
        displayList(reversedNumbers, "反轉後");
        
        // 洗牌
        ArrayList<Integer> shuffledNumbers = new ArrayList<>(numbers);
        Collections.shuffle(shuffledNumbers);
        displayList(shuffledNumbers, "洗牌後");
        
        // 8. 字串 ArrayList
        System.out.println("=== 字串 ArrayList ===");
        
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");
        names.add("Diana");
        
        System.out.println("名字列表：" + names);
        
        // 字串排序
        Collections.sort(names);
        System.out.println("排序後：" + names);
        
        // 9. 轉換操作
        System.out.println("=== 轉換操作 ===");
        
        // ArrayList 轉陣列
        Integer[] numberArray = numbers.toArray(new Integer[0]);
        System.out.print("轉換為陣列：");
        for (Integer num : numberArray) {
            System.out.print(num + " ");
        }
        System.out.println();
        
        // 陣列轉 ArrayList
        String[] nameArray = {"Eve", "Frank", "Grace"};
        ArrayList<String> nameList = new ArrayList<>();
        Collections.addAll(nameList, nameArray);
        System.out.println("陣列轉 ArrayList：" + nameList);
        
        // 10. 互動式操作
        System.out.println("\n=== 互動式操作 ===");
        ArrayList<Integer> userList = new ArrayList<>();
        
        while (true) {
            System.out.println("\n當前列表：" + userList);
            System.out.println("1. 添加數字");
            System.out.println("2. 刪除數字");
            System.out.println("3. 搜尋數字");
            System.out.println("4. 排序列表");
            System.out.println("5. 清空列表");
            System.out.println("0. 離開");
            System.out.print("請選擇操作：");
            
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    System.out.print("請輸入要添加的數字：");
                    int addNumber = scanner.nextInt();
                    userList.add(addNumber);
                    System.out.println("已添加 " + addNumber);
                    break;
                    
                case 2:
                    if (!userList.isEmpty()) {
                        System.out.print("請輸入要刪除的數字：");
                        int removeNumber = scanner.nextInt();
                        boolean success = userList.remove(Integer.valueOf(removeNumber));
                        System.out.println(success ? "刪除成功" : "數字不存在");
                    } else {
                        System.out.println("列表為空");
                    }
                    break;
                    
                case 3:
                    System.out.print("請輸入要搜尋的數字：");
                    int searchNumber = scanner.nextInt();
                    int index = userList.indexOf(searchNumber);
                    if (index != -1) {
                        System.out.println("找到了！位於索引：" + index);
                    } else {
                        System.out.println("沒有找到該數字");
                    }
                    break;
                    
                case 4:
                    Collections.sort(userList);
                    System.out.println("列表已排序");
                    break;
                    
                case 5:
                    userList.clear();
                    System.out.println("列表已清空");
                    break;
                    
                case 0:
                    System.out.println("感謝使用！");
                    scanner.close();
                    return;
                    
                default:
                    System.out.println("無效選擇");
            }
        }
    }
}
```
繼續第四單元的內容...

```java name=StudentManager.java
        System.out.println("待改進 (2.7-)：" + poor + " 人");
    }
    
    // 主選單
    public void showMenu() {
        while (true) {
            System.out.println("\n=== 學生資訊管理系統 ===");
            System.out.println("1. 顯示所有學生");
            System.out.println("2. 添加學生");
            System.out.println("3. 搜尋學生");
            System.out.println("4. 修改學生資料");
            System.out.println("5. 刪除學生");
            System.out.println("6. 排序學生");
            System.out.println("7. 統計資訊");
            System.out.println("0. 離開系統");
            System.out.print("請選擇功能：");
            
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    displayAllStudents();
                    break;
                case 2:
                    addStudent();
                    break;
                case 3:
                    searchStudent();
                    break;
                case 4:
                    updateStudent();
                    break;
                case 5:
                    deleteStudent();
                    break;
                case 6:
                    sortStudents();
                    break;
                case 7:
                    displayStatistics();
                    break;
                case 0:
                    System.out.println("感謝使用學生資訊管理系統！");
                    return;
                default:
                    System.out.println("無效選擇，請重新輸入！");
            }
        }
    }
    
    public static void main(String[] args) {
        StudentManager manager = new StudentManager();
        manager.showMenu();
    }
}
```

---

## 🧮 4.4 常見陣列演算法

### **排序演算法**
```java name=SortingAlgorithms.java
import java.util.Arrays;
import java.util.Random;

public class SortingAlgorithms {
    
    // 顯示陣列
    public static void printArray(int[] array, String title) {
        System.out.print(title + ": ");
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
    
    // 泡沫排序 (Bubble Sort)
    public static void bubbleSort(int[] array) {
        int n = array.length;
        boolean swapped;
        
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            
            for (int j = 0; j < n - 1 - i; j++) {
                if (array[j] > array[j + 1]) {
                    // 交換元素
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                    swapped = true;
                }
            }
            
            // 如果這一輪沒有交換，表示已經排序完成
            if (!swapped) {
                break;
            }
        }
    }
    
    // 選擇排序 (Selection Sort)
    public static void selectionSort(int[] array) {
        int n = array.length;
        
        for (int i = 0; i < n - 1; i++) {
            // 找到最小元素的索引
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }
            
            // 交換最小元素與當前元素
            if (minIndex != i) {
                int temp = array[i];
                array[i] = array[minIndex];
                array[minIndex] = temp;
            }
        }
    }
    
    // 插入排序 (Insertion Sort)
    public static void insertionSort(int[] array) {
        int n = array.length;
        
        for (int i = 1; i < n; i++) {
            int key = array[i];
            int j = i - 1;
            
            // 將 key 插入到已排序的部分中的正確位置
            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j--;
            }
            
            array[j + 1] = key;
        }
    }
    
    // 快速排序 (Quick Sort)
    public static void quickSort(int[] array, int low, int high) {
        if (low < high) {
            // 分割陣列，獲得樞紐位置
            int pivotIndex = partition(array, low, high);
            
            // 遞迴排序樞紐左邊和右邊的子陣列
            quickSort(array, low, pivotIndex - 1);
            quickSort(array, pivotIndex + 1, high);
        }
    }
    
    private static int partition(int[] array, int low, int high) {
        int pivot = array[high]; // 選擇最後一個元素作為樞紐
        int i = low - 1; // 較小元素的索引
        
        for (int j = low; j < high; j++) {
            if (array[j] <= pivot) {
                i++;
                // 交換元素
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        
        // 將樞紐放到正確位置
        int temp = array[i + 1];
        array[i + 1] = array[high];
        array[high] = temp;
        
        return i + 1;
    }
    
    // 合併排序 (Merge Sort)
    public static void mergeSort(int[] array, int left, int right) {
        if (left < right) {
            int middle = (left + right) / 2;
            
            // 遞迴排序左半部分
            mergeSort(array, left, middle);
            // 遞迴排序右半部分
            mergeSort(array, middle + 1, right);
            
            // 合併兩個已排序的部分
            merge(array, left, middle, right);
        }
    }
    
    private static void merge(int[] array, int left, int middle, int right) {
        // 計算子陣列的大小
        int leftSize = middle - left + 1;
        int rightSize = right - middle;
        
        // 建立暫存陣列
        int[] leftArray = new int[leftSize];
        int[] rightArray = new int[rightSize];
        
        // 複製資料到暫存陣列
        System.arraycopy(array, left, leftArray, 0, leftSize);
        System.arraycopy(array, middle + 1, rightArray, 0, rightSize);
        
        // 合併暫存陣列
        int i = 0, j = 0, k = left;
        
        while (i < leftSize && j < rightSize) {
            if (leftArray[i] <= rightArray[j]) {
                array[k] = leftArray[i];
                i++;
            } else {
                array[k] = rightArray[j];
                j++;
            }
            k++;
        }
        
        // 複製剩餘元素
        while (i < leftSize) {
            array[k] = leftArray[i];
            i++;
            k++;
        }
        
        while (j < rightSize) {
            array[k] = rightArray[j];
            j++;
            k++;
        }
    }
    
    // 測試排序演算法效能
    public static void testSortingPerformance() {
        int[] sizes = {1000, 5000, 10000};
        
        System.out.println("=== 排序演算法效能測試 ===");
        System.out.printf("%-15s %-10s %-10s %-10s\n", "演算法", "1000", "5000", "10000");
        System.out.println("-----------------------------------------------");
        
        for (int size : sizes) {
            // 生成隨機陣列
            int[] originalArray = generateRandomArray(size);
            
            // 測試各種排序演算法
            if (size <= 5000) { // 泡沫排序太慢，只測試小陣列
                int[] bubbleArray = originalArray.clone();
                long startTime = System.currentTimeMillis();
                bubbleSort(bubbleArray);
                long bubbleTime = System.currentTimeMillis() - startTime;
                
                if (size == 1000) {
                    System.out.printf("%-15s %-10d", "泡沫排序", bubbleTime);
                } else if (size == 5000) {
                    System.out.printf(" %-10d", bubbleTime);
                }
            }
        }
        System.out.println();
        
        // 測試其他演算法
        for (int size : sizes) {
            int[] originalArray = generateRandomArray(size);
            
            // 選擇排序
            int[] selectionArray = originalArray.clone();
            long startTime = System.currentTimeMillis();
            selectionSort(selectionArray);
            long selectionTime = System.currentTimeMillis() - startTime;
            
            if (size == 1000) {
                System.out.printf("%-15s %-10d", "選擇排序", selectionTime);
            } else {
                System.out.printf(" %-10d", selectionTime);
            }
        }
        System.out.println();
        
        for (int size : sizes) {
            int[] originalArray = generateRandomArray(size);
            
            // 插入排序
            int[] insertionArray = originalArray.clone();
            long startTime = System.currentTimeMillis();
            insertionSort(insertionArray);
            long insertionTime = System.currentTimeMillis() - startTime;
            
            if (size == 1000) {
                System.out.printf("%-15s %-10d", "插入排序", insertionTime);
            } else {
                System.out.printf(" %-10d", insertionTime);
            }
        }
        System.out.println();
        
        for (int size : sizes) {
            int[] originalArray = generateRandomArray(size);
            
            // 快速排序
            int[] quickArray = originalArray.clone();
            long startTime = System.currentTimeMillis();
            quickSort(quickArray, 0, quickArray.length - 1);
            long quickTime = System.currentTimeMillis() - startTime;
            
            if (size == 1000) {
                System.out.printf("%-15s %-10d", "快速排序", quickTime);
            } else {
                System.out.printf(" %-10d", quickTime);
            }
        }
        System.out.println();
        
        for (int size : sizes) {
            int[] originalArray = generateRandomArray(size);
            
            // 合併排序
            int[] mergeArray = originalArray.clone();
            long startTime = System.currentTimeMillis();
            mergeSort(mergeArray, 0, mergeArray.length - 1);
            long mergeTime = System.currentTimeMillis() - startTime;
            
            if (size == 1000) {
                System.out.printf("%-15s %-10d", "合併排序", mergeTime);
            } else {
                System.out.printf(" %-10d", mergeTime);
            }
        }
        System.out.println();
        
        for (int size : sizes) {
            int[] originalArray = generateRandomArray(size);
            
            // Arrays.sort (Java 內建)
            int[] javaArray = originalArray.clone();
            long startTime = System.currentTimeMillis();
            Arrays.sort(javaArray);
            long javaTime = System.currentTimeMillis() - startTime;
            
            if (size == 1000) {
                System.out.printf("%-15s %-10d", "Java內建排序", javaTime);
            } else {
                System.out.printf(" %-10d", javaTime);
            }
        }
        System.out.println();
    }
    
    // 生成隨機陣列
    private static int[] generateRandomArray(int size) {
        Random random = new Random();
        int[] array = new int[size];
        
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(1000);
        }
        
        return array;
    }
    
    public static void main(String[] args) {
        // 示範各種排序演算法
        int[] testArray = {64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42};
        
        System.out.println("=== 排序演算法示範 ===");
        printArray(testArray, "原始陣列");
        
        // 泡沫排序
        int[] bubbleArray = testArray.clone();
        bubbleSort(bubbleArray);
        printArray(bubbleArray, "泡沫排序結果");
        
        // 選擇排序
        int[] selectionArray = testArray.clone();
        selectionSort(selectionArray);
        printArray(selectionArray, "選擇排序結果");
        
        // 插入排序
        int[] insertionArray = testArray.clone();
        insertionSort(insertionArray);
        printArray(insertionArray, "插入排序結果");
        
        // 快速排序
        int[] quickArray = testArray.clone();
        quickSort(quickArray, 0, quickArray.length - 1);
        printArray(quickArray, "快速排序結果");
        
        // 合併排序
        int[] mergeArray = testArray.clone();
        mergeSort(mergeArray, 0, mergeArray.length - 1);
        printArray(mergeArray, "合併排序結果");
        
        System.out.println();
        
        // 效能測試
        testSortingPerformance();
    }
}
```

### **搜尋演算法**
```java name=SearchAlgorithms.java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class SearchAlgorithms {
    
    // 線性搜尋 (Linear Search)
    public static int linearSearch(int[] array, int target) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) {
                return i;
            }
        }
        return -1; // 找不到
    }
    
    // 線性搜尋 - 找到所有匹配的索引
    public static ArrayList<Integer> linearSearchAll(int[] array, int target) {
        ArrayList<Integer> indices = new ArrayList<>();
        
        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) {
                indices.add(i);
            }
        }
        
        return indices;
    }
    
    // 二分搜尋 (Binary Search) - 遞迴版本
    public static int binarySearchRecursive(int[] array, int target, int left, int right) {
        if (left > right) {
            return -1; // 找不到
        }
        
        int middle = left + (right - left) / 2;
        
        if (array[middle] == target) {
            return middle;
        } else if (array[middle] > target) {
            return binarySearchRecursive(array, target, left, middle - 1);
        } else {
            return binarySearchRecursive(array, target, middle + 1, right);
        }
    }
    
    // 二分搜尋 (Binary Search) - 迴圈版本
    public static int binarySearchIterative(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;
        
        while (left <= right) {
            int middle = left + (right - left) / 2;
            
            if (array[middle] == target) {
                return middle;
            } else if (array[middle] > target) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        
        return -1; // 找不到
    }
    
    // 找到目標值第一次出現的位置
    public static int findFirst(int[] array, int target) {
        int result = -1;
        int left = 0;
        int right = array.length - 1;
        
        while (left <= right) {
            int middle = left + (right - left) / 2;
            
            if (array[middle] == target) {
                result = middle;
                right = middle - 1; // 繼續向左搜尋
            } else if (array[middle] > target) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        
        return result;
    }
    
    // 找到目標值最後一次出現的位置
    public static int findLast(int[] array, int target) {
        int result = -1;
        int left = 0;
        int right = array.length - 1;
        
        while (left <= right) {
            int middle = left + (right - left) / 2;
            
            if (array[middle] == target) {
                result = middle;
                left = middle + 1; // 繼續向右搜尋
            } else if (array[middle] > target) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        
        return result;
    }
    
    // 在排序陣列中統計目標值出現的次數
    public static int countOccurrences(int[] array, int target) {
        int first = findFirst(array, target);
        if (first == -1) {
            return 0;
        }
        
        int last = findLast(array, target);
        return last - first + 1;
    }
    
    // 在排序陣列中找到小於等於目標值的最大元素
    public static int findFloor(int[] array, int target) {
        int result = -1;
        int left = 0;
        int right = array.length - 1;
        
        while (left <= right) {
            int middle = left + (right - left) / 2;
            
            if (array[middle] <= target) {
                result = middle;
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        
        return result;
    }
    
    // 在排序陣列中找到大於等於目標值的最小元素
    public static int findCeiling(int[] array, int target) {
        int result = -1;
        int left = 0;
        int right = array.length - 1;
        
        while (left <= right) {
            int middle = left + (right - left) / 2;
            
            if (array[middle] >= target) {
                result = middle;
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        
        return result;
    }
    
    // 搜尋效能測試
    public static void searchPerformanceTest() {
        System.out.println("=== 搜尋演算法效能測試 ===");
        
        int[] sizes = {10000, 50000, 100000};
        
        for (int size : sizes) {
            // 建立排序陣列
            int[] array = new int[size];
            for (int i = 0; i < size; i++) {
                array[i] = i * 2; // 建立連續偶數陣列
            }
            
            int target = size; // 搜尋目標
            
            // 線性搜尋測試
            long startTime = System.nanoTime();
            int linearResult = linearSearch(array, target);
            long linearTime = System.nanoTime() - startTime;
            
            // 二分搜尋測試
            startTime = System.nanoTime();
            int binaryResult = binarySearchIterative(array, target);
            long binaryTime = System.nanoTime() - startTime;
            
            // Java 內建二分搜尋
            startTime = System.nanoTime();
            int javaResult = Arrays.binarySearch(array, target);
            long javaTime = System.nanoTime() - startTime;
            
            System.out.printf("陣列大小: %d\n", size);
            System.out.printf("線性搜尋: %d ns (結果: %d)\n", linearTime, linearResult);
            System.out.printf("二分搜尋: %d ns (結果: %d)\n", binaryTime, binaryResult);
            System.out.printf("Java內建: %d ns (結果: %d)\n", javaTime, javaResult);
            System.out.println("---");
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 測試陣列
        int[] unsortedArray = {64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42, 25, 11, 76};
        int[] sortedArray = {11, 11, 12, 22, 25, 25, 34, 42, 50, 64, 76, 76, 88, 90};
        
        System.out.println("=== 搜尋演算法示範 ===");
        System.out.println("未排序陣列: " + Arrays.toString(unsortedArray));
        System.out.println("已排序陣列: " + Arrays.toString(sortedArray));
        
        while (true) {
            System.out.println("\n=== 搜尋選單 ===");
            System.out.println("1. 線性搜尋（未排序陣列）");
            System.out.println("2. 線性搜尋所有匹配");
            System.out.println("3. 二分搜尋（遞迴版本）");
            System.out.println("4. 二分搜尋（迴圈版本）");
            System.out.println("5. 找到第一個出現位置");
            System.out.println("6. 找到最後一個出現位置");
            System.out.println("7. 統計出現次數");
            System.out.println("8. 找到 Floor 值");
            System.out.println("9. 找到 Ceiling 值");
            System.out.println("10. 效能測試");
            System.out.println("0. 離開");
            System.out.print("請選擇功能：");
            
            int choice = scanner.nextInt();
            
            if (choice == 0) {
                break;
            }
            
            if (choice == 10) {
                searchPerformanceTest();
                continue;
            }
            
            System.out.print("請輸入要搜尋的數字：");
            int target = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    int linearResult = linearSearch(unsortedArray, target);
                    if (linearResult != -1) {
                        System.out.println("線性搜尋：找到 " + target + " 在索引 " + linearResult);
                    } else {
                        System.out.println("線性搜尋：找不到 " + target);
                    }
                    break;
                    
                case 2:
                    ArrayList<Integer> allResults = linearSearchAll(unsortedArray, target);
                    if (!allResults.isEmpty()) {
                        System.out.println("找到 " + target + " 在以下索引：" + allResults);
                    } else {
                        System.out.println("找不到 " + target);
                    }
                    break;
                    
                case 3:
                    int binaryRecursiveResult = binarySearchRecursive(sortedArray, target, 0, sortedArray.length - 1);
                    if (binaryRecursiveResult != -1) {
                        System.out.println("二分搜尋（遞迴）：找到 " + target + " 在索引 " + binaryRecursiveResult);
                    } else {
                        System.out.println("二分搜尋（遞迴）：找不到 " + target);
                    }
                    break;
                    
                case 4:
                    int binaryIterativeResult = binarySearchIterative(sortedArray, target);
                    if (binaryIterativeResult != -1) {
                        System.out.println("二分搜尋（迴圈）：找到 " + target + " 在索引 " + binaryIterativeResult);
                    } else {
                        System.out.println("二分搜尋（迴圈）：找不到 " + target);
                    }
                    break;
                    
                case 5:
                    int firstOccurrence = findFirst(sortedArray, target);
                    if (firstOccurrence != -1) {
                        System.out.println(target + " 第一次出現在索引 " + firstOccurrence);
                    } else {
                        System.out.println("找不到 " + target);
                    }
                    break;
                    
                case 6:
                    int lastOccurrence = findLast(sortedArray, target);
                    if (lastOccurrence != -1) {
                        System.out.println(target + " 最後一次出現在索引 " + lastOccurrence);
                    } else {
                        System.out.println("找不到 " + target);
                    }
                    break;
                    
                case 7:
                    int count = countOccurrences(sortedArray, target);
                    System.out.println(target + " 總共出現 " + count + " 次");
                    break;
                    
                case 8:
                    int floorIndex = findFloor(sortedArray, target);
                    if (floorIndex != -1) {
                        System.out.println("小於等於 " + target + " 的最大值是 " + 
                                         sortedArray[floorIndex] + "（索引 " + floorIndex + "）");
                    } else {
                        System.out.println("沒有小於等於 " + target + " 的元素");
                    }
                    break;
                    
                case 9:
                    int ceilingIndex = findCeiling(sortedArray, target);
                    if (ceilingIndex != -1) {
                        System.out.println("大於等於 " + target + " 的最小值是 " + 
                                         sortedArray[ceilingIndex] + "（索引 " + ceilingIndex + "）");
                    } else {
                        System.out.println("沒有大於等於 " + target + " 的元素");
                    }
                    break;
                    
                default:
                    System.out.println("無效選擇");
            }
        }
        
        scanner.close();
    }
}
```

---

## 🎮 4.5 綜合實作專案：俄羅斯方塊（簡化版）

```java name=SimpleTetris.java
import java.util.Random;
import java.util.Scanner;

public class SimpleTetris {
    // 遊戲板設定
    private static final int BOARD_WIDTH = 10;
    private static final int BOARD_HEIGHT = 20;
    private static final char EMPTY = '.';
    private static final char FILLED = '#';
    
    // 遊戲狀態
    private char[][] board;
    private int score;
    private int linesCleared;
    private Random random;
    private Scanner scanner;
    
    // 方塊類型（簡化版，只有 I, O, T, L 四種）
    private static final char[][][] PIECES = {
        // I 方塊
        {
            {'#', '#', '#', '#'}
        },
        // O 方塊
        {
            {'#', '#'},
            {'#', '#'}
        },
        // T 方塊
        {
            {'.', '#', '.'},
            {'#', '#', '#'}
        },
        // L 方塊
        {
            {'#', '.', '.'},
            {'#', '#', '#'}
        }
    };
    
    public SimpleTetris() {
        board = new char[BOARD_HEIGHT][BOARD_WIDTH];
        score = 0;
        linesCleared = 0;
        random = new Random();
        scanner = new Scanner(System.in);
        initializeBoard();
    }
    
    // 初始化遊戲板
    private void initializeBoard() {
        for (int i = 0; i < BOARD_HEIGHT; i++) {
            for (int j = 0; j < BOARD_WIDTH; j++) {
                board[i][j] = EMPTY;
            }
        }
    }
    
    // 顯示遊戲板
    private void displayBoard() {
        System.out.println("\n=== 簡化版俄羅斯方塊 ===");
        System.out.println("分數: " + score + " | 消除行數: " + linesCleared);
        System.out.println();
        
        // 顯示列號
        System.out.print("  ");
        for (int j = 0; j < BOARD_WIDTH; j++) {
            System.out.print(j % 10);
        }
        System.out.println();
        
        // 顯示遊戲板
        for (int i = 0; i < BOARD_HEIGHT; i++) {
            System.out.printf("%2d", i);
            for (int j = 0; j < BOARD_WIDTH; j++) {
                System.out.print(board[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }
    
    // 檢查位置是否有效
    private boolean isValidPosition(char[][] piece, int row, int col) {
        for (int i = 0; i < piece.length; i++) {
            for (int j = 0; j < piece[i].length; j++) {
                if (piece[i][j] == FILLED) {
                    int boardRow = row + i;
                    int boardCol = col + j;
                    
                    // 檢查邊界
                    if (boardRow < 0 || boardRow >= BOARD_HEIGHT || 
                        boardCol < 0 || boardCol >= BOARD_WIDTH) {
                        return false;
                    }
                    
                    // 檢查是否與已有方塊重疊
                    if (board[boardRow][boardCol] == FILLED) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
    
    // 放置方塊到遊戲板
    private void placePiece(char[][] piece, int row, int col) {
        for (int i = 0; i < piece.length; i++) {
            for (int j = 0; j < piece[i].length; j++) {
                if (piece[i][j] == FILLED) {
                    board[row + i][col + j] = FILLED;
                }
            }
        }
    }
    
    // 檢查並清除滿行
    private void clearFullLines() {
        int linesCleared = 0;
        
        for (int i = BOARD_HEIGHT - 1; i >= 0; i--) {
            boolean isFull = true;
            
            // 檢查這一行是否滿了
            for (int j = 0; j < BOARD_WIDTH; j++) {
                if (board[i][j] == EMPTY) {
                    isFull = false;
                    break;
                }
            }
            
            if (isFull) {
                // 清除這一行，並將上面的行下移
                for (int k = i; k > 0; k--) {
                    System.arraycopy(board[k - 1], 0, board[k], 0, BOARD_WIDTH);
                }
                
                // 清空最上面一行
                for (int j = 0; j < BOARD_WIDTH; j++) {
                    board[0][j] = EMPTY;
                }
                
                linesCleared++;
                i++; // 重新檢查同一行（因為上面的行下移了）
            }
        }
        
        if (linesCleared > 0) {
            this.linesCleared += linesCleared;
            
            // 計分系統
            int points = 0;
            switch (linesCleared) {
                case 1: points = 100; break;
                case 2: points = 300; break;
                case 3: points = 500; break;
                case 4: points = 800; break;
            }
            
            score += points;
            
            System.out.println("🎉 消除了 " + linesCleared + " 行！獲得 " + points + " 分！");
        }
    }
    
    // 檢查遊戲是否結束
    private boolean isGameOver() {
        // 檢查頂部是否有方塊
        for (int j = 0; j < BOARD_WIDTH; j++) {
            if (board[0][j] == FILLED) {
                return true;
            }
        }
        return false;
    }
    
    // 隨機生成方塊
    private char[][] getRandomPiece() {
        int pieceType = random.nextInt(PIECES.length);
        char[][] originalPiece = PIECES[pieceType];
        
        // 複製方塊（避免修改原始資料）
        char[][] piece = new char[originalPiece.length][originalPiece[0].length];
        for (int i = 0; i < originalPiece.length; i++) {
            System.arraycopy(originalPiece[i], 0, piece[i], 0, originalPiece[i].length);
        }
        
        return piece;
    }
    
    // 顯示方塊
    private void displayPiece(char[][] piece, String title) {
        System.out.println(title + ":");
        for (char[] row : piece) {
            for (char cell : row) {
                System.out.print(cell);
            }
            System.out.println();
        }
        System.out.println();
    }
    
    // 旋轉方塊（順時針 90 度）
    private char[][] rotatePiece(char[][] piece) {
        int rows = piece.length;
        int cols = piece[0].length;
        char[][] rotated = new char[cols][rows];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                rotated[j][rows - 1 - i] = piece[i][j];
            }
        }
        
        return rotated;
    }
    
    // 玩家輸入
    private int getPlayerInput(String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);
            try {
                int input = scanner.nextInt();
                if (input >= min && input <= max) {
                    return input;
                } else {
                    System.out.println("請輸入 " + min + " 到 " + max + " 之間的數字");
                }
            } catch (Exception e) {
                System.out.println("請輸入有效的數字");
                scanner.nextLine(); // 清除錯誤輸入
            }
        }
    }
    
    // 模擬方塊下落
    private int simulateDrop(char[][] piece, int col) {
        int row = 0;
        
        // 找到方塊可以放置的最下面位置
        while (row < BOARD_HEIGHT && isValidPosition(piece, row, col)) {
            row++;
        }
        
        return row - 1; // 返回最後一個有效位置
    }
    
    // 人工智慧建議
    private void suggestBestMove(char[][] piece) {
        int bestCol = 0;
        int bestScore = -1;
        
        // 嘗試所有可能的列位置
        for (int col = 0; col <= BOARD_WIDTH - piece[0].length; col++) {
            if (isValidPosition(piece, 0, col)) {
                int dropRow = simulateDrop(piece, col);
                
                // 簡單評分：越靠近底部越好，越能消除行越好
                int positionScore = BOARD_HEIGHT - dropRow;
                
                // 檢查這個位置是否能形成滿行
                char[][] tempBoard = new char[BOARD_HEIGHT][BOARD_WIDTH];
                for (int i = 0; i < BOARD_HEIGHT; i++) {
                    System.arraycopy(board[i], 0, tempBoard[i], 0, BOARD_WIDTH);
                }
                
                // 模擬放置方塊
                for (int i = 0; i < piece.length; i++) {
                    for (int j = 0; j < piece[i].length; j++) {
                        if (piece[i][j] == FILLED) {
                            tempBoard[dropRow + i][col + j] = FILLED;
                        }
                    }
                }
                
                // 檢查能消除多少行
                int possibleLines = 0;
                for (int row = 0; row < BOARD_HEIGHT; row++) {
                    boolean isFull = true;
                    for (int c = 0; c < BOARD_WIDTH; c++) {
                        if (tempBoard[row][c] == EMPTY) {
                            isFull = false;
                            break;
                        }
                    }
                    if (isFull) possibleLines++;
                }
                
                int totalScore = positionScore + possibleLines * 1000;
                
                if (totalScore > bestScore) {
                    bestScore = totalScore;
                    bestCol = col;
                }
            }
        }
        
        System.out.println("💡 AI 建議：放在第 " + bestCol + " 列");
    }
    
    // 顯示遊戲說明
    private void showInstructions() {
        System.out.println("=== 遊戲說明 ===");
        System.out.println("1. 方塊會從頂部落下");
        System.out.println("2. 選擇方塊的列位置（0-9）");
        System.out.println("3. 可以選擇是否旋轉方塊");
        System.out.println("4. 填滿一整行會消除該行並得分");
        System.out.println("5. 頂部被方塊填滿時遊戲結束");
        System.out.println("6. 消除多行同時可獲得更高分數");
        System.out.println();
    }
    
    // 主要遊戲循環
    public void playGame() {
        showInstructions();
        
        while (!isGameOver()) {
            displayBoard();
            
            // 生成新方塊
            char[][] currentPiece = getRandomPiece();
            displayPiece(currentPiece, "當前方塊");
            
            // 詢問是否旋轉
            System.out.print("是否要旋轉方塊？(y/n): ");
            String rotateChoice = scanner.next();
            
            if (rotateChoice.toLowerCase().equals("y")) {
                char[][] rotatedPiece = rotatePiece(currentPiece);
                
                // 檢查旋轉後是否還能放置
                boolean canPlace = false;
                for (int col = 0; col <= BOARD_WIDTH - rotatedPiece[0].length; col++) {
                    if (isValidPosition(rotatedPiece, 0, col)) {
                        canPlace = true;
                        break;
                    }
                }
                
                if (canPlace) {
                    currentPiece = rotatedPiece;
                    displayPiece(currentPiece, "旋轉後的方塊");
                } else {
                    System.out.println("❌ 旋轉後無法放置，使用原方塊");
                }
            }
            
            // AI 建議
            suggestBestMove(currentPiece);
            
            // 獲取玩家選擇的列位置
            int maxCol = BOARD_WIDTH - currentPiece[0].length;
            int selectedCol = getPlayerInput(
                "請選擇放置的列位置 (0-" + maxCol + "): ", 
                0, maxCol
            );
            
            // 檢查選擇的位置是否有效
            if (!isValidPosition(currentPiece, 0, selectedCol)) {
                System.out.println("❌ 遊戲結束！無法放置新方塊！");
                break;
            }
            
            // 模擬方塊下落
            int finalRow = simulateDrop(currentPiece, selectedCol);
            
            // 放置方塊
            placePiece(currentPiece, finalRow, selectedCol);
            
            // 檢查並清除滿行
            clearFullLines();
            
            // 顯示放置後的結果
            System.out.println("方塊已放置在第 " + finalRow + " 行，第 " + selectedCol + " 列");
        }
        
        // 遊戲結束
        displayBoard();
        System.out.println("🎮 遊戲結束！");
        System.out.println("最終分數：" + score);
        System.out.println("消除行數：" + linesCleared);
        
        // 評分
        if (score >= 1000) {
            System.out.println("🏆 優秀！");
        } else if (score >= 500) {
            System.out.println("👍 不錯！");
        } else {
            System.out.println("💪 繼續努力！");
        }
        
        // 詢問是否重新開始
        System.out.print("要重新開始嗎？(y/n): ");
        String playAgain = scanner.next();
        
        if (playAgain.toLowerCase().equals("y")) {
            initializeBoard();
            score = 0;
            linesCleared = 0;
            playGame();
        }
    }
    
    public static void main(String[] args) {
        SimpleTetris game = new SimpleTetris();
        game.playGame();
    }
}
```

---

## 📝 重點整理

### **陣列與 ArrayList 比較**
| 特性 | 傳統陣列 | ArrayList |
|------|----------|-----------|
| 大小 | 固定 | 動態 |
| 效能 | 較好 | 稍慢 |
| 資料型別 | 所有型別 | 只能存物件 |
| 方法 | 基本操作 | 豐富的方法 |
| 記憶體 | 連續分配 | 可能不連續 |

### **演算法複雜度**
| 演算法 | 時間複雜度 | 空間複雜度 |
|--------|------------|------------|
| 線性搜尋 | O(n) | O(1) |
| 二分搜尋 | O(log n) | O(1) |
| 泡沫排序 | O(n²) | O(1) |
| 快速排序 | O(n log n) | O(log n) |
| 合併排序 | O(n log n) | O(n) |

### **最佳實踐**
1. **陣列大小已知且固定時使用傳統陣列**
2. **需要動態增減元素時使用 ArrayList**
3. **大量搜尋操作時保持陣列排序**
4. **選擇適合的排序演算法**
5. **注意陣列邊界檢查**

---

## 🏠 課後作業

### **作業 1：圖書館管理系統**
使用 ArrayList 建立圖書館管理系統：
- 圖書資訊管理（新增、刪除、修改）
- 多條件搜尋功能
- 借還書記錄
- 統計報表

### **作業 2：成績分析工具**
建立二維陣列成績分析系統：
- 多科目多學生成績管理
- 各科平均分、排名
- 學生總分排名
- 成績分布圖表

### **作業 3：簡易遊戲開發**
選擇實作以下遊戲之一：
- 踩地雷
- 貪食蛇
- 拼圖遊戲
- 數獨求解器

---

## 🔍 實用技巧

### **陣列除錯技巧**
```java
// 快速顯示陣列內容
int[] array = {1, 2, 3, 4, 5};
System.out.println(Arrays.toString(array));

// 顯示二維陣列
int[][] matrix = {{1, 2}, {3, 4}};
System.out.println(Arrays.deepToString(matrix));

// 陣列邊界檢查
public static boolean isValidIndex(int[] array, int index) {
    return index >= 0 && index < array.length;
}
```

### **效能優化建議**
1. **預先分配 ArrayList 容量**：`new ArrayList<>(expectedSize)`
2. **使用增強型 for 迴圈**：避免索引錯誤且效能更好
3. **大資料集使用二分搜尋**：排序一次，多次快速搜尋
4. **避免頻繁的陣列複製操作**

通過第四單元的學習，學生將掌握陣列和基本資料結構的使用，為後續學習更複雜的資料結構和演算法打下堅實的基礎。這些知識在實際開發中非常重要，幾乎每個程式都會用到陣列相關的操作。

需要我繼續第五單元或者針對某個特定概念做更深入的講解嗎？

