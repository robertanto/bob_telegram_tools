import telegram
import time
import os
import shutil

class TelegramBot():

    def __init__(self, token, user_ids, tmp_dir='./temp/'):
        self.bot = telegram.Bot(token)
        self.user_ids = user_ids
        self.tmp_dir = tmp_dir

    def send_text(self, text):
        return self.bot.send_message(self.user_ids, text)

    def update_text(self, message, text):
        if message.text != text:
            try:
                message.edit_text(text)
            except Exception as e:
                pass

    def send_structured_text(self, fields=[], values=[], units=[]):
        msg_text = ''
        for i in range(len(fields)):
            v = values[i] if not isinstance(
                values[i], float) else round(values[i], 3)
            msg_text += fields[i]+': '+str(v)+units[i]+'\n'

        return self.send_text(msg_text)

    def update_structured_text(self, message, fields=[], values=[], units=[]):
        msg_text = ''
        for i in range(len(fields)):
            v = values[i] if not isinstance(
                values[i], float) else round(values[i], 2)
            msg_text += fields[i]+': '+str(v)+units[i]+'\n'

        return self.update_text(message, msg_text)

    def send_plot(self, plt, name=None):
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)

        if name is None:
            ts = int(time.time())
            img_path = self.tmp_dir+str(ts)+'.png'
        else:
            img_path = self.tmp_dir+name

        plt.savefig(img_path, dpi=100)
        return self.bot.send_photo(self.user_ids, open(img_path, 'rb'))

    def send_image(self, img_path):
        return self.bot.send_photo(self.user_ids, open(img_path, 'rb'))

    def update_plot(self, message, plt, name=None):
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)

        if name is None:
            ts = int(time.time())
            img_path = self.tmp_dir+str(ts)+'.png'
        else:
            img_path = self.tmp_dir+name

        plt.savefig(img_path, dpi=100)
        new_media = telegram.InputMediaPhoto(open(img_path, 'rb'))
        try:
            message.edit_media(new_media)
        except Exception as e:
            pass

    def clean_tmp_dir(self):
        shutil.rmtree(self.tmp_dir)