package ch1_working_with_java_data_types;

public class ex6 {
	public void process(byte v){
		System.out.println("Byte value "+v);
	}
	public void process(short v){
		System.out.println("Short value "+v);
	}
	public void process(Object v){
		System.out.println("Object value "+v);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		byte x=12;
		short y=13;
		//promotion
		int z = x + y;
		//Integer it = z;
		new ex6().process(x+y);// line 1
		
	}

}
/*
Given:

public class Test{
	public void process(byte v){
		System.out.println("Byte value "+v);
	}
	public void process(short v){
		System.out.println("Short value "+v);
	}
	public void process(Object v){
		System.out.println("Object value "+v);
	}
	public static void main(String[] args){
		byte x=12;
		short y=13;
		new Test().process(x+y);// line 1
	}
}

What is the output?

A) Object value 25
B) Byte value 25
C) Short value 25
D) The compilation fails due to an error in line 1




ans:A
*/