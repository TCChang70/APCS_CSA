/**
 * Unit 06：迴圈與數學計算 — 練習程式
 * 包含範例和練習題解答
 */
public class LoopMathPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 06: 迴圈與數學計算 ===\n");

        // ----- 範例 1：累加 (1-100) -----
        System.out.println("範例 1：1 到 100 總和");
        int sum = 0;
        for (int i = 1; i <= 100; i++) sum += i;
        System.out.println("Sum = " + sum + "\n");

        // ----- 範例 2：階乘 -----
        System.out.println("範例 2：10! 階乘");
        long factorial = 1;
        for (int i = 1; i <= 10; i++) factorial *= i;
        System.out.println("10! = " + factorial + "\n");

        // ----- 範例 3：平均值 -----
        System.out.println("範例 3：陣列平均值");
        int[] data = {85, 90, 78, 92, 88};
        double total = 0;
        for (int i = 0; i < data.length; i++) total += data[i];
        double avg = total / data.length;
        System.out.printf("平均：%.2f%n%n", avg);

        // ----- 範例 4：GCD -----
        System.out.println("範例 4：GCD(48, 18)");
        int a = 48, b = 18;
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        System.out.println("GCD = " + a + "\n");

        // ----- 範例 5：Fibonacci -----
        System.out.println("範例 5：Fibonacci 前 15 項");
        int f1 = 1, f2 = 1;
        System.out.print(f1 + " " + f2 + " ");
        for (int i = 3; i <= 15; i++) {
            int f3 = f1 + f2;
            System.out.print(f3 + " ");
            f1 = f2;
            f2 = f3;
        }
        System.out.println("\n");

        // ----- 練習題 1 (Easy)：計算次方 -----
        System.out.println("練習題 1：計算 3^5");
        int base = 3, exp = 5;
        int result = 1;
        for (int i = 0; i < exp; i++) result *= base;
        System.out.println("3^5 = " + result + "\n");

        // ----- 練習題 2 (Medium)：Fibonacci 已完成 -----
        System.out.println("練習題 2：Fibonacci 如上\n");

        // ----- 現在試試看：1² + 2² + ... + 20² -----
        System.out.println("現在試試看：平方和");
        int sumSq = 0;
        for (int i = 1; i <= 20; i++) sumSq += i * i;
        System.out.println("1² + 2² + ... + 20² = " + sumSq);
    }
}
