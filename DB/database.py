import sqlite3


class Database():
    
    def __init__(self):
        self.conn = sqlite3.connect('HR.db', check_same_thread=False)
        self.cursor = self.conn.cursor()