#!/usr/bin/env python3
'''video dsp fice read'''


#人脸识别器官	
def fice_read(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	#将图片你转化为灰色
	
	# OpenCV人脸识别分类器
	classifier = cv2.CascadeClassifier(
		r"/Users/yefeng/Desktop/python-test/ficedriver/haarcascade_frontalface_default.xml"				#\u是转义字符 所以前面要加r  不然会识别不到文件位置
	)
	color = (0, 255, 0)  # 定义绘制颜色
	
	#调用人脸识别
	faceRects = classifier.detectMultiScale(
		gray, scaleFactor=1.2, minNeighbors=3, minSize=(32,32))
		
	if len(faceRects):  #大于0检测到人脸
		for faceRect in faceRects:		#遍历人脸数量
			x,y,w,h = faceRect	
			#框出人脸
			cv2.rectangle(img, (x,y), (x+h,y+w), color, 2)  #绘制矩形
	cv2.imshow("image",img)
			



import cv2
cap = cv2.VideoCapture(0)
while True:
	ret,imag = cap.read()
	fice_read(imag)
#	cv2.imshow("Image", img)				#将视频一帧一帧的显示
	if (cv2.waitKey(1)&0xff)==ord('q'):  	#检测到按键是q的话就退出
		break
cap.release()								#释放摄像头
cv2.destroyAllWindows()						#释放窗口资源




