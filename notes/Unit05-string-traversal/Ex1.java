public class Ex1 {
    public static void main(String[] args){
      String str="Hello World APCS";
      int length = str.length();
      int uppercase=0;
      for(int i=0; i<length; i++) {
         char ch= str.charAt(i);
         if(ch>='A' && ch<='Z') {
            uppercase++;
         }
      }
      System.out.println("Number of uppercase letters: " + uppercase);
    }
}
