#****************************************************************************************************#
# time:2019.7.9
#test tipoc
#****************************************************************************************************#
"""程序测试"""
import matplotlib.pyplot as plt

from random_walk import Randomwalk


def show_plot():
	lienx = list(range(1,5001))
	lieny = [x**3 for x in lienx]

	plt.plot(lienx, lieny, linewidth = 5)

	plt.title('5**3',fontsize=24)
	plt.xlabel('x',fontsize=14)
	plt.ylabel('y',fontsize=14)

	plt.show()

def show_color_scatter():
	lienx = list(range(1,5001))
	lieny = [x**3 for x in lienx]
	
	plt.title('5**3',fontsize=24)
	plt.xlabel('x',fontsize=14)
	plt.ylabel('y',fontsize=14)
	
	plt.scatter(lienx, lieny, c=lieny, cmap=plt.cm.Blues, edgecolor='none', s=40)

	plt.show()


#show_color_scatter()
def show_choice_num():
	random = Randomwalk()
	random.fill_walk()
	
	plt.title('5**3',fontsize=24)
	plt.xlabel('x',fontsize=14)
	plt.ylabel('y',fontsize=14)

	plt.plot(random.x_values, random.y_values)

	plt.show()

show_choice_num()













