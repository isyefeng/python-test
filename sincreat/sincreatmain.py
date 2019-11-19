import wx
from math import *
from matplotlib import pyplot as plt

'''
parent = None #父元素，假如为None，代表顶级窗口 
id = None #组件的标识，唯一，假如id为-1代表系统分配id
title = None #窗口组件的名称
pos = None #组件的位置，就是组件左上角点距离父组件或者桌面左和上的距离
size = None #组件的尺寸，宽高
style = None #组件的样式
name = None #组件的名称，也是用来标识组件的，但是用于传值
'''

strint = 'int'
strfloat = 'float'

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

	plt.title('f(x)=Asin(x)+B',  fontsize = 24)
	plt.xlabel('X', fontsize = 15)
	plt.ylabel('Y', fontsize = 15)
	fig.autofmt_xdate()
	plt.show()

'''定义事件函数'''
def creatfile(event):
	A = int(A_text.GetValue()) #获取文文本框内容
	B = int(B_text.GetValue())
	NUM = int(num_text.GetValue())
	FILE = file_text.GetValue()
	DataType = radiobox3.GetSelection()
	if DataType == 0:
		start = CreatSinINTArray(FILE, NUM, A, B)
	elif DataType == 1:
		start = CreatSinArray(FILE, NUM, A, B)
	if start:
		wx.MessageBox("OK!")
	else:
		wx.MessageBox("ERROR")

def DisplaySinWave(event):
	A = int(A_text.GetValue()) #获取文文本框内容
	B = int(B_text.GetValue())
	NUM = int(num_text.GetValue())
	FILE = file_text.GetValue()
	DataType = radiobox3.GetSelection()
	print(DataType)
	if DataType == 0:
		ShowSinWave(CreatSinINTArray(FILE, NUM, A, B))	
	elif DataType == 1:
		ShowSinWave(CreatSinArray(FILE, NUM, A, B))	
	
'''	
def typeChange(event):
	print(radiobox3.GetStringSelection(),'---',radiobox3.GetSelection())
	print(event.GetString(),event.GetInt())
'''

app = wx.App() #实例化一个主循环
frame = wx.Frame(None, title = '正弦数组生成器',pos = (1000,200),size = (350,260))#实例化一个窗口

'''创建编辑框'''
wx.StaticText(frame, label = 'f(x) = Asin(x)+B',pos=(5,5))
wx.StaticText(frame, label = 'A:',pos=(5,30))
wx.StaticText(frame, label = 'B:',pos=(100,30))
wx.StaticText(frame, label = 'NUM:',pos=(200,30))
wx.StaticText(frame, label = 'FileName:',pos=(5,60))
A_text = wx.TextCtrl(frame, pos = (25,25), size = ( 60,24)) #
B_text = wx.TextCtrl(frame, pos = (125,25), size = ( 60,24)) #
num_text = wx.TextCtrl(frame, pos = (250,25), size = ( 60,24)) #
file_text = wx.TextCtrl(frame, pos = (70,55), size = ( 200,24)) #

'''并选框'''
list3 = ["int","float" ]
#RadioBox(parent, id=ID_ANY, label=EmptyString, pos=DefaultPosition, size=DefaultSize, 
#         choices=[], majorDimension=0, style=RA_SPECIFY_COLS, validator=DefaultValidator, name=RadioBoxNameStr)               
radiobox3 = wx.RadioBox(frame,-1,"选择数据类型",pos=(100,90),choices=list3,style=wx.RA_SPECIFY_COLS)
#radiobox3.Bind(wx.EVT_RADIOBOX,typeChange)

creat_button = wx.Button(frame,label = '生成',pos = (60,180),size = (90,24)) #创建按钮
creat_button.Bind(wx.EVT_BUTTON, creatfile) #绑定时间到open_button按钮上

display_button = wx.Button(frame,label = '显示图像',pos = (160,180),size = (90,24))
display_button.Bind(wx.EVT_BUTTON, DisplaySinWave)


frame.Show() #调用窗口展示功能
app.MainLoop() #启动主循环


	


	

