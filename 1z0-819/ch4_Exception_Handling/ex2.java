package ch4_Exception_Handling;

public class ex2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
/*
Given the following application, what is the name of the class printed at line e1?

package canyon;
final class FallenException extends Exception{}
final class HikingGer implements AutoCloseable{
	@Override public void close() throws Exception{
		throw new FallenException();
	}
}

public class Cliff{
	public final void climb() throws Exception{
		try(HikingGear gear=new HikingGear()){
			throw new RuntimeException();
		}	
	}
	public static void main(String... rocks){
		try{
			new Cliff().climb();		
		}catch(Throwable t){
			System.out.println(t); //e1
		}	
	}
}


A. canyon.fallenException
B. java.lang.RuntimeException
C. The code does not compile.
D. The code compile, but the answer cannot be determined until runtime.
E. None of the above


ans:B


*/