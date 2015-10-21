import csv

sf_to_links={}

with open('wikinews.tsv','rb') as tsvin:
	tsvin = csv.reader(tsvin, delimiter='\t')
	for row in tsvin:
		if len(row)==2:
			if row[1]!='Link':
				if row[0] not in sf_to_links:
					sf_to_links[row[0]]={row[1]:1}
				elif row[1] in sf_to_links[row[0]]:
					sf_to_links[row[0]][row[1]]+=1
				else:
                                        sf_to_links[row[0]][row[1]]=1
	print sf_to_links
