#****************************************************************************************************#
# time:2019.6.24
#test tipoc
#****************************************************************************************************#

tip = '*--------------------------------------------*\r\n'

#函数
def display_message():
	print('这是一个学习函数的章节')

display_message()

#函数参数的传递
def favorit_book(book_name):
	print('我最喜欢的一本书是' + book_name)

favorit_book('三体')

def make_shirt( size = 'L', logo = 'I LOVE PYTHON'):
	print('您需要一件' + size + '码的衣服，并且加上' + logo + '字样')
	
print('位置实参')
make_shirt('m','hello word!')
print('关键字实参')
make_shirt(logo = 'hello!', size = 'M')
print('默认参数调用')
make_shirt()
make_shirt('M')
make_shirt(logo = 'hello python')
print(tip)

#默认参数的使用
def describe_city(city_name, city_contry = 'china'):
	print(city_name + ' is in ' + city_contry)
	
describe_city('guangdong')
describe_city('new yonw','amrican')
describe_city('fujian','china')
print(tip)

#为了使程序更加美观，写函数的时候最好是可以使用位置参数的方法。

def city_country(city_name, city_from):
	return city_name + ',' + city_from
	
print(city_country('santiago','chile'))
print(city_country('guangdong','china'))

print(tip)

#返回字典
def make_album(plepol_neme, album_name, album_number = ''):
	info = {}
	info['plepol_neme'] = plepol_neme
	info['album_name'] = album_name
	if album_number:
		info['album_number'] = album_number
	return info
	
def display_album(album_info):
	for key,value in album_info.items():
		print(key + ':' + value)
	print('\r\n')

def album_test(plepol_neme, album_name):
	display_album(make_album(plepol_neme, album_name))

album_test('liu','alzm')
album_test('zhou','dx')

display_album(make_album('wang','y','15'))

#循环输入,并传入函数中
def while_input_info():
	while True:
		p_name = input('please input pelpol name:')
		a_name = input('please input album name:')
		a_number = input('please input album namber:')
		display_album(make_album(p_name, a_name, a_number))
		flag = input('woule you want to quit(q/n)')
		if flag == 'q':
			break
#while_input_info()
print(tip)
	

#向函数传入列表或字典	
show_magicians = ['liu','lin','ye']
def show_magicians_name(names):
	for name in names:
		print(name + ' is a migicians\n')

show_magicians_name(show_magicians)

def make_great(names):
	num = 0
	for name in names:
		names[num] = 'the Great' + name
		num = num + 1
	return names
#传入的列表是可以改变的
make_great(show_magicians)
show_magicians_name(show_magicians)


show_magicians = ['liu','lin','ye']
#传入一个不可改变的列表，函数内会复制这个列表生成一个副本
name_buf = make_great(show_magicians[:])
show_magicians_name(show_magicians) #原始的
show_magicians_name(name_buf)		#更改的
print(tip)

#传入不确定数量的列表元素/字典元素
#传入列表
def make_sandwich(*info):
	print('you sandwich include:')
	for buf in info:
		print('- ' + buf)

make_sandwich('yu','cai','ega')
make_sandwich('zr','hj')
make_sandwich('nr')

#传入字典
def user_profile(frise_name, last_name, **user_info):
	user = {}
	user['frise_name'] = frise_name
	user['last_name'] = last_name
	for key,value in user_info.items():
		user[key] = value
	return user
	
user1 = user_profile('ye','feng',high=15,city='gd')
user2 = user_profile('l','hh',h=10,city='gz')
print(user1)
print(user2)
print(user2)

def buy_cat(name, number, **other_info):
	cat_info = {}
	cat_info['name'] = name
	cat_info['number'] = number
	for key,value in other_info.items():
		cat_info[key] = value
	return cat_info

cat1 = buy_cat('porsche','cayenne',color='reg',tc='qj',zy='jr')
cat2 = buy_cat('bans','AMG',lg='hkq',wy='hws')
print(cat1)
print(cat2)


