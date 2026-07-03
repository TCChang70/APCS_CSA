package ch3_java_Object_Oriented_Approach;

public class ex12 {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		

	}

	

}
/*
Given:

interface AbilityA{
	default void action(){
		System.out.println("a action");
	}
}

and

interface AbilityB{
	void action();

}

and

public class Test implements AbilityA,AbilityB{ // line 1
	public void action() {
		System.out.println("ab action");
	}
	public static void main(S[] args){ 
		AbilityB x=new Test(); 			//line 2
		x.action();	
	}
}

What is the result?

A) The compilation fails on line 1
B) An exception is thrown at run time
C) The compilation fails on line 2
D) a action
E) ab action




ans:E

*/