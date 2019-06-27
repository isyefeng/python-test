#****************************************************************************************************#
# time:2019.6.27
#test tipoc
#****************************************************************************************************#
"""alien invasion game"""
import sys
import pygame
from Settings import Settings
from ship import Ship


def getevent():
	for event in pygame.event.get():	#获取鼠标键盘的输入事件
		if event.type == pygame.QUIT:		#如果事件类型是退出
			sys.exit()					#关闭窗口
			
def update_screen(screen, ship, baseinfo):
	screen.fill(baseinfo.screen_color)				#重画，设置背景颜色,这个要放在重画的最开始，否则会覆盖下面的东西
	ship.dsp_ship()									#重画飞船
	pygame.display.flip()							#让最近绘制的窗口可见


def run_game():
	pygame.init()  										#init pygame mode
	baseinfo = Settings()
	screen = pygame.display.set_mode((baseinfo.screen_width,baseinfo.screen_high))			#creat a game surfcae,and windo(800x1200)
	pygame.display.set_caption('Alien Invasion')		#set the game caption
	ship = Ship(screen)
	#stat game master while
	while True:
		getevent()										#事件检查和处理
		update_screen(screen, ship, baseinfo)			#显示函数,需要传入显示的参数，句柄等

run_game()
			

			
			
			
			



























