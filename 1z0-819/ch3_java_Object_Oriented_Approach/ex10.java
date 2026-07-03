package ch3_java_Object_Oriented_Approach;


public class ex10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		
	}

}
/*
Given:

public class Foo{
	public void foo(Collection arg){
		System.out.println("Bonjour le monde");	
	}
	
}

and
public class Bar extends Foo{
	public void foo(Collection arg){
		System.out.println("Hello world");	
	}
	public void foo(List arg){
		System.out.println("Hello Mundol!");	
	}


}

and

Foo f1=new Foo();
Foo f2=new Bar();
Bar b1=new Bar();
List<String> li=new ArrayList<>();

Which three are correct?

A) f2.foo(li) prints Bonjour le monde
B) f1.foo(li) prints Hola Mundo!
C) f2.foo(li) prints Hola Mundo!
D) b1.foo(li) prints Hola Mundo!
E) f2.foo(li) prints Hello world!
F) b1.foo(li) prints Hello world!
G) f1.foo(li) prints Bonjour le monde!
H) f1.foo(li) prints Hello world!
I) b1.foo(li) prints Bonjour le monde!


ans:DEG
*/