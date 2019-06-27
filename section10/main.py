#****************************************************************************************************#
# time:2019.6.26
#test tipoc
#****************************************************************************************************#
"""文件操作、异常处理、json"""
import json

tip = '*--------------------------------------------*\r\n'

#访问文件操作，使用with可以不用关心关闭文件，python会自动帮你关闭
with open('pi.txt') as pi_file:
	pi_buffer = pi_file.read()
	print(pi_buffer.rstrip())	#文件的末尾会有一个空行，这里rstrip()用来删除文件末尾的空行

#打开关闭文件操作
pi_file1 = open('pi.txt')
print(pi_file1.read())
pi_file1.close()

#访问不同路径的文件，在win中路径使用‘\’，mac/linux中使用‘/’
addres = r'file\cat.txt'
with open(addres) as file_t:
	print(file_t.read().rstrip())
	
addres = r'D:\yefeng\python-test\FileTxt\pizza.txt'
with open(addres) as file_t:
	print(file_t.read().rstrip())

#此方法不支持打开含有中文的文件
addres = r'..\FileTxt\pizza.txt'
with open(addres) as file_t:
	print(file_t.read().rstrip())

#readlines()是读取行的
addres = 'pi_million_digits.txt'
with open(addres) as file_t:
	lines = file_t.readlines()

pi_str = ''
for line in lines[:5]:
	pi_str += line.strip()

print(pi_str)	

#逐行读取
addres = 'pi.txt'
with open(addres) as file_t:
	for line in file_t:
		print(line.rstrip())

#写文件,‘w’方法会先清空文件再写入
addres = 'jsontest.txt'
with open(addres, 'w') as file_t:
	file_t.write('hello python!')

#写文件，‘a’方法会在文件的末尾加入
with open(addres, 'a') as file_t:
	file_t.write('hello yefeng!')
	
#写JSON格式的文件
addres = 'jsonfile.json'
with open(addres, 'w') as file_t:
	json.dump('hello python!', file_t)

#读JSON格式文件
with open(addres) as file_t:
	jsonbuf = json.load(file_t)
print(jsonbuf)






























