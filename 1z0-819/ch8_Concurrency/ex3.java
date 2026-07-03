package ch8_Concurrency;



import java.util.concurrent.CopyOnWriteArrayList;

public class ex3 {

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub
		
		
	}

}
/*
Given:

var c=new CopyOnWriteArrayList<>(List.of("1","2","3","4"));
Runnable r=()->{
	try{
		Thread.sleep(150);
	}
	catch(InterruptedException e){
		System.out.println(e);	
	}
	c.set(3,"four");
	System.out.print(c+" ");
	};
Thread t=new Thread(r);
t.start();
for(var s:c)
{
	System.out.print(s+" ");
	Thread.sleep(100);
}


What is the output?

A) 1 2 [1, 2, 3, four] 3 4

B) 1 2 [1, 2, 3, 4] 3 four

C) 1 2 [1, 2, 3, 4] 3 4

D) 1 2 [1, 2, 3, four] 3 four





ans:A
*/