import pygame
import math
from pygame.locals import *
from constants import *
from level import *
from ai import *

ai = Ai()

class Mobs(object):

	def __init__(self):
		self.x = [3*TILESIZE,25*TILESIZE]
		self.y = [2*TILESIZE,2*TILESIZE]
		self.width = 32
		self.height = 64
		self.speed = 1
		self.knockbackSpeed = 16
		self.mobNumber = 2
		self.canGetHit = [True, True]
		self.gotHit = False
		self.health = [32,32]
		self.alive = [True, True]
		self.weaponX = [-10,-10]
		self.weaponY = [-10,-10]
		self.weaponW = [32,32]
		self.weaponH = [16,16]
		self.attack_count = [0, 0]
		self.attack_duration = [8, 8]


	def movement(self, mobs, playerX, playerY, shieldHit):
		fall = ai.falling(GRAVITY, self.x[mobs], self.y[mobs], self.width, self.height)
		move = ai.move(self.x[mobs], self.y[mobs], self.width, self.height, self.speed, mobs, playerX, playerY, shieldHit)
		self.x[mobs] = move
		self.y[mobs] = fall

	def hitDetect(self, mobs, swordX, swordY, swordW, swordH, damage):
		if self.canGetHit[mobs]:			
			if ai.getHit(self.x[mobs], self.y[mobs], self.width, self.height, swordX, swordY, swordW, swordH):
				self.health[mobs] -= damage*0.32

			if self.health[mobs] <= 0:
				self.alive[mobs] = False
				
	def attack(self, window, mobs, playerX, playerY, camX, camY, shieldHit):
		if ai.attack(self.x[mobs], self.y[mobs], self.width, self.height, self.speed, mobs, playerX, playerY, shieldHit):
			if self.attack_count[mobs] <= self.attack_duration[mobs]:
				self.attack_count[mobs] += 1
				self.weapon(mobs, playerX, playerY, camX, camY, shieldHit)
				pygame.draw.rect(window, RED, (self.weaponX[mobs] - camX, self.weaponY[mobs] - camY, self.weaponW[mobs], self.weaponH[mobs]), 2)
		else:
			self.weapon(mobs, playerX, playerY, camX, camY, shieldHit)
			self.attack_count[mobs] = 0

	def weapon(self, mobs, playerX, playerY, camX, camY, shieldHit):
		weapon = ai.weapon(self.x[mobs], self.y[mobs], self.width, self.height, self.speed, mobs, playerX, playerY, shieldHit)
		self.weaponX[mobs] = weapon
		self.weaponY[mobs] = self.y[mobs] + self.height/4
		
	def healthBar(self, window, camX, camY, mobs):
		pygame.draw.rect(window, RED, (self.x[mobs] - camX, self.y[mobs] - 10  - camY, self.health[mobs], 2))

	def render(self, window, camX, camY, mobs):
		pygame.draw.rect(window, RED, (self.x[mobs] - camX, self.y[mobs] - camY, self.width, self.height))
		
	def update(self, window, camX, camY, playerX, playerY, swordX, swordY, swordW, swordH, damage, shieldHit):
		for mobs in range (self.mobNumber):
			if (self.x[mobs] > camX and self.y[mobs] > camY and self.x[mobs] < camX + WINDOW_WIDTH and self.y[mobs] < camY + WINDOW_HEIGHT):
				if self.alive[mobs]:
					self.movement(mobs, playerX, playerY, shieldHit)
					self.attack(window, mobs, playerX, playerY, camX, camY, shieldHit)
					self.hitDetect(mobs, swordX, swordY, swordW, swordH, damage)
					self.healthBar(window, camX, camY, mobs)
					self.render(window, camX, camY, mobs)