import telebot
import configparser
import DB.database
from telebot import types
from content import TG

config = configparser.ConfigParser()
config.read("settings.ini")
tokenBot = config["bot"]["bot_token"]

db = DB.database.Database()
bot = telebot.TeleBot(tokenBot)


def keyboards_create(ListNameBTN, NumberColumns=2):
    keyboards = types.ReplyKeyboardMarkup(
        row_width=NumberColumns, resize_keyboard=True)
    btn_names = [types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards


@bot.message_handler(commands=['start'])
def start(message):
    name = db.check_human(message.chat.id)
    if name is not None:
        bot.send_message(message.chat.id, f'Привет, {name}!\n' + TG.welcome_message)
    else:
        bot.send_message(message.chat.id, 'Нет допступа!')