from math import *
import numpy as np
import re
from matplotlib import pyplot as plt

'''
f(x) = Asin(wt+φ)+B
'''

winname=[]

def CreatSinArray(file='sin.txt', size=100, A=1, B=0, f=50, offset = 0):
	data = []
	winname = str(A)+'sin(2pi*'+str(f)+'T+'+str(offset)+')+'+str(B)
	print(winname)
	angleoffset = 0
	offsettime = 1/(f*size)
	print(offsettime)
	for i in range(size):
		angle_s = (2*(pi)*angleoffset)*f
		angle = angle_s + (2*(pi)*offset/360)
		data.append(sin(angle)*A+B)
		angleoffset = angleoffset + offsettime
	with open(file,'w') as f:
		f.write( str(data) )
	return data

def xbSinCreat():
	bascsin = np.array( CreatSinArray(A=500,offset=90))
	xbsin_1 = np.array( CreatSinArray(A=200,f=30,offset=20))
	xb = bascsin+xbsin_1
	ShowSinWave(xb, winname,'x','y')

'''show the sin arrays'''
def ShowSinWave( arrays , title, x_title, y_title):
	x_line = range(len(arrays))
		
	fig = plt.figure(dpi=128,figsize=(10,6))
	
	#s 表示散点的大小，形如 shape (n, )
    #label 表示显示在图例中的标注
    #alpha 是 RGBA 颜色的透明分量
    #edgecolors 指定三点圆周的颜色    
	plt.scatter(x_line, arrays, edgecolor='none', s=40)
	
	#plt.ylim(-1,6)
	plt.plot(x_line, arrays, c='red')								#alpha:透明度

	plt.title(title,  fontsize = 24)
	plt.xlabel(x_title, fontsize = 15)
	plt.ylabel(y_title, fontsize = 15)
	fig.autofmt_xdate()
	plt.show()

xbSinCreat()


