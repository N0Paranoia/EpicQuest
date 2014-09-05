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

		# self.spriteSheet = pygame.image.load(TILE_PATH)
		# self.rect = pygame.Rect((0,0),(TILESIZE,TILESIZE))
		# self.sprite = pygame.Surface(self.rect.size).convert()
		# self.sprite.blit(self.spriteSheet,(0,0),self.rect)

	def render(self, window):
		pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
		# window.blit(self.sprite, (self.x, self.y), self.rect)