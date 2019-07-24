import cv2

def cv2_test():
	imagename = 'a1.jpg'			
	img = cv2.imread(imagename)		#获取一张图片
	cv2.namedWindow('Image')		#设置标题
	cv2.imshow('Image', img)		#显示图片
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#cv2_test()

'''
分类器classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))参数说明：

gray：转换的灰图

scaleFactor：图像缩放比例，可理解为相机的X倍镜

minNeighbors：对特征检测点周边多少有效点同时检测，这样可避免因选取的特征检测点太小而导致遗漏

minSize：特征检测点的最小尺寸
'''

#人脸识别器官	
def fice_read():
	filename = 'timg1.jpg'
	img = cv2.imread(filename)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	#将图片你转化为灰色
	
	# OpenCV人脸识别分类器
	classifier = cv2.CascadeClassifier(
		r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"				#\u是转义字符 所以前面要加r  不然会识别不到文件位置
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
			'''
			 # 左眼
			cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),			#circle画圆
					   color)
			#右眼
			cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
					   color)
			#嘴巴
			cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
						  (x + 5 * w // 8, y + 7 * h // 8), color)
						  
			'''

			
	'''
	x = y = 10										#坐标
	w = 100											#矩形大小
	color = (0,0,255)								#绘制颜色
	cv2.rectangle(img, (x,y), (x+w,y+w), color, 1)  #绘制矩形
	'''
	
	cv2.imshow('Image',img)
	c = cv2.waitKey(10)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
fice_read()	
	