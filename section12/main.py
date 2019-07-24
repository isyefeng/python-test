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
from button import Button
from scoreboard import Scoreboard
			
def update_bullte(bullets):
	for bu in bullets.sprites():					#遍历编组,返回每个精灵的类
		bu.draw_bullet()							#调用每个精灵的draw_bullet()方法，也就是Bullet类的draw_bullet()方法
				
			
def update_screen(screen, ship, bullets, baseinfo, alien, button, setting, scroe):
	screen.fill(baseinfo.screen_color)				#重画，设置背景颜色,这个要放在重画的最开始，否则会覆盖下面的东西
	update_bullte(bullets)							#更新子弹坐标
	alien.draw(screen)
	ship.dsp_ship()									#重画飞船
	scroe.shou_score()
	if not setting.stat_flag:
		button.draw_button()
	pygame.display.flip()							#让最近绘制的窗口可见
	
	
	
def del_bullet(bullets):							#删除消失的子弹
	for bullet in bullets:
		if bullet.rect.bottom <= 0:
			bullets.remove_internal(bullet)
	#print(len(bullets))


#创建多行外星人
def creat_alien_second(aliens, screen, setting):
	setting.alien_add_index += 1
	if setting.alien_add_index%1000 == 0:
		creat_aliens(aliens, screen, setting)
		
	if setting.alien_add_index > 3000:
		setting.alien_add_index = 0
		setting.game_speed_add()									#增加速度


def update_bullets(bullets, aliens, screen, setting, stat, scroe):
	bullets.update()														#此操作将会更新所有编组中子弹的参数（更新每个精灵的参数）
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)	#检测子弹之间的碰撞，两个True表示是否删除该精灵，前一个True表示bullet 后一个表示alien, 返回值是一个字典，键是子弹，值是与子弹碰撞的外新人列表
	if collisions:
		for aliens in collisions.values():
			stat.scroe += setting.alien_score * len(aliens)
			scroe.prep_score()
		
	del_bullet(bullets)														#删除到达边缘的子弹		
	if len(aliens) == 0:
		bullets.empty()
		creat_aliens(aliens, screen, setting)
			
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

def ship_hit(aliens, bullets, screen, stat, setting, scroe):
	setting.ship_left -= 1
	if stat.scroe > stat.max_scroe:
		stat.max_scroe = stat.scroe
	stat.scroe = 0
	scroe.prep_max_score()
	scroe.prep_score()
	scroe.prep_ships()
	bullets.empty()
	aliens.empty()
	creat_aliens(aliens, screen, setting)
	stat.reset_stat()
	setting.reset_speed()
	
	sleep(0.5)
	

def alien_update(setting, aliens, ship, bullets, screen, stat, scroe):
	check_fleet_edges(setting, aliens)
	cheak_alien_bottom(aliens, screen, bullets, stat, setting, scroe)
	creat_alien_second(aliens, screen, setting)
	if pygame.sprite.spritecollideany(ship, aliens):
		ship.center_ship()
		ship_hit(aliens, bullets, screen, stat, setting, scroe)
	if stat.ships_left < 0:
		setting.stat_flag = False
		pygame.mouse.set_visible(True)
		setting.ship_left = 3
		scroe.prep_ships()	
	aliens.update()

'''检查外星人是否到底'''
def cheak_alien_bottom(aliens, screen, bullets, stat, setting, scroe):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(aliens, bullets, screen, stat, setting, scroe)
			break


def run_game():
	pygame.init()  																			#init pygame mode
	baseinfo = Settings()
	stat = GameStart(baseinfo)
	screen = pygame.display.set_mode((baseinfo.screen_width,baseinfo.screen_high))			#creat a game surfcae,and windo(800x1200)
	pygame.display.set_caption('Alien Invasion')											#set the game caption
	ship = Ship(screen, baseinfo)
	button = Button(screen, baseinfo, "PLAY")
	scroe = Scoreboard(baseinfo, screen, stat)												#实例化一个分数显示类
	aliens = Group()																		#creat alien group
	bullets = Group()																		#creat a bullet group
	creat_aliens(aliens, screen, baseinfo) 
	#stat game master while
	while True:
		getevent(ship, screen, bullets, baseinfo, button, aliens, stat, scroe)						#事件检查和处理
		if baseinfo.stat_flag:
			ship.update()																	#飞船移动
			update_bullets(bullets, aliens, screen, baseinfo, stat, scroe)
			alien_update(baseinfo, aliens, ship, bullets, screen, stat, scroe)
		update_screen(screen, ship, bullets, baseinfo, aliens, button, baseinfo, scroe)									#显示函数,需要传入显示的参数，句柄等
		
run_game()
			

			
			
			
			



























