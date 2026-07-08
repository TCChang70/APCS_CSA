public class Fib {
    public static void main(String[] args){
        int f1=1;
        int f2=1;
       for(int i=3;i<=15;i++){
           int f3=f1+f2;
           System.out.print(f3+"  ");           
           f1=f2;
           f2=f3;
       }
    }
}
