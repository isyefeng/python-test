"""Ship class"""
import pygame

class Ship():
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def dsp_ship(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)





























