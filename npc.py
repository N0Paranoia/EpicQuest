import pygame
from pygame.locals import *
from constants import *

class Npc(object):

	def __init__(self):
		self.x = [2*TILESIZE, 8*TILESIZE]
		self.y = [1*TILESIZE, 5*TILESIZE]
		self.z = [1,2]
		self.width = 32
		self.height = 64
		self.interactRange = 2*TILESIZE
		self.text = ""

		self.npcSheet = pygame.image.load(NPC_PATH).convert_alpha()
		self.npcSurface = pygame.Surface((LEVEL_WIDTH*TILESIZE,LEVEL_HEIGHT*TILESIZE), pygame.SRCALPHA)
		self.npcSurface.blit(self.npcSheet,(0,0))


	def interact(self, npc, window,  playerX, playerY, levelID):
		font = pygame.font.Font(FONT_PATH, 8)
		textControl = font.render(self.text, 1, (BLACK))

		if levelID == 1: 
			if playerX > self.x[npc] - self.interactRange and playerX < self.x[npc] + self.interactRange and playerY == self.y[npc]:
				self.text = self.dialog(2)
				pygame.draw.rect(window, WHITE, (self.x[npc] - 5*TILESIZE- 8, self.y[npc], 7*TILESIZE, TILESIZE-3/TILESIZE))
				window.blit(textControl, (self.x[npc] - 5*TILESIZE, self.y[npc] - TILESIZE))

		if levelID == 2: 
			if playerX > self.x[1] - self.interactRange and playerX < self.x[1] + self.interactRange and playerY == self.y[1] and self.z[1]:
					self.text = self.dialog(1)
					pygame.draw.rect(window, WHITE, (self.x[1] - 5*TILESIZE- 8, self.y[1] - TILESIZE- 4, 7*TILESIZE, TILESIZE-3/TILESIZE))
					window.blit(textControl, (self.x[1] - 5*TILESIZE, self.y[1] - TILESIZE))

	def dialog(self, NPC):
		if NPC == 0:
			return "VISIT MY BROTHER IN DE HOUSE BELOW."
		if NPC == 1:
			return "IT'S DANGEROUS TO GO ALONE! TAKE THESE."
		else:
			return ""

	def render(self, npc, window, camX, camY, levelID):
		if self.y[1]:
			window.blit(self.npcSurface, (self.x[npc] - camX, self.y[npc] - camY), OLD_MAN)
		
		if levelID == 2:
			window.blit(self.npcSurface, (self.x[npc+1] - camX, self.y[npc+1] - camY), OLD_MAN)

	def update(self, window, camX, camY, playerX, playerY, levelID):
		for npc in range (NPC_NUMBER):
			self.render(npc, window, camX, camY, levelID)
			self.interact(npc, window, playerX, playerY, levelID)