import sqlite3
from app import main, db_init


if __name__ == "__main__":
    print('This simple app keep your body hydrated!')
    with sqlite3.connect('watering.db') as init_database:
        cursor = init_database.cursor()
        db_init(cursor)
        main()
