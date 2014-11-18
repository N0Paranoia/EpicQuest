import pygame
from pygame.locals import *
from constants import *
from collision import *

class Ai(object):

	def __init__(self):
		self.velocity_x = 0
		self.velocity_y = 0
		self.LEFT = False
		self.RIGHT = True
		self.LEFTx = [0,1]
		self.RIGHTx = [0,1]


	def falling(self, gravity, x, y, width, height):
		self.is_falling = True
		y += gravity
		if y < 0 or y + height > MAPHEIGHT*TILESIZE or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) == True or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, LADDER_TOP) == True or Collision().CloudCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, PLATFORM) == True:
			y -= gravity
			self.is_falling = False

		return y

	def move(self, x, y, width, height, speed, numberOfMobs):

		if self.LEFT:
			self.velocity_x = -speed

		elif self.RIGHT:
			self.velocity_x = speed

		x += self.velocity_x

		if x < 0 or x > MAPWIDTH*32 - TILESIZE or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, LAVA) or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, SKY) or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_LEFT) or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_RIGHT) or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, SLOPE_LEFT) or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, SLOPE_RIGHT):
			x -= self.velocity_x

			self.velocity_x = -speed
			# self.LEFT = not self.LEFT
			# self.RIGHT = not self.RIGHT

			print "xVel", self.velocity_x, numberOfMobs
		return x

		y += self.velocity_y
		if y < 0 or y > MAPHEIGHT*32 - TILESIZE or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) == True:
			y -= self.velocity_y

		return y
