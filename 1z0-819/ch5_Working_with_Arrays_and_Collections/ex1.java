package ch5_Working_with_Arrays_and_Collections;

import java.util.Collection;

public class ex1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static void getExceptions(Collection<? super Exception> coll) {
		coll.add(new RuntimeException());
		coll.add(new Exception());
	}

}
/*
Which of the following fills in the blank so this code compiles?
public static void getExceptions(Collection<__> coll){
	coll.add(new RuntimeException());
	coll.add(new Exception());
}


A. ?
B. ? extends Exception
C. ? super Exception
D. None of the above


ans:C


*/