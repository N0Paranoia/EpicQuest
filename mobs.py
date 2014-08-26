import pygame
from pygame.locals import *
from constants import *
from ai import *

class Mobs(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 32
		self.height = 32

	def movement(self):
		ai = Ai()
		move = ai.move(self.x, self.y)
		self.x = move

	def render(self, window, camX, camY):
		pygame.draw.rect(window, YELLOW, (self.x - camX, self.y - camY, self.width, self.height))

	def update(self, window, camX, camY):
		self.movement()
		self.render(window, camX, camY)