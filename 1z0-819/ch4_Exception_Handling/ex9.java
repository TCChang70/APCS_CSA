package ch4_Exception_Handling;

public class ex9 {
	private int sum;
	public int compute() {
		int x=0;
		while(x<3) {
			sum+=++x;
			/*
			 * sum=sum+++x;
			 * x=x+1;
			 * sum=sum+x;
			 * 
			 */
			System.out.println("x="+x+"\tsum="+sum);
		}
		return sum/4;	
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ex9 t=new ex9();
		int sum=t.compute();
		sum=t.compute();
		System.out.print(sum);
		
		

	}

}
/*
Given:

public class Test {
	private int sum;
	public int compute() {
		int x=0;
		while(x<3) {
			sum+=++x;
		}
		return sum/4;	
	}
	
	public static void main(String[] args) {
		Test t=new Test();
		int sum=t.compute();
		sum=t.compute();
		System.out.print(sum);
	}
}

What is the output?

A) 6
B) 3
C) An exception is thrown at runtime
D) 9




ans:B



*/