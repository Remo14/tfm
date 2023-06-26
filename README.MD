### TFM CODE - REMO GARCIA PELLICER ###

The following scripts utilise data extracted from the KinDiv database (Khishigsuren et al., 2022) and from a variety of queries from different corpora using (see the file corpus_queries2.xls). To replicate the analysis of the data, run the scripts in the following order:

    1)  score_complexity.py - calculates the complexity of all languages based on the database of words (language_ordered_kin_words.tsv)
    2)  language_concepts.py - lists the concepts of every language.
    3)  score_costs.py - calculates the communicative costs of all concepts in all languages.
    4)  language_totals.py - calculates the communicative costs of all languages by adding the costs of their concepts.

The following script plots the results:

    1)  language_scores.R - plots results for complexity and communicative cost values of all languages (Figure 2). Also plots need probabilities by communicative cost of the languages divided by subdomain (Figure 3).


### DEPENDENCIES ###

The packages needed to run the scripts are the following:

    a)  pandas
    b)  math
    c)  re