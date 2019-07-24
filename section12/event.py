"""event mode"""
import pygame
import sys
from alien import Alien
from bullet import Bullet
from random import randint		

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
		'''if not setting.stat_flag:
			setting.stat_flag = True'''
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

def cheak_play_button(setting, button, mouse_x, mose_y, stat, bullets, aliens, ship, screen, scroe):
	coll_start = button.rect.collidepoint(mouse_x, mose_y)
	if coll_start and not setting.stat_flag:				  	#检测mouse_x, mose_y是否在button.rect内部，如果是返回真
		setting.stat_flag = True
		setting.ship_left = 3
		scroe.prep_ships()
		stat.reset_stat()
		aliens.empty()
		bullets.empty()
		
		creat_aliens(aliens, screen, setting)
		ship.center_ship()
		
		pygame.mouse.set_visible(False)
		
		setting.reset_speed()								#重置速度
		
		

def creat_aliens(aliens, screen, setting):			#创建外星人群
	alien = Alien(screen, setting)
	alien_with = alien.rect.width
	alien_high = alien.rect.height
	alien_x_long = setting.screen_width - alien_with*2
	alien_x_num = int(alien_x_long/(alien_with*2))
	
	for num in range(alien_x_num):
		alien = Alien(screen, setting)
		alien.x = randint(0, setting.screen_width - alien_with)
		alien.rect.x = alien.x
		alien.rect.y = alien_high
		aliens.add(alien)
	'''		//规则外星人
	for numy in range(0,3):
		for numx in range(alien_x_num):
			alien = Alien(screen, setting)
			alien.x = alien_with + alien_with*numx*2
			alien.rect.x = alien.x
			alien.rect.y = alien_high + alien_high*numy*2
			aliens.add(alien)
	'''		

def getevent(screen_ship, screen, bullets, setting, button, aliens, stat, scroe):
	for event in pygame.event.get():								#获取鼠标键盘的输入事件
		if event.type == pygame.QUIT:								#如果事件类型是退出
			stat.save_scroe()
			sys.exit()												#关闭窗口
		elif event.type == pygame.KEYDOWN:							#键盘按下检测
			key_down_event(event, screen_ship, screen, setting, bullets)					
		elif event.type == pygame.KEYUP:							#键盘松开检测
			key_up_event(event, screen_ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:					#鼠标按下类型
			mouse_x, mose_y = pygame.mouse.get_pos()				#获取鼠标按下坐标
			cheak_play_button(setting, button, mouse_x, mose_y, stat, bullets, aliens, screen_ship, screen, scroe)
















