package ch11_Database_Application_with_JDBC;



public class ex1 {

	public static void main(String[] args)   {
		// TODO Auto-generated method stub
		
		

	}

}
/*
What is the most likely outcome of this code if the bunnies table is empty?

var url="jdbc:derby:bunnies";
var sql="insert into bunny(name,color) values(?,?)";
try(var conn=DriverManager.getConnection(url);
var stmt=conn.createStatement()){   // PreparedStatement
	stmt.setString(1,"Hoppy");
	stmt.setString(2,"Brown");
	
	stmt.executeUpdate(sql);
}


A. One row is in the table.
B. Two rows are in the table.
C. The code does not compile.
D. The code throws a SQLException





ans:C


*/