import pygame

""" -- Window Settings -- """
WINDOW_WIDTH = 854
WINDOW_HEIGHT = 480

""" -- Player Starting point -- """
PLAYER_START_X = 32
PLAYER_START_Y = 32
PLAYER_SPEED = 4
PLAYER_HEIGHT = 64
PLAYER_WIDTH = 32

""" -- Define gamestates -- """
INTRO = 0
MAIN_MENU = 1
RUNNING = 2
PAUSE = 8
GAME_OVER = 9

""" -- Define levels -- """
# FIRST_LEVEL = 1


FONT_PATH = './fonts/Grand9K Pixel.ttf'
SPRITE_PATH = './art/spriteSheet.png'
TILE_PATH = './art/tileSheet.png'

#  -- Physics -- """
FPS = 120
GRAVITY = 4

""" -- Colors -- """
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
LIGHT_BLUE = (0,200,255)
MAGENTA = (255,0,255)
GRAY = (100,100,100)
LIGHT_GRAY = (200, 200, 200)
SKY_BLUE = (140, 190, 214)

""" -- Tile(map) constants -- """
TILESIZE = 32
MAPWIDTH = 30
MAPHEIGHT = 30

""" -- tile Sheet -- """
NO_TILE = (-TILESIZE, -TILESIZE, TILESIZE, TILESIZE)
WHITE_TILE = (0, 0, TILESIZE, TILESIZE)
BLACK_TILE = (32, 0, TILESIZE, TILESIZE)
GRAY_TILE = (64, 0, TILESIZE, TILESIZE)
LIGHT_GRAY_TILE = (96, 0, TILESIZE, TILESIZE)
RED_TILE = (0, 32, TILESIZE, TILESIZE)
GREEN_TILE = (32, 32, TILESIZE, TILESIZE)
BLUE_TILE = (64, 32, TILESIZE, TILESIZE)
YELLOW_TILE = (0, 64, TILESIZE, TILESIZE)
MAGENTA_TILE = (32, 64, TILESIZE, TILESIZE)
CYAN_TILE = (64, 64, TILESIZE, TILESIZE)
LIGHT_BLUE_TILE = (96, 64, TILESIZE, TILESIZE)
SLOPE_TILE_RIGHT = (0, 96, TILESIZE, TILESIZE)
SLOPE_TILE_LEFT = (32, 96, TILESIZE, TILESIZE)

CLEAR = 0
SKY = 1
WALL = 2
WOOD = 3
DOOR = 4
LAVA = 5
GRASS = 6
WATER = 7
PLATFORM = 10
LADDER = 11
LADDER_TOP = 12
SLOPE_RIGHT = 13
SLOPE_LEFT = 14

""" -- Linking recources/ colors -- (can be deleted) -- """
colors = {
			SKY : WHITE,
			WALL : BLACK,
			GRASS : GREEN,
			WATER : BLUE,
			LAVA : RED,
			LADDER : CYAN,
			LADDER_TOP : LIGHT_BLUE,
			PLATFORM : MAGENTA,
			DOOR : LIGHT_GRAY
		 }

""" -- Linking telesheet and numbers -- """
textures =	{
				CLEAR : NO_TILE,
				SKY : WHITE_TILE,
				WALL : BLACK_TILE,
				GRASS : GREEN_TILE,
				WATER : BLUE_TILE,
				LAVA : RED_TILE,
				LADDER : CYAN_TILE,
				LADDER_TOP : LIGHT_BLUE_TILE,
				PLATFORM : MAGENTA_TILE,
				DOOR : LIGHT_GRAY_TILE,
				WOOD : GRAY_TILE,
				SLOPE_RIGHT : SLOPE_TILE_RIGHT,
				SLOPE_LEFT : SLOPE_TILE_LEFT
			}

""" -- Mob types -- """

MOB_NUMBER = 2
