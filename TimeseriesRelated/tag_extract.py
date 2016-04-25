'''
This script will crawl through the data and extract user tags for all the images and write 
them to a txt file.
'''

import csv
import re
import operator
from collections import defaultdict

tags = {}
tags = defaultdict(int)
with open("samrx") as tsv:
	for line in csv.reader(tsv, dialect="excel-tab"):
		if line[10]!="":
			for val in line[8].split(","):
				tags[val] += 1

sorted_x = sorted(tags.items(), key= operator.itemgetter(1),reverse=True)
a = open('tags.txt','wb')
for key in sorted_x:
	a.write(str(key))
	#a.write("-->")
	#a.write(str(tags.get(key)))
	a.write("\n")
		
		
