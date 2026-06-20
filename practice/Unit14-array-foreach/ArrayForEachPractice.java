/**
 * Unit 14：Array 遍歷 — for-each 迴圈 — 練習程式
 * 包含範例和練習題解答
 */
public class ArrayForEachPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 14: Array 遍歷 — for-each ===\n");

        int[] nums = {3, 7, 1, 9, 4};

        // ----- 範例 1：for-each 印出 -----
        System.out.println("範例 1：for-each 印出");
        for (int n : nums) {
            System.out.print(n + " ");
        }
        System.out.println("\n");

        // ----- 範例 2：for-each 計算總和 -----
        System.out.println("範例 2：for-each 計算總和");
        int sum = 0;
        for (int n : nums) sum += n;
        System.out.println("Sum = " + sum + "\n");

        // ----- 範例 3：for-each 修改（錯誤示範）-----
        System.out.println("範例 3：for-each 修改（錯誤示範）");
        for (int n : nums) {
            n *= 2;  // 只修改了本地變數
        }
        System.out.print("nums[0] 仍是 " + nums[0] + "（未被修改）");
        System.out.println("\n");

        // ----- 範例 4：String 陣列 for-each -----
        System.out.println("範例 4：String 陣列");
        String[] names = {"Alice", "Bob", "Charlie"};
        for (String name : names) {
            System.out.println("Hello, " + name + "!");
        }
        System.out.println();

        // ----- 練習題 1 (Easy)：用 for-each 找最大值 -----
        System.out.println("練習題 1：for-each 找最大值");
        int[] data = {15, 42, 8, 27, 99, 3};
        int max = data[0];
        for (int n : data) {
            if (n > max) max = n;
        }
        System.out.println("最大值：" + max + "\n");

        // ----- 練習題 2 (Easy)：判斷是否全為正數 -----
        System.out.println("練習題 2：是否全為正數");
        int[] posArr = {3, 7, 1, 9, 4};
        int[] negArr = {3, -1, 7, 9, 4};
        System.out.println("{3,7,1,9,4} → " + allPositive(posArr));
        System.out.println("{3,-1,7,9,4} → " + allPositive(negArr) + "\n");

        // ----- 現在試試看：double[] 乘積 -----
        System.out.println("現在試試看：double 陣列乘積");
        double[] doubles = {1.5, 2.0, 4.0};
        double product = 1.0;
        for (double d : doubles) {
            product *= d;
        }
        System.out.println("乘積 = " + product);
    }

    // 判斷陣列是否所有元素都是正數
    public static boolean allPositive(int[] arr) {
        for (int n : arr) {
            if (n <= 0) return false;
        }
        return true;
    }
}
