<%@page import="com.user.domain.Memo"%>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'welcome.jsp' starting page</title>
    
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
    <h1>Welcome</h1>
    <c:choose>
    	<c:when test="${empty sessionScope.sessionUser }"><jsp:forward page="login.jsp"></jsp:forward></c:when>
    	<c:otherwise>welcome ${sessionScope.sessionUser.username }</c:otherwise>
    </c:choose>
    <form action="${pageContext.request.contextPath }/MemoServlet" method="post">
    	Date：<input type="date" name="date" value="${memo.date }"/><br>
    	thing：<input type="text" name="thing" value="${memo.thing }"/><br>
    	<input type="submit" value="insert"/> 
    </form>
    
    <form action="${pageContext.request.contextPath }/SearchServlet" method="post">
    	Search Memo from：<input type="date" name="fromDate" value=""/>
    	 to：<input type="date" name="toDate" value=""/><br>
    	<input type="submit" value="search"/> 
    </form>
    <%
    	Map<String, Memo> res = (Map<String, Memo>)(request.getAttribute("searchRes"));
    	if(res != null){
    		for(String key:res.keySet()){
    			Memo memo = res.get(key);
    			Date d = memo.getDate();
    			String thing = memo.getThing();
    			//System.out.println(date);
    			int year = d.getYear()+1900;
    			int month = d.getMonth() + 1;
    			int date = d.getDate();
    			String day = date >= 10 ? String.valueOf(date) : "0"+date;
    			String mon = month >= 10 ? String.valueOf(month) : "0"+month;
    			String dat = year+"-"+mon+"-"+day;
    			request.setAttribute("temp_date", dat);
    			request.setAttribute("temp_thing", thing);
    			
    %>
    <form action="${pageContext.request.contextPath }/DeleteServlet" method="post">
    	Date：<input type="date" name="date" value="${temp_date }"/><br>
    	thing：<input type="text" name="thing" value="${temp_thing}"/><br>
    	<input type="submit" name="delete" value="delete"/> 
    </form>
    <%
    		}
    	}
    %>
  </body>
</html>
