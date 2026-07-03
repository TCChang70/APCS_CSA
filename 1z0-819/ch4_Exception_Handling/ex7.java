package ch4_Exception_Handling;


public class ex7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		

	}
	
	
	

}
/*
Given:

import java.io.*;
public class Tester {
	public static void main(String args[])
	{
		try{
			doA();
			doB();	
		} catch(IOException e) {
			System.out.print("c");
			return;	
		} finally {
			System.out.print("d");	
		}
		System.out.print("f");
	}
	private static void doA() {
		System.out.print("a");
		if(false) {
			throw new IndexOutOfBoundsException();
		}	
	}
	private static void doB() throws FileNotFoundException {
		System.out.print("b");
		if(true) {
			throw new FileNotFoundException();
		}	
	}
}

What is the result?

A) The compilation fails.
B) adf
C) abd
D) abcd
E) abdf



ans:D


*/