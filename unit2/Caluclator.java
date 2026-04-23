package unit2;

public class Caluclator {
    public static void basicOperation(double a, double b) {
        System.out.println("Addition " + a + " and " + b + " is: " + (a + b));
        System.out.println("Subtraction " + a + " and " + b + " is: " + (a - b));
        System.out.println("Multiplication " + a + " and " + b + " is: " + (a * b));    
        System.out.println("Division " + a + " and " + b + " is: " + (a / b));
    }
    public static void advancedOperation(double a, double b) {
        System.out.println("Power of " + a + " and " + b + " is: " + Math.pow(a, b));
        System.out.println("Square root of " + a + " is: " + Math.sqrt(a));
        System.out.print("Absolute value of " + a + " is: " + Math.abs(a));
        System.out.println(" Absolute value of " + b + " is: " + Math.abs(b));
    } 
}
