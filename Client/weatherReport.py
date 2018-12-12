import pygame
import Color


class menu():
    def __init__(self, report):
        self.report = report
        self.text = 'Weather'
        self.pos = [160, 60]
        self.exit = False

    def isExit(self, pos):
        x, y =pos
        return x > 260 and x < 320 and y > 200 and y < 240

    def range(self, pos):
        ref_x, ref_y = self.pos
        x, y = pos
        if x > ref_x - 30 and x < ref_x + 30:
            if y > ref_y - 20 and y < ref_y + 20:
                return True
        return False

    def drawWeather(self,screen):
	res = self.report['forecast']		
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

    def display(self, screen):
        while not self.exit:
            screen.fill(Color.black)
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                elif event.type is pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.isExit(pos):
                        self.exit = True

            my_font = pygame.font.Font(None, 30)


            text_surface = my_font.render('Back', True, Color.white)
            rect = text_surface.get_rect(center=[280,200])
            screen.blit(text_surface, rect)
			
	    self.drawWeather(screen)
            pygame.display.flip()

        self.exit = False

