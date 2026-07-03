package ch4_Exception_Handling;

import java.util.Optional;

public class ex6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Ans: "+convert("10").get());	
		

	}
	
	private static Optional<Integer> convert(String s) {
		try{
			return Optional.of(Integer.parseInt(s));		
		} catch(Exception e) {
			return Optional.empty();
		}	
	}
}
/*
Given:

public class Option{
	public static void main(String[] args) {
		System.out.println("Ans: "+convert("a").get());	
	}
	
	private static Optional<Integer> convert(String s) {
		try{
			return Optional.of(Integer.parseInt(s));		
		} catch(Exception e) {
			return Optional.empty();
		}	
	}
}

What is the result?

A) Ans:
B) Ans: a
C) A java.util.NoSuchFilementException is thrown at run time
D) The compilation fails


ans:C


*/