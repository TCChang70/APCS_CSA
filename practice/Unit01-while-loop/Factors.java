public class Factors {
    public static void main(String[] args) {
        int n=24;
        int i=1;
        while(i<=n){
            if(n%i==0){
                System.out.print(i + " ");
            }
            i++;
        }   
    }
}
