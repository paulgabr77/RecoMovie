package org.example;

import org.example.database.DatabaseConnector;

import java.sql.DatabaseMetaData;

public class Main {
    public static void main(String[] args) {
        DatabaseConnector.connect();
    }
}