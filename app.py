import time
import sqlite3
from datetime import date
from stats import stats


def main():
    while True:
        time.sleep(60 * 0.1)
        user_response = input('Drink water: ').lower()
        if user_response == 'ok':
            with sqlite3.connect('hydration.db') as database:
                cursor = database.cursor()
                text = 'H20'
                today_date = date.today()
                cursor.execute('INSERT INTO hydrating VALUES (null, ?, ?)', (text, today_date))
                database.commit()
                print('Cheers!')
                for item in stats():
                    print('You drunk', item, 'times')
        elif user_response != 'Stop':
            print("Exiting the program.")
            break


def db_init(db_cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS hydrating(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value TEXT,
        date DATE 
        )''')
