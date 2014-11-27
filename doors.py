import pygame
from pygame.locals import *
from constants import *

class Doors(object):
	def __init__(self):

		self.door1Ax = 9*TILESIZE
		self.door1Ay = 1*TILESIZE

		self.door1Bx = 2*TILESIZE
		self.door1By = 27*TILESIZE

		self.door2Ax = 20*TILESIZE
		self.door2Ay = 1*TILESIZE

		self.door2Bx = 27*TILESIZE
		self.door2By = 27*TILESIZE

	def doorConnections(self, x, y):
		if x + TILESIZE/2 >= self.door1Ax  and x - TILESIZE/2 <= self.door1Ax and y == self.door1Ay:
			return (self.door1Bx, self.door1By)
		elif x + TILESIZE/2 >= self.door1Bx  and x - TILESIZE/2 <= self.door1Ax and y == self.door1By:
			return (self.door1Ax, self.door1Ay)

		if x + TILESIZE/2 >= self.door2Ax  and x - TILESIZE/2 <= self.door2Ax and y == self.door2Ay:
			return (self.door2Bx, self.door2By)
		elif x + TILESIZE/2 >= self.door2Bx  and x - TILESIZE/2 <= self.door2Bx and y == self.door2By:
			return (self.door2Ax, self.door2Ay)

		else:
			return x, y
