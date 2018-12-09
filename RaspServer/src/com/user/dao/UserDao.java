package com.user.dao;


import java.util.*;
import com.user.domain.Memo;
import com.user.domain.User;

public interface UserDao {
	public User findByUsername(String username);
	public void add(User user);
	public void addMemo(String username, Memo memo);
	public Map<String,Memo> searchMemo(String username, Date from, Date to);
	public void deleteMemo(Memo memo);
}
