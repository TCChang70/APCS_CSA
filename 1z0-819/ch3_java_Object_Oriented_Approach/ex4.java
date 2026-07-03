package ch3_java_Object_Oriented_Approach;

public class ex4 {
	enum Machine{
		AUTO("Truck"),MEDICAL("Scanner");
		private String type;
		private Machine(String type){
			this.type=type;
		}
		private void setType(String type){
			this.type=type;			//line 1
		}
		private String getType()
		{
			return type;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Machine.AUTO.setType("Sedan");		//line 2
		for(Machine p:Machine.values())
		{
			System.out.println(p+": "+p.getType());	//line 3
		}	
		
	}

}
/*
public class Menu{
	enum Machine{
		AUTO("Truck"),MEDICAL("Scanner");
		private String type;
		private Machine(String type){
			this.type=type;
		}
		private void setType(String type){
			this.type=type;			//line 1
		}
		private String getType()
		{
			return type;
		}
	}
	
	public static void main(String[] args)
	{
		Machine.AUTO.setType("Sedan");		//line 2
		for(Machine p:Machine.values())
		{
			System.out.println(p+": "+p.getType());	//line 3
		}	
	}
}


What is the result?

A) The compilation fails due to an error on line 3.
B) The compilation due to an error on line 2.
C) AUTO: Truck
   MEDICAL: Scanner
D) An exception is throw at run time
E) The compilation fails due to an error on line 1
F) AUTO: Sedan
   MEDICAL:Scanner
   
   

ans:F

*/