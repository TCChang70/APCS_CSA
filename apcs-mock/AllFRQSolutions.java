/**
 * APCS CSA 模擬練習 — 全部 FRQ 解答
 * 包含 Phase 1 ~ Phase 3 所有 FRQ 方法
 */
public class AllFRQSolutions {

    public static void main(String[] args) {
        System.out.println("========== APCS CSA Mock FRQ 解答驗證 ==========\n");

        // ---- Phase 1 ----
        System.out.println("=== Phase 1 ===");
        System.out.println("countWordLength(\"Hello world Java\", 4) = "
                + countWordLength("Hello world Java", 4) + " (期望: 3)");
        System.out.println("countWordLength(\"A B C D\", 2) = "
                + countWordLength("A B C D", 2) + " (期望: 0)");
        System.out.println("passwordStrength(\"abc\") = "
                + passwordStrength("abc") + " (期望: Weak)");
        System.out.println("passwordStrength(\"Abc123!\") = "
                + passwordStrength("Abc123!") + " (期望: Medium)");
        System.out.println("passwordStrength(\"P@ssw0rd\") = "
                + passwordStrength("P@ssw0rd") + " (期望: Strong)");

        // ---- Phase 2 ----
        System.out.println("\n=== Phase 2 ===");
        System.out.println("isPerfectNumber(6) = "
                + isPerfectNumber(6) + " (期望: true)");
        System.out.println("isPerfectNumber(28) = "
                + isPerfectNumber(28) + " (期望: true)");
        System.out.println("isPerfectNumber(12) = "
                + isPerfectNumber(12) + " (期望: false)");
        System.out.println("caesarCipher(\"abc\", 3) = "
                + caesarCipher("abc", 3) + " (期望: def)");
        System.out.println("caesarCipher(\"xyz\", 3) = "
                + caesarCipher("xyz", 3) + " (期望: abc)");
        System.out.println("caesarCipher(\"Hello World!\", 5) = "
                + caesarCipher("Hello World!", 5) + " (期望: Mjqqt Btwqi!)");

        // ---- Phase 3 ----
        System.out.println("\n=== Phase 3 ===");
        int[] g1 = {80, 90, 70};
        System.out.println("analyzeGrades({80,90,70}) = "
                + analyzeGrades(g1) + " (期望: 90.0)");
        int[] g2 = {60, 60, 60};
        System.out.println("analyzeGrades({60,60,60}) = "
                + analyzeGrades(g2) + " (期望: 0.0)");
        int[] g3 = {85, 90, 78, 92, 88};
        System.out.println("analyzeGrades({85,90,78,92,88}) = "
                + analyzeGrades(g3) + " (期望: 90.0)");

        int[] c1 = compress(new int[]{1, 2, 3, 4, 5, 6}, 2);
        System.out.print("compress({1,2,3,4,5,6}, 2) = {");
        for (int i = 0; i < c1.length; i++) {
            System.out.print(c1[i] + (i < c1.length - 1 ? "," : ""));
        }
        System.out.println("} (期望: {3,7,11})");

        int[] c2 = compress(new int[]{1, 2, 3, 4, 5}, 3);
        System.out.print("compress({1,2,3,4,5}, 3) = {");
        for (int i = 0; i < c2.length; i++) {
            System.out.print(c2[i] + (i < c2.length - 1 ? "," : ""));
        }
        System.out.println("} (期望: {6,9})");

        System.out.println("\n========== 全部驗證完成 ==========");
    }

    // ========== Phase 1 FRQ 解答 ==========

    /**
     * FRQ 1-1：字串分析 — 計算長度 ≥ n 的單字數量
     */
    public static int countWordLength(String sentence, int n) {
        int count = 0;
        String currentWord = "";

        for (int i = 0; i < sentence.length(); i++) {
            char c = sentence.charAt(i);
            if (c == ' ') {
                if (currentWord.length() >= n) {
                    count++;
                }
                currentWord = "";
            } else {
                currentWord += c;
            }
        }

        if (currentWord.length() >= n) {
            count++;
        }

        return count;
    }

    /**
     * FRQ 1-2：密碼強度檢查
     */
    public static String passwordStrength(String password) {
        int score = 0;

        if (password.length() >= 8) score++;

        boolean hasUpper = false;
        boolean hasLower = false;
        boolean hasDigit = false;
        boolean hasSpecial = false;

        for (int i = 0; i < password.length(); i++) {
            char c = password.charAt(i);
            if (c >= 'A' && c <= 'Z') hasUpper = true;
            else if (c >= 'a' && c <= 'z') hasLower = true;
            else if (c >= '0' && c <= '9') hasDigit = true;
            else hasSpecial = true;
        }

        if (hasUpper) score++;
        if (hasLower) score++;
        if (hasDigit) score++;
        if (hasSpecial) score++;

        if (score <= 2) return "Weak";
        else if (score <= 4) return "Medium";
        else return "Strong";
    }

    // ========== Phase 2 FRQ 解答 ==========

    /**
     * FRQ 2-1：完美數判斷
     */
    public static boolean isPerfectNumber(int n) {
        if (n <= 1) return false;

        int sum = 0;
        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                sum += i;
            }
        }

        return sum == n;
    }

    /**
     * FRQ 2-2：Caesar 密碼加密
     */
    public static String caesarCipher(String text, int shift) {
        String result = "";
        shift = shift % 26;

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);

            if (c >= 'A' && c <= 'Z') {
                c = (char) ((c - 'A' + shift) % 26 + 'A');
            } else if (c >= 'a' && c <= 'z') {
                c = (char) ((c - 'a' + shift) % 26 + 'a');
            }

            result += c;
        }

        return result;
    }

    // ========== Phase 3 FRQ 解答 ==========

    /**
     * FRQ 3-1：陣列統計 — 高於平均的成績之平均
     */
    public static double analyzeGrades(int[] grades) {
        double sum = 0;
        for (int grade : grades) {
            sum += grade;
        }
        double average = sum / grades.length;

        double aboveSum = 0;
        int aboveCount = 0;
        for (int grade : grades) {
            if (grade > average) {
                aboveSum += grade;
                aboveCount++;
            }
        }

        if (aboveCount == 0) return 0.0;
        return aboveSum / aboveCount;
    }

    /**
     * FRQ 3-2：陣列壓縮
     */
    public static int[] compress(int[] arr, int k) {
        int newLength = (arr.length + k - 1) / k;
        int[] result = new int[newLength];

        for (int i = 0; i < arr.length; i++) {
            result[i / k] += arr[i];
        }

        return result;
    }
}
