import bot
from website import app
import threading


if __name__ == '__main__':
    thread_syte = threading.Thread(target=app.run)
    thread_syte.start()
    bot.bot.polling()