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

	def movement(self, mobs):
		fall = ai.falling(GRAVITY, self.x[mobs], self.y[mobs], self.width, self.height)
		move = ai.move(self.x[mobs], self.y[mobs], self.width, self.height, self.speed1, mobs)
		self.x[mobs] = move
		self.y[mobs] = fall

	def render(self, window, camX, camY, mobs):
		pygame.draw.rect(window, RED, (self.x[mobs] - camX, self.y[mobs] - camY, self.width, self.height))

	def update(self, window, camX, camY):
		for mobs in range (self.mobNumber):
			if (self.x[mobs] > camX and self.y[mobs] > camY and self.x[mobs] < camX + WINDOW_WIDTH and self.y[mobs] < camY + WINDOW_HEIGHT):
				self.movement(mobs)
				self.render(window, camX, camY, mobs)
