package ch3_java_Object_Oriented_Approach;


public class ex16 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

/*
Given:

public interface A{
	public Iterable a();
}

public interface B extends A{
	public Collection a();
}
public interface C extends A{
	public Path a();
}
public interface D extends B,C{

}

why does D cause a compilation error?

A) D does not define any method.
B) D inherits a() only from c.
C) D inherits a() from B and c but the return types are incompatible.
D) D extends more than one interface


ans:C



*/