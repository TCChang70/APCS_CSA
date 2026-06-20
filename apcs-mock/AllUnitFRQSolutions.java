/**
 * APCS CSA 15 單元 — 全部 FRQ 解答
 * 包含 Unit 01 ~ 15 每個單元的 FRQ 解答方法
 */
public class AllUnitFRQSolutions {

    public static void main(String[] args) {
        System.out.println("========== APCS CSA 15 單元 FRQ 解答驗證 ==========\n");

        // Unit 01
        System.out.println("【Unit 01】digitSum(123) = " + digitSum(123) + " (期望: 6)");
        System.out.println("  digitSum(9999) = " + digitSum(9999) + " (期望: 36)");

        // Unit 02
        System.out.println("【Unit 02】alternatingSquareSum(4) = " + alternatingSquareSum(4) + " (期望: -10)");
        System.out.println("  alternatingSquareSum(5) = " + alternatingSquareSum(5) + " (期望: 15)");

        // Unit 03
        System.out.println("【Unit 03】sumOddInRange(1, 10) = " + sumOddInRange(1, 10) + " (期望: 25)");
        System.out.println("  sumOddInRange(4, 8) = " + sumOddInRange(4, 8) + " (期望: 12)");

        // Unit 04
        System.out.println("【Unit 04】printMultiplicationTable(3):");
        printMultiplicationTable(3);
        System.out.println();

        // Unit 05
        System.out.println("【Unit 05】shiftOne(\"abc\") = " + shiftOne("abc") + " (期望: bcd)");
        System.out.println("  shiftOne(\"zoo\") = " + shiftOne("zoo") + " (期望: app)");
        System.out.println("  shiftOne(\"Hello!\") = " + shiftOne("Hello!") + " (期望: Ifmmp!)");

        // Unit 06
        System.out.println("【Unit 06】primeFactors(12):");
        primeFactors(12);
        System.out.println();
        System.out.print("  primeFactors(100): ");
        primeFactors(100);
        System.out.println();

        // Unit 07
        System.out.println("【Unit 07】nextPerfectSquare(10) = " + nextPerfectSquare(10) + " (期望: 16)");
        System.out.println("  nextPerfectSquare(50) = " + nextPerfectSquare(50) + " (期望: 64)");

        // Unit 08
        System.out.println("【Unit 08】factorial(5) = " + factorial(5) + " (期望: 120)");
        System.out.println("  factorial(0) = " + factorial(0) + " (期望: 1)");

        // Unit 09
        System.out.println("【Unit 09】countPrimes(10) = " + countPrimes(10) + " (期望: 4)");
        System.out.println("  countPrimes(20) = " + countPrimes(20) + " (期望: 8)");

        // Unit 10
        System.out.println("【Unit 10】isValidPassword(\"P@ssw0rd\") = " + isValidPassword("P@ssw0rd") + " (期望: true)");
        System.out.println("  isValidPassword(\"pass word\") = " + isValidPassword("pass word") + " (期望: false)");
        System.out.println("  isValidPassword(\"ABC12345\") = " + isValidPassword("ABC12345") + " (期望: false)");

        // Unit 11
        int[] g1 = generateArray(5, 1, 2);
        System.out.print("【Unit 11】generateArray(5,1,2) = {");
        printIntArray(g1);
        System.out.println("} (期望: {1,3,5,7,9})");

        // Unit 12
        int[] s1 = {1, 2, 3, 4, 5};
        shiftRight(s1, 2);
        System.out.print("【Unit 12】shiftRight({1,2,3,4,5}, 2) = {");
        printIntArray(s1);
        System.out.println("} (期望: {4,5,1,2,3})");

        // Unit 13
        System.out.println("【Unit 13】range({3,7,1,9,4}) = " + range(new int[]{3, 7, 1, 9, 4}) + " (期望: 8)");

        // Unit 14
        System.out.println("【Unit 14】hasAdjacentSumGreaterThan({3,7,9,1,4}, 15) = "
                + hasAdjacentSumGreaterThan(new int[]{3, 7, 9, 1, 4}, 15) + " (期望: true)");
        System.out.println("  hasAdjacentSumGreaterThan({3,7,1,9,4}, 20) = "
                + hasAdjacentSumGreaterThan(new int[]{3, 7, 1, 9, 4}, 20) + " (期望: false)");

        // Unit 15
        System.out.println("【Unit 15】secondLargest({5,3,9,1,7}) = "
                + secondLargest(new int[]{5, 3, 9, 1, 7}) + " (期望: 7)");
        System.out.println("  secondLargest({10,10,9}) = "
                + secondLargest(new int[]{10, 10, 9}) + " (期望: 9)");

        System.out.println("\n========== 全部驗證完成 ==========");
    }

    // ========== Unit 01: while ==========
    public static int digitSum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    // ========== Unit 02: for ==========
    public static int alternatingSquareSum(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) sum += i * i;
            else sum -= i * i;
        }
        return sum;
    }

    // ========== Unit 03: loop control ==========
    public static int sumOddInRange(int start, int end) {
        int sum = 0;
        for (int i = start; i <= end; i++) {
            if (i % 2 == 1) sum += i;
        }
        return sum;
    }

    // ========== Unit 04: nested loops ==========
    public static void printMultiplicationTable(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                System.out.print((i * j) + " ");
            }
            System.out.println();
        }
    }

    // ========== Unit 05: String traversal ==========
    public static String shiftOne(String text) {
        String result = "";
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c == 'z') result += 'a';
            else if (c == 'Z') result += 'A';
            else if ((c >= 'a' && c < 'z') || (c >= 'A' && c < 'Z')) {
                result += (char) (c + 1);
            } else {
                result += c;
            }
        }
        return result;
    }

    // ========== Unit 06: loop math ==========
    public static void primeFactors(int n) {
        int d = 2;
        while (n > 1) {
            if (n % d == 0) {
                System.out.print(d + " ");
                n /= d;
            } else {
                d++;
            }
        }
    }

    // ========== Unit 07: break & continue ==========
    public static int nextPerfectSquare(int n) {
        for (int i = 1; ; i++) {
            int square = i * i;
            if (square > n) return square;
        }
    }

    // ========== Unit 08: debugging ==========
    public static int factorial(int n) {
        int product = 1;
        for (int i = 1; i <= n; i++) {
            product *= i;
        }
        return product;
    }

    // ========== Unit 09: methods ==========
    public static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static int countPrimes(int n) {
        int count = 0;
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) count++;
        }
        return count;
    }

    // ========== Unit 10: FRQ review ==========
    public static boolean isValidPassword(String password) {
        if (password.length() < 8 || password.length() > 20) return false;
        boolean hasUpper = false, hasLower = false, hasDigit = false;
        for (int i = 0; i < password.length(); i++) {
            char c = password.charAt(i);
            if (c == ' ') return false;
            if (c >= 'A' && c <= 'Z') hasUpper = true;
            else if (c >= 'a' && c <= 'z') hasLower = true;
            else if (c >= '0' && c <= '9') hasDigit = true;
        }
        return hasUpper && hasLower && hasDigit;
    }

    // ========== Unit 11: array declaration ==========
    public static int[] generateArray(int n, int start, int step) {
        int[] result = new int[n];
        int value = start;
        for (int i = 0; i < n; i++) {
            result[i] = value;
            value += step;
        }
        return result;
    }

    // ========== Unit 12: array access ==========
    public static void shiftRight(int[] arr, int k) {
        int n = arr.length;
        if (n == 0) return;
        k = k % n;
        if (k == 0) return;
        reverse(arr, 0, n - 1);
        reverse(arr, 0, k - 1);
        reverse(arr, k, n - 1);
    }

    private static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }

    // ========== Unit 13: array for loop ==========
    public static int range(int[] arr) {
        int max = arr[0];
        int min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) max = arr[i];
            if (arr[i] < min) min = arr[i];
        }
        return max - min;
    }

    // ========== Unit 14: for-each ==========
    public static boolean hasAdjacentSumGreaterThan(int[] arr, int threshold) {
        if (arr.length < 2) return false;
        int prev = arr[0];
        boolean first = true;
        for (int current : arr) {
            if (first) { first = false; continue; }
            if (prev + current > threshold) return true;
            prev = current;
        }
        return false;
    }

    // ========== Unit 15: array algorithms ==========
    public static int secondLargest(int[] arr) {
        if (arr.length < 2) return Integer.MIN_VALUE;
        int max = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;
        for (int val : arr) {
            if (val > max) {
                second = max;
                max = val;
            } else if (val > second && val < max) {
                second = val;
            }
        }
        return second;
    }

    // ========== Helper: print int array ==========
    private static void printIntArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) System.out.print(",");
        }
    }
}
