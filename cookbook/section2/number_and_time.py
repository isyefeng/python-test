'''cookbook section test'''
from decimal import Decimal   #精确浮点运算模块

'''
数字的四舍五入
round（a,b） a:数字  b:做摄入运算的位数
'''

#浮点数的舍入运算b为正数
num = round(4.22341, 3)

#正数的摄入运算b为负数
num = round(123456, -2)

#print(num)

'''
精确的浮点运算
'''

a=4.2
b=2.1
c=a+b
print('4.2+2.1='+str(c))
print('python通病，由于底层CPU浮点运算单元引起，如果需要非常精确的')
print('运算，可使用decimal模块，前提是要牺牲一些性能')

a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)

'''
数字格式化输出  format方法
str.format（'表达式'）
format(num, '表达式')
'''
x = 123.4567
print('%.2f' % x)
print(format(x,'0.2%'))

'''
二八十六进制转换
'''
print('--------------------------------------')
x=1234
print('bin:'+str(bin(x)))
print('oct:'+str(oct(x)))
print('hex:'+str(hex(x)))

print('format')
print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))

print(int('0x255',16))
