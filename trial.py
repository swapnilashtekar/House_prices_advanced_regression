#!/usr/bin/python
import os, sys
from collections import defaultdict

filename = "train.csv"
superDict = defaultdict(dict)
headers = dict()
count = 0
for line in open(filename):
	lineList = line.split(",")
	if count == 0:
		cnt = 0
		for name in lineList:
			headers[str(cnt)] = name
			cnt += 1
	else:
		valueCount = 1
		for values in lineList[1:]:

			superDict[str(lineList[0])][headers[str(valueCount)]] = lineList[valueCount]
			valueCount += 1

	count +=1




for keys in sorted (superDict):
	if(superDict[keys]['SaleCondition'] != "Normal"):
		print str(keys) + "\t" + str(superDict[keys]['SaleCondition'])


