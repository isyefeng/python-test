#****************************************************************************************************#
# time:2019.6.17
#test tipoc
#****************************************************************************************************#

tip = '*--------------------------------------------*\r\n'

flag_pizs = True
while flag_pizs:
	pizs_buf = input('请输入您想要的披萨配料：')
	if pizs_buf == 'quit':
		flag_pizs = False
	else:
		print('我们会在您的披萨中加入' + pizs_buf + '这种配料！')
print(tip)
#****************************************************************************************************#

while True:
	num = input('请输入您的年龄:')
	if num == 'quit':
		break
	elif int(num) <= 3:
		print('不用钱')
	elif int(num) <= 12:
		print('10美元')
	else:
		print('15美元')
print(tip)
#****************************************************************************************************#

sandwich_orders = ['牛肉','猪肉','斋']
finished_sandwiches = []

while sandwich_orders:
	sandwich_buf = sandwich_orders.pop()
	print(sandwich_buf)
	finished_sandwiches.append(sandwich_buf)
print(finished_sandwiches)

sandwich_orders = ['牛肉','五香','猪肉','五香','斋','五香']
print('五香的卖完了')
print(sandwich_orders)
while '五香' in sandwich_orders:
	sandwich_orders.remove('五香')
print(sandwich_orders)

print(tip)
#****************************************************************************************************#

user = []
user_info = {}
while True:
	name_buf = input('请输入你的名字：')
	city_buf = input('请输入你想去城市：')
	user_info['name'] = name_buf
	user_info['city'] = city_buf
	user.append(user_info)
	buf = input('继续输入下一个用户（yes/no）:')
	if buf == 'yes':
		continue
	elif buf == 'no':
		break

print(user)


def str_cty(buf1, buf2):
	return buf1 + ' ' + buf2



































