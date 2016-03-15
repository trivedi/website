import requests
import secret
import xml.etree.ElementTree as ET
from random import choice

def get_books(shelf, n=4):
    '''Get last @n books from @shelf'''
    books = []
    # https://www.goodreads.com/api/index#reviews.list
    r=requests.get('https://www.goodreads.com/review/list.xml', params={'key':secret.key, 'id':secret.id, 'v':'2', 'shelf':shelf})

    xml = r.text
    print xml
    root = ET.fromstring(xml.encode('utf-8'))
    # (title, isbn-10) -> ('Infinite Jest', '0316066524')
    return [(book.find('title').text, book.find('isbn').text) for book in root.iter('book')][:n]
   


def get_quote():
	quotes = ['"Think? Why think! We have computers to do that for us." - Jean Rostand', 
				'"Dear Sir: Regarding your article \'What\'s Wrong with the World?\' I am. Yours truly," - G.K. Chesterton']
	return choice(quotes)

print get_books('currently-reading')
#print get_books('read')
