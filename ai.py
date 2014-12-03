import pygame
from pygame.locals import *
from constants import *
from collision import *

class Ai(object):

	def __init__(self):
		self.velocity_x = 0
		self.velocity_y = 0
		self.LEFT = [False, False]
		self.RIGHT = [True, True]
		self.aggroGange = 3*TILESIZE

	def falling(self, gravity, x, y, width, height):
		self.is_falling = True
		y += gravity
		if y < 0 or y + height > MAPHEIGHT*TILESIZE or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) == True or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, LADDER_TOP) == True or Collision().CloudCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, PLATFORM) == True:
			y -= gravity
			self.is_falling = False

		return y

	def health(self, swordX, swordY):
		pass

	def getHit(self, x, y, width, height, playerX, playerY,  swordX, swordY, swordW, swordH):
		if Collision().MobCollision(x, y, width, height, swordX, swordY, swordW, swordH):
			return True

	def move(self, x, y, width, height, speed, numberOfMobs, playerX, playerY, swordX, swordY, swordW, swordH, gotHit):

		if self.LEFT[numberOfMobs]:
			self.velocity_x = -speed

		elif self.RIGHT[numberOfMobs]:
			self.velocity_x = speed

		x += self.velocity_x

		""" -- KnockBack -- """
		if gotHit:
			if playerX < x:
				print "Knockback RIGHT"
			if playerX > x + width:
				print "Knockback LEFT"


		""" -- Ai collision -- """
		if x < 0 or x > MAPWIDTH*32 - TILESIZE or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, LAVA) or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, SKY) or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_LEFT) or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, SLOPE_RIGHT) or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, SLOPE_LEFT) or Collision().TileCollision(x, y+TILESIZE, width, height, x+TILESIZE, y+TILESIZE, SLOPE_RIGHT):
			x -= self.velocity_x

			self.LEFT[numberOfMobs] = not self.LEFT[numberOfMobs]
			self.RIGHT[numberOfMobs] = not self.RIGHT[numberOfMobs]

		""" -- Aggro -- """
		if playerX > x - self.aggroGange and playerX < x and playerY > y - self.aggroGange and playerY	< y + self.aggroGange:
			self.RIGHT[numberOfMobs] = False
			self.LEFT[numberOfMobs] = True
		if playerX < x + self.aggroGange and playerX > x and playerY > y - self.aggroGange and playerY	< y + self.aggroGange:
			self.LEFT[numberOfMobs] = False
			self.RIGHT[numberOfMobs] = True

		return x

		y += self.velocity_y
		if y < 0 or y > MAPHEIGHT*32 - TILESIZE or Collision().TileCollision(x, y, width, height, x+TILESIZE, y+TILESIZE, WALL) == True:
			y -= self.velocity_y

		return y
