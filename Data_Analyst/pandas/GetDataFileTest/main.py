import pandas as pd

#读取Excel文件
df = pd.read_excel('test.xlsx')

#指定读取某一个sheet
df = pd.read_excel('test.xlsx', sheet_name = "Sheet1")

#从某一列开始读取,第二列开始按顺序
df = pd.read_excel('test.xlsx', sheet_name = "Sheet1", index_col = 1)

#从某一行开始读
df = pd.read_excel('test.xlsx', header = 1)

#导入指定的列,这个usecols可以是一个列表
df = pd.read_excel('test.xlsx', usecols = 0)
df = pd.read_excel('test.xlsx', usecols = [1,3])

'''导入csv文件'''
df = pd.read_csv('testcsv.csv', sep = ',') #sep 指明csv文件的分隔符，默认是逗号，也可以是空格或其他好分辨的符号

df = pd.read_csv('testcsv.csv', nrows = 2) #nrows 读取行数

df = pd.read_csv('testcsv.csv', encoding = 'utf-8', engine  = 'python') #encoding指定编码格式 engine指定解析语言，默认是C，是不支持中文路径的，换成python才可以使用中文路径


df = pd.read_table('testcsv.csv', encoding = 'utf-8', sep = ',') #指定编码格式

print(df.head())#默认显示前5行
print(df.head(2))#只显示两行
print(df.shape) #显示行列数
print(df.info()) #显示信息
print(df.describe()) #求均值、分布、最大、最小.....
print(df)




