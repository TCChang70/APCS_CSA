package ch4_Exception_Handling;

import java.io.FileNotFoundException;

public class ex3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		

	}
	
	
}
/*
Given:

import java.io.FileNotFoundException;
import java.io.IOException;

public class Tester{
	public static void main(String[] args){
		try{
			doA();
		}//line 1
	}
	private static void doA() throws Exception,IndexOutOfBoundsException{
		if(false){
			throw new FileNotFoundException();
		}else{
			throw now IndexOutOfBoundsException();
		}
	}
}

What must be added in line 1 to compile this class?

A) catch(FileNotFoundException | Exception e){}
B) catch(FileNotFoundException e){}
   catch(IndexOutOfBoundsException e){}
C) catch(Exception e){}
D) catch(IndexOutOfBoundsEexception e){}
   catch(FileNotFoundException e){}

E) catch(FileNotFoundException | IndexOutBoundException e){}


ans:C


*/