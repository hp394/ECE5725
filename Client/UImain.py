import pygame
from pygame.locals import *
import SettingMenu
import Runmenu
import menu
import test
import Color
import clockSetting
import IntelligentClock
import SenSet
import homeSecurity
import os


os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')


pygame.init()
pygame.mouse.set_visible(False)

size = [320, 240]
screen = pygame.display.set_mode(size)
setting = SettingMenu.menu(clockSetting.clockSet(), SenSet.SenSet())
run = Runmenu.menu(IntelligentClock.clock(), homeSecurity.homeSecurity())
mainmenu = menu.menu(run, setting)

mainmenu.display(screen)




