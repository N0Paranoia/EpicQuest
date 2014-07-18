import pygame
from constants import *

class Camera(object):

	def __init__(self, x, y):
		self.x = (x + TILESIZE/2) - (WINDOW_WIDTH/2)
		self.y = (y + TILESIZE/2) - (WINDOW_HEIGHT/2)
		self.width = WINDOW_WIDTH
		self.height = WINDOW_HEIGHT

	def update (self, x, y):
		pass

	def render(self, window):
		pygame.draw.rect(window, WHITE, (self.x, self.y, self.width, self.height), 2)