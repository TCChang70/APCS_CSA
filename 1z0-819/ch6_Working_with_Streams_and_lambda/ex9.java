package ch6_Working_with_Streams_and_lambda;


public class ex9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		

	}

}
/*
Given:

public class Employee {
	private String name;
	private String neighborhood;
	private int salary;
	//Constructors and setter and getter methods go here
}

and the code fragment:

List<Employee> roster=new ArrayList<>();
Predicate<Employee> p=e->e.getSalary()>30;
Function<Employee,Optional<String>> f=
      e->Optional.ofNullable(e.getNeighborhood());

Which two objects group all employees with a salary greater than 30 by neighborhood?

A) Map<Optional<String>,List<Employee>> r4=roster.stream()
       .collect(Collectors.groupingBy(f,Collectors.filtering(p,Collectors.toList())));
       
B) Map<Optional<String>,List<Employee>> r2=roster.stream().filter(p)
       .collect(Collectors.groupingBy(f,Employee::getNeighborhood));

C) Map<Optional<String>,List<Employee>> r5=roster.stream()
		    	       .collect(Collectors.groupingBy(Employee::getNeighborhood,
		    	               Collectors.filtering(p,Collectors.toList())));

D) Map<Optional<String>,List<Employee>> r3=roster.stream().filter(p)
       .collect(Collectors.groupingBy(p));
       
E) Map<String,List<Employee>> r1=roster.stream()
       .collect(Collectors.groupingBy(Employee::getNeighborhood,
               Collectors.filtering(p,Collectors.toList())));




ans:AE
*/