import pymongo
from pymongo import MongoClient
import re
import pickle
from datetime import datetime
from collections import defaultdict
import csv

client =  MongoClient()
db = client['flickr']

image_collection = db['image_dataset_timeseries']

regx = re.compile("france", re.IGNORECASE)



cursor = image_collection.find({"field8": regx})

dates = []
print cursor.count()

for hit in cursor:
	print hit['field3']
	#if 
	if ('null' not in hit['field3']) :
		dates.append(datetime.strptime(hit['field3'], '%Y-%m-%d %H:%M:%S.%f'))


dates.sort()

pickle.dump(dates, open('temp1.txt', 'wb'))

dd = pickle.load(open('temp1.txt', 'rb'))

final_dict = defaultdict(int)

for date in dd:
	final_dict[(date.year,date.month)]+=1


years = range(2000,2015)
dump_list = []

for year in years:
	for i in range(1,13):
		dump_list.append(final_dict.get((year,i),0))

ff = open('date.csv','wb')
wr =  csv.writer(ff,quoting = csv.QUOTE_ALL)
wr.writerow(dump_list)
