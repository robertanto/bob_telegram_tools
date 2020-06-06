# Send a plot

The **TelegramBot** provides a simple to send matplotlib plots.

## Example

### Screenshot

<p style="text-align:center;">
<img style="" src="bot.png" width=300>
</p>

### Code
```python

from bob_telegram_tools.bot import TelegramBot
import matplotlib.pyplot as plt


token = '<your_token>'
user_id = int('<your_chat_id>')
bot = TelegramBot(token, user_id)

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')

bot.send_plot(plt)

# This method delete the generetad image
bot.clean_tmp_dir()

```