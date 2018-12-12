import pygame
import Color
import subprocess
import time
import config

def drawText(name,size,pos):
    global screen
    my_font = pygame.font.Font(None, size)
    text_surface = my_font.render(name, True, Color.white)
    rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, rect)

def isTemp(self,pos):
    x, y =pos
    return x > 120 and x < 160 and y > 25 and y < 75
    
def isHum(self,pos):
    x, y =pos
    return x > 120 and x < 160 and y > 75 and y < 125
    
def isMot(self,pos):
	x, y =pos
    return x > 120 and x < 160 and y > 125 and y < 175

pygame.init()
size = [320, 240]
center_pos = [160,120]

global screen
screen = pygame.display.set_mode(size)

runflag  = True

TempFlag = True
HumFlag  = True
MotFlag  = True

while runflag:
	time.sleep(0.15)
	
	Tem_pos = [140, 50]
	Hum_pos = [140,100]
	PIR_pos = [140,150]
	
	screen.fill(Color.black)
	
	if (TempFlag == True):
		drawText('Temp', 30, Tem_pos)
	if (HumFlag == True):
		drawText('Humidity', 30, Hum_pos)
	if (MotFlag == True):
		drawText('Motion', 30, PIR_pos)
		
	pygame.display.flip()

