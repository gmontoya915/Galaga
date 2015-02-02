import pygame
import constants 
import random

class star(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.speed =  2
		self.x = x
		self.y = y 
		self.width = 1
		self.height = 5
	def move (self):
		self.y = self.y + self.speed 



