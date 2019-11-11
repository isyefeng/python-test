import socket
'''建立socket连接'''
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''连接新浪服务器'''
s.connect(('www.sina.com.cn',80))
'''发送请求'''
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

'''创建一个死循环接收数据'''
buffer=[]
while True:
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break;
'''将buffer列表用b''连接起来组成新的字符串  join()方法'''
data=b''.join(buffer) 
'''关闭socket连接'''
s.close()
'''将字符从b'\r\n\r\n'开始串分割成2个元素的列表'''
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8')) 
#将数据写入文件中
with open('sina.html','wb') as f:
	f.write(html)

