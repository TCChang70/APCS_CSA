import java.util.Scanner;
public class forop1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        int sum=0;
        for (int i = 1; i <= n; i++) {
           if(i%2==0){
            if(i==n)
                System.out.print(i+"^2=");
            else
                System.out.print(i+"^2+");
            sum=sum-i*i;
           }else{
            if(i==n)
                System.out.print(i+"^2=");
            else
                System.out.print(i+"^2-");
            sum=sum+i*i;
           }
        }
        
        System.out.println(sum);
        scanner.close();
    }
}
