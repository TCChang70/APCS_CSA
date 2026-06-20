/**
 * Unit 13：Array 遍歷 — 標準 for 迴圈 — 練習程式
 * 包含範例和練習題解答
 */
public class ArrayForLoopPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 13: Array 遍歷 — 標準 for ===\n");

        int[] scores = {85, 90, 78, 92, 88, 76, 95};

        // ----- 範例 1：印出所有元素 -----
        System.out.println("範例 1：印出所有元素");
        for (int i = 0; i < scores.length; i++) {
            System.out.println("scores[" + i + "] = " + scores[i]);
        }
        System.out.println();

        // ----- 範例 2：計算總和與平均 -----
        System.out.println("範例 2：計算總和與平均");
        int sum = 0;
        for (int i = 0; i < scores.length; i++) sum += scores[i];
        double avg = (double) sum / scores.length;
        System.out.printf("總和：%d, 平均：%.2f%n%n", sum, avg);

        // ----- 範例 3：找最大值 -----
        System.out.println("範例 3：找最大值");
        int max = scores[0];
        for (int i = 1; i < scores.length; i++) {
            if (scores[i] > max) max = scores[i];
        }
        System.out.println("最高分：" + max + "\n");

        // ----- 範例 4：計數（80 分以上）-----
        System.out.println("範例 4：80 分以上人數");
        int passCount = 0;
        for (int i = 0; i < scores.length; i++) {
            if (scores[i] >= 80) passCount++;
        }
        System.out.println("80 分以上：" + passCount + " 人\n");

        // ----- 練習題 1 (Easy)：找最小值 -----
        System.out.println("練習題 1：最小值");
        int[] testArr = {64, 25, 12, 22, 11};
        System.out.println("min = " + min(testArr) + "\n");

        // ----- 練習題 2 (Hard)：判斷是否有重複 -----
        System.out.println("練習題 2：是否有重複值");
        int[] dupArr = {1, 3, 5, 3, 7};
        int[] noDupArr = {1, 3, 5, 7, 9};
        System.out.println("{1,3,5,3,7} → " + hasDuplicate(dupArr));
        System.out.println("{1,3,5,7,9} → " + hasDuplicate(noDupArr) + "\n");

        // ----- 現在試試看：找最大值索引 -----
        System.out.println("現在試試看：最大值索引");
        int[] nums = {12, 45, 8, 45, 23};
        int maxIdx = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[maxIdx]) {
                maxIdx = i;
            }
        }
        System.out.println("最大值 " + nums[maxIdx] + " 在索引 " + maxIdx);
    }

    // 練習 1：找最小值
    public static int min(int[] arr) {
        int min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) min = arr[i];
        }
        return min;
    }

    // 練習 2：判斷是否有重複值
    public static boolean hasDuplicate(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j]) return true;
            }
        }
        return false;
    }
}
