package ch3_java_Object_Oriented_Approach;
interface Builder{
	public A build(String str);
}
class BuilderImpl implements Builder{
	@Override
	public B build(String str){
		return new B(str);
	}
}

abstract class A
{
	
}
class B extends A
{
	B(String x){}
}
public class ex9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
/*
Given:
public interface Builder{
	public A build(String str);
}

and

public class BuilderImpl implements Builder{
	@Override
	public B build(String str){
		return new B(str);
	}
}

Assuming that this code compiles correctly,which three statements are true?

A) A cannot be abstract.
B) A is a subtype of B.
C) B cannot be final.
D) B is a subtype of A. 
E) B cannot be abstract.
F) A cannot be final.





ans:DEF




*/