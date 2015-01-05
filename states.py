import pygame
from constants import *

class GameStates(object):

	def __init__(self):
		self.intro = False
		self.mainMenu = False
		self.running = True
		self.pause = False
		self.gameOver = False
		
	def changestate(self, lives):
		""" -- GameOVer when user dies -- """
		if lives <= 0:
			self.gameOver = True

class LevelStates(object):

	def __init__(self):
		pass

	def changeState(self, level):
		return level