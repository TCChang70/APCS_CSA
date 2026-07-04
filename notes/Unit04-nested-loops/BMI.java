import java.util.Scanner;
public class BMI {
    public static void main(String[] args){
       Scanner input = new Scanner(System.in);
       System.out.print("Enter your name: ");
       String name = input.nextLine();
       System.out.print("Enter your age: ");
       int age = input.nextInt();
       System.out.print("How tall are you in(cm): ");
       int height = input.nextInt();
       System.out.print("How much do you weigh in(kg): ");
       int weight = input.nextInt();
       double heightInMeters = height / 100.0;
       double bmi = weight / (heightInMeters * heightInMeters);
       System.out.println(name + "'s BMI is: " + bmi);
       System.out.println("Age: " + age);
       input.close();
    }
}
