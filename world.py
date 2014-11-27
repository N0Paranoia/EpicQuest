import pygame
from pygame.locals import *
from constants import *
from level import *

class World(object):

  def __init__(self):
    """ -- Load Tilesheet -- """
    self.tileSheet = pygame.image.load(TILE_PATH)
    """ -- Create Surface to draw tiles on -- """
    self.TileSurface = pygame.Surface((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE)).convert()

  def generateTileMap(self, window, rangeX, rangeY):
    self.TileSurface.blit(self.tileSheet,(0,0))
    for row in range (MAPHEIGHT):
      for column in range (MAPWIDTH):
        if column * TILESIZE > rangeX - TILESIZE and column * TILESIZE < rangeX + WINDOW_WIDTH and row * TILESIZE > rangeY - TILESIZE and row * TILESIZE < rangeY + WINDOW_HEIGHT:
          """ -- for tiles that doesn't have to be drawn -- """
          if level[row][column] > 1:
            self.initializeTiles(column*TILESIZE - rangeX, row*TILESIZE - rangeY, textures[level[row][column]])
            self.renderTiles(window)

  def initializeTiles(self, x, y, textures):
    self.x = x
    self.y = y
    self.textures = textures

  def renderTiles(self, window):
    """ -- Blit textures on the surface -- """
    window.blit(self.TileSurface, (self.x, self.y),(self.textures))

  def update(self, window, rangeX, rangeY):
    self.generateTileMap(window, rangeX, rangeY)

""" -- Tile Position for the collision class -- """
class Tile(object):

    def __init__(self, x, y):
      self.x = x
      self.y = y
