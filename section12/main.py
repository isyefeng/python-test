#****************************************************************************************************#
# time:2019.6.27
#test tipoc
#****************************************************************************************************#
"""alien invasion game"""
import sys
import pygame

def run_game():
	pygame.init()  										#init pygame mode
	screen = pygame.display.set_mode((500,600))			#creat a game surfcae,and windo(800x1200)
	pygame.display.set_caption('Alien Invasion')		#set the game caption
	
	bg_color = (230,230,230)							#定义RGB颜色的元组
	
	#stat game master while
	while True:
		for event in pygame.event.get(): 				#获取鼠标键盘的输入事件
			if event.type == pygame.QUIT:				#如果事件类型是退出
				sys.exit()								#关闭窗口
		screen.fill(bg_color)
		pygame.display.flip()							#让最近绘制的窗口可见

run_game()
			

			
			
			
			



























