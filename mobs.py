import pygame
from pygame.locals import *
from constants import *
from level import *
from ai import *

ai = Ai(MOB_NUMBER)

class Mobs(object):

	def __init__(self):
		self.x = [8*TILESIZE,21*TILESIZE,5*TILESIZE,24*TILESIZE]
		self.y = [3*TILESIZE,3*TILESIZE,27*TILESIZE,27*TILESIZE]
		self.z = [1,1,1,1]
		self.width = TILESIZE
		self.height = 2*TILESIZE
		self.speed = 1
		self.canGetHit = [True]*MOB_NUMBER
		self.health = [self.width]*MOB_NUMBER
		self.alive = [True]*MOB_NUMBER
		self.weaponX,self.weaponY,self.weaponW,self.weaponH = [-10]*MOB_NUMBER,[-10]*MOB_NUMBER,[TILESIZE]*MOB_NUMBER,[TILESIZE/4]*MOB_NUMBER
		self.attacking = [False]*MOB_NUMBER
		self.attack_count = [0]*MOB_NUMBER
		self.attack_duration = [20]*MOB_NUMBER
		self.idle = 0
		self.left = 1
		self.right = 2

		self.mobSheet = pygame.image.load(MOB_PATH).convert_alpha()
		self.mobSurface = pygame.Surface((LEVEL_WIDTH*TILESIZE,LEVEL_HEIGHT*TILESIZE), pygame.SRCALPHA)
		self.mobSurface.blit(self.mobSheet,(0,0))


	def movement(self, window, camX, camY, mobs, playerX, playerY, shieldHit, tileMap):
		# fall = ai.falling(GRAVITY, self.x[mobs], self.y[mobs], self.width, self.height, tileMap)
		move = ai.move(self.x[mobs], self.y[mobs], self.width, self.height, self.speed, mobs, playerX, playerY, shieldHit, tileMap)
		self.x[mobs] = move
		# self.y[mobs] = fall

	def hitDetect(self, mobs, swordX, swordY, swordW, swordH, playerAttack, damage):
		if self.canGetHit[mobs]:
			if ai.getHit(self.x[mobs], self.y[mobs], self.width, self.height, swordX, swordY, swordW, swordH, playerAttack):
				self.health[mobs] -= damage*0.48
			if self.health[mobs] <= 0:
				self.alive[mobs] = False

	def attack(self, window, mobs, playerX, playerY, camX, camY):
		pass

	def render(self, window, camX, camY, levelID):
		for mobs in range (MOB_NUMBER):
			if self.z[mobs] == levelID:
				if (self.x[mobs] > camX-(WINDOW_WIDTH/2) and self.y[mobs] > camY - (TILESIZE*2) and self.x[mobs] < camX + (WINDOW_WIDTH + (WINDOW_WIDTH/2)) and self.y[mobs] < camY + WINDOW_HEIGHT + (TILESIZE*2)):
					if self.alive[mobs]:
						if ai.velocity_x[mobs] < 0:
							window.blit(self.mobSurface, (self.x[mobs] - camX, self.y[mobs] - camY), MOB_ONE_LEFT)
						elif ai.velocity_x[mobs] > 0:
							window.blit(self.mobSurface, (self.x[mobs] - camX, self.y[mobs] - camY), MOB_ONE_RIGHT)
						else:
							window.blit(self.mobSurface, (self.x[mobs] - camX, self.y[mobs] - camY), MOB_ONE_LEFT)
						""" -- Draw sword -- """
						pygame.draw.rect(window, RED, (self.weaponX[mobs] - camX, self.weaponY[mobs] - camY, self.weaponW[mobs], self.weaponH[mobs]), 1)
						""" -- Draw healthBar -- """
						pygame.draw.rect(window, RED, (self.x[mobs] - camX, self.y[mobs] - 10  - camY, self.health[mobs], 2))

	def update(self, window, camX, camY, playerX, playerY, swordX, swordY, swordW, swordH, damage, shieldHit, playerAttack, playerBlock, levelID, tileMap):
		for mobs in range (MOB_NUMBER):
			if self.z[mobs] == levelID:
				if (self.x[mobs] > camX-(WINDOW_WIDTH/2) and self.y[mobs] > camY - (TILESIZE*2) and self.x[mobs] < camX + (WINDOW_WIDTH + (WINDOW_WIDTH/2)) and self.y[mobs] < camY + WINDOW_HEIGHT + (TILESIZE*2)):
					if self.alive[mobs]:
						self.movement(window, camX, camY, mobs, playerX, playerY, shieldHit, tileMap)
						self.attack(window, mobs, playerX, playerY, camX, camY)
						self.hitDetect(mobs, swordX, swordY, swordW, swordH, playerAttack, damage)