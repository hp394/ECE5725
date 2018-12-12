import pygame
import Color


class menu():
    def __init__(self, weatherReport, Memo):
        self.weatherReport = weatherReport
        self.Memo = Memo
        self.pos = [160, 60]
        self.exit = False

    def isExit(self, pos):
        x, y = pos
        if x > 130 and x < 190:
            if y > 170 and y < 190:
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
                    if self.weatherReport.range(pos):
                        self.weatherReport.display(screen)
                    elif self.Memo.range(pos):
                        self.Memo.display(screen)
                    elif self.isExit(pos):
                        self.exit = True

            my_font = pygame.font.Font(None, 30)

            text_surface_run = my_font.render(self.weatherReport.text, True, Color.white)
            rect = text_surface_run.get_rect(center=self.weatherReport.pos)
            screen.blit(text_surface_run, rect)

            text_surface_set = my_font.render(self.Memo.text, True, Color.white)
            rect = text_surface_set.get_rect(center=self.Memo.pos)
            screen.blit(text_surface_set, rect)

            text_surface = my_font.render('Back', True, Color.white)
            rect = text_surface.get_rect(center=[160, 180])
            screen.blit(text_surface, rect)

            pygame.display.flip()

        self.exit = False

