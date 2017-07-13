import sys, os
from newspaper import Article
parent = os.path.dirname(os.path.realpath(__file__))
print (parent+ '/../MITIE/mitielib')
sys.path.append(parent + '/../MITIE/mitielib')
from mitie import *

def parse():
    URL = "https://www.nytimes.com/2017/06/12/us/politics/right-and-left-partisan-writing-you-shouldnt-miss.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=b-lede-package-region&region=top-news&WT.nav=top-news"

    article = Article(URL)
    article.download()
    article.parse()
    data = {'title' : article.title , 'authors' : article.authors,'text' : article.text,'image': article.top_image}
    return data

# MAIN

data = parse()
# Named Entity Extraction
print("loading NER model...")
ner = named_entity_extractor("../MITIE/MITIE-models/english/ner_model.dat")
# print("\nTags output by this NER model:", ner.get_possible_ner_tags())

# # Load a text file and convert it into a list of words.
# tokens = tokenize(data['text'])
# print("Tokenized input:", tokens)

# entities = ner.extract_entities(tokens)
# print("\nEntities found:", entities)
# print("\nNumber of entities detected:", len(entities))

# # entities is a list of tuples, each containing an xrange that indicates which
# # tokens are part of the entity, the entity tag, and an associate score.  The
# # entities are also listed in the order they appear in the input text file.
# # Here we just print the score, tag, and text for each entity to the screen.
# # The larger the score the more confident MITIE is in its prediction.
# for e in entities:
#     range = e[0]
#     tag = e[1]
#     score = e[2]
#     score_text = "{:0.3f}".format(score)
#     entity_text = " ".join(tokens[i].decode() for i in range)
#     print("   Score: " + score_text + ": " + tag + ": " + entity_text)