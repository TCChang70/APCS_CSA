/**
 * Unit 10：Iteration 綜合練習與 FRQ 準備 — 練習程式
 * 包含密碼驗證 FRQ 範例和練習
 */
public class FRQPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 10: FRQ 綜合練習 ===\n");

        // ----- 密碼驗證測試 -----
        System.out.println("密碼驗證測試：");
        System.out.println("\"abc123\" → " + isValidPassword("abc123"));           // false (長度不足)
        System.out.println("\"abcdefgh\" → " + isValidPassword("abcdefgh"));       // false (無大寫、無數字)
        System.out.println("\"Abcdefgh\" → " + isValidPassword("Abcdefgh"));       // false (無數字)
        System.out.println("\"Abc12345\" → " + isValidPassword("Abc12345"));       // true
        System.out.println("\"P@ssw0rd\" → " + isValidPassword("P@ssw0rd") + "\n"); // true

        // ----- 強密碼驗證測試 -----
        System.out.println("強密碼驗證測試：");
        System.out.println("\"Abc12345\" → " + isStrongPassword("Abc12345"));       // false (無特殊符號)
        System.out.println("\"P@ssw0rd\" → " + isStrongPassword("P@ssw0rd"));       // true
        System.out.println("\"Str0ng!\" → " + isStrongPassword("Str0ng!") + "\n");  // false (長度)

        // ----- 里程碑自我檢查 -----
        System.out.println("=== 里程碑自我檢查 ===");
        System.out.println("[ ] 能不看筆記寫出 while 和 for 迴圈");
        System.out.println("[ ] 能計算任意 for 迴圈的執行次數");
        System.out.println("[ ] 能追蹤巢狀迴圈的變數值");
        System.out.println("[ ] 能用迴圈處理 String 的每個字元");
        System.out.println("[ ] 能正確使用 break 和 continue");
        System.out.println("[ ] 能識別並修正常見的迴圈 bug");
        System.out.println("[ ] 能將迴圈邏輯封裝進方法");
    }

    /**
     * FRQ 範例：密碼驗證
     * 規則：長度 ≥ 8、含大寫字母、含數字
     */
    public static boolean isValidPassword(String password) {
        if (password.length() < 8) return false;

        boolean hasUpper = false;
        boolean hasDigit = false;

        for (int i = 0; i < password.length(); i++) {
            char c = password.charAt(i);
            if (c >= 'A' && c <= 'Z') hasUpper = true;
            if (c >= '0' && c <= '9') hasDigit = true;
        }

        return hasUpper && hasDigit;
    }

    /**
     * 進階：強密碼驗證
     * 規則：長度 ≥ 8、含大寫、含小寫、含數字、含特殊符號
     */
    public static boolean isStrongPassword(String password) {
        if (password.length() < 8) return false;

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

        return hasUpper && hasLower && hasDigit && hasSpecial;
    }
}
