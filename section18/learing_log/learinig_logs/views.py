from django.shortcuts import render

# Create your views here.
def index(request):
	'''
	index url模块的首页图像
	返回html文件的位置给diango
	'''
	return render(request, 'learinig_logs/index.html')






