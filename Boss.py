import pygame
import random
import constants
from bullet import *
class Boss(pygame.sprite.Sprite):
	image = None 
	def __init__(self,x,y): 
		if Boss.image is None:
	 		Boss.image = pygame.image.load("assets/boss.png")
	 	self.image = Boss.image
		self.moving_down = False 
	 	self.rect = self.image.get_rect()
		self.speed =  3
		self.x = x
		self.y = y
		self.rect.topleft = (self.x, self.y) 
		self.width = 240
		self.height = 180
		self.num_pixels_down = 0
		# direction  = 1 : going right
		# direction  = -1 : going left
		self.direction = 1
	def move_up(self):
		if self.y - self.speed < 0:
			self.y = 0
		else:
			self.y = self.y - self.speed
		self.rect.topleft = (self.x, self.y) 

	def move_down(self):
		self.num_pixels_down = self.num_pixels_down + self.speed
		if self.y + self.speed > constants.SCREEN_HEIGHT - self.height:
			self.y = constants.SCREEN_HEIGHT - self.height
		else:
			self.y = self.y + self.speed
		self.rect.topleft = (self.x, self.y) 

	def move_left(self):
		if self.x - self.speed < 0:
			self.x = 0
		else:
			self.x = self.x - self.speed
		self.rect.topleft = (self.x, self.y) 

	def move_right(self):
		if self.x + self.speed > constants.SCREEN_WIDTH - self.width:
			self.x = constants.SCREEN_WIDTH - self.width
		else:
			self.x = self.x + self.speed
		self.rect.topleft = (self.x, self.y)

	def update(self):
		if self.x == constants.SCREEN_WIDTH - self.width:
			 self.direction = -1
			 self.moving_down = True

		elif self.x == 0:
			self.direction = 1
			self.moving_down = True

		##CHnge thiS IF YOU CHNge spedd
		if self.num_pixels_down == 108:
			self.num_pixels_down = 0
			self.moving_down = False

		if self.moving_down == False:
			if self.direction == -1:
				self.move_left()
			if self.direction == 1:
				self.move_right()		
		else: 
			self.move_down()

		if random.randint(1,20) == 1:
			return self.shoot()


	def reverse_direction(self):
   		self.direction = self.direction * -1

	def shoot (self): 
		return bullet(self.x + self.width/2 - constants.A_BULLET_WIDTH/2 ,self.y, constants.ALIEN_BULLET)