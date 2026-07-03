package ch1_working_with_java_data_types;

public class ex3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		var i=10;
		var j=5;
		i+=(j*5+i)/j-2;//i=i+(j*5+i)/j-2--.=10+35/5-2=10+7-2
		System.out.println(i);

	}

}
/*
Given the code fragment:

var i=10;
var j=5;
i+=(j*5+i)/j-2;
System.out.println(i);

What is the result?

A) 5
B) 11
C) 21
D) 23
E) 15


ans:E
*/