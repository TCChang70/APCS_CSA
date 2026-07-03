package ch10_Secure_Coding_in_java_se_Application;

public class ex3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
/*
Given:

public class Foo {
	public static String ALPHA="alpha";
	protected String beta="beta";
	private final String delta;
	public Foo(String d) {
		delta=ALPHA+d;	
	}
	public String foo() {
		return beta+=delta	
	}
}

Which change would make Foo more secure?

A) private String delta;
B) public String beta="beta";
C) protected final String beta="beta";
D) public static final String ALPHA="alpha";



ans:D



*/