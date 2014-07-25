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
		self.velocity_j = 4
		self.jump_speed = 4
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
			if self.is_falling == False:
				self.JUMP = True
			
	def falling(self, gravity, camX, camY):
		colf = Collision()
		self.is_falling = True
		self.y += gravity
  		if self.y < 0 or self.y + self.height > MAPHEIGHT*32 or colf.WallCollision(self.x, self.y, self.width, self.height, camX, camY) == True:
	  		self.y -= gravity
	  		self.is_falling = False

	def jump(self):
		if self.JUMP:
			if self.jump_count <= self.jump_height:
				self.velocity_j = -self.jump_speed
				self.jump_count += 1
				self.is_falling = False
			else:
				self.velocity_j = 0
				self.JUMP = False
		else:
			self.jump_count = 0

	def climbing(self, camX, camY):
		colL = Collision()
		if self.JUMP == False:
			if self.x < 0 or self.x + self.width > MAPWIDTH*32 or colL.TileCollision(self.x, self.y, self.width, self.height, camX, camY, LADDER) == True:
				print "ladder collission"

	def move(self, gravity, camX, camY):
		col = Collision()

		if self.LEFT:
			self.velocity_x = -self.speed
		elif self.RIGHT:
			self.velocity_x = self.speed
		else:
			self.velocity_x = 0		
		if self.UP:
			self.velocity_y = -self.speed
		elif self.DOWN:
			self.velocity_y = self.speed
		else:
			self.velocity_y = 0

		if self.JUMP:
			self.velocity_j -= self.jump_speed
		else:
			self.velocity_j = 0

		self.x += self.velocity_x
		if self.x < 0 or self.x + self.width > MAPWIDTH*32 or col.WallCollision(self.x, self.y, self.width, self.height, camX, camY) == True:
			self.x -= self.velocity_x

		self.y += self.velocity_y
		if self.y < 0 or self.y + self.height > MAPHEIGHT*32 or col.WallCollision(self.x, self.y, self.width, self.height, camX, camY) == True:
			self.y -= self.velocity_y

		self.y += self.velocity_j
		if self.y < 0 or self.y + self.height > MAPHEIGHT*32 or col.WallCollision(self.x, self.y, self.width, self.height, camX, camY) == True:
			self.y -= self.velocity_j

			
	def render(self, window, camX, camY):
		pygame.draw.rect(window, GRAY, (self.x - camX, self.y - camY, self.width, self.height))

	def update (self, event, window, camX, camY, gravity):
		self.input(event)
		self.falling(gravity, camX, camY)
		self.jump()
		self.climbing(camX, camY)
		self.move(gravity, camX, camY)
		self.render(window, camX, camY)