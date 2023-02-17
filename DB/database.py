import sqlite3
import random

class Database:
    
    def __init__(self):
        self.conn = sqlite3.connect('DB/HR.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def check_human(self, id): # проверка на наличие доступа
        self.cursor.execute(f'SELECT name FROM users WHERE id={id}')
        return self.cursor.fetchone()
    
    def all_human(self, id):
        self.cursor.execute(f'SELECT name, subdivision, department FROM users WHERE id={id}')
        return self.cursor.fetchone()
    
    def close(self):
        self.conn.close()


class People(Database):
    
    def create(self, id, name, subdivision, JOBTITLE, department):  # регистрируем нового пользователя
        self.conn = sqlite3.connect('DB/HR.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.id = id  
        self.name = name
        self.subdivision = subdivision
        self.JOBTITLE = JOBTITLE
        self.department = department
        self.new = 0
        self.cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, 0);', [id, name, subdivision, JOBTITLE, department])
        self.conn.commit()

    def check(self, param : str, id): # получаем нужный параметр
        self.cursor.execute(f'SELECT {param} FROM users WHERE id={id}')
        return self.cursor.fetchone()[0]


class Ticket:
    
    def __init__(self):
        self.conn = sqlite3.connect('DB/HR.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def new_tikket(self, message_ticket, id):
        self.id_ticket = str(random.randint(100000, 999999)) + ''
        self.cursor.execute('INSERT INTO ticket VALUES (?, ?, ?);', [self.id_ticket, message_ticket, id])
        self.conn.commit()
        return self.id_ticket

    def get_tikket(self, id_ticket):
        self.cursor.execute(f'SELECT id FROM ticket WHERE id_ticket={id_ticket}')
        return self.cursor.fetchone()[0]

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    pass