import telebot
import configparser


config = configparser.ConfigParser()
config.read("settings.ini")
tokenBot = config["bot"]["bot_token"]

bot = telebot.TeleBot(tokenBot)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')