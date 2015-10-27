#!/usr/bin/env python

# This script reads the AIDA-Yago2 dataset and only outputs the surface form and the link 

# Date: 22 October 2015
# Author: Marieke van Erp  
# Contact: marieke.van.erp@vu.nl

import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1])]  # Specify the location of the AIDA-YAGO2 dataset

previous_entity = ''
for line in lines:
    line = line.rstrip()
    terms = line.split('\t')
    if len(terms) > 2:
        if terms[3] == '--NME--':
            terms.append("NIL")
        if previous_entity == terms[2]:
            continue
        sys.stdout.write(terms[2] + "\t" + terms[4] + "\n")
        # ugly hack to remove duplicates. This assumes that there are no sequential repetitions of entities
        previous_entity = terms[2]
    

