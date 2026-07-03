package ch4_Exception_Handling;

import java.io.IOException;

public class ex1 {

	public static void main(String[] args) throws IOException  {
		// TODO Auto-generated method stub
		try {
			throw new ClassCastException();
		} catch (IllegalArgumentException e) {
			throw new IllegalArgumentException();
		} catch (RuntimeException e) {
			throw new NullPointerException();
		} 
		

	}

}
/*
Given the following application, which specific type of exception will be printed in the stack trace at runtime?

package carnival;
public class WhackAnException{
	public static void main(String... hammer)
	{
		try{
			throw new ClassCastException();
		}catch(IllegalArgumentException e){
			throw new IlleaglArgumentException();
		}catch(RuntimeException e){
			throw new NullPointerException();
		}finally{
			throw new RuntimeException();
		}
	
	}

}

A. ClassCastException
B. IllegalArgumentException
C. NullPointerException
D. RuntimeException
E. The code does not compile.
F. None of the above




ans:D



*/