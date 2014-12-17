import pygame
from pygame.locals import *
from constants import *
from level import *
from ai import *

ai = Ai(MOB_NUMBER)

class Mobs(object):

	def __init__(self):
		self.x = [5*TILESIZE,24*TILESIZE,5*TILESIZE,24*TILESIZE]
		self.y = [2*TILESIZE,2*TILESIZE,27*TILESIZE,27*TILESIZE]
		self.width = 32
		self.height = 64
		self.speed = 1
		self.canGetHit = [True]*MOB_NUMBER
		self.health = [32]*MOB_NUMBER
		self.alive = [True]*MOB_NUMBER
		self.weaponX,self.weaponY,self.weaponW,self.weaponH = [-10]*MOB_NUMBER,[-10]*MOB_NUMBER,[32]*MOB_NUMBER,[8]*MOB_NUMBER
		self.attacking = [False]*MOB_NUMBER
		self.attack_count = [0]*MOB_NUMBER
		self.attack_duration = [8]*MOB_NUMBER


	def movement(self, mobs, playerX, playerY, shieldHit, tileMap):
		fall = ai.falling(GRAVITY, self.x[mobs], self.y[mobs], self.width, self.height, tileMap)
		move = ai.move(self.x[mobs], self.y[mobs], self.width, self.height, self.speed, mobs, playerX, playerY, shieldHit, tileMap)
		self.x[mobs] = move
		self.y[mobs] = fall

	def hitDetect(self, mobs, swordX, swordY, swordW, swordH, damage):
		if self.canGetHit[mobs]:			
			if ai.getHit(self.x[mobs], self.y[mobs], self.width, self.height, swordX, swordY, swordW, swordH):
				self.health[mobs] -= damage*0.32

			if self.health[mobs] <= 0:
				self.alive[mobs] = False
				
	def attack(self, window, mobs, playerX, playerY, camX, camY):
		if ai.attack(self.x[mobs], self.y[mobs], self.width, self.height, self.speed, mobs, playerX, playerY):
			if self.attack_count[mobs] <= self.attack_duration[mobs]:
				self.attacking[mobs] = True
				self.attack_count[mobs] += 1
				self.weapon(mobs, playerX, playerY, camX, camY)
				pygame.draw.rect(window, RED, (self.weaponX[mobs] - camX, self.weaponY[mobs] - camY, self.weaponW[mobs], self.weaponH[mobs]), 1)
		else:
			self.weapon(mobs, playerX, playerY, camX, camY)
			self.attack_count[mobs] = 0
			self.attacking[mobs] = False 

	def weapon(self, mobs, playerX, playerY, camX, camY):
		weapon = ai.weapon(self.x[mobs], self.y[mobs], self.width, self.height, self.speed, mobs, playerX, playerY)
		self.weaponX[mobs] = weapon
		self.weaponY[mobs] = self.y[mobs] + self.height/4
		
	def healthBar(self, window, camX, camY, mobs):
		pygame.draw.rect(window, RED, (self.x[mobs] - camX, self.y[mobs] - 10  - camY, self.health[mobs], 2))

	def render(self, window, camX, camY, mobs):
		pygame.draw.rect(window, RED, (self.x[mobs] - camX, self.y[mobs] - camY, self.width, self.height))
		
	def update(self, window, camX, camY, playerX, playerY, swordX, swordY, swordW, swordH, damage, shieldHit, tileMap):
		if levelID == 1:
			for mobs in range (MOB_NUMBER):
				if (self.x[mobs] > camX and self.y[mobs] > camY and self.x[mobs] < camX + WINDOW_WIDTH and self.y[mobs] < camY + WINDOW_HEIGHT):
					if self.alive[mobs]:
						self.movement(mobs, playerX, playerY, shieldHit, tileMap)
						self.attack(window, mobs, playerX, playerY, camX, camY)
						self.hitDetect(mobs, swordX, swordY, swordW, swordH, damage)
						self.healthBar(window, camX, camY, mobs)
						self.render(window, camX, camY, mobs)