import pygame
from pygame.locals import *
from constants import *

class Mobs(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 32
		self.height = 32 

	def render(self, window):
		pygame.draw.rect(window, YELLOW, (self.x, self.y, self.width, self.height))

	def update(self, window):
		self.render(window)