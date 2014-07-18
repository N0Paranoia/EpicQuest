import pygame
from constants import *
from tilemap import *
from level import *
from pygame.locals import *


class Collision(object):

	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0
		
	def CheckCollision(self, x, y, w, h, tile):
		leftA = x
		rightA = x + w
		topA = y
		bottomA = y + h

		leftB = tile.x
		rightB = tile.x + TILESIZE
		topB = tile.y
		bottomB = tile.y + TILESIZE

		if bottomA <= topB:
			return False
		if topA >= bottomB:
			return False
		if rightA <= leftB:
			return False
		if leftA >= rightB:
			return False
		#If none of the sides from A are outside B 
		return True


	def WallCollision(self, x, y, w, h, camX, camY):
		
		for row in range(MAPHEIGHT):
				for column in range (MAPWIDTH):
					if tilemap[row][column] > 0:
						tiles = Tile(column*TILESIZE - camX, row*TILESIZE - camY, None)
						col = Collision()
						if col.CheckCollision(x, y, w, h, tiles) == True:
							return True