import pygame
from pygame.locals import *
from constants import *
from level import *
from ai import *

ai = Ai()

class Mobs(object):

	def __init__(self):
		self.x = [3*TILESIZE,25*TILESIZE]
		self.y = [3*TILESIZE,3*TILESIZE]
		self.width = 32
		self.height = 32
		self.speed = 1
		self.knockbackSpeed = 16
		self.mobNumber = 2
		self.canGetHit = [True, True]
		self.gotHit = False
		self.health = [32,32]
		self.alive = [True, True]

	# def generateMob(self, window, camX, camY, playerX, playerY):
	# 	for row in range(MAPHEIGHT):
	# 		for column in range (MAPWIDTH):
	# 			if column * TILESIZE > camX - TILESIZE and column * TILESIZE < camX + WINDOW_WIDTH and row * TILESIZE > camY - TILESIZE and row * TILESIZE < camY + WINDOW_HEIGHT:
	# 				if mobsMap[row][column] == 5:
	# 					m0bs = MobPosition(column*TILESIZE, row*TILESIZE)
	# 					m0bs.update(window, camX, camY, playerX, playerY)

	def movement(self, mobs, playerX, playerY, swordX, swordY, swordW, swordH):
		fall = ai.falling(GRAVITY, self.x[mobs], self.y[mobs], self.width, self.height)
		move = ai.move(self.x[mobs], self.y[mobs], self.width, self.height, self.speed, mobs, playerX, playerY, swordX, swordY, swordW, swordH)
		self.x[mobs] = move
		self.y[mobs] = fall

	def hitDetect(self, mobs, playerX, playerY, swordX, swordY, swordW, swordH):
		if self.canGetHit[mobs]:			
			if ai.getHit(self.x[mobs], self.y[mobs], self.width, self.height, playerX, playerY, swordX, swordY, swordW, swordH):
				self.health[mobs] -= 5

			if self.health[mobs] <= 0:
				self.alive[mobs] = False
	
	def healthBar(self, window, camX, camY, mobs):
		pygame.draw.rect(window, RED, (self.x[mobs] - camX, self.y[mobs] - 10  - camY, self.health[mobs], 2))

	def render(self, window, camX, camY, mobs):
		pygame.draw.rect(window, RED, (self.x[mobs] - camX, self.y[mobs] - camY, self.width, self.height))

	# def renderMobs(self, window, camX, camY):
	# 	pygame.draw.rect(window, YELLOW, (self.x1 - camX, self.y1 - camY, self.width, self.height))

	def update(self, window, camX, camY, playerX, playerY, swordX, swordY, swordW, swordH):
		# self.generateMob(window, camX, camY, playerX, playerY)
		for mobs in range (self.mobNumber):
			if (self.x[mobs] > camX and self.y[mobs] > camY and self.x[mobs] < camX + WINDOW_WIDTH and self.y[mobs] < camY + WINDOW_HEIGHT):
				if self.alive[mobs]:
					self.movement(mobs, playerX, playerY, swordX, swordY, swordW, swordH)
					self.hitDetect(mobs, playerX, playerY, swordX, swordY, swordW, swordH)
					self.healthBar(window, camX, camY, mobs)
					self.render(window, camX, camY, mobs)


# class MobPosition(object):

# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
# 		self.width = 32
# 		self.height = 32

# 	def movement(self, mobs, playerX, playerY):
# 		fall = ai.falling(GRAVITY, self.x[mobs], self.y[mobs], self.width, self.height)
# 		move = ai.move(self.x[mobs], self.y[mobs], self.width, self.height, self.speed1, mobs, playerX, playerY)
# 		self.x[mobs] = move
# 		self.y[mobs] = fall

# 	def render(self, window, camX, camY):
# 		pygame.draw.rect(window, GREEN, (self.x - camX, self.y - camY, self.width, self.height))

# 	def update(self, window, camX, camY, playerX, playerY):
# 		self.render(window, camX, camY)
