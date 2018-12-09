package com.user.web.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.user.domain.User;
import com.user.service.UserException;
import com.user.service.UserService;

import cn.itcast.utils.CommonUtils;

public class LoginServlet extends HttpServlet {
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
		
		UserService userservice = new UserService();
		User form = CommonUtils.toBean(request.getParameterMap(), User.class);
		
		try {
			User user =userservice.login(form);
			request.getSession().setAttribute("sessionUser", user);
			response.sendRedirect(request.getContextPath()+"/user/welcome.jsp");
		} catch (UserException e) {
			// TODO Auto-generated catch block
			request.setAttribute("msg", e.getMessage());
			request.setAttribute("user", form);
			request.getRequestDispatcher("/user/login.jsp").forward(request, response);
		}
	}

}
