# Telegram Progress Bar

In order to receive a progress bar not strictly related to your keras training you can use the **TelegramTqdm** class by simple reusing the (widely adopted) [tqdm](https://github.com/tqdm/tqdm) interface.

## Example

### Screenshot

<p style="text-align:center;">
<img style="" src="bot.jpg" width=300>
</p>

### Code
```python
from time import sleep

from bob_telegram_tools.utils import TelegramTqdm
from bob_telegram_tools.bot import TelegramBot

token = '<your_token>'
user_id = int('<your_chat_id>')
bot = TelegramBot(token, user_id)

pb = TelegramTqdm(bot)
for i in pb(range(20)):
    sleep(1)
```