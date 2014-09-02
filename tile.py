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
		self.tileSheet = pygame.image.load(TILE_PATH)

	def render(self, window, x):
		pygame.draw.rect(window, tile, (tile.x, tile.y, tile.width, tile.height))