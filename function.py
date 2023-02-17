import cv2
import pytesseract
import numpy as np
from pyzbar.pyzbar import decode


def read_qr_code(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    else:
        return None


def get_calendar(month, number):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = cv2.imread(f'content/calendar/{month}.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.addWeighted(gray, 1.5, gray, -0.5, 0)
    text = pytesseract.image_to_string(gray, config='--psm 6')
    if number in text:
        print(f"Число {number} найдено на изображении!")
    else:
        print(f"Число {number} не найдено на изображении.")


if __name__ == '__main__':
    get_calendar('February', '2')