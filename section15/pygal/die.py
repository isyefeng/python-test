'''die calss'''
from random import randint

class Die():
	def __init__(self, num_sizes = 6):
		self.num_sizes = num_sizes
		
	def roll(self):
		return randint(1,self.num_sizes)



