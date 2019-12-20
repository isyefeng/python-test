import pandas as pd

df = pd.read_csv('data.csv')

print('---------------------------')
print(df)
print('---------------------------')

print('加法运算')
print(df['c1']+df['c2'])
print(df['c1']+4)
print('减乘除同上')
print('---------------------------')

print('比较运算')
print(df['c1'] < df['c2'])
print('---------------------------')

print('count()个数运算 axis默认等于0 是对列的操作，axis=1的时候是对行操作')
print(df.count()) 
print(df['c1'].count())
print(df.count(axis=1))
print('---------------------------')

print('sum()求和运算')
print(df.sum())
print(df['c1'].sum())
print(df.sum(axis=1))
print('---------------------------')

print('mean()求平均')
print(df.mean())
print(df['c1'].mean())
print(df.mean(axis=1))
print('---------------------------')

print('max()求最大值运算')
print(df.max())
print(df['c1'].max())
print(df.max(axis=1))
print('---------------------------')

print('min()求最最小运算')
print(df.min())
print(df['c1'].min())
print(df.min(axis=1))
print('---------------------------')

print('median()求中位数')
print(df.median())
print(df['c1'].median())
print(df.median(axis=1))
print('---------------------------')

print('mode()求众数')
print(df.mode())
print(df['c1'].mode())
print(df.mode(axis=1))
print('---------------------------')

