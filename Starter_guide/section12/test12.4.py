"""test 12.4"""
import pygame
import sys

def get_event():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			print(event.key)

def run_date():
	pygame.init()
	screen = pygame.display.set_mode((500,600))
	pygame.display.set_caption('test12.4')
	
	while True:
		get_event()
		screen.fill((230,230,230))
		pygame.display.flip()

run_date()













































