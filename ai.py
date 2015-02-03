import pygame
from pygame.locals import *
from constants import *
from collision import *


class Ai(object):

	def __init__(self, mobNumber):
		self.velocity_x = [0] * mobNumber
		self.velocity_y = 0
		self.LEFT = [False]*mobNumber
		self.RIGHT = [False]*mobNumber
		self.aggroRange = 4*TILESIZE

		self.collision = Collision()

	def falling(self, gravity, x, y, width, height, tileMap):

		self.is_falling = True
		y += gravity
		if y < 0 or y + height > LEVEL_HEIGHT*TILESIZE or self.collision.TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL, tileMap) == True or self.collision.TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, LADDER_TOP, tileMap) == True or self.collision.CloudCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, PLATFORM, tileMap) == True:
			y -= gravity
			self.is_falling = False
		return y

	def getHit(self, x, y, width, height, swordX, swordY, swordW, swordH, playerAttack):
		if playerAttack == True:
			if self.collision.VarCollision(x, y, width, height, swordX, swordY, swordW, swordH):
				return True

	def attack(self, x, y, width, height, speed, numberOfMobs, playerX, playerY):
		if playerX > x - self.aggroRange and playerX < x and playerY > y - self.aggroRange and playerY	< y + self.aggroRange or  playerX < x + self.aggroRange and playerX > x and playerY > y - self.aggroRange and playerY	< y + self.aggroRange:
			return True
		else:
			return False
		
	def move(self, x, y, width, height, speed, numberOfMobs, playerX, playerY, shieldHit, tileMap):

		if self.LEFT[numberOfMobs]:
			self.velocity_x[numberOfMobs] = -speed

		elif self.RIGHT[numberOfMobs]:
			self.velocity_x[numberOfMobs] = speed
		else:
			x -= self.velocity_x[numberOfMobs]

		x += self.velocity_x[numberOfMobs]

		""" -- Ai collision -- """
		if self.collision.TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL, tileMap) or self.collision.TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_LEFT, tileMap) or self.collision.TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_RIGHT, tileMap):
			x -= self.velocity_x[numberOfMobs]

			self.LEFT[numberOfMobs] = not self.LEFT[numberOfMobs]
			self.RIGHT[numberOfMobs] = not self.RIGHT[numberOfMobs]

		""" -- Shield Collision -- """
		if shieldHit == True:
			x -= self.velocity_x[numberOfMobs]

		""" -- Aggro -- """
		if playerX > x - self.aggroRange and playerX < x and playerY > y - self.aggroRange and playerY	< y + self.aggroRange:
			self.RIGHT[numberOfMobs] = False
			self.LEFT[numberOfMobs] = True
		elif playerX < x + self.aggroRange and playerX > x and playerY > y - self.aggroRange and playerY	< y + self.aggroRange:
			self.LEFT[numberOfMobs] = False
			self.RIGHT[numberOfMobs] = True
		else:
			self.LEFT[numberOfMobs] = False
			self.RIGHT[numberOfMobs] = False
		return x

		y += self.velocity_y
		if y < 0 or y > MAPHEIGHT*TILESIZE - TILESIZE or self.collision.TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) == True:
			y -= self.velocity_y
		return y