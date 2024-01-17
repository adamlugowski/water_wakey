import time
from stats import stats
from add_to_db import add


def main():
    while True:
        time.sleep(60 * 0.1)
        user_response = input('Drink water: ').lower()
        try:
            if user_response == 'ok':
                add()
            elif user_response == 'stop':
                for item in stats():
                    print('You drunk', item, 'times')
                print('Exiting the program. Bye!')
                break
            else:
                raise ValueError("You should type 'ok' to add or 'stop' to end app and get statistics")
        except ValueError as error:
            print(error)
            continue


def db_init(db_cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS hydrating(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value TEXT,
        date DATE CURRENT_DATE 
        )''')
