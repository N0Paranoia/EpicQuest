import pygame
from pygame.locals import *
from constants import *

class Doors(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

		door1.x = 7*TILESIZE
		door1.y = 2*TILESIZE

	def doorConnections(self):
		pass