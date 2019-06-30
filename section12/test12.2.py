"""section 12 test"""
import sys
import pygame

class Ship():
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
	def dsp_ship(self):
		self.screen.blit(self.image, self.rect)

def get_event():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def creat_win():
	pygame.init()
	screen = pygame.display.set_mode((500,600))
	ship = Ship(screen)
	pygame.display.set_caption('test window')
	
	while True:
		get_event()
		screen.fill((0,162,232))
		ship.dsp_ship()
		pygame.display.flip()


creat_win()






































