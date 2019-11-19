import wx
'''
parent = None #父元素，假如为None，代表顶级窗口 
id = None #组件的标识，唯一，假如id为-1代表系统分配id
title = None #窗口组件的名称
pos = None #组件的位置，就是组件左上角点距离父组件或者桌面左和上的距离
size = None #组件的尺寸，宽高
style = None #组件的样式
name = None #组件的名称，也是用来标识组件的，但是用于传值
'''

'''定义事件函数'''
def openfile(event):
	path = path_text.GetValue() #获取文文本框内容
	with open(path,"r",encoding="utf-8") as f:
		content_text.SetValue(f.read())
		

app = wx.App() #实例化一个主循环
frame = wx.Frame(None, title = 'GUI TEST EDITOR',pos = (1000,200),size = (500,400))#实例化一个窗口

#自定义位置
'''
path_text = wx.TextCtrl(frame, pos = (5,5), size = ( 350,24)) #创建文本编辑框
open_button = wx.Button(frame,label = '打开',pos = (370,5),size = (50,24)) #创建按钮
open_button.Bind(wx.EVT_BUTTON, openfile) #绑定时间到open_button按钮上

save_button = wx.Button(frame,label = '保存',pos = (430,5),size = (50,24))

content_text = wx.TextCtrl(frame, pos = (5,39), size = (475,300), style = wx.TE_MULTILINE)
#  wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行
'''
#使用尺寸器
panel = wx.Panel(frame)

path_text = wx.TextCtrl(panel)
open_button = wx.Button(panel, label = 'open')
open_button.Bind(wx.EVT_BUTTON, openfile)

save_button = wx.Button(panel, label = 'save')

content_text = wx.TextCtrl(panel, style = wx.TE_MULTILINE)

box = wx.BoxSizer() #不带参数表示默认实例化一个水平尺寸器
box.Add(path_text,proportion = 5,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
    #proportion：相对比例
    #flag：填充的样式和方向,wx.EXPAND为完整填充，wx.ALL为填充的方向
    #border：边框
box.Add(open_button,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
box.Add(save_button,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件

v_box = wx.BoxSizer(wx.VERTICAL) # wx.VERTICAL参数表示实例化一个垂直尺寸器
v_box.Add(box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
v_box.Add(content_text,proportion = 5,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件

panel.SetSizer(v_box) # 设置主尺寸器

frame.Show() #调用窗口展示功能
app.MainLoop() #启动主循环


	


	

