public class scope {
    public static void main(String[] args) {
       int x=0; 
       for(int i=0;i<5;i++){
        x=10;
        System.out.println("x = "+x);
       }
        System.out.println("x = "+x);
    }
}
