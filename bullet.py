import pygame
import constants 
class bullet(pygame.sprite.Sprite):
	image = None
	def __init__(self,x,y, bullet_type):
		if bullet_type == constants.SPACESHIP_BULLET:
			bullet.image = pygame.image.load("assets/ss_bullet2.png")
		else:
			bullet.image = pygame.image.load("assets/a_bullet.png")
		self.image = bullet.image
		self.rect = self.image.get_rect()
		if bullet_type == constants.ALIEN_BULLET:
			self.speed = constants.A_BULLET_SPEED
			self.width = constants.A_BULLET_WIDTH
			self.height = constants.A_BULLET_HEIGHT
		if bullet_type == constants.SPACESHIP_BULLET:  
			self.speed = constants.SS_BULLET_SPEED
			self.width = constants.SS_BULLET_WIDTH
			self.height = constants.SS_BULLET_HEIGHT		
		self.x = x
		self.y = y
		self.bullet_type = bullet_type 
		self.rect.topleft = (self.x, self.y)
	def move (self):
		if self.bullet_type == constants.ALIEN_BULLET:
			self.y = self.y + self.speed
		if self.bullet_type == constants.SPACESHIP_BULLET:
			self.y = self.y - self.speed 
		self.rect.topleft = (self.x, self.y)

	def is_offscreen(self):
		if self.y < -10 or self.y > constants.SCREEN_HEIGHT + 20:
			return True