from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import config

with TelegramClient(StringSession(), config.App_api_id, config.App_api_hash) as client:
    print(client.session.save())