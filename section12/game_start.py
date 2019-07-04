'''统计'''
class GameStart():
	def __init__(self, setting):
		self.set = setting
		self.reset_stat()				#创建该类的时候就会调用一次该函数
	
	def reset_stat(self):
		self.ships_left = self.set.ship_left

