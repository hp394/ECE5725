package com.user.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.*;

import com.user.domain.Memo;
import com.user.domain.User;

public class JdbcUserDaoImpl implements UserDao {

	public User findByUsername(String username) {
		//System.out.println("hello");
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		try {
			con = JDBCUtils.getConnection();
			
			String sql = "SELECT * FROM user WHERE username=?";
			ps = con.prepareStatement(sql);
			
			ps.setString(1, username);
			
			rs = ps.executeQuery();
			
			if(rs == null ){
				return null;
			}if(rs.next()) {
				User user = new User();
				user.setUsername(rs.getString("username"));
				user.setPassword(rs.getString("password"));
				
				return user;
			}else
				return null;
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {			
				try {
					if(ps !=null) ps.close();
					if(con != null) con.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}			
		}
		return null;
	}

	public void add(User user) {
	//	System.out.println("hello");
		Connection con = null;
		PreparedStatement ps = null;
		try {
			con = JDBCUtils.getConnection();
			
			String sql = "INSERT INTO user VALUES(?,?)";
			ps = con.prepareStatement(sql);
			
			ps.setString(1, user.getUsername());
			ps.setString(2, user.getPassword());
			
			ps.executeUpdate();
			
			String sql1 = "CREATE TABLE "+user.getUsername()+" (submission_date DATE, thing VARCHAR(255) NOT NULL )";
			ps = con.prepareStatement(sql1);
			
			ps.executeUpdate();
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {
			
				try {
					if(ps !=null) ps.close();
					if(con != null) con.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			
		}
	}

	@Override
	public void addMemo(String username, Memo memo) {
	//	System.out.println("hello");
		Connection con = null;
		PreparedStatement ps = null;
		try {
			con = JDBCUtils.getConnection();
			
			String sql = "INSERT INTO "+username+" VALUES(?,?)";
			ps = con.prepareStatement(sql);
			
			//ps.setString(1, username);
			ps.setDate(1, new java.sql.Date(memo.getDate().getTime()));
			ps.setString(2, memo.getThing());
			
			ps.executeUpdate();
			
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {
			
				try {
					if(ps !=null) ps.close();
					if(con != null) con.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			
		}
	}

	@Override
	public Map<String, Memo> searchMemo(String username, Date from, Date to) {
		
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		try {
			con = JDBCUtils.getConnection();
			
			String sql = "SELECT * FROM "+username+" WHERE submission_date >= ? AND submission_date <= ?";
			ps = con.prepareStatement(sql);
			
			ps.setDate(1, new java.sql.Date(from.getTime()));
			ps.setDate(2, new java.sql.Date(to.getTime()));
			
			rs = ps.executeQuery();
			Map<String, Memo> res = new HashMap<String, Memo>();
			if(rs == null ){
				return res;
			}
			
			while(rs.next()) {
				
				Memo m = new Memo();
				m.setUsername(username);
				m.setDate(rs.getString("submission_date"));
				m.setThing(rs.getString("thing"));
				res.put(rs.getString("submission_date")+rs.getString("thing"),m);
//				User user = new User();
//				user.setUsername(rs.getString("username"));
//				user.setPassword(rs.getString("password"));
				
			//	return user;
			}
			return res;
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {			
				try {
					if(ps !=null) ps.close();
					if(con != null) con.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}			
		}
		return null;
	}

	@Override
	public void deleteMemo(Memo memo) {
		// TODO Auto-generated method stub
		Connection con = null;
		PreparedStatement ps = null;
		try {
			con = JDBCUtils.getConnection();
			
			String sql = "DELETE FROM "+memo.getUsername()+" WHERE submission_date = ? AND thing = ?";
			ps = con.prepareStatement(sql);
			
			//ps.setString(1, username);
			ps.setDate(1, new java.sql.Date(memo.getDate().getTime()));
			ps.setString(2, memo.getThing());
			
			ps.executeUpdate();
			
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {
			
				try {
					if(ps !=null) ps.close();
					if(con != null) con.close();
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			
		}
	}

}
