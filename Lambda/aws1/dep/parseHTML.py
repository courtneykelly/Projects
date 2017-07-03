from newspaper import Article

def parse(event, context):
	URL = "https://www.nytimes.com/2017/06/12/us/politics/right-and-left-partisan-writing-you-shouldnt-miss.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=b-lede-package-region&region=top-news&WT.nav=top-news"

	article = Article(URL)
	article.download()
	article.parse()
	json = {'title' : article.title , 'authors' : article.authors,'text' : article.text,'image': article.top_image}
