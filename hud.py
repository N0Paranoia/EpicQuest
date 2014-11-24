import pygame
from constants import *


from pygame.locals import *

class Hud(object):

	def __init__(self, health, stamina, lives):
		self.lifeX = 32
		self.lifeY = 12
		self.staminaX = 32
		self.staminaY = 26
		self.healthWidth = health
		self.staminaWidth = stamina
		self.height = 8
		self.lives = lives

	def text(self, window, FPS, clock, state):
		font = pygame.font.Font(FONT_PATH, 10)
		font14 = pygame.font.Font(FONT_PATH, 14)

		if state == INTRO:
			textIntro = textIntro = font14.render("Intro", 1, (BLACK))
			window.blit(textIntro, (WINDOW_WIDTH/2- TILESIZE, WINDOW_HEIGHT/4))


		elif state == MAIN_MENU:
			textMainMenu = font14.render("Main Menu", 1, (BLACK))
			textMainMenu2 = font.render("Press [Enter] to Start", 1, (BLACK))

			window.blit(textMainMenu, (WINDOW_WIDTH/2- TILESIZE, WINDOW_HEIGHT/4))
			window.blit(textMainMenu2, (WINDOW_WIDTH/2- 52, WINDOW_HEIGHT/4 + TILESIZE))

		elif state == RUNNING:
			textLifes =  font.render(str(self.lives), 1, (WHITE))
			textControl = font.render("use [ASWD] to move, [K] to block, [L] to attack and [P] to pause", 1, (WHITE))
			textFPS = font.render("FPS = " + str(clock.get_fps()), 1, (WHITE))

			window.blit(textControl, (WINDOW_WIDTH - (11*TILESIZE), 2))
			window.blit(textFPS, (WINDOW_WIDTH - (4*TILESIZE), 16))
			window.blit(textLifes, (16,16))

		elif state == PAUSE:
			textPause = font14.render("PAUSE", 1, (GRAY))

			window.blit(textPause, (WINDOW_WIDTH/2- TILESIZE, WINDOW_HEIGHT/2))

		elif state == GAME_OVER:
			textGameOver= font14.render("Game Over", 1, (WHITE))
			textGameOver2 = font.render("Press [Return] to start over or [q] to quit", 1, (WHITE))

			window.blit(textGameOver, (WINDOW_WIDTH/2- TILESIZE, WINDOW_HEIGHT/2))
			window.blit(textGameOver2, (WINDOW_WIDTH/2- TILESIZE*3, WINDOW_HEIGHT/2 + TILESIZE))


	def render(self, window, state):
		if state == RUNNING or state == PAUSE:
			pygame.draw.rect(window, BLACK, (0, 0, WINDOW_WIDTH, 48))
			""" -- Draw Life and stamina Bar -- """
			pygame.draw.rect(window, BLACK, (self.lifeX-2, self.lifeY-2, 100+4, self.height+4))
			if self.healthWidth > 0:
				pygame.draw.rect(window, RED, (self.lifeX, self.lifeY, self.healthWidth, self.height))
			pygame.draw.rect(window, BLACK, (self.staminaX-2, self.staminaY-2, 100+4, self.height+4))
			if self.staminaWidth > 0:
				pygame.draw.rect(window, GREEN, (self.staminaX, self.staminaY, self.staminaWidth, self.height))


	def update(self, window, FPS, clock, state):
		self.render(window, state)
		self.text(window, FPS, clock, state)
