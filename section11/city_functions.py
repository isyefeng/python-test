"""city functions"""

def city_add(city, country, population = 0):
	if population == 0:
		return city + ',' + country
	else:
		return city + ',' + country + '- population' + str(population)
	
class Employee():
	def __init__(self, first_name, last_name, money):
		self.first_name = first_name
		self.last_name = last_name
		self.money = money
	
	def give_raise(self, add = 5000):
		self.money += add
		
	