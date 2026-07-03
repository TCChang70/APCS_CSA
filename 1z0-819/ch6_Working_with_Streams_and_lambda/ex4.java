package ch6_Working_with_Streams_and_lambda;




public class ex4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}

}
/*
Given:

var fruits=List.of("apple","orange","banana","lemon");
Optional<String> result=fruits.stream().filter(f->f.contains("n")).findAny();// line 1

System.out.println(result.get());

You replace the code on line 1 to use parallelStream.

Which one is correct?

A) The compilation fails.
B) The code will produce the same result
C) A NoSuchElementException is thrown at run time
D) The code may produce a different result



ans:D




*/