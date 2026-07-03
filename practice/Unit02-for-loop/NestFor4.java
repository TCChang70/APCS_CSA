public class NestFor4 {
    public static void main(String[] args){
       int count = 0;
       for (int i = 0; i < 4; i++) {
          for (int j = 0; j < i; j++) {
              count++;
          }
       }
       System.out.println(count); 
    }
}
