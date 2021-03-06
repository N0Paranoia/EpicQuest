import pygame
from constants import *
from level import *
from world import *
from pygame.locals import *


class Collision(object):

	def __init__(self):
		self.x = 0
		self.y = 0

	@staticmethod
	def CheckCollision(x, y, w, h, tile):
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

	@staticmethod
	def CheckCloudCollision(x, y, w, h, tile):
		leftA = x
		rightA = x + w
		topA = y + h - GRAVITY
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

	@staticmethod
	def CheckVarCollision(x, y, w, h, x2, y2, w2, h2):
		leftA = x
		rightA = x + w
		topA = y
		bottomA = y + h

		leftB = x2
		rightB = x2 + w2
		topB = y2
		bottomB = y2 + h2

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
	@staticmethod
	def TileCollision(x, y, w, h, camX, camY, tile, tileMap):
		for row in range(LEVEL_HEIGHT):
				for column in range (LEVEL_WIDTH):
					if tileMap[row][column] == tile:
						if column * TILESIZE > camX - 2*TILESIZE and column * TILESIZE < camX + WINDOW_WIDTH + TILESIZE and row * TILESIZE > camY - 2*TILESIZE and row * TILESIZE < camY + WINDOW_HEIGHT + TILESIZE:
							tiles = Tile(column*TILESIZE, row*TILESIZE)
							if Collision.CheckCollision(x, y, w, h, tiles) == True:
								return True

	""" -- Tile specific collision check -- """
	@staticmethod
	def CloudCollision(x, y, w, h, camX, camY, tile, tileMap):
		for row in range(LEVEL_HEIGHT):
				for column in range (LEVEL_WIDTH):
					if tileMap[row][column] == tile:
						if column * TILESIZE > camX - 2*TILESIZE and column * TILESIZE < camX + WINDOW_WIDTH + TILESIZE and row * TILESIZE > camY - 2*TILESIZE and row * TILESIZE < camY + WINDOW_HEIGHT + TILESIZE:
							tiles = Tile(column*TILESIZE, row*TILESIZE)
							if Collision.CheckCloudCollision(x, y, w, h, tiles) == True:
								return True

	@staticmethod
	def VarCollision(x, y, w, h, x2, y2, w2, h2):
		if Collision.CheckVarCollision(x, y, w, h, x2, y2, w2, h2) == True:
			return True