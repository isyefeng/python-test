#****************************************************************************************************#
# time:2019.6.25
#test tipoc
#****************************************************************************************************#
from restanrant import Restaurant,IceCream
from user import User,Admin,AdminRoot
from random import randint
#from restanrant import *
#from user import *

tip = '*--------------------------------------------*\r\n'

#创建一个实例res
res = Restaurant('kfc','snack')
print('-' + res.restaurant_name)
print('-' + res.cuisine_type)

res.describe_restaurant()
res.open_restaurant()
res.restaurant()
res.number_served = 23
res.restaurant()
print('\n')


sj = Restaurant('sjms','kc')
sj.describe_restaurant()
sj.set_number_served(15)
sj.restaurant()
print('\n')

ys = Restaurant('yskc','fd')
ys.describe_restaurant()
ys.set_number_served(15)
ys.increment_number_served(7)
ys.restaurant()
print('\n')
print(tip)
#****************************************************************************************************#

ye = User('ye','feng')
ye.descride_user()
ye.greet_user()

lin = User('lin','hh','hello lin!')
lin.descride_user()
lin.greet_user()

for num in range(10):
	lin.increment_login_attempts()

print('Login number is:' + str(lin.login_attempts))
lin.reset_login_attempts()
print('Login number is:' + str(lin.login_attempts))
print(tip)
#****************************************************************************************************#

ice = IceCream('hgds','icecream')
ice.describe_restaurant()
ice.dsp_icecream_list()
print(tip)
#****************************************************************************************************#

root = Admin('y','f')
root.descride_user()
root.greet_user()
root.dsp_admin_privilege()

kh_yf = AdminRoot('l','hh')
kh_yf.descride_user()
kh_yf.greet_user()
kh_yf.root.dsp_admin_privilege()   #调用AdminRoot类内部实例化的root类的dsp_admin_privilege函数
print(tip)
#****************************************************************************************************#

#调用标准库方法
for num in range(6):
	print(randint(1,6))

















