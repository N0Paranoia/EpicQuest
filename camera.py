import pygame
from constants import *

class Camera(object):

	def __init__(self, x, y):
		self.x = (x + TILESIZE/2) - (WINDOW_WIDTH/2)
		self.y = (y + TILESIZE/2) - (WINDOW_HEIGHT/2)
		self.width = WINDOW_WIDTH
		self.height = WINDOW_HEIGHT

	def follow (self, x, y):
		if self.x < 0:
			self.x = 0
		if self.y < 0:
			self.y = 0
		if self.x + self.width > LEVEL_WIDTH*TILESIZE:
			self.x = LEVEL_WIDTH*TILESIZE - self.width
		if self.y + self.height > LEVEL_HEIGHT*TILESIZE:
			self.y = LEVEL_HEIGHT*TILESIZE - self.height

	def update(self, cCamX, cCamY, window):
		self.follow(cCamX, cCamY)

class CenterCamera(object):

	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = 2*PLAYER_WIDTH
		self.height = 2*PLAYER_HEIGHT - PLAYER_HEIGHT/4

	def follow (self, x, y):
		if self.x > x:
			self.x = x
		if self.x + self.width < x + PLAYER_WIDTH:
			self.x = x + PLAYER_WIDTH - self.width

		if self.y > y:
			self.y = y
		if self.y + self.height < y + PLAYER_HEIGHT:
			self.y = y + PLAYER_HEIGHT - self.height

	def update(self, playerX, playerY, camX, camY, window):
		self.follow(playerX, playerY)