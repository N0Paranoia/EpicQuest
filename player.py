import pygame
from pygame.locals import *
from constants import *
from collision import *
from doors import *
from camera import *

class Player(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = PLAYER_WIDTH
		self.height = PLAYER_HEIGHT
		self.health = 100
		self.stamina = 100
		self.lives = 3
		self.speed = PLAYER_SPEED
		self.knockBackSpeed = PLAYER_SPEED
		self.velocity_x = 0
		self.velocity_y = 0
		self.velocity_j = 4
		self.climbing_speed = 4
		self.is_attacking = False
		self.canAttack = True
		self.is_blocking = False
		self.canBlock = True
		self.jump_speed = 0
		self.jump_height = 8
		self.jump_count = 0
		self.canJump = True
		self.is_jumping = False;
		self.is_climbing = False
		self.canGoTroughDoor = True

		self.attack_count = 0
		self.attack_duration = 8

		self.frameCounter = 0
		self.frameSpeed = 6
		self.frameSwitch = 60

		self.frameHor = 0
		self.frameVert = 0
		self.frameRightIdelX = 80
		self.frameLeftIdelX = 64
		self.frameIdelY = 0
		self.frameRightStartX = 96
		self.frameLeftStartX = 48
		self.frameStartY = 0
		self.frameAnimation = PLAYER_WIDTH/2
		self.frameRightEnd = 144
		self.frameLeftEnd = 0
		self.spriteSheet = pygame.image.load(SPRITE_PATH).convert_alpha()
		self.rightFrame = True
		self.leftFrame = False

	def input(self, event):
		keys = pygame.key.get_pressed()

		self.LEFT = False
		self.RIGHT = False
		self.UP = False
		self.DOWN = False
		self.JUMP = False
		self.ATTACK = False
		self.BLOCK = False

		if keys[K_a]:
			self.LEFT = True
		if keys[K_d]:
			self.RIGHT = True
		if keys[K_w]:
			self.UP = True
		if keys[K_s]:
			self.DOWN = True
		if keys[K_l]:
			self.ATTACK = True
		if keys[K_k]:
			self.BLOCK = True
		if keys[K_SPACE]:
			if self.is_falling == False:
				self.JUMP = True

	def falling(self, gravity):
		colf = Collision()
		self.is_falling = True
		self.y += gravity
		if self.y < 0 or self.y + self.height > MAPHEIGHT*TILESIZE or colf.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, WALL) == True or colf.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, LADDER_TOP) == True or colf.CloudCollision(self.x, self.y, self.width, self.height, self.x, self.y, PLATFORM) == True or self.is_climbing == True:
			self.y -= gravity
			self.is_falling = False

		""" -- Gravity function for sloped tiles "y1 = y + (x1 - x)" -- """
		if colf.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_LEFT):
			if self.y ==  (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - ((self.x-1+TILESIZE) - (((self.x-1+TILESIZE)/TILESIZE)*TILESIZE)):
				self.y -= gravity
				self.is_falling = False

		if colf.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_RIGHT):
			if self.y == (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - (TILESIZE - (self.x - ((self.x/TILESIZE)*TILESIZE))):
				self.y -= gravity
				self.is_falling = False

	def attack(self, mobsX, mobsY):
		self.swordX = -10
		self.swordY = -10
		self.swordW  = 0
		self.swordH = 0

		if self.canAttack:
			if self.ATTACK:
				self.is_attacking = True
				if self.attack_count <= self.attack_duration:
					if self.rightFrame:
						self.swordX = self.x + TILESIZE
						self.swordY = self.y + TILESIZE
					elif self.leftFrame:
						self.swordX = self.x - TILESIZE
						self.swordY = self.y + TILESIZE
					self.stamina -= 10
					self.swordW  = 32
					self.swordH = 8
					self.attack_count += 1
					# if self.mobCollision(self.swordX, self.swordY, self.swordW, self.swordH, mobsX, mobsY):
					# 	print "KILL"
			else:
				self.attack_count = 0
				self.is_attacking = False;

	def block(self):
		if self.canBlock:
			if self.BLOCK:
				self.is_blocking = True
				self.stamina -= 5
			else:
				self.is_blocking = False

	def jump(self):
		if self.canJump:
			if self.JUMP:
				self.is_jumping = True
				self.jump_speed = 4
				self.is_climbing = False
				if self.jump_count <= self.jump_height:
					self.velocity_j = -self.jump_speed
					self.jump_count += 1
					self.is_falling = False
					self.stamina -= 10
				else:
					self.jump_speed = 0
			else:
				self.jump_count = 0
				self.jump_speed = 0
				self.is_jumping = False

	def climbing(self):
		colL = Collision()
		if colL.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, LADDER) == True or colL.TileCollision(self.x, self.y, self.width, self.height,
			self.x, self.y, LADDER_TOP) == True:
			if self.UP:
				self.is_climbing = True
				self.velocity_y = -self.climbing_speed
			elif self.DOWN:
				self.is_climbing = True
				self.velocity_y = self.climbing_speed
			else:
				self.velocity_y = 0
		else:
			self.velocity_y = 0
			self.is_climbing = False

	def gotroughdoor(self):
		colD = Collision()
		doorD = Doors()
		if self.UP:
			if self.canGoTroughDoor:
				if colD.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, DOOR) == True:
					self.x, self.y = doorD.doorConnections(self.x, self.y)
					self.canGoTroughDoor = False
					self.UP = False
		else:
			self.canGoTroughDoor = True

	def playerHealth(self, mobsX, mobsY, mobsW, mobsH, alive):
		colH = Collision()
		if colH.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, LAVA) == True :
			self.health -= 5
		if self.mobCollision(self.x, self.y, self.width, self.height, mobsX, mobsY, mobsW, mobsH, alive):
			self.health -= 25
		if self.health <= 0:
			self.x = PLAYER_START_X
			self.y = PLAYER_START_Y
			self.health = 100
			self.lives -= 1

	def playerStamina(self):
		if self.stamina <= 100:
			self.stamina += 1
		""" -- Stamina Threshold for Jumping -- """
		if self.stamina <= 50:
			if self.is_jumping == False:
				self.canJump = False
		if self.stamina <= 10:
			if self.is_attacking == False:
				self.canAttack = False
		else:
			self.canJump = True
		""" -- Stamina Threshold for Attcking -- """
		if self.stamina <= 5:
			if self.is_attacking == False:
				self.canAttack = False
		else:
			self.canAttack = True
		""" -- Stamina Threshold for Blocking -- """
		if self.stamina <= 5:
			self.canBlock = False
		else:
			self.canBlock = True

	def mobCollision(self, x, y, w, h, mobsX, mobsY, mobsW, mobsH, alive):
		self.knockBackLeft = 0
		self.knockBackRight = 1
		self.knockBackUp = 2
		self.knockBackDown = 3
		col = Collision()
		for i in range(MOB_NUMBER):
			if alive[i]:
				if col.MobCollision(x, y, w, h, mobsX[i], mobsY[i],  mobsW, mobsH):
					if self.x < mobsX[i]: 
						self.knockBack(self.knockBackLeft)
					if self.x > mobsX[i]:
						self.knockBack(self.knockBackRight)
					if self.y < mobsY[i]:
						self.knockBack(self.knockBackUp)
					if self.y > mobsY[i]:
						self.knockBack(self.knockBackDown)
					return True

	def knockBack(self, direction):
		if direction == self.knockBackLeft:
			self.velocity_x = -self.knockBackSpeed
		if direction == self.knockBackRight:
			self.velocity_x = self.knockBackSpeed
		if direction == self.knockBackUp:
			self.velocity_y = -self.knockBackSpeed
		if direction == self.knockBackDown:
			self.velocity_y = self.knockBackSpeed		

		self.x += self.velocity_x
		self.y += self.velocity_y

	def move(self, gravity):
		col = Collision()

		if self.LEFT:
			self.velocity_x = -self.speed
		elif self.RIGHT:
			self.velocity_x = self.speed
		else:
			self.velocity_x = 0

		if self.DOWN:
			self.velocity_y = self.speed

		if self.JUMP:
			self.velocity_j -= self.jump_speed
		else:
			self.velocity_j = 0

		self.x += self.velocity_x
		if self.x < 0 or self.x + self.width > MAPWIDTH*TILESIZE or col.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, WALL) == True:
			self.x -= self.velocity_x

		""" -- X Move (collision) function for sloped tiles "y1 = y + (x1 - x)"" -- """
		if col.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_LEFT):
			if not self.JUMP:
				if self.y is not (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - ((self.x-1+TILESIZE) - (((self.x-1+TILESIZE)/TILESIZE)*TILESIZE)):
					self.y = (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - ((self.x + TILESIZE) - (((self.x-1+TILESIZE)/TILESIZE)*TILESIZE)) - self.velocity_x

		if col.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_RIGHT):
			if self.y is not (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - (TILESIZE - (self.x - ((self.x/TILESIZE)*TILESIZE))):
				self.y = (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - (TILESIZE - (self.x - ((self.x/TILESIZE)*TILESIZE))) + self.velocity_x

		self.y += self.velocity_y
		if self.y < 0 or self.y + self.height > MAPHEIGHT*TILESIZE or col.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, WALL) == True:
			self.y -= self.velocity_y

		""" -- Y Move (collision) function for sloped tiles "y1 = y + (x1 - x)"" -- """
		if col.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_LEFT):
			if self.y == (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - ((self.x-1+TILESIZE) - (((self.x-1+TILESIZE)/TILESIZE)*TILESIZE)):
				self.y -= self.velocity_y

		if col.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_RIGHT):
			if self.y == (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - (TILESIZE - (self.x - ((self.x/TILESIZE)*TILESIZE))):
				self.y -= self.velocity_y

		self.y += self.velocity_j
		if self.y < 0 or self.y + self.height > MAPHEIGHT*TILESIZE or col.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, WALL) == True:
			self.y -= self.velocity_j

	def animate(self):

		self.frameCounter += self.frameSpeed
		if self.frameCounter > self.frameSwitch:
			if self.is_attacking :
				if self.leftFrame:
					self.frameHor = 80
				elif self.rightFrame:
					self.frameHor = 64
				self.frameVert = 32
			elif self.BLOCK:
				if self.rightFrame:
					self.frameHor = 96
				elif self.leftFrame:
					self.frameHor = 48
				self.frameVert = 32
			elif self.RIGHT:
				self.frameHor += self.frameAnimation
				if self.frameHor > self.frameRightEnd:
					self.frameHor = self.frameRightStartX
				self.frameCounter = 0
				self.leftFrame = False
				self.rightFrame = True
			elif self.LEFT:
				self.frameHor -= self.frameAnimation
				if self.frameHor < self.frameLeftEnd:
					self.frameHor = self.frameLeftStartX
				self.frameCounter = 0
				self.rightFrame = False
				self.leftFrame = True
			else:
				if self.rightFrame:
					self.frameHor = self.frameRightIdelX
				elif self.leftFrame:
					self.frameHor = self.frameLeftIdelX
				self.frameVert = self.frameIdelY

		self.rect = pygame.Rect((self.frameHor,self.frameVert),(self.frameHor+PLAYER_WIDTH,self.frameVert+PLAYER_HEIGHT))

		self.spriteSurface = pygame.Surface((self.rect.size), pygame.SRCALPHA)
		self.spriteSurface.blit(self.spriteSheet,(0,0),self.rect)

	def render(self, window, camX, camY):
		window.blit(self.spriteSurface, (self.x - camX, self.y - camY), self.rect)
		pygame.draw.rect(window, RED, (self.swordX - camX, self.swordY - camY, self.swordW, self.swordH), 2)

	def update (self, event, window, camX, camY, gravity, mobsX, mobsY, mobsW, mobsH, alive):
		self.input(event)
		self.falling(gravity)
		self.attack(mobsX, mobsY)
		self.block()
		self.jump()
		self.climbing()
		self.gotroughdoor()
		self.move(gravity)
		self.playerStamina()
		self.playerHealth(mobsX, mobsY, mobsW, mobsH, alive)
		self.animate()
		self.render(window, camX, camY)
