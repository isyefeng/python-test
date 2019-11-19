#****************************************************************************************************#
# time:2019.6.17
#test tipoc
#****************************************************************************************************#

tip = '*--------------------------------------------*\r\n'

age = 12
if age < 4:
	print('不用钱')
elif age < 18:
	print('5美元')
else:
	print('10美元')

alien_color = 'green'
if alien_color == 'green':
	print('正确！你获得了5个点')
#****************************************************************************************************#
print(tip)
alien_color = 'red'
if alien_color == 'green':
	print('正确！你获得了5个点')
#****************************************************************************************************#
print(tip)
if alien_color == 'green':
	print('正确！你获得了5个点')
else:
	print('你获得了10个点')
#****************************************************************************************************#
print(tip)
alien_color = 'green'
if alien_color == 'green':
	print('正确！你获得了5个点')
else:
	print('你获得了10个点')
#****************************************************************************************************#	
print(tip)
if alien_color == 'green':
	print('你获得了5个点')
elif alien_color == 'yellow':
	print('你获得了10个点')
else:
	print('你获得了15个点')
	
	
users = ['admin','root','yefeng','kh','pec']

for user in users:
	print('hello ' + user + ' welcome!\r\n')
print(tip)

for user in users:
	if user == 'admin':
		print('hello admin!you are particularly\r\n')
	else:
		print('hello ' + user + ' welcome!\r\n')
print(tip)

print('del list')
for num in range(0,5):
	del users[4-num]

if users:
	for user in users:
		print('hello ' + user + ' welcome!\r\n')
else:
	print('we need find user!')

current_users = ['admin','root','yefeng','kh','pec']
new_users = ['admin','isyefeng','khpec','root','PEC']
for user in new_users:
	if user in current_users:
		print(user + ' this user name is define!')
	else:
		print(user + ' this user is ok!')
		
for	user in new_users:
	if user.lower() in current_users:
		print(user + ' this user name is define!')
	else:
		print(user + ' this user is ok!')
		
numbers = range(1,10)
for num in numbers:
	print(num)	
	
for num in numbers:
	if num == 1:
		print('1st\r\n')
	elif num == 2:
		print('2nd\r\n')
	elif num == 3:
		print('3rd\r\n')
	else:
		print(str(num) + 'th\r\n')
		























		
