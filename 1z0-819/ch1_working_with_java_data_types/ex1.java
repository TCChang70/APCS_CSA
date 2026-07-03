package ch1_working_with_java_data_types;

import java.util.Comparator;

public class ex1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
	}

}
/*
How many of these compile?
18: Comparator<String> c1=(j,k)->0;
19: Comparator<String> c2=(String j,String k)->0;
20: Comparator<String> c3=(var j,String k)->0;
21: Comparator<String> c4=(var j,k)->0;
22: Comparator<String> c5=(var j,var k)->0;

A. 0
B. 1
C. 2
D. 3
E. 4
F. 5


ans:D

*/