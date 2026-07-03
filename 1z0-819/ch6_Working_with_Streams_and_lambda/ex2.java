package ch6_Working_with_Streams_and_lambda;

import java.util.function.BooleanSupplier;
import java.util.function.UnaryOperator;

public class ex2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		UnaryOperator<Integer> op = (var i) -> i * 2;
	}

}

class Warehouse {
	private int quantity = 40;
	private final BooleanSupplier stock;
	{
		stock = () -> quantity > 0;
	}

	public void checkInventory() {
		if (stock.get())
			System.out.print("Plenty!");
		else {
			System.out.print("On Backorder!");
		}
	}
}
/*
 * What is the output of the following application?
 * package lot;
 * import java.util.function.*;
 * 
 * public class Warehouse {
 * private int quantity=40;
 * private final BooleanSupplier stock;
 * {
 * stock=()->quantity>0;
 * }
 * 
 * public void checkInventory() {
 * if(stock.get())
 * System.out.print("Plenty!");
 * else {
 * System.out.print("On Backorder!");
 * }
 * }
 * 
 * 
 * public static void main(String... widget) {
 * final Warehouse w13=new Warehouse();
 * w13.checkInventory();
 * }
 * }
 * 
 * 
 * A. Plenty
 * B. On Backorder!
 * C. The code does not compile because of the checkInventory() method.
 * D. The code does not compile for a different reason
 * 
 * 
 * 
 * ans:C
 */