"""set game class"""
class Settings():
	def __init__(self):
		self.screen_width = 600
		self.screen_high = 600
		self.screen_color = (230,230,230)
		self.screen_speed = 1.5
		
		self.bullet_with = 30
		self.bullet_high = 15
		self.bullet_speed = 0.5
		self.bullet_color = 60,60,60
		self.bullet_max = 5
		
		self.alien_speed = 1.0
		self.alien_down_speed = 20
		self.alien_tl_flag = 1
		self.alien_add_index = 0
		
		self.ship_left = 3				#生命值
		
		self.speed_add = 1.1			#速度增量
		self.scroe_add = 1.5			#分值增量
		
		self.stat_flag = False			#游戏开始/结束标志
		
		self.alien_score = 50			#击杀外新人得分
		
		self.reset_speed()
		
		
	def reset_speed(self):
		self.bullet_speed = 0.5
		self.screen_speed = 1.5
		self.alien_speed = 1
		self.alien_score = 50
		
	
	def game_speed_add(self):
		self.bullet_speed *= self.speed_add
		self.screen_speed *= self.speed_add
		self.alien_speed *= self.speed_add
		self.alien_score = int(self.scroe_add * self.alien_score)






















