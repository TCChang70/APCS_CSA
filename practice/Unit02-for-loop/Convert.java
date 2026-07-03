import java.util.Scanner;
public class Convert {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a value in Celsius: ");
        double celsius = scanner.nextDouble();
        double fahrenheit = (celsius * 9/5) + 32;
        //  (fahrenheit-32) * 5/9 = celsius
        System.out.println("Temperature in Fahrenheit: " + fahrenheit);
        scanner.close();
    }
}
