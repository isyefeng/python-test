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


print(df)
