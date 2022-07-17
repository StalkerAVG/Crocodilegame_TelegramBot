#import random
#import codecs
import requests
from bs4 import BeautifulSoup

import config

def get_new_word(chat_id):
    """you can use that varient if you have a document with words"""
    # num = random.randint(0,1121)
    # with codecs.open('words.txt', encoding='utf-8') as f:
    #     word = f.readlines()[num]
    #     f.close()

    """this part of code gets a random word from the online ukrainian dictionary"""
    url = 'http://sum.in.ua/random'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    word = soup.find('div', id="tlum").find('strong').getText()
    config.server[chat_id][1] = word
