from math import *
from matplotlib import pyplot as plt

sinfilename = 'sin.txt'

'''
生成整数型的sin值数组，省略了小数
file:生成文件名
size:长度
A:幅度
B:直流分量
'''
def CreatSinINTArray(file='SinDataFile.txt', size=100, A=1, B=0):
	data = []
	for i in range(size):
		angle = (i*2*3.14159)/size
		data.append(int(sin(angle)*A+B))
	with open(file,'w') as f:
		f.write( str(data) )
	return data

'''
生成小数型sin值数组
file:生成文件名
size:长度
A:幅度
B:直流分量
'''
def CreatSinArray(file, size, A, B):
	data = []
	for i in range(size):
		angle = (i*2*3.14159)/size
		data.append(sin(angle)*A+B)
	with open(file,'w') as f:
		f.write( str(data) )
	return data
		
'''show the sin arrays'''
def ShowSinWave( arrays ):
	x_line = range(len(arrays))
		
	fig = plt.figure(dpi=128,figsize=(10,6))
	
	#s 表示散点的大小，形如 shape (n, )
    #label 表示显示在图例中的标注
    #alpha 是 RGBA 颜色的透明分量
    #edgecolors 指定三点圆周的颜色    
	plt.xlabel('x',fontsize=14)
	plt.ylabel('y',fontsize=14)
	plt.scatter(x_line, arrays, edgecolor='none', s=40)
	
	#plt.ylim(-1,6)
	plt.plot(x_line, arrays, c='red')								#alpha:透明度

	plt.title('PID',  fontsize = 24)
	plt.xlabel('time', fontsize = 15)
	plt.ylabel('PID-DA-OUT(V)', fontsize = 15)
	fig.autofmt_xdate()
	plt.show()
	
#CreatSinINTArray(sinfilename, 512, 850, 850)
#ShowSinWave(CreatSinINTArray(sinfilename, 512, 750, 900))




