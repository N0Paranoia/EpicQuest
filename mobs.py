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
			move = ai.move(self.xX[i], self.yY[i], self.width, self.height, self.speed1, self.mobNumber)
			self.xX[i] = move
			self.yY[i] = fall

		# fall = ai.falling(GRAVITY, self.x, self.y, self.width, self.height)
		fall1 = ai.falling(GRAVITY, self.x1, self.y1, self.width, self.height)
		fall2 = ai.falling(GRAVITY, self.x2, self.y2, self.width, self.height)
		# move = ai.move(self.x, self.y, self.width, self.height, self.speed1)
		move1 = ai.move(self.x1, self.y1, self.width, self.height, self.speed1, self.mobNumber)
		move2 = ai.move(self.x2, self.y2, self.width, self.height, self.speed2, self.mobNumber)
		# self.y = fall
		# self.x = move
		self.y1 = fall1
		self.x1 = move1
		self.y2 = fall2
		self.x2 = move2


	def render(self, window, camX, camY):
		# pygame.draw.rect(window, YELLOW, (self.x - camX, self.y - camY, self.width, self.height))
		pygame.draw.rect(window, YELLOW, (self.x1 - camX, self.y1 - camY, self.width, self.height))
		pygame.draw.rect(window, GREEN, (self.x2 - camX, self.y2 - camY, self.width, self.height))
		for i in range (self.mobNumber):
			pygame.draw.rect(window, RED, (self.xX[i] - camX, self.yY[i] - camY, self.width, self.height))



	def update(self, window, camX, camY):
		self.movement()
		self.render(window, camX, camY)
