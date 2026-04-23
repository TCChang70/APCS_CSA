````markdown name=Unit04_Arrays_and_Collections.md
# 第四單元：陣列與資料結構（Arrays 與 ArrayList）- 深入教學

本單元將帶你從基礎到進階，完整掌握 Java 陣列與動態集合 ArrayList 的使用、內部原理、效能考量與常見坑，並透過大量範例與練習鞏固觀念。

## 🎯 學習目標
- 了解一維與二維（陣列的陣列）在記憶體與語法上的差異
- 熟悉陣列的宣告、初始化、遍歷、複製、排序與搜尋
- 掌握 ArrayList 的泛型用法、常見操作、迭代與移除元素的正確姿勢
- 了解 Arrays 與 Collections 常用工具方法與時間複雜度
- 能針對情境選擇「陣列」或「ArrayList」，並避免常見錯誤

---

## 4.1 一維陣列（1D Array）

### 4.1.1 觀念與特性
- 陣列是固定長度、連續記憶體的容器；長度一旦建立就不能改變。
- 索引從 0 開始到 length - 1。
- 元素類型一致，可為基本型別或參考型別。
- 預設值：
  - 數值型：0、0.0
  - 布林：false
  - 參考型：null
  - 字元：'\u0000'

### 4.1.2 宣告與初始化
```java
int[] a;                 // 建議寫法
a = new int[5];          // [0,0,0,0,0]
int[] b = {1, 2, 3};     // 直寫初始化
String[] names = new String[3]; // [null, null, null]
```

常見例外：ArrayIndexOutOfBoundsException（索引越界）

### 4.1.3 遍歷與操作
- 索引 for：適合需索引或改值
- 增強 for-each：簡潔，但不可改變元素（對基本型別）/不提供索引

```java
for (int i = 0; i < a.length; i++) { /* ... */ }
for (int v : a) { /* 讀取用，不能直接改 a 的值 */ }
```

### 4.1.4 常用工具與實務
- 填值：Arrays.fill(arr, value)
- 複製：
  - Arrays.copyOf(arr, newLen)
  - System.arraycopy(src, srcPos, dst, dstPos, len)
- 相等比較：
  - arr1 == arr2 比較參考位址
  - Arrays.equals(arr1, arr2) 比較內容
- 排序與搜尋：
  - Arrays.sort(arr) 為原地排序（快排/雙軸快排/TimSort 視型別）
  - Arrays.binarySearch(arr, key) 需「已排序」，否則結果未定義

### 4.1.5 參考語意與淺/深拷貝
- 陣列變數是「參考」。賦值只複製參考，兩者指向同一塊記憶體。
- 對於元素為參考型別的陣列，Arrays.copyOf 是「淺拷貝」（只複製參考）。
- 深拷貝需逐一複製元素內部物件。

---

## 4.2 二維陣列（2D Array，實為陣列的陣列）

### 4.2.1 觀念
- Java 的 2D 陣列是「int[][]」＝一個元素為 int[] 的陣列。
- 可不規則（Jagged）：每列長度可不同。

```java
int[][] m = new int[3][4];       // 規則 3x4
int[][] j = new int[3][];        // 先列數，再逐列配置
j[0] = new int[1];
j[1] = new int[3];
j[2] = new int[2];
```

### 4.2.2 遍歷範式
```java
for (int i = 0; i < m.length; i++) {
    for (int j2 = 0; j2 < m[i].length; j2++) {
        // 使用 m[i][j2]
    }
}

// For-each
for (int[] row : m) {
    for (int v : row) {
        // 使用 v
    }
}
```

### 4.2.3 常見任務
- 列/行加總、對角線和
- 鄰居掃描（上下左右與對角）
- 矩陣乘法（O(n^3) 標準法）

注意：未初始化的列為 null，直接 m[i][j] 會 NullPointerException。

---

## 4.3 ArrayList（動態陣列）

### 4.3.1 觀念與泛型
- 動態調整容量的陣列實作 List 介面。
- 僅能存放參考型別：整數用 Integer，浮點用 Double（自動裝箱/拆箱）。

```java
import java.util.ArrayList;
ArrayList<Integer> list = new ArrayList<>();
list.add(10);            // 自動裝箱：int -> Integer
int x = list.get(0);     // 自動拆箱：Integer -> int
```

### 4.3.2 常用方法
- 新增：add(e), add(index, e)
- 讀取/修改：get(i), set(i, e)
- 移除：remove(index), remove(Object o)
- 查詢：size(), isEmpty(), contains(o), indexOf(o), lastIndexOf(o)
- 其他：clear(), toArray(), subList(from, to)

易踩坑：
- remove 對 Integer：remove(1) 是移除索引 1；要移除值 1 用 remove(Integer.valueOf(1))
- Arrays.asList 產生固定長度 List，不能 add/remove
- subList 回傳「視圖」，原 List 變動會影響它（反之亦然），跨容器操作易拋 ConcurrentModificationException

### 4.3.3 迭代與安全移除
- for-each 迭代中直接 list.remove 會拋 ConcurrentModificationException
- 正確：使用 Iterator.remove()

```java
import java.util.Iterator;
Iterator<Integer> it = list.iterator();
while (it.hasNext()) {
    if (it.next() % 2 == 0) it.remove(); // 安全移除偶數
}
```

### 4.3.4 排序與比較器
```java
import java.util.*;
list.sort(Comparator.naturalOrder());             // 升冪
list.sort(Comparator.reverseOrder());             // 降冪

ArrayList<String> names = new ArrayList<>(List.of("Ann","bob","Cindy"));
names.sort(String.CASE_INSENSITIVE_ORDER);        // 不分大小寫
names.sort(Comparator.comparingInt(String::length).thenComparing(String::compareTo));
```

### 4.3.5 陣列與 List 轉換
```java
// 陣列 -> 可變 List
String[] arr = {"a","b","c"};
ArrayList<String> l1 = new ArrayList<>(java.util.Arrays.asList(arr));

// List -> 陣列
String[] arr2 = l1.toArray(new String[0]);
```

---

## 4.4 效能與選型建議

### 4.4.1 時間複雜度（常見操作）
- 陣列：索引存取 O(1)、插入/刪除（中間）O(n)、尋找（未排序）O(n)、二分搜尋（排序後）O(log n)
- ArrayList：末端 add 攤銷 O(1)、中間插刪 O(n)、get O(1)、contains O(n)

### 4.4.2 陣列 vs ArrayList
- 適合用陣列：
  - 固定長度、追求極致性能、基本型別大量數據、與原生 API/庫對接
- 適合用 ArrayList：
  - 尺寸變化、需要豐富操作（插入、移除、搜尋）、與 Collections 工具/Comparators 配合

---

## 4.5 常見陷阱總結
- Off-by-one：for (i <= length) 應為 < length
- 索引越界：IndexOutOfBoundsException
- 未初始化的 2D 列：NullPointerException
- equals vs Arrays.equals / Arrays.deepEquals
- Arrays.binarySearch 未排序先用會出錯（結果未定義）
- for-each 移除元素：使用 Iterator.remove()
- Integer remove 歧義：remove(int index) vs remove(Object o)
- Arrays.asList 固定長度（不可 add/remove）；List.of 不可變
- subList 視圖與原 List 共享資料，跨容器修改易出問題

---

## 4.6 練習題（由淺入深）
1) 陣列統計：輸入 N 個整數，輸出最小、最大、平均、媒數（median）。
2) 陣列去重：輸入整數陣列，回傳去重後且保留原順序的新陣列。
3) 二分搜尋：實作對排序陣列的 binarySearch（傳回索引或 -1）。
4) 旋轉陣列：將陣列右旋 k 次（原地 O(1) 空間，三次反轉法）。
5) 矩陣運算：實作矩陣加法、乘法與轉置。
6) 鄰居掃描：給定 0/1 2D 陣列，計算每格的 1 鄰居數（上下左右與對角共 8 鄰）。
7) 最長連續遞增子序列（陣列連續索引）：回傳長度與起訖索引。
8) ArrayList 排序：將學生物件按成績降冪、分數相同按姓名升冪。
9) 安全移除：從整數列表中移除所有奇數，要求不丟 ConcurrentModificationException。
10) 字詞統計（進階預告 Map）：計算一段文字每個單字出現次數，輸出 Top-K。

提示關鍵字：Arrays、System.arraycopy、reverse（三段反轉）、Iterator、Comparator、二分搜尋邏輯

---

## 4.7 小測驗（快速檢核）
- Q1：Arrays.equals 與 == 的差別？
- Q2：二分搜尋可用於未排序陣列嗎？為什麼？
- Q3：如何安全地在遍歷 List 時移除元素？
- Q4：Arrays.asList 與 new ArrayList<>(Arrays.asList(...)) 的差異？
- Q5：移除 Integer 值 1 為何可能意外變成移除索引 1？如何避免？

建議答案（簡述）：
- A1：equals 比內容，== 比參考（位址）
- A2：不可，二分搜尋前提是有序
- A3：使用 Iterator 的 remove()
- A4：前者固定長度；後者可變
- A5：因為有 remove(int) 重載；用 remove(Integer.valueOf(1))

---

## 4.8 延伸閱讀
- Java 官方文件：[Arrays](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html)、
  [ArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html)、
  [Collections](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html)
- 比較器：[Comparator](https://docs.oracle.com/javase/8/docs/api/java/util/Comparator.html)

---

## 附：教學示例程式
請參考本單元附檔：
- ArrayBasics.java：一維陣列常用操作、拷貝、排序、搜尋
- TwoDArrayExamples.java：二維陣列遍歷、鄰居掃描、矩陣乘法
- ArrayListExamples.java：常用方法、迭代與安全移除、排序與比較器

````

```java name=ArrayBasics.java
import java.util.Arrays;

public class ArrayBasics {

    // 統計：最小、最大、平均
    static double[] stats(int[] arr) {
        if (arr == null || arr.length == 0) throw new IllegalArgumentException("empty");
        int min = arr[0], max = arr[0];
        long sum = 0;
        for (int v : arr) {
            if (v < min) min = v;
            if (v > max) max = v;
            sum += v;
        }
        double avg = sum * 1.0 / arr.length;
        return new double[]{min, max, avg};
    }

    // 中位數（需要拷貝，以免改動原資料）
    static double median(int[] arr) {
        int[] copy = Arrays.copyOf(arr, arr.length);
        Arrays.sort(copy);
        int n = copy.length;
        if (n % 2 == 1) return copy[n / 2];
        return (copy[n / 2 - 1] + copy[n / 2]) / 2.0;
    }

    // 三段反轉：原地右旋 k
    static void rotateRight(int[] a, int k) {
        int n = a.length;
        k = ((k % n) + n) % n;
        reverse(a, 0, n - 1);
        reverse(a, 0, k - 1);
        reverse(a, k, n - 1);
    }
    static void reverse(int[] a, int l, int r) {
        while (l < r) {
            int t = a[l]; a[l] = a[r]; a[r] = t;
            l++; r--;
        }
    }

    // 自訂二分搜尋（回傳索引或 -1）
    static int binarySearch(int[] sorted, int key) {
        int l = 0, r = sorted.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (sorted[mid] == key) return mid;
            if (sorted[mid] < key) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] a = {7, 2, 9, 4, 4, 1};
        System.out.println("原陣列: " + Arrays.toString(a));

        // 拷貝（淺拷貝對基本型別即值複製）
        int[] b = Arrays.copyOf(a, a.length);
        System.out.println("拷貝   : " + Arrays.toString(b));

        // 排序 + 二分搜尋
        Arrays.sort(b);
        System.out.println("排序後 : " + Arrays.toString(b));
        System.out.println("搜尋 4 的索引: " + Arrays.binarySearch(b, 4));

        // 自訂二分搜尋
        System.out.println("自訂搜尋 9 的索引: " + binarySearch(b, 9));

        // 統計與中位數
        double[] s = stats(a);
        System.out.printf("最小=%.0f 最大=%.0f 平均=%.2f\n", s[0], s[1], s[2]);
        System.out.printf("中位數=%.2f\n", median(a));

        // 右旋
        rotateRight(a, 2);
        System.out.println("右旋 2 : " + Arrays.toString(a));

        // System.arraycopy 範例（區段複製）
        int[] dst = new int[10];
        System.arraycopy(b, 1, dst, 3, 3);
        System.out.println("arraycopy -> " + Arrays.toString(dst));
    }
}
```

```java name=TwoDArrayExamples.java
import java.util.Arrays;

public class TwoDArrayExamples {

    // 鄰居方向（8 向）
    static final int[][] DIR8 = {
        {-1,-1}, {-1,0}, {-1,1},
        { 0,-1},         { 0,1},
        { 1,-1}, { 1,0}, { 1,1}
    };

    // 計算每格周圍的 1 個數（雷同地雷鄰近數）
    static int[][] neighborOnes(int[][] grid) {
        int R = grid.length;
        int C = grid[0].length;
        int[][] ans = new int[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                int cnt = 0;
                for (int[] d : DIR8) {
                    int ni = i + d[0], nj = j + d[1];
                    if (ni >= 0 && ni < R && nj >= 0 && nj < C && grid[ni][nj] == 1) {
                        cnt++;
                    }
                }
                ans[i][j] = cnt;
            }
        }
        return ans;
    }

    // 矩陣乘法 A[R x K] * B[K x C] = C[R x C]
    static int[][] multiply(int[][] A, int[][] B) {
        int R = A.length, K = A[0].length, C = B[0].length;
        if (B.length != K) throw new IllegalArgumentException("維度不相容");
        int[][] M = new int[R][C];
        for (int i = 0; i < R; i++) {
            for (int k = 0; k < K; k++) {
                int aik = A[i][k];
                for (int j = 0; j < C; j++) {
                    M[i][j] += aik * B[k][j];
                }
            }
        }
        return M;
    }

    // 轉置
    static int[][] transpose(int[][] A) {
        int R = A.length, C = A[0].length;
        int[][] T = new int[C][R];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                T[j][i] = A[i][j];
            }
        }
        return T;
    }

    // 列/行和
    static int[] rowSums(int[][] A) {
        int R = A.length; int[] s = new int[R];
        for (int i = 0; i < R; i++) {
            int sum = 0;
            for (int v : A[i]) sum += v;
            s[i] = sum;
        }
        return s;
    }

    static int[] colSums(int[][] A) {
        int R = A.length, C = A[0].length;
        int[] s = new int[C];
        for (int j = 0; j < C; j++) {
            int sum = 0;
            for (int i = 0; i < R; i++) sum += A[i][j];
            s[j] = sum;
        }
        return s;
    }

    public static void main(String[] args) {
        int[][] grid = {
            {1,0,1},
            {0,1,0},
            {1,0,1}
        };
        System.out.println("鄰居 1 計數：");
        int[][] cnt = neighborOnes(grid);
        for (int[] row : cnt) System.out.println(Arrays.toString(row));

        int[][] A = {{1,2,3},{4,5,6}};
        int[][] B = {{7,8},{9,10},{11,12}};
        System.out.println("A*B：");
        int[][] M = multiply(A, B);
        for (int[] row : M) System.out.println(Arrays.toString(row));

        System.out.println("轉置(B)：");
        int[][] TB = transpose(B);
        for (int[] row : TB) System.out.println(Arrays.toString(row));

        System.out.println("列和：" + Arrays.toString(rowSums(A)));
        System.out.println("行和：" + Arrays.toString(colSums(A)));
    }
}
```

```java name=ArrayListExamples.java
import java.util.*;

class Student {
    final String name;
    final int score;
    Student(String name, int score) { this.name = name; this.score = score; }
    @Override public String toString() { return name + "(" + score + ")"; }
}

public class ArrayListExamples {

    static void basicOps() {
        ArrayList<String> list = new ArrayList<>();
        list.add("Ann");
        list.add("Bob");
        list.add(1, "Cindy"); // 插入索引 1
        System.out.println("list: " + list); // [Ann, Cindy, Bob]

        // 取得與設定
        String x = list.get(0);
        list.set(2, "Bill");
        System.out.println("get(0)=" + x + " set -> " + list);

        // 移除（值 vs 索引）
        ArrayList<Integer> ints = new ArrayList<>(List.of(1, 2, 3, 2, 1));
        ints.remove(Integer.valueOf(1)); // 移除值 1（首個）
        System.out.println("remove 值 1 -> " + ints);
        ints.remove(1); // 移除索引 1
        System.out.println("remove 索引 1 -> " + ints);

        // contains / indexOf
        System.out.println("contains 'Cindy'? " + list.contains("Cindy"));
        System.out.println("indexOf 'Bill' = " + list.indexOf("Bill"));

        // Arrays.asList 固定長度
        List<String> fixed = Arrays.asList("a", "b", "c");
        // fixed.add("d"); // 會拋 UnsupportedOperationException
        ArrayList<String> mutable = new ArrayList<>(fixed); // 可變副本
        mutable.add("d");
        System.out.println("mutable: " + mutable);

        // subList 是視圖
        List<String> view = mutable.subList(1, 3); // [b,c]
        view.set(0, "B");
        System.out.println("view: " + view + " | mutable: " + mutable);
    }

    static void safeRemove() {
        ArrayList<Integer> nums = new ArrayList<>(List.of(1,2,3,4,5,6));
        // 錯誤：for-each 直接 remove 會 CME
        // 正確：Iterator.remove()
        for (Iterator<Integer> it = nums.iterator(); it.hasNext(); ) {
            if (it.next() % 2 == 0) it.remove();
        }
        System.out.println("移除偶數 -> " + nums);
    }

    static void sortExamples() {
        ArrayList<Student> students = new ArrayList<>(List.of(
            new Student("Bob", 82),
            new Student("Ann", 90),
            new Student("Cindy", 90),
            new Student("David", 75)
        ));

        // 分數降冪，分數相同姓名升冪
        students.sort(
            Comparator.comparingInt((Student s) -> s.score).reversed()
                      .thenComparing(s -> s.name)
        );
        System.out.println("排序後: " + students);

        // 自然排序（字串）
        ArrayList<String> names = new ArrayList<>(List.of("Ann","bob","Cindy","alex"));
        names.sort(String.CASE_INSENSITIVE_ORDER);
        System.out.println("不分大小寫排序: " + names);
    }

    static void conversions() {
        String[] arr = {"x","y","z"};
        ArrayList<String> list = new ArrayList<>(Arrays.asList(arr));
        String[] back = list.toArray(new String[0]);
        System.out.println("list: " + list + " | array: " + Arrays.toString(back));
    }

    public static void main(String[] args) {
        basicOps();
        safeRemove();
        sortExamples();
        conversions();
    }
}
```