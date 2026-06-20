/**
 * Unit 09：迴圈與方法整合 — 練習程式
 * 包含範例和練習題解答
 */
public class LoopMethodsPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 09: 迴圈與方法整合 ===\n");

        // ----- 範例 1：sum 方法 -----
        System.out.println("範例 1：sum 方法");
        System.out.println("sum(10) = " + sum(10));
        System.out.println("sum(100) = " + sum(100) + "\n");

        // ----- 範例 2：isPrime 方法 -----
        System.out.println("範例 2：2 到 30 的質數");
        for (int i = 2; i <= 30; i++) {
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
        System.out.println("\n");

        // ----- 範例 3：countVowels 方法 -----
        System.out.println("範例 3：母音計數");
        String test = "Hello World";
        System.out.println("母音數：" + countVowels(test) + "\n");

        // ----- 練習題 1：max 方法 -----
        System.out.println("練習題 1：max(7, 3, 9) = " + max(7, 3, 9) + "\n");

        // ----- 練習題 2：reverse 方法 -----
        System.out.println("練習題 2：reverse(12345) = " + reverse(12345) + "\n");

        // ----- 現在試試看：sumOfSquares -----
        System.out.println("現在試試看：sumOfSquares(10) = " + sumOfSquares(10));
    }

    // 範例 1：累加
    public static int sum(int n) {
        int total = 0;
        for (int i = 1; i <= n; i++) {
            total += i;
        }
        return total;
    }

    // 範例 2：質數判斷
    public static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    // 範例 3：母音計數
    public static int countVowels(String s) {
        int count = 0;
        String vowels = "aeiouAEIOU";
        for (int i = 0; i < s.length(); i++) {
            if (vowels.indexOf(s.charAt(i)) >= 0) {
                count++;
            }
        }
        return count;
    }

    // 練習題 1：找出三個數中最大值
    public static int max(int a, int b, int c) {
        int m = a;
        if (b > m) m = b;
        if (c > m) m = c;
        return m;
    }

    // 練習題 2：反轉整數
    public static int reverse(int n) {
        int result = 0;
        while (n != 0) {
            result = result * 10 + n % 10;
            n /= 10;
        }
        return result;
    }

    // 現在試試看：平方和
    public static int sumOfSquares(int n) {
        int total = 0;
        for (int i = 1; i <= n; i++) {
            total += i * i;
        }
        return total;
    }
}
