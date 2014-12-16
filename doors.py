import pygame
from pygame.locals import *
from constants import *

class Doors(object):
	def __init__(self):
		# self.numberOfDoors = 4

		# self.doorAx = [10*TILESIZE,19*TILESIZE,14*TILESIZE]
		# self.doorAy = [1*TILESIZE,1*TILESIZE,19*TILESIZE]
		# self.doorBx = [2*TILESIZE,27*TILESIZE,15*TILESIZE]
		# self.doorBy = [26*TILESIZE,26*TILESIZE,19*TILESIZE]

		self.door1Ax = 10*TILESIZE
		self.door1Ay = 1*TILESIZE

		self.door1Bx = 2*TILESIZE
		self.door1By = 26*TILESIZE

		self.door2Ax = 19*TILESIZE
		self.door2Ay = 1*TILESIZE

		self.door2Bx = 27*TILESIZE
		self.door2By = 26*TILESIZE

		self.door3Ax = 14*TILESIZE
		self.door3Ay = 19*TILESIZE

		self.door3Bx = 15*TILESIZE
		self.door3By = 19*TILESIZE

	def doorConnections(self, x, y):
		if x + TILESIZE/2 >= self.door1Ax  and x - TILESIZE/2 <= self.door1Ax and y == self.door1Ay:
			return (self.door1Bx, self.door1By)
		elif x + TILESIZE/2 >= self.door1Bx  and x - TILESIZE/2 <= self.door1Ax and y == self.door1By:
			return (self.door1Ax, self.door1Ay)

		if x + TILESIZE/2 >= self.door2Ax  and x - TILESIZE/2 <= self.door2Ax and y == self.door2Ay:
			return (self.door2Bx, self.door2By)
		elif x + TILESIZE/2 >= self.door2Bx  and x - TILESIZE/2 <= self.door2Bx and y == self.door2By:
			return (self.door2Ax, self.door2Ay)

		if x + TILESIZE/2 >= self.door3Ax  and x - TILESIZE/2 <= self.door3Ax and y == self.door3Ay:
			return (self.door3Bx, self.door3By)
		elif x + TILESIZE/2 >= self.door3Bx  and x - TILESIZE/2 <= self.door3Bx and y == self.door3By:
			return (self.door3Ax, self.door3Ay)

		else:
			return x, y