import java.util.Scanner;
public class Power3 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int value=1;
        System.out.print("Enter the power: ");
        int p = input.nextInt();
        System.out.print("Enter the base: ");
        int b = input.nextInt();
        for(int i=1;i<=p;i++)
        {
            value *= b;
            
        }
        System.out.println(b + "^" + p + " = " + value);
        input.close();
    }
}
