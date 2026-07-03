package ch6_Working_with_Streams_and_lambda;


public class ex5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		

	}

}
/*
Given the code fragment:

 1. var list=List.of(1,2,3,4,5,6,7,8,9,10);
 2. UnaryOperator<Integer> u=i->i*2;
 3. list.replaceAll(u);
 
Which can replace line 2?

A) UnaryOperator<Integer> u=var i->{return i*2;}
B) UnaryOperator<Integer> u=i->{return i*2;}
C) UnaryOperator<Integer> u=(var i)->(i*2);
D) UnaryOperator<Integer> u=(int i)->i*2;


ans:C
*/