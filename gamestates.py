import pygame
from level import *

class GameStates(object):

	def __init__(self):
		self.intro = True
		self.mainMenu = False
		self.running = False
		self.pause = False
		self.gameOver = False

	def changestate(self, lives):
		""" -- GameOVer when user dies -- """
		if lives <= 0:
			self.gameOver = True

	def changelevel(self, currentLevel, addLevel):
		return currentLevel+addLevel
