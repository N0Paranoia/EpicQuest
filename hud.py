import pygame
from constants import *


from pygame.locals import *

class Hud(object):

	def __init__(self):
		self.x = 0
		self.y = 0

	def text(self, window, FPS, clock):
		font = pygame.font.SysFont('consolas', 12)
			
		textControl = font.render("use [ASWD] to move", 1, (GRAY))
		textFPS = font.render("FPS = " + str(clock.get_fps()), 1, (GRAY))
		window.blit(textFPS, (16, 16))
		window.blit(textControl, (16, 32))

	def update(self, window, FPS, clock):
		self.text(window, FPS, clock)


