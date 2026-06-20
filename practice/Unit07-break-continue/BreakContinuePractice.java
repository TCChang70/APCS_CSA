/**
 * Unit 07：break 與 continue — 練習程式
 * 包含範例和練習題解答
 */
public class BreakContinuePractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 07: break 與 continue ===\n");

        // ----- 範例 1：搜尋第一個負數 -----
        System.out.println("範例 1：搜尋第一個負數");
        int[] nums = {4, 7, -2, 9, -5, 3};
        int firstNeg = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < 0) {
                firstNeg = nums[i];
                break;
            }
        }
        System.out.println("第一個負數：" + firstNeg + "\n");

        // ----- 範例 2：印出非空白字元 -----
        System.out.println("範例 2：印出非空白字元");
        String s = "A B C D";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') continue;
            System.out.print(s.charAt(i));
        }
        System.out.println("\n");

        // ----- 練習題 1 (Easy)：找到第一個 --------------------------
        System.out.println("練習題 1：第一個 >100 且能被 13 整除的數");
        for (int i = 101; i <= 1000; i++) {
            if (i % 13 == 0) {
                System.out.println(i + "\n");
                break;
            }
        }

        // ----- 練習題 2 (Hard)：字元首次出現位置 -----
        System.out.println("練習題 2：字元首次出現位置");
        String str = "abcabc";
        for (int i = 0; i < str.length(); i++) {
            boolean seen = false;
            for (int j = 0; j < i; j++) {
                if (str.charAt(j) == str.charAt(i)) {
                    seen = true;
                    break;
                }
            }
            if (seen) continue;
            System.out.println("'" + str.charAt(i) + "' 首次出現在索引 " + i);
        }
        System.out.println();

        // ----- 現在試試看：用 break 改進質數判斷 -----
        System.out.println("現在試試看：質數判斷（有 break）");
        int num = 97;
        boolean isPrime = true;
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                isPrime = false;
                break;  // 找到因數後立即停止
            }
        }
        System.out.println(num + " 是質數嗎？" + isPrime);
    }
}
