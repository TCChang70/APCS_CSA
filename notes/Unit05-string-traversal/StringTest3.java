public class StringTest3 {
    public static void main(String[] args){
        String str1="racecar";
        String rev="";
        for(int i=str1.length()-1;i>=0;i--){
            rev=rev+str1.charAt(i);
        }
        if(str1.equals(rev)){
            System.out.println("The string is a palindrome");
        } else {
            System.out.println("The string is not a palindrome");
        }
    }
}
