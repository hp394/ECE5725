package com.user.domain;

import java.util.Date;

public class Memo {
	private String username;
	private Date date;
	private String thing;
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public Date getDate() {
		return date;
	}
	public void setDate(String date) {
		//System.out.println("huamiaomiaomzuikeaile:"+date);
		String[] d = date.split("-");
		int year = Integer.valueOf(d[0]);
		int month = Integer.valueOf(d[1]);
		int day = Integer.valueOf(d[2]);
		this.date = new Date(year - 1900, month - 1, day);
		//this.date = new Date()
	}
	public void setDate(long date) {

		this.date = new Date(date);
	}
	
	public String getThing() {
		return thing;
	}
	public void setThing(String thing) {
		this.thing = thing;
	}
	
}
