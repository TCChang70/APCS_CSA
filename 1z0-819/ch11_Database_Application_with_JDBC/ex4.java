package ch11_Database_Application_with_JDBC;

import java.sql.*;

public class ex4 {
    public static void main(String[] args) throws SQLException {
        String url = "jdbc:mysql://localhost:3306/classicmodels";
        String sql = "select * from Coffees";
        String user = "root";
        String password = "1234";
        Connection cn = DriverManager.getConnection(url, user, password);
        Statement st = cn.createStatement();
        boolean b = st.execute(sql);
        ResultSet rs = null;
        if (b) {
            rs = st.getResultSet();
        }
        // ResultSet rs = st.executeQuery(sql);
        while (rs.next()) {
            String name = rs.getString("COF_NAME");
            int sid = rs.getInt("SUP_ID");
            double price = rs.getDouble("Price");
            int sales = rs.getInt("SALES");
            int total = rs.getInt("Total");
            System.out.printf("%s %d %.2f %d %d\n ", name, sid, price, sales, total);
        }
        cn.close();
    }
}
