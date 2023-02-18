import bot, time, os
from website import app
import threading


if __name__ == '__main__':
    try:
        os.system("pip install -r requirements.txt")
        thread_syte = threading.Thread(target=app.run)
        thread_syte.start()
        bot.bot.polling()
    except Exception as ex:
        input(ex)
        time.sleep(3)