import pygame
from constants import *

class Camera(object):

	def __init__(self, x, y):
		self.x = x - (WINDOW_WIDTH/2)
		self.y = y - (WINDOW_HEIGHT/2)
		self.width = WINDOW_WIDTH
		self.height = WINDOW_HEIGHT

	def update (self, x, y):
		if x <= self.x:
			self.x = x
		if x >= self.x + TILESIZE:
			self.x = x - TILESIZE
		if y <= self.y:
			self.y = y
		if y >= self.y + TILESIZE:
			self.y = y - TILESIZE

	def render(self, window):
		pygame.draw.rect(window, RED, (self.x, self.y, self.width, self.height), 1)