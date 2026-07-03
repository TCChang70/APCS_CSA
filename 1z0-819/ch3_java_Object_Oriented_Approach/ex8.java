package ch3_java_Object_Oriented_Approach;

public class ex8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		

	}

}
/*
Given:

public class Price{
	private final double value;
	public Price(String value){
		this(Double.parseDouble(value));
	}
	public Price(double value){
		this.value=value;
	}
	public Price(){}
	public double getValue(){ return value;}
	public static void main(String[] args)
	{
		Price p1=new Price("1.99");
		Price p2=new Price(2.99);
		Price p3=new Price();
		System.out.println(p1.getValue()+","+p2.getValue()+","+p3.getValue());
	}
}

What is the result?

A) 1.99,2.99,0.0
B) 1.99,2.99
C) The compilation fails
D) 1.99,2.99,0




ans:C




*/