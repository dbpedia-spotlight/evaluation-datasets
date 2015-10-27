import rdflib
import argparse
import sys
import os
import codecs

def file_choices(fname):
    ext = os.path.splitext(fname)[1][1:]
    if ext != 'tsv':
       parser.error("the output file '{}' doesn't end with 'tsv' extension".format(fname))
    return fname

def nif2tsv():
	parser = argparse.ArgumentParser(prog='nif2tsv.py', description='Translate a NIF dataset into a list of "mention	link" TSV representation. If no output file is given print the result on stdout by default.', version='1.0')
	parser.add_argument('-i', '--input', type=argparse.FileType('r', 0), help='NIF input file', required=True)
	parser.add_argument('-o', '--output', type=lambda s:file_choices(s), help='TSV output file')
	args = parser.parse_args()
	g = rdflib.graph.Graph()
	g.parse(args.input, format=rdflib.util.guess_format(args.input.name))
	qres = g.query(
	    """
	    PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
	    PREFIX itsrdf: <http://www.w3.org/2005/11/its/rdf#>
	    PREFIX owl: <http://www.w3.org/2002/07/owl#>

	    SELECT DISTINCT ?sf ?entity WHERE {
	        ?s nif:anchorOf ?sf .
	        ?s itsrdf:taIdentRef ?ref .
	        OPTIONAL {
	            ?ref owl:sameAs ?link .
	        }
	        BIND(COALESCE(?link, "NIL") AS ?entity) .
	    }
	    """
	)
	    
	if args.output == None:
		for row in qres.result:
			print("%s	%s" % row)
	else:
		file = codecs.open(args.output, "w", "utf-8")
		for row in qres.result:
			file.write("%s	%s\n" % row)
		file.close()

if __name__ == '__main__':
    nif2tsv()