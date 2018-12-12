import pygame
import getTime
import config
import Color

class clockSet():
    def __init__(self):
        self.text = 'Alarm Setting'
        self.pos = [160, 60]
        self.exit = False;
        self.hour = int(config.hour)
        self.minute = int(config.minute)
        
    def range(self, pos):
        ref_x, ref_y = self.pos
        x, y = pos
        if x > ref_x - 30 and x < ref_x + 30:
            if y > ref_y - 20 and y < ref_y + 20:
                return True
        return False    
        
    def isExit(self,pos):
        x, y =pos
        return x > 260 and x < 320 and y > 180 and y < 240
        
    def isAddHour(self, pos):
	x, y = pos
    	return x > 20 and x < 140 and y > 20 and y < 100
		
    def isMinusHour(self, pos):
    	x, y = pos
    	return x > 20 and x < 140 and y > 140 and y < 200
		
    def isAddMin(self, pos):
    	x, y = pos
    	return x > 180 and x < 260 and y > 20 and y < 100
		
    def isMinusMin(self, pos):
    	x, y = pos
    	return x > 180 and x < 260 and y > 140 and y < 200
		
    def hour2str(self):
    	if self.hour/10 == 0:
    		return '0' + str(self.hour)
    	else:
	    	return str(self.hour)
		
    def min2str(self):
	if self.minute/10 == 0:
    		return '0' + str(self.minute)
    	else:
    		return str(self.minute)
			
			
    def add_hour(self):
    	self.hour += 1
    	if self.hour >= 24:
    		self.hour = 0

    def add_min(self):
    	self.minute += 1
    	if self.minute >= 60:
    		self.minute = 0
			
    def minus_hour(self):
    	self.hour -= 1
    	if self.hour <= 0:
    		self.hour = 23

    def minus_min(self):
    	self.minute -= 1
    	if self.minute <= 0:
    		self.minute = 59		

    def display(self, screen):
        while not self.exit:
            screen.fill(Color.black)
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                elif event.type is pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.isAddHour(pos):
                        self.add_hour()
                    elif self.isMinusHour(pos):
                        self.minus_hour()
                    elif self.isAddMin(pos):
                        self.add_min()
                    elif self.isMinusMin(pos):
                        self.minus_min()    
                    elif self.isExit(pos):
                        self.exit = True
                        config.hour = self.hour2str()
                        config.minute = self.min2str()
	    
            time_info = self.hour2str()+':'+self.min2str()

            my_font = pygame.font.Font(None, 40)
    	    text_surface = my_font.render(time_info, True, Color.white)
	    pos = [160,120]
	    rect = text_surface.get_rect(center=pos)
	    screen.blit(text_surface, rect)
			
	    my_font_ok = pygame.font.Font(None, 20)
	    text_surface_ok = my_font_ok.render('Confirm', True, Color.white)
	    pos_ok = [280,200]
	    rect = text_surface_ok.get_rect(center=pos_ok)
	    screen.blit(text_surface_ok, rect)
			
	    pygame.display.flip()

        self.exit = False
		
