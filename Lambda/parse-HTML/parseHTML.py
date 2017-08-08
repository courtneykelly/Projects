from newspaper import Article
import json

def parse(event, context):
	if event:
		URL = event
		try:
		    article = Article(URL)
		    article.download()
		    article.parse()
		    data = {'title' : article.title , 'authors' : article.authors,'text' : article.text,'image': article.top_image}
		except:
			data = {'error': 'failed to download URL'}	    
	else:
		data = {'error': 'missing url'}	    
	return data

