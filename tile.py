import pygame
from pygame.locals import *
from constants import *
from level import *


class Tile(object):
	
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.width = TILESIZE
		self.height = TILESIZE
		self.color = color

	def render(self, window):
		pygame.draw.rect(window, tile, (tile.x, tile.y, tile.width, tile.height))