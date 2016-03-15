import requests
import secret
import xml.etree.ElementTree as ET

def get_books(shelf, n=4):
    '''Get last @n books from @shelf'''
    books = []
    # https://www.goodreads.com/api/index#reviews.list
    r=requests.get('https://www.goodreads.com/review/list.xml', params={'key':secret.key, 'id':secret.id, 'v':'2', 'shelf':shelf})

    xml = r.text
    root = ET.fromstring(xml.encode('utf-8'))
    return [title.text for book in root.iter('book') for title in book.iter('title')][:n]


#print get_books('currently-reading')
#print get_books('read')