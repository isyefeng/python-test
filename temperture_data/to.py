'''hex to str'''
from matplotlib import pyplot as plt
from datetime import datetime
import csv

filename = '1.txt'
datafile = '2.txt'
csvfile = '3.csv'

def HextoString( file ):
	f = open(datafile, 'w')
	Hex_data = []
	with open(file) as file_t:
		lines = file_t.readlines()
		
	for line in lines[1:-50]:
		f.write(line[9:-3])
	f.write('\n')
	f.close()
	
	with open(datafile) as file_t:
		tempdata = file_t.read()
	
	f = open(csvfile,'w')
	templen = int(len(tempdata)/2)
	print(templen)
	for num in range(templen):
		f.write(chr(int(str(tempdata[num*2:num*2+2]),16)))
	f.close()
	
HextoString(filename)
