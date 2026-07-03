package ch13_Annotations;

public class ex3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
/*
Given the declaration:

@interface Resource {
	String[] value();
}

Examine this code fragment:
/** Loc1**//* class ProcessOrders{...}

Which two annotation may be applied at Loc1 in the code fragment?

A) @Resource()
B) @Resource(value={{}})
C) @Resource
D) @Resource({"Customer1","Customer2"})
E) @Resource("Customer1")


ans:DE
*/