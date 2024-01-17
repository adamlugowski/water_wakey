import sqlite3
from datetime import date


def stats():
    with sqlite3.connect('hydration.db') as database:
        cursor = database.cursor()
        today = date.today()
        row = cursor.execute('SELECT COUNT(*) FROM hydrating WHERE date=?', (today, ))
        return row.fetchone()
