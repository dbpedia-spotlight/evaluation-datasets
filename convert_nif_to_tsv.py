#!/usr/bin/python
# -*- coding: utf-8 -*-

from rdflib import Graph

g = Graph()
g.parse("rss500-nif-ner.ttl", format="n3")

print len(g)

qres = g.query(
               """SELECT DISTINCT ?surfform ?dblink
                   WHERE {
                   ?a <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#anchorOf> ?surfform .
                   OPTIONAL { ?a <http://www.w3.org/2005/11/its/rdf#taIdentRef> ?dblink . }
                   }""")

for row in qres:
    print("%s\t%s" % (row["surfform"].encode('utf-8'), row["dblink"].encode('utf-8')))