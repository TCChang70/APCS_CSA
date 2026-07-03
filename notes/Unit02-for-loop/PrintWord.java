public class PrintWord {
    public static void main(String[] args) {
        String word = "123456789";
        // for (int i = 0; i < word.length(); i++) {
        //     System.out.println(word.charAt(i));
        // }
        for(int i=word.length()-1; i>=0; i--){
            System.out.println(word.charAt(i));
        }
    }
}
