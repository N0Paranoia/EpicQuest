import pygame
from pygame.locals import *
from constants import *

class Npc(object):

	def __init__(self):
		self.x = [4*TILESIZE, 8*TILESIZE]
		self.y = [2*TILESIZE, 5*TILESIZE]
		self.z = [1,2]
		self.width = TILESIZE
		self.height = 2*TILESIZE
		self.interactRange = 2*TILESIZE
		self.text = ""

		self.npcSheet = pygame.image.load(NPC_PATH).convert_alpha()
		self.npcSurface = pygame.Surface((LEVEL_WIDTH*TILESIZE,LEVEL_HEIGHT*TILESIZE), pygame.SRCALPHA)
		self.npcSurface.blit(self.npcSheet,(0,0))

		
	def interact(self, npc, window,  playerX, playerY):
		font = pygame.font.Font(FONT_PATH, 16)
		textControl = font.render(self.text, 1, (BLACK))
		textRect = textControl.get_rect().height

		if playerX > self.x[npc] - self.interactRange and playerX < self.x[npc] + self.interactRange and playerY == self.y[npc]:
			self.text = self.dialog(npc)
			pygame.draw.rect(window, WHITE, (self.x[npc] - TILESIZE, self.y[npc] - TILESIZE, textControl.get_rect().width + 8, textControl.get_rect().height + 8))
			window.blit(textControl, (self.x[npc] - TILESIZE + 4, self.y[npc] - TILESIZE + 4))

	def dialog(self, NPC):
		if NPC == 0:
			return "Visit my brother in the house below."
		if NPC == 1:
			return "It's dangerous to go alone! Take these."
		else:
			return ""

	def render(self, npc, window, camX, camY):
		window.blit(self.npcSurface, (self.x[npc] - camX, self.y[npc] - camY), OLD_MAN)
		
	def update(self, window, camX, camY, playerX, playerY, levelID):
		for npc in range (NPC_NUMBER):
			if self.z[npc] == levelID:
				self.render(npc, window, camX, camY)
				self.interact(npc, window, playerX, playerY)