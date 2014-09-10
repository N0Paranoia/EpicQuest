import pygame
from pygame.locals import *
from constants import *
from level import *


class Tile(object):

	def __init__(self, x, y, textures):
		self.x = x
		self.y = y
		self.width = TILESIZE
		self.height = TILESIZE
		self.color = color
		self.textures = textures

		# myimage = pygame.image.load(TILE_PATH)

		self.imagerect = pygame.Rect((0,0),(32,32))
		self.sprite = pygame.Surface(self.imagerect.size)#.convert()
		self.sprite.blit(TILE_SHEET,(0,0),(textures))

	def render(self, window):
		# pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
		# window.blit(self.sprite, (self.x, self.y), self.imagerect)
		window.blit(self.sprite, (self.x, self.y), self.imagerect)
