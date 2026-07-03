package ch3_java_Object_Oriented_Approach;
public class ex1 {
	interface Long {
		Number length();
	}

	class Elephant {
		public class Trunk implements Long {
			public Number length() {
				return 6;
			} //k1
		}

		public class MyTrunk extends Trunk { //k2
			
			public Double length() {
				return 9.0;
			} //k3
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
	}

}
/*
Which statement about the Elephant program is correct?

package stampede;
interface Long{
	Number length();
}

public class Elephant{
	public class Trunk implements Long{
		public Number length(){ return 6;} //k1
	}
	
	public class MyTrunk extends Trunk{		//k2
		public Integer length(){ return 9;} //k3
	}
	public static void charage(){
		System.out.print(new MyTrunk().length());
	}
	
	public static void main(String[] cute){
		new Elephant().charge();			//k4
	}
	
}

A. It compiles nad prints 6.
B. The code does not compile because of line k1.
C. The code does not compile becaues of line k2.
D. The code does not compile becaues of line k3.
E. The code does not compile becaues of line k4.
F. None of the above





ans:F
*/