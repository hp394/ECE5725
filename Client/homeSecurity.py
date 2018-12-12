import pygame
import temp_detect
import pir
import sendemail
import getTime
import config
import Color
import threading
import time

global hs_exit
global count_flag

hs_exit = False
count_flag = True

def isExit(pos):
        x, y =pos
        return x > 210 and x < 320 and y > 170 and y < 240
        
        
def click():
	global hs_exit
	global count_flag
	for event in pygame.event.get():
			if event.type is pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
			elif event.type is pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if isExit(pos):
					hs_exit = True
					count_flag = False
				

def delay(sleeptime):
	global count_flag
	count = 0
	while count != sleeptime and count_flag:
		click()
		time.sleep(1)
		count += 1
		
	count_flag = True
		

class homeSecurity():
    def __init__(self):
	global hs_exit
        self.text = 'Home Security'
        self.pos = [160, 120]
        self.exit = hs_exit;
        
        
        self.temp_flag = config.TempFlag
        self.hum_flag = config.HumFlag
        self.mot_flag = config.MotFlag
        self.run_flag = config.TempFlag or config.HumFlag or config.MotFlag
        
        self.max_temp = config.max_temp
        self.min_temp = config.min_temp
        self.max_humid = config.max_humid
        self.min_humid = config.min_humid
        
        self.ths = temp_detect.temp_hum_sensor(13)
	self.p = pir.pir(19)
    	self.se = sendemail.sendEmail('mf734@cornell.edu')
        

        
    def range(self, pos):
        ref_x, ref_y = self.pos
        x, y = pos
        if x > ref_x - 30 and x < ref_x + 30:
            if y > ref_y - 20 and y < ref_y + 20:
                return True
        return False    
        
    '''def isExit(self,pos):
        x, y =pos
        return x > 260 and x < 320 and y > 200 and y < 240
    '''    	
	
    def display(self, screen):
	global hs_exit
    	global countFlag
    	screen.fill(Color.black)
    	my_font_ok = pygame.font.Font(None, 20)
        text_surface_ok = my_font_ok.render('Back', True, Color.white)
        pos_ok = [280,200]
        rect = text_surface_ok.get_rect(center=pos_ok)
        screen.blit(text_surface_ok, rect)			
        pygame.display.flip()
	    
        count = 0
        temp_count = 0
    	humid_count = 0
    	pir_count = 0		
        	
    	pir_err_flag = False
    	temp_err_flag = False
    	humid_err_flag = False
	
	self.temp_flag = config.TempFlag
        self.hum_flag = config.HumFlag
        self.mot_flag = config.MotFlag
        self.run_flag = config.TempFlag or config.HumFlag or config.MotFlag
    	time.sleep(2)
        
        while not hs_exit:
	    click()
	    if self.run_flag:
		    temp = 23
		    humid = 35
		    if ( count%2 == 0 ) and (self.temp_flag or self.hum_flag):
				THData = self.ths.collect()
				click()
				screen.fill(Color.black)
			        my_font_ok = pygame.font.Font(None, 20)
			        text_surface_ok = my_font_ok.render('Back', True, Color.white)
			        pos_ok = [280,200]
			        rect_back = text_surface_ok.get_rect(center=pos_ok)
			        screen.blit(text_surface_ok, rect_back)	
				count = 0
				temp = THData[0]
				humid = THData[1]
				text_surface_temp = my_font_ok.render('Temperature:'+str(temp)+'*C', True, Color.white)
				pos_temp = [160,60]
				rect_temp = text_surface_temp.get_rect(center=pos_temp)
				screen.blit(text_surface_temp, rect_temp)
				
				text_surface_humid = my_font_ok.render('Humid:'+str(humid)+'%', True, Color.white)
				pos_humid = [160,120]
				rect_humid = text_surface_humid.get_rect(center=pos_humid)
				screen.blit(text_surface_humid, rect_humid)
				
				if self.temp_flag:
						if ( temp >= self.max_temp or temp <= self.min_temp ) and temp_count < 2:
							temp_count += 1
						elif ( temp >= self.max_temp or temp <= self.min_temp ) and temp_count >= 2 and not temp_err_flag:
							temp_err_flag = True
						else:
							temp_count = 0	
				if self.hum_flag:
						if ( humid >= self.max_humid or humid <= self.min_humid ) and humid_count < 2:
							humid_count += 1
						elif ( humid >= self.max_humid or humid <= self.min_humid ) and humid_count >= 2 and not humid_err_flag:
							humid_err_flag = True
						else:
							humid_count = 0	
		    click()
		    pygame.display.flip()
		    if self.mot_flag:		
					pir_detect = self.p.detect()
					if pir_detect and not pir_err_flag:
						pir_err_flag = True
						print("detected")
						
					'''
					if pir_detect and pir_count < 2 :
						print("detected")
						pir_count += 1
					elif pir_detect and pir_count >= 2 and not pir_err_flag:
						print("detected")
						pir_err_flag = True
					else:
						print("not detected")
						pir_count = 0
					'''

		    click()
		    count += 1
		    
		    sendflag = pir_err_flag or temp_err_flag or humid_err_flag
		    print("pir:"+str(pir_err_flag))
		    print("temp:"+str(temp_err_flag))
		    print("humid:"+str(humid_err_flag))	    
		    print("send:"+str(sendflag))
		    
		    click()
		    if(sendflag):	
					ret = self.se.mail(temp,self.min_temp,self.max_temp,humid,self.min_humid,self.max_humid,pir_err_flag)
					if(ret):
						print("OK")
					else:
						print("FAIL")
						
					delay(300)
					sendflag = False
					humid_count = 0
					humid_flag = False
					temp_count = 0
					temp_flag = False
					pir_count = 0
					pir_flag = False
					
	         
            
                        
            

	hs_exit = False
    	countFlag = True
        self.exit = hs_exit
		

