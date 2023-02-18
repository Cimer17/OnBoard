from PIL import Image, ImageDraw, ImageFont
from docxtpl import DocxTemplate
from pyzbar.pyzbar import decode
import cv2
import numpy as np
import makevcard
import datetime
import DB.database


def draw(id, text):
    image = Image.open('img/cate.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('static/font/ofont.ru_Sriracha.ttf', size=100)
    x, y = 100, 230
    color = (255, 0, 0)
    draw.text((x, y), text, fill=color, font=font)
    image.save(f'{id}.png')


def read_qr_code(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    else:
        return None


def get_calendar(month, number):
   pass

# получение контактов
def get_contact():
    number = '+792091552140 - Отдел кадров\n+79190011976 - Директор \n+79134953224 - Столовая'
    telephone = f'📞Вот полезные номера телефонов:\n' + number
    phonebook = {}
    for line in telephone.split('\n'):
        if line.count(' - ') == 1:
            phone, name = line.split(' - ')
            phonebook[phone] = name
    return {'message' : telephone,
    'phonebook' : phonebook
    }

# загрузка контактов
def load_conatct(contacts, id):
    makevcard.main(contacts, id)

def get_data(id):
    doc = DocxTemplate("references/НДФЛ.docx")
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    people = DB.database.People()
    data = people.check('name', id)
    li = []
    for i in data.split():
        if data.split()[0] == i:
            li.append(i)
        else:
            li.append(i[0])
    fio = '.'.join(li).replace('.', ' ', 1)
    jobtitle = people.check('JOBTITLE', id)
    year = now.year
    date  = f"{current_day}.{current_month}.{current_year} г."
    dict = { 'fio' : fio,
    'jobtitle' : jobtitle,
    'year' : year,
    'date' : date,
    'fiotitle' : fio,
    }
    doc.render(dict)
    doc.save(f"references/save/{id}.docx")