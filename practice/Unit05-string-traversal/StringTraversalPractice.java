/**
 * Unit 05：String 字串遍歷 — 練習程式
 * 包含範例和練習題解答
 */
public class StringTraversalPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 05: String 字串遍歷 ===\n");

        // ----- 範例 1：印出每個字元 -----
        System.out.println("範例 1：印出每個字元");
        String s = "Java";
        for (int i = 0; i < s.length(); i++) {
            System.out.println(s.charAt(i));
        }
        System.out.println();

        // ----- 範例 2：統計 'a' 出現次數 -----
        System.out.println("範例 2：統計 'a' 出現次數");
        String text = "banana";
        int count = 0;
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == 'a') count++;
        }
        System.out.println("a 出現 " + count + " 次\n");

        // ----- 範例 3：反轉字串 -----
        System.out.println("範例 3：反轉字串");
        String original = "Hello";
        String reversed = "";
        for (int i = original.length() - 1; i >= 0; i--) {
            reversed += original.charAt(i);
        }
        System.out.println("反轉後：" + reversed + "\n");

        // ----- 範例 4：回文判斷 -----
        System.out.println("範例 4：回文判斷");
        String word = "racecar";
        boolean isPalindrome = true;
        for (int i = 0; i < word.length() / 2; i++) {
            if (word.charAt(i) != word.charAt(word.length() - 1 - i)) {
                isPalindrome = false;
            }
        }
        System.out.println(word + " 是回文嗎？" + isPalindrome + "\n");

        // ----- 練習題 1 (Easy)：統計大寫字母 -----
        System.out.println("練習題 1：統計大寫字母");
        String str = "Hello World APCS";
        int upperCount = 0;
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c >= 'A' && c <= 'Z') {
                upperCount++;
            }
        }
        System.out.println("大寫字母數：" + upperCount + "\n");

        // ----- 練習題 2 (Medium)：刪除母音 -----
        System.out.println("練習題 2：刪除母音");
        String input = "Hello World";
        String result = "";
        String vowels = "aeiouAEIOU";
        for (int i = 0; i < input.length(); i++) {
            if (vowels.indexOf(input.charAt(i)) == -1) {
                result += input.charAt(i);
            }
        }
        System.out.println("刪除母音後：" + result + "\n");

        // ----- 現在試試看：忽略大小寫的回文判斷 -----
        System.out.println("現在試試看：進階回文判斷");
        String test = "A man a plan a canal Panama";
        String clean = "";
        for (int i = 0; i < test.length(); i++) {
            char c = test.charAt(i);
            if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) {
                if (c >= 'A' && c <= 'Z') {
                    c = (char) (c + 32);  // 轉小寫
                }
                clean += c;
            }
        }
        boolean palin = true;
        for (int i = 0; i < clean.length() / 2; i++) {
            if (clean.charAt(i) != clean.charAt(clean.length() - 1 - i)) {
                palin = false;
            }
        }
        System.out.println("「" + test + "」是回文嗎？" + palin);
    }
}
