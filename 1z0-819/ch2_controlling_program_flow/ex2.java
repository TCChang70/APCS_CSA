package ch2_controlling_program_flow;

public class ex2 {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 var plan=1;
	 plan=plan++ + --plan;
	 if(plan==1){
		 System.out.print("Plan A");
	 }else{
		 if(plan==2)
		    System.out.print("Plan B");
	  }
	  System.out.print("Plan C");}

	

}

/*
What is the output of the following application?

package planning;
 public class ThePlan{
	 var plan=1;
	 plan=plan++ + --plan;
	 if(plan==1){
		 System.out.print("Plan A");
	 }else{ if(plan==2) System.out.print("Plan B");
	 }else System.out.print("Plan C");}
	}
}

A. Plan A
B. Plan B
C. Plan C
D. The class does not compile
E. None of the above




ans: D




*/