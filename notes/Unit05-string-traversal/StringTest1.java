public class StringTest1 {
    public static void main(String[] args) {
        String str1 = "Hello";
        int length = str1.length();
        for(int i=0; i<length; i++) {
            System.out.println("index " + i + ": " + str1.charAt(i));
        }
        int position=str1.indexOf('e');
        System.out.println("The position of 'e' is: " + position);
        String str2 = str1.substring(1, 3);
        System.out.println("Substring from index 1 to 3: " + str2);
    }
}
