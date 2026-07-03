package ch13_Annotations;

@Deprecated(since = "5.0")
class ProjectPlanner<T> {
	ProjectPlanner create(T t) {
		return this;
	}
}

// @SuppressWarnings({ "deprecation", "unchecked" })
class SystemPlanner {
	ProjectPlanner<String> planner = new ProjectPlanner<String>().create("TPS");
}

public class ex2 {

	public static void main(String[] args) {

		SystemPlanner sp = new SystemPlanner();
		ProjectPlanner<String> ps = sp.planner;
	}

}
/*
 * Fill in the blank with the correct annotation usage that allows the code to
 * compile without
 * any warnings.
 * 
 * @Deprecated(since="5.0")
 * public class ProjectPlanner<T>{
 * ProjectPlanner create(T t) { return this; }
 * }
 * 
 * @SuppressWarnings(________)
 * class SystemPlanner {
 * ProjectPlanner planner=new ProjectPlanner().create("TPS");
 * }
 * 
 * 
 * A. value=ignoreAll
 * B. value="deprecation","unchecked"
 * C. "unchecked","deprecation"
 * D. {"deprecation","unchecked"}
 * E. "deprecation"
 * F. None of the above
 * 
 * 
 * 
 * 
 * ans:D
 * 
 * 
 * 
 */