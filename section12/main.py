#****************************************************************************************************#
# time:2019.6.27
#test tipoc
#****************************************************************************************************#
"""alien invasion game"""
import sys
import pygame
from Settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group				#调用pygame编组类,保存子弹编组
from pygame.sprite import Sprite
from event import*							#调用事件操作
from random import randint
from game_start import GameStart
from time import sleep

			
def update_bullte(bullets):
	for bu in bullets.sprites():					#遍历编组,返回每个精灵的类
		bu.draw_bullet()							#调用每个精灵的draw_bullet()方法，也就是Bullet类的draw_bullet()方法
				
			
def update_screen(screen, ship, bullets, baseinfo, alien):
	screen.fill(baseinfo.screen_color)				#重画，设置背景颜色,这个要放在重画的最开始，否则会覆盖下面的东西
	update_bullte(bullets)							#更新子弹坐标
	alien.draw(screen)
	ship.dsp_ship()									#重画飞船
	pygame.display.flip()							#让最近绘制的窗口可见
	
	
	
def del_bullet(bullets):							#删除消失的子弹
	for bullet in bullets:
		if bullet.rect.bottom <= 0:
			bullets.remove_internal(bullet)
	#print(len(bullets))

'''
#创建多行外星人
def creat_alien_second(aliens, screen, setting):
	for alien in aliens.sprites():
		if alien.rect.y == setting.alien_down_speed*10:
			creat_aliens(aliens, screen, setting)
			break
'''

def update_bullets(bullets, aliens, screen, setting):
	bullets.update()								#此操作将会更新所有编组中子弹的参数（更新每个精灵的参数）
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)	#检测子弹之间的碰撞，两个True表示是否删除该精灵，前一个True表示bullet 后一个表示alien
	del_bullet(bullets)								#删除消失的子弹		
	if len(aliens) == 0:
		bullets.empty()
		creat_aliens(aliens, screen, setting)	

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
	'''		//规则外新人
	for numy in range(0,3):
		for numx in range(alien_x_num):
			alien = Alien(screen, setting)
			alien.x = alien_with + alien_with*numx*2
			alien.rect.x = alien.x
			alien.rect.y = alien_high + alien_high*numy*2
			aliens.add(alien)
	'''		
			
def alien_down_date(setting, aliens):			#向下移动飞船
	for alien in aliens.sprites():
		alien.rect.y += setting.alien_down_speed
	setting.alien_tl_flag *= -1
			
def check_fleet_edges(setting, aliens):			#检查是否到达边缘
	for alien in aliens.sprites():
		if alien.check_edges():
			alien.tl_flag *= -1
			alien.rect.y += setting.alien_down_speed
			'''								 	#全部外新人一起改变方向
			alien_down_date(setting, aliens)
			break
			'''

def ship_hit(aliens, bullets, screen, stat, setting):
	setting.ship_left -= 1
	bullets.empty()
	aliens.empty()
	creat_aliens(aliens, screen, setting)
	stat.reset_stat()
	
	sleep(0.5)
	

def alien_update(setting, aliens, ship, bullets, screen, stat):
	check_fleet_edges(setting, aliens)
	cheak_alien_bottom(aliens, screen, bullets, stat, setting)
	creat_alien_second(aliens, screen, setting)
	if pygame.sprite.spritecollideany(ship, aliens):
		ship.center_ship()
		ship_hit(aliens, bullets, screen, stat, setting)
	if stat.ships_left < 0:
		setting.stat_flag = False
	aliens.update()

'''检查外星人是否到底'''
def cheak_alien_bottom(aliens, screen, bullets, stat, setting):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(aliens, bullets, screen, stat, setting)
			break


def run_game():
	pygame.init()  																			#init pygame mode
	baseinfo = Settings()
	stat = GameStart(baseinfo)
	screen = pygame.display.set_mode((baseinfo.screen_width,baseinfo.screen_high))			#creat a game surfcae,and windo(800x1200)
	pygame.display.set_caption('Alien Invasion')											#set the game caption
	ship = Ship(screen, baseinfo)
	aliens = Group()																		#creat alien group
	bullets = Group()																		#creat a bullet group
	creat_aliens(aliens, screen, baseinfo)
	#stat game master while
	while True:
		getevent(ship, screen, bullets, baseinfo)										#事件检查和处理
		if baseinfo.stat_flag:
			ship.update()																	#飞船移动
			update_bullets(bullets, aliens, screen, baseinfo)
			alien_update(baseinfo, aliens, ship, bullets, screen, stat)
		update_screen(screen, ship, bullets, baseinfo, aliens)									#显示函数,需要传入显示的参数，句柄等
		
run_game()
			

			
			
			
			



























