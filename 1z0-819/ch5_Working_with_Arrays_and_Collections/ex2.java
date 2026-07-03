package ch5_Working_with_Arrays_and_Collections;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class ex2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 List<String> list=List.of("Mary","had","a","little","lamb");
		 Set<String> set=new HashSet<>(list);
				 set.addAll(list);
		
		for(String sheep:set)
			if(sheep.length()>1) //System.out.println(sheep);
				set.remove(sheep);
			//System.out.println(set);*/
		 

	}

}
/*
What does the following output?
18: List<String> list=List.of(
19:  "Mary","had","a","little","lamb");
20:	Set<String> set=new HashSet<>(list);
21: set.addAll(list);
22: for(String sheep:set)
23:		if(sheep.length()>1)
24:			set.remove(sheep);
25: System.out.println(set);

A. [a.lamb,had,Mary,little]
B. [a]
C. [a,a]
D. The code does not compile.
E. The code throws an exception at runtime




ans:E.




*/