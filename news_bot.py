import requests
import config
from bs4 import BeautifulSoup
import tweepy
import config
import json
import data_file
# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=IN&'
#        'apiKey='+config.News_API_key)


class NewsApi:
    def __init__(self):
        self.count = 0
        
    def fetch_news(self, url):
        response = requests.get(url)
        data = response.json()
        # data = data_file.jsondata
        headline = ''
        
        for result in data["results"]:
            headline = f"{result['title']} - {result['source_id']} "
            return headline
        
        return headline
    
               

