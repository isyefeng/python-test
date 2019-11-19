'''button class'''
import pygame.font

class Button():
	def __init__(self, screen, setting, msg):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.msg = msg
		
		self.button_color = (0,230,0)
		self.txt_color = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)	#设置字体及字体大小
		
		self.width, self.high = 200,50
		
		self.rect = pygame.Rect(0, 0, self.width, self.high)
		self.rect.center = self.screen_rect.center
		
		self.prep_msg(msg)

	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.txt_color, self.button_color)	#创建一个字体图片，True是是否开启抗锯齿效果，msg是文本内容
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.screen_rect.center

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)





















