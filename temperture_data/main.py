"""程序测试"""
from matplotlib import pyplot as plt
from datetime import datetime
import csv

temperture_file = '3.csv'

with open(temperture_file) as csv_f:
	csv_file = csv.reader(csv_f)
	list = next(csv_file)

x_line = []
y_line = []
cnt = 0	
for num in list:
	cnt = cnt + 1
	x_line.append(cnt)
	y_line.append(float(num))

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(x_line, y_line, c='red')								#alpha:透明度

plt.title('Temperture record',  fontsize = 24)
plt.xlabel('Num', fontsize = 15)
plt.ylabel('Temperture', fontsize = 15)
fig.autofmt_xdate()
plt.show()
	


























