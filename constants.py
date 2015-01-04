import pygame

""" -- Window Settings -- """
WINDOW_WIDTH = 1280	
WINDOW_HEIGHT = 720

""" -- Player Starting point -- """
PLAYER_START_X = 64
PLAYER_START_Y = 64
PLAYER_SPEED = 4
PLAYER_HEIGHT = 128
PLAYER_WIDTH = 64

""" -- Define gamestates -- """
INTRO = 0
MAIN_MENU = 1
RUNNING = 2
PAUSE = 8
GAME_OVER = 9

""" -- Define levels -- """
# FIRST_LEVEL = 1

FONT_PATH = './fonts/Grand9K Pixel.ttf'
SPRITE_PATH = './art/spriteSheet64.png'
NPC_PATH = './art/npcSheet64.png'
MOB_PATH = './art/mobSheet64.png'
TILE_PATH = './art/tileSheet64.png'
ITEM_PATH   = './art/itemSheet64.png'

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
TILESIZE = 64

LEVEL_WIDTH = 30
LEVEL_HEIGHT = 30

""" -- tile Sheet -- """
NO_TILE = (-TILESIZE, -TILESIZE, TILESIZE, TILESIZE)
WHITE_TILE = (0, 0, TILESIZE, TILESIZE)
BLACK_TILE = (TILESIZE, 0, TILESIZE, TILESIZE)
GRAY_TILE = (2*TILESIZE, 0, TILESIZE, TILESIZE)
LIGHT_GRAY_TILE = (3*TILESIZE, 0, TILESIZE, TILESIZE)
RED_TILE = (0, TILESIZE, TILESIZE, TILESIZE)
GREEN_TILE = (TILESIZE, TILESIZE, TILESIZE, TILESIZE)
BLUE_TILE = (2*TILESIZE, TILESIZE, TILESIZE, TILESIZE)
YELLOW_TILE = (0, 2*TILESIZE, TILESIZE, TILESIZE)
MAGENTA_TILE = (TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)
CYAN_TILE = (2*TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)
LIGHT_BLUE_TILE = (3*TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)
SLOPE_TILE_RIGHT = (0, 3*TILESIZE, TILESIZE, TILESIZE)
SLOPE_TILE_LEFT = (TILESIZE, 3*TILESIZE, TILESIZE, TILESIZE)

""" -- item Sheet -- """
SWORD = ((0, 0), (TILESIZE, TILESIZE))
SHIELD  = ((TILESIZE, 0), (TILESIZE,TILESIZE))

""" -- NPC Sheet -- """
OLD_MAN = ((0, 0), (TILESIZE, 2*TILESIZE))

""" -- Mob Sheet -- """
MOB_ONE_RIGHT = ((0, 0), (TILESIZE, 2*TILESIZE))
MOB_ONE_LEFT = ((TILESIZE, 0), (TILESIZE, 2*TILESIZE))


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

SIMPLE = 5

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

MOB_NUMBER = 4
NPC_NUMBER = 2
