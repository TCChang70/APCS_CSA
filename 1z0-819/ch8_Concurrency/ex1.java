package ch8_Concurrency;

import java.util.List;

public class ex1<T>{
	
	private List<T> data;
	private boolean foundMatch=false;
	public ex1(List<T> list) {
		this.data=list;	
	}
	public void exists(T v,int start,int end) {//v=5 ,start=0, end=6
		if(end-start==0) {}
		else if(end-start==1) {
			foundMatch=foundMatch || v.equals(data.get(start));
		} else {
			final int middle=start+(end-start)/2;
			
			System.out.println(v+","+middle+","+end);
			new Thread(()->exists(v,start,middle)).run();
			
			System.out.println(v+","+middle+","+end);
			new Thread(()->exists(v,middle,end)).run();
		}
	
	}
	public static void main(String[] args) {
		List<Integer> data=List.of(1,2,3,4,5,6);
		ex1<Integer> t=new ex1<Integer>(data);
		t.exists(5,0,data.size());
		System.out.print(t.foundMatch);	
	}

}
/*
What is the output of the following application?
import java.util.*;

public class SearchList<T> {
	private List<T> data;
	private boolean foundMatch=false;
	public SearchList(List<T> list) {
		this.data=list;	
	}
	public void exists(T v,int start,int end) {
		if(end-start==0) {}
		else if(end-start==1) {
			foundMatch=foundMatch || v.equals(data.get(start));
		} else {
			final int middle=start+(end-start)/2;
			new Thread(()->exists(v,start,middle)).run();
			new Thread(()->exists(v,middle,end)).run();
		}
	
	}
	
	public static void main(String[] a) throws Exception {
		List<Integer> data=List.of(1,2,3,4,5,6);
		SearchList<Integer> t=new SearchList<Integer>(data);
		t.exists(5,0,data.size());
		System.out.print(t.foundMatch);	
	}

}



A. true
B. false
C. The code does not compile
D. The result is unknown until runtime
E. An exception is thrown
F. Noe of the above




ans:A
*/