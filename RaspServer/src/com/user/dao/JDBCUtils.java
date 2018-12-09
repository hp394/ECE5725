package com.user.dao;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Properties;
/*
 * @Author:huamiaomiao
 * 1.0
 */
public class JDBCUtils {
	private static Properties prop = null;
	static{
		try {
			InputStream is = JDBCUtils.class.getClassLoader().getResourceAsStream("dbConfig.properties");
			prop = new Properties();
			prop.load(is);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			throw new RuntimeException(e);
		}
		try {
			Class.forName(prop.getProperty("DriverClassName"));
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			
			throw new RuntimeException(e);
		}
	}
	public static Connection getConnection() throws Exception {	
		return DriverManager.getConnection(prop.getProperty("url"), prop.getProperty("username"),prop.getProperty("password"));
		
	}
}
