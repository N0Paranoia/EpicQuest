import pygame
from pygame.locals import *
from constants import *

class Ai(object):

	def __init__(self):
		self.velocity_x = 0
		self.velocity_y = 0
		self.speed = 4
		self.LEFT = True
		self.RIGHT = False

	def move(self, x, y):


		if x <= 0:
		 	self.velocity_x = self.speed
		elif x >= MAPWIDTH*32 - TILESIZE:
		 	self.velocity_x = -self.speed
		else:
			self.velocity_x = -self.speed

		x += self.velocity_x

	 	print self.velocity_x

		return x