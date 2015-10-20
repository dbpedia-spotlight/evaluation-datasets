# evaluation-datasets

Will store links to known evaluation datasets alongside stats to characterize them


# Methodology

* Identify a list of well known evaluation datasets (a.k.a benchmarks). These datasets have text fragments (documents, paragraphs, sentences, etc.) where entity mentions are marked and entity URIs for those mentions are provided.
* Brainstorm and generate a list of aspects to be evaluated on those benchmarks
* Preprocess benchmarks to obtain a common format from the original formats (which may differ greatly from one another).
* Obtain helper datasets with statistics about target knowledge bases and other aspects. These helper datasets will be used to generate statistics about the benchmarks (e.g. benchmarks have only very popular entities)
* Scripts that generate tables/charts with benchmark statistics for any benchmark (number of sentences, number of annotations, pos tags, etc.)
* Scripts that generate tables/charts with target entity statistics (are the entities popular? which types? etc.)
* Scripts that generate tables/charts with mention statistics (are the mentions "easy", which POS? etc.)
* Discussions will be held on Slack: https://nlpdbpedia2015.slack.com/messages/general/
* Issues will be tracked on GitHub: https://github.com/dbpedia-spotlight/evaluation-datasets/issues

# Benchmark Common Format

We will translate all benchmarks to a (simple) common format so that every script can read in the same format. Here are current suggestions. We can take this incrementally. Easier formats first, and as we get those done, we add scripts to work on the more complicated formats. TODO: settle on the official format so everyone can get working

* Heiko: entity lists. Example:
```
http://dbpedia.org/resource/Berlin
```
* Pablo: TSV list of pairs (surface form -> entity)
```
Berlin  http://dbpedia.org/resource/Berlin
German capital  http://dbpedia.org/resource/Berlin
Berlin  http://dbpedia.org/resource/Berlin
Paris http://dbpedia.org/resource/Paris
```
* Giuseppe: also add POS tags (could be TSV, but perhaps easier in JSON if we have many fields?)
```
Berlin  NNP http://dbpedia.org/resource/Berlin
German capital  NP  http://dbpedia.org/resource/Berlin
Berlin  NNP http://dbpedia.org/resource/Berlin
Paris NNP http://dbpedia.org/resource/Paris
```
or:
```json
[
  {
    "uri": "http://dbpedia.org/resource/Berlin",
    "pos_tag": "NNP",
    "surface_form": "Berlin"
  },
  {
    "uri": "http://dbpedia.org/resource/Berlin",
    "pos_tag": "NNP",
    "surface_form": "German capital"
  }
  ...
]
```

(Bash+jq) Command line to convert from JSON to CSV:

TSV
```
cat data.json | jq -r '.[] | "\(.surface_form)\t\(.pos_tag)\t\(.uri)"' 
```

CSV:
```
cat data.json | jq -c -r '.[] | [.surface_form, .uri] | @csv '
```

## NIF to TSV

The script uses Python 2.7.10 (or 3.4.3) with RDFlib 4.2.1.

Usage to print the TSV result on stdout:

```
python nif2tsv.py -i <nif_file>
```

Usage to print the TSV result in a file:

```
python nif2tsv.py -i <nif_file> -o <output_file>
```

## NIF to JSON

The script uses Python 2.7.10 (or 3.4.3) with RDFlib 4.2.1.

Usage to print the JSON result on stdout:

```
python nif2tsv.py -i <nif_file>
```

Usage to print the JSON result in a file:

```
python nif2tsv.py -i <nif_file> -o <output_file>
```

# Benchmarks

These datasets are the target of our evaluations. We want to learn more about how they behave and what exactly are they evaluating.

See the [original Google Doc we created in the workshop](https://docs.google.com/document/d/1pZH9KihVYLxjEh7wMViMLcigei0C7EQgF4W6-Di0bmU/edit) (currently private; results will later be migrated here). The Doc is being migrated to a Spreadsheet because it's easier to handle in that format and then export to LaTeX and Markdown

* Spreadsheet: https://docs.google.com/spreadsheets/d/19KhVh5OMGJa7bO8sRrmBbBf9pM1e4g2CmvkcCdjcWKY/edit#gid=0
* Original Doc: https://docs.google.com/document/d/1pZH9KihVYLxjEh7wMViMLcigei0C7EQgF4W6-Di0bmU

# Helper datasets

Helper datasets contain helpful stats or other metadata that we will use to characterize the benchmarks

* [URI counts, Sf counts and SfUri counts](https://github.com/dbpedia-spotlight/dbpedia-spotlight/wiki/Raw-data)
* Wikipedia URL to DBpedia URI. ???link???
* Entity types (as mentioned by Julien, Giuseppe)
* [DBpedia Graph Measures](http://s16a.org/node/6)


