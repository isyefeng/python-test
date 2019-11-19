'''统计'''
import json

class GameStart():
	def __init__(self, setting):
		'''
		self.max_scroe_file = 'scroefile.txt'				#文本格式储存
		'''
		self.max_scroe_file = 'scroefile.json'				#json格式储存
		
		self.set = setting
		self.reset_stat()				#创建该类的时候就会调用一次该函数
		
		self.scroe = 0					#分数
		self.max_scroe = 0				#最高得分
		
		self.read_scroe()				#读取最高分数
	
	def reset_stat(self):
		self.ships_left = self.set.ship_left
		
	'''
	def read_scroe(self):
		try:
			with open(self.max_scroe_file) as file_t:
				 num = file_t.read()
			self.max_scroe = int(num)
		except FileNotFoundError:
			with open(self.max_scroe_file, 'w') as file_t:
				file_t.write('0')
		
	def save_scroe(self):
		with open(self.max_scroe_file, 'w') as file_t:
			file_t.write(str(self.max_scroe))	
	'''		
			
	def read_scroe(self):
		try:
			with open(self.max_scroe_file) as f_obj:
				 num = json.load(f_obj)
			self.max_scroe = num
		except FileNotFoundError:
			with open(self.max_scroe_file, 'w') as f_obj:
				json.dump(0, f_obj)
		
	def save_scroe(self):
		with open(self.max_scroe_file, 'w') as f_obj:
			json.dump(self.max_scroe, f_obj)
	
		

