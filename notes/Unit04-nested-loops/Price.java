import java.util.Scanner;
public class Price {
    public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       System.out.println("Product Unit Price:");
       double unitPrice = input.nextDouble();
       System.out.println("Product Quantity:");
       double quantity = input.nextDouble();
       System.out.println("Product Tax(%):");
       double tax = input.nextDouble();
       System.out.println("Customer Paid:");
       double customerPaid = input.nextDouble();
       double subtotal = unitPrice * quantity;
       double totalTax = subtotal * (tax / 100);
       double grandTotal = subtotal + totalTax;
       double change = customerPaid - grandTotal;
       System.out.println("Subtotal: $" + subtotal);
       System.out.println("Total Tax: $" + totalTax);
       System.out.println("Grand Total: $" + grandTotal);
       System.out.println("Change: $" + change);
    }
}
