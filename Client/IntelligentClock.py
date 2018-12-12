import pygame
import Color
import getTime
import subprocess
import GetWeather
import RPi.GPIO as GPIO
import time
import config
import MySQLdb
import UserInfo
import datetime
import WeatherMemoMenu
import weatherReport
import Memo
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def GPIO17_callback(channel): 
    global clockflag
    cmd = 'echo "q"> /home/pi/final_project/mplayerfifo'
    subprocess.check_output(cmd, shell=True)
    
GPIO.add_event_detect(17,GPIO.FALLING,callback=GPIO17_callback,bouncetime=300) 

def Timer():
    global timer_count
    global clockflag
    
    while timer_count >= 0:
       # print(str(count))
        time.sleep(1)
        timer_count -= 1
        
    clockflag = True
     
def drawWeather(report,screen):
	res = report['forecast']
	
	for i in range(0,3):
	    weather = res[i]['text']
            ht = res[i]['high']
            lt = res[i]['low']
            date = res[i]['date']
            info = date+'   '+weather+'  '+str(ht)+'  '+str(lt)
            my_font = pygame.font.Font(None, 20)
            text_surface = my_font.render(info, True, Color.white)
            pos = [160,60*(i+1)]
            rect = text_surface.get_rect(center=pos)
            screen.blit(text_surface, rect)
     
     
class clock():
    def __init__(self):
        self.text = 'At Home'
        self.pos = [160, 60]
        self.exit = False
        self.alarm = False
      #  self.weatherMemo = None

    def isExit(self, pos):
        x, y =pos
        return x > 260 and x < 320 and y > 180 and y < 240

    def range(self, pos):
        ref_x, ref_y = self.pos
        x, y = pos
        if x > ref_x - 30 and x < ref_x + 30:
            if y > ref_y - 20 and y < ref_y + 20:
                return True
        return False
        

    def display(self, screen):
	global timer_count
	global clockflag
	clockflag = True
        while not self.exit:
			screen.fill(Color.black)
			for event in pygame.event.get():
                                    if event.type is pygame.MOUSEBUTTONDOWN:
                                          pos = pygame.mouse.get_pos()
                                    elif event.type is pygame.MOUSEBUTTONUP:
                                          pos = pygame.mouse.get_pos()
                                          if self.isExit(pos):
                                            self.exit = True
                                            timer_count = -10
                                            clockflag = False
			hour = getTime.getHour()
			minute = getTime.getMin()
			center_pos = [160, 120]
			my_font = pygame.font.Font(None, 40)
			text_surface = my_font.render(hour+':'+minute, True, Color.white)
			rect = text_surface.get_rect(center=center_pos)
			screen.blit(text_surface, rect)	
			my_font_ok = pygame.font.Font(None, 20)
			text_surface_ok = my_font_ok.render('Back', True, Color.white)
			pos_ok = [280,200]
			rect = text_surface_ok.get_rect(center=pos_ok)
			screen.blit(text_surface_ok, rect)
			pygame.display.flip()
			
			if hour == config.hour and minute == config.minute:
					if clockflag:
						timer_count = 60
						timer_thread = threading.Thread(target=Timer, args=())
						timer_thread.start()
						cmd = 'mplayer -vo sdl -framedrop -input file=/home/pi/final_project/mplayerfifo /home/pi/final_project/clock.mp3 &'
						subprocess.check_output(cmd, shell=True)
						self.alarm = True
						clockflag = False
					
					
							
			
        
			if( self.alarm == True ):
				report = GetWeather.getWeatherReport()
				#screen.fill(Color.black)
				#drawWeather(report, screen)
				#pygame.display.flip()
				GetWeather.outputAdvice()  
				#time.sleep(10)
				t = datetime.datetime.now()
				time_str = str(t).split(' ')[0]
				db = MySQLdb.connect('47.254.19.144','root','123','usermanagement',charset='utf8')

				cursor = db.cursor()

				#sql = 'SELECT thing FROM '+UserInfo.username+' WHERE submission_date = '+time_str
				sql = "SELECT thing FROM "+UserInfo.username+" WHERE submission_date = " +'\''+time_str.split(' ')[0]+'\''
				try:
					cursor.execute(sql)						
				except:
					print 'Error'
				
				count = 0
				res = cursor.fetchall()
				for row in res:
					#date = str(row[0])
					thing = str(row[0])
					count += 1
					print(thing)	
				db.close()
				sentence = "In addition,"
				if( count ==0 ):
					sentence += "There is no events today"
				else:
					sentence += "there are "+str(count)+" task you need to deal with today"
					
				GetWeather.speak(sentence)
				
				transition = "next you can check the weather and memo information in the following menu"
				GetWeather.speak(transition)
				weatherReport_m = weatherReport.menu(report)
				Memo_m = Memo.menu(res,count)
				weatherMemo = WeatherMemoMenu.menu(weatherReport_m,Memo_m)
				weatherMemo.display(screen)
				self.alarm = False
				#clockflag = True
				
			

        self.exit = False
