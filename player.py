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
		self.velocity_j = 0
		self.jump_speed = 2
		self.jump_height = 8
		self.jump_count = 0

	def input(self, event):
		keys = pygame.key.get_pressed()

		self.LEFT = False
		self.RIGHT = False
		self.UP = False
		self.DOWN = False
		self.JUMP = False

		if keys[K_a]:
			self.LEFT = True
		if keys[K_d]:
			self.RIGHT = True
		if keys[K_w]:
			self.UP = True
		if keys[K_s]:
			self.DOWN = True
		if keys[K_SPACE]:
			self.JUMP = True
			self.jump()

	def jump(self):
		if self.JUMP == True:
			print self.JUMP
			print self.velocity_j
			if self.jump_count <= self.jump_height:
				self.jump_count += 1
				self.velocity_j = -self.jump_speed
			else:
				jump_count = 0
				self.velocity_j = 0
				

	def move(self, gravity, camX, camY):
		col = Collision()

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

		self.x += self.velocity_x
		if self.x < 0 or self.x + self.width > MAPWIDTH*32 or col.WallCollision(self.x, self.y, self.width, self.height) == True:
			self.x -= self.velocity_x

		self.velocity_y += gravity
		self.y += self.velocity_y
		if self.y < 0 or self.y + self.height > MAPHEIGHT*32 or col.WallCollision(self.x, self.y, self.width, self.height) == True:
			self.y -= self.velocity_y

		self.y += self.velocity_j
		if self.y < 0 or self.y + self.height > MAPHEIGHT*32 or col.WallCollision(self.x, self.y, self.width, self.height) == True:
			self.y -= self.velocity_j
		
	def render(self, window, camX, camY):
		pygame.draw.rect(window, WHITE, (self.x - camX, self.y - camY, self.width, self.height))

	def update (self, event, window, camX, camY, gravity):
		self.input(event)
		self.move(gravity, camX, camY)
		self.render(window, camX, camY)
