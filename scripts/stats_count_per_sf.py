#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script takes the json counts per surface forms file as input and computes 
# the average number of meanings per surface form, the min and max number and 
# the standard deviation
#
# created by: marieke.van.erp@vu.nl
# 9 March 2016

from __future__ import division
import sys
import json
import pprint
import statistics 


# sys.argv[1] is the json file with the counts per surface form 
with open(sys.argv[1]) as data_file:    
    data = json.load(data_file)

total = 0 
number_of_resources = {}
link_combo_frequency = {}
for item in data:
#	print item, len(data[item]), data[item]
	total=+1 
	if len(data[item]) in number_of_resources:
		number_of_resources[len(data[item])] = number_of_resources[len(data[item])] + 1 
	else:
		number_of_resources[len(data[item])] = 1 
	for link in data[item]:
	#	print "link combo", item, link, data[item][link]
		if item in link_combo_frequency:
			if link in link_combo_frequency[item]:
				link_combo_frequency[item][link] = link_combo_frequency[item][link] + int(data[item][link])
			else:
				link_combo_frequency[item][link] = int(data[item][link])
		else:
			link_combo_frequency[item] = {}
			link_combo_frequency[item][link]= int(data[item][link]) 

meanings = 0
forms = 0
confus_data = []
for i in number_of_resources:
	print i, number_of_resources[i]
	#meanings = meanings + (int(i) * int(number_of_resources[i]))
	#forms = forms + int(number_of_resources[i])
	for x in range (0, int(number_of_resources[i])):
		#print x, int(number_of_resources[i])
		confus_data.append(int(i))
		 
#print data 
print "confusability mean: ", "%.2f" % statistics.mean(confus_data)
print  "confusability stdev: ", "%.2f" % statistics.stdev(confus_data)  	

dom_data = [] 
max = 0 
min = 1000  
for x in link_combo_frequency:
	total = 0 
	local_max = 0 
	for y in link_combo_frequency[x]:
	#	print x, y, link_combo_frequency[x][y], len(link_combo_frequency[x])
		total = total + int(link_combo_frequency[x][y])
		if int(link_combo_frequency[x][y]) > max:
			max = int(link_combo_frequency[x][y])
	#		print x, y, link_combo_frequency[x][y], len(link_combo_frequency[x])
	#		print "whoop whoop"
		if int(link_combo_frequency[x][y]) < min:
			min = int(link_combo_frequency[x][y])
		if int(link_combo_frequency[x][y]) > local_max:
			local_max = int(link_combo_frequency[x][y])
	dom_per_sf =  local_max / total
#	print "total, local_max, dom_per_sf", x, y, total, local_max, dom_per_sf
	dom_data.append(dom_per_sf)	
#	print idx, wikilinks_frequency[val]
#	for x in range (0, wikilinks_frequency[val]):
#		dom_data.append(wikilinks_frequency[val]) 



#print dom_data
print "dominance mean: ", "%.2f" % statistics.mean(dom_data)
print  "dominance stdev: ", "%.2f" % statistics.stdev(dom_data)
print "max/min", max, min