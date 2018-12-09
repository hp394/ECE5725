<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'register.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->
<script type="text/javascript">
	function _change() {
		var ele = document.getElementById("vCode");
		ele.src = "${pageContext.request.contextPath }/VerifyCodeServlet?xxx="+new Date().getTime();
	}
</script>
  </head>
  
  <body>
    <<h1>register</h1>
    <p style="color: red; font-weight: 900">${msg }</p>
    <form action="${pageContext.request.contextPath }/RegisterServlet" method="post">
    	username:<input type="text" name="username" value="${user.username }"/>${errors.username }<br>
    	password:<input type="password" name="password" value="${user.password }"/>${errors.password }<br>
    	verifycode:<input type="text" name="verifyCode" value="${user.verifyCode }" size="3"/>
    		  <img id="vCode" src="${pageContext.request.contextPath }/VerifyCodeServlet" border="2"/>
    		  <a href="javascript:_change()">change</a>${errors.verifyCode }<br>
    	 <input type="submit" value="register"/> 
    </form>
  </body>
</html>
