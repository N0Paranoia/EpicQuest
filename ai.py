import pygame
from pygame.locals import *
from constants import *
from collision import *


class Ai(object):

	def __init__(self, mobNumber):
		self.velocity_x = 0
		self.velocity_y = 0
		self.LEFT = [False]*mobNumber
		self.RIGHT = [True]*mobNumber
		self.aggroRange = 3*TILESIZE

		self.collision = Collision()
		
	def falling(self, gravity, x, y, width, height, tileMap):
		
		self.is_falling = True
		y += gravity
		if y < 0 or y + height > LEVEL_HEIGHT*TILESIZE or self.collision.TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL, tileMap) == True or self.collision.TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, LADDER_TOP, tileMap) == True or Collision().CloudCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, PLATFORM, tileMap) == True:
			y -= gravity
			self.is_falling = False

		return y

	def getHit(self, x, y, width, height, swordX, swordY, swordW, swordH):
		
		if self.collision.VarCollision(x, y, width, height, swordX, swordY, swordW, swordH):
			return True

	def attack(self, x, y, width, height, speed, numberOfMobs, playerX, playerY):
		if playerX > x - self.aggroRange and playerX < x and playerY > y - self.aggroRange and playerY	< y + self.aggroRange or  playerX < x + self.aggroRange and playerX > x and playerY > y - self.aggroRange and playerY	< y + self.aggroRange:
			return True
		else:
			return False

	def weapon(self, x, y, width, height, speed, numberOfMobs, playerX, playerY):
		if self.LEFT[numberOfMobs]:
			return x - width
		elif self.RIGHT[numberOfMobs]:
			return x + width


	def move(self, x, y, width, height, speed, numberOfMobs, playerX, playerY, shieldHit, tileMap):
		
		if self.LEFT[numberOfMobs]:
			self.velocity_x = -speed

		elif self.RIGHT[numberOfMobs]:
			self.velocity_x = speed

		x += self.velocity_x
				
		""" -- Ai collision -- """
		if x < 0 or x > LEVEL_WIDTH*TILESIZE - TILESIZE or self.collision.TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL, tileMap) or self.collision.TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, LAVA, tileMap) or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_LEFT, tileMap) or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_RIGHT, tileMap) or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, SLOPE_LEFT, tileMap) or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, SLOPE_RIGHT, tileMap) or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+height+TILESIZE, SKY, tileMap):
			x -= self.velocity_x
		
			self.LEFT[numberOfMobs] = not self.LEFT[numberOfMobs]
			self.RIGHT[numberOfMobs] = not self.RIGHT[numberOfMobs]

		""" -- Shield Collision -- """
		if shieldHit == True:
			x -= self.velocity_x

		""" -- Aggro -- """
		if playerX > x - self.aggroRange and playerX < x and playerY > y - self.aggroRange and playerY	< y + self.aggroRange:
			self.RIGHT[numberOfMobs] = False
			self.LEFT[numberOfMobs] = True
		if playerX < x + self.aggroRange and playerX > x and playerY > y - self.aggroRange and playerY	< y + self.aggroRange:
			self.LEFT[numberOfMobs] = False
			self.RIGHT[numberOfMobs] = True

		return x

		y += self.velocity_y
		if y < 0 or y > MAPHEIGHT*TILESIZE - TILESIZE or self.collision.TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) == True:
			y -= self.velocity_y

		return y
