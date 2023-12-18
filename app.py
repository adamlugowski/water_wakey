import time
import sqlite3
from datetime import date


def main():
    while True:
        time.sleep(60 * 0.5)
        user_response = input('Drink water: ').lower()
        if user_response == 'ok':
            with sqlite3.connect('watering.db') as database:
                cursor = database.cursor()
                text = 'H20'
                today_date = date.today()
                cursor.execute('INSERT INTO watering VALUES (null, ?, ?)', (text, today_date))
                database.commit()
                print('Zdrowie!')
        elif user_response != 'Stop':
            print("Exiting the program.")
            break


def db_init(db_cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS watering(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value TEXT,
        date DATE 
        )''')