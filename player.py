import pygame
from pygame.locals import *
from constants import *
from collision import *
from doors import *
from camera import *

class Player(object):

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z # z coordinate is level
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
		self.jump_height = 6
		self.jump_count = 0
		self.canJump = True
		self.is_jumping = False
		self.is_climbing = False
		self.canGoTroughDoor = True

		self.attack_count = 0
		self.attack_duration = 8

		self.frameCounter = 0
		self.frameSpeed = 6
		self.frameSwitch = 60

		self.frameHor = 0
		self.frameVert = 0
		self.frameRightIdelX = 9*self.width
		self.frameLeftIdelX = 8*self.width
		self.frameIdelY = 0
		self.frameRightStartX = 10*self.width
		self.frameLeftStartX = 7*self.width
		self.frameStartY = 0
		self.frameAnimation = self.width
		self.frameRightEnd = 17*self.width
		self.frameLeftEnd = 0
		self.spriteSheet = pygame.image.load(SPRITE_PATH).convert_alpha()
		self.rightFrame = True
		self.leftFrame = False

		self.haveSword = False
		self.haveShield = False

		self.damage = 5


		self.LEFT = False
		self.RIGHT = False
		self.UP = False
		self.DOWN = False
		self.JUMP = False
		self.ATTACK = False
		self.BLOCK = False

		self.collision = Collision()

	def controls(self, tileMap):
		keys = pygame.key.get_pressed()

		if keys[K_a]:
			self.LEFT = True
			self.RIGHT = False
		else:
			self.LEFT = False
		if keys[K_d]:
			self.RIGHT = True
			self.LEFT = False
		else:
			self.RIGHT = False
		if keys[K_w]:
			self.UP = True
		else:
			self.UP = False
		if keys[K_s]:
			self.DOWN = True
		else:
			self.DOWN = False
		if keys[K_l]:
			self.ATTACK = True
		else:
			self.ATTACK = False
		if keys[K_k]:
			self.BLOCK = True
		else:
			self.BLOCK = False

		if keys[K_SPACE]:
			if self.is_falling == False:
				self.JUMP = True
			else:
				self.JUMP = False
		else:
			self.JUMP = False

		
	def falling(self, gravity, tileMap):

		self.is_falling = True
		self.y += gravity
		if self.y < 0 or self.y + self.height > LEVEL_HEIGHT*TILESIZE or self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, WALL, tileMap) == True or self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, LADDER_TOP, tileMap) == True or self.collision.CloudCollision(self.x, self.y, self.width, self.height, self.x, self.y, PLATFORM, tileMap) == True or self.is_climbing == True:
			self.y -= gravity
			self.is_falling = False

		""" -- Gravity function for sloped tiles "y1 = y + (x1 - x)" -- """
		if self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_LEFT, tileMap):
			if self.y ==  (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - ((self.x+TILESIZE) - (((self.x-1+TILESIZE)/TILESIZE)*TILESIZE)) + self.speed:
				self.y -= gravity
				self.is_falling = False

		if self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_RIGHT, tileMap):
			if self.y == (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - (TILESIZE - (self.x - ((self.x/TILESIZE)*TILESIZE))) + self.speed:
				self.y -= gravity
				self.is_falling = False

	def attack(self, mobsX, mobsY, pickedUpSword):
		self.swordX = -10
		self.swordY = -10
		self.swordW  = 0
		self.swordH = 0
		if pickedUpSword == True:
			if self.canAttack:
				if self.ATTACK:
					self.is_attacking = True
					self.canBlock = False
					if self.attack_count <= self.attack_duration:
						self.stamina -= 10
						self.swordW  = TILESIZE
						self.swordH = TILESIZE/4
						self.attack_count += 1
						if self.rightFrame:
							self.swordX = self.x + TILESIZE
							self.swordY = self.y + TILESIZE
						elif self.leftFrame:
							self.swordX = self.x - TILESIZE
							self.swordY = self.y + TILESIZE
				else:
					self.attack_count = 0
					self.is_attacking = False;

	def block(self, mobsX, mobsY, pickedUpShield):
		self.shieldX = -10
		self.shieldY = -10
		self.shieldW = 0
		self.shieldH = 0
		if pickedUpShield == True:
			if self.canBlock:
				if self.BLOCK:
					self.is_blocking = True
					self.shieldW  = TILESIZE/4
					self.shieldH = TILESIZE
					if self.rightFrame:
						self.shieldX = self.x + TILESIZE
						self.shieldY = self.y + TILESIZE/2
					elif self.leftFrame:
						self.shieldX = self.x - self.shieldW
						self.shieldY = self.y + TILESIZE/2
					if self.shieldHit:
						self.stamina -= 15
				else:
					self.is_blocking = False

	def jump(self):
		if self.canJump:
			if self.JUMP:
				self.is_jumping = True
				self.jump_speed = 6
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

	def climbing(self, tileMap):
		if self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, LADDER, tileMap) == True or self.collision.TileCollision(self.x, self.y, self.width, self.height,
			self.x, self.y, LADDER_TOP, tileMap) == True:
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

	def gotroughdoor(self, tileMap):
		door = Doors()
		if self.UP:
			if self.canGoTroughDoor:
				if self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, DOOR, tileMap) == True:
					self.x, self.y, self.z = door.doorConnections(self.x, self.y, self.z)
					self.canGoTroughDoor = False
					self.UP = False
		else:
			self.canGoTroughDoor = True

	def playerHealth(self, mobsX, mobsY, mobsW, mobsH, mobAlive, mobsWeaponX, mobsWeaponY, mobsWeaponW, mobsWeaponH, mobsAttacking, tileMap):
		if self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, LAVA, tileMap):
			self.health -= 5
		if self.MobCollision(self.x, self.y, self.width, self.height, mobsX, mobsY, mobsW, mobsH, mobAlive, mobsWeaponX, mobsWeaponY, mobsWeaponW, mobsWeaponH, mobsAttacking):
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

	def MobCollision(self, x, y, w, h, mobsX, mobsY, mobsW, mobsH, mobAlive, mobsWeaponX, mobsWeaponY, mobsWeaponW, mobsWeaponH, mobsAttacking):
		self.knockBackLeft = 0
		self.knockBackRight = 1
		self.knockBackUp = 2
		self.knockBackDown = 3
		self.shieldHit = False
		for mobs in range(MOB_NUMBER):
			if mobAlive[mobs]:
				""" -- Check if the Mob weapon hits the player shield -- """
				if self.shieldX > 0 or self.shieldY > 0:
					if self.collision.VarCollision(self.shieldX, self.shieldY, self.shieldW, self.shieldH, mobsWeaponX[mobs], mobsWeaponY[mobs], mobsWeaponW[mobs], mobsWeaponH[mobs]):
						if self.x < mobsX[mobs]:
							self.knockBack(self.knockBackLeft)
						if self.x > mobsX[mobs]:
							self.knockBack(self.knockBackRight)
						if self.y < mobsY[mobs]:
							self.knockBack(self.knockBackUp)
						if self.y > mobsY[mobs]:
							self.knockBack(self.knockBackDown)
						self.shieldHit = True
						return False

				""" -- Check if the mob hits the player -- """
				if self.collision.VarCollision(x, y, w, h, mobsX[mobs], mobsY[mobs],  mobsW, mobsH):
					if self.x < mobsX[mobs]:
						self.knockBack(self.knockBackLeft)
					if self.x > mobsX[mobs]:
						self.knockBack(self.knockBackRight)
					if self.y < mobsY[mobs]:
						self.knockBack(self.knockBackUp)
					if self.y > mobsY[mobs]:
						self.knockBack(self.knockBackDown)
					return True

				""" -- Check id the mob's weapon hits the player -- """
				if mobsAttacking[mobs]:
					if self.collision.VarCollision(x, y, w, h, mobsWeaponX[mobs], mobsWeaponY[mobs], mobsWeaponW[mobs], mobsWeaponH[mobs]):
						if self.x < mobsX[mobs]:
							self.knockBack(self.knockBackLeft)
						if self.x > mobsX[mobs]:
							self.knockBack(self.knockBackRight)
						if self.y < mobsY[mobs]:
							self.knockBack(self.knockBackUp)
						if self.y > mobsY[mobs]:
							self.knockBack(self.knockBackDown)
						return True

				""" -- Check if the mob is hitting the shield -- """
				if self.shieldX > 0 or self.shieldY > 0:
					if self.collision.VarCollision(self.shieldX, self.shieldY, self.shieldW, self.shieldH, mobsX[mobs], mobsY[mobs],  mobsW, mobsH):
						self.shieldHit = True
						return False

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

	def move(self, tileMap):
		if self.is_attacking == False:

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
			if self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, WALL, tileMap) == True:
				self.x -= self.velocity_x

			""" -- X Move (collision) function for sloped tiles "y1 = y + (x1 - x)"" -- """
			if self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_LEFT, tileMap):
				if not self.JUMP:
					if self.y is not (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - ((self.x +TILESIZE) - (((self.x-1+TILESIZE)/TILESIZE)*TILESIZE)):
						self.y = (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - ((self.x + TILESIZE) - (((self.x-1+TILESIZE)/TILESIZE)*TILESIZE))- self.velocity_x

			if self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_RIGHT, tileMap):
				if not self.JUMP:
					if self.y is not (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - (TILESIZE - (self.x - ((self.x/TILESIZE)*TILESIZE))):
						self.y = (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - (TILESIZE - (self.x - ((self.x/TILESIZE)*TILESIZE)))

			self.y += self.velocity_y
			if self.y < 0 or self.y + self.height > LEVEL_HEIGHT*TILESIZE or self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, WALL, tileMap) == True:
				self.y -= self.velocity_y

			""" -- Y Move (collision) function for sloped tiles "y1 = y + (x1 - x)"" -- """
			if self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_LEFT, tileMap):
				if self.y == (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - ((self.x-1+TILESIZE) - (((self.x-1+TILESIZE)/TILESIZE)*TILESIZE)):
					self.y -= self.velocity_y

			if self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, SLOPE_RIGHT, tileMap):
				if self.y == (((self.y-1+TILESIZE)/TILESIZE)*TILESIZE) - (TILESIZE - (self.x - ((self.x/TILESIZE)*TILESIZE))):
					self.y -= self.velocity_y

			self.y += self.velocity_j
			if self.y < 0 or self.y + self.height > LEVEL_HEIGHT*TILESIZE or self.collision.TileCollision(self.x, self.y, self.width, self.height, self.x, self.y, WALL, tileMap) == True:
				self.y -= self.velocity_j

	def animate(self):

		self.frameCounter += self.frameSpeed
		if self.frameCounter > self.frameSwitch:
			# """ -- Attck animation -- """
			if self.is_attacking :
				if self.leftFrame:
					self.frameHor = 8*self.width
				elif self.rightFrame:
					self.frameHor = 9*self.width
				self.frameVert = self.height
			# """ -- Block Animation -- """
			elif self.is_blocking:
				if self.rightFrame:
					self.frameHor = 10*self.width
				elif self.leftFrame:
					self.frameHor = 7*self.width
				self.frameVert = self.height
			# """ -- Walking Animation -- """
			elif self.RIGHT:
				self.frameHor += self.frameAnimation
				if self.frameHor > self.frameRightEnd or self.frameHor < self.frameRightStartX :
					self.frameHor = self.frameRightStartX
				self.frameCounter = 0
				self.leftFrame = False
				self.rightFrame = True
				self.frameVert = self.frameIdelY
			elif self.LEFT:
				self.frameHor -= self.frameAnimation
				if self.frameHor < self.frameLeftEnd or self.frameHor > self.frameLeftStartX:
					self.frameHor = self.frameLeftStartX
				self.frameCounter = 0
				self.rightFrame = False
				self.leftFrame = True
				self.frameVert = self.frameIdelY
			# """ -- Idle animation -- """
			else:
				if self.rightFrame:
					self.frameHor = self.frameRightIdelX
				elif self.leftFrame:
					self.frameHor = self.frameLeftIdelX
				self.frameVert = self.frameIdelY

		self.rect = pygame.Rect((self.frameHor, self.frameVert),(self.frameHor+self.width, self.frameVert+self.height))

		self.spriteSurface = pygame.Surface((self.rect.size), pygame.SRCALPHA)
		self.spriteSurface.blit(self.spriteSheet,(0,0))

	def render(self, window, camX, camY):
		window.blit(self.spriteSurface, (self.x - camX, self.y - camY), self.rect)
		pygame.draw.rect(window, RED, (self.swordX - camX, self.swordY - camY, self.swordW, self.swordH), 1)
		pygame.draw.rect(window, BLUE, (self.shieldX - camX, self.shieldY - camY, self.shieldW, self.shieldH), 1)

	def update (self, event, window, camX, camY, gravity, mobsX, mobsY, mobsW, mobsH, mobAlive, mobsWeaponX, mobsWeaponY, mobsWeaponW, mobsWeaponH, mobsAttacking, tileMap, pickedUpSword, pickedUpShield):
		self.falling(gravity, tileMap)
		self.jump()
		self.climbing(tileMap)
		self.gotroughdoor(tileMap)
		self.move(tileMap)
		self.attack(mobsX, mobsY, pickedUpSword)
		self.block(mobsX, mobsY, pickedUpShield)
		self.playerStamina()
		self.playerHealth(mobsX, mobsY, mobsW, mobsH, mobAlive, mobsWeaponX, mobsWeaponY, mobsWeaponW, mobsWeaponH, mobsAttacking, tileMap)
		self.animate()