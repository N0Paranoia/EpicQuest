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

		self.player = Player(PLAYER_START_X, PLAYER_START_Y, 1)
		self.npc = Npc()
		self.items = Items()
		self.mobs = Mobs()
		self.camera = Camera(0,0)
		self.centerCam = CenterCamera()
		self.gamestate = GameStates()
		self.world = World()
		self.levelStates = LevelStates()

		""" -- Variables to implement frame delays -- """
		self.startFrame = 0
		self.delayFrame = 1

		self.run = True
		while self.run:

			self.gamestate.changestate(self.player.lives)

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
							""" -- Reset Game values -- """
							self.player = Player(PLAYER_START_X, PLAYER_START_Y, 1)
							self.npc = Npc()
							self.items = Items()
							self.mobs = Mobs()
							self.world = World()
							self.levelStates = LevelStates()
							self.gamestate.mainMenu = True

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
				self.gamestate.intro = False
				self.gamestate.gameOver = False

				self.hud = Hud(0, None, None)
				pygame.draw.rect(self.window, WHITE, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
				self.hud.update(self.window, FPS, self.clock, MAIN_MENU)

			""" -- Running game State -- """
			if self.gamestate.running == True:

				self.gamestate.mainMenu = False

				if self.gamestate.pause == False:
					self.window.fill ((SKY_BLUE))
					
					self.input()
					self.update()
					self.render() 

					self.debug()
				

			""" -- Pause Game State -- """
			if self.gamestate.pause:
				self.hud = Hud(self.player.health, self.player.stamina, self.player.lives)
				self.hud.update(self.window, FPS, self.clock, PAUSE)

			""" -- GameOver Game State -- """
			if self.gamestate.gameOver:
				self.hud = Hud(0, None, None)
				self.gamestate.running = False
				pygame.draw.rect(self.window, BLACK, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
				self.hud.update(self.window, FPS, self.clock, GAME_OVER)

			""" -- Update Screen -- """

			pygame.display.flip()

	def input(self):
		self.player.input(self.event)
		
	def update(self):

		""" -- Set FPS -- """
		self.clock.tick(FPS)

		""" -- Set level -- """
		self.levelID = self.levelStates.changeState(self.player.z)
		self.level = Levels(self.levelID)

		""" -- Initialize world -- """
		self.world.update(self.window, self.camera.x, self.camera.y, self.level.level)

		""" -- Handle player events -- """
		self.player.update(self.event, self.window, self.camera.x, self.camera.y, GRAVITY, self.mobs.x, self.mobs.y, self.mobs.width, self.mobs.height, self.mobs.alive, self.mobs.weaponX, self.mobs.weaponY, self.mobs.weaponW, self.mobs.weaponH,self. mobs.attacking, self.level.level, self.items.pickedUpSword, self.items.pickedUpShield)

		""" -- Handle NPC Events -- """
		self.npc.update(self.window, self.camera.x, self.camera.y, self.player.x, self.player.y, self.levelID)

		""" -- Handle Item Events -- """
		self.items.update(self.window, self.camera.x, self.camera.y, self.player.x, self.player.y, self.levelID)

		""" -- Handle AI events -- """
		self.mobs.update(self.window, self.camera.x, self.camera.y, self.player.x, self.player.y, self.player.swordX, self.player.swordY, self.player.swordW, self.player.swordH, self.player.damage, self.player.shieldHit, self.player.ATTACK, self.player.BLOCK, self.levelID, self.level.level)

		""" -- Camera -- """
		self.centerCam.update(self.player.x, self.player.y, self.camera.x, self.camera.y,self. window)
		self.camera = Camera(self.centerCam.x, self.centerCam.y)
		self.camera.update(self.centerCam.x, self.centerCam.y, self.window)

		""" -- HUD -- """
		self.hud = Hud(self.player.health, self.player.stamina, self.player.lives)
		self.hud.update(self.window, FPS, self.clock, RUNNING)

	def render(self):
		self.player.render(self.window, self.camera.x, self.camera.y)

	def debug(self):
		print self.player.JUMP

Main()

# def main():
#     for x in range(10000):
#         pass

# import cProfile as profile
# profile.run('Main()')
