from numpy import *
import operator
from plt_wave import *

'''创建K临近算法的原始数据'''
def creatDataSet():
	'''创建一个矩阵数组'''
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels

'''
	K临近算法实施例子
	inX:需要预测的对象，这个对象应该是一个有对象属性的列表
	dataset:数据的原始样本
	lables:原始样本所属类别
	k:目标对象与k个最邻近他的对象进行对比
	----------------------------------------------------
	距离计算公式（欧氏距离公式）
	d=（(xA0-xB0)^2+(xA1-xB1)^2+......）^1/2
	----------------------------------------------------
	
'''
def classify0( inX, dataset, lables, k ):
	datasetsize = dataset.shape[0]  								#计算原始数据的行数（多少个数据）  如果是shape 则会返回（4,2）shape[0]是行数，shape[1]元素数
	'''计算inX与原始数据的距离,使用欧拉距离计算公式'''
	diffMat = tile(inX, (datasetsize,1)) - dataset 					#将目标数据复制成与样本数据相同行数的矩阵数据，并进行矩阵相减运算（xA-xB）
	print(diffMat)
	print('--------------')
	sqDiffMat = diffMat**2											#矩阵平方运算(xA-xB)^2
	print(sqDiffMat)
	print('--------------')
	sqDistances = sqDiffMat.sum(axis=1)								#行求和
	print(sqDistances)
	print('--------------')
	distamces = sqDistances**0.5                                    #开方
	print(distamces) 
	print('--------------')

	sorteDistIndicies = distamces.argsort()							#argsort() 返回数组值从小到大的索引 
	print(sorteDistIndicies)
	print('--------------')
	classCount = {}
	for i in range(k): 												#距离越小，越相似
		voteIlabel = lables[sorteDistIndicies[i]]					#查找前K个最小距离所属分类
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1	#合计前K个最邻近对象的数量（将对象类别些为键，对象的数量写为值.eg:{A:2,B:1} 这时K=3,A接近目标对象较多，所目标对象为A类）
	print(classCount)
	
	sortedClassCount = sorted(classCount.items(), key=lambda x:x[1],reverse=True)	#
	print(sortedClassCount)
	return sortedClassCount[0][0] #返回最多个点的数类型
    
 
'''
    将数据文件转换成矩阵数据
'''
def file2matrix( filename ):
    fr = open(filename)                             #读取文件
    arrayOLines = fr.readlines()                    #按行获取信息
    numberfrOLinex = len(arrayOLines)               #行数
    returnMat = zeros((numberfrOLinex,3))           #以0位参数创建一个矩阵
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line.strip()                                # strip(x)方法 删除字符串头尾的x值（x默认为字符串或空格）
        listFromLine = line.split('\t')             # split(x)方法 字符串按x来切片 比如 'xabxscxwfxsdx'.split('x')  ====> ['ab','sc','wf'...]
        returnMat[index,:] = listFromLine[0:3]      # 给矩阵赋值
        classLabelVector.append(int(listFromLine[-1]))  #获取分类
        index = index + 1
    return returnMat, classLabelVector

a,b = creatDataSet()
print('属于'+classify0([0.7,0.5], a, b, 3)+'类')

array,classvector = file2matrix('datingTestSet2.txt')
DisplayWave(array[:,1],array[:,2])





























	