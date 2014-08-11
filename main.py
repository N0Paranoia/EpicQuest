import pygame
from player import *
from constants import *
from tilemap import *
from level import *
from camera import *
from hud import *
from gamestates import *

from pygame.locals import *


pygame.init()

class Main(object):

	def __init__(self):
		screenSize = (WINDOW_WIDTH, WINDOW_HEIGHT)
		window = pygame.display.set_mode(screenSize)
		pygame.display.set_caption("EpicQuest")

		clock = pygame.time.Clock()

		player = Player(PLAYER_START_X, PLAYER_START_Y)
		camera = Camera(0,0)
		centerCam = CenterCamera()
		gamestate = GameStates()

		Run = True
		while Run:

			print gamestate.gameOver

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
							gamestate.mainMenu = False
						

			if gamestate.mainMenu:					
				hud = Hud(0, None)
	 			pygame.draw.rect(window, WHITE, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
	 			hud.update(window, FPS, clock, MAIN_MENU)

	 			# -- Update Screen

	 			pygame.display.flip()

				
			# -- Running game State
			if gamestate.running == True:
				# gamestate.mainMenu = False
			
				if gamestate.pause == False:
			
					# -- Draw tilemap -- only inside camera rectangele

					for row in range(MAPHEIGHT):
						for column in range (MAPWIDTH):
							if column * TILESIZE > camera.x - TILESIZE and column * TILESIZE < camera.x + WINDOW_WIDTH and row * TILESIZE > camera.y -TILESIZE and row * TILESIZE < camera.y + WINDOW_HEIGHT:
								tile = Tile(column*TILESIZE - camera.x, row*TILESIZE - camera.y, colors[tilemap[row][column]])
								tile.render(window)
					
					# -- Handle player events

					player.update(event, window, camera.x, camera.y, GRAVITY)

					# -- Camera

					centerCam.update(player.x, player.y, camera.x, camera.y, window)
					camera = Camera(centerCam.x, centerCam.y)
					camera.update(centerCam.x, centerCam.y, window)

					# -- Set FPS

					clock.tick(FPS)

					# -- Hud

					hud = Hud(player.health, player.lives)
					hud.update(window, FPS, clock, RUNNING)

		 			# -- Update Screen

		 			pygame.display.flip()

		 	# -- Pause Game State

	 		if gamestate.pause:
	 			hud = Hud(player.health, player.lives)
				hud.update(window, FPS, clock, PAUSE)

				# -- Update Screen

	 			pygame.display.flip()

	 		# -- GameOver Game State

	 		if gamestate.gameOver:
	 			hud = Hud(0, None)

	 			gamestate.running = False
	 			pygame.draw.rect(window, BLACK, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
	 			hud.update(window, FPS, clock, GAME_OVER)

	 			# -- Update Screen

	 			pygame.display.flip()

Main()