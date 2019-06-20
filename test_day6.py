#****************************************************************************************************#
# time:2019.6.20
#test tipoc
#****************************************************************************************************#

tip = '*--------------------------------------------*\r\n'

user_info = {
	'first_name':'ye',
	'last_name':'feng',
	'age':'22',
	'city':'guangdong',
	}

print(user_info)

print(user_info['first_name'])

#遍历键-值，打印两个需要用到items()方法
for key,value in user_info.items():
	print(key + ':' + value)

like_number = {
	'yefeng':3,
	'lhh':4,
	'liuyan':5,
	}
print(like_number)

print(like_number['yefeng'])

#修改键-值
like_number['yefeng'] = 10
print(like_number['yefeng'])

#删除一对键-值
del like_number['liuyan']
print(like_number)

function_zd = {
	'title()':'用于输出首字母大写的字符串',
	'lower()':'用于输出全部小写字母',
	'pop(x)':'用于删除列表x号元素',
	'del':'删除一个列表元素或字典元素',
	'del':'删除一个列表元素或字典元素',
	}

for key,value in function_zd.items():
	print(key + ':' + value + '\n')

for key in function_zd:
	print(key)
#keys()方法用来只输出键
for key in function_zd.keys():
	print(key)

#values()方法用来只输出值
for value in function_zd.values():
	print(value)

#set()方法使用来排除相同值得
list_buf = set(function_zd.keys())
print(list_buf)

#添加键-值 字典元素
function_zd['set()'] = '用于排除相同的值'
function_zd['sorten()'] = '单次顺序排列，按字母大小或数字大小'
for value in set(function_zd.values()):
	print(value)
print(tip)

river = {
	'中国':'长江',
	'印度':'尼罗河',
	'美国':'密西西比河',
	}

for key, value in river.items():
	print(value + '是' + key + '的河流')

for value in river.values():
	print(value)

for key in river:
	print(key)

favorit = {
	'jen':'python',
	'sarch':'c',
	'edward':'ruby',
	'phil':'python',
	}

names = ['sarch','tom','phil','li','ye']

for name in names:
	if name in favorit.keys():
		print('谢谢参加！')
	else:
		print('请来参加！')
