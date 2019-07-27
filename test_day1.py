#!/usr/bin/env python3

print("hello word")

massage = "hello python"
print(massage)

#首字母大写
print(massage.title())

#全部大写
print(massage.upper())

#全部小写
print(massage.lower())

#合并
frist = 'ye'
last = 'feng'
allstr = frist + ' ' + last
print(allstr) 

#删除空白/空格
massage = ' python ！ '
print(massage.rstrip()) #删尾部
print(massage)
print(massage.strip()) #删头部
print(massage.lstrip()) #两边删
