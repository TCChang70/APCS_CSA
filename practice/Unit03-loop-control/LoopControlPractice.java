/**
 * Unit 03：迴圈控制變數與條件設計 — 練習程式
 * 包含範例和練習題解答
 */
public class LoopControlPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 03: 迴圈控制變數與條件設計 ===\n");

        // ----- 範例 1：精確控制範圍 -----
        System.out.println("範例 1：索引 2 到 7");
        for (int i = 2; i <= 7; i++) {
            System.out.print(i + " ");
        }
        System.out.println("\n");

        // ----- 範例 2：計算 1 到 100 總和 -----
        System.out.println("範例 2：1 到 100 總和");
        int total = 0;
        for (int i = 1; i <= 100; i++) {
            total += i;
        }
        System.out.println("總和 = " + total + "\n");

        // ----- 範例 3：String 長度作為終止條件 -----
        System.out.println("範例 3：字串遍歷");
        String word = "hello";
        for (int i = 0; i < word.length(); i++) {
            System.out.print(word.charAt(i) + " ");
        }
        System.out.println("\n");

        // ----- 練習題 1 (Easy)：計算執行次數 -----
        System.out.println("練習題 1：計算執行次數");
        System.out.println("(A) for (int i = 0; i < 10; i++) → 10 次");
        System.out.println("(B) for (int i = 1; i <= 10; i++) → 10 次");
        System.out.println("(C) for (int i = 0; i < 10; i += 2) → 5 次");
        System.out.println("(D) for (int i = 10; i >= 1; i--) → 10 次\n");

        // ----- 練習題 2 (Medium)：FizzBuzz -----
        System.out.println("練習題 2：FizzBuzz (1-30)");
        for (int i = 1; i <= 30; i++) {
            if (i % 15 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
        System.out.println();

        // ----- 練習題 3 (Easy)：同時被 3 和 5 整除 -----
        System.out.println("練習題 3：1 到 50 同時被 3 和 5 整除的數");
        for (int i = 1; i <= 50; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.print(i + " ");
            }
        }
        System.out.println("\n");

        // ----- 練習題 4 (Medium)：字串大寫字母計數 -----
        System.out.println("練習題 4：計算大寫字母數量");
        String str = "Hello World! Java123";
        int upperCount = 0;
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c >= 'A' && c <= 'Z') {
                upperCount++;
            }
        }
        System.out.println("大寫字母數量 = " + upperCount + "\n");

        // ----- 練習題 5 (Hard)：質數總和 -----
        System.out.println("練習題 5：1 到 100 的質數與總和");
        int primeSum = 0;
        for (int n = 2; n <= 100; n++) {
            boolean isPrime = true;
            for (int d = 2; d < n; d++) {
                if (n % d == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                System.out.print(n + " ");
                primeSum += n;
            }
        }
        System.out.println("\n質數總和 = " + primeSum + "\n");

        // ----- 現在試試看：計算 1 到 50 中質數的個數 -----
        System.out.println("現在試試看：1 到 50 中的質數");
        int primeCount = 0;
        for (int n = 2; n <= 50; n++) {
            boolean isPrime = true;
            for (int d = 2; d < n; d++) {
                if (n % d == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                System.out.print(n + " ");
                primeCount++;
            }
        }
        System.out.println("\n共有 " + primeCount + " 個質數");
    }
}
