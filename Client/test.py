import time
import Color
import pygame

class testDisplay():
    def __init__(self):
        self.t = 5
        self.pos = [250,200]
        self.text = "test"

    def range(self, pos):
        ref_x, ref_y = self.pos
        x, y = pos
        if x > ref_x - 30 and x < ref_x + 30:
            if y > ref_y - 20 and y < ref_y + 20:
                return True
        return False

    def display(self, screen):
        screen.fill(Color.black)
        pygame.display.flip()
        time.sleep(self.t)