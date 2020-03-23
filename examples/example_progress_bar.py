from time import sleep

from bob_telegram_tools.utils import TelegramTqdm
from bob_telegram_tools.bot import TelegramBot

token = '<your_token>'
user_id = int('<your_chat_id>')
bot = TelegramBot(token, user_id)

pb = TelegramTqdm(bot)
for i in pb(range(20)):
    sleep(1)