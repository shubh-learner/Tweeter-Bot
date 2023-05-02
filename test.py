
from all_clients import Clients
import config
from requests.models import Response

data = Response()
data = data(data={'edit_history_tweet_ids': ['1653304094054920192'], 'id': '1653304094054920192', 'text': 'Please wait a moment while the chatbot responds to your query . . .'}, includes={}, errors=[], meta={})

print (data)