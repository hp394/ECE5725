#coding:utf-8   #强制使用utf-8编码格式
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
class sendEmail():
	def __init__(self,user):
		self.user = user
		#my_sender='pgxapply1@sina.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
		#my_user='mf734@cornell.edu' #收件人邮箱账号，为了后面易于维护，所以写成了变量
	def mail(self,temp,temp_ref_min,temp_ref_max,hum,hum_ref_min,hum_ref_max,pir):
		ret=True
		try:
			det = 'not '
			if pir == True:
				det = ''
			
			content = 'Dear Customer,\n  According to data from sensors: the current room temperature is '+str(temp)+' Celsius compared to our preset reference '+str(temp_ref_min)+'-'+str(temp_ref_max)+' Celsius. The room humidity is '+str(hum) +'% compared to our preset reference '+str(hum_ref_min)+'-'+str(hum_ref_max)+'%. We have '+det+'detected unusual motion in your house.\n  We highly suggest you check any potential hazards in your house such as: water outlets, gas, air conditions, windows, doors, etc. If necessary, please contact emergency services as soon as possible.\n  We are trying our best to make sure your house is safe, and we will keep monitoring your house!\n\nYours,\nLand Guardian'
			#print content
			
			msg=MIMEText(content,'plain','utf-8')
			msg['From']=formataddr(["Land Guardian",'pgxapply1@sina.com'])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
			msg['To']=formataddr(["AWater",self.user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
			msg['Subject']="Warning!! Unusual Situation Reported!! " #邮件的主题，也可以说是标题

			server=smtplib.SMTP("smtp.sina.com",25)  #发件人邮箱中的SMTP服务器，端口是25
			server.login('pgxapply1@sina.com',"941218")    #括号中对应的是发件人邮箱账号、邮箱密码
			server.sendmail('pgxapply1@sina.com',[self.user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
			server.quit()   #这句是关闭连接的意思
			
		except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
			ret=False
		return ret
	'''
	ret=mail()
	if ret:
		print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
	else:
		print("failed")  #如果发送失败则会返回failed
	'''
