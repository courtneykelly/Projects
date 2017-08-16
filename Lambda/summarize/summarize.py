#! /usr/bin/env python 

from flask import Flask, jsonify, request
from newspaper import Article
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# Variables
app = Flask(__name__)
LANGUAGE = "english"
SENTENCES_COUNT = 5

# Routes
@app.route('/', methods=['GET', 'PUT'])
def index():
    data = {}

    if request.method == 'GET':
        data['message'] = 'submit PUT request with json containing \'url\' and \'sentence count\' object, default is 5'
    
    elif request.method == 'PUT': 
        try:
            URL = request.form['url']
        except:
            data['message'] = 'submit PUT request with json containing \'url\' and \'sentence count\' objects'
            data['error'] = 'missing url'
            return jsonify(data), 404

        try:
            article = Article(URL)
            article.download()
            article.parse()
            data = {'title' : article.title , 'authors' : article.authors}

        except:
            data = {'error': 'failed to download example URL'}   

        try:
            SENTENCES_COUNT = int(request.form['sentence count'])
        except:
            pass

        try:
            parser = HtmlParser.from_url(URL, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)
            summarizer = Summarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            # extract 
            sum_string = ""
            for sentence in summarizer(parser.document, SENTENCES_COUNT):
                sum_string = sum_string + str(sentence) + ' '
           
            # return as json
            data["summary"] = sum_string
        except:
            data = {'error': 'failed to summarize URL'}
           
    
    return jsonify(data), 200

if __name__ == '__main__':
    app.run()