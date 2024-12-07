import pandas as pd
from bs4 import BeautifulSoup
import requests as rq

Book_url = 'https://books.toscrape.com/'

Book_Header = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

Book_resp = rq.get(url=Book_url,headers=Book_Header)

Book_soup = BeautifulSoup(Book_resp.content,'html.parser')


Bookfind = Book_soup.findAll('h3')

Booklist =[]
for Book1 in Bookfind:
    Booklist.append({'Book_name': Book1.text})
name_of_book = pd.DataFrame(Booklist)
name_of_book.to_csv('Book_Names.csv')