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

			self.sprite = pygame.Surface(TILERECT.size)
			self.sprite.blit(TILE_SHEET,(0,0),(textures))

		def render(self, window):
			# pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
			window.blit(self.sprite, (self.x, self.y), TILERECT)
			# window.blit(self.textures, (self.x, self.y, self.width, self.height))
