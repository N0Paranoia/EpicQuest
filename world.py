import pygame
from pygame.locals import *
from constants import *
from level import *

class World(object):

  def __init__(self):
    self.TILERECT = pygame.Rect((0,0),(TILESIZE,TILESIZE))
    self.TileSurface = pygame.Surface(self.TILERECT.size).convert()

  def generateTileMap(self, window, camX, camY):
    for row in range(MAPHEIGHT):
      for column in range (MAPWIDTH):
        if column * TILESIZE > camX - TILESIZE and column * TILESIZE < camX + WINDOW_WIDTH and row * TILESIZE > camY - TILESIZE and row * TILESIZE < camY + WINDOW_HEIGHT:
          tilePos = Tile(column*TILESIZE - camX, row*TILESIZE - camY)
          tile = self.initializeTiles(column*TILESIZE - camX, row*TILESIZE - camY, textures[tilemap[row][column]])
          self.renderTiles(window)

  def initializeTiles(self, x, y, textures):
    self.x = x
    self.y = y
    self.textures = textures

    self.TileSurface.blit(TILE_SHEET,(0,0),(textures))

  def renderTiles(self, window):
    window.blit(self.TileSurface, (self.x, self.y), self.TILERECT)

  def update(self, window, camX, camY):
    self.generateTileMap(window, camX, camY)

 # -- Tile Possion for the collision class
class Tile(object):

    def __init__(self, x, y):
      self.x = x
      self.y = y
