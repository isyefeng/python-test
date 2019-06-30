#****************************************************************************************************#
# time:2019.6.27
#test tipoc
#****************************************************************************************************#
"""alien invasion game"""
import sys
import pygame
from Settings import Settings
from ship import Ship
from pygame.sprite import Group				#调用pygame编组类,保存子弹编组
from bullet import Bullet					

def event_space(bullets, setting, ship, screen):			
	if len(bullets) <= setting.bullet_max:					#限制子弹数量
		new_bullet = Bullet(setting, screen, ship)			#实例化一个子弹类
		bullets.add_internal(new_bullet)					#将这个子弹类添加到编组中，每个元素都是一个精灵

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
			
def update_bullte(bullets):
	for bu in bullets.sprites():					#遍历编组,返回每个精灵的类
		bu.draw_bullet()							#调用每个精灵的draw_bullet()方法，也就是Bullet类的draw_bullet()方法
			
def update_screen(screen, ship, bullets, baseinfo):
	screen.fill(baseinfo.screen_color)				#重画，设置背景颜色,这个要放在重画的最开始，否则会覆盖下面的东西
	update_bullte(bullets)							#更新子弹坐标
	ship.dsp_ship()									#重画飞船
	pygame.display.flip()							#让最近绘制的窗口可见
	
def del_bullet(bullets):							#删除消失的子弹
	for bullet in bullets:
		if bullet.rect.bottom <= 0:
			bullets.remove_internal(bullet)
	#print(len(bullets))

def update_bullets(bullets):
	bullets.update()								#此操作将会更新所有编组中子弹的参数（更新每个精灵的参数）	
	del_bullet(bullets)								#删除消失的子弹										


def run_game():
	pygame.init()  										#init pygame mode
	baseinfo = Settings()
	screen = pygame.display.set_mode((baseinfo.screen_width,baseinfo.screen_high))			#creat a game surfcae,and windo(800x1200)
	pygame.display.set_caption('Alien Invasion')		#set the game caption
	ship = Ship(screen, baseinfo)
	bullets = Group()									#creat a bullet group
	#stat game master while
	while True:
		getevent(ship, screen, bullets, baseinfo)										#事件检查和处理
		ship.update()																	#飞船移动
		update_bullets(bullets)
		update_screen(screen, ship, bullets, baseinfo)									#显示函数,需要传入显示的参数，句柄等
		
run_game()
			

			
			
			
			



























