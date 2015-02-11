import pygame
import constants
from level import *
from player import *
from mobs import *
from npc import *
from items import *
from world import *
from camera import *
from hud import *
from states import *
from pygame.locals import *

pygame.init()

class Main(object):

	def __init__(self):
		screenSize = (WINDOW_WIDTH, WINDOW_HEIGHT)
		self.window = pygame.display.set_mode(screenSize)
		pygame.display.set_caption("EpicQuest")

		self.clock = pygame.time.Clock()

		""" -- Initialize Game -- """
		self.initialize(None)

		""" -- Variables to implement frame delays -- """
		self.startFrame = 0
		self.delayFrame = 1

		self.run = True
		while self.run:

			self.gamestate.changestate(self.player.lives)

			""" -- Intro game state -- """
			if self.gamestate.intro:
				for x in range(0, WINDOW_WIDTH):
					hud = Hud(0, None, None)
					pygame.draw.rect(window, WHITE, (0, WINDOW_HEIGHT - 100, x, 32))

					hud.update(window, FPS, clock, INTRO)

					""" -- Update Screen -- """
					pygame.display.flip()

					if x == WINDOW_WIDTH -1:
						gamestate.mainMenu = True

			""" -- Main menu game State -- """
			if self.gamestate.mainMenu:
				self.input()
				self.gamestate.intro = False
				self.gamestate.gameOver = False

				self.hud = Hud(0, None, None)
				pygame.draw.rect(self.window, WHITE, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
				self.hud.render(self.window, FPS, self.clock, MAIN_MENU)

			""" -- Running game State -- """
			if self.gamestate.running == True:

				self.gamestate.mainMenu = False

				if self.gamestate.pause == False:
					self.window.fill ((SKY_BLUE))
					
					self.input()
					self.update(self.gamestate.running)
					self.render(self.gamestate.running)

					self.debug()

			""" -- Pause Game State -- """
			if self.gamestate.pause:
				self.input()
				self.render(self.gamestate.pause)

			""" -- GameOver Game State -- """
			if self.gamestate.gameOver:
				self.input()
				self.hud = Hud(0, None, None)
				self.gamestate.running = False
				pygame.draw.rect(self.window, BLACK, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
				self.hud.render(self.window, FPS, self.clock, GAME_OVER)

			""" -- Update Screen -- """
			pygame.display.flip()

	def initialize(self, state):
		if state == None:
			self.camera = Camera(0,0)
			self.centerCam = CenterCamera()
			self.gamestate = GameStates()

		self.player = Player(PLAYER_START_X, PLAYER_START_Y, 1)
		self.npc = Npc()
		self.items = Items()
		self.mobs = Mobs()
		self.world = World()
		self.levelStates = LevelStates()
		
		if state == self.gamestate.gameOver:
			self.levelStates = LevelStates()
			self.gamestate.mainMenu = True

	def input(self):
		
		for self.event in pygame.event.get():
			if self.event.type == QUIT:
				self.run = False

			if self.event.type == KEYDOWN:
				if self.event.key == K_q:
					self.run = False
				if self.event.key == K_p:
					self.gamestate.pause = not self.gamestate.pause

				if self.event.key == K_RETURN:
					if self.gamestate.mainMenu:
						self.gamestate.running = True
					elif self.gamestate.gameOver:
						self.initialize(self.gamestate.gameOver)
		
		
		self.levelID = self.levelStates.changeState(self.player.z)
		self.level = Levels(self.levelID)				
		self.player.controls(self.level.level)

	def update(self, state):

		""" -- Set FPS -- """
		self.clock.tick(FPS)

		if state == self.gamestate.running:
			""" -- Initialize And Change Level -- """
			self.levelID = self.levelStates.changeState(self.player.z)
			self.level = Levels(self.levelID)

			""" -- Update Player Class -- """
			self.player.update(self.event, self.window, self.camera.x, self.camera.y, GRAVITY, self.mobs.x, self.mobs.y, self.mobs.width, self.mobs.height, self.mobs.alive, self.mobs.weaponX, self.mobs.weaponY, self.mobs.weaponW, self.mobs.weaponH,self. mobs.attacking, self.level.level, self.items.pickedUpSword, self.items.pickedUpShield)

			""" -- Update Ai Class -- """
			self.mobs.update(self.window, self.camera.x, self.camera.y, self.player.x, self.player.y, self.player.swordX, self.player.swordY, self.player.swordW, self.player.swordH, self.player.damage, self.player.shieldHit, self.player.ATTACK, self.player.BLOCK, self.levelID, self.level.level)

			""" -- Update Npc Class -- """
			self.npc.update(self.window, self.player.x, self.player.y, self.levelID)

			""" -- Update Item Class -- """
			self.items.update(self.window, self.player.x, self.player.y, self.levelID)

			""" -- Update Camera and Center Cam Class -- """
			self.centerCam.update(self.player.x, self.player.y, self.camera.x, self.camera.y,self. window)
			self.camera = Camera(self.centerCam.x, self.centerCam.y)
			self.camera.update(self.centerCam.x, self.centerCam.y, self.window)

			""" -- Update HUD Class -- """
			self.hud = Hud(self.player.health, self.player.stamina, self.player.lives)

		if state == self.gamestate.pause:
			""" -- Update HUD Class -- """
			self.hud = Hud(self.player.health, self.player.stamina, self.player.lives)


	def render(self, state):

		if state == self.gamestate.running:
			""" -- Render World -- """
			self.world.render(self.window, self.camera.x, self.camera.y, self.level.level)

			""" -- Render Mobs -- """
			self.mobs.render(self.window, self.camera.x, self.camera.y, self.levelID)

			""" -- Render NPC's -- """
			self.npc.render(self.window, self.player.x, self.player.y, self.camera.x, self.camera.y, self.levelID)

			""" -- Render Player -- """
			self.player.render(self.window, self.camera.x, self.camera.y)

			""" -- Render Items -- """
			self.items.render(self.window, self.camera.x, self.camera.y, self.levelID)

			""" -- Render Text -- """
			self.npc.renderText(self.window)

			""" -- Render HUD -- """
			self.hud.render(self.window, FPS, self.clock, RUNNING)

		if state == self.gamestate.pause:
			""" -- Render HUD -- """
			self.hud.render(self.window, FPS, self.clock, PAUSE)

	def debug(self):
		print "attacking =",self.mobs.attacking, "blocking =",self.mobs.blocking

Main()

# def main():
#     for x in range(10000):
#         pass

# import cProfile as profile
# profile.run('Main()')