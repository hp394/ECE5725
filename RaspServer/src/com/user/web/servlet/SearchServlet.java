package com.user.web.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.*;

import com.user.domain.Memo;
import com.user.domain.User;
import com.user.service.MemoService;

public class SearchServlet extends HttpServlet {

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
		User u = (User)(request.getSession().getAttribute("sessionUser"));
		if( u == null){
			request.getRequestDispatcher("/user/welcome.jsp").forward(request, response);
			return;
		}
		String username = u.getUsername();
		String from = request.getParameter("fromDate");
		String to = request.getParameter("toDate");
		Map<String,Memo> res = memoservice.searchMemo(username, from, to);
		request.setAttribute("searchRes", res);
		request.getRequestDispatcher("/user/welcome.jsp").forward(request, response);
		
	}

}
