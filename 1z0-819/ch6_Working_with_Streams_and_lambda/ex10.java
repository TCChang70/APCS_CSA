package ch6_Working_with_Streams_and_lambda;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ex10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<String> fruits=List.of("banana","orange","apple","lemon");
		Stream<String> s1=fruits.stream();
		Stream<String> s2=s1.peek(i->System.out.print(i+" "));
		System.out.println("--------");
		
		Stream<String> s3=s2.sorted();
		Stream<String> s4=s3.peek(i->System.out.print(i+" "));
		System.out.println("--------");
		
		String strFruits=s4.collect(Collectors.joining(","));	
		

	}

}
/*
Given the code fragment:

public class Main {
	public static void main(String[] args)
	{
		List<String> fruits=List.of("banana","orange","apple","lemon");
		Stream<String> s1=fruits.stream();
		Stream<String> s2=s1.peek(i->System.out.print(i+" "));
		System.out.println("--------");
		Stream<String> s3=s2.sorted();
		Stream<String> s4=s3.peek(i->System.out.print(i+" "));
		System.out.println("--------");
		String strFruits=s4.collect(Collectors.joining(","));	
	}
}

What is the output?

A) --------
   --------
   banana orange apple lemon apple banana lemon orange

B) banana orange apple lemon
   ------
   apple banana lemon orange
   ------
   
C) -----
   banana orange apple lemon
   -----
   apple banana lemon orange
   
 D) -----
    -----
    
 E) banana orange apple lemon apple banana lemon orange
    ------
    ------
    
    
    
    
 ans:A



*/