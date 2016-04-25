'''
This script will find the dates for all the images for a given tag and sort. 
These dates are then grouped according to month and year for 15 years and dumped into 
a csv which is then passed to R code for generating time series for each tag.
'''


import pymongo
from pymongo import MongoClient
import re
import pickle
from datetime import datetime
from collections import defaultdict
import csv


client =  MongoClient()
db = client['flickr']

tags = ['beach', 'church', 'mountains', 'sculpture','landscape', 'france', 'lake', 'island', 'temple', 'sunset',
'snow', 'hiking', 'river', 'forest', 'zoo', 'bridge', 'wildlife', 'castle']

image_collection = db['image_dataset_timeseries']

for tag in tags:
	regx = re.compile(tag, re.IGNORECASE)
	cursor = image_collection.find({"field8": regx})

	dates = []
	print cursor.count()

	for hit in cursor:
		print hit['field3']
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

	ff = open(tag+'.csv','wb')
	wr =  csv.writer(ff,quoting = csv.QUOTE_ALL)
	wr.writerow(dump_list)
