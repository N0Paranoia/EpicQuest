import pygame

# -- Window Settings
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# -- Player Starting point
PLAYER_START_X = 32
PLAYER_START_Y = 32
PLAYER_SPEED = 4
PLAYER_HEIGHT = 32
PLAYER_WIDTH = 32

# -- Define gamestates
INTRO = 0
MAIN_MENU = 1
RUNNING = 2
PAUSE = 8
GAME_OVER = 9

FONT_PATH = './fonts/Grand9K Pixel.ttf'
SPRITE_PATH = './art/spriteSheet.png'
TILE_PATH = './art/tileSheet.png'

TILE_SHEET = pygame.image.load(TILE_PATH)

#  -- Physics
FPS = 60
GRAVITY = 4

# -- Colors
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

# -- Tile(map) constants

TILESIZE = 32
MAPWIDTH = 22
MAPHEIGHT = 16

# -- tiles
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

SKY = 0
WALL = 1
GRASS = 2
WATER = 3
LAVA = 4
LADDER = 5
LADDER_TOP = 6
PLATFORM = 7
DOOR = 8


TILERECT = pygame.Rect((0,0),(TILESIZE,TILESIZE))

# -- Linking recources/ colors
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

# -- Linking telesheet and numbers
textures_test =	{
				SKY : pygame.image.load(TILE_PATH),
				WALL : pygame.image.load(TILE_PATH),
				GRASS : pygame.image.load(TILE_PATH),
				WATER : pygame.image.load(TILE_PATH),
				LAVA : pygame.image.load(TILE_PATH),
				LADDER : pygame.image.load(TILE_PATH),
				LADDER_TOP : pygame.image.load(TILE_PATH),
				PLATFORM : pygame.image.load(TILE_PATH),
				DOOR : pygame.image.load(TILE_PATH)
			}

textures =	{
				SKY : WHITE_TILE,
				WALL : BLACK_TILE,
				GRASS : GREEN_TILE,
				WATER : BLUE_TILE,
				LAVA : RED_TILE,
				LADDER : CYAN_TILE,
				LADDER_TOP : LIGHT_BLUE_TILE,
				PLATFORM : MAGENTA_TILE,
				DOOR : LIGHT_GRAY_TILE
			}

# -- Mob types

MOB_SIMPLE = 0
