import sqlite3
from datetime import date
from stats import stats


def add():
    with sqlite3.connect('hydration.db') as database:
        cursor = database.cursor()
        text = 'H20'
        today_date = date.today()
        cursor.execute('INSERT INTO hydrating VALUES (null, ?, ?)', (text, today_date))
        database.commit()
        print('Cheers!')
        for item in stats():
            print('You drunk', item, 'times')
