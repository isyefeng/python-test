'''random num creat'''
from random import choice

class Randomwalk():
	def __init__(self, walk_num = 5000):
		self.walk_num = walk_num
		self.walk_num = walk_num		
		self.x_values = [0]
		self.y_values = [0]
	
	def fill_walk(self):
		while len(self.x_values) < self.walk_num:
			x_direction = choice([-1,1])
			x_distance = choice(list(range(1,9)))
			x_step = x_direction*x_distance
			
			y_direction = choice([0,1])
			y_distance = choice([1,2,3,4])
			y_step = y_direction*y_distance
			
			if x_step == 0 and y_step == 0:
				continue
				
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)


