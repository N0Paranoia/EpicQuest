import pygame
from pygame.locals import *
from constants import *
from level import *

class World(object):

  def __init__(self):
    """ -- Load Tilesheet -- """
    self.tileSheet = pygame.image.load(TILE_PATH).convert()
    """ -- Create Surface to draw tiles on -- """
    self.TileSurface = pygame.Surface((LEVEL_WIDTH*TILESIZE,LEVEL_HEIGHT*TILESIZE)).convert()

  def generateTileMap(self, window, rangeX, rangeY, tileMap):
    self.TileSurface.blit(self.tileSheet,(0,0))
    for row in range (LEVEL_HEIGHT):
      for column in range (LEVEL_WIDTH):
        if column * TILESIZE > rangeX - TILESIZE and column * TILESIZE < rangeX + WINDOW_WIDTH and row * TILESIZE > rangeY - TILESIZE and row * TILESIZE < rangeY + WINDOW_HEIGHT:
          """ -- for tiles that doesn't have to be drawn -- """
          if tileMap[row][column] > 0:
            self.initializeTiles(column*TILESIZE - rangeX, row*TILESIZE - rangeY, textures[tileMap[row][column]])
            self.renderTiles(window)

  def initializeTiles(self, x, y, textures):
    self.x = x
    self.y = y
    self.textures = textures

  def renderTiles(self, window):
    """ -- Blit textures on the surface -- """
    window.blit(self.TileSurface, (self.x, self.y),(self.textures))

  def render(self, window, rangeX, rangeY, tileMap):
    self.generateTileMap(window, rangeX, rangeY, tileMap)

""" -- Tile Position for the collision class -- """
class Tile(object):

    def __init__(self, x, y):
      self.x = x
      self.y = y
