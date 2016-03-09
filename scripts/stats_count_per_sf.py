#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script takes the json counts per surface forms file as input and computes 
# the average number of meanings per surface form, the min and max number and 
# the standard deviation
#
# created by: marieke.van.erp@vu.nl
# 9 March 2016

import sys
import json
import pprint
import statistics 


# sys.argv[1] is the json file with the counts per surface form 
with open(sys.argv[1]) as data_file:    
    data = json.load(data_file)

total = 0 
number_of_resources = {}
for item in data:
#	print item, len(data[item])
	total=+1 
	if len(data[item]) in number_of_resources:
		number_of_resources[len(data[item])] = number_of_resources[len(data[item])] + 1 
	else:
		number_of_resources[len(data[item])] = 1 

meanings = 0
forms = 0
data = []
for i in number_of_resources:
	print i, number_of_resources[i]
	#meanings = meanings + (int(i) * int(number_of_resources[i]))
	#forms = forms + int(number_of_resources[i])
	for x in range (0, int(number_of_resources[i])):
		#print x, int(number_of_resources[i])
		data.append(int(i))
		 
#print data 
print "mean: ", "%.2f" % statistics.mean(data)
print  "stdev: ", "%.2f" % statistics.stdev(data)  	