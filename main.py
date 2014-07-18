import pygame
from player import *
from constants import *
from tilemap import *
from level import *
from camera import *
from pygame.locals import *


pygame.init()

class Main(object):

	def __init__(self):
		screenSize = (WINDOW_WIDTH, WINDOW_HEIGHT)
		window = pygame.display.set_mode(screenSize)
		pygame.display.set_caption("EpicQuest")
		clock = pygame.time.Clock()

		font = pygame.font.SysFont('consolas', 12)
			
		textControl = font.render("use [ASWD] to move", 1, (255, 255, 255))

		player = Player(WINDOW_WIDTH/2 - TILESIZE/2,WINDOW_HEIGHT/2 - TILESIZE/2)
		camera = Camera(0,0)
		
		running = True

		while running:
	
			for event in pygame.event.get():
				if event.type == QUIT:
					running = False

				if event.type == KEYDOWN:
					if event.key == K_q:
						running = False
			

			window.fill((BLACK))

			# -- Draw tilemap

			for row in range(MAPHEIGHT):
				for column in range (MAPWIDTH):
					tile = Tile(column*TILESIZE - camera.x, row*TILESIZE - camera.y, colors[tilemap[row][column]])
					tile.render(window)
			
			# -- Handle player events

			player.input(event)
			player.update(GRAVITY, camera.x, camera.y)
			player.move()
			player.render(window, camera.x, camera.y)

			# -- Camera

			camera = Camera(player.x, player.y)
			camera.update(player.x, player.y)
			camera.render(window)
			
			# -- Set FPS

			clock.tick(FPS)

			# -- Debug info
			
			textFPS = font.render("FPS = " + str(clock.get_fps()), 1, (255, 255, 255))
			window.blit(textFPS, (0, 0))
 			window.blit(textControl, (0, 32))

 			# -- Update Screen

			pygame.display.flip()
			
Main()