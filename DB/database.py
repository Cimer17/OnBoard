import sqlite3


class Database():
    
    def __init__(self):
        self.conn = sqlite3.connect('DB/HR.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def check_human(self, id): # проверка на наличие доступа
        self.cursor.execute(f'SELECT name FROM users')
        return self.cursor.fetchone()

if __name__ == '__main__':
    pass