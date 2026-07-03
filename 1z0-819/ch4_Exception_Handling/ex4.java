package ch4_Exception_Handling;

import java.io.FileReader;
import java.io.IOException;

public class ex4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		

	}

}
/*
Given:

   char[] characters=new char[100];
   try(FileReader reader=new FileReader("file_to_path");){
	// line 1
	  System.out.println(String.valueOf(characters));
	} catch(IOException e){
	  e.printStackTrace();	
	}

	You want to read data through the reader object.
	
	Which statement inserted on line 1 will accomplish this?
	
	A) reader.readLine();
	B) characters=reader.read();
	C) reader.read(characters);
	D) characters.read();
	
	
	ans:C


*/