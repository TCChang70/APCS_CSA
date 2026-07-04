import java.util.Scanner;
public class StudentGrade {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the student's name: ");
        String name = scanner.nextLine();
        System.out.print("Enter the 1st grade: ");
        double grade1 = scanner.nextDouble();
        System.out.print("Enter the 2nd grade: ");
        double grade2 = scanner.nextDouble();
        System.out.print("Enter the 3rd grade: ");
        double grade3 = scanner.nextDouble();
        double average = (grade1 + grade2 + grade3) / 3;
        System.out.println(name + "'s average grade is: " + average);
        scanner.close();
    }
}
