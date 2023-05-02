import config
import asyncio
from news_bot import NewsApi
import telegram_chatgptbot
from tweet_bot import TweetHeadlines
from telegram_chatgptbot import TelegramChat
import time

def main():
    try:
        newsapi = NewsApi()
        tweet_headlines = TweetHeadlines()
        tele_chat = TelegramChat()
        
        headline = newsapi.fetch_news(config.url)
        print(headline)
        
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

if __name__ == "__main__":
    main()
