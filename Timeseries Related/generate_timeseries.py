import csv
import re
import pickle
from datetime import datetime
from collections import defaultdict

dd = pickle.load(open('temp1.txt', 'rb'))

final_dict = defaultdict(int)

for date in dd:
	#print date.year
	#print date.month
	final_dict[(date.year,date.month)]+=1


years = range(2000,2015)
dump_list = []

for year in years:
	for i in range(1,13):
		dump_list.append(final_dict.get((year,i),0))

print dump_list
print len(dump_list)

ff = open('date.csv','wb')
wr = csv.writer(ff, quoting=csv.QUOTE_ALL)
wr.writerow(dump_list)