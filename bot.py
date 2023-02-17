import telebot
import configparser
import DB.database
import re
import content.TG as tg
from telebot import types
import function
import os
import random


config = configparser.ConfigParser()
config.read("settings.ini")
tokenBot = config["bot"]["bot_token"]


db = DB.database.Database()
bot = telebot.TeleBot(tokenBot)


id_support = '-666276498'  # тут автоматический чат с главным и поддержкой


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
        bot.send_message(message.chat.id, f'Привет, {name[0]}!\n{tg.welcome_message}',
            reply_markup=keyboards_create(tg.welcome_keyboard))
    else:
        bot.send_message(message.chat.id, 'Нет доступа❗')


@bot.message_handler(func = lambda m : m.text == '✔️Мои достижения')
def my_achievements(message):
    id = str(message.chat.id)
    ac = DB.database.Achievements()
    rows = ac.received(id)
    ac.close()
    text = ""
    for row in rows:
        if id in row[2]:
            text += f'✅ {row[1]} - {row[3]}' + "\n"
        else:
            text += f'❌ {row[1]} - {row[3]}' + "\n"
    bot.send_message(int(id), text)
            

@bot.message_handler(func = lambda m : m.text == '📅Календарь событий')
def сalendar(message):
    kl = DB.database.Callendar()
    event = kl.get_date()
    kl.close()
    btn = ['Меню']
    for i in event:
        btn.append(str(i[0]))
    msg = bot.send_message(message.chat.id, 'Держи календарь на текущий месяц!\nВыбери день, \
чтобы узнать подробнее о событии:', reply_markup=keyboards_create(btn))
    bot.register_next_step_handler(msg, calendarday, btn, event)


def calendarday(message, btn, event):
    if message.text == 'Меню':
        start(message)
    elif str(message.text) in btn:
        subscribe = types.InlineKeyboardButton("🔔Подписаться на событие", callback_data="subscribeivent")
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(subscribe)
        bot.send_message(message.chat.id, f'Событие - {event[0][1]} \n📌{event[0][2]}', reply_markup=keyboard)
        start(message)
    else:
        bot.send_message(message.chat.id, f'Событий на эту дату нет!', reply_markup=types.ReplyKeyboardRemove())
        start(message)

@bot.message_handler(func = lambda m : m.text == '📂Навигатор')
def navigator(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text='Полезные материалы', callback_data='Usefulmaterials'),
           types.InlineKeyboardButton(text='Телефонный справочник', callback_data='phonebook'),
           types.InlineKeyboardButton(text='Меню', callback_data='menu'),)
    bot.send_message(message.chat.id, 'Навигатор:', reply_markup=markup)


@bot.message_handler(func = lambda m : m.text == '👤Задать вопрос')
def askQuestion(message):
    msg = bot.send_message(message.chat.id, 'Не стесняйся задать вопрос, ответим в билжэайщее время!\n\
Введи свой вопрос:')
    bot.register_next_step_handler(msg, send_Question)


def send_Question(message):
    # подбираем данные
    people = DB.database.People()
    id = message.from_user.id
    name = people.check('name', id)[0]
    subdivision = people.check('subdivision', id)[0]
    department = people.check('department', id)[0]
    people.close()
    # формируем тикет
    tiket = DB.database.Ticket()
    idtiket = tiket.new_tikket(message.text, message.from_user.id)
    tiket.close()
    # отправляем
    ok = types.InlineKeyboardButton("🟥Взять в обработку", callback_data="takeTicket")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(ok)
    bot.send_message(id_support, f'Обращение от: {name} \nПодразделение: {subdivision}\nОтдел :{department}\nНомер:{idtiket}\nВопрос: {message.text}',
    reply_markup=keyboard)
    bot.send_message(message.chat.id, 'Ваше обращение отправлено, дождитесь ответа!')

""" доработать """
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    data = call.data
    
    if data == 'takeTicket':
        new_markup = types.InlineKeyboardMarkup()
        new_button = types.InlineKeyboardButton(text='✅Взято на обработку', callback_data='takeTicket')
        new_markup.add(new_button)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_markup)
    
    elif data == 'Usefulmaterials':
        button = types.InlineKeyboardButton(text="Открыть ссылку", url="https://www.example.com")
        Usefulmaterials = types.InlineKeyboardMarkup()
        Usefulmaterials.add(button)
        bot.send_message(call.message.chat_id, "Нажмите кнопку, чтобы открыть ссылку", reply_markup=Usefulmaterials)
    
    # дописать подписку
    elif data == 'subscribeivent':
        new_markup = types.InlineKeyboardMarkup()
        new_button = types.InlineKeyboardButton(text='🔕 Отписаться', callback_data='unsubscribeivent')
        new_markup.add(new_button)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_markup)

    elif data == 'unsubscribeivent':
        new_markup = types.InlineKeyboardMarkup()
        new_button = types.InlineKeyboardButton(text='🔔 Подписаться на событие', callback_data='subscribeivent')
        new_markup.add(new_button)
        #cl = DB.database.Callendar()
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_markup)
    
    elif data == 'phonebook':
        pass
    
    elif data == 'menu':
        start(call.message)


@bot.message_handler(func=lambda message: message.reply_to_message is not None)
def reply_to_message_handler(message):
    try:
        number = re.search(r"Номер:(\d+)", message.reply_to_message.text).group(1)
        id = message.reply_to_message.chat.id
        bot.send_message(id, f'Ответ принят!')
        tiket = DB.database.Ticket()
        chatid = tiket.get_tikket(number)
        tiket.close()
        bot.send_message(chatid, f'⚠️Вам пришел ответ!\n{message.text}')
    except:
        pass


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    photo = f"img/{photo.file_id}.jpg"
    with open(photo, 'wb') as new_file:
        new_file.write(downloaded_file)
    code = function.read_qr_code(photo)
    if code:
        ac = DB.database.Achievements()
        description = ac.check_code(code)
        if description:
            ac.update_activate(message.from_user.id, code)
            mes = random.choice(['Продолжай в том же духе', 'Всё получится!', 'Молодец!'])
            bot.send_message(message.chat.id, f'Новое достижение! \n{description[0]}\nПоздравляю!\n{mes}')
            ac.close()
            os.remove(photo)
        else:
            bot.send_message(message.chat.id, 'Такого кода не существует!')
            ac.close()
            os.remove(photo)
    else:
        bot.send_message(message.chat.id, 'Код отсуствует на картинке!')
        os.remove(photo)