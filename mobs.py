import pygame
from pygame.locals import *
from constants import *
from ai import *

ai = Ai()

class Mobs(object):

	def __init__(self):
		self.x = [9*TILESIZE,21*TILESIZE]
		self.y = [3*TILESIZE,3*TILESIZE]
		self.width = 32
		self.height = 32
		self.speed1 = 2
		self.speed2 = 2
		self.mobNumber = 2

	def movement(self, i):
		fall = ai.falling(GRAVITY, self.x[i], self.y[i], self.width, self.height)
		move = ai.move(self.x[i], self.y[i], self.width, self.height, self.speed1, i)
		self.x[i] = move
		self.y[i] = fall

	def render(self, window, camX, camY, i):
		pygame.draw.rect(window, RED, (self.x[i] - camX, self.y[i] - camY, self.width, self.height))

	def update(self, window, camX, camY):
		for i in range (self.mobNumber):
			self.movement(i)
			self.render(window, camX, camY, i)
