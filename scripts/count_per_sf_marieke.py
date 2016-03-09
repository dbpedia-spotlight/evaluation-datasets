import csv
import sys
import json 

if len(sys.argv)<2:
	print "Please add the TSV file of the dataset as an argument"
	sys.exit(1)

sf_to_links = {} 
with open(sys.argv[1],'rb') as tsvin:
	tsvin = csv.reader(tsvin, delimiter='\t')
	for row in tsvin:
		if len(row)==2:
			if row[1]!='Link':
				if row[0] not in sf_to_links:
					sf_to_links[row[0]] = {row[1]:1}
				elif row[1] in sf_to_links[row[0]]:
					sf_to_links[row[0]][row[1]]+=1
				else:
					sf_to_links[row[0]][row[1]]=1
                    
with open(sys.argv[2], 'w') as outfile:
	json.dump(sf_to_links, outfile)

