/**
 * Unit 11：Array 宣告與初始化 — 練習程式
 * 包含範例和練習題解答
 */
public class ArrayDeclarationPractice {

    public static void main(String[] args) {
        System.out.println("=== Unit 11: Array 宣告與初始化 ===\n");

        // ----- 範例 1：三種初始化方式 -----
        System.out.println("範例 1：三種初始化方式");
        int[] nums1 = new int[5];
        int[] nums2 = {85, 90, 78, 92, 88};
        int[] nums3;
        nums3 = new int[]{10, 20, 30};

        System.out.print("nums1（預設值）：");
        for (int i = 0; i < nums1.length; i++) {
            System.out.print(nums1[i] + " ");
        }
        System.out.println();

        System.out.print("nums2（初始值清單）：");
        for (int i = 0; i < nums2.length; i++) {
            System.out.print(nums2[i] + " ");
        }
        System.out.println();

        System.out.print("nums3（先宣告後賦值）：");
        for (int i = 0; i < nums3.length; i++) {
            System.out.print(nums3[i] + " ");
        }
        System.out.println("\n");

        // ----- 範例 2：String 陣列 -----
        System.out.println("範例 2：String 陣列");
        String[] fruits = {"apple", "banana", "cherry"};
        System.out.println("最後一個水果：" + fruits[fruits.length - 1] + "\n");

        // ----- 練習題 1 (Easy)：基本操作 -----
        System.out.println("練習題 1：陣列基本操作");
        int[] arr = {10, 20, 30, 40, 50};
        System.out.println("第一個：" + arr[0]);
        System.out.println("最後一個：" + arr[arr.length - 1]);
        System.out.println("長度：" + arr.length + "\n");

        // ----- 練習題 2 (Easy)：填入偶數 -----
        System.out.println("練習題 2：填入偶數");
        int[] evens = new int[5];
        for (int i = 0; i < evens.length; i++) {
            evens[i] = (i + 1) * 2;
        }
        System.out.print("偶數陣列：");
        for (int i = 0; i < evens.length; i++) {
            System.out.print(evens[i] + " ");
        }
        System.out.println("\n");

        // ----- 現在試試看：成績陣列 -----
        System.out.println("現在試試看：5 門課成績");
        int[] grades = {88, 92, 76, 85, 90};
        for (int i = 0; i < grades.length; i++) {
            System.out.println("成績[" + i + "] = " + grades[i]);
        }
    }
}
