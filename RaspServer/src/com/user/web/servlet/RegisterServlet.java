package com.user.web.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.*;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.user.domain.User;
import com.user.service.UserException;
import com.user.service.UserService;

import cn.itcast.utils.CommonUtils;

public class RegisterServlet extends HttpServlet {

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
		
		Map<String, String> errors = new HashMap<String,String>();
		String username = form.getUsername();
		if(username == null||username.trim().isEmpty()){
			errors.put("username","Empty username");
		}else if(username.length()<3||username.length()>15) {
			errors.put("username", "Username must be in length of 3-15");
		}
		
		
		String password = form.getPassword();
		if(password == null||password.trim().isEmpty()){
			errors.put("password","Empty password");
		}else if(password.length()<3||password.length()>15) {
			errors.put("password", "Username must be in length of 3-15");
		}
		
		
		String verifyCode = form.getVerifyCode();
		String session_vcode = (String)request.getSession().getAttribute("session_vcode");
		if(verifyCode == null||verifyCode.trim().isEmpty()){
			errors.put("verifyCode","Empty VerifyCode");
		}else if(verifyCode.length()!=4) {
			errors.put("verifyCode", "VerifyCode must be 4 digits");
		}else if(!session_vcode.equalsIgnoreCase(form.getVerifyCode())){
			errors.put("verifyCode", "Invalid VerifyCode");
		}
		
		if(errors != null && errors.size()>0){
			request.setAttribute("errors", errors);
			request.setAttribute("user", form);
			request.getRequestDispatcher("/user/register.jsp").forward(request, response);
			return;
		}
		
		
		try {
			userservice.register(form);
			response.getWriter().print("<h1>successfully signed up！</h1><a href='"
					+request.getContextPath()+
					"/user/login.jsp"+"'>Login Here</a>");
		} catch (UserException e) {
			// TODO Auto-generated catch block
			request.setAttribute("msg", e.getMessage());
			request.setAttribute("user", form);
			request.getRequestDispatcher("/user/register.jsp").forward(request, response);
		}

	}

}
