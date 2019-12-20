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

print('--------------------------------------------')
'''缺失值处理'''
df = pd.read_csv('null.csv')
print(df.info())  #info 可以查看到某一列有多少个非缺失（非空）的值
print(df.isnull())  #isnull 如果是缺失值返回True 否则返回 False
print(df.dropna()) #删除有空值的那一行数据
print(df.dropna(how='all')) #how = 'all' 当整行缺失时才删除
#缺失值的填充
print(df.fillna(0)) #使用fillna()方法填充，这里表示全填充0
print(df.fillna({'性别':'女','年龄':18}))

#删除重复行
print(df.drop_duplicates()) #默认不填参数是一模一样时保留第一个
print(df.drop_duplicates(subset = '年龄')) #指定列
print(df.drop_duplicates(subset = ['年龄','性别'])
#print(df.drop_duplicates(subset = ['年龄','性别'], keep(last)) '''keep 是保留哪一个相同项，first是保留第一个，last是保留最后一个，F alse删除全部'''