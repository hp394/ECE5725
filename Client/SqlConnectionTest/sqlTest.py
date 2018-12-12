import MySQLdb
import datetime

db = MySQLdb.connect('47.254.19.144','root','123','usermanagement',charset='utf8')

cursor = db.cursor()

t = datetime.datetime.now()
time_str = str(t)
print time_str.split(' ')[0]


sql = "SELECT * FROM huamiaomiao WHERE submission_date = " +'\''+time_str.split(' ')[0]+'\''
print sql

try:
	cursor.execute(sql)
	res = cursor.fetchall()
	for row in res:
		username = str(row[0])
		password = str(row[1])
		print(username + ' '+ password)	
		
except:
	print 'Error'


db.close()

