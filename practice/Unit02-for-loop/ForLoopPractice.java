/**
 * Unit 02：for 迴圈基礎 — 練習程式
 * 包含範例和練習題解答
 */
public class ForLoopPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 02: for 迴圈基礎 ===\n");

        // ----- 範例 1：基本遞增計數 -----
        System.out.println("範例 1：基本遞增計數");
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }
        System.out.println("\n");

        // ----- 範例 2：遞減計數 -----
        System.out.println("範例 2：遞減計數");
        for (int i = 5; i >= 1; i--) {
            System.out.print(i + " ");
        }
        System.out.println("\n");

        // ----- 範例 3：步進 2（印偶數） -----
        System.out.println("範例 3：步進 2（印偶數）");
        for (int i = 0; i <= 10; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println("\n");

        // ----- 練習題 1 (Easy)：印出 1-20 的偶數 -----
        System.out.println("練習題 1：1 到 20 的偶數");
        for (int i = 2; i <= 20; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println("\n");

        // ----- 練習題 2 (Medium)：星號三角形 -----
        System.out.println("練習題 2：星號三角形");
        for (int i = 1; i <= 5; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        System.out.println();

        // ----- 現在試試看：能被 3 整除的數 -----
        System.out.println("現在試試看：1 到 100 中能被 3 整除的數");
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0) {
                System.out.print(i + " ");
                count++;
            }
        }
        System.out.println("\n共有 " + count + " 個數");
    }
}
