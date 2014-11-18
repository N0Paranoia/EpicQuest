import pygame
from pygame.locals import *
from constants import *
from ai import *

ai = Ai()

class Mobs(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.xX = [576,32]
		self.yY = [32,32]
		self.x1 = 576
		self.x2 = 32
		self.y1 = 32
		self.y2 = 32
		self.width = 32
		self.height = 32
		self.speed1 = 2
		self.speed2 = 2
		self.mobNumber = 2

	def movement(self):
		for i in range (self.mobNumber):
			fall = ai.falling(GRAVITY, self.xX[i], self.yY[i], self.width, self.height)
			move = ai.move(self.xX[i], self.yY[i], self.width, self.height, self.speed1, i)
			self.xX[i] = move
			self.yY[i] = fall
			
	def render(self, window, camX, camY):
		for i in range (self.mobNumber):
			pygame.draw.rect(window, RED, (self.xX[i] - camX, self.yY[i] - camY, self.width, self.height))



	def update(self, window, camX, camY):
		self.movement()
		self.render(window, camX, camY)
