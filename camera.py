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
		if self.x + self.width > MAPWIDTH*32:
			self.x = MAPWIDTH*32 - self.width
		if self.y + self.height > MAPHEIGHT*32:
			self.y = MAPHEIGHT*32 - self.height

	def render(self, window):
		pygame.draw.rect(window, WHITE, (self.x/WINDOW_WIDTH, self.y/WINDOW_HEIGHT, self.width, self.height), 2)

	def update(self, cCamX, cCamY, window):
		self.follow(cCamX, cCamY)
		self.render(window)

class CenterCamera(object):

	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = 64
		self.height = 96

	def follow (self, x, y):
		if self.x > x:
			self.x = x
		if self.x < x - TILESIZE:
			self.x = x - TILESIZE
		if self.y > y:
			self.y = y
		if self.y < y - 2*TILESIZE:
			self.y = y - 2*TILESIZE

	def render(self, window, camX, camY):
		pygame.draw.rect(window, BLACK, (self.x - camX, self.y - camY, self.width, self.height), 1)

	def update(self, playerX, playerY, camX, camY, window):
		self.follow(playerX, playerY)
		self.render(window, camX, camY)