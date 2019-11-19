"""alien class"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, screen, setting):
		super(Alien, self).__init__()
		self.set = setting
		self.screen = screen
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.tl_flag = 1			#方向
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
	
	def update(self):
		self.x += self.set.alien_speed*self.tl_flag
		self.rect.x = self.x
	
	def check_edges(self):
		if self.rect.right >= self.screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
		
	def dsp_alien(self):		#绘制外星人
		self.screen.blit(self.image, self.rect)

















