#****************************************************************************************************#
# time:2019.6.21
#test tipoc
#****************************************************************************************************#

tip = '*--------------------------------------------*\r\n'

mr_ye = {
	'first_name':'ye',
	'last_name':'feng',
	'age':'22',
	'city':'gd',
	}

mr_l = {
	'first_name':'l',
	'last_name':'r',
	'age':'22',
	'city':'gd',
	}

mr_g = {
	'first_name':'g',
	'last_name':'sx',
	'age':'22',
	'city':'gd',
	}

#创建一个列表嵌套字典
user_info = [mr_g,mr_l,mr_ye]
for info in user_info:
	for key,value in info.items():
		print(key + ':' + value)
	print('\n')
#****************************************************************************************************#

tom = {
	'fathe':'ye',
	'lx':'dog',
	}	
jeri = {
	'fathe':'lin',
	'lx':'has',
	}
kiki = {
	'fathe':'fei',
	'lx':'cat',
	}

pets = [tom,jeri,kiki]
for pet in pets:
	print(pet)
#****************************************************************************************************#
print(tip)
#字典嵌套列表	
favorite_places = {
	'ye':['us','thai','china'],
	'lin':['amrk','yg'],
	'jie':['us','cx','rb'],
	}	

for key,value in favorite_places.items():
	print(key + 'favorite like placse is:')
	for places in value:
		print(places)
	print('\n')
#****************************************************************************************************#
print(tip)
#字典嵌套字典		
citise = {
	'gd':{
		'country':'china',
		'people':1300000000,
		'fact':'美丽'
		},
	'new_york':{
		'country':'america',
		'people':100000000,
		'fact':'丑陋'
		},
	'london':{
		'country':'england',
		'people':10000000,
		'fact':'浪漫'
		},
	}

for key,value in citise.items():
	print(key + ' info:')
	for key1,value1 in value.items():
		print(key1 + ':' + str(value1))
	print('\n')
	
 	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	