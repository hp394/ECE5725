import pygame
import Color


class menu():
    def __init__(self, clockset, sensor):
        self.clockset = clockset
        self.sensor = sensor
        self.text = 'Run'
        self.pos = [160, 60]
        self.exit = False

    def isExit(self, pos):
        x, y = pos
        if x > 130 and x < 190:
            if y > 170 and y < 190:
                return True
        return False

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
                    if self.clockset.range(pos):
                        self.clockset.display(screen)
                    elif self.sensor.range(pos):
                        self.sensor.display(screen)
                    elif self.isExit(pos):
                        self.exit = True

            my_font = pygame.font.Font(None, 30)

            text_surface_run = my_font.render(self.clockset.text, True, Color.white)
            rect = text_surface_run.get_rect(center=self.clockset.pos)
            screen.blit(text_surface_run, rect)

            text_surface_set = my_font.render(self.sensor.text, True, Color.white)
            rect = text_surface_set.get_rect(center=self.sensor.pos)
            screen.blit(text_surface_set, rect)

            text_surface = my_font.render('Back', True, Color.white)
            rect = text_surface.get_rect(center=[160, 180])
            screen.blit(text_surface, rect)

            pygame.display.flip()

        self.exit = False
