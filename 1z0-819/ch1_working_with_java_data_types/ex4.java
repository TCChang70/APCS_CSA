package ch1_working_with_java_data_types;

public class ex4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StringBuilder sb=new StringBuilder(10);
		System.out.println(sb.length());
		sb.append("HOWDY");//HOWDY
		System.out.println(sb.length());
		sb.insert(0,' ');// HOWDY
		System.out.println(sb.length());
		
		sb.replace(3,5,"LL");// HOLLY
		System.out.println(sb.length());
		
		sb.insert(6,"COW");// HOLLYCOW
		System.out.println(sb.length());
		sb.delete(2,7);// HOW
		System.out.println(sb.length());
		

	}

}
/*
Given:

public class Tester{
	public static void main(String[] args){
		StringBuilder sb=new StringBuilder(5);
		sb.append("HOWDY");
		sb.insert(0,' ');
		sb.replace(3,5,"LL");
		sb.insert(6,"COW");
		sb.delete(2,7);
		System.out.println(sb.length());
	}
}

What is the result?

A) 5
B) 3
C) An exception is thrown at runtime.
D) 4


ans:D


*/