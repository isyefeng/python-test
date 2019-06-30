"""alien class"""
import pygame

class Alien():
	def __init__(self, screen, setting):
		self.set = setting
		self.screen = screen
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.left = self.screen_rect.left
		self.rect.top = self.screen_rect.top
		
	#def update(self):
		
	
	def dsp_alien(self):
		self.screen.blit(self.image, self.rect)

















