<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'login.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

  </head>
  
  <body>
  <h1>login</h1>
    <p style="color: red; font-weight: 900">${msg }</p>
    <form action="${pageContext.request.contextPath }/LoginServlet" method="post">
    	username：<input type="text" name="username" value="${user.username }"/><br>
    	password：<input type="password" name="password" value="${user.password }"/><br>
    	<input type="submit" value="login"/> 
    </form>
    <a href=${pageContext.request.contextPath }/user/register.jsp>register</a><br>
  </body>
</html>
