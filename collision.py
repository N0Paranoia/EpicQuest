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

	def CheckCloudCollision(self, x, y, w, h, tile):
		leftA = x
		rightA = x + w
		topA = y + TILESIZE - TILESIZE/4;
		bottomA = y + h

		leftB = tile.x
		rightB = tile.x + TILESIZE
		topB = tile.y
		bottomB = tile.y + TILESIZE/4;

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

	# -- Standard wall collision
	def WallCollision(self, x, y, w, h, camX, camY):
		
		for row in range(MAPHEIGHT):
				for column in range (MAPWIDTH):
					if tilemap[row][column] > 0 and tilemap[row][column] < LADDER :
						if column * TILESIZE > camX -TILESIZE and column * TILESIZE < camX + WINDOW_WIDTH and row * TILESIZE > camY -TILESIZE and row * TILESIZE < camY + WINDOW_HEIGHT:
							tiles = Tile(column*TILESIZE, row*TILESIZE, None)
							col = Collision()
							if col.CheckCollision(x, y, w, h, tiles) == True:
								return True

	# -- Tile specific collision check
	def TileCollision(self, x, y, w, h, camX, camY, tile):
		
		for row in range(MAPHEIGHT):
				for column in range (MAPWIDTH):
					if tilemap[row][column] == tile:
						if column * TILESIZE > camX -TILESIZE and column * TILESIZE < camX + WINDOW_WIDTH and row * TILESIZE > camY -TILESIZE and row * TILESIZE < camY + WINDOW_HEIGHT:
							tiles = Tile(column*TILESIZE, row*TILESIZE, None)
							col = Collision()
							if col.CheckCollision(x, y, w, h, tiles) == True:
								return True

		# -- Tile specific collision check
	def PlatformCollision(self, x, y, w, h, camX, camY, tile):
		
		for row in range(MAPHEIGHT):
				for column in range (MAPWIDTH):
					if tilemap[row][column] == tile:
						if column * TILESIZE > camX -TILESIZE and column * TILESIZE < camX + WINDOW_WIDTH and row * TILESIZE > camY -TILESIZE and row * TILESIZE < camY + WINDOW_HEIGHT:
							tiles = Tile(column*TILESIZE, row*TILESIZE, None)
							col = Collision()
							if col.CheckCloudCollision(x, y, w, h, tiles) == True:
								return True