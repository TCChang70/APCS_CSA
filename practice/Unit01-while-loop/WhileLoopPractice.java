/**
 * Unit 01：while 迴圈基礎 — 練習程式
 * 包含範例和練習題解答
 */
public class WhileLoopPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 01: while 迴圈基礎 ===\n");

        // ----- 範例 1：從 1 數到 5 -----
        System.out.println("範例 1：從 1 數到 5");
        int i = 1;
        while (i <= 5) {
            System.out.print(i + " ");
            i++;
        }
        System.out.println("\n");

        // ----- 範例 2：計算 1 到 10 的總和 -----
        System.out.println("範例 2：1 到 10 的總和");
        int sum = 0;
        int n = 1;
        while (n <= 10) {
            sum += n;
            n++;
        }
        System.out.println("總和 = " + sum + "\n");

        // ----- 練習題 1 (Easy)：倒數計時 -----
        System.out.println("練習題 1：倒數計時");
        int count = 10;
        while (count >= 1) {
            System.out.println(count);
            count--;
        }
        System.out.println("Go!\n");

        // ----- 練習題 2 (Medium)：找出第一個大於 50 且能被 7 整除的數 -----
        System.out.println("練習題 2：第一個大於 50 且能被 7 整除的數");
        int num = 1;
        while (!(num > 50 && num % 7 == 0)) {
            num++;
        }
        System.out.println("答案：" + num + "\n");

        // ----- 練習題 3 (Medium)：數字反轉 -----
        System.out.println("練習題 3：數字反轉");
        int original = 1234;
        int reversed = 0;
        int temp = original;
        while (temp > 0) {
            int digit = temp % 10;
            reversed = reversed * 10 + digit;
            temp /= 10;
        }
        System.out.println(original + " 反轉後 = " + reversed + "\n");

        // ----- 練習題 4 (Hard)：印出所有因數 -----
        System.out.println("練習題 4：24 的所有因數");
        int target = 24;
        int divisor = 1;
        while (divisor <= target) {
            if (target % divisor == 0) {
                System.out.print(divisor + " ");
            }
            divisor++;
        }
        System.out.println("\n");

        // ----- 現在試試看：1 到 100 奇數總和 -----
        System.out.println("現在試試看：1 到 100 奇數總和");
        int oddSum = 0;
        int k = 1;
        while (k <= 100) {
            if (k % 2 == 1) {
                oddSum += k;
            }
            k++;
        }
        System.out.println("奇數總和 = " + oddSum);
    }
}
