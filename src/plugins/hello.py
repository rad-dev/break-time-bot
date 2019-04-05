import re

from slackbot.bot import listen_to
from slackbot.bot import respond_to


@listen_to('hello$', re.IGNORECASE)
def hello(message):
    message.send('World!')


@respond_to('break$')
def break_time(message):
    message.reply('It\'s break time!')

