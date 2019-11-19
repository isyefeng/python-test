#调用整个模块的函数，使用前需要加前缀
#import pizza
#pizza.make_pizza('rn','zr','sc')

#仅调用pizza模块的make_pizza函数
#from pizza import make_pizza
#make_pizza('rn','zr','sc')

#仅调用pizza模块的make_pizza函数，并将make_pizza函数改名为pi
#from pizza import make_pizza as pi
#pi('rn','zr','sc')

#调用整个模块的函数，并将模块重新定义名字为ppi
#import pizza as ppi
#ppi.make_pizza('rn','zr','sc')

#调用pizza模块的全部函数，并且不用加前缀调用
from pizza import*
make_pizza('rn','zr','sc')
