#****************************************************************************************************#
# time:2019.6.26
#test tipoc
#****************************************************************************************************#
import json
tip = '*--------------------------------------------*\r\n'

#10.1
filename = 'Iearning.txt'
with open(filename) as file_t:
	filebuf = file_t.read()
	print(filebuf)
		
with open(filename) as file_t:
	for filebuf in file_t:
		print(filebuf.rstrip())

with open(filename) as file_t:
	lines = file_t.readlines()
	
print(tip)

#10.2	
#replace(x，y)方法是将X换成Y
for line in lines:
	line = line.replace('python','c')
	print(line.rstrip())
print(tip)

#10.3
def input_name_and_save():
	filename = 'guest.txt'
	name = input('please input your name:')
	if name:
		with open(filename, 'w') as file_t:
			file_t.write(name)

#input_name_and_save()
print(tip)
#****************************************************************************************************#


#10.4
def input_names_and_save():
	filename = 'gusst_book.txt'
	num = 1
	flag = True
	while flag:
		username = input('please input your name:')
		if username == 'q':
			flag = False
		else:
			with open(filename, 'a') as file_t:
				file_t.write('User' + str(num) + ':' + username + '\n')
			num += 1


#input_names_and_save()
print(tip)
#****************************************************************************************************#

#10.5
def input_way_like_code():
	filename = 'gusst_book.txt'
	flag = True
	while flag:
		waystr = input('plsase input way you like code:')
		if waystr == 'q':
			flag = False
		else:
			with open(filename, 'a') as file_t:
				file_t.write(waystr + '\n')

#input_way_like_code()
print(tip)
#****************************************************************************************************#

#10.6
def add_math():
	num1 = input('please input a number:')
	num2 = input('please input a number:')
	try:
		sum = int(num1) + int(num2)
		print(sum)
	except ValueError:
		if num1 != 'q' and num2 != 'q':
			print('please net\'t input string!')
		
	return num1
	
#add_math()
print(tip)
#****************************************************************************************************#

#10.7
def add_wile():
	flag = True
	while flag:
		if add_math() == 'q':
			flag = False


#10.8
def read_file():
	try:
		with open('dog.txt') as file_t:
			buf = file_t.read()
			print(buf)
		with open('cat.txt') as file_t:
			buf = file_t.read()
			print(buf)
	except FileNotFoundError:
		#print('No find the file,please cheak!')		#10.8
		pass											#10.9

read_file()


#10.10
#count('xx') 查找字符串中的xx字眼个数
line = 'hello,word!Python is fine python is ku'
print(line.lower().count('python'))

#10.11
def input_number():
	num = input('pleas input a you favorite number:')
	with open('json_num.json', 'w') as file_t:
		json.dump(num, file_t)

def read_number():
	with open('json_num.json') as file_t:
		num = json.load(file_t)
	print('Your favrite like number is ' + num)

#input_number()
#read_number()


#10.12
def like_number():
	try:
		read_number()
	except FileNotFoundError:
		input_number()
	else:
		print('l know')
	
like_number()














