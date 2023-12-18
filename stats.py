import sqlite3


def stats():
    with sqlite3.connect('hydration.db') as database:
        cursor = database.cursor()
        return cursor.execute('SELECT COUNT(*) FROM hydrating')

