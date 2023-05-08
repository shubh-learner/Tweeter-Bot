import config
import asyncio
from news_bot import NewsApi
import telegram_chatgptbot
from tweet_bot import TweetHeadlines
from telegram_chatgptbot import TelegramChat
import time
import schedule
import random

def main():
    try:
        newsapi = NewsApi()
        tweet_headlines = TweetHeadlines()
        tele_chat = TelegramChat()
        
        random_category = random.choice(config.category)
        random_lan = random.choice(config.language)
        url = config.NewsIO_apikey+'&country='+config.country+'&language='+random_lan+'&category='+random_category
        
        headline = newsapi.fetch_news(url)
        print("Category: "+random_category+ " Headline: " + headline)
        
        if not headline:
            print("Check News API, No headlines returned")
        else:
            tele_chat.send_message(headline=headline)
            time.sleep(15)
            gpt_message = tele_chat.get_message()
            print("\n" + gpt_message)
            response = tweet_headlines.post_tweet(gpt_message) 
            print(response)
    except Exception as e:
        print(f"An error occurred: {e}")


schedule.every(5).hours.do(main)

if __name__ == "__main__":
    while 1:
        schedule.run_pending()
        time.sleep(1800)
