/**
 * Unit 08：常見迴圈錯誤與除錯技巧 — 練習程式
 * 包含錯誤範例、修正版和除錯練習
 */
public class DebuggingPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 08: 常見迴圈錯誤與除錯技巧 ===\n");

        // ----- 錯誤版 1：Off-by-one -----
        System.out.println("錯誤 1：Off-by-one (修正前)");
        int n = 10;
        int sum1 = 0;
        for (int i = 1; i < n; i++) {  // 錯誤：應為 i <= n
            sum1 += i;
        }
        System.out.println("錯誤結果：" + sum1 + " (應為 55)");

        // 修正版
        int sum1fixed = 0;
        for (int i = 1; i <= n; i++) {
            sum1fixed += i;
        }
        System.out.println("修正結果：" + sum1fixed + "\n");

        // ----- 錯誤版 2：累乘初始化錯誤 -----
        System.out.println("錯誤 2：累乘初始化錯誤 (修正前)");
        int product = 0;  // 錯誤：應為 1
        for (int i = 1; i <= 5; i++) {
            product *= i;
        }
        System.out.println("錯誤結果：" + product + " (應為 120)");

        int productFixed = 1;
        for (int i = 1; i <= 5; i++) {
            productFixed *= i;
        }
        System.out.println("修正結果：" + productFixed + "\n");

        // ----- 練習題：找 Bug -----
        System.out.println("練習題：找出以下程式碼的錯誤");
        int total = 1;  // Bug 1: 應初始化為 0
        for (int k = 1; k < 10; k++) {  // Bug 2: 應為 k <= 10
            total = total + k;
        }
        System.out.println("錯誤結果：" + total + " (應為 55)");

        // 修正版
        int totalFixed = 0;
        for (int k = 1; k <= 10; k++) {
            totalFixed += k;
        }
        System.out.println("修正結果：" + totalFixed);

        // ----- 除錯技巧示範 -----
        System.out.println("\n除錯技巧示範：加入 print 除錯");
        int debugSum = 0;
        for (int i = 1; i <= 5; i++) {
            debugSum += i;
            System.out.println("DEBUG: i=" + i + ", sum=" + debugSum);
        }
        System.out.println("最終總和：" + debugSum);
    }
}
