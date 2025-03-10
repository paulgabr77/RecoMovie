package org.example.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnector {
    private static final String URL = "jdbc:postgresql://localhost:5432/movie_reco";
    private static final String USER = "postgres";
    private static final String PASSWORD = "1q2w3e";

    public static Connection connect() {
        Connection connection = null;
        try {
            connection = DriverManager.getConnection(URL, USER, PASSWORD);
            System.out.println("Conexiunea a fost realizată cu succes!");
        } catch (SQLException e) {
            System.err.println("Eroare la conectare: " + e.getMessage());
        }
        return connection;
    }
}
