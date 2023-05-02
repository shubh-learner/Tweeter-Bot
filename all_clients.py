import config
from telethon.sync import TelegramClient
import tweepy

class Clients:
    def __init__(self):
            pass
              
    def telegram_client():
        api_id = config.App_api_id
        api_hash = config.App_api_hash
        phone = config.phone_no
        username = config.chatGpt_username
        teleclient = TelegramClient('session_name', api_id, api_hash)
        return teleclient
        
    def twitter_client():
        tweepyclient = tweepy.Client(consumer_key=config.API_Key, consumer_secret=config.API_Secret,
                        access_token=config.Access_Token,access_token_secret=config.Access_Token_Secret)
        return tweepyclient