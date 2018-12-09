package com.user.web.servlet;

import java.io.IOException;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.user.domain.Memo;
import com.user.domain.User;
import com.user.service.MemoService;

/**
 * Servlet implementation class DeleteServlet
 */
public class DeleteServlet extends HttpServlet {
	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		
		MemoService memoservice = new MemoService();
		
		Memo memo = new Memo();
		memo.setDate((String)(request.getParameter("date")));
		memo.setThing((String)(request.getParameter("thing")));
		
		memo.setUsername(((User)(request.getSession().getAttribute("sessionUser"))).getUsername());
		memoservice.deleteMemo(memo);
//		Map<String, Memo> res = (Map<String, Memo>)request.getAttribute("searchRes");
//		res.remove(memo.getDate()+memo.getThing());
		request.getRequestDispatcher("/user/welcome.jsp").forward(request, response);
//		request.getSession().setAttribute("sessionUser", user);
		response.sendRedirect(request.getContextPath()+"/user/welcome.jsp");
	}

}
