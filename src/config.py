import configparser
from aiogram.utils.helper import Helper, HelperMode, ListItem
import aiogram.dispatcher.filters.state

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')

token = config.get('tbot', 'token')


class States(Helper):
    mode = HelperMode.snake_case

    STATE_START = ListItem()
    STATE_JUNK = ListItem()
    STATE_SMOKE = ListItem()
    STATE_DRINK = ListItem()
    STATE_STOP = ListItem()


if __name__ == '__main__':
    print(States.all())
