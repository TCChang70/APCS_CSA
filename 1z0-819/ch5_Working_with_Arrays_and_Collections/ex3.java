package ch5_Working_with_Arrays_and_Collections;

import java.util.ArrayList;
import java.util.Iterator;

public class ex3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}

}
/*
Given:

ArrayList<Integer> a1=new ArrayList<>();
a1.add(1);
a1.add(2);
a1.add(3);
Iterator<Integer> itr=a1.iterator();
while(itr.hasNext()) {
	if(itr.next()==2) {
			a1.remove(2);
		System.out.print(itr.next());
	}
}

What is the result?

A) 1 2 followed by an exception
B) 1 2 3 followed by an exception
C) A ConcurrentModificationException is thrown at run time
D) 1 2 4 5


ans:C
	


*/