import pygame
import constants
import level
from player import *
from mobs import *
from world import *
from camera import *
from hud import *
from states import *
from pygame.locals import *

pygame.init()

class Main(object):

	def __init__(self):
		screenSize = (WINDOW_WIDTH, WINDOW_HEIGHT)
		window = pygame.display.set_mode(screenSize)
		pygame.display.set_caption("EpicQuest")

		clock = pygame.time.Clock()

		player = Player(PLAYER_START_X, PLAYER_START_Y)
		mobs = Mobs()
		camera = Camera(0,0)
		centerCam = CenterCamera()
		gamestate = GameStates()
		world = World()
		levelStates = LevelStates()

		""" -- Variables to implement frame delays -- """
		self.startFrame = 0
		self.delayFrame = 1

		Run = True
		while Run:

			gamestate.changestate(player.lives)

			for event in pygame.event.get():
				if event.type == QUIT:
					Run = False

				if event.type == KEYDOWN:
					if event.key == K_q:
						Run = False
					if event.key == K_p:
						gamestate.pause = not gamestate.pause

					if event.key == K_RETURN:
						if gamestate.mainMenu:
							gamestate.running = True
						elif gamestate.gameOver:
							""" -- Reset Player values -- """
							player = Player(PLAYER_START_X, PLAYER_START_Y)
							gamestate.mainMenu = True

			""" -- Intro game state -- """
			if gamestate.intro:
				for x in range(0, WINDOW_WIDTH):
					hud = Hud(0, None, None)
					pygame.draw.rect(window, WHITE, (0, WINDOW_HEIGHT - 100, x, 32))
 
					hud.update(window, FPS, clock, INTRO)

					""" -- Update Screen -- """
					pygame.display.flip()

					if x == WINDOW_WIDTH -1:
						gamestate.mainMenu = True

			""" -- Main menu game State -- """
			if gamestate.mainMenu:
				gamestate.intro = False
				gamestate.gameOver = False

				hud = Hud(0, None, None)
				pygame.draw.rect(window, WHITE, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
				hud.update(window, FPS, clock, MAIN_MENU)

			""" -- Running game State -- """
			if gamestate.running == True:

				gamestate.mainMenu = False

				if gamestate.pause == False:
					window.fill ((SKY_BLUE))
					self.startFrame += 1

					print levelStates.changeState(level)

					""" -- Initialize world -- """
					world.update(window, camera.x, camera.y, level)

					""" -- Handle player events -- """
					player.update(event, window, camera.x, camera.y, GRAVITY, mobs.x, mobs.y, mobs.width, mobs.height, mobs.alive, mobs.weaponX, mobs.weaponY, mobs.weaponW, mobs.weaponH, mobs.attacking, level)

					""" -- Handle AI events -- """
					mobs.update(window,camera.x, camera.y, player.x, player.y, player.swordX, player.swordY, player.swordW, player.swordH, player.damage, player.shieldHit, level)

					""" -- Camera -- """
					centerCam.update(player.x, player.y, camera.x, camera.y, window)
					camera = Camera(centerCam.x, centerCam.y) 
					camera.update(centerCam.x, centerCam.y, window)

					""" -- Set FPS -- """
					clock.tick(FPS)

					""" -- HUD -- """
					hud = Hud(player.health, player.stamina, player.lives)
					hud.update(window, FPS, clock, RUNNING)

					""" -- Debug info -- """

			""" -- Pause Game State -- """
			if gamestate.pause:
				hud = Hud(player.health, player.stamina, player.lives)
				hud.update(window, FPS, clock, PAUSE)

			""" -- GameOver Game State -- """
			if gamestate.gameOver:
				hud = Hud(0, None, None)

				gamestate.running = False
				pygame.draw.rect(window, BLACK, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
				hud.update(window, FPS, clock, GAME_OVER)

			""" -- Update Screen -- """
			pygame.display.flip()

Main()

# def main():
#     for x in range(10000):
#         pass
        
# import cProfile as profile
# profile.run('Main()')
