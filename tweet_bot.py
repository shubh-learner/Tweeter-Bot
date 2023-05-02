from all_clients import Clients
# api ver 2


class TweetHeadlines:
    def __init__(self):
            self.client = Clients.twitter_client()
            
    def post_tweet(self, headline):
            response = self.client.create_tweet(text=headline)
            return response