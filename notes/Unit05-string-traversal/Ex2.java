public class Ex2 {
    public static void main(String[] args){
      String str1="Hello World";
      int len=str1.length();
      for(int i=0;i<len;i++){
        switch(str1.charAt(i)){
          case 'a':
          case 'e':
          case 'i':
          case 'o':
          case 'u':
          case 'A':
          case 'E':
          case 'I':
          case 'O':
          case 'U':            
            break;
          default:
            System.out.print(str1.charAt(i));
        }       
      }
      System.out.println();
    }
}
