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

# -- tiles
RED_TILES = (0,32)

# -- Tile(map) constants
TILESIZE = 32
MAPWIDTH = 22
MAPHEIGHT = 16 

SKY = 0
WALL = 1
GRASS = 2
WATER = 3
LAVA = 4
LADDER = 5
LADDER_TOP = 6
PLATFORM = 7
DOOR = 8




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
textures =	{
				SKY : WHITE,
				WALL : BLACK,
				GRASS : GREEN,
				WATER : BLUE,
				LAVA : pygame.image.load("./art/tileSheet.png"),
				LADDER : CYAN,
				LADDER_TOP : LIGHT_BLUE,
				PLATFORM : MAGENTA,
				DOOR : LIGHT_GRAY
			}

# -- Mob types

MOB_SIMPLE = 0