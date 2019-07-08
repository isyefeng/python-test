'''分数显示'''
import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
	def __init__(self, setting, screen, stat):
		self.setting = setting
		
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.stat = stat
		
		self.txt_color = (30,30,30)
		self.font = pygame.font.SysFont(None, 48)
		self.max_font = pygame.font.SysFont(None, 48)
		
		self.prep_score()
		self.prep_max_score()
		self.prep_ships()
		
		
	def prep_score(self):
		scroe_num = int(round(self.stat.scroe, -1))						#将得分的各位部分省略，或者说是圆整得分
		scroe_str = "{:,}".format(scroe_num)							#在数字中插入逗号
		self.scroe_image = self.font.render(scroe_str, True, self.txt_color, self.setting.screen_color)
		
		self.scroe_rect = self.scroe_image.get_rect()
		self.scroe_rect.right = self.screen_rect.right - 10
		self.scroe_rect.top = 20
		
	def prep_max_score(self):											#最大分值的创建
		scroe_num = int(round(self.stat.max_scroe, -1))	
		scroe_str = "{:,}".format(scroe_num)
		self.scroe_max_image = self.max_font.render(scroe_str, True, self.txt_color, self.setting.screen_color)
		
		self.scroe_max_rect = self.scroe_image.get_rect()
		self.scroe_max_rect.centerx = self.screen_rect.centerx
		self.scroe_max_rect.top = 20
		
	def shou_score(self):
		self.screen.blit(self.scroe_image, self.scroe_rect)
		self.screen.blit(self.scroe_max_image, self.scroe_max_rect)			#最大分值显示
		self.ships.draw(self.screen)										#显示飞船数量
		
	def prep_ships(self):
		self.ships = Group()
		for ship_num in range(self.setting.ship_left):
			ship = Ship(self.screen, self.setting)
			ship.rect.x = 10 + ship_num*ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
		
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		