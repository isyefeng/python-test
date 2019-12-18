from numpy import *
import operator

'''创建K临近算法的原始数据'''
def creatDataSet():
	'''创建一个矩阵数组'''
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels

'''
	K临近算法实施例子
	
'''
def classify0( inX, dataset, lables, k ):
	datasetsize = dataset.shape[0]  #计算原始数据的行数（多少个数据）  如果是shape 则会返回（4,2）shape[0]是行数，shape[1]元素数
	'''计算inX与原始数据的距离,使用欧拉距离计算公式'''
	diffMat = tile(inX, (datasetsize,1)) - dataset #
	print(diffMat)
	print('--------------')
	sqDiffMat = diffMat**2
	print(sqDiffMat)
	print('--------------')
	sqDistances = sqDiffMat.sum(axis=1)
	print(sqDistances)
	print('--------------')
	distamces = sqDistances**0.5
	print(distamces)
	print('--------------')

	sorteDistIndicies = distamces.argsort()	#argsort() 返回数组值从小到大的索引 
	print(sorteDistIndicies)
	print('--------------')
	classCount = {}
	for i in range(k): 														#距离越小，越相似
		voteIlabel = lables[sorteDistIndicies[i]]							#查找前K个最小距离所属分类
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	print(classCount)
	
	sortedClassCount = sorted(classCount.items(), key=lambda x:x[1],reverse=True)
	print(sortedClassCount)
	return sortedClassCount[0][0] #返回最多个点的数类型
	'''
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]
	'''
	

a,b = creatDataSet()
print('属于'+classify0([0.7,0.5], a, b, 3)+'类')
	