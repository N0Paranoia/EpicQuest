import pygame
from player import *
from constants import *
from tilemap import *
from level import *
from camera import *
from hud import *
from engine import *

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
		engine = Engine()

		# -- Define games states
		running = True
		pause = False
		 
		while running:
	
			for event in pygame.event.get():
				if event.type == QUIT:
					running = False

				if event.type == KEYDOWN:
					if event.key == K_q: 
						running = False
					if event.key == K_p:
						pause = not pause


			if pause == False:
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
			
Main()