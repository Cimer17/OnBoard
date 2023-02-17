import bot
from website import app
import threading



if __name__ == '__main__':
    thread_syte = threading.Thread(target=bot.bot.polling, args=('127.0.0.1', 8000, True))
    thread_bot = threading.Thread(target=app.run)
    thread_syte.start()
    thread_bot.start()