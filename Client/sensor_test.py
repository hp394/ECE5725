import temp_detect
import pir
import sendemail
import config
import time
import threading
import RPi.GPIO as GPIO
def init_sys():
	#declare the sensor, mail system and reference value
	global ths
	global p
	global se
	global sendflag
	global temp_max_ref
	global temp_min_ref
	global humid_max_ref
	global humid_min_ref
	#initialize the detect value
	global pir_detect
	pir_detect = False
	global temp
	temp = -300
	global humid
	humid = -1
	#initialize the whole system, including the sensor, mail system and reference value	
	ths = temp_detect.temp_hum_sensor(13)
	p = pir.pir(19)
	se = sendemail.sendEmail('mf734@cornell.edu')
	temp_max_ref = config.max_temp
	temp_min_ref = config.min_temp
	humid_max_ref = config.max_humid
	humid_min_ref = config.min_humid
	print(str(humid_min_ref))
	sendflag = False

	
def delay(self,sleeptime):
	count = 0
	while count != sleeptime and self.count_flag:
   # print(str(count))
		time.sleep(1)
        count += 1


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def GPIO17_callback(channel):
    global switch
    global count_flag
    switch = False;
    count_flag = False
    #GPIO.cleanup();
    
GPIO.add_event_detect(17,GPIO.FALLING,callback=GPIO17_callback,bouncetime=300)    

init_sys()
#pir_thread = threading.Thread(target=pir_work, args=())
#temp_hum_thread = threading.Thread(target=temp_hum_work, args=())
#pir_thread.start()
#temp_hum_thread.start()
time.sleep(2)
temp_count = 0


humid_count = 0

pir_count = 0
count = 0
THData = [-300,-1]
global pir_detect
global sendflag
global ths
global p
global se
global temp
global humid 
global temp_max_ref
global temp_min_ref
global humid_max_ref
global humid_min_ref
global switch
global count_flag
global count_end;

count_flag = True
#count_end = False
switch = True
pir_flag = False
temp_flag = False
humid_flag = False


	
while switch:
	if ( count%2 == 0 ):
		THData = ths.collect()
		count = 0
		temp = THData[0]
		humid = THData[1]
		if ( temp >= temp_max_ref or temp <= temp_min_ref ) and temp_count < 2:
			temp_count += 1
		elif ( temp >= temp_max_ref or temp <= temp_min_ref ) and temp_count >= 2 and not temp_flag:
			temp_flag = True
		else:
			temp_count = 0	
			
		if ( humid >= humid_max_ref or humid <= humid_min_ref ) and humid_count < 2:
			humid_count += 1
		elif ( humid >= humid_max_ref or humid <= humid_min_ref ) and humid_count >= 2 and not humid_flag:
			humid_flag = True
		else:
			humid_count = 0	
	pir_detect = p.detect()
	if pir_detect and pir_count < 2 :
		print("detected")
		pir_count += 1
	elif pir_detect and pir_count >= 2 and not pir_flag:
		print("detected")
		pir_flag = True
	else:
		print("not detected")
		pir_count = 0
	time.sleep(1.5)
	count += 1

	sendflag = pir_flag or temp_flag or humid_flag
	print("pir:"+str(pir_flag))
	print("temp:"+str(temp_flag))
	print("humid:"+str(humid_flag))
	print("send:"+str(sendflag))
	if(sendflag):	
		#print("hello,huamiaomiao")	
		ret = se.mail(temp,temp_min_ref,temp_max_ref,humid,humid_min_ref,humid_max_ref,pir_detect)
		if(ret):
			print "OK"
		else:
			print "FAIL"
		delay(300)
		sendflag = False
		humid_count = 0
		humid_flag = False
		temp_count = 0
		temp_flag = False
		pir_count = 0
		pir_flag = False
			
	'''
	while True:
		data = ths.collect();
		if p.detect():
			print("detected")
		else :
			print("not detected")
		time.sleep(3)
        '''
#except Exception:
#	GPIO.cleanup()
#se.mail(21,4,31,60,True);
