import pygame
import Color


class menu():
    def __init__(self, memos, count):
        self.memos = memos
        self.count = count
        self.text = 'Memo'
        self.pos = [160, 120]
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
			
	    things = ''
	    if self.count == 0:
		things = 'No events today'
		thing_font = pygame.font.Font(None, 20)
		thing_surface = my_font.render(str(things), True, Color.white)
		thing_rect = text_surface.get_rect(center=[80,120])
		screen.blit(thing_surface, thing_rect)
	    else:
		id = 1
		for row in self.memos:
			#date = str(row[0])
			thing = str(row[0])
			things = str(id)+'.'+thing
			thing_font = pygame.font.Font(None, 20)
			thing_surface = thing_font.render(str(things), True, Color.white)
			thing_rect = text_surface.get_rect(center=[30,30*id])
			screen.blit(thing_surface, thing_rect)
			id += 1
	    
	    
			
            pygame.display.flip()

        self.exit = False
