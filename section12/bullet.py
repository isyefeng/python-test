"""子弹"""
import pygame
from pygame.sprite import Sprite

class Bullet():
	def __init__(self, setting, screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen
		
		self.rect = pygame.Rect(0, 0, setting.bullet_with, setting.bullet_high)		#创建子弹的矩形
		self.rect.centerx = ship.rect.centerx									#设置子弹的X坐标
		self.rect.top = ship.rect.top											#设置子弹的顶部坐标
		
		self.y = float(self.rect.y)
				
		self.color = setting.bullet_color										#定义子弹颜色
		self.speed = setting.bullet_speed										#定义子弹速度
		
	def update(self):
		self.y -= self.speed
		self.rect.y = self.y 
		#self.rect.y -= self. 												#子弹向上移动(这种方法不会让子弹消失)
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)					#重画子弹
			
	





















