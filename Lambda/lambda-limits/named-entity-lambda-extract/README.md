# Named Entity Extraction with Lambda

Attempt to put the [MITIE](https://github.com/mit-nlp/MITIE) named entity extraction tool behind a lambda. I used the [python newspaper](http://newspaper.readthedocs.io/en/latest/) to parse HTML and get the main text of an article. Then used MITIE named entity extraction model to extract the name entities from the text. 

The model file is `~330 MB` so this definitely test the `50 MB` lambda hard limit. The total size of the project zip file (with everything else) was `~480 MB` + `40 MB` for the size of the handler, so `520 MB` total, just barely exceeding the `512 MB` size of the `/tmp` directory. 

For full analysis, see [ANALYSIS REPORT](https://docs.google.com/document/u/2/d/1trBt1KfTCIZb6hCWNGxI6ryVfr7OxqMQXSc_Y549J7s/pub).