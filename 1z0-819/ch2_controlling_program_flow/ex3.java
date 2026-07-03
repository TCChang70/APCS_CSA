package ch2_controlling_program_flow;

public class ex3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i=10;
		do {
			for(int j=i/2;j>0;j--){
				System.out.print(j+" ");
			}
			i-=2;
		}while(i>0);
		
		
	}

}
/*
Given:

int i=10;
do {
	for(int j=i/2;j>0;j--){
		System.out.print(j+" ");
	}
	i-=2;
}while(i>0);

What is the result?

A) 5 4 3 2 1
B) nothing
C) 5
D) 5 4 3 2 1 4 3 2 1 3 2 1 2 1 1


ans:D
*/