#****************************************************************************************************#
# time:2019.6.17
#test tipoc
#****************************************************************************************************#

tip = '*--------------------------------------------*\r\n'


lists = ['aa','bb','cc','dd','ee','ff','gg']
lists_cp = lists
print(lists)
print(lists_cp)
#这种方式不属于列表的复制，属于一种类似映射的方式，当改变lists时  lists_cp也会跟着改变
lists_cp[1] = 'cc'
print(lists_cp)
print(lists)

#****************************************************************************************************#
print('切片打印前三个元素')
print(lists[:3])

num = int(len(lists)/2)
print('切片打印中间三个元素')
print(lists[(num-1):(num+2)])

print('切片打印末尾三个元素')
print(lists[-3:])

pisa = ['猫王','烤肉','芝士']
pisa_cp = pisa[:]
pisa.append('牛肉')
pisa_cp.append('尖椒')
print('第一个列表')
for buf in pisa:
	print(buf)

print('第二个列表')
for buf in pisa_cp:
	print(buf)

print(tip)

#元组，不可修改的，但是可以对整个元组赋值，从而改变元组
foods = ('ega','apple','banana')
for buf in foods:
	print(buf)

#foods[0] = 'aa'   不可以这样修改
foods = ('aa','bb','cc')
print(foods)

print(tip)
#****************************************************************************************************#
#if 语句的使用
ifbuf = 'Yefeng'
if ifbuf == 'yefeng':
	print('True')
else:
	print('False')

if ifbuf.lower() == 'yefeng':
	print(ifbuf)
	print('True')
else:
	print('False')

print(ifbuf.upper())
print(ifbuf)

#and 和 or 的使用  and（与） or（或）
num1 = 10
num2 = 15
if num1 >= 5 and num2 >=10:
	print('True')
else:
	print('False')
	
if num1 <= 5 and num2 >=10:
	print('True')
else:
	print('False')

if num1 <= 5 or num2 >=10:
	print('True')
else:
	print('False')

#in 的用法  判断列表中是否存在某元素
#not in 用法和in相反，判断某元素是否不再列表中
inbuf = pisa[:]
print(inbuf)
num = '猫王' in inbuf
print(num)




















	
