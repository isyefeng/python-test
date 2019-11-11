from socket import *

'''creat a basc IPV4 and  TCP protocol socket'''
s=socket(AF_INET, SOCK_STREAM)
#绑定监听IP地址和端口号
#自定义的端口号最好是大于1024的数，因为小于1024的数一般是WED协议使用了
s.bind(('127.0.0.1',9999))

s.close()





