import pygame
from pygame.locals import *
from constants import *
from collision import *
from doors import *
from camera import *

class Player(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 32
		self.height = 32
		self.health = 100
		self.lives = 3
		self.speed = PLAYER_SPEED
		self.velocity_x = 0
		self.velocity_y = 0
		self.velocity_j = 4
		self.climbing_speed = 4
		self.jump_speed = 4
		self.jump_height = 8
		self.jump_count = 0
		self.is_climbing = False
		self.canGoTroughDoor = True

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
		if self.y < 0 or self.y + self.height > MAPHEIGHT*32 or colf.TileCollision(self.x, self.y, self.width, self.height, camX, camY, WALL) == True or colf.TileCollision(self.x, self.y, self.width, self.height, camX, camY, LADDER_TOP) == True or colf.CloudCollision(self.x, self.y, self.width, self.height, camX, camY, PLATFORM) == True or self.is_climbing == True:
			self.y -= gravity
			self.is_falling = False

	def jump(self):
		if self.JUMP:
			self.is_climbing = False
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
		if colL.TileCollision(self.x, self.y, self.width, self.height, camX, camY, LADDER) == True or colL.TileCollision(self.x, self.y, self.width, self.height, 
			camX, camY, LADDER_TOP) == True:
			if self.UP:
				self.is_climbing = True
				self.velocity_y = -self.climbing_speed
			elif self.DOWN:
				self.is_climbing = True
				self.velocity_y = self.climbing_speed
			else:
				self.velocity_y = 0
		else:
			self.velocity_y = 0
			self.is_climbing = False

	def gotroughdoor(self, camX, camY):
		colD = Collision()
		doorD = Doors()
		if self.UP:
			if self.canGoTroughDoor:
				if colD.TileCollision(self.x, self.y, self.width, self.height, camX, camY, DOOR) == True:
					self.x, self.y = doorD.doorConnections(self.x, self.y)
					self.canGoTroughDoor = False
					self.UP = False
		else:		
			self.canGoTroughDoor = True

	def playerHealth(self, camX, camY):
		colH = Collision()
		if colH.TileCollision(self.x, self.y, self.width, self.height, camX, camY, LAVA) == True :
			self.health -= 5
		if self.health <= 0:
			self.health = 100
			self.lives -= 1

	def move(self, gravity, camX, camY):
		col = Collision()

		if self.LEFT:
			self.velocity_x = -self.speed
		elif self.RIGHT:
			self.velocity_x = self.speed
		else:
			self.velocity_x = 0		

		if self.DOWN:
		 	self.velocity_y = self.speed

		if self.JUMP:
			self.velocity_j -= self.jump_speed
		else:
			self.velocity_j = 0

		self.x += self.velocity_x
		if self.x < 0 or self.x + self.width > MAPWIDTH*32 or col.TileCollision(self.x, self.y, self.width, self.height, camX, camY, WALL) == True:
			self.x -= self.velocity_x

		self.y += self.velocity_y
		if self.y < 0 or self.y + self.height > MAPHEIGHT*32 or col.TileCollision(self.x, self.y, self.width, self.height, camX, camY, WALL) == True:
			self.y -= self.velocity_y

		self.y += self.velocity_j
		if self.y < 0 or self.y + self.height > MAPHEIGHT*32 or col.TileCollision(self.x, self.y, self.width, self.height, camX, camY, WALL) == True:
			self.y -= self.velocity_j
			
	def render(self, window, camX, camY):
		pygame.draw.rect(window, GRAY, (self.x - camX, self.y - camY, self.width, self.height))

	def update (self, event, window, camX, camY, gravity):
		self.input(event)
		self.falling(gravity, camX, camY)
		self.jump()
		self.climbing(camX, camY)
		self.gotroughdoor(camX, camY)
		self.move(gravity, camX, camY)
		self.playerHealth(camX, camY)
		self.render(window, camX, camY)