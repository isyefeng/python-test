# coding:utf-8
import serial
import serial.tools.list_ports
import time

portx41 = "COM41"
portx46 = 'COM46'

def SearchSerial():
	plist = list(serial.tools.list_ports.comports())
	 
	if len(plist) <= 0:
		print("没有发现端口!")
	else:
		plist_0 = list(plist[0])
		serialName = plist_0[0]
		serialFd = serial.Serial(serialName, 9600, timeout=60)
		print("可用端口名>>>", serialFd.name)



def ConnectSerial( portx ):
	try:
		bps=115200
		#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
		timex=None
		ser=serial.Serial(portx,bps,timeout=timex)
		print("串口详情参数：", ser)

		#十六进制的发送
		for cnt in range(100):
			result=ser.write(chr(0xaa).encode("utf-8"))
			time.sleep(1)


		print("写总字节数:",result)

		#十六进制的读取
		print(ser.read().hex())#读一个字节

		print("---------------")
		ser.close()#关闭串口

	except Exception as e:
		print("---异常---：",e)

SearchSerial()		
ConnectSerial(portx46)		

		
		
