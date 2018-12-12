import pygame
import Color
class menu():
    def __init__(self, run, setting):
        self.run = run
        self.setting = setting
        self.exit = False;
    def isExit(self,pos):
        x, y =pos
        if x > 130 and x < 190 :
            if y > 170 and y <190:
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
                    if self.run.range(pos):
                        self.run.display(screen)
                    elif self.setting.range(pos):
                        self.setting.display(screen)
                    elif self.isExit(pos):
                        self.exit = True

            my_font = pygame.font.Font(None, 30)
            text_surface_run = my_font.render(self.run.text, True, Color.white)
            rect = text_surface_run.get_rect(center=self.run.pos)
            screen.blit(text_surface_run, rect)

            text_surface_set = my_font.render(self.setting.text, True, Color.white)
            rect = text_surface_set.get_rect(center=self.setting.pos)
            screen.blit(text_surface_set, rect)

            text_surface = my_font.render('Exit', True, Color.white)
            rect = text_surface.get_rect(center=[160, 180])
            screen.blit(text_surface, rect)
            pygame.display.flip()

        self.exit = False


