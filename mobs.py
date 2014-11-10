import pygame
from pygame.locals import *
from constants import *
from ai import *

ai = Ai()

class Mobs(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 32
		self.height = 32
		self.speed1 = 2
		
	def movement(self):
		fall = ai.falling(GRAVITY, self.x, self.y, self.width, self.height)
		move = ai.move(self.x, self.y, self.width, self.height, self.speed1)
		self.y = fall
		self.x = move


	def render(self, window, camX, camY):
		pygame.draw.rect(window, YELLOW, (self.x - camX, self.y - camY, self.width, self.height))
		pygame.draw.rect(window, GREEN, ((self.x-2*TILESIZE) - camX, self.y - camY, self.width, self.height))


	def update(self, window, camX, camY):
		self.movement()
		self.render(window, camX, camY)