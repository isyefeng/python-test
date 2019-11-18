import pandas as pd

'''Series'''
s1 = pd.Series([1,2,3,4,5])
print(s1)

print(s1.index) #查看索引
print(s1.values)    #查看值

#更改索引index
s2 = pd.Series(['a','b','c','d','e'],index=[1,2,3,4,5])
print(s2)

#传入字典
s3 = pd.Series({'a':1,'b':2,'c':3})
print(s3)


'''DataFrame'''
s4 = pd.DataFrame([['a','b'],['c','d'],['e','f']])
print(s4)

s5 = pd.DataFrame([['a','b'],['c','d'],['e','f']],
    columns = ['frist','last'],             #设置行索引
    index = [1,2,3])                        #设置列索引
print(s5)

'''传入字典方式创建，key相当于列索引'''
s6 = pd.DataFrame({'frist':[2,3,4],'last':[6,7,8]})
print(s6)

print(s6.index)
print(s6.columns)





