import pygame
from constants import *
from pygame.locals import *

class Doors(object):
	def __init__(self):
		self.numberOfDoors = 3

		self.doorAx = [10*TILESIZE,19*TILESIZE,14*TILESIZE]
		self.doorAy = [1*TILESIZE,1*TILESIZE,19*TILESIZE]
		self.doorAz = [1,1,1]
		
		self.doorBx = [2*TILESIZE,27*TILESIZE,2*TILESIZE]
		self.doorBy = [26*TILESIZE,26*TILESIZE,5*TILESIZE]
		self.doorBz = [1,1,2]

	def doorConnections(self, x, y, z):
		for doors in range (self.numberOfDoors):
			if x + TILESIZE/2 >= self.doorAx[doors]  and x - TILESIZE/2 <= self.doorAx[doors] and y == self.doorAy[doors]:
				return (self.doorBx[doors], self.doorBy[doors], self.doorBz[doors])
			if x + TILESIZE/2 >= self.doorBx[doors]  and x - TILESIZE/2 <= self.doorBx[doors] and y == self.doorBy[doors]:
			 	return (self.doorAx[doors], self.doorAy[doors], self.doorAz[doors])
		return x, y, z