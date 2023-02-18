import cv2
import numpy as np
from pyzbar.pyzbar import decode
import makevcard

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

if __name__ == '__main__':
    get_calendar('February', '2')