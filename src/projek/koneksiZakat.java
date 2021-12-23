/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

package projek;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;


/**
 *
 * @author nanchaara
 */
public class koneksiZakat {
    private static Connection MySQLConfig;
    public static Connection configDB() throws SQLException{
        try {
            String url = "jdbc:mysql://localhost:3306/pv_zakat";
            String user = "root";
            String pass = "";
            
            DriverManager.registerDriver(new com.mysql.jdbc.Driver());
            MySQLConfig = DriverManager.getConnection(url, user, pass);
            
        } catch (SQLException e) {
            System.out.println ("KONEKSI KE DATABASE GAGAL " + e.getMessage ());
        }
        return MySQLConfig;
    }
    
    static Statement createStatement () {
        throw new UnsupportedOperationException ("Not supported yet.");
    }
}
