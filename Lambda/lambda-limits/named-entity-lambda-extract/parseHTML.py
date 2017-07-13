import sys, os
from newspaper import Article
from mitie import *

def parse(event, context):
    data = event
    URL = "https://www.nytimes.com/2017/06/12/us/politics/right-and-left-partisan-writing-you-shouldnt-miss.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=b-lede-package-region&region=top-news&WT.nav=top-news"

    article = Article(URL)
    article.download()
    article.parse()
    data = {'title' : article.title.encode('utf-8').replace("\xe2\x80\x99", "'"), 'authors' : [x.encode("utf-8").replace("\\xe2\\x80\\x99","'") for x in article.authors],'image': article.top_image.encode("utf-8")}

    # # Named Entity Extraction
    # ner_model.dat is the model file from MITIE library
    ner = named_entity_extractor("ner_model.dat")

    # Load parsed HTML text and convert it into a list of words.
    tokens = tokenize(article.text.encode("utf-8"))
    entities = ner.extract_entities(tokens)
    data['Number of Entities'] = len(entities)
    data['ORGANIZATION'] = []
    data['PERSON'] = []
    data['LOCATION'] = []
    data['MISC'] = []

    # Get entities and score
    for e in entities:
        range = e[0]
        tag = e[1]
        score = e[2]
        score_text = "{:0.3f}".format(score)
        entity_text = " ".join(tokens[i].decode('utf-8') for i in range)
        data[tag].append((entity_text.encode('utf-8').replace("\xe2\x80\x9c", ""), score_text))

    return data
