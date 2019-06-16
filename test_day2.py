# time:2019-6-15
tip = '*------------------------------------------------*\r\n'
#test tipoc
name = 'yefeng'
print('Hello ' + name + ',would you like to learn some Python tody\r\n')

print('Hello ' + name.title() + ',would you like to learn some Python tody\r\n')

name = ' yefeng '
print('Hello ' + name.rstrip() + ',would you like to learn some Python tody\r\n')
print('Hello ' + name.strip() + ',would you like to learn some Python tody\r\n')

arg = 22
print('name:' + name.strip() + '\r\n' + 'arg:' + str(arg))

#列表，类似于C的数组 -1号元素代表从最后一个开始算起
names = ['yefeng','linghanhong','jiecheng','liuyan']
print(names)
print(names[0].title() + ' ' + names[2] +  ' ' + names[-1])

#修改，添加，插入，删除列表元素
motos = ['honda','yamaha','suzuki']
#修改
motos[0] = 'ducati'
print(motos)

#添加 user append(data)方法 在末尾添加 data：数据
motos.append('honda')
print(motos)

#插入 user insert(x,data)方法 在x位置插入data数据
motos = ['honda','yamaha','suzuki']
motos.insert(1,'ducati')
print(motos)
print(tip)

#删除 user del ro pop(x)方法 
#del 直接删除
#pop() 可回读一次删除数据 x默认不写的话删除最后一个元素
del motos[1]
print(motos)
print(tip)

motos_buf = motos.pop()
print(motos)
print('delet data is: ' + motos_buf)
print(tip)

motos = ['honda','yamaha','suzuki']
motos_buf = motos.pop(1)
print(motos)
print('delet data is: ' + motos_buf)
print(tip)

#根据数值删除元素 remove(data)
motos = ['honda','yamaha','suzuki']
print(motos)
motos_buf = 'yamaha'
motos.remove(motos_buf)
print(motos)
print('delet data is: ' + motos_buf)
print(tip)



