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
							gamestate.gameOver = False
						

			if gamestate.mainMenu:
					
	 			font = pygame.font.Font(FONT_PATH, 16)
	 			font2 = pygame.font.Font(FONT_PATH, 10)
	 			textMainMenu = font.render("Main Menu", 1, (BLACK))
	 			textMainMenu2 = font2.render("Press [Enter] to Start", 1, (BLACK))

	 			pygame.draw.rect(window, WHITE, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
	 			window.blit(textMainMenu, (WINDOW_WIDTH/2- TILESIZE, WINDOW_HEIGHT/4))
	 			window.blit(textMainMenu2, (WINDOW_WIDTH/2- 52, WINDOW_HEIGHT/4 + TILESIZE))
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
					hud.update(window, FPS, clock)

		 			# -- Update Screen

		 			pygame.display.flip()

		 	# -- Pause Game State

	 		if gamestate.pause:
	 			font = pygame.font.Font(FONT_PATH, 16)
	 			textPause = font.render("Pause", 1, (GRAY))
	 			window.blit(textPause, (WINDOW_WIDTH/2- TILESIZE, WINDOW_HEIGHT/2))
	 			pygame.display.flip()

	 		# -- GameOver Game State

	 		if gamestate.gameOver:
	 			font = pygame.font.Font(FONT_PATH, 16)
	 			font2 = pygame.font.Font(FONT_PATH, 10)
	 			textGameOver= font.render("Game Over", 1, (WHITE))
	 			textGameOver2 = font2.render("Press [q] to quit", 1, (WHITE))

	 			gamestate.running = False
	 			pygame.draw.rect(window, BLACK, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
	 			window.blit(textGameOver, (WINDOW_WIDTH/2- TILESIZE, WINDOW_HEIGHT/2))
	 			window.blit(textGameOver2, (WINDOW_WIDTH/2- TILESIZE, WINDOW_HEIGHT/2 + TILESIZE))
	 			pygame.display.flip()

Main()