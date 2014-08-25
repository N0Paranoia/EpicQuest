import pygame
from pygame.locals import *
from constants import *

class Ai(object):

	def __init__(self):
		self.velocity_x = 4
		self.velocity_y = 0

	def move(self, x, y):
		x -= self.velocity_x
		if x <= 0:
			x += self.velocity_x
		elif x >= MAPWIDTH*32:
			x -= self.velocity_x
		return x