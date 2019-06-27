#****************************************************************************************************#
# time:2019.6.25
#test tipoc
#****************************************************************************************************#

tip = '*--------------------------------------------*\r\n'

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print('This restaurant name is ' + self.restaurant_name + 
		'\n' + 'cuisine type is ' + self.cuisine_type)
		
	def open_restaurant(self):
		print('Restaurant is open!')
		
	def restaurant(self):
		print('Sreved number:' + str(self.number_served))
	
	def set_number_served(self, number):
		self.number_served = number
	
	def increment_number_served(self, number):
		self.number_served += number
	
	
#****************************************************************************************************#	
	
#继承，括号内需要添加父类的名字
class IceCream(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)	#这里是给父类的属性赋值
		self.flavors = ['cm','ny','mc']					#添加一个列表属性
		
	def dsp_icecream_list(self):
		print('We have icecream flavors list:')
		for flavor in self.flavors:
			print('-' + flavor)



	




















