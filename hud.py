import pygame
from constants import *


from pygame.locals import *

class Hud(object):

	def __init__(self, health, lives):
		self.lifeX = 16
		self.lifeY = 16
		self.width = health
		self.height = 16
		self.lives = lives

	def text(self, window, FPS, clock):
		font = pygame.font.SysFont('consolas', 12)
			
		textLifes =  font.render(str(self.lives), 1, (GRAY))
		textControl = font.render("use [ASWD] to move", 1, (GRAY))
		textFPS = font.render("FPS = " + str(clock.get_fps()), 1, (GRAY))
		window.blit(textFPS, (500, 16))
		window.blit(textControl, (500, 32))
		window.blit(textLifes, (8,16))

	def render(self, window):
		pygame.draw.rect(window, RED, (self.lifeX, self.lifeX , self.width, self.height))

	def update(self, window, FPS, clock):
		self.render(window)
		self.text(window, FPS, clock)


