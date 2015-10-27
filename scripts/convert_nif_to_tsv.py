#!/usr/bin/python
# -*- coding: utf-8 -*-

from rdflib import Graph
import io
import urllib


g = Graph()
g.parse("rss500.ttl", format="n3")

print len(g)

qres = g.query(
               """SELECT DISTINCT ?surfform ?dblink
                   WHERE {
                   ?a <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#anchorOf> ?surfform .
                   OPTIONAL { ?a <http://www.w3.org/2005/11/its/rdf#taIdentRef> ?dblink . }
                   }""")

    #print("%s\t%s" % (row["surfform"].encode('utf-8'), row["dblink"].encode('utf-8')))
file = io.open("rss500-codecs.tsv", "w")
for row in qres:
    file.write("%s\t%s\n" % (urllib.unquote(row["surfform"]), urllib.unquote(row["dblink"])))
file.close()
