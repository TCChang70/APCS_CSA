package ch3_java_Object_Oriented_Approach;

public class ex3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		

	}

}
/*
Given:

public class GameObject{
	public Object[] move(int x,int y){
		System.out.println("Move GameObject");
		return new Integer[]{x+10,y+10};
	}	
}

and

public class Avatar extends GameObject{
	public Object[] move(Number x,Number y){
		System.out.println("Move Character");
		return super.move(x.intValue(),y.intValue());
	}
	
	public static void main(String... args)
	{
		var character=new Avatar();
		character.move(10.0,10.0);//Move Character,Move GameObject
		character.move(10,10);	//Move GameObject
	}
}


What is the result?

A) Move Character
   Move GameObject
   Move GameObject
   
B) Move GameObject
   Move GameObject
   
C) Move GameObject
   Move Character
   Move GameObject
   
D) Move GameObject




ans:A

*/