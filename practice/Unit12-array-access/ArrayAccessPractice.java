/**
 * Unit 12：Array 元素存取與修改 — 練習程式
 * 包含範例和練習題解答
 */
public class ArrayAccessPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 12: Array 元素存取與修改 ===\n");

        // ----- 範例 1：存取與修改 -----
        System.out.println("範例 1：存取與修改");
        int[] nums = {5, 10, 15, 20, 25};
        nums[2] = 99;
        System.out.println("nums[2] = " + nums[2] + "\n");

        // ----- 範例 2：負數改為 0 -----
        System.out.println("範例 2：負數改為 0");
        int[] data = {3, -1, 7, -4, 0, -2};
        System.out.print("修改前：");
        for (int v : data) System.out.print(v + " ");
        System.out.println();

        for (int i = 0; i < data.length; i++) {
            if (data[i] < 0) data[i] = 0;
        }
        System.out.print("修改後：");
        for (int v : data) System.out.print(v + " ");
        System.out.println("\n");

        // ----- 範例 3：參考型別示範 -----
        System.out.println("範例 3：參考型別（方法修改陣列）");
        int[] scores = {10, 20, 30};
        System.out.print("呼叫前：");
        for (int v : scores) System.out.print(v + " ");
        System.out.println();

        doubleAll(scores);

        System.out.print("呼叫後：");
        for (int v : scores) System.out.print(v + " ");
        System.out.println("\n");

        // ----- 練習題 1 (Easy)：交換首尾元素 -----
        System.out.println("練習題 1：交換首尾元素");
        int[] testArr = {1, 2, 3, 4, 5};
        swapEnds(testArr);
        System.out.print("交換後：");
        for (int v : testArr) System.out.print(v + " ");
        System.out.println("\n");

        // ----- 練習題 2 (Medium)：加上偏移量 -----
        System.out.println("練習題 2：加上偏移量 10");
        int[] offsetArr = {1, 2, 3, 4, 5};
        addOffset(offsetArr, 10);
        System.out.print("加上偏移後：");
        for (int v : offsetArr) System.out.print(v + " ");
        System.out.println("\n");

        // ----- 現在試試看：原地反轉陣列 -----
        System.out.println("現在試試看：陣列反轉");
        int[] revArr = {1, 2, 3, 4, 5, 6};
        reverse(revArr);
        System.out.print("反轉後：");
        for (int v : revArr) System.out.print(v + " ");
        System.out.println();
    }

    // 將陣列每個元素乘以 2（示範參考型別）
    public static void doubleAll(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] *= 2;
        }
    }

    // 交換首尾元素
    public static void swapEnds(int[] arr) {
        int temp = arr[0];
        arr[0] = arr[arr.length - 1];
        arr[arr.length - 1] = temp;
    }

    // 加上偏移量
    public static void addOffset(int[] arr, int offset) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] += offset;
        }
    }

    // 原地反轉陣列
    public static void reverse(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
}
