#!/usr/bin/env python3

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print('url code:' + str(r.status_code))		#打印响应码  响应码为200表示成功

requests_json = r.json()

print(requests_json.keys())

print('total count:' + str(requests_json['total_count'])) #打印项目数

repo_dicts = requests_json['items']
print('repositories returned:' + str(len(repo_dicts)))

#研究第一个仓库
repo_dict = repo_dicts[0]
print('key:',len(repo_dict))
'''
for keys in repo_dict.keys():
	print(keys)
'''

print('Github NO.1 project is ' + repo_dict['name'])

index = 0
#name,stars = [],[]			#采集项目名称及点赞数
name,plot_dicts = [],[]

for repo in repo_dicts:				#查看github上前30的python开源项目
	index += 1
	print(index,repo['name'])
	#将API中的项目名称和星星数添加到列表中
	name.append(repo['name'])
	plot_dict = {
		'value':repo['stargazers_count'],
		'label':repo['description'],
		'xlink':repo['html_url']
		}
	plot_dicts.append(plot_dict)
	#stars.append(repo['stargazers_count'])
	
#设置样式，LS设置数据条为深蓝色 #333366
#x_label_robel_rotation = 45  是让X轴的数据类型旋转45度
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.tyrbcate_label = 15		#x轴名字最长是15个字
my_config.show_y_guides = False		#隐藏虚线
my_config.width = 1000				#设置宽度

chart = pygal.Bar(my_config, style=my_style)

#chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
#这里是没有设置样式的
#chart = pygal.Bar( x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python project on github'
#设置X轴数据
chart.x_labels = name					
#添加数据
chart.add('', plot_dicts)
chart.render_to_file('Python_repos.svg')


''''鼠标悬停显示提示信息'''
def cheak_info():
	chart = pygal.Bar()
	chart.title = 'Python Project'
	chart.x_labels = ['httpie','label','description']
	plot = [
	{'value':1610,'label':'description of httpie'},
	{'value':1244,'label':'description of label'},
	{'value':1630,'label':'description of decription'}
	]
	
	chart.add('',plot)
	chart.render_to_file('Python_info.svg')
	
#cheak_info()































