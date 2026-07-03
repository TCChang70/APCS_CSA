package ch6_Working_with_Streams_and_lambda;




public class ex8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		


	}

}
/*
Given the content from lines.txt

C
C++
Java
Go
Kotlin


and

String fileName="lines.txt";
List<String> list=new ArrayList<>();
try(Stream<String> stream=Files.lines(Paths.get(fileName))) {
		list=stream
		           .filter(line->!line.equalsIgnoreCase("JAVA"))
		           .map(String::toUpperCase)
		           .collect(Collectors.toList());
	} catch(IOException e) {

	}
list.forEach(System.out::println);


What is the Result?

A) C
   C++
   Go
   Kotlin
   
B) JAVA

C) C
   C++
   GO
   KOTLIN
   
D) C
   C++
   JAVA
   GO
   KOTLIN
   
   
ans:C






*/