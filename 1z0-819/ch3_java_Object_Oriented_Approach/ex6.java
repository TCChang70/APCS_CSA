package ch3_java_Object_Oriented_Approach;

public class ex6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
/*
Given:

package test.t1;
public class A{
	public int x=42;
	protected A(){}      //line 1
}

and

package test.t2;
import test.t1.*;
public class B extends A{
	int x=17;				//line 2
	public B(){super();}	//line 3
}


and

package test;
import test.t1.*;
import test.t2.*;
public class Tester{
	public static void main(String[] args){
		A obj=new B();					//line 4
		System.out.println(obj.x);		//line 5	
	}
}

What is the result?

A) The compilation fails due to an error in line 4
B) 17
C) The compilation fails due to an error in line 2
D) The compilation fails due to an error in line 3
E) The compilation fails due to an error in line 1
F) The compilation fails due to an error in line 5
G) 42



ans:G


*/