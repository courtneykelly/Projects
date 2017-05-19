# Taken from: http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
# author: 'Eloff', edited by 'Ooker'

from html.parser import HTMLParser

# strip HTML from collected strings
class MLStripper(HTMLParser):

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)