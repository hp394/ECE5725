import pygame
import Color
import config

class SenSet():    
    def __init__(self):
        self.text = 'Sensors Setting'
        self.pos = [160,120]
        self.exit = False
        
        self.temp_flag = config.TempFlag
        self.hum_flag = config.HumFlag
        self.pir_flag = config.MotFlag
    
    def isExit(self,pos):
        x, y =pos
        if x > 260 and x < 320 :
            if y > 170 and y <240:
                return True
        return False
        
    def isTemp(self,pos):
        x, y =pos
        return x > 40 and x < 260 and y > 25 and y < 75
    
    def isHum(self,pos):
        x, y =pos
        return x > 40 and x < 240 and y > 75 and y < 125
    
    def isMot(self,pos):
        x, y =pos
        return x > 40 and x < 240 and y > 125 and y < 175
     
		
    def range(self, pos):
        ref_x, ref_y = self.pos
        x, y = pos
        if x > ref_x - 30 and x < ref_x + 30:
            if y > ref_y - 20 and y < ref_y + 20:
                return True
        return False        

    def display(self, screen):
        while not self.exit:
            screen.fill(Color.black)
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                elif event.type is pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.isTemp(pos):
			self.temp_flag = not self.temp_flag
                    elif self.isHum(pos):
			self.hum_flag = not self.hum_flag
                    elif self.isMot(pos):
			self.pir_flag = not self.pir_flag
                    elif self.isExit(pos):
			config.TempFlag = self.temp_flag
			config.HumFlag = self.hum_flag
			config.MotFlag = self.pir_flag
                        self.exit = True

            my_font = pygame.font.Font(None, 30)
            
            Tem_pos = [200, 50]
	    Hum_pos = [180,100]
	    PIR_pos = [180,150]
	    
	    Tem_on_pos = [80, 50]
	    Hum_on_pos = [80, 100]
	    PIR_on_pos = [80, 150]
	    
	    
			
            text_surface_temp = my_font.render('Temperature', True, Color.white)
            rect1 = text_surface_temp.get_rect(center=Tem_pos)
            screen.blit(text_surface_temp, rect1)
            
            temp_on_info = ''
            if not self.temp_flag:
		temp_on_info = 'Disable'
            else:
                temp_on_info = 'Enable'
	    text_surface_temp_on = my_font.render(temp_on_info, True, Color.white)
            rect1_on = text_surface_temp_on.get_rect(center=Tem_on_pos)
            screen.blit(text_surface_temp_on, rect1_on)
				

            text_surface_hum = my_font.render('Humidity', True, Color.white)
            rect2 = text_surface_hum.get_rect(center=Hum_pos)
            screen.blit(text_surface_hum, rect2)
            
            hum_on_info = ''
            if not self.hum_flag:
		    hum_on_info = 'Disable'
            else:
                    hum_on_info = 'Enable'
	    text_surface_hum_on = my_font.render(hum_on_info, True, Color.white)
            rect2_on = text_surface_hum_on.get_rect(center=Hum_on_pos)
            screen.blit(text_surface_hum_on, rect2_on)
            
            text_surface_PIR = my_font.render('Motion', True, Color.white)
            rect3 = text_surface_PIR.get_rect(center=PIR_pos)
            screen.blit(text_surface_PIR, rect3)
            
            mot_on_info = ''
            if not self.pir_flag:
		mot_on_info = 'Disable'
            else:
                mot_on_info = 'Enable'
	    text_surface_mot_on = my_font.render(mot_on_info, True, Color.white)
            rect3_on = text_surface_mot_on.get_rect(center=PIR_on_pos)
            screen.blit(text_surface_mot_on, rect3_on)

            text_surface = my_font.render('confirm', True, Color.white)
            rect = text_surface.get_rect(center=[280, 190])
            screen.blit(text_surface, rect)
            
            pygame.display.flip()

        self.exit = False


