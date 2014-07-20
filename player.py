import pygame
from pygame.locals import *
from constants import *
from collision import *
from camera import *

class Player(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 32
		self.height = 32
		self.speed = 4
		self.velocity_x = 0
		self.velocity_y = 0

	def input(self, event):
		keys = pygame.key.get_pressed()

		self.LEFT = False
		self.RIGHT = False
		self.UP = False
		self.DOWN = False

		if keys[K_a]:
			self.LEFT = True
		if keys[K_d]:
			self.RIGHT = True
		if keys[K_w]:
			self.UP = True
		if keys[K_s]:
			self.DOWN = True

	def move(self):
		if self.LEFT == True:
			self.velocity_x = -self.speed
		elif self.RIGHT == True:
			self.velocity_x = self.speed
		else:
			self.velocity_x = 0		
		if self.UP == True:
			self.velocity_y = -self.speed
		elif self.DOWN == True:
			self.velocity_y = self.speed
		else:
			self.velocity_y = 0

	def update(self, gravity, camX, camY):
		col = Collision()

		self.x += self.velocity_x
		if self.x < 0 or self.x + self.width > MAPWIDTH*32 or col.WallCollision(self.x, self.y, self.width, self.height) == True:
			self.x -= self.velocity_x

		# self.velocity_y += gravity
		self.y += self.velocity_y
		if self.y < 0 or self.y + self.height > MAPHEIGHT*32 or col.WallCollision(self.x, self.y, self.width, self.height) == True:
			self.y -= self.velocity_y
		
	def render(self, window, camX, camY):
		pygame.draw.rect(window, WHITE, (self.x - camX, self.y - camY, self.width, self.height))