import pygame
from pygame.locals import *
from constants import *
from collision import *

class Ai(object):

	def __init__(self):
		self.velocity_x = 0
		self.velocity_y = 0
		self.speed = 4
		self.LEFT = True
		self.RIGHT = False
		self.BACK = False

	def falling(self, gravity, x, y, width, height, camX, camY):
		self.is_falling = True
		y += gravity
		if y < 0 or y + height > MAPHEIGHT*TILESIZE or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) == True or Collision().TileCollision(x, y, width, height, camX, camY, LADDER_TOP) == True or Collision().CloudCollision(x, y, width, height, camX, camY, PLATFORM) == True:
			y -= gravity
			self.is_falling = False

		return y

	def move(self, x, y, width, height, camX, camY, speed):

		if self.LEFT:
			self.velocity_x = -speed

		elif self.RIGHT:
			self.velocity_x = speed

		x += self.velocity_x

		if x < 0 or x > MAPWIDTH*32 - TILESIZE or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) == True or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, LAVA) == True:
			if not Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_LEFT) or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_RIGHT):
				x -= self.velocity_x

			 	if self.LEFT:
			 		self.LEFT = not self.LEFT
					self.RIGHT = not self.RIGHT
				elif self.RIGHT:
					self.RIGHT = not self.RIGHT
					self.LEFT = not self.LEFT
				else:
					self.LEFT = not self.LEFT
					self.RIGHT = not self.RIGHT

		if self.RIGHT and Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_LEFT) == True:
 			pass
 		if self.LEFT and Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_RIGHT) == True:
 			pass

		return x

		y += self.velocity_y
		if y < 0 or y > MAPHEIGHT*32 - TILESIZE or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) == True:
			y -= self.velocity_y

	 	return y