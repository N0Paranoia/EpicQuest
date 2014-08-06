import pygame

class GameStates(object):

	def __init__(self):
		self.intro = True
		self.running = True
		self.pause = False
		self.gameOver = False

	def changestate(self, lives):
		if lives <= 0:
			self.gameOver = True
			