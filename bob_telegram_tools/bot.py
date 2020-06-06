"""
Package containing the TelegramBot core class. 
"""
import telegram
import time
import os
import shutil
import json
from typing import Union


class InputError(Exception):
    """
    Base class for input exception.        
    """

    def __init__(self, message):
        self.messege = message


class TelegramBot():
    """
    This class allows to send through a Telegram Bot text, images and plots.
    Furthermore the send messages can be updated. 
    """

    def __init__(self, token: str = None, user_ids: Union[int, list] = None, cred_file: Union[str, dict] = None, tmp_dir='./temp/'):
        """
        Constructor

        !!! warning 
            At least one between (token, user_ids) and cred_file has to be passed. 

        Arguments:
            token : Telegram token

            user_ids : Telegram chat id to which send the messages

            cred_file : Path to or the dict containing the token and the user_ids.
                ```json
                {
                    "token": "<your_token>",
                    "user_ids": <user_id>
                }
                ```

            tmp_dir : Folder in which store the temporary images. The folder will be created if not existing.
        """
        if user_ids == cred_file == user_ids:
            raise InputError(
                'At least one between (token, user_ids) and cred_file has to be passed.')

        if cred_file is not None:
            with open(cred_file) as json_file:
                data = json.load(json_file)
                token = data['token']
                user_ids = data['user_ids']

        self.bot = telegram.Bot(token)
        self.user_ids = user_ids
        self.tmp_dir = tmp_dir

    def send_text(self, text: str) ->telegram.Message:
        """
        Send text function. Returns the message obj needed for the update method.

        Arguments:
            text : Text to send

        Returns:
            Message Object 

        """
        return self.bot.send_message(self.user_ids, text)

    def update_text(self, message: telegram.Message, text: str):
        """
        Update text function.

        Arguments:
            message : Message to update

            text : New text to send
        """
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

    def send_plot(self, plt, name: str = None) -> telegram.Message:
        """
        Send plot function. Returns the message obj needed for the update method.

        Arguments:
            plt : Plot to send

            name : Name of the temporary file

        Returns:
            Message Object 

        """
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)

        if name is None:
            ts = int(time.time())
            img_path = self.tmp_dir+str(ts)+'.png'
        else:
            img_path = self.tmp_dir+name

        plt.savefig(img_path, dpi=100)
        return self.bot.send_photo(self.user_ids, open(img_path, 'rb'))

    def send_image(self, img_path: str) -> telegram.Message:
        """
        Send plot function. Returns the message obj needed for the update method.

        Arguments:
            img_path : Path of the image file to send

        Returns:
            Message Object 

        """
        return self.bot.send_photo(self.user_ids, open(img_path, 'rb'))

    def update_plot(self, message: telegram.Message, plt, name: str = None):
        """
        Update plot function.

        Arguments:
            message : Message to update

            plt : New plot to send

            name : Name of the temporary file
        """
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
        """
        Delete temporary folder function.
        """
        shutil.rmtree(self.tmp_dir)
