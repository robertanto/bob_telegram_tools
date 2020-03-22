from datetime import datetime
from tqdm import tqdm


class _TelegramIO():
    def __init__(self, bot, show_last_update=True):
        self.bot = bot
        self.text = self.prev_text = '<< Init tqdm >>'
        self.message = self.bot.send_text(self.text)
        self.show_last_update = show_last_update

    def write(self, s):
        new_text = s.strip().replace('\r', '')
        if len(new_text) != 0:
            self.text = new_text

    def flush(self):
        if self.prev_text != self.text:
            if '%' in self.text:
                self.bot.update_text(self.message, self.text +
                                     '\nLast update: {}'.format(datetime.now()) if self.show_last_update else self.text)
                self.prev_text = self.text


class TelegramTqdm():
    def __init__(self, bot, show_last_update=False):
        self.bot = bot
        self.tg_io = _TelegramIO(self.bot, show_last_update)

    def __call__(self, iterable=None, show_last_update=False,
                 desc=None, total=None, leave=True, ncols=None, mininterval=1.0, maxinterval=10.0,
                 miniters=None, ascii=False, disable=False, unit='it',
                 unit_scale=False, dynamic_ncols=False, smoothing=0.3,
                 bar_format=None, initial=0, position=None, postfix=None,
                 unit_divisor=1000, gui=False, **kwargs):

        params = {
            'desc': desc,
            'total': total,
            'leave': leave,
            'file': self.tg_io,
            'ncols': ncols,
            'mininterval': mininterval,
            'maxinterval': maxinterval,
            'miniters': miniters,
            'ascii': ascii,
            'disable': disable,
            'unit': unit,
            'unit_scale': unit_scale,
            'dynamic_ncols': dynamic_ncols,
            'smoothing': smoothing,
            'bar_format': bar_format,
            'initial': initial,
            'position': position,
            'postfix': postfix,
            'unit_divisor': unit_divisor,
            'gui': gui
        }

        params.update(kwargs)

        if iterable is not None:
            params['iterable'] = iterable
            
        return tqdm(**params)
