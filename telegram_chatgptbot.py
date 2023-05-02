
from all_clients import Clients
import config

class TelegramChat:
    def __init__(self):
        self.client = Clients.telegram_client()
        self.count = 0
    
    def send_message(self, headline):
        para_headline = config.paraphrase_tweet + headline
        with self.client:
            self.client.send_message(config.chatGpt_username, para_headline)

    def get_message(self):      
        with self.client:
            for message in self.client.iter_messages(config.chatGpt_username):
                if self.count == 0:
                    self.count += 1
                    return(message.text)               
                else:
                    break

