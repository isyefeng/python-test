'''定义learinig_logs的URL模式'''
from django.conf.urls import url

from . import views

urlpatterns=[
	#主页
	#第一个参数是匹配url请求
	#第二个参数是画界面的，第三个参数是这个URL模块的名称
	url(r'^$', views.index, name='index')
]





