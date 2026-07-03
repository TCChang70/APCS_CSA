public class PrintZZ {
    public static void main(String[] args) {
        int num=30;
        for(int i=1;i<=num;i++){
            if(i%3==0 && i%5==0){
                System.out.println(i+" FIZZBUZZ");
            }else if(i%3==0){
                System.out.println(i+" FIZZ");
            }else if(i%5==0){
                System.out.println(i+" BUZZ");
            }
        }
    }
}
