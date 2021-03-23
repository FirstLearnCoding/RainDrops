import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen=ai_game.screen
		self.screen_rect=ai_game.screen_rect
		self.image=pygame.image.load('drop.bmp')
		self.rect=self.image.get_rect()
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height

		self.x=float(self.rect.x)
		self.y=float(self.rect.y)
		self.drop_speed=10
		self.fleet_direction=1
		self.rain_speed=1.0
	
	def update(self):
		if self.status():
			self.reset()
	def reset(self):
		self.y=self.rect.height
	def status(self):
		
		if self.rect.y>self.screen_rect.bottom:
			print("hello")
			return True
