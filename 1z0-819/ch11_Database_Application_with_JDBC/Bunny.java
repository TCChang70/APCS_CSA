package ch11_Database_Application_with_JDBC;

import java.sql.*;

public class Bunny {
    public static void main(String[] args) throws SQLException {
        String url = "jdbc:mysql://localhost:3306/classicmodels";
        String sql = "insert into Bunnies(name,color)values(?,?)";
        String user = "root";
        String password = "1234";
        Connection cn = DriverManager.getConnection(url, user, password);
        PreparedStatement st = cn.prepareStatement(sql);
        st.setString(1, "Ted");
        st.setString(2, "Yellow");
        // st.executeUpdate();
        boolean b = st.execute();
        System.out.println(b);
        cn.close();
        System.out.println("Successful");
    }
}
