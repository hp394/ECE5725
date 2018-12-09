package com.user.dao;

import java.io.InputStream;
import java.util.Properties;

public class DaoFactory {
	private static Properties props = null;
	static {
		try {
			InputStream in = DaoFactory.class.getClassLoader().getResourceAsStream("dao.properties");
			props = new Properties();
			props.load(in);
		} catch (Exception e) {
			// TODO: handle exception
			throw new RuntimeException(e);
		}
	}
	public static UserDao getUserDao(){
		
		String daoClassName = props.getProperty("com.user.dao.UserDao");
		try {
			Class c = Class.forName(daoClassName);
			
			return (UserDao)c.newInstance();
		} catch (Exception e) {
			throw new RuntimeException(e);
		} 
	}
}
