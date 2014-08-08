import pygame

class GameStates(object):

	def __init__(self):
		self.intro = False
		self.mainMenu = True
		self.running = False
		self.pause = False
		self.gameOver = False

	def changestate(self, lives):
		# -- GameOVer when user dies
		if lives <= 0:
			self.gameOver = True

		