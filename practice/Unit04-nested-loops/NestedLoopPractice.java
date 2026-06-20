/**
 * Unit 04：巢狀迴圈 — 練習程式
 * 包含範例和練習題解答
 */
public class NestedLoopPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 04: 巢狀迴圈 ===\n");

        // ----- 範例 1：(i, j) 組合追蹤 -----
        System.out.println("範例 1：(i, j) 組合");
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                System.out.println("i=" + i + ", j=" + j);
            }
        }
        System.out.println();

        // ----- 範例 2：矩形圖案 (4x6) -----
        System.out.println("範例 2：矩形圖案");
        for (int row = 0; row < 4; row++) {
            for (int col = 0; col < 6; col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();

        // ----- 練習題 1 (Easy)：追蹤 count -----
        System.out.println("練習題 1：count 最終值");
        int count = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < i; j++) {
                count++;
            }
        }
        System.out.println("count = " + count + "\n");

        // ----- 練習題 2 (Medium)：數字三角形 -----
        System.out.println("練習題 2：數字三角形");
        int n = 5;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
        System.out.println();

        // ----- 練習題 3 (Hard)：質數篩選 2-50 -----
        System.out.println("練習題 3：2 到 50 的質數");
        for (int num = 2; num <= 50; num++) {
            boolean isPrime = true;
            for (int d = 2; d < num; d++) {
                if (num % d == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                System.out.print(num + " ");
            }
        }
        System.out.println("\n");

        // ----- 現在試試看：九九乘法表 -----
        System.out.println("現在試試看：九九乘法表");
        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                System.out.printf("%4d", i * j);
            }
            System.out.println();
        }
    }
}
