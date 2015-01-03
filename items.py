import pygame
from pygame.locals import *
from constants import *
from collision import *

class Items(object):
	
	def __init__(self):
		self.swordX = 6 * TILESIZE
		self.swordY = 6 * TILESIZE
		self.swordW = 8
		self.swordH = 32
		self.shieldX = 7 * TILESIZE
		self.shieldY = 6 * TILESIZE
		self.shieldW = 16
		self.shieldH = 32
		self.pickedUpSword = False
		self.pickedUpShield = False
		self.frameSword = 0
		self.frameShield = 32

		self.itemSheet = pygame.image.load(ITEM_PATH).convert_alpha()
		self.itemSurface = pygame.Surface((LEVEL_WIDTH*TILESIZE,LEVEL_HEIGHT*TILESIZE), pygame.SRCALPHA)
		self.itemSurface.blit(self.itemSheet,(0,0))

		self.collision = Collision()

	def interact(self, playerX, playerY):
		if self.collision.VarCollision(self.swordX, self.swordY, self.swordW, self.swordH, playerX, playerY, PLAYER_WIDTH, PLAYER_HEIGHT):
			self.pickedUpSword = True
		if self.collision.VarCollision(self.shieldX, self.shieldY, self.shieldW, self.shieldH, playerX, playerY, PLAYER_WIDTH, PLAYER_HEIGHT):
			self.pickedUpShield = True

	def render(self, window, camX, camY):
		if not self.pickedUpSword:
			window.blit(self.itemSurface, (self.swordX - camX, self.swordY - camY), SWORD)
		if not self.pickedUpShield:
			window.blit(self.itemSurface, (self.shieldX - camX, self.shieldY - camY), SHIELD)

	def update(self, window, camX, camY, playerX, playerY, levelID):
		if levelID == 2:
			self.interact(playerX, playerY)
			self.interact(playerX, playerY)
			self.render(window, camX, camY)