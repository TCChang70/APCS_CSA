import java.util.Scanner;
public class InputNumber {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        System.out.println("You entered: " + number);
        int sum = 0;
        int i = 1;
        while (i <= number) {
           sum += i;   // sum=sum+i                   
           i++;
        }
        System.out.println("The sum of numbers from 1 to " + number + " is: " + sum);
        scanner.close();
    }
}
