package ch3_java_Object_Oriented_Approach;
abstract class Ball{
	protected final int size;
	public Ball(int size){
		this.size=size;
	}
}
interface Equipment{}
class SoccerBall extends Ball implements Equipment{
	public SoccerBall(){
		super(5);
	}
	public Ball get(){ return this; }
	

}
public class ex2 {

	public static void main(String[] args) {
		var equipment=(Equipment)(Ball)new SoccerBall().get();
		System.out.print(((SoccerBall)equipment).size);
		
	}

}
/*
What is the output of the following application?

package sports;
abstract class Ball{
	protected final int size;
	public Ball(int size){
		this.size=size;
	}
}

interface Equipment{}

public class SoccerBall extends Ball implements Equipment{
	public SoccerBall(){
		super(5);
	}
	public Ball get(){ return this; }
	public static void main(String[] passes){
		var equipment=(Equipment)(Ball)new SoccerBall().get();
		System.out.print(((SoccerBall)equipment).size);
	}

}


A. 5
B. The code does not compile due to an invalid cast
C. The code does not compile for a different reason
D. The code compiles but throws a ClassCastException at runtime


Ans A




*/