import pygame
import constants
from bullet import *
class Spaceship(pygame.sprite.Sprite):
	image = None
	def __init__(self):
		if Spaceship.image is None:
	 		Spaceship.image = pygame.image.load("assets/Galaga2.png")
	 	self.image = Spaceship.image

	 	self.rect = self.image.get_rect()
		self.speed =  10
		self.x = 400
		self.y = 260
		self.rect.topleft = (self.x, self.y) 
		self.width = 60
		self.height = 80
	def move_up(self):
		print self.y, constants.BARRIER
		if self.y >= constants.BARRIER:
			if self.y - self.speed < 0:
				self.y = 0
			else:
				self.y = self.y - self.speed
			self.rect.topleft = (self.x, self.y) 

	def move_down(self):
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

	def shoot (self): 
		return bullet(self.x + self.width/2 - constants.SS_BULLET_WIDTH/2 ,self.y, constants.SPACESHIP_BULLET)