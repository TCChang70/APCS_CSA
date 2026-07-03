package ch4_Exception_Handling;

import java.io.FileNotFoundException;

class ExSuper extends Exception{
	private final int eCode;
	public ExSuper(int eCode,Throwable cause){
		super(cause);
		this.eCode=eCode;
	}
	
	public ExSuper(int eCode,String msg,Throwable cause){
		super(msg,cause);
		this.eCode=eCode;	
	}
	
	public String getMessage(){
		return this.eCode+": "+super.getMessage()+"_"+this.getCause().getMessage();	
	}
}
class ExSub extends ExSuper{
	public ExSub(int eCode,String msg,Throwable cause)
	{
		super(eCode,msg,cause);
	}	
}
public class ex5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
			String param1="oracle";
			if(param1.equalsIgnoreCase("oracle")) {
				throw new ExSub(9001, "APPLICATION ERROR-9001",new FileNotFoundException("MyFile.txt"));	
				}
				throw new ExSuper(9001, new FileNotFoundException("MyFile.txt")); // Line 1
		}
		catch(ExSuper ex)
		{
			System.out.println(ex.getMessage());
		}
		

	}

}
/*
Given:

public class ExSuper extends Exception{
	private final int eCode;
	public ExSuper(int eCode,Throwable cause){
		super(cause);
		this.eCode=eCode;
	}
	
	public ExSuper(int eCode,String msg,Throwable cause){
		super(msg,cause);
		this.eCode=eCode;	
	}
	
	public String getMessage(){
		return this.eCode+": "+super.getMessage()+"_"+this.getCause().getMessage();	
	}
}
	
public class ExSub extends ExSuper{
	public ExSub(int eCode,String msg,Throwable cause)
	{
		super(eCode,msg,cause);
	}	
}

and the code fragment:

try{
	String param1="oracle";
	if(param1.equalsIgnoreCase("oracle")) {
		throw new ExSub(9001, "APPLICATION ERROR-9001",new FileNotFoundException("MyFile.txt"));	
		}
		throw new ExSuper(9001, new FileNotFoundException("MyFile.txt")); // Line 1
}
catch(ExSuper ex)
{
	System.out.println(ex.getMessage());
}


What is the result?

A) Compilations fails at Line 1;
B) 9001: java.io.FileNotFoundException:MyFile.txt-MyFile.txt
C) 9001: APPLICATION ERROR-9001-MyFile.txt
D) 9001: APPLICATION ERROR-9001-MyFile.txt
   9001: java.io.FileNotFoundException: MyFile.txt-MyFile.txt
   
   
ans: C






*/