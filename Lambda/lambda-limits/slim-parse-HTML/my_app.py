from flask import Flask, jsonify
from newspaper import Article

app = Flask(__name__)

@app.route('/')
def index():
	URL = "https://www.nytimes.com/2017/06/12/us/politics/right-and-left-partisan-writing-you-shouldnt-miss.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=b-lede-package-region&region=top-news&WT.nav=top-news"

	article = Article(URL)
	article.download()
	article.parse()
	data = {'title' : article.title, 'authors' : [x for x in article.authors],'image': article.top_image}

	return jsonify(data), 200

# We only need this for local development.
if __name__ == '__main__':
    app.run()