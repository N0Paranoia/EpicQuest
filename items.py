import pygame
from pygame.locals import *
from constants import *

class Items(object):
	
	def __init__(self):
		self.x = 0
		self.y = 0
		self.pickedUpSword = True
		self.pickedUpShield = False

	def interact(self, playerX, playerY):
		pass
	
	def update(self, window, camX, camY, playerX, playerY, levelID):
		if levelID == 2:
			self.interact(playerX, playerY)