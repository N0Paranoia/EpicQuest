import pygame
from pygame.locals import *
from constants import *
from level import *


class Tile(object):
	
	def __init__(self, x, y, color, textures):
		self.x = x
		self.y = y
		self.width = TILESIZE
		self.height = TILESIZE
		self.color = color
		self.textures = textures

	def render(self, window):
		pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))