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

# Benchmark Common Format

We will translate all benchmarks to a (simple) common format so that every script can read in the same format. Here are current suggestions. TODO: settle on the official format so everyone can get working
* Heiko: entity lists
* Pablo: TSV list of pairs (surface form -> entity)

# Benchmarks

These datasets are the target of our evaluations. We want to learn more about how they behave and what exactly are they evaluating.

See the Google Doc (currently private, later will be migrated here).

* https://docs.google.com/document/d/1pZH9KihVYLxjEh7wMViMLcigei0C7EQgF4W6-Di0bmU/edit

# Helper datasets

Helper datasets contain helpful stats or other metadata that we will use to characterize the benchmarks

* URI counts, Sf counts and SfUri counts. [link](https://github.com/dbpedia-spotlight/dbpedia-spotlight/wiki/Raw-data)
* Wikipedia URL to DBpedia URI. ???link???
