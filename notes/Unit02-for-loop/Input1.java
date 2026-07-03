import java.util.Scanner;
public class Input1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input your age:");
        int age = scanner.nextInt();
        System.out.print("Input your gpa score:(1.0-4.0)");
        double gpa = scanner.nextDouble();
        scanner.nextLine(); // Consume the newline left-over
        System.out.print("Input your name:");        
        String name = scanner.nextLine();
        System.out.print("Input your gender:(M/F)");
        boolean gender = scanner.nextBoolean();
        System.out.println("Your age is: " + age);
        System.out.println("Your gpa score is: " + gpa);
        System.out.println("Your name is: " + name);
        System.out.println("Your gender is: " + gender);
        scanner.close();
    }
}
