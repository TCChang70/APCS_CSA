/**
 * Unit 15：Array 基礎演算法 — 練習程式
 * 包含 4 大演算法和練習題解答
 */
public class ArrayAlgorithmsPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 15: Array 基礎演算法 ===\n");

        int[] arr = {64, 25, 12, 22, 11};

        // ----- 演算法 1：最大值 -----
        System.out.println("演算法 1：最大值");
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) max = arr[i];
        }
        System.out.println("Max: " + max + "\n");

        // ----- 演算法 2：最小值 -----
        System.out.println("演算法 2：最小值");
        int min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) min = arr[i];
        }
        System.out.println("Min: " + min + "\n");

        // ----- 演算法 3：總和與平均 -----
        System.out.println("演算法 3：總和與平均");
        int sum = 0;
        for (int val : arr) sum += val;
        double avg = (double) sum / arr.length;
        System.out.printf("Sum: %d, Avg: %.2f%n%n", sum, avg);

        // ----- 演算法 4：線性搜尋 -----
        System.out.println("演算法 4：線性搜尋");
        int target = 22;
        int index = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                index = i;
                break;
            }
        }
        System.out.println(target + " 在索引 " + index + "\n");

        // ----- 練習題 1 (Medium)：找最大值的索引 -----
        System.out.println("練習題 1：最大值索引");
        int[] testArr = {12, 45, 8, 45, 23};
        System.out.println("索引：" + indexOfMax(testArr) + "（值：" + testArr[indexOfMax(testArr)] + "）\n");

        // ----- 練習題 2 (Hard)：高於平均的個數 -----
        System.out.println("練習題 2：高於平均的個數");
        int[] scores = {85, 90, 78, 92, 88, 76, 95};
        System.out.println("高於平均的人數：" + countAboveAverage(scores) + "\n");

        // ----- 現在試試看：第二大 -----
        System.out.println("現在試試看：陣列中第二大的值");
        int[] nums = {64, 25, 12, 22, 11, 64, 89};
        int secondMax = findSecondMax(nums);
        System.out.println("第二大：" + secondMax);
    }

    // 練習題 1：回傳最大值的索引
    public static int indexOfMax(int[] arr) {
        int maxIndex = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > arr[maxIndex]) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }

    // 練習題 2：統計高於平均的個數
    public static int countAboveAverage(int[] arr) {
        double sum = 0;
        for (int val : arr) sum += val;
        double avg = sum / arr.length;

        int count = 0;
        for (int val : arr) {
            if (val >= avg) count++;
        }
        return count;
    }

    // 挑戰：找出陣列中第二大的值
    public static int findSecondMax(int[] arr) {
        int max = Math.max(arr[0], arr[1]);
        int secondMax = Math.min(arr[0], arr[1]);

        for (int i = 2; i < arr.length; i++) {
            if (arr[i] > max) {
                secondMax = max;
                max = arr[i];
            } else if (arr[i] > secondMax && arr[i] != max) {
                secondMax = arr[i];
            }
        }
        return secondMax;
    }
}
