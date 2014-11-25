import pygame
from constants import *
from level import *
from world import *
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
		""" -- If none of the sides from A are outside B """
		return True

	def CheckCloudCollision(self, x, y, w, h, tile):
		leftA = x
		rightA = x + w
		topA = y + TILESIZE - GRAVITY
		bottomA = y + h

		leftB = tile.x
		rightB = tile.x + TILESIZE
		topB = tile.y
		bottomB = tile.y + GRAVITY

		if bottomA <= topB:
			return False
		if topA >= bottomB:
			return False
		if rightA <= leftB:
			return False
		if leftA >= rightB:
			return False
		""" -- If none of the sides from A are outside B -- """
		return True

	def CheckMobCollision(self, playerX, playerY, mobX, mobY):
		leftA = playerX
		rightA = playerX + TILESIZE
		topA = playerY
		bottomA = playerY + TILESIZE

		leftB = mobX
		rightB = mobX + TILESIZE
		topB = mobY
		bottomB = mobY + TILESIZE

		if bottomA <= topB:
			return False
		if topA >= bottomB:
			return False
		if rightA <= leftB:
			return False
		if leftA >= rightB:
			return False
		""" -- If none of the sides from A are outside B """
		return True

	""" -- Tile specific collision check -- """
	def TileCollision(self, x, y, w, h, camX, camY, tile):
		for row in range(MAPHEIGHT):
				for column in range (MAPWIDTH):
					if level[row][column] == tile:
						if column * TILESIZE > camX - 2*TILESIZE and column * TILESIZE < camX + WINDOW_WIDTH + TILESIZE and row * TILESIZE > camY - 2*TILESIZE and row * TILESIZE < camY + WINDOW_HEIGHT + TILESIZE:
							tiles = Tile(column*TILESIZE, row*TILESIZE)
							col = Collision()
							if col.CheckCollision(x, y, w, h, tiles) == True:
								return True

	""" -- Tile specific collision check -- """
	def CloudCollision(self, x, y, w, h, camX, camY, tile):
		for row in range(MAPHEIGHT):
				for column in range (MAPWIDTH):
					if level[row][column] == tile:
						if column * TILESIZE > camX - 2*TILESIZE and column * TILESIZE < camX + WINDOW_WIDTH + TILESIZE and row * TILESIZE > camY - 2*TILESIZE and row * TILESIZE < camY + WINDOW_HEIGHT + TILESIZE:
							tiles = Tile(column*TILESIZE, row*TILESIZE)
							col = Collision()
							if col.CheckCloudCollision(x, y, w, h, tiles) == True:
								return True

	def MobCollision(self, playerX, playerY, mobX, mobY):
		col = Collision()
		if col.CheckMobCollision(playerX, playerY, mobX, mobY) == True:
			return True
