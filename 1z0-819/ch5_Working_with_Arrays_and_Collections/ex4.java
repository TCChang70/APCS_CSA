package ch5_Working_with_Arrays_and_Collections;

import java.util.ArrayList;
import java.util.Arrays;

public class ex4 {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] catNames={"abyssinian","oxicat",
				"korat","laperm","bengal","sphynx"};
			var cats=new ArrayList<>(Arrays.asList(catNames));
			cats.sort((var a,var b)->-a.compareTo(b));
			cats.forEach(System.out::println);
		
	}

}
/*
Given:

import java.util.ArrayList;
import java.util.Arrays;
public class NewMain{
	public static void main(String[] args) {
		String[] catNames={"abyssinian","oxicat",
			"korat","laperm","bengal","sphynx"};
		var cats=new ArrayList<>(Arrays.asList(catNames));
		cats.sort((var a,var b)-> -a.compareTo(b));
		cats.forEach(System.out::println);
	}
}


What is the result?

A) nothing

B) sphynx
   oxicat
   laperm
   korat
   bengal
   abyssinian
   
C) abyssinian
   oxicat
   korat
   laperm
   bengal
   sphynx
   
D) abyssinian
   bengal
   korat
   laperm
   oxicat
   sphynx
  
  
  
ans:B


*/