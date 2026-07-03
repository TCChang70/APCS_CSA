package ch4_Exception_Handling;

public class ex8 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
		

	}

}
/*
Given:

public class Test{
	private int num=1;
	private int div=0;
	
	public void divide() {
		try {
			num=num/div;
			System.out.print("Exception");
		}
		catch(ArithmeticException ae) { num=100; }
		catch(Exception e) { num=200; }
		finally { num=300; }
		System.out.print(num);	
	}
	public static void main(String args[])
	{
		Test test=new Test();
		test.divide();	
	}

}

What is the ouput?

A) 200
B) 100
C) 300
D) Exception




ans: c




*/