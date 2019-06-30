"""Ship class"""
import pygame

#屏幕坐标是这样分的
#(0,0) -------->
#     |
#	  |
#	  v		 (max,max)
#

class Ship():
	def __init__(self, screen, setting):
		self.screen = screen
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()	#获取主窗口矩形信息
		
		self.set = setting					#设置类
		
		self.right_flag = False				#上下左右移动标志
		self.left_flag = False
		self.up_flag = False
		self.down_flag = False

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def dsp_ship(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""飞船移动"""
		if self.right_flag and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.set.screen_speed
		if self.left_flag and self.rect.left > 0:
			self.rect.centerx -= self.set.screen_speed
		if self.up_flag and self.rect.top > 0:
			self.rect.centery -= self.set.screen_speed
		if self.down_flag and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.set.screen_speed























