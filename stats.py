import sqlite3


def stats():
    with sqlite3.connect('hydration.db') as database:
        cursor = database.cursor()
        # kod zwraca obiekt <sqlite3.Cursor object at 0x000001B00C5CBDC0>
        return cursor.execute('SELECT COUNT(*) FROM hydrating')

