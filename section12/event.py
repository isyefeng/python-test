"""event mode"""
import pygame
import sys
from bullet import Bullet					

def event_space(bullets, setting, ship, screen):			
	if len(bullets) <= setting.bullet_max:					#限制子弹数量
		new_bullet = Bullet(setting, screen, ship)			#实例化一个子弹类
		bullets.add(new_bullet)					#将这个子弹类添加到编组中，每个元素都是一个精灵

def key_down_event(event, ship, screen, setting, bullets):
	if event.key == pygame.K_RIGHT:
		ship.right_flag = True
	elif event.key == pygame.K_LEFT:
		ship.left_flag = True
	elif event.key == pygame.K_UP:
		ship.up_flag = True
	elif event.key == pygame.K_DOWN:
		ship.down_flag = True	
	elif event.key == pygame.K_SPACE:
		event_space(bullets, setting, ship, screen)
		
def key_up_event(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.right_flag = False
	elif event.key == pygame.K_LEFT:
		ship.left_flag = False
	elif event.key == pygame.K_UP:
		ship.up_flag = False
	elif event.key == pygame.K_DOWN:
		ship.down_flag = False	

def getevent(screen_ship, screen, bullets, setting):
	for event in pygame.event.get():								#获取鼠标键盘的输入事件
		if event.type == pygame.QUIT:								#如果事件类型是退出
			sys.exit()												#关闭窗口
		elif event.type == pygame.KEYDOWN:							#键盘按下检测
			key_down_event(event, screen_ship, screen, setting, bullets)					
		elif event.type == pygame.KEYUP:							#键盘松开检测
			key_up_event(event, screen_ship)
















