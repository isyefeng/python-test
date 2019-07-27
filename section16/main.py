#!/usr/bin/env python3
#****************************************************************************************************#
# time:2019.7.13
#test tipoc
#****************************************************************************************************#
"""程序测试"""
from matplotlib import pyplot as plt
from datetime import datetime
import csv

#file_neme = 'sitka_weather_07-2014.csv'
#file_neme = 'sitka_weather_2014.csv'
file_neme = 'death_valley_2014.csv'
sitka = 'sitka_weather_2014.csv'

dates,highs,low = [],[],[]

with open(file_neme) as csv_f:
	csv_file = csv.reader(csv_f)
	list = next(csv_file)
	
	for row in csv_file:
		try:
			high_date = int(row[1])
			low_date = int(row[3])
			time_date = datetime.strptime(row[0], '%Y-%m-%d')
		except ValueError:
			print('miss ' + str(datetime.strptime(row[0], '%Y-%m-%d')) + ' dates')
		else:
			highs.append(high_date)
			low.append(low_date)
			dates.append(time_date)
			
dates1,highs1,low1 = [],[],[]

with open(sitka) as csv_f:
	csv1_file = csv.reader(csv_f)
	list = next(csv1_file)
	
	for row in csv1_file:
		try:
			high_date = int(row[1])
			low_date = int(row[3])
			time_date = datetime.strptime(row[0], '%Y-%m-%d')
		except ValueError:
			print('miss ' + str(datetime.strptime(row[0], '%Y-%m-%d')) + ' dates')
		else:
			highs1.append(high_date)
			low1.append(low_date)
			dates1.append(time_date)
		
		
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)								#alpha:透明度
plt.plot(dates1, highs1, c='blue', alpha=0.5)								#alpha:透明度

#plt.plot(dates, low, c='blue', alpha=0.5)
#plt.fill_between(dates, highs, low, alpha=0.3, facecolor='yellow')		#填充两个值之间的区间颜色
plt.title('Max and Mini Temperture',  fontsize = 24)
plt.xlabel('Time', fontsize = 15)
plt.ylabel('Max Temperture', fontsize = 15)
fig.autofmt_xdate()
plt.show()
	



























