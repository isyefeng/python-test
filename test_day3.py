# time:2019.6.16
#test tipoc
tip = '*--------------------------------------------*\r\n'
names = ['yefeng','linghanhong','liuyan']
print('welcome ' + str(names))
print(tip)

print(names[2] + '无法来，换人')
names[2] = 'jiecheng'
print('welcome ' + str(names))
print(tip)

print('还能邀请多3人')
names.insert(0,'liuyan')
names.insert(2,'wangfeng')
names.append('zhanggong')

print(names)

print('缩减名单')
name = names.pop()
print('抱歉你不能来了' + name + '\r\n还剩' + str(len(names)) + '人')
name = names.pop()
print('抱歉你不能来了' + name + '\r\n还剩' + str(len(names)) + '人')
name = names.pop()
print('抱歉你不能来了' + name + '\r\n还剩' + str(len(names)) + '人')
name = names.pop()
print('抱歉你不能来了' + name + '\r\n还剩' + str(len(names)) + '人')
del names[len(names) - 1]
print(names)
del names[len(names) - 1]
print(names)
print(tip)

location = ['china','meiguo','taiguo','faguo']
print('去这些地方：' + str(location))
print('单次顺序排序：' + str(sorted(location)))
print('单次反向顺序排序' + str(sorted(location,reverse = True)))
print(location)
location.reverse()
print('反向：' + str(location))
location.reverse()
print('再反向：' + str(location))
location.sort()
print('永久顺序排序：' + str(location))
location.sort(reverse = True)
print('永久反序排序：' + str(location))

locations = ['中国','美国','泰国']
print(locations)
locations.sort()
print('实测sort()方法中文无法顺序排序：' + str(locations))
print(tip)

#遍历列表
#for循环
miagicians = ['aa','bb','cc','dd','ee']
for buffer in miagicians:
	print(buffer.title() + '遍历列表\r\n')

pisa = ['猫王','烤肉','芝士']
print('我爱吃的披萨')
for buffer in pisa:
	print(buffer)

print('\r\n')
for buffer in pisa:
	print(buffer)
	print('l like pepperoni pizza!')

print('l really love pizza')

#数字列表
#list()方法创建列表
#使用reage(x,y,z)方法创建 x:开始 y：结束 z:累加间隔
number =  list(range(0,5))
print(number)

for num in range(0,10,2):
	print(num)
	
cnt = []
for num in range(1,10):
	cntbuf = num**2  # ** 是幂运算
	cnt.append(cntbuf)
print(cnt)

#列表解析
cnts = [buf**2 for buf in range(1,10)]
print(cnts)

#tipoc
for buf in range(1,21):
	print(buf)


lists = range(1,1000000)
#for buf in lists:
	#print(buf)
	
print(max(lists))
print(min(lists))
print(sum(lists))

jishu = range(1,21,2)
for buf in jishu:
	print(buf)

#能被3整除的 3,30的数
ls_3 = range(3,31,3)
for buf in ls_3:
	print(buf)
	
#1-10的3次幂
ls_x3 = [buf**3 for buf in range(1,11)]
for buf in ls_x3:
	print(buf)
print(tip)
	
#切片
#xxx[x:y] 从x号元素到y号元素，如果x为空，则从最开始到y；如果y为空，则从x到结尾

#复制列表
list_ers = miagicians[:]
print(list_ers)
list_ers = miagicians[1:3]
print(list_ers)



























