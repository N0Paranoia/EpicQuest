import pygame
from pygame.locals import *
from constants import *

class Doors(object):
	def __init__(self):
		self.numberOfDoors = 3

		self.doorAx = [10*TILESIZE,19*TILESIZE,14*TILESIZE]
		self.doorAy = [1*TILESIZE,1*TILESIZE,19*TILESIZE]
		self.doorBx = [2*TILESIZE,27*TILESIZE,15*TILESIZE]
		self.doorBy = [26*TILESIZE,26*TILESIZE,19*TILESIZE]

	def doorConnections(self, x, y):
		for doors in range (self.numberOfDoors):
			if x + TILESIZE/2 >= self.doorAx[doors]  and x - TILESIZE/2 <= self.doorAx[doors] and y == self.doorAy[doors]:
				return (self.doorBx[doors], self.doorBy[doors])
			if x + TILESIZE/2 >= self.doorBx[doors]  and x - TILESIZE/2 <= self.doorBx[doors] and y == self.doorBy[doors]:
			 	return (self.doorAx[doors], self.doorAy[doors])
		return x, y