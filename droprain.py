import sys
import pygame
from settings import Settings
from rain import Rain


class DropRain():
	def __init__(self):
		pygame.init()
		self.settings=Settings()
		self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption('Drop Rain')
		self.screen_rect=self.screen.get_rect()
		self.rains=pygame.sprite.Group()

		self.create_fleet_rain()
		
		
		

	def run(self):
		while True:
			self.check_events()
			self.check_update_rains()
			self.update_screen()
			



	def check_events(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()

	def check_update_rains(self):
		self.update_rain()
		self.rains.update()
		self.check_rain()

	def create_fleet_rain(self):
		rain=Rain(self)
		rect_width, rect_height=rain.rect.size
		available_space_x=self.settings.screen_width - (2*rect_width)
		number_rains_x=available_space_x//(2*rect_width)
		available_space_y=self.settings.screen_height - (2*rect_height)
		number_rains_y=available_space_y//(2*rect_height)
		for star_y in range(number_rains_y):
			for star_x in range(number_rains_x):
			
				self.drop_rain(star_x, star_y)
	def drop_rain(self,star_x, star_y):
		rain=Rain(self)
		print(len(self.rains))
		rect_width, rect_height=rain.rect.size
		rain.x=rect_width+2*rect_width*star_x
		rain.rect.x=rain.x
		#rain.rect.y=rain.rect.height+2*rain.rect.height*star_y
		self.rains.add(rain)	
	def check_rain(self):

		for rain_g in self.rains.sprites():
			print(f"{rain_g} y value")
			if rain_g.status():
				rain_g.reset()
				self.remove()
				self.create_fleet_rain()
				

				break
	def update_rain(self):
		for rain in self.rains.sprites():
			rain.rect.y+=1
			
				
	def remove(self):
		for rain in self.rains.copy():
			if rain.rect.y>self.screen_rect.bottom:
				self.rains.remove(rain)
				print('delete')
	def update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.rains.draw(self.screen)
		pygame.display.flip()


		
if __name__=='__main__':
	dr=DropRain()
	dr.run()
