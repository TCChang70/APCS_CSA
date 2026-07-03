package ch1_working_with_java_data_types;

public class ex5 {
	static StringBuilder sb1=new StringBuilder("yo ");
	StringBuilder sb2=new StringBuilder("hi ");

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		sb1=sb1.append(new ex5().foo(new StringBuilder("hey")));//hey oh hi yo ey
		System.out.println(sb1);
		
	}
	StringBuilder foo(StringBuilder s){
		System.out.print(s+" oh " +sb2);
		return new StringBuilder("ey");
	}
	

}
/*
Given:

public class StrBldr{
	static StringBuilder sb1=new StringBuilder("yo ");
	StringBuilder sb2=new StringBuilder("hi ");
	
	public static void main(String[] args){
		sb1=sb1.append(new StrBldr().foo(new StringBuilder("hey")));
		System.out.println(sb1);
	}
	
	StringBuilder foo(StringBuilder s){
		System.out.print(s+" oh " +sb2);
		return new StringBuilder("ey");
	}
	
}

What is the result?

A) oh hi hey
B) hey oh hi
C) A compile time error occurs.
D) hey oh hi yo ey
E) yo ey
F) hey oh hi ey


ans:D


*/