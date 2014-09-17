import pygame
from pygame.locals import *
from constants import *
from level import *
from tile import *

class World(object):

  def __init__(self):
    pass

  def generateTileMap(self, window, camX, camY):
    for row in range(MAPHEIGHT):
      for column in range (MAPWIDTH):
        if column * TILESIZE > camX - TILESIZE and column * TILESIZE < camX + WINDOW_WIDTH and row * TILESIZE > camY - TILESIZE and row * TILESIZE < camY + WINDOW_HEIGHT:
          tile = Tile(column*TILESIZE - camX, row*TILESIZE - camY, textures[tilemap[row][column]])
          tile.render(window)

  def update(self, window, camX, camY):
    self.generateTileMap(window, camX, camY)
