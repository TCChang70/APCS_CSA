package unit2;
import java.util.Scanner;
public class CalculatorMain {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter two numbers: ");
        System.out.print("First number: ");
        double a = input.nextDouble();
        System.out.print("Second number: ");
        double b = input.nextDouble();
        System.out.println("1) Basic Operations 2) Advanced Operations");
        System.out.print("Enter your choice: ");
        int choice = input.nextInt();
        switch (choice) {
            case 1:
                Caluclator.basicOperation(a, b);
                break;
            case 2:
                Caluclator.advancedOperation(a, b);
                break;
            default:
                System.out.println("Invalid choice!");
        }
        input.close();
    }
}
