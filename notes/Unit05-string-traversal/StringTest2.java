public class StringTest2 {
    public static void main(String[] args){
        String str1 = "Danny Chen";
        int position = str1.indexOf(' ');
        String leftPart = str1.substring(0, position);
        String rightPart = str1.substring(position + 1);
        System.out.println("Left part: " + leftPart);
        System.out.println("Right part: " + rightPart);
        
    }
}
