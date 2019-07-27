#!/usr/bin/env python3
'''这是一个搜索GITHUB中JAVA按星星排名，创建前30的项目条形图及github链接'''
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'

r = requests.get(url)
print('url code:' + str(r.status_code))		#打印响应码  响应码为200表示成功

requests_json = r.json()

repo_dicts = requests_json['items']

#print(repo_dicts[0].keys())

print('total count:' + str(requests_json['total_count'])) #打印项目数

print('Github NO.1 Java project is ' + repo_dicts[0]['name'])

name,plot_dicts = [],[]

for repo in repo_dicts:				#查看github上前30的python开源项目
	#将API中的项目名称和星星数添加到列表中
	name.append(repo['name'])
	plot_dict = {
		'value':repo['stargazers_count'],
		'label':repo['description'],
		'xlink':repo['html_url']
		}
	plot_dicts.append(plot_dict)
	
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

chart.title = 'Most-Starred java project on github'
#设置X轴数据
chart.x_labels = name					
#添加数据
chart.add('', plot_dicts)
chart.render_to_file('Java_repos.svg')


















