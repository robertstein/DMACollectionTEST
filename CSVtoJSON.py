#!/usr/bin/python

import csv
import json

outfile = open('DMACollectionJSON.txt', 'w')
outfile.write('[\n')

count = 0
reader = csv.DictReader(open('DMACollectionTest.csv', 'r')) # read binary
for d in reader:
	print count
	# print json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False)
	outfile.write(json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False))
	outfile.write(",\n")
	count = count + 1

outfile.close();
