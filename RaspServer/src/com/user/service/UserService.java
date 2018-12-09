package com.user.service;

import com.user.dao.DaoFactory;
import com.user.dao.UserDao;
import com.user.domain.User;

public class UserService {
	private UserDao userdao = DaoFactory.getUserDao(); 
	
	public void register(User user) throws UserException {
		
		String s = userdao.getClass().getName();
		//System.out.print(s);
		User _user = userdao.findByUsername(user.getUsername());
		if(_user != null) throw new UserException("username"+user.getUsername()+"has been registered");
		
		userdao.add(user);
	}

	public User login(User form) throws UserException {

		User user = userdao.findByUsername(form.getUsername());
		if(user == null)
			throw new UserException("user dose not exist");
		if(!form.getPassword().equals(user.getPassword()))
			throw new UserException("wrong password");
		return user;

	}
}
