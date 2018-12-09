package com.user.web.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.*;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.user.domain.Memo;
import com.user.domain.User;
import com.user.service.MemoService;
import com.user.service.UserException;
import com.user.service.UserService;

import cn.itcast.utils.CommonUtils;

public class MemoServlet extends HttpServlet {

	/**
		 * The doPost method of the servlet. <br>
		 *
		 * This method is called when a form has its tag value method equals to post.
		 * 
		 * @param request the request send by the client to the server
		 * @param response the response send by the server to the client
		 * @throws ServletException if an error occurred
		 * @throws IOException if an error occurred
		 */
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		
		MemoService memoservice = new MemoService();
//		Memo memo = CommonUtils.toBean(request.getParameterMap(), Memo.class);
//		String method = (String)(request.getAttribute("delete"));
//		if(method == null) {
		String date = (String)(request.getParameter("date"));
		String thing = (String)(request.getParameter("thing"));
		User u = (User)(request.getSession().getAttribute("sessionUser"));
		if(date == null || date.length() == 0 || thing == null || thing.length() == 0 || u == null) {
			response.sendRedirect(request.getContextPath()+"/user/welcome.jsp");
			return;
		}
		Memo memo = new Memo();
		memo.setDate(date);
		memo.setThing(thing);
		
		memo.setUsername(u.getUsername());
		memoservice.addMemo(memo);
		request.getRequestDispatcher("/user/welcome.jsp").forward(request, response);
//			request.getSession().setAttribute("sessionUser", user);
		response.sendRedirect(request.getContextPath()+"/user/welcome.jsp");
//		} else {
//		//	System.out.println("huammmmmmmmm");
//			Memo memo = new Memo();
//			memo.setDate((String)(request.getParameter("date")));
//			memo.setThing((String)(request.getParameter("thing")));
//			
//			memo.setUsername(((User)(request.getSession().getAttribute("sessionUser"))).getUsername());
//			memoservice.deleteMemo(memo);
//			Map<String, Memo> res = (Map<String, Memo>)request.getAttribute("searchRes");
//			res.remove(memo.getDate()+memo.getThing());
//		}
	}

}
