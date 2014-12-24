import pygame
from pygame.locals import *
from constants import *

class Npc(object):

	def __init__(self):
		self.x = 8*TILESIZE
		self.y = 5*TILESIZE
		self.interactRange = 2*TILESIZE

		self.rect = pygame.Rect((0,0),(32,64))

		self.npcSheet = pygame.image.load(NPC_PATH).convert_alpha()
		self.npcSurface = pygame.Surface((self.rect.size), pygame.SRCALPHA)
		self.npcSurface.blit(self.npcSheet,(0,0),self.rect)

	def interact(self, playerX, playerY):
		if playerX > self.x - self.interactRange and playerX < self.x + self.interactRange and playerY == self.y:
			print "IT'S DANGEROUS TO GO ALONE! TAKE THIS."

	def render(self, window, camX, camY):
		window.blit(self.npcSurface, (self.x - camX, self.y - camY), self.rect)

	def update(self, window, camX, camY, playerX, playerY, levelID):
		if levelID == 2:
			self.render(window, camX, camY)
			self.interact(playerX, playerY)