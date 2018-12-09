package com.user.service;

import com.user.dao.DaoFactory;
import com.user.dao.UserDao;
import com.user.domain.Memo;
import java.util.*;

public class MemoService {
	private UserDao userdao = DaoFactory.getUserDao();
	
	public void addMemo(Memo memo){
		String username = memo.getUsername();
		userdao.addMemo(username,memo);
	}
	
	public Map<String, Memo> searchMemo(String username,String from, String to){
		if(from == null || from.equals("") || to == null || to.equals(""))
			return new HashMap<String, Memo>();
		String[] froms = from.split("-");
		String[] tos = to.split("-");
		int from_year = Integer.valueOf(froms[0]);
		int from_month = Integer.valueOf(froms[1]);
		int from_day = Integer.valueOf(froms[2]);
		Date from_date = new Date(from_year - 1900, from_month - 1, from_day);
		
		int to_year = Integer.valueOf(tos[0]);
		int to_month = Integer.valueOf(tos[1]);
		int to_day = Integer.valueOf(tos[2]);
		Date to_date = new Date(to_year - 1900, to_month - 1, to_day);
		return userdao.searchMemo(username, from_date, to_date);
	}
	
	public void deleteMemo(Memo memo){
		userdao.deleteMemo(memo);
	}
}
