import java.util.Scanner;
public class InputGpa {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter your GPA: ");
        double gpa = scanner.nextDouble();
        System.out.println("Your Name is: " + name);
        System.out.println("Your GPA is: " + gpa);
        scanner.close();
    }
}
