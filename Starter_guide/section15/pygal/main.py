#****************************************************************************************************#
# time:2019.7.9
#test tipoc
#****************************************************************************************************#
"""程序测试"""
from die import Die
import pygal
import matplotlib.pyplot as plt

def creat_sdv_file():
	die = Die()
	results = []
	for roll_num in range(1000):
		results.append(die.roll())
		
	frequencies = []
	for num in range(1,die.num_sizes+1):
		frequencies.append(results.count(num))
		
	print('随机数：' + str(results))
	print('随机数个数' + str(frequencies))
	
	hist = pygal.Bar()
	
	hist.title = 'DIE NUMBER'
	hist.x_labels = [str(x) for x in range(die.num_sizes + 1)]
	hist.x_title = 'DIE NUM'
	hist.y_title = 'frequency of result'
	
	hist.add('D6', frequencies)
	hist.render_to_file('die_values.svg')
	
	
def creat_two_sdv_file():
	die1 = Die(8)
	die2 = Die(8)
	results = []
	for roll_num in range(5000):
		results.append(die1.roll() + die2.roll())
		
	frequencies = []
	for num in range(2,die1.num_sizes + die2.num_sizes + 1):
		frequencies.append(results.count(num))

	hist = pygal.Bar()
	
	hist.title = 'DIE NUMBER'
	hist.x_labels = [str(x) for x in range(2, die1.num_sizes + die2.num_sizes + 1)]
	hist.x_title = 'DIE NUM'
	hist.y_title = 'frequency of result'
	
	hist.add('D8+D8', frequencies)
	hist.render_to_file('die_values.svg')
	
	
def creat_three_sdv_file():
	die1 = Die()
	die2 = Die()
	die3 = Die()
	results = []
	for roll_num in range(1000):
		results.append(die1.roll() + die2.roll() + die3.roll())
		
	frequencies = []
	for num in range(2,die1.num_sizes + die2.num_sizes + die3.num_sizes + 1):
		frequencies.append(results.count(num))

	hist = pygal.Bar()
	
	hist.title = 'DIE NUMBER'
	hist.x_labels = [str(x) for x in range(3, die1.num_sizes + die2.num_sizes + die3.num_sizes + 1)]
	hist.x_title = 'DIE NUM'
	hist.y_title = 'frequency of result'
	
	hist.add('D8+D8', frequencies)
	hist.render_to_file('die_values.svg')


def creat_two_mult_sdv_file():
	die1 = Die()
	die2 = Die()
	results = []
	for roll_num in range(1000):
		results.append(die1.roll()*die2.roll())
		
	frequencies = []
	for num in range(1,die1.num_sizes*die2.num_sizes + 1):
		frequencies.append(results.count(num))

	hist = pygal.Bar()
	
	hist.title = 'DIE NUMBER'
	hist.x_labels = [str(x) for x in range(1, die1.num_sizes*die2.num_sizes + 1)]
	hist.x_title = 'DIE NUM'
	hist.y_title = 'frequency of result'
	
	hist.add('D8+D8', frequencies)
	hist.render_to_file('die_values.svg')
	

def creat_die_image():
	die = Die()
	results = []
	for roll_num in range(1000):
		results.append(die.roll())
		
	frequencies = []
	for num in range(1,die.num_sizes+1):
		frequencies.append(results.count(num))
		
	x_labels = [x for x in range(1, die.num_sizes + 1)]
	
	plt.plot(x_labels, frequencies)
	plt.show()

#creat_sdv_file()
#creat_two_sdv_file()
#creat_three_sdv_file()
#creat_two_mult_sdv_file()
creat_die_image()















