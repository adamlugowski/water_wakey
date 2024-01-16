import time
import sqlite3
from datetime import date
from stats import stats


def main():
    while True:
        time.sleep(60 * 0.1)
        user_response = input('Drink water: ').lower()
        try:
            if user_response == 'ok':
                with sqlite3.connect('hydration.db') as database:
                    cursor = database.cursor()
                    text = 'H20'
                    today_date = date.today()
                    cursor.execute('INSERT INTO hydrating VALUES (null, ?, ?)', (text, today_date))
                    database.commit()
                    print('Cheers!')
                    for item in stats():
                        # kod pokazuje tuple jednoelementową
                        print('You drunk', item, 'times')
            # kod zachowuje się dziwnie przy poniższym kodzie
            elif user_response == 'stop' or 'Stop':
                print('Exiting the program. Bye!')
                # kod nie pokazuje statystyk
                print(stats())
                break
            else:
                raise ValueError("You should type 'ok'")
        except ValueError as error:
            print(error)


def db_init(db_cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS hydrating(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value TEXT,
        date DATE 
        )''')
